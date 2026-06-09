---
id: "wwdc2022-110350"
event: "wwdc2022"
year: 2022
title: "Visualize and optimize Swift concurrency"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110350"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Visualize and optimize Swift concurrency

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110350](https://developer.apple.com/videos/play/wwdc2022/110350)

Learn how you can optimize your app with the Swift Concurrency template in Instruments. We'll discuss common performance issues and show you how to use Instruments to find and resolve these problems. Learn how you can keep your UI responsive, maximize parallel performance, and analyze Swift concurrency activity within your app.

To get the most out of this session, we recommend familiarity with Swift concurrency (including tasks and actors).

**Keywords:** `swift`, `swift concurrency`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,671 words)

## Documentation & Resources

- [Concurrency](https://developer.apple.com/documentation/Swift/concurrency) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/concurrency.json
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### CompressionState class — [10:24]

```swift
@MainActor
class CompressionState: ObservableObject {
    @Published var files: [FileStatus] = []
    var logs: [String] = []

    func update(url: URL, progress: Double) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].progress = progress
        }
    }

    func update(url: URL, uncompressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].uncompressedSize = uncompressedSize
        }
    }

    func update(url: URL, compressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].compressedSize = compressedSize
        }
    }

    func compressAllFiles() {
        for file in files {
            Task {
                let compressedData = compressFile(url: file.url)
                await save(compressedData, to: file.url)
            }
        }
    }

    func compressFile(url: URL) -> Data {
        log(update: "Starting for \(url)")
        let compressedData = CompressionUtils.compressDataInFile(at: url) { uncompressedSize in
            update(url: url, uncompressedSize: uncompressedSize)
        } progressNotification: { progress in
            update(url: url, progress: progress)
            log(update: "Progress for \(url): \(progress)")
        } finalNotificaton: { compressedSize in
            update(url: url, compressedSize: compressedSize)
        }
        log(update: "Ending for \(url)")
        return compressedData
    }

    func log(update: String) {
        logs.append(update)
    }
```

### CompressionState class using ParallelCompressor actor — [11:49]

```swift
actor ParallelCompressor {
    var logs: [String] = []
    unowned let status: CompressionState

    init(status: CompressionState) {
        self.status = status
    }

    func compressFile(url: URL) -> Data {
        log(update: "Starting for \(url)")
        let compressedData = CompressionUtils.compressDataInFile(at: url) { uncompressedSize in
            Task { @MainActor in
                status.update(url: url, uncompressedSize: uncompressedSize)
            }
        } progressNotification: { progress in
            Task { @MainActor in
                status.update(url: url, progress: progress)
                await log(update: "Progress for \(url): \(progress)")
            }
        } finalNotificaton: { compressedSize in
            Task { @MainActor in
                status.update(url: url, compressedSize: compressedSize)
            }
        }
        log(update: "Ending for \(url)")
        return compressedData
    }

    func log(update: String) {
        logs.append(update)
    }
}

@MainActor
class CompressionState: ObservableObject {
    @Published var files: [FileStatus] = []
    var compressor: ParallelCompressor!

    init() {
        self.compressor = ParallelCompressor(status: self)
    }

    func update(url: URL, progress: Double) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].progress = progress
        }
    }

    func update(url: URL, uncompressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].uncompressedSize = uncompressedSize
        }
    }

    func update(url: URL, compressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].compressedSize = compressedSize
        }
    }

    func compressAllFiles() {
        for file in files {
            Task {
                let compressedData = await compressor.compressFile(url: file.url)
                await save(compressedData, to: file.url)
            }
        }
    }
}
```

### CompressionState class using ParallelCompressor with minimal actor-isolation and detached tasks — [17:46]

```swift
actor ParallelCompressor {
    var logs: [String] = []
    unowned let status: CompressionState

    init(status: CompressionState) {
        self.status = status
    }

    nonisolated func compressFile(url: URL) async -> Data {
        await log(update: "Starting for \(url)")
        let compressedData = CompressionUtils.compressDataInFile(at: url) { uncompressedSize in
            Task { @MainActor in
                status.update(url: url, uncompressedSize: uncompressedSize)
            }
        } progressNotification: { progress in
            Task { @MainActor in
                status.update(url: url, progress: progress)
                await log(update: "Progress for \(url): \(progress)")
            }
        } finalNotificaton: { compressedSize in
            Task { @MainActor in
                status.update(url: url, compressedSize: compressedSize)
            }
        }
        await log(update: "Ending for \(url)")
        return compressedData
    }

    func log(update: String) {
        logs.append(update)
    }
}

@MainActor
class CompressionState: ObservableObject {
    @Published var files: [FileStatus] = []
    var compressor: ParallelCompressor!

    init() {
        self.compressor = ParallelCompressor(status: self)
    }

    func update(url: URL, progress: Double) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].progress = progress
        }
    }

    func update(url: URL, uncompressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].uncompressedSize = uncompressedSize
        }
    }

    func update(url: URL, compressedSize: Int) {
        if let loc = files.firstIndex(where: {$0.url == url}) {
            files[loc].compressedSize = compressedSize
        }
    }

    func compressAllFiles() {
        for file in files {
            Task.detached {
                let compressedData = await self.compressor.compressFile(url: file.url)
                await save(compressedData, to: file.url)
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110350/4/3B87EB1E-4E88-4D11-817A-16852AEA794C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110350/4/3B87EB1E-4E88-4D11-817A-16852AEA794C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110350) — developer.apple.com. Indexed for agent consumption._