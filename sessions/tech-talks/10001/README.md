---
id: "tech-talks-10001"
event: "tech-talks"
year: 2017
title: "Explore Live GPU Profiling with Metal Counters"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/10001"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Explore Live GPU Profiling with Metal Counters

**Event:** Tech Talks · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-10-21 · **Session:** [tech-talks-10001](https://developer.apple.com/videos/play/tech-talks/10001)

Take advantage of the Metal Counters API for GPU profiling in macOS Big Sur and iOS 14. This API provides access at runtime to low-level GPU profiling information, which was previously available only through offline tools in Xcode and Instruments. Metal Counters accelerate the optimization process by giving you access to important GPU information, helping you fine-tune your app's performance to create faster and more fluid apps and gaming experiences. Learn to collect and parse these low-level GPU timestamps and use the in-depth information to help with performance tuning in Metal.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,011 words)

## Code Snippets

### Checking for available Metal counters — [3:38]

```swift
if (@available(macOS 11.0, iOS 14.0, *))
{
    _supportsStageBoundary = [_device supportsCounterSampling:MTLCounterSamplingPointAtStageBoundary];
    _supportsDrawBoundary  = [_device supportsCounterSampling:MTLCounterSamplingPointAtDrawBoundary];
}
```

### Counter sets — [3:52]

```swift
[_device.counterSets enumerateObjectsUsingBlock:^(id<MTLCounterSet> nonnull obj,
                                                  NSUInteger                idx,
                                                  BOOL * nonnull            stop) {
       if ([[obj name] isEqualToString:MTLCommonCounterSetTimestamp])
            _counterSetTimestamp = obj;
}];
```

### Sampling counters on Apple GPUs  — [5:05]

```swift
// When setting up the render pass descriptor

if (_supportsStageBoundary || _supportsDrawBoundary)
{
    MTLCounterSampleBufferDescriptor *desc = [MTLCounterSampleBufferDescriptor new];

    desc.sampleCount = 6; // Number of samples to store 
    desc.storageMode = MTLStorageModeShared;
    desc.label       = @"Live Profiling HUD Metal counter sample buffer";
    desc.counterSet  = _counterSetTimestamp;

    id<MTLCounterSampleBuffer> sampleBuffer =
                               [_device newCounterSampleBufferWithDescriptor:desc error:nil];

    MTLRenderPassSampleBufferAttachmentDescriptor *sampleBufferDesc =
                                  renderPassDescriptor.sampleBufferAttachments[0];

    if (_supportsStageBoundary)
    {
        sampleBufferDesc.startOfVertexSampleIndex   = 0;
        sampleBufferDesc.endOfVertexSampleIndex     = 1;
        sampleBufferDesc.startOfFragmentSampleIndex = 2;
        sampleBufferDesc.endOfFragmentSampleIndex   = 3;
    }

    sampleBufferDesc.sampleBuffer = sampleBuffer;
}
```

### Sampling counters at draw boundary — [6:23]

```swift
// After creating a new render command encoder
[renderCommandEncoder sampleCountersInBuffer:sampleBuffer
                               atSampleIndex:4
                                 withBarrier:NO];

// All draw calls
[renderCommandEncoder sampleCountersInBuffer:sampleBuffer
                               atSampleIndex:5
                                 withBarrier:NO];

// End encoding
```

### Collecting timestamps — [7:28]

```swift
// For each tracked sampleBuffer, resolve the counters
NSData *data = [sampleBuffer resolveCounterRange:NSMakeRange(0, 6)];

MTLCounterResultTimestamp *sample = (MTLCounterResultTimestamp *)[data bytes];

// And simply access the timestamps
if (_supportsStageBoundary)
{
    double vertexStart = sample[0].timestamp / (double)NSEC_PER_SEC;
}

// Check for errors
if (sample[0].timestamp == MTLCounterErrorValue) 
{
  // Handle error
}
```

### Aligning timestamps — [9:05]

```swift
// On immediate mode GPU
MTLTimestamp cpuTimestamp;
MTLTimestamp gpuTimestamp;
[_device sampleTimestamps:&cpuTimestamp gpuTimestamp:&gpuTimestamp];

// Do a linear interpolation between correlated timestamps
gpu_ns = cpu_t0 + (cpu_t1 - cpu_t0) * (gpu_timestamp - gpu_t0) / (gpu_t1 - gpu_t0);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/10001/3/B2344663-580B-4B92-AB59-E198E39B8F0F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/10001/3/B2344663-580B-4B92-AB59-E198E39B8F0F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/10001) — developer.apple.com. Indexed for agent consumption._