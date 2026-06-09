---
id: "wwdc2020-10167"
event: "wwdc2020"
year: 2020
title: "Safely manage pointers in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10167"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Safely manage pointers in Swift

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10167](https://developer.apple.com/videos/play/wwdc2020/10167)

Come with us as we delve into unsafe pointer types in Swift. Discover the requirements for each type and how to use it correctly. We’ll discuss typed pointers, drop down to raw pointers, and finally circumvent pointer type safety entirely by binding memory. This session is a follow-up to "Unsafe Swift" from WWDC20. To get the most out of it, you should be familiar with Swift and the C programming language.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,307 words)

## Documentation & Resources

- [Manual Memory Management](https://developer.apple.com/documentation/Swift/manual-memory-management) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/manual-memory-management
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/manual-memory-management.json

## Code Snippets

### Images: undefined behavior can lead to data loss — [5:44]

```swift
struct Image {
    // elided...
}

// Undefined behavior can lead to data loss…
struct Collage {
    var imageData: UnsafeMutablePointer<Image>?
    var imageCount: Int = 0
}

// C-style API expects a pointer-to-Int
func addImages(_ countPtr: UnsafeMutablePointer<UInt32>) -> UnsafeMutablePointer<Image> {
    // ...
    let imageData = UnsafeMutablePointer<Image>.allocate(capacity: 1)
    imageData[0] = Image()
    countPtr.pointee += 1
    return imageData
}

func saveImages(_ imageData: UnsafeMutablePointer<Image>, _ count: Int) {
    // Arbitrary function body...
    print(count)
}

var collage = Collage()
collage.imageData = withUnsafeMutablePointer(to: &collage.imageCount) {
    addImages(UnsafeMutableRawPointer($0).assumingMemoryBound(to: UInt32.self))
}
saveImages(collage.imageData!, collage.imageCount) // May see imageCount == 0
```

### Direct memory allocation — [10:06]

```swift
func directAllocation<T>(t: T, count: Int) {
    let tPtr = UnsafeMutablePointer<T>.allocate(capacity: count)
    tPtr.initialize(repeating: t, count: count)
    tPtr.assign(repeating: t, count: count)
    tPtr.deinitialize(count: count)
    tPtr.deallocate()
}
```

### Using a raw pointer to read from Foundation Data — [14:24]

```swift
import Foundation

func readUInt32(data: Data) -> UInt32 {
    data.withUnsafeBytes { (buffer: UnsafeRawBufferPointer) in
        buffer.load(fromByteOffset: 4, as: UInt32.self)
    }
}

let data = Data(Array<UInt8>([0, 0, 0, 0, 1, 0, 0, 0]))
print(readUInt32(data: data))
```

### Raw allocation — [14:37]

```swift
func rawAllocate<T>(t: T, numValues: Int) -> UnsafeMutablePointer<T> {
    let rawPtr = UnsafeMutableRawPointer.allocate(
            byteCount: MemoryLayout<T>.stride * numValues,
            alignment: MemoryLayout<T>.alignment)
    let tPtr = rawPtr.initializeMemory(as: T.self, repeating: t, count: numValues)
    // Must use the typed pointer ‘tPtr’ to deinitialize.
    return tPtr
}
```

### Contiguous allocation — [15:43]

```swift
func contiguousAllocate<Header>(header: Header, numValues: Int) -> (UnsafeMutablePointer<Header>, UnsafeMutablePointer<Int32>) {
    let offset = MemoryLayout<Header>.stride
    let byteCount = offset + MemoryLayout<Int32>.stride * numValues
    assert(MemoryLayout<Header>.alignment >= MemoryLayout<Int32>.alignment)
    let bufferPtr = UnsafeMutableRawPointer.allocate(
            byteCount: byteCount, alignment: MemoryLayout<Header>.alignment)
    let headerPtr = bufferPtr.initializeMemory(as: Header.self, repeating: header, count: 1)
    let elementPtr = (bufferPtr + offset).initializeMemory(as: Int32.self, repeating: 0, count: numValues)
    return (headerPtr, elementPtr)
}
```

### Using assumingMemoryBound(to:) to recover a typed pointer — [18:03]

```swift
func takesIntPointer(_: UnsafePointer<Int>) { /* elided */ }

struct RawContainer {
    var rawPtr: UnsafeRawPointer
    var pointsToInt: Bool
}

func testContainer(numValues: Int) {
    let intPtr = UnsafeMutablePointer<Int>.allocate(capacity: numValues)
    let rc = RawContainer(rawPtr: intPtr, pointsToInt: true)
    // ...
    if rc.pointsToInt {
        takesIntPointer(rc.rawPtr.assumingMemoryBound(to: Int.self))
    }
}
```

### Calling pthread_create — [18:40]

```swift
// Use assumingMemoryBound to recover a pointer type from a (void *) C callback.
/*
func pthread_create(_ thread: UnsafeMutablePointer<pthread_t?>!,
    _ attr: UnsafePointer<pthread_attr_t>?,
    _ start_routine: (UnsafeMutableRawPointer) -> UnsafeMutableRawPointer?,
    _ arg: UnsafeMutableRawPointer?) -> Int32
*/
import Darwin

struct ThreadContext { /* elided */ }

func testPthreadCreate() {
    let contextPtr = UnsafeMutablePointer<ThreadContext>.allocate(capacity: 1)
    contextPtr.initialize(to: ThreadContext())
    var pthread: pthread_t?
    let result = pthread_create(
            &pthread, nil,
            { (ptr: UnsafeMutableRawPointer) in
                let contextPtr = ptr.assumingMemoryBound(to: ThreadContext.self)
                // ... The rest of the thread start routine
                return nil
            },
            contextPtr)
}
```

### Pointing to tuple elements — [19:26]

```swift
func takesIntPointer(_: UnsafePointer<Int>) { /* elided */ }

func testPointingToTuple() {
    let tuple = (0, 1, 2)
    withUnsafePointer(to: tuple) { (tuplePtr: UnsafePointer<(Int, Int, Int)>) in
        takesIntPointer(UnsafeRawPointer(tuplePtr).assumingMemoryBound(to: Int.self))
    }
}
```

### Pointing to struct properties — [20:26]

```swift
func takesIntPointer(_: UnsafePointer<Int>) { /* elided */ }

struct MyStruct {
    var status: Bool
    var value: Int
}

func testPointingToStructProperty() {
    let myStruct = MyStruct(status: true, value: 0)
    withUnsafePointer(to: myStruct) { (ptr: UnsafePointer<MyStruct>) in
        let rawValuePtr =
                (UnsafeRawPointer(ptr) + MemoryLayout<MyStruct>.offset(of: \MyStruct.value)!)
        takesIntPointer(rawValuePtr.assumingMemoryBound(to: Int.self))
    }
}
```

### bindMemory(to:capacity:) invalidates pointers — [21:17]

```swift
func testBindMemory() {
    let uint16Ptr = UnsafeMutablePointer<UInt16>.allocate(capacity: 2)
    uint16Ptr.initialize(repeating: 0, count: 2)
    let int32Ptr = UnsafeMutableRawPointer(uint16Ptr).bindMemory(to: Int32.self, capacity: 1)
    // Accessing uint16Ptr is now undefined
    int32Ptr.deallocate()
}
```

### withMemoryRebound(to:capacity:) API — [23:13]

```swift
func takesUInt8Pointer(_: UnsafePointer<UInt8>) { /* elided */ }

func testWithMemoryRebound(int8Ptr: UnsafePointer<Int8>, count: Int) {
    int8Ptr.withMemoryRebound(to: UInt8.self, capacity: count) {
        (uint8Ptr: UnsafePointer<UInt8>) in
        // int8Ptr cannot be used within this closure
        takesUInt8Pointer(uint8Ptr)
    }
    // uint8Ptr cannot be used outside this closure
}
```

### BufferView: Layering types on top of raw memory — [25:49]

```swift
struct UnsafeBufferView<Element>: RandomAccessCollection {
    let rawBytes: UnsafeRawBufferPointer
    let count: Int

    init(reinterpret rawBytes: UnsafeRawBufferPointer, as: Element.Type) {
        self.rawBytes = rawBytes
        self.count = rawBytes.count / MemoryLayout<Element>.stride
        precondition(self.count * MemoryLayout<Element>.stride == rawBytes.count)
        precondition(Int(bitPattern: rawBytes.baseAddress).isMultiple(of: MemoryLayout<Element>.alignment))
    }

    var startIndex: Int { 0 }

    var endIndex: Int { count }

    subscript(index: Int) -> Element {
        rawBytes.load(fromByteOffset: index * MemoryLayout<Element>.stride, as: Element.self)
    }
}

func testBufferView() {
    let array = [0,1,2,3]
    array.withUnsafeBytes {
        let view = UnsafeBufferView(reinterpret: $0, as: UInt.self)
        for val in view {
            print(val)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10167/3/5A7F9994-6332-4CE6-8132-10C43C01827B/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10167) — developer.apple.com. Indexed for agent consumption._
