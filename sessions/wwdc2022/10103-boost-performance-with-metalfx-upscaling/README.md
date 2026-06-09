---
id: "wwdc2022-10103"
event: "wwdc2022"
year: 2022
title: "Boost performance with MetalFX Upscaling"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10103"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Boost performance with MetalFX Upscaling

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10103](https://developer.apple.com/videos/play/wwdc2022/10103)

Discover MetalFX, a new API that provides platform optimized graphics effects for Metal applications. With MetalFX Upscaling, your application can now render frames at a lower resolution, reducing rendering time, without compromising rendering quality. We'll also show you how and when to use its two effects: spatial upscaling, which delivers substantial performance gains, and temporal AA and upscaling, which delivers the highest quality rendering.

**Keywords:** `game dev`, `game developer`, `games`, `metal`, `metal 3`, `metalfx`, `metalfx upscaling`, `metal tools`, `performance`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,167 words)

## Documentation & Resources

- [Applying temporal antialiasing and upscaling using MetalFX](https://developer.apple.com/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx.json
- [4K Video (WWDC22-10103)](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10103/7/0DA14AB6-97A2-4E95-A960-E27CBC5E5012/downloads/wwdc2022-10103_4k.mp4?dl=1) _download_
- [MetalFX](https://developer.apple.com/documentation/MetalFX) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalFX
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalFX.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Spatial upscaling (initialization) — [3:39]

```swift
// Spatial upscaling (initialization)

let desc = MTLFXSpatialScalerDescriptor()
desc.inputWidth = 1280
desc.inputHeight = 720
desc.outputWidth = 2560
desc.outputHeight = 1440
desc.colorTextureFormat = .bgra8Unorm_srgb
desc.outputTextureFormat = .bgra8Unorm_srgb
desc.colorProcessingMode = .perceptual

spatialScaler = desc.makeSpatialScaler(device: mtlDevice)
```

### Spatial upscaling (per frame) — [9:16]

```swift
// Spatial upscaling (per frame)

// Encode Metal commands to draw game frame here...

// Begin setting per frame properties for effect
spatialScaler.colorTexture = currentFrameColor
spatialScaler.outputTexture = currentFrameUpscaledColor

// Encode scaling effect into command buffer
spatialScaler.encode(commandBuffer: cmdBuffer)

// Encode Metal commands for particle/noise effects and game UI drawing for frame here...
```

### Temporal antialiasing and upscaling (initialization) — [9:16]

```swift
// Temporal antialiasing and upscaling (initialization)

let desc = MTLFXTemporalScalerDescriptor()
desc.inputWidth = 1280
desc.inputHeight = 720
desc.outputWidth = 2560
desc.outputHeight = 1440
desc.colorTextureFormat = .rgba16Float
desc.depthTextureFormat = .depth32Float
desc.motionTextureFormat = .rg16Float
desc.outputTextureFormat = .rgba16Float

temporalScaler = desc.makeTemporalScaler(device: mtlDevice)
temporalScaler.motionVectorScale = CGPoint(x: 1280, y: 720)
```

### Temporal antialiasing and upscaling (per frame) — [10:35]

```swift
// Temporal antialiasing and upscaling (per frame)

// Encode Metal commands to draw game frame here...

// Setup per frame effect properties
temporalScaler.resetHistory = firstFrameOrSceneCut
temporalScaler.colorTexture = currentFrameColor
temporalScaler.depthTexture = currentFrameDepth
temporalScaler.motionTexture = currentFrameMotion
temporalScaler.outputTexture = currentFrameUpscaledColor
temporalScaler.reversedDepth = reversedDepth
temporalScaler.jitterOffset = currentFrameJitterOffset

// Encode scaling effect into commandBuffer
temporalScaler.encode(commandBuffer: cmdBuffer)

// Encode Metal commands for post processing/game UI drawing for frame here...
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10103/7/0DA14AB6-97A2-4E95-A960-E27CBC5E5012/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10103/7/0DA14AB6-97A2-4E95-A960-E27CBC5E5012/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10103) — developer.apple.com. Indexed for agent consumption._
