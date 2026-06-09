---
id: "wwdc2021-10233"
event: "wwdc2021"
year: 2021
title: "Use Accelerate to improve performance and incorporate encrypted archives"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10233"
topics: ["AI & Machine Learning", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Use Accelerate to improve performance and incorporate encrypted archives

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10233](https://developer.apple.com/videos/play/wwdc2021/10233)

The Accelerate framework helps you make large-scale mathematical computations and image calculations that are optimized for high-performance, low-energy consumption. Explore the latest updates to Accelerate and its Basic Neural Network Subroutines library, including additional layers, activation functions, and improved optimizer support. Check out improvements to simd.h that include better support for C++ templates. Discover support for Apple Encrypted Archive, an extension to Apple Archive that combines compression with powerful encryption and a digital signature. And learn how you can keep data your safe and secure without compromising on performance.

**Keywords:** `accelerate`, `apple archive`, `archives`, `bnns`, `encryption`, `numerics`, `performance`, `simd`, `vector`, `vectorization`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,238 words)

## Documentation & Resources

- [Encrypting and Decrypting Directories](https://developer.apple.com/documentation/AppleArchive/encrypting-and-decrypting-directories) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppleArchive/encrypting-and-decrypting-directories
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppleArchive/encrypting-and-decrypting-directories.json
- [Accelerate](https://developer.apple.com/documentation/Accelerate) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accelerate
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accelerate.json

## Code Snippets

### Using Accelerate in C/C++ — [1:55]

```objectivec
// How to use in your own code

// C / Objective C / C++
#include <Accelerate/Accelerate.h> // Add framework Accelerate
#include <AppleArchive/AppleArchive.h> // Add framework AppleArchive
#include <Compression/Compression.h> // Add framework Compression
#include <simd/simd.h> // No framework to add

// Swift
import Accelerate
import AppleArchive
import Compression
import simd
```

### simd example — [4:26]

```swift
import simd

public func swishharder_scalar (_ data: [Float]) -> [Float] {
  return data.map { x in
    if x <= -.pi { return 0 }                         //        {  0                if  x ≤ -π
    if x <=  .pi { return 2*exp(x) * (x + .pi)/2 }    // f(x) = {  2eˣ * (x+π)/2    if -π <  x < π
    else         { return 2*exp(x) }                  //        {  2eˣ              if  π ≤  x
  }
}

func swishharder_elementwise(_ x: SIMD8<Float>) -> SIMD8<Float> {
    let y = 2*simd.exp(x)
    let a = y.replacing(with: 0, where: x .<= -.pi)
    let b = ((x + .pi)/2).replacing(with: 1, where: .pi .<= x)
    return a*b
}

extension SIMD {
    internal func store(
        into buffer: UnsafeMutableBufferPointer<Scalar>,
        startingAt offset: Int
    ) {
        for i in 0 ..< scalarCount {
            buffer[offset + i] = self[i]
        }
    }
}

public func swishharder_simd(_ data: [Float]) -> [Float] {
    return Array<Float>(unsafeUninitializedCapacity: data.count) {
        (buffer: inout UnsafeMutableBufferPointer<Float>, count: inout Int) in
        for i in stride(from: 0, to: data.count, by: 8) {
            let v = SIMD8(data[i ..< i+8])
            let w = swishharder_elementwise(v)
            w.store(into: buffer, startingAt: i)
        }
        count = data.count
    }
}
```

### AEA Encryption — [12:14]

```swift
/// Encrypts and archives the directory at the specified URL.
    ///
    /// - Parameter sourceURL: The URL of the directory that the function encrypts and archives.
    /// - Returns: A string containing the status message.
    ///
    /// This function writes the result to `directory`. The archive shares the name
    /// of the supplied directory with an `aea` extension.
    static func encrypt(sourceURL: URL) -> ConsoleMessage {

        // Verify that the URL path represents a directory.
        if !sourceURL.hasDirectoryPath {
            return ConsoleMessage(status: .error,
                                  message: "The specified URL doesn't point to a directory.")
        }

        guard let source = FilePath(sourceURL) else {
            return ConsoleMessage(status: .error,
                                  message: "Unable to create file path from source URL.")
        }

        // Create the destination `FilePath`.
        let destination = directory
            .appending(sourceURL.lastPathComponent)
            .appending(".aea")
        let archiveDestination = FilePath(destination)

        // Create the encryption context + setup credentials
        let encryptionKey = SymmetricKey(size: .bits256)

        let context = ArchiveEncryptionContext(
            profile: .hkdf_sha256_aesctr_hmac__symmetric__none,
            compressionAlgorithm: .lzfse)
        do {
            try context.setSymmetricKey(encryptionKey)
        } catch {
            return ConsoleMessage(status: .error,
                                  message: "Error setting password (\(error).)")
        }

        // Create the file stream, encryption stream, archive encode stream.
        guard
            let archiveDestinationFileStream = ArchiveByteStream.fileStream(
                path: archiveDestination,
                mode: .writeOnly,
                options: [ .create, .truncate ],
                permissions: FilePermissions(rawValue: 0o644)),

                let encryptionStream = ArchiveByteStream.encryptionStream(
                    writingTo: archiveDestinationFileStream,
                    encryptionContext: context),

                let encoderStream = ArchiveStream.encodeStream(
                    writingTo: encryptionStream) else {

                    return ConsoleMessage(status: .error,
                                          message: "Error creating streams.")
                }

        // Remember to close things in the correct order
        defer {
            try? encoderStream.close()
            try? encryptionStream.close()
            try? archiveDestinationFileStream.close()
        }

        // Encode all files in the target directory with the specifed fields.
        do {

            let fields = ArchiveHeader.FieldKeySet("TYP,PAT,DAT,UID,GID,MOD")!
            try encoderStream.writeDirectoryContents(archiveFrom: source,
                                                     keySet: fields)
        } catch {
            return ConsoleMessage(status: .error,
                                  message: "Error writing directory contents.")
        }

        if let url = URL(archiveDestination) {
            NSWorkspace.shared.activateFileViewerSelecting([url])
        }

        let message = """
Encrypted with key '\(encryptionKey.base64Encoded)'.
Archived and encrypted to: \(archiveDestination.description).
"""

        return ConsoleMessage(status: .encryptionSuccess(base64EncodedKeyData: encryptionKey.base64Encoded),
                              message: message)
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10233/4/72F4F22E-DDAB-4A58-B049-7AC537198EFC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10233/4/72F4F22E-DDAB-4A58-B049-7AC537198EFC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10233) — developer.apple.com. Indexed for agent consumption._
