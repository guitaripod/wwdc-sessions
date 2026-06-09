---
id: "wwdc2026-359"
event: "wwdc2026"
year: 2026
title: "Build real-time neural rendering pipelines with Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/359"
topics: ["AI & Machine Learning", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build real-time neural rendering pipelines with Metal

**Event:** WWDC26 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-359](https://developer.apple.com/videos/play/wwdc2026/359)

Discover how to integrate machine learning into your real-time rendering pipeline using Metal 4. We’ll explore practical adoption patterns and best practices for achieving production-quality results with MetalFX neural denoising, featuring real-world insights from Maxon’s Redshift Live. Learn how to train and deploy a neural tone mapper using the ML command encoder inline with your graphics work. Finally, dive into the new tensor API to build and evaluate small, specialized neural networks directly within your shaders.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,243 words)

## Documentation & Resources

- [Training a neural network to render irradiance in real time](https://developer.apple.com/documentation/Metal/training-a-neural-network-to-render-irradiance-in-real-time) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/training-a-neural-network-to-render-irradiance-in-real-time
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/training-a-neural-network-to-render-irradiance-in-real-time.json
- [Metal sample code library](https://developer.apple.com/documentation/Metal/metal-sample-code-library) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/metal-sample-code-library
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/metal-sample-code-library.json
- [Download the Metal Performance Primitives (MPP) Programming Guide](https://developer.apple.com/download/files/Metal-Performance-Primitives-Programming-Guide.pdf) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/files/Metal-Performance-Primitives-Programming-Guide.pdf
- [Understanding the Metal 4 core API](https://developer.apple.com/documentation/Metal/understanding-the-metal-4-core-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/understanding-the-metal-4-core-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/understanding-the-metal-4-core-api.json

## Code Snippets

### Compute camera-only motion vectors — [8:46]

```cpp
#include <metal_stdlib>
using namespace metal;

// Compute camera-only motion vectors
float4 clipCurrent = viewProjCurrent * float4(worldPos, 1.0);
float2 ndcCurrent = clipCurrent.xy / clipCurrent.w;

float4 clipPrevious = viewProjPrevious * float4(worldPos, 1.0);
float2 ndcPrevious = clipPrevious.xy / clipPrevious.w;

float2 motion = ndcPrevious - ndcCurrent;

// Get subpixel offset for current and previous frames
float2 jitterCurrent = getJitter(frameIndex);
float2 jitterPrevious = getJitter(frameIndexPrevious);
motion -= jitterPrevious - jitterCurrent;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/359/5/9da4a720-0dcb-4b8e-b61b-ba8310a61f29/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/359/5/9da4a720-0dcb-4b8e-b61b-ba8310a61f29/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/359) — developer.apple.com. Indexed for agent consumption._
