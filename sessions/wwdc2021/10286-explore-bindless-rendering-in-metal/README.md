---
id: "wwdc2021-10286"
event: "wwdc2021"
year: 2021
title: "Explore bindless rendering in Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10286"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Explore bindless rendering in Metal

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10286](https://developer.apple.com/videos/play/wwdc2021/10286)

Unleash the full potential of your shaders and implement modern rendering techniques by adding Argument Buffers to adopt bindless rendering. Learn how to make your entire scene and resources available to the GPU to make the most out of raytracing and rasterization pipelines.

**Keywords:** `3d graphics`, `game`, `game dev`, `game developer`, `metal`, `metal shading language`, `metal tools`, `proapps`, `raytracing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,397 words)

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
- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/Metal-Feature-Set-Tables.pdf
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Simple Intersection Kernel 2 — [0:07]

```objectivec
if(i.type == intersection_type::triangle)
{
  constant Instance& inst     = get_instance(i);
  constant Mesh&     mesh     = get_mesh(inst, i);
  constant Material& material = get_material(inst, i);

  color = shade_pixel(mesh, material, i);
}   

outImage.write(color, tid);
```

### PBR fragment shading requires several textures — [0:08]

```objectivec
fragment half4 pbrFragment(ColorInOut in [[stage_in]],
                           texture2d< float > albedo    [[texture(0)]],
                           texture2d< float > roughness [[texture(1)]],
                           texture2d< float > metallic  [[texture(2)]],
                           texture2d< float > occlusion [[texture(3)]])
{	
	half4 color = calculateShading(in, albedo, roughness, metallic, occlusion);
	return color;
}
```

### Bindless makes all textures available via AB navigation — [0:09]

```objectivec
fragment half4 pbrFragmentBindless(ColorInOut in [[stage_in]], 
                                   device const Scene* pScene [[buffer(0)]])
{
	device const Instance& instance = pScene->instances[in.instance_id];
	device const Material& material = pScene->materials[instance.material_id];

	half4 color = calculateShading(in, material);

	return color;
}
```

### Simple Intersection Kernel 1 — [1:48]

```objectivec
if (intersection.type == intersection_type::triangle) 
{
  // solid blue triangle
  color = float4(0.0f, 0.0f, 1.0f, 1.0f);
}   

outImage.write(color, tid);
```

### Encoder creation — [11:33]

```objectivec
struct Instance
{
    constant Mesh*     pMesh            [[id(0)]];
    constant Material* pMaterial        [[id(1)]];
    constant float4x4  modelTransform   [[id(2)]];
};
```

### Encoder via reflection — [11:50]

```objectivec
// Shader code references scene
kernel void RTReflections( constant Scene* pScene [[buffer(0)]] );
```

### Argument Buffers referenced indirectly — [13:08]

```objectivec
MTLArgumentDescriptor* meshArg 
= [MTLArgumentDescriptor argumentDescriptor];

meshArg.index    = 0;
meshArg.dataType = MTLDataTypePointer;
meshArg.access   = MTLArgumentAccessReadOnly;

// Declare all other arguments (material and transform)

id<MTLArgumentEncoder> instanceEncoder 
= [device newArgumentEncoderWithArguments:@[meshArg, 
                                            materialArg, 
                                            transformArg]];
```

### Navigation 1 — [16:10]

```objectivec
// Instance and Mesh

constant Instance& instance = pScene->instances[intersection.instance_id];
constant Mesh&     mesh     = instance.mesh[intersection.geometry_id];

// Primitive indices

ushort3 indices; // assuming 16-bit indices, use uint3 for 32-bit

indices.x = mesh.indices[ intersection.primitive_id * 3 + 0 ];
indices.y = mesh.indices[ intersection.primitive_id * 3 + 1 ];
indices.z = mesh.indices[ intersection.primitive_id * 3 + 2 ];
```

### Navigation 2 — [16:43]

```objectivec
// Vertex data

packed_float3 n0 = mesh.normals[ indices.x ];
packed_float3 n1 = mesh.normals[ indices.y ];
packed_float3 n2 = mesh.normals[ indices.z ];

// Interpolate attributes

float3 barycentrics = calculateBarycentrics(intersection);
float3 normal       = weightedSum(n0, n1, n2, barycentrics);
```

### Simple Intersection Kernel — [17:15]

```objectivec
if(i.type == intersection_type::triangle)
{
  constant Instance& inst     = get_instance(i);
  constant Mesh&     mesh     = get_mesh(inst, i);
  constant Material& material = get_material(inst, i);

  color = shade_pixel(mesh, material, i);
}   

outImage.write(color, tid);
```

### PBR fragment shading requires several textures — [19:30]

```objectivec
fragment half4 pbrFragment(ColorInOut in [[stage_in]],
                           texture2d< float > albedo    [[texture(0)]],
                           texture2d< float > roughness [[texture(1)]],
                           texture2d< float > metallic  [[texture(2)]],
                           texture2d< float > occlusion [[texture(3)]])
{	
	half4 color = calculateShading(in, albedo, roughness, metallic, occlusion);

  return color;
}
```

### Bindless makes all textures available via AB navigation — [19:48]

```objectivec
fragment half4 pbrFragmentBindless(ColorInOut in [[stage_in]], 
                                   device const Scene* pScene [[buffer(0)]])
{
	device const Instance& instance = pScene->instances[in.instance_id];
	device const Material& material = pScene->materials[instance.material_id];

	half4 color = calculateShading(in, material);

	return color;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10286/7/76356517-0CAC-4E8D-81E3-B42DCE552D15/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10286/7/76356517-0CAC-4E8D-81E3-B42DCE552D15/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10286) — developer.apple.com. Indexed for agent consumption._
