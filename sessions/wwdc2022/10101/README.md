---
id: "wwdc2022-10101"
event: "wwdc2022"
year: 2022
title: "Go bindless with Metal 3"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10101"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Go bindless with Metal 3

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10101](https://developer.apple.com/videos/play/wwdc2022/10101)

Learn how you can unleash powerful rendering techniques like ray tracing when you go bindless with Metal 3. We'll show you how to make your app’s bindless journey a joy by simplifying argument buffers, allocating acceleration structures from heaps, and benefitting from the improvements to the Metal’s validation layer and Debugger Tools. We'll also explore how you can command more CPU and GPU performance with long-term resource structures.


**Keywords:** `3d graphics`, `bindless`, `game`, `game dev`, `game developer`, `metal`, `metal shading language`, `metal tools`, `proapps`, `raytracing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,943 words)

## Documentation & Resources

- [Rendering reflections in real time using ray tracing](https://developer.apple.com/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing.json
- [Metal for Accelerating Ray Tracing](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Write argument buffers in Metal 3 — [5:38]

```objectivec
// Write argument buffers in Metal 3

struct Mesh
{
   uint64_t normals; // 64-bit uint for constant packed_float3*
};

NSUInteger meshArgumentSize = sizeof(struct Mesh);

id<MTLBuffer> meshArgumentBuffer = [device newBufferWithLength:meshArgumentSize
                                                       options:storageMode];

struct Mesh* meshes = (struct Mesh *)(meshArgumentBuffer.contents); 

meshes->normals = normalBuffer.gpuAddress + normalBufferOffset;
```

### // Shader struct: — [6:31]

```objectivec
// Shader struct:

struct Mesh
{
   constant packed_float3* normals;
};

// Host-side struct:

struct Mesh
{
    uint64_t normals;
};
```

### Shared struct: — [6:53]

```objectivec
// Shared struct:

#if __METAL_VERSION__
#define CONSTANT_PTR(x) constant x*
#else
#define CONSTANT_PTR(x) uint64_t
#endif

struct Mesh
{
    CONSTANT_PTR(packed_float3) normals;
};
```

### Write unbounded arrays of resources in Metal 3 — [7:53]

```objectivec
// Write unbounded arrays of resources in Metal 3

struct Mesh
{
   uint64_t normals; // 64-bit uint for constant packed_float3*
};

NSUInteger meshArgumentSize = sizeof(struct Mesh) * meshes.count;

id<MTLBuffer> meshArgumentBuffer = [device newBufferWithLength:meshArgumentSize
                                                        options:storageMode];

struct Mesh* meshes = (struct Mesh *)(meshArgumentBuffer.contents); 

for ( NSUInteger i = 0; i < meshes.count; ++i )
{
   meshes[i].normals = normalBuffers[i].gpuAddress + normalBufferOffsets[i];
}
```

### Metal shading language: unbounded arrays option 1 — [9:03]

```objectivec
// Metal shading language:

struct Mesh
{
   constant packed_float3* normals;
};


fragment half4 fragmentShader(ColorInOut v          [[stage_in]],
                              constant Mesh* meshes [[buffer(0)]] )
{
    /* determine mesh to read, e.g. geometry_id */

    packed_float3 n0 = meshes[ geometry_id ].normals[0];
    packed_float3 n1 = meshes[ geometry_id ].normals[1];
    packed_float3 n2 = meshes[ geometry_id ].normals[2];

    /* interpolate normals and calculate shading */
}
```

### Metal shading language: unbounded arrays option 2 — [9:25]

```objectivec
// Metal shading language:
struct Mesh
{
   constant packed_float3* normals;
};

struct Scene
{
   constant Mesh*     meshes;     // mesh array
   constant Material* materials;  // material array
};

fragment half4 fragmentShader(ColorInOut v          [[stage_in]],
                              constant Scene& scene [[buffer(0)]] )
{
    /* determine mesh to read, e.g. geometry_id */
    packed_float3 n0 = scene.meshes[ geometry_id ].normals[0];
    packed_float3 n1 = scene.meshes[ geometry_id ].normals[1];
    packed_float3 n2 = scene.meshes[ geometry_id ].normals[2];
    /* interpolate normals and calculate shading */
}
```

### Size and alignment for MTLAccelerationStructure in a MTLHeap — [11:00]

```objectivec
heapAccelerationStructureSizeAndAlignWithDescriptor:
```

### Store individual indirect resources in NSMutableSet — [13:49]

```objectivec
// Argument buffer loading
for (NSUInteger i = 0; i < mesh.submeshes.count; ++i) {

    Submesh*      submesh     = mesh.submeshes[i];
    id<MTLBuffer> indexBuffer = submesh.indexBuffer;
    NSArray*      textures    = submesh.textures;

    // Copy index buffer into argument buffer
   submeshAB[i].indices = indexBuffer.gpuAddress;

    // Copy material textures into argument buffer
   for (NSUInteger m = 0; m < textures.count; ++m) {
        submeshAB[i].textures[m] = textures[m].gpuResourceID;
    }

    // Remember indirect resources
    [sceneResources addObject:indexBuffer];
    [sceneResources addObjectsFromArray:textures];
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10101/4/E7651C9D-CAC8-44A9-9BF8-8D0DC317F4A2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10101/4/E7651C9D-CAC8-44A9-9BF8-8D0DC317F4A2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10101) — developer.apple.com. Indexed for agent consumption._