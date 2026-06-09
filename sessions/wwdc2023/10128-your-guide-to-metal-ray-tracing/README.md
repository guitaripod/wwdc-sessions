---
id: "wwdc2023-10128"
event: "wwdc2023"
year: 2023
title: "Your guide to Metal ray tracing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10128"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Your guide to Metal ray tracing

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10128](https://developer.apple.com/videos/play/wwdc2023/10128)

Discover how you can enhance the visual quality of your games and apps with Metal ray tracing. We’ll take you through the fundamentals of the Metal ray tracing API. Explore the latest enhancements and techniques that will enable you to create larger and more complex scenes, reduce memory usage and build times, and efficiently render visual content like hair and fur.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,498 words)

## Documentation & Resources

- [Rendering reflections in real time using ray tracing](https://developer.apple.com/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing.json
- [Accelerating ray tracing using Metal](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
- [Metal for Accelerating Ray Tracing](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json

## Code Snippets

### Create triangle geometry descriptor — [3:06]

```swift
// Create geometry descriptor:
let geometryDescriptor = MTLAccelerationStructureTriangleGeometryDescriptor()

geometryDescriptor.vertexBuffer = vertexBuffer
geometryDescriptor.indexBuffer = indexBuffer
geometryDescriptor.triangleCount = triangleCount
```

### Create bounding box geometry descriptor — [3:20]

```swift
// Create geometry descriptor:
let geometryDescriptor = MTLAccelerationStructureBoundingBoxGeometryDescriptor()

geometryDescriptor.boundingBoxBuffer = boundingBoxBuffer
geometryDescriptor.boundingBoxCount = boundingBoxCount
```

### Create curve geometry descriptor — [6:42]

```swift
let geometryDescriptor = MTLAccelerationStructureCurveGeometryDescriptor()

geometryDescriptor.controlPointBuffer = controlPointBuffer
geometryDescriptor.radiusBuffer = radiusBuffer
geometryDescriptor.indexBuffer = indexBuffer

geometryDescriptor.controlPointCount = controlPointCount
geometryDescriptor.segmentCount = segmentCount
geometryDescriptor.curveType = .round
geometryDescriptor.curveBasis = .bezier
geometryDescriptor.segmentControlPointCount = 4
```

### Create primitive acceleration structure descriptor — [7:29]

```swift
// Create acceleration structure descriptor
let accelerationStructureDescriptor = MTLPrimitiveAccelerationStructureDescriptor()

// Add geometry descriptor to acceleration structure descriptor
accelerationStructureDescriptor.geometryDescriptors = [ geometryDescriptor ]
```

### Query for acceleration size and alignment requirements — [8:08]

```swift
// Query for acceleration structure sizes
let sizes: MTLAccelerationStructureSizes
sizes = device.accelerationStructureSizes(descriptor: accelerationStructureDescriptor)

// Query for size and alignment requirement in a heap
let heapSize: MTLSizeAndAlign
heapSize = device.heapAccelerationStructureSizeAndAlign(size: sizes.accelerationStructureSize)
```

### Allocate acceleration structure and scratch buffer — [8:39]

```swift
// Allocate acceleration structure from heap
var accelerationStructure: MTLAccelerationStructure!
accelerationStructure = heap.makeAccelerationStructure(size: heapSize.size)

// Allocate scratch buffer
let scratchBuffer = device.makeBuffer(length: sizes.buildScratchBufferSize,
                                      options: .storageModePrivate)!
```

### Encode the acceleration structure build — [8:40]

```swift
let commandEncoder = commandBuffer.makeAccelerationStructureCommandEncoder()!

commandEncoder.build(accelerationStructure: accelerationStructure,
                     descriptor: accelerationStructureDescriptor,
                     scratchBuffer: scratchBuffer,
                     scratchBufferOffset: 0)

commandEncoder.endEncoding()
```

### Create instance acceleration structure descriptor — [11:30]

```swift
var instanceASDesc = MTLInstanceAccelerationStructureDescriptor()

instanceASDesc.instanceCount = ...
instanceASDesc.instancedAccelerationStructures = [ mountainAS, treeAS, ... ]
instanceASDesc.instanceDescriptorType = .userID
```

### Allocate the instance descriptor buffer — [12:07]

```swift
let size = MemoryLayout<MTLAccelerationStructureUserIDInstanceDescriptor>.stride
let instanceDescriptorBufferSize = size * instanceASDesc.instanceCount

let instanceDescriptorBuffer = device.makeBuffer(length: instanceDescriptorBufferSize,
                                                 options: .storageModeShared)!

instanceASDesc.instanceDescriptorBuffer = instanceDescriptorBuffer
```

### Populate instance descriptors — [12:33]

```swift
var instanceDesc = MTLAccelerationStructureUserIDInstanceDescriptor()

instanceDesc.accelerationStructureIndex = 0    // index into instancedAccelerationStructures
instanceDesc.transformationMatrix = ...
instanceDesc.mask = 0xFFFFFFFF
```

### Configure indirect instance acceleration structure descriptor — [14:06]

```swift
var instanceASDesc = MTLIndirectInstanceAccelerationStructureDescriptor()

instanceASDesc.instanceDescriptorType = .indirect
instanceASDesc.maxInstanceCount = ...
instanceASDesc.instanceCountBuffer = ...
instanceASDesc.instanceDescriptorBuffer = ...
```

### Populate indirect instance descriptor — [14:29]

```cpp
device MTLIndirectAccelerationStructureInstanceDescriptor *instance_buffer = ...;
// ...
acceleration_structure<> as = ...;
instance_buffer[i].accelerationStructureID = as;
instance_buffer[i].transformationMatrix[0] = ...;
instance_buffer[i].transformationMatrix[1] = ...;
instance_buffer[i].transformationMatrix[2] = ...;
instance_buffer[i].transformationMatrix[3] = ...;
instance_buffer[i].mask = 0xFFFFFFFF;
```

### Update geometry using refitting — [19:22]

```swift
// Allocate scratch buffer
let scratchBuffer = device.makeBuffer(length: sizes.refitScratchBufferSize,
                                      options: .storageModePrivate)!

// Create command buffer/encoder ...

// Refit acceleration structure
commandEncoder.refit(sourceAccelerationStructure: accelerationStructure,
                     descriptor: asDescriptor,
                     destinationAccelerationStructure: accelerationStructure,
                     scratchBuffer: scratchBuffer,
                     scratchBufferOffset: 0)
```

### Use compaction to reclaim memory — [20:24]

```swift
// Use compaction to reclaim memory

// Create command buffer/encoder ...

sizeCommandEncoder.writeCompactedSize(accelerationStructure: accelerationStructure,
                                      buffer: sizeBuffer,
                                      offset: 0,
                                      sizeDataType: .ulong)

// endEncoding(), commit command buffer and wait until completed ...

// Allocate new acceleration structure using UInt64 from sizeBuffer ...

compactCommandEncoder.copyAndCompact(sourceAccelerationStructure: accelerationStructure,
                             destinationAccelerationStructure: compactedAccelerationStructure)
```

### Set acceleration structure on the command encoder — [21:36]

```swift
encoder.setAccelerationStructure(primitiveAccelerationStructure, bufferIndex:0)
```

### Intersect rays with primitive acceleration structure — [21:48]

```cpp
// Intersect rays with a primitive acceleration structure

[[kernel]]
void trace_rays(acceleration_structure<> as, /* ... */) {
  intersector<> i;

  ray r(origin, direction);

  intersection_result<> result = i.intersect(r, as);

  if (result.type == intersection_type::triangle) {
    float distance = result.distance;


    // shade triangle...
  }
}
```

### Use triangle_data tag to get triangle barycentric coordinates — [22:24]

```cpp
// Intersect rays with a primitive acceleration structure

[[kernel]]
void trace_rays(acceleration_structure<> as, /* ... */) {
  intersector<triangle_data> i;

  ray r(origin, direction);

  intersection_result<triangle_data> result = i.intersect(r, as);

  if (result.type == intersection_type::triangle) {
    float distance = result.distance;
    float2 coords = result.triangle_barycentric_coord;

    // shade triangle...
  }
}
```

### Set instance acceleration structure on the command encoder — [22:51]

```swift
encoder.setAccelerationStructure(instanceAccelerationStructure, bufferIndex:0)
encoder.useHeap(accelerationStructureHeap);
```

### Intersect rays with instance acceleration structure — [23:07]

```cpp
// Intersect rays with an instance acceleration structure

[[kernel]]
void trace_rays(acceleration_structure<instancing> as, /* ... */) {
  intersector<instancing, max_levels<3>> i;

  ray r(origin, direction);

  intersection_result<instancing, max_levels<3>> result = i.intersect(r, as);

  if (result.type == intersection_type::triangle) {
    float distance = result.distance;

    // shade triangle...
  }
}
```

### Find intersected instance information in the intersection result — [24:43]

```cpp
// Intersect rays with an instance acceleration structure

[[kernel]]
void trace_rays(acceleration_structure<instancing> as, /* ... */) {
  intersector<instancing, max_levels<3>> i;

  ray r(origin, direction);

  intersection_result<instancing, max_levels<3>> result = i.intersect(r, as);

  if (result.type == intersection_type::triangle) {
    float distance = result.distance;
    for (uint i = 0; i < result.instance_count; ++i) {
      uint id = result.instance_id[i];
      // ...
    }
    // shade triangle...
  }
}
```

### Intersect rays with curve primitives — [25:02]

```cpp
// Intersect rays with curve primitives

[[kernel]]
void trace_rays(acceleration_structure<> as, /* ... */) {
  intersector<> i;

  i.assume_geometry_type(geometry_type::curve | geometry_type::triangle);

  ray r(origin, direction);

  intersection_result<> result = i.intersect(r, as);

  if (result.type == intersection_type::curve) {
    float distance = result.distance;
    // shade curve...
  }
}
```

### Find curve parameter in the intersection result — [25:26]

```cpp
// Intersect rays with curve primitives

[[kernel]]
void trace_rays(acceleration_structure<> as, /* ... */) {
  intersector<curve_data> i;

  i.assume_geometry_type(geometry_type::curve | geometry_type::triangle);

  ray r(origin, direction);

  intersection_result<curve_data> result = i.intersect(r, as);

  if (result.type == intersection_type::curve) {
    float distance = result.distance;
    float param = result.curve_parameter;
    // shade curve...
  }
}
```

### Set geometry type on the intersector for better performance — [26:04]

```cpp
// Intersect rays with curve primitives

[[kernel]]
void trace_rays(acceleration_structure<> as, /* ... */) {
  intersector<curve_data> i;

  i.assume_geometry_type(geometry_type::curve | geometry_type::triangle);
  i.assume_curve_type(curve_type::round);
  i.assume_curve_basis(curve_basis::bezier);
  i.assume_curve_control_point_count(3);

  ray r(origin, direction);

  intersection_result<curve_data> result = i.intersect(r, as);

  if (result.type == intersection_type::curve) {
    float distance = result.distance;
    float param = result.curve_parameter;
    // shade curve...
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10128/5/D57CE53D-520E-44FB-99BA-4E63AA58C47C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10128/5/D57CE53D-520E-44FB-99BA-4E63AA58C47C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10128) — developer.apple.com. Indexed for agent consumption._
