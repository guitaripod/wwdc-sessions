---
id: "wwdc2020-10012"
event: "wwdc2020"
year: 2020
title: "Discover ray tracing with Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10012"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Discover ray tracing with Metal

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10012](https://developer.apple.com/videos/play/wwdc2020/10012)

Achieve photorealistic 3D scenes in your apps and games through ray tracing — a core part of the Metal graphics framework and Shading Language. Discover the fundamentals of the Metal ray tracing API and Shading Language extensions for ray tracing, find out how to use them in your graphics apps and games, and learn how to take control of your kernels and combine them into a single compute kernel for optimal performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,627 words)

## Documentation & Resources

- [Accelerating ray tracing using Metal](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
- [Modern rendering with Metal](https://developer.apple.com/documentation/Metal/modern-rendering-with-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/modern-rendering-with-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/modern-rendering-with-metal.json
- [Accelerating ray tracing and motion blur using Metal](https://developer.apple.com/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal.json
- [Debugging the shaders within a draw command or compute dispatch](https://developer.apple.com/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch.json
- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/Metal-Feature-Set-Tables.pdf
- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Ray tracing with Metal — [2:42]

```objectivec
[[kernel]]
void rtKernel(primitive_acceleration_structure accelerationStructure [[buffer(0)]],
              /* ... */)
{
    // Generate ray
    ray r = generateCameraRay(tid);

    // Create an intersector
    intersector<triangle_data> intersector;

    // Intersect with scene
    intersection_result<triangle_data> intersection;

    intersection = intersector.intersect(r, accelerationStructure);

    // shading...
}
```

### Create an acceleration structure descriptor — [4:48]

```swift
let accelerationStructureDescriptor = MTLPrimitiveAccelerationStructureDescriptor()

// Create geometry descriptor(s)
let geometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()

geometryDescriptor.vertexBuffer = vertexBuffer
geometryDescriptor.triangleCount = triangleCount

accelerationStructureDescriptor.geometryDescriptors = [ geometryDescriptor ]
```

### Allocate acceleration storage — [5:46]

```swift
// Query for acceleration structure sizes
let sizes = device.accelerationStructureSizes(descriptor: accelerationStructureDescriptor)

// Allocate acceleration structure
let accelerationStructure =
    device.makeAccelerationStructure(size: sizes.accelerationStructureSize)!

// Allocate scratch buffer
let scratchBuffer = device.makeBuffer(length: sizes.buildScratchBufferSize,
                                      options: .storageModePrivate)!
```

### Build acceleration structure — [6:24]

```swift
// Create command buffer/encoder
let commandBuffer = commandQueue.makeCommandBuffer()!
let commandEncoder = commandBuffer.makeAccelerationStructureCommandEncoder()!

// Encode acceleration structure build
commandEncoder.build(accelerationStructure: accelerationStructure,
                     descriptor: accelerationStructureDescriptor,
                     scratchBuffer: scratchBuffer,
                     scratchBufferOffset: 0)

// Commit command buffer
commandEncoder.endEncoding()
commandBuffer.commit()
```

### Pass acceleration structure to ray intersector — [7:15]

```objectivec
[[kernel]]
void rtKernel(primitive_acceleration_structure accelerationStructure [[buffer(0)]],
              /* ... */)
{
    // generate ray, create intersector...

    intersection = intersector.intersect(r, accelerationStructure);

    // shading...
}
```

### Bind acceleration structure with compute command encoder — [7:25]

```swift
computeEncoder.setAccelerationStructure(accelerationStructure, bufferIndex: 0)
```

### Triangle intersection functions — [12:16]

```objectivec
[[intersection(triangle, triangle_data)]]
bool alphaTestIntersectionFunction(uint primitiveIndex        [[primitive_id]],
                                   uint geometryIndex         [[geometry_id]],
                                   float2 barycentricCoords   [[barycentric_coord]],
                                   device Material *materials [[buffer(0)]])
{
    texture2d<float> alphaTexture = materials[geometryIndex].alphaTexture;

    float2 UV = interpolateUVs(materials[geometryIndex].UVs,
        primitiveIndex, barycentricCoords);

    float alpha = alphaTexture.sample(sampler, UV).x;

    return alpha > 0.5f;
}
```

### Creating a bounding box acceleration structure — [14:38]

```swift
// Create a primitive acceleration structure descriptor
let accelerationStructureDescriptor = MTLPrimitiveAccelerationStructureDescriptor()

// Create one or more bounding box geometry descriptors:
let geometryDescriptor = MTLAccelerationStructureBoundingBoxGeometryDescriptor()

geometryDescriptor.boundingBoxBuffer = boundingBoxBuffer
geometryDescriptor.boundingBoxCount = boundingBoxCount

accelerationStructureDescriptor.geometryDescriptors = [ geometryDescriptor ]
```

### Bounding Box Result — [15:29]

```objectivec
struct BoundingBoxResult {
    bool accept [[accept_intersection]];
    float distance [[distance]];
};
```

### Bounding box intersection functions — [15:38]

```objectivec
[[intersection(bounding_box)]]
BoundingBoxResult sphereIntersectionFunction(float3 origin            [[origin]],
                                             float3 direction         [[direction]],
                                             float minDistance        [[min_distance]],
                                             float maxDistance        [[max_distance]],
                                             uint primitiveIndex      [[primitive_id]],
                                             device Sphere *spheres   [[buffer(0)]])
{
    float distance;

    if (!intersectRaySphere(origin, direction, spheres[primitiveIndex], &distance))
        return { false, 0.0f };

    if (distance < minDistance || distance > maxDistance)
        return { false, 0.0f };

    return { true, distance };
}
```

### Ray payload — [16:20]

```objectivec
[[intersection(bounding_box)]]
BoundingBoxResult sphereIntersectionFunction(/* ... */,
                                             ray_data float3 & normal [[payload]])
{
    // ...

    if (distance < minDistance || distance > maxDistance)
        return { false, 0.0f };

    float3 intersectionPoint = origin + direction * distance;
    normal = normalize(intersectionPoint - spheres[primitiveIndex].origin);

    return { true, distance };
}
```

### Ray payload 2 — [16:48]

```objectivec
[[kernel]]
void rtKernel(/* ... */)
{
    // generate ray, create intersector...

  float3 normal;

    intersection = intersector.intersect(r, accelerationStructure, functionTable, normal);

    // shading...
}
```

### Linking intersection functions — [17:18]

```swift
// Load functions from Metal library
let sphereIntersectionFunction = library.makeFunction(name: “sphereIntersectionFunction”)!
// other functions...

// Attach functions to ray tracing compute pipeline descriptor
let linkedFunctions = MTLLinkedFunctions()

linkedFunctions.functions = [ sphereIntersectionFunction, alphaTestFunction, ... ]

computePipelineDescriptor.linkedFunctions = linkedFunctions

// Compile and link ray tracing compute pipeline
let computePipeline = try device.makeComputePipeline(descriptor: computePipelineDescriptor,
                                                     options: [],
                                                     reflection: nil)
```

### Intersection function table offsets — [18:17]

```swift
class MTLAccelerationStructureGeometryDescriptor : NSObject {

    var intersectionFunctionTableOffset: Int

// ...

}

struct MTLAccelerationStructureInstanceDescriptor {
    var intersectionFunctionTableOffset: UInt32
    // ...
};
```

### Creating an intersection function table — [18:35]

```swift
// Allocate intersection function table
let descriptor = MTLIntersectionFunctionTableDescriptor()

descriptor.functionCount = intersectionFunctions.count

let functionTable = computePipeline.makeIntersectionFunctionTable(descriptor: descriptor)

for i in 0 ..< intersectionFunctions.count {
    // Get a handle to the linked intersection function in the pipeline state
    let functionHandle = computePipeline.functionHandle(function: intersectionFunctions[i])

    // Insert the function handle into the table
    functionTable.setFunction(functionHandle, index: i)
}

// Bind intersection function resources
functionTable.setBuffer(sphereBuffer, offset: 0, index: 0)
```

### Pass intersection function table to ray intersector — [19:26]

```objectivec
[[kernel]]
void rtKernel(primitive_acceleration_structure accelerationStructure   [[buffer(0)]],
              intersection_function_table<triangle_data> functionTable [[buffer(1)]],
              /* ... */)
{
    // generate ray, create intersector...

    intersection = intersector.intersect(r, accelerationStructure, functionTable);

    // shading...
}
```

### Bind intersection function table with compute command encoder — [19:33]

```swift
encoder.setIntersectionFunctionTable(functionTable, bufferIndex: 1)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10012/5/C35EF7F6-AAB8-4A37-9F4D-21E5ABC1C26A/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10012) — developer.apple.com. Indexed for agent consumption._
