---
id: "wwdc2025-312"
event: "wwdc2025"
year: 2025
title: "Improve memory usage and performance with Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/312"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Improve memory usage and performance with Swift

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-312](https://developer.apple.com/videos/play/wwdc2025/312)

Discover ways to improve the performance and memory management of your Swift code. We’ll explore ways to refine your code – from making high-level algorithmic changes to adopting the new InlineArray and Span types for finer control over memory and allocations.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,890 words)

## Documentation & Resources

- [Swift Binary Parsing](https://github.com/apple/swift-binary-parsing) _guide_
- [Performance and metrics](https://developer.apple.com/documentation/Xcode/performance-and-metrics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/performance-and-metrics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/performance-and-metrics.json
- [The Swift website](https://www.swift.org) _documentation_
- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Corrected Data.readByte() method — [7:01]

```swift
import Foundation

extension Data {
  /// Consume a single byte from the start of this data.
  mutating func readByte() -> UInt8? {
    guard !isEmpty else { return nil }
    return self.popFirst()
  }
}
```

### RGBAPixel.data(channels:) method — [9:56]

```swift
extension RGBAPixel {
  /// Returns the RGB or RGBA values for this pixel, as specified
  /// by the given channels information.
  func data(channels: QOI.Channels) -> some Collection<UInt8> {
    switch channels {
    case .rgb:
      [r, g, b]
    case .rgba:
      [r, g, b, a]
    }
  }
}
```

### Original QOIParser.parseQOI(from:) method — [10:21]

```swift
extension QOIParser {
  /// Parses an image from the given QOI data.
  func parseQOI(from input: inout Data) -> QOI? {
    guard let header = QOI.Header(parsing: &input) else { return nil }

    let pixels = readEncodedPixels(from: &input)
      .flatMap { decodePixels(from: $0) }
      .prefix(header.pixelCount)
      .flatMap { $0.data(channels: header.channels) }

    return QOI(header: header, data: Data(pixels))
  }
}
```

### Revised QOIParser.parseQOI(from:) method — [12:53]

```swift
extension QOIParser {
  /// Parses an image from the given QOI data.
  func parseQOI(from input: inout Data) -> QOI? {
    guard let header = QOI.Header(parsing: &input) else { return nil }

    let totalBytes = header.pixelCount * Int(header.channels.rawValue)
    var pixelData = Data(repeating: 0, count: totalBytes)
    var offset = 0

    while offset < totalBytes {
      guard let nextPixel = parsePixel(from: &input) else { break }

      switch nextPixel {
      case .run(let count):
        for _ in 0..<count {
          state.previousPixel
            .write(to: &pixelData, at: &offset, channels: header.channels)
        }
      default:
        decodeSinglePixel(from: nextPixel)
          .write(to: &pixelData, at: &offset, channels: header.channels)
      }
    }

    return QOI(header: header, data: pixelData)
  }
}
```

### Array behavior — [15:07]

```swift
var array = [1, 2, 3]
array.append(4)
array.removeFirst()
// array == [2, 3, 4]

var copy = array
copy[0] = 10      // copy happens on mutation
// array == [2, 3, 4]
// copy == [10, 3, 4]
```

### InlineArray behavior (part 1) — [19:47]

```swift
var array: InlineArray<3, Int> = [1, 2, 3]
array[0] = 4
// array == [4, 2, 3]

// Can't append or remove elements
array.append(4)
// error: Value of type 'InlineArray<3, Int>' has no member 'append'

// Can only assign to a same-sized inline array
let bigger: InlineArray<6, Int> = array
// error: Cannot assign value of type 'InlineArray<3, Int>' to type 'InlineArray<6, Int>'
```

### InlineArray behavior (part 2) — [20:23]

```swift
var array: InlineArray<3, Int> = [1, 2, 3]
array[0] = 4
// array == [4, 2, 3]

var copy = array    // copy happens on assignment
for i in copy.indices {
    copy[i] += 10
}
// array == [4, 2, 3]
// copy == [14, 12, 13]
```

### processUsingBuffer() function — [23:13]

```swift
// Safe usage of a buffer pointer
func processUsingBuffer(_ array: [Int]) -> Int {
    array.withUnsafeBufferPointer { buffer in
        var result = 0
        for i in 0..<buffer.count {
            result += calculate(using: buffer, at: i)
        }
        return result
    }
}
```

### Dangerous getPointerToBytes() function — [23:34]

```swift
// Dangerous - DO NOT USE!
func getPointerToBytes() -> UnsafePointer<UInt8> {
    let array: [UInt8] = Array(repeating: 0, count: 128)
    // DANGER: The next line escapes a pointer
    let pointer = array.withUnsafeBufferPointer { $0.baseAddress! }
    // DANGER: The next line returns the escaped pointer
    return pointer
}
```

### processUsingSpan() function — [24:46]

```swift
// Safe usage of a span
@available(macOS 16.0, *)
func processUsingSpan(_ array: [Int]) -> Int {
    let intSpan = array.span
    var result = 0
    for i in 0..<intSpan.count {
        result += calculate(using: intSpan, at: i)
    }
    return result
}
```

### getHiddenSpanOfBytes() function (attempt 1) — [25:07]

```swift
@available(macOS 16.0, *)
func getHiddenSpanOfBytes() -> Span<UInt8> { }
// error: Cannot infer lifetime dependence...
```

### getHiddenSpanOfBytes() function (attempt 2) — [25:28]

```swift
@available(macOS 16.0, *)
func getHiddenSpanOfBytes() -> () -> Int {
    let array: [UInt8] = Array(repeating: 0, count: 128)
    let span = array.span
    return { span.count }
}
```

### RawSpan.readByte() method — [26:27]

```swift
@available(macOS 16.0, *)
extension RawSpan {
  mutating func readByte() -> UInt8? {
    guard !isEmpty else { return nil }

    let value = unsafeLoadUnaligned(as: UInt8.self)
    self = self._extracting(droppingFirst: 1)
    return value
  }
}
```

### Final QOIParser.parseQOI(from:) method — [28:02]

```swift
/// Parses an image from the given QOI data.
mutating func parseQOI(from input: inout RawSpan) -> QOI? {
  guard let header = QOI.Header(parsing: &input) else { return nil }

  let totalBytes = header.pixelCount * Int(header.channels.rawValue)

  let pixelData = Data(rawCapacity: totalBytes) { outputSpan in
    while outputSpan.count < totalBytes {
      guard let nextPixel = parsePixel(from: &input) else { break }

      switch nextPixel {
      case .run(let count):
        for _ in 0..<count {
          previousPixel
            .write(to: &outputSpan, channels: header.channels)
        }

      default:
        decodeSinglePixel(from: nextPixel)
          .write(to: &outputSpan, channels: header.channels)

      }
    }
  }

  return QOI(header: header, data: pixelData)
}
```

### RGBAPixel.write(to:channels:) method — [28:31]

```swift
@available(macOS 16.0, *)
extension RGBAPixel {
  /// Writes this pixel's RGB or RGBA data into the given output span.
  @lifetime(&output)
  func write(to output: inout OutputRawSpan, channels: QOI.Channels) {
    output.append(r)
    output.append(g)
    output.append(b)

    if channels == .rgba {
      output.append(a)
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/312/4/ae42066d-6af2-4371-bf68-81a81ddef963/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/312/4/ae42066d-6af2-4371-bf68-81a81ddef963/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/312) — developer.apple.com. Indexed for agent consumption._