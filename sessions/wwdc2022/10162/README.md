---
id: "wwdc2022-10162"
event: "wwdc2022"
year: 2022
title: "Transform your geometry with Metal mesh shaders"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10162"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Transform your geometry with Metal mesh shaders

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10162](https://developer.apple.com/videos/play/wwdc2022/10162)

Meet Metal mesh shaders — a modern and flexible pipeline in Metal for GPU-driven geometry creation and processing. We'll explore how this API can improve and add flexibility to your render pipeline, and share some of the opportunities that GPU-driven work can create. Discover how you can create procedural geometry — like hair rendering — on the GPU using mesh shaders, and build single render passes without additional compute passes or intermediate buffers. We'll also show you how to improve scene processing and rendering through GPU-driven meshlet culling.

**Keywords:** `3d graphics`, `game dev`, `game developer`, `mesh shaders`, `metal`, `metal 3`, `metal shading language`, `metal tools`, `proapps`, `procedural geometry`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,695 words)

## Documentation & Resources

- [Adjusting the level of detail using Metal mesh shaders](https://developer.apple.com/documentation/Metal/adjusting-the-level-of-detail-using-metal-mesh-shaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/adjusting-the-level-of-detail-using-metal-mesh-shaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/adjusting-the-level-of-detail-using-metal-mesh-shaders.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Object shader (MSL) — [8:13]

```cpp
[[object]] 
void objectShader(object_data CurvePayload *payloadOutput [[payload]],
                             const device void *inputData [[buffer(0)]], 
                             uint hairID [[thread_index_in_threadgroup]],
                             uint triangleID [[threadgroup_position_in_grid]],
                             mesh_grid_properties mgp)
{
    if (hairID < kHairsPerBlock)
       payloadOutput[hairID] = generateCurveData(inputData, hairID, triangleID);
    if (hairID == 0)
       mgp.set_threadgroups_per_grid(uint3(kHairPerBlockX, kHairPerBlockY, 1));
}
```

### Initializing object stage — [8:35]

```swift
let meshPipelineDescriptor = MTLMeshRenderPipelineDescriptor()
meshPipelineDescriptor.objectFunction = objectFunction
meshPipelineDescriptor.payloadMemoryLength = payloadLength
meshPipelineDescriptor.maxTotalThreadsPerObjectThreadgroup = hairsPerBlock
```

### Defining a Metal Mesh — [9:26]

```cpp
struct VertexData    { float4 position [[position]]; };
struct PrimitiveData { float4 color; };

using triangle_mesh_t = metal::mesh<
                                    VertexData,               // Vertex type
                                    PrimitiveData,            // Primitive type
                                    10,                       // Maximum vertices
                                    6,                        // Maximum primitives
                                    metal::topology::triangle // Topology
>;

[[mesh]] 
void myMeshShader(triangle_mesh_t outputMesh, ...);
```

### Mesh Shader (MSL) — [11:16]

```cpp
[[mesh]] void myMeshShader(triangle_mesh_t outputMesh,
                         uint tid [[thread_index_in_threadgroup]])
{

    if (tid < kVertexCount) 
        outputMesh.set_vertex(tid, calculateVertex(tid));

    if (tid < kIndexCount) 
        outputMesh.set_index(tid, calculateIndex(tid));

    if (tid < kPrimitiveCount)
        outputMesh.set_primitive(tid, calculatePrimitive(tid));

if (tid == 0)
    outputMesh.set_primitive_count(kPrimitiveCount);

}
```

### Initializing the mesh stage — [11:35]

```swift
meshPipelineDescriptor.meshFunction = meshFunction
meshPipelineDescriptor.maxTotalThreadsPerMeshThreadgroup = vertexCountPerHair
```

### Initializing the fragment stage — [12:08]

```swift
meshPipelineDescriptor.maxTotalThreadsPerMeshThreadgroup = vertexCountPerHair
```

### Creating a mesh render pipeline — [12:14]

```swift
/// A mesh pipeline state the device creates from a mesh render pipeline descriptor.
let meshPipeline: MTLRenderPipelineState

do {
    /// A tuple of the mesh pipeline and its reflection information, if applicable.
    let (pipeline, reflection) = try device.makeRenderPipelineState(descriptor: meshRenderPipelineDescriptor,
                                                                    options: [])
    meshPipeline = pipeline
} catch {
    print("The device can't create a mesh pipeline state: \(error)")
    return
}
```

### Encoding a mesh pipeline — [12:25]

```swift
// Create a encoder for a render pass from the command buffer.
let encoder: MTLRenderCommandEncoder!
encoder = commandBuffer.makeRenderCommandEncoder(descriptor: descriptor)

// Apply the mesh pipeline to the render pass.
encoder.setRenderPipelineState(meshPipeline)

// Bind the resources for the render pass.
encoder.setObjectBuffer(objectBuffer, offset: 0, index: 0)
encoder.setMeshTexture(meshTexture, index: 2)
encoder.setFragmentBuffer(fragmentBuffer, offset: 0, index: 0)

// Create the size instances for the mesh threadgroups.
let objectGridDimensions = MTLSize(width: trianglesPerModel, height: 1, depth: 1)
let threadsPerObject = MTLSize(width: hairsPerBlock, height: 1, depth: 1)
let threadsPerMesh = MTLSize(width: threadsPerHair, height: 1, depth: 1)

// Encode the draw command for the render pass.
encoder.drawMeshThreadgroups(objectGridDimensions,
                             threadsPerObjectThreadgroup: threadsPerObject,
                             threadsPerMeshThreadgroup: threadsPerMesh)

// Finish encoding the render pass.
encoder.endEncoding()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10162/5/9408DC15-0B03-4DD9-8ADE-161821D0E7FC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10162/5/9408DC15-0B03-4DD9-8ADE-161821D0E7FC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10162) — developer.apple.com. Indexed for agent consumption._