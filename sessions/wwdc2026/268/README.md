---
id: "wwdc2026-268"
event: "wwdc2026"
year: 2026
title: "Profile, fix, and verify: Improve app responsiveness with Instruments"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/268"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Profile, fix, and verify: Improve app responsiveness with Instruments

**Event:** WWDC26 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-268](https://developer.apple.com/videos/play/wwdc2026/268)

Tackle app responsiveness issues with a clear workflow. Explore the Swift Concurrency instrument, Time Profiler, and System Trace to pinpoint bottlenecks. Discover how to use top functions and run comparisons to measure your improvements and confirm your fixes. And learn about other enhancements in Instruments which make each iteration of this cycle faster than ever, so you can deliver a smoother user experience in less time.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,825 words)

## Documentation & Resources

- [Analyzing CPU profiles with call tree views](https://developer.apple.com/documentation/Xcode/analyzing-cpu-profiles-with-call-tree-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-cpu-profiles-with-call-tree-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-cpu-profiles-with-call-tree-views.json

## Code Snippets

### Add signpost interval around Lasso Selection — [5:41]

```swift
// Add signpost interval around Lasso Selection

import os.signpost

let signposter = OSSignposter(subsystem: “Demo App", category: .pointsOfInterest)
var lassoIntervalState: OSSignpostIntervalState? = nil

func lassoSelectionUpdated() {
    lassoIntervalState = signposter.beginInterval("Lasso Selection")
    // Update selection in canvas…
}

func lassoSelectionEnded() {
    // Finalize lasso selection...
    signposter.endInterval("Lasso Selection", lassoIntervalState!)
}
```

### Existentials — [12:11]

```swift
// Existentials

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar(_ foo: any Foo) {

}
```

### Concrete Types — [12:39]

```swift
// Concrete types

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar(_ a: TypeA) {

}

func bar(_ b: TypeB) {

}
```

### Concrete Types + Generics — [12:46]

```swift
// Concrete types

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar(_ a: TypeA) {

}

func bar(_ b: TypeB) {

}

// Generics

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar<T: Foo>(_ generic: T) {

}
```

### Concrete Types + Generics + Enums — [12:49]

```swift
// Concrete types

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar(_ a: TypeA) {

}

func bar(_ b: TypeB) {

}

// Generics

protocol Foo { }

struct TypeA: Foo { }
struct TypeB: Foo { }

func bar<T: Foo>(_ generic: T) {

}

// Enums

enum Foo {
    case a(TypeA)
    case b(TypeB)
}

struct TypeA { }
struct TypeB { }

func bar(_ enum: Foo) {

}
```

### Thumbnail Rendering — [18:24]

```swift
// Thumbnail rendering

let drawingData = note.drawingData
let canvasImages = note.decodeCanvas()
thumbnail = await Task(name: "Render Thumbnail") {
    await renderThumbnail(drawingData: drawingData, canvasImages: canvasImages, size: CGSize(width: 300, height: 240))
}.value
```

### Thumbnail Rendering Off Main Actor — [18:29]

```swift
// Thumbnail rendering off Main Actor

let drawingData = note.drawingData
let canvasImages = note.decodeCanvas()
thumbnail = await Task(name: "Render Thumbnail") { @concurrent in
    await renderThumbnail(drawingData: drawingData, canvasImages: canvasImages, size: CGSize(width: 300, height: 240))
}.value
```

### File Saving — [24:12]

```swift
// File saving

let encoder = PropertyListEncoder()
encoder.outputFormat = .binary
guard let data = try? encoder.encode(snapshots) else { return }
let id = signposter.beginInterval("Writing To File")
try? data.write(to: fileURL, options: .atomic)
signposter.endInterval("Writing To File", id)
```

### File Saving off Main thread — [24:25]

```swift
// File saving

Task { @concurrent in
	let encoder = PropertyListEncoder()
	encoder.outputFormat = .binary
	guard let data = try? encoder.encode(snapshots) else { return }
	let id = signposter.beginInterval("Writing To File")
	try? data.write(to: fileURL, options: .atomic)
	signposter.endInterval("Writing To File", id)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/268/4/7d94575d-e65b-4033-811f-199586ac587a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/268/4/7d94575d-e65b-4033-811f-199586ac587a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/268) — developer.apple.com. Indexed for agent consumption._