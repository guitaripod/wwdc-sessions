---
id: "wwdc2022-10104"
event: "wwdc2022"
year: 2022
title: "Load resources faster with Metal 3"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10104"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Load resources faster with Metal 3

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10104](https://developer.apple.com/videos/play/wwdc2022/10104)

Discover how you can use fast resource streaming in Metal 3 to quickly load assets. We'll show you how to use an asynchronous set-it-and-forget-it workflow in your app to take advantage of the speed of SSD storage and the throughput of Apple silicon’s unified memory architecture. We'll also explore how you can create separate queues that run parallel to — and synchronize with — your GPU render and compute work. Finally, we'll share how to designate assets like audio with high-priority queues to help you load data with lower latency.

**Keywords:** `3d graphics`, `game`, `game dev`, `game developer`, `metal`, `metal 3`, `metal tools`, `raytracing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,247 words)

## Documentation & Resources

- [Resource loading](https://developer.apple.com/documentation/Metal/resource-loading) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/resource-loading
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/resource-loading.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Create a handle to an existing file — [5:19]

```swift
// Create an Metal File IO Handle

// Create handle to an existing file
var fileIOHandle: MTLIOFileHandle!
do {
    try fileHandle = device.makeIOHandle(url: filePath)
} catch {
    print(error)
}
```

### Create a Metal IO command queue — [6:49]

```swift
// Create a Metal IO command queue

let commandQueueDescriptor = MTLIOCommandQueueDescriptor()

commandQueueDescriptor.type = MTLIOCommandQueueType.concurrent // or serial

var ioCommandQueue: MTLIOCommandQueue!
do {
    try ioCommandQueue = device.makeIOCommandQueue(descriptor: commandQueueDescriptor)
} catch {
    print(error)
}
```

### Create and submit a Metal IO command buffer — [7:17]

```swift
// Create Metal IO Command Buffer

let ioCommandBuffer = ioCommandQueue.makeCommandBuffer()

// Encode load commands
// Encode load texture and load buffer commands
ioCommandBuffer.load(texture, slice: 0, level: 0, size: size, 
                     sourceBytesPerRow:bytesPerRow, sourceBytesPerImage: bytesPerImage,  
                     destinationOrigin: destOrigin,
                     sourceHandle: fileHandle, sourceHandleOffset: 0)
ioCommandBuffer.load(buffer, offset: 0, size: size,
                     sourceHandle: fileHandle, sourceHandleOffset: 0)


// Commit command buffer for execution
ioCommandBuffer.commit()
```

### Synchronize loading and rendering with Metal shared events — [8:51]

```swift
var sharedEvent: MTLSharedEvent!
sharedEvent = device.makeSharedEvent()

// Create Metal IO command buffer
let ioCommandBuffer = ioCommandQueue.makeCommandBuffer()

ioCommandBuffer.waitForEvent(sharedEvent, value: waitVal)

// Encode load commands

ioCommandBuffer.signalEvent(sharedEvent, value: signalVal)
ioCommandBuffer.commit()

// Graphics work waits for the IO command buffer to signal
```

### TryCancel Metal IO command buffer — [10:29]

```swift
// Player in the center region
// Encode loads for the North-West region
ioCommandBufferNW.commit()
// Encode loads for the West region
ioCommandBufferW.commit()
// Encode loads for the South-West region
ioCommandBufferSW.commit()

// Player in the western region and heading south
// tryCancel NW command buffer
ioCommandBufferNW.tryCancel()

// ..
// ..
func regionNWCancelled() -> Bool {
    return ioCommandBufferNW.status == MTLIOStatus.cancelled
}
```

### Create a High Priority Metal IO command queue — [12:28]

```swift
// Create a Metal IO command queue

let commandQueueDescriptor = MTLIOCommandQueueDescriptor()
commandQueueDescriptor.type = MTLIOCommandQueueType.concurrent // or serial

// Set Metal IO command queue Priority
commandQueueDescriptor.priority = MTLIOPriority.high // or normal or low

var ioCommandQueue: MTLIOCommandQueue!
do {
    try ioCommandQueue = device.makeIOCommandQueue(descriptor: commandQueueDescriptor)
} catch {
    print(error)
}
```

### Create a compressed file — [14:04]

```swift
// Create a compressed file

// Create compression context
let chunkSize = 64 * 1024
let compressionMethod = MTLIOCompressionMethod.zlib
let compressionContext = MTLIOCreateCompressionContext(compressedFilePath, compressionMethod, chunkSize)

// Append uncompressed file data to the compression context
// Get uncompressed file data 
MTLIOCompressionContextAppendData(compressionContext, filedata.bytes, filedata.length)


// Write the compressed file
MTLIOFlushAndDestroyCompressionContext(compressionContext)
```

### Create a handle to a compressed file — [15:05]

```swift
// Create an Metal File IO Handle

// Create handle to a compressed file
var compressedFileIOHandle : MTLIOFileHandle!
do {
    try compressedFileHandle = device.makeIOHandle(url: compressedFilePath, compressionMethod: MTLIOCompressionMethod.zlib)
} catch {
    print(error)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10104/4/E095D698-00CE-4A00-812C-4BA755CE26DB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10104/4/E095D698-00CE-4A00-812C-4BA755CE26DB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10104) — developer.apple.com. Indexed for agent consumption._