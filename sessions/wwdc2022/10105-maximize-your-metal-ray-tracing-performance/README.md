---
id: "wwdc2022-10105"
event: "wwdc2022"
year: 2022
title: "Maximize your Metal ray tracing performance"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10105"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Maximize your Metal ray tracing performance

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10105](https://developer.apple.com/videos/play/wwdc2022/10105)

Learn how to simplify your ray tracing code and increase performance with the power of Metal 3. We’ll explore the GPU debugging and profiling tools that can help you tune your ray tracing applications. We'll also show you how you can speed up intersection tests and reduce shader code memory accesses and indirections with per-primitive data in an acceleration structure. And we'll help you implement faster acceleration structure builds and refits to reduce load times and per-frame overhead.

**Keywords:** `game dev`, `game developer`, `metal`, `metal 3`, `metal shading language`, `metal tools`, `optimization`, `proapps`, `raytracing`, `ray tracing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,840 words)

## Documentation & Resources

- [Accelerating ray tracing using Metal](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Alpha testing with intersection functions — [4:04]

```objectivec
float alpha = texture.sample(sampler, UV).w;
return alpha >= 0.5f;
```

### Alpha testing intersection function — [5:46]

```objectivec
[[intersection(triangle, raytracing::triangle_data, raytracing::instancing)]]
bool alphaTestIntersection(float2               coordinates    [[barycentric_coord]],
                           unsigned int         primitiveIndex [[primitive_id]],
                           unsigned int         instanceIndex  [[instance_id]],
                           device GlobalData   *globalData     [[buffer(1)]],
                           device InstanceData *instanceData   [[buffer(0)]])
{
    device Material *materials = globalData->materials;
    InstanceData instance = instanceData[instanceIndex];
    float2 UV = calculateSamplingCoords(coordinates,
                                        instance.uvs[primitiveIndex * 3 + 0],
                                        instance.uvs[primitiveIndex * 3 + 1],
                                        instance.uvs[primitiveIndex * 3 + 2]);
    int materialIndex = instance.materialIndices[primitiveIndex];
    float alpha = materials[materialIndex].texture.sample(sam, UV).w;
    return alpha >= 0.5f;
}
```

### Primitive Data — [6:48]

```objectivec
struct PrimitiveData
{
    texture2d<float> texture;
    float2 uvs[3];
};
```

### Alpha testing intersection function using per-primitive data — [7:08]

```objectivec
// Alpha testing intersection function
[[intersection(triangle, raytracing::triangle_data, raytracing::instancing)]]
bool alphaTestIntersection(float2               coordinates    [[barycentric_coord]],
                     const device PrimitiveData *primitiveData [[primitive_data]])
{
    PrimitiveData ppd = *primitiveData;
    float2 UV = calculateSamplingCoords(coordinates,
                                        ppd.uvs[0],
                                        ppd.uvs[1],
                                        ppd.uvs[2]);
    float alpha = ppd.texture.sample(sam, UV).w;
    return alpha >= 0.5f;
}
```

### Setting up per-primitive data — [8:54]

```swift
geometryDescriptor.primitiveDataBuffer = primitiveDataBuffer
geometryDescriptor.primitiveDataElementSize = MemoryLayout<PrimitiveData>.size
geometryDescriptor.primitiveDataStride = MemoryLayout<PrimitiveData>.stride
geometryDescriptor.primitiveDataBufferOffset = primitiveDataOffset
```

### Using per-primitive data — [9:18]

```objectivec
// Intersection function argument:
const device void *primitiveData [[primitive_data]]

// Intersection result:
primitiveData = intersection.primitive_data;

// Intersection query:
primitiveData = query.get_candidate_primitive_data();
primitiveData = query.get_committed_primitive_data();
```

### Buffers from intersection function tables — [11:08]

```objectivec
device int *buffer = intersectionFunctionTable.get_buffer<device int *>(index);

visible_function_table<uint(uint)> table =
    intersectionFunctionTable.get_visible_function_table<uint(uint)>(index);

uint result = table[0](parameter);
```

### Ray tracing from indirect command buffers — [11:36]

```swift
let icbDescriptor = MTLIndirectCommandBufferDescriptor()

icbDescriptor.supportRayTracing = true
```

### Parallel acceleration structure builds — [15:43]

```swift
for (index, accelerationStructure) in accelerationStructures.enumerated() {
    encoder.build(accelerationStructure: accelerationStructure,
                  descriptor: descriptors[index],
                  scratchBuffer: scratchBuffers[index % numScratchBuffers],
                  scratchBufferOffset: 0)
}
```

### Setting vertex formats — [17:28]

```swift
let geometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()

geometryDescriptor.vertexFormat = .uint1010102Normalized
```

### Creating transformation matrix buffer — [18:29]

```swift
var scaleTransform =
    MTLPackedFloat4x3(columns: (
        MTLPackedFloat3Make( scale.x,      0.0,      0.0),
        MTLPackedFloat3Make(     0.0,  scale.y,      0.0),
        MTLPackedFloat3Make(     0.0,      0.0,  scale.z),
        MTLPackedFloat3Make(offset.x, offset.y, offset.z))

let transformBuffer = device.makeBuffer(length: MemoryLayout<MTLPackedFloat4x3>.size,
                                        options: .storageModeShared)!

transformBuffer.contents().copyMemory(from: &scaleTransform,
                                      byteCount: MemoryLayout<MTLPackedFloat4x3>.size)
```

### Setting transformation matrix buffer on geometry descriptor — [18:51]

```swift
let geometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()

geometryDescriptor.transformationMatrixBuffer = transformBuffer
geometryDescriptor.transformationMatrixBufferOffset = 0
```

### Merging instances using transformation matrices — [20:12]

```swift
let sphereGeometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()
sphereGeometryDescriptor.vertexBuffer = sphereVertexBuffer
sphereGeometryDescriptor.indexBuffer = sphereIndexBuffer
sphereGeometryDescriptor.transformationMatrixBuffer = sphereTransformBuffer

let redBoxGeometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()
redBoxGeometryDescriptor.vertexBuffer = boxVertexBuffer
redBoxGeometryDescriptor.indexBuffer = boxIndexBuffer
redBoxGeometryDescriptor.transformationMatrixBuffer = redBoxTransformBuffer

let blueBoxGeometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()
blueBoxGeometryDescriptor.vertexBuffer = boxVertexBuffer
blueBoxGeometryDescriptor.indexBuffer = boxIndexBuffer blueBoxGeometryDescriptor.transformationMatrixBuffer = blueBoxTransformBuffer

let primitiveASDescriptor = MTLPrimitiveAccelerationStructureDescriptor()

primitiveASDescriptor.geometryDescriptors =
    [sphereGeometryDescriptor, redBoxGeometryDescriptor, blueBoxGeometryDescriptor]
```

### Heap acceleration structure allocation — [22:33]

```swift
let heap = device.makeHeap(descriptor: heapDescriptor)!

let accelerationStructure = heap.makeAccelerationStructure(descriptor: descriptor)

let sizeAndAlign = device.heapAccelerationStructureSizeAndAlign(descriptor: descriptor)

let accelerationStructure = heap.makeAccelerationStructure(size: sizeAndAlign.size)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10105/7/A0348CEB-F711-422B-9FA4-D1A0E1DB8BF8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10105/7/A0348CEB-F711-422B-9FA4-D1A0E1DB8BF8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10105) — developer.apple.com. Indexed for agent consumption._
