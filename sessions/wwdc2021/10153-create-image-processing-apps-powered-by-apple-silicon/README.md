---
id: "wwdc2021-10153"
event: "wwdc2021"
year: 2021
title: "Create image processing apps powered by Apple silicon"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10153"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Create image processing apps powered by Apple silicon

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10153](https://developer.apple.com/videos/play/wwdc2021/10153)

Discover how to optimize your image processing app for Apple silicon. Explore how to take advantage of Metal render command encoders, tile shading, unified memory architecture, and memoryless attachments. We’ll show you how to use Apple's unique tile based deferred renderer architecture to create power efficient apps with low memory footprint, and take you through best practices when migrating your compute-based apps from discrete GPUs to Apple silicon.

**Keywords:** `apple silicon`, `cuda`, `metal`, `metal shading language`, `metal tools`, `opencl`, `performance`, `proapps`, `tips and tricks`, `video`, `video effects`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,520 words)

## Documentation & Resources

- [Debugging the shaders within a draw command or compute dispatch](https://developer.apple.com/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch.json
- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/Metal-Feature-Set-Tables.pdf
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Memoryless attachments — [10:53]

```swift
let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(…)
let outputTexture = device.makeTexture(descriptor: textureDescriptor)

textureDescriptor.storageMode = .memoryless
let tempTexture = device.makeTexture(descriptor: textureDescriptor) 

let renderPassDesc = MTLRenderPassDescriptor()
renderPassDesc.colorAttachments[0].texture      = outputTexture
renderPassDesc.colorAttachments[0].loadAction   = .dontCare
renderPassDesc.colorAttachments[0].storeAction  = .store
renderPassDesc.colorAttachments[1].texture      = tempTexture
renderPassDesc.colorAttachments[1].loadAction   = .clear
renderPassDesc.colorAttachments[1].storeAction  = .dontCare

let renderPass = commandBuffer.makeRenderCommandEncoder(descriptor: renderPassDesc)
```

### Uber-shaders impact on registers — [12:25]

```objectivec
fragment float4 processPixel(const constant ParamsStr* cs [[ buffer(0) ]])
{
  if (cs->inputIsHDR) {
    // do HDR stuff
  } else {
    // do non-HDR stuff
  }
  if (cs->tonemapEnabled) {
    // tone map
  }
}
```

### Function constants for Uber-shaders — [13:32]

```objectivec
constant bool featureAEnabled[[function_constant(0)]];
constant bool featureBEnabled[[function_constant(1)]];

fragment float4 processPixel(...)
{
  if (featureAEnabled) {
    // do A stuff
  } else {
    // do not-A stuff
  }
  if (featureBEnabled) {
    // do B stuff
  }
}
```

### Image processing filter graph — [23:02]

```objectivec
typedef struct
{
    float4 OPTexture        [[ color(0) ]];
    float4 IntermediateTex  [[ color(1) ]];
} FragmentIO;

fragment FragmentIO Unpack(RasterizerData in [[ stage_in ]],
                           texture2d<float, access::sample> srcImageTexture [[texture(0)]])
{
    FragmentIO out;

    //...

    // Run necessary per-pixel operations
    out.OPTexture       = // assign computed value;
    out.IntermediateTex = // assign computed value;
    return out;
}

fragment FragmentIO CSC(RasterizerData in [[ stage_in ]], FragmentIO Input)
{
    FragmentIO out;

    //...    

    out.IntermediateTex = // assign computed value;
    return out;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10153/4/F8C484C1-A0A2-4377-992B-313BEB320A28/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10153/4/F8C484C1-A0A2-4377-992B-313BEB320A28/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10153) — developer.apple.com. Indexed for agent consumption._
