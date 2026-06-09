---
id: "wwdc2020-10632"
event: "wwdc2020"
year: 2020
title: "Optimize Metal Performance for Apple silicon Macs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10632"
topics: ["Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# Optimize Metal Performance for Apple silicon Macs

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10632](https://developer.apple.com/videos/play/wwdc2020/10632)

Apple silicon Macs are a transformative new platform for graphics-intensive apps — and we’re going to show you how to fire up the GPU to create blazingly fast apps and games. Discover how to take advantage of Apple’s unique Tile-Based Deferred Rendering (TBDR) GPU architecture within Apple silicon Macs and learn how to schedule workloads to provide maximum throughput, structure your rendering pipeline, and increase overall efficiency. And dive deep with our graphics team as we explore shader optimizations for the Apple GPU shader core. We’ve designed this session in tandem with “Bring your Metal app to Apple silicon Macs,” and recommend you watch that first. For more, watch “Harness Apple GPUs with Metal” to learn how TBDR applies to a variety of modern rendering techniques.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(7,138 words)

## Documentation & Resources

- [Learn more about Apple Silicon](https://developer.apple.com/documentation/apple-silicon) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/apple-silicon
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/apple-silicon.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Encoding with parallel render commands — [11:16]

```swift
// Encoding with parallel render commands

let parallelDescriptor = MTLRenderPassDescriptor()
// … setup render pass as usual … 

let parallelEncoder = commandBuffer.makeParallelRenderCommandEncoder(descriptor:parallelDescriptor)

let subEncoder0 = parallelEncoder.makeRenderCommandEncoder()
let subEncoder1 = parallelEncoder.makeRenderCommandEncoder()

let syncPoint = DispatchGroup()
DispatchQueue.global(qos: .userInteractive).async(group: syncPoint) { 
    /* … encode with subEncoder0 … */ }
DispatchQueue.global(qos: .userInteractive).async(group: syncPoint) { 
    /* … encode with subEncoder1 … */ }

syncPoint.wait()
parallelEncoder.end()
```

### Multiple render target setup — [14:51]

```swift
// Multiple render target setup

let textureDescriptor = MTLTextureDescriptor.texture2DDescriptor(…)
let lightingTexture = device.makeTexture(descriptor: textureDescriptor)

textureDescriptor.storageMode = .memoryless
let attenuationTexture = device.makeTexture(descriptor: textureDescriptor) 

let renderPassDesc = MTLRenderPassDescriptor()
renderPassDesc.colorAttachments[0].texture      = lightingTexture
renderPassDesc.colorAttachments[0].loadAction   = .clear
renderPassDesc.colorAttachments[0].storeAction  = .store
renderPassDesc.colorAttachments[1].texture      = attenuationTexture
renderPassDesc.colorAttachments[1].loadAction   = .clear
renderPassDesc.colorAttachments[1].storeAction  = .dontCare

let renderPass = commandBuffer.makeRenderCommandEncoder(descriptor: renderPassDesc);
```

### Write masking — [19:47]

```swift
let descriptor = MTLRenderPipelineDescriptor();
// ...
descriptor.colorAttachments[0].writeMask = .red | .green;
```

### Write to all render pass attachments — [21:15]

```swift
struct FragInput { ... };
struct FragOutput { float3 albedo; float3 normals; float3 lighting; };

fragment FragOutput GenerateGbuffer(
                         FragInput in [[stage_in]]) {
    FragOutput out;
    out.albedo = sampleAlbedo(in);
    out.normals = interpolateNormals(in);
    out.lighting = float3(0, 0, 0);
    return out;
}
```

### Optimized tiled deferred render pass setup — [30:19]

```swift
let renderPassDesc = MTLRenderPassDescriptor()

renderPassDesc.tileWidth = 32
renderPassDesc.tileHeight = 32

renderPassDesc.threadgroupMemoryLength = MemoryLayout<LightInfo>.size * 8

renderPassDesc.colorAttachments[0].texture      = albedoMemorylessTexture
renderPassDesc.colorAttachments[0].loadAction   = .clear
renderPassDesc.colorAttachments[0].storeAction  = .dontCare
renderPassDesc.colorAttachments[1].texture      = normalsMemorylessTexture
renderPassDesc.colorAttachments[1].loadAction   = .clear
renderPassDesc.colorAttachments[1].storeAction  = .dontCare
renderPassDesc.colorAttachments[2].texture      = roughnessMemorylessTexture
renderPassDesc.colorAttachments[2].loadAction   = .clear
renderPassDesc.colorAttachments[2].storeAction  = .dontCare
renderPassDesc.colorAttachments[3].texture      = lightingTexture
renderPassDesc.colorAttachments[3].loadAction   = .clear
renderPassDesc.colorAttachments[3].storeAction  = .store
```

### Transitioning from deferred rendering to multi-layer alpha blending layout — [32:20]

```swift
// Transitioning from deferred rendering to multi-layer alpha blending layout
struct DeferredShadingFragment {
    rgba8unorm<half4> albedo;
    rg11b10f<half3>   normal;
    float             depth;
    rgb9e5<half3>     lighting;
};
struct MultiLayerAlphaBlendFragments {
    half4 color_and_transmittence[3];
    float depth[3];
};
struct FragmentOutput {
    MultiLayerAlphaBlendFragments v [[imageblock_data]];
};
fragment FragmentOutput my_tile_shader(DeferredShadingFragment input [[imageblock_data]]) {
    FragmentOutput output;
    output.v.color_and_transmittence[0] = half4(input.lighting, 0.0h);
    output.v.depth[0]                   = input.depth;
    return output;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10632/7/9639690B-2E3B-4B2D-A211-879DBACDE84E/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10632) — developer.apple.com. Indexed for agent consumption._
