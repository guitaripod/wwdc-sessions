---
id: "wwdc2021-10150"
event: "wwdc2021"
year: 2021
title: "Explore hybrid rendering with Metal ray tracing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10150"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore hybrid rendering with Metal ray tracing

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10150](https://developer.apple.com/videos/play/wwdc2021/10150)

Discover how you can combine ray tracing with your rasterization engine to implement simplified graphics techniques and elevate visuals in your app or game. We’ll explore how you can use natural algorithms to accurately simulate the interplays of light, and learn how to take advantage of the latest tools in Xcode to capture, inspect, and debug your ray-traced scenes.

**Keywords:** `game dev`, `game developer`, `metal`, `metal shading language`, `metal tools`, `optimization`, `proapps`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,578 words)

## Documentation & Resources

- [Rendering reflections in real time using ray tracing](https://developer.apple.com/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing.json
- [Applying realistic material and lighting effects to entities](https://developer.apple.com/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities.json
- [Accelerating ray tracing using Metal](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
- [Managing groups of resources with argument buffers](https://developer.apple.com/documentation/metal/buffers/managing_groups_of_resources_with_argument_buffers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/buffers/managing_groups_of_resources_with_argument_buffers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/buffers/managing_groups_of_resources_with_argument_buffers.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Hybrid rendering in Metal 1 — [6:32]

```objectivec
// Create render pass

MTLRenderPassDescriptor* gbufferPass = [MTLRenderPassDescriptor new];
gbufferPass.depthAttachment.texture = gbuffer.depthTexture;
gbufferPass.depthAttachment.storeAction = MTLStoreActionStore;

gbufferPass.colorAttachments[0].texture = gbuffer.normalTexture;
gbufferPass.colorAttachments[0].storeAction = MTLStoreActionStore;
```

### Hybrid rendering in Metal 2 — [6:50]

```objectivec
// Create render pass

id< MTLRenderCommandEncoder > renderEncoder =
             [commandBuffer renderCommandEncoderWithDescriptor:gbufferPass];

encodeRenderScene( scene, renderEncoder );

[renderEncoder endEncoding];
```

### Hybrid rendering in Metal 3 — [7:06]

```objectivec
// Dispatch ray tracing via compute

id< MTLComputeCommandEncoder > compEncoder = [commandBuffer computeCommandEncoder];

[compEncoder setTexture:gbuffer.depthTexture atIndex:0];
[compEncoder setTexture:gbuffer.normalTexture atIndex:1];

[compEncoder setTexture:outReflectionMap atIndex:2];

[compEncoder setComputePipelineState:raytraceReflectionKernel];

encode2dDispatch( width, height, compEncoder );

[compEncoder endEncoding];
```

### Ray-traced shadow kernel — [11:54]

```objectivec
// Calculate shadow ray from G-Buffer

float3 p = calculatePosition( depth_texture, thread_id );
ray shadowRay( p, lightDirection, 0.01f, 1.0f );

// Trace for any intersections

intersector< triangle_data, instancing > shadowIntersector;
shadowIntersector.accept_any_intersection( true );

auto shadowIntersection = shadowIntersector.intersect( shadowRay, accel_structure );

// Point is in light if no intersections are found

if ( intersection.type == intersection_type::none ) {
   // Point is illuminated by this light
}
```

### Ray-traced ambient occlusion kernel — [15:07]

```objectivec
// Generate ray in hemisphere

ray ray = cosineWeightedRay( thread_id );

ray.max_distance = 0.5f;

// Trace nearby intersections

intersector< triangle_data, instancing > i;

auto intersection = i.intersect( ray, accel_structure );

if ( intersection.type != intersection_type::none ) {
   // Point is obscured by nearby geometry
}
```

### Ray-traced reflection kernel — [19:34]

```swift
// Calculate shadow ray from G-Buffer

float3 p = calculatePosition( depth_texture, thread_id );
float3 reflectedDir = reflect( p - cameraPosition, normal );

ray reflectedRay( p, reflectedDir, 0.01f, FLT_MAX );

// Trace for any intersections

intersector< triangle_data, instancing > refIntersector;
auto intersection = refIntersector.intersect( reflectedRay, accel_structure );

// Shade depending on intersection

if ( intersection.type != intersection_type::none ) {
   // Reflected ray hit an object: perform shading
}
else {
   // No intersection: draw skybox
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10150/9/F2EBE5D9-9990-476B-82FF-D73638B5E1AF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10150/9/F2EBE5D9-9990-476B-82FF-D73638B5E1AF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10150) — developer.apple.com. Indexed for agent consumption._