---
id: "wwdc2020-10170"
event: "wwdc2020"
year: 2020
title: "What's new in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10170"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in Swift

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10170](https://developer.apple.com/videos/play/wwdc2020/10170)

Join us for an update on Swift. Discover the latest advancements in runtime performance, along with improvements to the developer experience that make your code faster to read, edit, and debug. Find out how to take advantage of new language features like multiple trailing closures. Learn about new libraries available in the SDK, and explore the growing number of APIs available as Swift Packages.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,540 words)

## Documentation & Resources

- [Swift Standard Library Preview](https://github.com/apple/swift-standard-library-preview) _documentation_
- [Swift Argument Parser on GitHub](https://github.com/apple/swift-argument-parser) _documentation_
- [Swift Evolution](https://apple.github.io/swift-evolution/) _guide_
- [Swift Numerics on GitHub](https://github.com/apple/swift-numerics) _documentation_
- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Swift on AWS Lambda — [13:32]

```swift
import AWSLambdaRuntime

Lambda.run { (_, event: String, callback) in
    callback(.success("Hello, \(event)"))
}
```

### @main — [21:08]

```swift
// Type-based program entry points

import ArgumentParser

@main
struct Hello: ParsableCommand {
    @Argument(help: "The name to greet.")
    var name: String

    func run() {
        print("Hello, \(name)!")
    }
}
```

### Synthesized comparable conformance for enums — [23:50]

```swift
// Synthesized comparable conformance for enums

enum MessageStatus: Hashable, Comparable {
    case draft
    case saved
    case failedToSend
    case sent
    case delivered
    case read

    var wasSent: Bool {
        self >= .sent
    }
}
```

### Compress and archive a source directory using Apple Archive — [27:19]

```swift
// Apple Archive

import AppleArchive

try ArchiveByteStream.withFileStream(
    path: "/tmp/VacationPhotos.aar",
    mode: .writeOnly,
    options: [.create, .truncate],
    permissions: [.ownerReadWrite, .groupRead, .otherRead]
) { file in
    // Receives raw bytes and writes compressed bytes to `file`
    try ArchiveByteStream.withCompressionStream(using: .lzfse, writingTo: file) { compressor in
        // Receives archive entries, and writes bytes to `compressor`
        try ArchiveStream.withEncodeStream(writingTo: compressor) { encoder in
            // Writes all entries from `src` to `encoder`
            try encoder.writeDirectoryContents(archiveFrom: source, keySet: fieldKeySet)
        }
    }
}
```

### OSLog support for String interpolations and formatting options — [28:34]

```swift
logger.log("\(offerID, align: .left(columns: 10), privacy: .public)")
// Logs "E1Z3F    "

logger.log("\(seconds, format: .fixed(precision: 2)) seconds")
// Logs "1.30 seconds"
```

### ArgumentParser Swift Package — [30:05]

```swift
// Swift ArgumentParser

import ArgumentParser

@main
struct Hello: ParsableCommand {
    @Option(name: .shortAndLong, help: "The number of times to say hello.")
    var count: Int = 1

    @Argument(help: "The name to greet.")
    var name: String

    func run() {
        for _ in 1...count {
            print("Hello, \(name)!")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10170/7/9782B095-447A-49C8-A7D2-BB3B006CA5E2/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10170) — developer.apple.com. Indexed for agent consumption._