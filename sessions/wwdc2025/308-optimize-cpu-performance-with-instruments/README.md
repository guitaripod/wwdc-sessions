---
id: "wwdc2025-308"
event: "wwdc2025"
year: 2025
title: "Optimize CPU performance with Instruments"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/308"
topics: ["AI & Machine Learning", "Graphics & Games", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Optimize CPU performance with Instruments

**Event:** WWDC25 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-308](https://developer.apple.com/videos/play/wwdc2025/308)

Learn how to optimize your app for Apple silicon with two new hardware-assisted tools in Instruments. We’ll start by covering how to profile your app, then dive deeper by showing every single function called with Processor Trace. We’ll also discuss how to use CPU Counters’ modes to analyze your code for CPU bottlenecks.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,178 words)

## Documentation & Resources

- [Performance and metrics](https://developer.apple.com/documentation/Xcode/performance-and-metrics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/performance-and-metrics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/performance-and-metrics.json
- [Analyzing CPU usage with the Processor Trace instrument](https://developer.apple.com/documentation/Xcode/analyzing-cpu-usage-with-processor-trace) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-cpu-usage-with-processor-trace
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-cpu-usage-with-processor-trace.json
- [Apple Silicon CPU Optimization Guide Version 4](https://developer.apple.com/documentation/Apple-Silicon/cpu-optimization-guide) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Apple-Silicon/cpu-optimization-guide
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Apple-Silicon/cpu-optimization-guide.json
- [Tuning your code’s performance for Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Apple-Silicon/tuning-your-code-s-performance-for-apple-silicon.json

## Code Snippets

### Binary search in Collection — [6:37]

```swift
public func binarySearch<E, C>(
    needle: E,
    haystack: C
) -> C.Index where E: Comparable, C: Collection<E> {
    var start = haystack.startIndex
    var length = haystack.count

    while length > 0 {
        let half = length / 2
        let middle = haystack.index(start, offsetBy: half)
        let middleValue = haystack[middle]
        if needle < middleValue {
            length = half
        } else if needle == middleValue {
            return middle
        } else {
            start = haystack.index(after: middle)
            length -= half + 1
        }
    }

    return start
}
```

### Throughput benchmark — [7:49]

```swift
import Testing
import OSLog

let signposter = OSSignposter(
    subsystem: "com.example.apple-samplecode.MyBinarySearch",
    category: .pointsOfInterest
)

func search(
    name: StaticString,
    duration: Duration,
    _ search: () -> Void
) {
    var now = ContinuousClock.now
    var outerIterations = 0

    let interval = signposter.beginInterval(name)
    let start = ContinuousClock.now
    repeat {
        search()
        outerIterations += 1
        now = .now
    } while (start.duration(to: now) < duration)
    let elapsed = start.duration(to: now)
    let seconds = Double(elapsed.components.seconds) +
            Double(elapsed.components.attoseconds) / 1e18
    let throughput = Double(outerIterations) / seconds
    signposter.endInterval(name, interval, "\(throughput) ops/s")
    print("\(name): \(throughput) ops/s")
}

let arraySize = 8 << 20
let arrayCount = arraySize / MemoryLayout<Int>.size
let searchCount = 10_000

struct MyBinarySearchTests {
    let sortedArray: [Int]
    let randomElements: [Int]

    init() {
        let sortedArray: [Int] = (0..<arrayCount).map { _ in
                .random(in: 0..<arrayCount)
        }.sorted()
        self.randomElements = (0..<searchCount).map { _ in
            sortedArray.randomElement()!
        }
        self.sortedArray = sortedArray
    }

    @Test func searchCollection() throws {
        search(name: "Collection", duration: .seconds(1)) {
            for element in randomElements {
                _ = binarySearch(needle: element, haystack: sortedArray)
            }
        }
    }
}
```

### Binary search in Span — [13:46]

```swift
public func binarySearch<E: Comparable>(
    needle: E,
    haystack: Span<E>
) -> Span<E>.Index {
    var start = haystack.indices.startIndex
    var length = haystack.count

    while length > 0 {
        let half = length / 2
        let middle = haystack.indices.index(start, offsetBy: half)
        let middleValue = haystack[middle]
        if needle < middleValue {
            length = half
        } else if needle == middleValue {
            return middle
        } else {
            start = haystack.indices.index(after: middle)
            length -= half + 1
        }
    }

    return start
}
```

### Throughput benchmark for binary search in Span — [15:09]

```swift
extension MyBinarySearchTests {
    @Test func searchSpan() throws {
        let span = sortedArray.span
        search(name: "Span", duration: .seconds(1)) {
            for element in randomElements {
                _ = binarySearch(needle: element, haystack: span)
            }
        }
    }

    @Test func searchSpanForProcessorTrace() throws {
        let span = sortedArray.span
        signposter.withIntervalSignpost("Span") {
            for element in randomElements[0..<10] {
                _ = binarySearch(needle: element, haystack: span)
            }
        }
    }
}
```

### Binary search in Span<Int> — [19:17]

```swift
public func binarySearchInt(
    needle: Int,
    haystack: Span<Int>
) -> Span<Int>.Index {
    var start = haystack.indices.startIndex
    var length = haystack.count

    while length > 0 {
        let half = length / 2
        let middle = haystack.indices.index(start, offsetBy: half)
        let middleValue = haystack[middle]
        if needle < middleValue {
            length = half
        } else if needle == middleValue {
            return middle
        } else {
            start = haystack.indices.index(after: middle)
            length -= half + 1
        }
    }
    return start
}
```

### Throughput benchmark for binary search in Span<Int> — [23:04]

```swift
extension MyBinarySearchTests {
    @Test func searchSpanInt() throws {
        let span = sortedArray.span
        search(name: "Span<Int>", duration: .seconds(1)) {
            for element in randomElements {
                _ = binarySearchInt(needle: element, haystack: span)
            }
        }
    }
}
```

### Branchless binary search — [26:34]

```swift
public func binarySearchBranchless(
    needle: Int,
    haystack: Span<Int>
) -> Span<Int>.Index {
    var start = haystack.indices.startIndex
    var length = haystack.count

    while length > 0 {
        let remainder = length % 2
        length /= 2
        let middle = start &+ length
        let middleValue = haystack[middle]
        if needle > middleValue {
            start = middle &+ remainder
        }
    }

    return start
}
```

### Throughput benchmark for branchless binary search — [27:20]

```swift
extension MyBinarySearchTests {
    @Test func searchBranchless() throws {
        let span = sortedArray.span
        search(name: "Branchless", duration: .seconds(1)) {
            for element in randomElements {
                _ = binarySearchBranchless(needle: element, haystack: span)
            }
        }
    }
}
```

### Eytzinger binary search — [29:27]

```swift
public func binarySearchEytzinger(
    needle: Int,
    haystack: Span<Int>
) -> Span<Int>.Index {
    var start = haystack.indices.startIndex.advanced(by: 1)
    let length = haystack.count

    while start < length {
        let value = haystack[start]
        start *= 2
        if value < needle {
            start += 1
        }
    }

    return start >> ((~start).trailingZeroBitCount + 1)
}
```

### Throughput benchmark for Eytzinger binary search — [30:34]

```swift
struct MyBinarySearchEytzingerTests {
    let eytzingerArray: [Int]
    let randomElements: [Int]

    static func reorderEytzinger(_ input: [Int], array: inout [Int], sourceIndex: Int, resultIndex: Int) -> Int {
        var sourceIndex = sourceIndex
        if resultIndex < array.count {
            sourceIndex = reorderEytzinger(input, array: &array, sourceIndex: sourceIndex, resultIndex: 2 * resultIndex)
            array[resultIndex] = input[sourceIndex]
            sourceIndex = reorderEytzinger(input, array: &array, sourceIndex: sourceIndex + 1, resultIndex: 2 * resultIndex + 1)
        }
        return sourceIndex
    }

    init() {
        let sortedArray: [Int] = (0..<arrayCount).map { _ in
            .random(in: 0..<arrayCount)
        }.sorted()
        var eytzingerArray: [Int] = Array(repeating: 0, count: arrayCount + 1)
        _ = Self.reorderEytzinger(sortedArray, array: &eytzingerArray, sourceIndex: 0, resultIndex: 1)
        self.randomElements = (0..<searchCount).map { _ in
            sortedArray.randomElement()!
        }
        self.eytzingerArray = eytzingerArray
    }

    @Test func searchEytzinger() throws {
        let span = eytzingerArray.span
        search(name: "Eytzinger", duration: .seconds(1)) {
            for element in randomElements {
                _ = binarySearchEytzinger(needle: element, haystack: span)
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/308/4/5c144645-dea8-4f16-97ac-a6dd76cf72d8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/308/4/5c144645-dea8-4f16-97ac-a6dd76cf72d8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/308) — developer.apple.com. Indexed for agent consumption._
