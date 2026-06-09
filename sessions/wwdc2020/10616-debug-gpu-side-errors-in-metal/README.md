---
id: "wwdc2020-10616"
event: "wwdc2020"
year: 2020
title: "Debug GPU-side errors in Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10616"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Debug GPU-side errors in Metal

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10616](https://developer.apple.com/videos/play/wwdc2020/10616)

Track down even the trickiest GPU-side programming errors with enhanced reporting in Xcode 12. While Metal’s API validation layer can catch most problems in a project, GPU errors can cause a host of difficult-to-debug issues. Get an introduction to GPU-side errors and learn how to find and eliminate problems like visual corruption, infinite loop timeouts, out of bounds memory accesses, nil resource access, or invalid resource residency with Xcode 12. Discover how to enable enhanced command buffer error reporting and shader validation, use them effectively as part of your debugging strategy, and automate them in your production pipeline.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,319 words)

## Documentation & Resources

- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Enable enhanced command buffer errors — [3:40]

```swift
let desc = MTLCommandBufferDescriptor()
desc.errorOptions = .encoderExecutionStatus
let commandBuffer = commandQueue.makeCommandBuffer(descriptor: desc)
```

### Processing enhanced command buffer errors — [3:55]

```swift
if let error = commandBuffer.error as NSError? {

    if let encoderInfos =
        error.userInfo[MTLCommandBufferEncoderInfoErrorKey]
        as? [MTLCommandBufferEncoderInfo] {

        for info in encoderInfos {
            print(info.label + info.debugSignposts.joined())
            if info.errorState == .faulted {
                print(info.label + " faulted!")
            }
        }
    }
}
```

### Command buffer logs API — [15:39]

```swift
commandBuffer.addCompletedHandler { (commandBuffer) in
    for log in commandBuffer.logs {
        let encoderLabel = log.encoderLabel ?? "Unknown Label"
        print("Faulting encoder \"\(encoderLabel)\"")
        guard let debugLocation = log.debugLocation,
              let functionName = debugLocation.functionName
        else {
            return
        }
        print("Faulting function \(functionName):\(debugLocation.line):\(debugLocation.column)")
    }
}
```

### Accessing the log — [15:40]

```bash
log stream --predicate "subsystem = 'com.apple.Metal' and category = 'GPUDebug'"
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10616/5/F585B9C6-DBD8-4C59-B210-5228EF5B86B1/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10616) — developer.apple.com. Indexed for agent consumption._
