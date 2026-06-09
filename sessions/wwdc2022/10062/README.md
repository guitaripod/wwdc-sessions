---
id: "wwdc2022-10062"
event: "wwdc2022"
year: 2022
title: "Meet Transferable"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10062"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet Transferable

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10062](https://developer.apple.com/videos/play/wwdc2022/10062)

Meet Transferable: a model-layer protocol that allows for effortless support for sharing, drag and drop, copy/paste, and other features in your app.

We'll explore how you can use the API for common use cases, and take advantage of advanced features to customize the behavior. We'll also share how you can optimize for memory efficiency when dealing with large amounts of data. Whether you're extending your models to share with other applications as strings or images or creating custom declared data types, Transferable can help you facilitate a great experience in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,758 words)

## Documentation & Resources

- [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ShareLink
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ShareLink.json

## Code Snippets

### Declaring a custom content type — [4:36]

```swift
import UniformTypeIdentifiers

// also declare the content type in the Info.plist
extension UTType {
    static var profile: UTType = UTType(exportedAs: "com.example.profile")
}
```

### PasteButton interface — [5:10]

```swift
import SwiftUI

struct Profile {
    private var funFacts: [String] = []
    mutating func addFunFacts(_ newFunFacts: [String]) {
        funFacts.append(newFunFacts)
    }
}

struct PasteButtonView: View {
    @State var profile = Profile()
    var body: some View {
        PasteButton(payloadType: String.self) { funFacts in
            profile.addFunFacts(funFacts)
        }
    }
}
```

### Drag and Drop — [5:19]

```swift
import SwiftUI

struct PortraitView: View {
    @State var portrait: Image
    var body: some View {
        portrait
            .cornerRadius(8)
            .draggable(portrait)
            .dropDestination(payloadType: Image.self) { (images: [Image], _) in
                if let image = images.first {
                    portrait = image
                    return true
                }
                return false
            }
    }
}
```

### Sharing — [5:27]

```swift
import SwiftUI

struct Profile {
    var name: String
}

struct ProfileView: View {
    @State private var portrait: Image
    var model: Profile

    var body: some View {
        VStack {
            portrait
            Text(model.name)
        }
        .toolbar {
            ShareLink(item: portrait, preview: SharePreview(model.name))
        }
    }
}
```

### Profile structure — [6:34]

```swift
import Foundation

struct Profile: Codable {
    var id: UUID
    var name: String
    var bio: String
    var funFacts: [String]
    var video: URL?
    var portrait: URL?
}
```

### CodableRepresentation — [7:31]

```swift
import CoreTransferable
import UniformTypeIdentifiers

struct Profile: Codable {
    var id: UUID
    var name: String
    var bio: String
    var funFacts: [String]
    var video: URL?
    var portrait: URL?
}

extension Profile: Codable, Transferable {
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .profile)
    }
}

// also declare the content type in the Info.plist
extension UTType {
    static var profile: UTType = UTType(exportedAs: "com.example.profile")
}
```

### DataRepresentation — [8:30]

```swift
import CoreTransferable
import UniformTypeIdentifiers

struct ProfilesArchive {
    init(csvData: Data) throws { }
    func convertToCSV() throws -> Data { Data() }
}

extension ProfilesArchive: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(contentType: .commaSeparatedText) { archive in
            try archive.convertToCSV()
        } importing: { data in
            try ProfilesArchive(csvData: data)
        }
    }
}
```

### FileRepresentation — [9:14]

```swift
import CoreTransferable

struct Video: Transferable {
    let file: URL
    static var transferRepresentation: some TransferRepresentation {
        FileRepresentation(contentType: .mpeg4Movie) { 
            SentTransferredFile($0.file)
        } importing: { received in
            let destination = try Self.copyVideoFile(source: received.file)
            return Self.init(file: destination)
        }
    }

    static func copyVideoFile(source: URL) throws -> URL {
        let moviesDirectory = try FileManager.default.url(
            for: .moviesDirectory, in: .userDomainMask,
            appropriateFor: nil, create: true
        )
        var destination = moviesDirectory.appendingPathComponent(
            source.lastPathComponent, isDirectory: false)
        if FileManager.default.fileExists(atPath: destination.path) {
            let pathExtension = destination.pathExtension
            var fileName = destination.deletingPathExtension().lastPathComponent
            fileName += "_\(UUID().uuidString)"
            destination = destination
                .deletingLastPathComponent()
                .appendingPathComponent(fileName)
                .appendingPathExtension(pathExtension)
        }
        try FileManager.default.copyItem(at: source, to: destination)
        return destination
    }
}
```

### ProxyRepresentation — [10:05]

```swift
import CoreTransferable
import UniformTypeIdentifiers

struct Profile: Codable {
    var id: UUID
    var name: String
    var bio: String
    var funFacts: [String]
    var video: URL?
    var portrait: URL?
}

extension Profile: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .profile)
        ProxyRepresentation(exporting: \.name)
    }
}

// also declare the content type in the Info.plist
extension UTType {
    static var profile: UTType = UTType(exportedAs: "com.example.profile")
}
```

### Proxy and file representations — [11:34]

```swift
import CoreTransferable

struct Video: Transferable {
    let file: URL
    static var transferRepresentation: some TransferRepresentation {
        FileRepresentation(contentType: .mpeg4Movie) { SentTransferredFile($0.file) }
           importing: { received in
               let copy = try Self.copyVideoFile(source: received.file)
               return Self.init(file: copy) }
        ProxyRepresentation(exporting: \.file)
  }

    static func copyVideoFile(source: URL) throws -> URL {
        let moviesDirectory = try FileManager.default.url(
            for: .moviesDirectory, in: .userDomainMask,
            appropriateFor: nil, create: true
        )
        var destination = moviesDirectory.appendingPathComponent(
            source.lastPathComponent, isDirectory: false)
        if FileManager.default.fileExists(atPath: destination.path) {
            let pathExtension = destination.pathExtension
            var fileName = destination.deletingPathExtension().lastPathComponent
            fileName += "_\(UUID().uuidString)"
            destination = destination
                .deletingLastPathComponent()
                .appendingPathComponent(fileName)
                .appendingPathExtension(pathExtension)
        }
        try FileManager.default.copyItem(at: source, to: destination)
        return destination
    }
}
```

### Exporting condition — [12:57]

```swift
import CoreTransferable
import UniformTypeIdentifiers

struct ProfilesArchive {
    var supportsCSV: Bool { true }
    init(csvData: Data) throws {  }
    func convertToCSV() throws -> Data { Data() }
}

extension ProfilesArchive: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(contentType: .commaSeparatedText) { archive in
            try archive.convertToCSV()
        } importing: { data in
            try Self(csvData: data)
        }
        .exportingCondition { $0.supportsCSV }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10062/4/004375E4-2295-45FB-9D6D-20F1B8C3834C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10062/4/004375E4-2295-45FB-9D6D-20F1B8C3834C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10062) — developer.apple.com. Indexed for agent consumption._