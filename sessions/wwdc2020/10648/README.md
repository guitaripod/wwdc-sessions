---
id: "wwdc2020-10648"
event: "wwdc2020"
year: 2020
title: "Unsafe Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10648"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Unsafe Swift

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10648](https://developer.apple.com/videos/play/wwdc2020/10648)

What exactly makes code “unsafe”? Join the Swift team as we take a look at the programming language’s safety precautions — and when you might need to reach for unsafe operations. We’ll take a look at APIs that can cause unexpected states if not used correctly, and how you can write code more specifically to avoid undefined behavior. Learn how to work with C APIs that use pointers and the steps to take when you want to use Swift’s unsafe pointer APIs.

To get the most out of this session, you should have some familiarity with Swift and the C programming language. And for more information on working with pointers, check out "Safely Manage Pointers in Swift".

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,590 words)

## Documentation & Resources

- [Manual Memory Management](https://developer.apple.com/documentation/Swift/manual-memory-management) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/manual-memory-management
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/manual-memory-management.json

## Code Snippets

### Optional's force unwrapping operator — [0:52]

```swift
let value: Int? = nil

print(value!) // Fatal error: Unexpectedly found nil while unwrapping an Optional value
```

### Unsafe force-unwrapping — [1:58]

```swift
let value: String? = "Hello"

print(value.unsafelyUnwrapped) // Hello
```

### Invalid use of unsafe force-unwrapping — [2:25]

```swift
let value: String? = nil

print(value.unsafelyUnwrapped) // ?!
```

### Invalid use of unsafe force-unwrapping — [4:23]

```swift
let value: String? = nil

print(value.unsafelyUnwrapped) // Guaranteed fatal error in debug builds
```

### Manual memory management — [7:37]

```swift
let ptr = UnsafeMutablePointer<Int>.allocate(capacity: 1)
ptr.initialize(to: 42)
print(ptr.pointee) // 42
ptr.deallocate()
ptr.pointee = 23 // UNDEFINED BEHAVIOR
```

### Passing an array of integers to a C function (1) — [10:04]

```objectivec
void process_integers(const int *start, size_t count);
```

### Passing an array of integers to a C function (2) — [10:08]

```swift
func process_integers(_ start: UnsafePointer<CInt>!, _ count: Int)
```

### Passing an array of integers to a C function (3) — [10:17]

```swift
let start = UnsafeMutablePointer<CInt>.allocate(capacity: 4)

start.initialize(to: 0)
(start + 1).initialize(to: 2)
(start + 2).initialize(to: 4)
(start + 3).initialize(to: 6)

process_integers(start, 4)

start.deinitialize(count: 4)
start.deallocate()
```

### Unsafe buffer pointer types — [12:33]

```swift
UnsafeBufferPointer<Element>
UnsafeMutableBufferPointer<Element>

UnsafeRawBufferPointer
UnsafeMutableRawBufferPointer
```

### Accessing contiguous collection storage — [13:28]

```swift
Sequence.withContiguousStorageIfAvailable(_:)
MutableCollection.withContiguousMutableStorageIfAvailable(_:)

String.withCString(_:)
String.withUTF8(_:)

Array.withUnsafeBytes(_:)
Array.withUnsafeBufferPointer(_:)
Array.withUnsafeMutableBytes(_:)
Array.withUnsafeMutableBufferPointer(_:)
```

### Temporary pointers to Swift values — [13:39]

```swift
withUnsafePointer(to:_:)
withUnsafeMutablePointer(to:_:)
withUnsafeBytes(of:_:)
withUnsafeMutableBytes(of:_:)
```

### Passing an array of integers to a C function (4) — [13:48]

```swift
let values: [CInt] = [0, 2, 4, 6]

values.withUnsafeBufferPointer { buffer in
  print_integers(buffer.baseAddress!, buffer.count)
}
```

### Passing an array of integers to a C function (5) — [14:25]

```swift
let values: [CInt] = [0, 2, 4, 6]

print_integers(values, values.count)
```

### Advanced C interoperability — [15:36]

```swift
func sysctl(
  _ name: UnsafeMutablePointer<CInt>!,
  _ namelen: CUnsignedInt,
  _ oldp: UnsafeMutableRawPointer!,
  _ oldlenp: UnsafeMutablePointer<Int>!,
  _ newp: UnsafeMutableRawPointer!,
  _ newlen: Int
) -> CInt
```

### Advanced C interoperability — [16:32]

```swift
import Darwin

func cachelineSize() -> Int {
    var query = [CTL_HW, HW_CACHELINE]
    var result: CInt = 0
    var resultSize = MemoryLayout<CInt>.size
    let r = sysctl(&query, CUnsignedInt(query.count), &result, &resultSize, nil, 0)
    precondition(r == 0, "Cannot query cache line size")
    precondition(resultSize == MemoryLayout<CInt>.size)
    return Int(result)
}

print(cachelineSize()) // 64
```

### Advanced C interoperability — [18:18]

```swift
import Darwin

func cachelineSize() -> Int {
    var query = [CTL_HW, HW_CACHELINE]
    return query.withUnsafeMutableBufferPointer { buffer in
        var result: CInt = 0
        withUnsafeMutablePointer(to: &result) { resultptr in
            var resultSize = MemoryLayout<CInt>.size
            let r = withUnsafeMutablePointer(to: &resultSize) { sizeptr in
                sysctl(buffer.baseAddress, CUnsignedInt(buffer.count),
                       resultptr, sizeptr,
                       nil, 0)
            }
            precondition(r == 0, "Cannot query cache line size")
            precondition(resultSize == MemoryLayout<CInt>.size)
        }
        return Int(result)
    }
}

print(cachelineSize()) // 64
```

### Advanced C interoperability — [18:30]

```swift
import Darwin

func cachelineSize() -> Int {
    var query = [CTL_HW, HW_CACHELINE]
    var result: CInt = 0
    var resultSize = MemoryLayout<CInt>.size
    let r = sysctl(&query, CUnsignedInt(query.count), &result, &resultSize, nil, 0)
    precondition(r == 0, "Cannot query cache line size")
    precondition(resultSize == MemoryLayout<CInt>.size)
    return Int(result)
}

print(cachelineSize()) // 64
```

### Closure-based vs. implicit pointers — [18:48]

```swift
var value = 42
withUnsafeMutablePointer(to: &value) { p in
  p.pointee += 1
}
print(value)  // 43
```

### Closure-based vs. implicit pointers — [19:19]

```swift
var value = 42
withUnsafeMutablePointer(to: &value) { p in
  p.pointee += 1
}
print(value)  // 43

var value2 = 42
let p = UnsafeMutablePointer(&value2) // BROKEN -- dangling pointer!
p.pointee += 1
print(value2)
```

### Initializing contiguous collection storage — [19:43]

```swift
Array.init(unsafeUninitializedCapacity:initializingWith:)
String.init(unsafeUninitializedCapacity:initializingUTF8With:)
```

### Initializing a String value using a C function — [20:02]

```swift
import Darwin

func kernelVersion() -> String {
    var query = [CTL_KERN, KERN_VERSION]
    var length = 0
    let r = sysctl(&query, 2, nil, &length, nil, 0)
    precondition(r == 0, "Error retrieving kern.version")
    return String(unsafeUninitializedCapacity: length) { buffer in
        var length = buffer.count
        let r = sysctl(&query, 2, buffer.baseAddress, &length, nil, 0)
        precondition(r == 0, "Error retrieving kern.version")
        precondition(length > 0 && length <= buffer.count)
        precondition(buffer[length - 1] == 0)
        return length - 1
    }
}

print(kernelVersion())
// Darwin Kernel Version 19.5.0: Thu Apr 30 18:25:59 PDT 2020; root:xnu-6153.121.1~7/RELEASE_X86_64
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10648/4/59961AEA-1ADD-470E-BD61-596E5950E0BE/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10648) — developer.apple.com. Indexed for agent consumption._