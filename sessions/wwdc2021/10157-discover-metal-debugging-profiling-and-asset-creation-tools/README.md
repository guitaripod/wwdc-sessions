---
id: "wwdc2021-10157"
event: "wwdc2021"
year: 2021
title: "Discover Metal debugging, profiling, and asset creation tools"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10157"
topics: ["Graphics & Games", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Discover Metal debugging, profiling, and asset creation tools

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10157](https://developer.apple.com/videos/play/wwdc2021/10157)

Explore how Xcode can help you take your Metal debugging, profiling and asset creation workflows to the next level. Discover the latest tools for ray tracing and GPU profiling, and learn about Metal Debugger workflows. We’ll also show you how to use the Texture Converter tool, which supports all modern GPU texture formats and can easily integrate into your multi-platform asset creation pipelines.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,977 words)

## Documentation & Resources

- [Metal Developer Tools on Windows](https://developer.apple.com/download/more/?=Metal%20Developer%20Tools%20for%20Windows) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/more/?=Metal%20Developer%20Tools%20for%20Windows
- [Debugging the shaders within a draw command or compute dispatch](https://developer.apple.com/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### RGBM Encoding Pseudocode — [27:51]

```swift
float4 EncodeRGBM(float3 in)
{ 
    float4 rgbm; 
    rgbm.a = max3(in.r, in.g, in.b) / RGBM_Range;
    rgbm.rgb = in / (rgbm.a * RGBM_Range);
    return rgbm;
}
```

### RGBM Decoding Pseudocode — [28:41]

```swift
float3 DecodeRGBM(float4 sample)
{ 
    const float RGBM_Range = 6.0f;
    float scale = sample.a * RGBM_Range;
    return sample.rgb * scale;
}
```

### MetalTextureSwizzles — [30:55]

```objectivec
// Remap the X and Y channels to red and green channels for normal maps 
compressed with ASTC.

MTLTextureDescriptor* descriptor = [[MTLTextureDescriptor alloc] init];

MTLTextureSwizzle r = MTLTextureSwizzleRed;
MTLTextureSwizzle g = MTLTextureSwizzleAlpha;
MTLTextureSwizzle b = MTLTextureSwizzleZero;
MTLTextureSwizzle a = MTLTextureSwizzleZero;

descriptor.swizzle = MTLTextureSwizzleChannelsMake( r, g, b, a );
```

### ReconstructNormal — [31:55]

```objectivec
// Reconstruct z-axis from normal sample in shader code.

float3 ReconstructNormal(float2 sample)
{
    float3 normal;

    normal.xy = sample.xy * 2.0f - 1.0f;
    normal.z  = sqrt( saturate( 1.0f - dot( normal.xy, normal.xy ) ) );

    return normal;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10157/5/7C79C8DE-984A-4BD6-904D-3FCDFF5432CC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10157/5/7C79C8DE-984A-4BD6-904D-3FCDFF5432CC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10157) — developer.apple.com. Indexed for agent consumption._
