---
id: "wwdc2020-10631"
event: "wwdc2020"
year: 2020
title: "Bring your Metal app to Apple silicon Macs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10631"
topics: ["Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# Bring your Metal app to Apple silicon Macs

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10631](https://developer.apple.com/videos/play/wwdc2020/10631)

Meet the Tile Based Deferred Rendering (TBDR) GPU architecture for Apple silicon Macs — the heart of your Metal app or game’s graphics performance. Learn how you can translate or port your graphics-intensive app over to Apple silicon, and how to take advantage of TBDR and Metal when building natively for the platform. We’ll look at how TBDR compares with the Immediate Mode Rendering pipeline of older Macs, go through common issues you may face when bringing an app or game over, and explore how to offer incredible performance when building with the native SDK.

We’ve designed this session in tandem with “Optimize Metal Performance for Apple silicon Macs.” After you’ve watched this session be sure to check that out next.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,592 words)

## Documentation & Resources

- [Learn more about Apple Silicon](https://developer.apple.com/documentation/apple-silicon) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/apple-silicon
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/apple-silicon.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Metal feature detection — [14:23]

```swift
{
    self.appleGPUFeatures = metalDevice.supportsFamily(.apple5)

    self.simdgroupSize = computePipeline.threadExecutionWidth

    self.isLowPower = metalDevice.isLowPower
}
```

### Enabling position invariance — [20:58]

```swift
// Renderer.swift
let options = MTLCompileOptions()
options.preserveInvariance = true

library = try device.makeLibrary(source: sourceString,
                                 options: options)


// vertex.metal
struct VertexOut
{
    float4 pos [[position, invariant]];
    float data;
};
```

### Threadgroup synchronization — [24:25]

```swift
// Correct synchronization

// launched with threadgroup size = 64
kernel void kernelMain(uint tid [[ thread_index_in_threadgroup ]],
                       uint simd_size [[ threads_per_simdgroup ]],
                       device uint * res [[ buffer(0) ]])
{
    threadgroup uint buf[64];

    buf[tid] = initBuffer(tid);

    if (simd_size == 64u)
        simdgroup_barrier(mem_flags::mem_threadgroup);
    else
        threadgroup_barrier(mem_flags::mem_threadgroup);

    uint index = (tid < 32) ? tid + 32 : tid - 32;
    res[tid] = buf[tid] + buf[index];
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10631/4/DC841F50-00E5-427F-90BD-555045D5EB52/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10631) — developer.apple.com. Indexed for agent consumption._