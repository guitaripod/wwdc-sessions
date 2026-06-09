---
id: "wwdc2021-10149"
event: "wwdc2021"
year: 2021
title: "Enhance your app with Metal ray tracing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10149"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance your app with Metal ray tracing

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10149](https://developer.apple.com/videos/play/wwdc2021/10149)

Achieve photorealistic 3D scenes in your apps and games through ray tracing, a core part of the Metal graphics framework and Shading Language. We’ll explore the latest improvements in implementing ray tracing and take you through upgrades to the production rendering process. Discover Metal APIs to help you create more detailed scenes, integrate natively-supported content with motion, and more.

**Keywords:** `game dev`, `game developer`, `metal`, `metal shading language`, `metal tools`, `optimization`, `proapps`, `raytracing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,987 words)

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

### Specify intersection functions on render pipeline state — [4:48]

```objectivec
// Create and attach MTLLinkedFunctions object
NSArray <id <MTLFunction>> *functions = @[ sphere, cone, torus ];

MTLLinkedFunctions *linkedFunctions = [MTLLinkedFunctions linkedFunctions];
linkedFunctions.functions = functions;

pipelineDescriptor.fragmentLinkedFunctions = linkedFunctions;

// Create pipeline
id<MTLRenderPipelineState> rayPipeline;
rayPipeline = [device newRenderPipelineStateWithDescriptor:pipelineDescriptor
                                                     error:&error];
```

### Create intersection function table — [5:02]

```objectivec
// Fill out intersection function table descriptor
MTLIntersectionFunctionTableDescriptor *tableDescriptor =
    [MTLIntersectionFunctionTableDescriptor intersectionFunctionTableDescriptor];

tableDescriptor.functionCount = functions.count;

// Create intersection function table
id<MTLIntersectionFunctionTable> table;
table = [rayPipeline newIntersectionFunctionTableWithDescriptor:tableDescriptor
                                                          stage:MTLRenderStageFragment];
```

### Populate intersection function table — [5:14]

```objectivec
id<MTLFunctionHandle> handle;

for (NSUInteger i = 0 ; i < functions.count ; i++) {
    // Get a handle to the linked intersection function in the pipeline state
    handle = [rayPipeline functionHandleWithFunction:functions[i]
                                               stage:MTLRenderStageFragment];

    // Insert the function handle into the table
    [table setFunction:handle atIndex:i];
}
```

### Bind resources — [5:48]

```objectivec
[renderEncoder setFragmentAccelerationStructure:accelerationStructure atBufferIndex:0];
[renderEncoder setFragmentIntersectionFunctionTable:table atBufferIndex:1];
```

### Intersect from fragment shader — [5:57]

```objectivec
[[fragment]]
float4 rayFragmentShader(vertex_output vo [[stage_in]],
                         primitive_acceleration_structure accelerationStructure,
                         intersection_function_table<triangle_data> functionTable,
                         /* ... */)
{
    // generate ray, create intersector...

    intersection = intersector.intersect(ray, accelerationStructure, functionTable);

    // shading...
}
```

### Triangle intersection function — [9:32]

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

### Custom intersection with intersection query — [10:36]

```objectivec
intersection_query<instancing, triangle_data> iq(ray, as, params);

// Step 1: start traversing acceleration structure
while (iq.next())
{
    // Step 2: candidate was found. Check type and run custom intersection.
    switch (iq.get_candidate_intersection_type())
    {
	    case intersection_type::triangle:
	    { 
	       bool alphaTestResult = alphaTest(iq.get_candidate_geometry_id(),
	                                iq.get_candidate_primitive_id(),
	                                iq.get_candidate_triangle_barycentric_coord());
    	   // Step 3: commit candidate or ignore
           if (alphaTestResult) 
               iq.commit_triangle_intersection()
  	  }
    }
}
```

### Custom intersection with intersection query 2 — [10:39]

```objectivec
switch (iq.get_committed_intersection_type())
{
  // Miss case  
  case intersection_type::none:
  {
      missShading();
      break;
  } 

  // Triangle intersection was committed. Query some info and do shading.
  case intersection_type::triangle:
  {
      shadeHitTriangle(iq.get_committed_instance_id(),
                       iq.get_committed_distance(),
                       iq.get_committed_triangle_barycentric_coord());
      break;
  }
}
```

### Specifying user instance IDs — [15:30]

```objectivec
// New instance descriptor type

typedef struct {
    uint32_t userID;
    // Members from MTLAccelerationStructureInstanceDescriptor...
} MTLAccelerationStructureUserIDInstanceDescriptor;

// Specify instance descriptor type through acceleration structure descriptor

accelDesc.instanceDescriptorType = MTLAccelerationStructureInstanceDescriptorTypeUserID;
```

### Retrieving user instance IDs 1 — [15:47]

```objectivec
// Available in intersection functions

[[intersection(bounding_box, instancing)]]
IntersectionResult sphereInstanceIntersectionFunction(unsigned int userID[[user_instance_id]],
                                                      /** other args **/)
{
    // ...
}
```

### Retrieving user instance IDs 2 — [15:58]

```objectivec
// Available from intersection result

intersection_result<instancing> intersection = instanceIntersector.intersect(/* args */);

if (intersection.type != intersection_type::none)
    instanceIndex = intersection.user_instance_id;

// Available from intersection query

intersection_query<instancing> iq(/* args */);

iq.next()

if (iq.get_committed_intersection_type() != intersection_type::none)
    instanceIndex = iq.get_committed_user_instance_id();
```

### Instance transforms — [16:36]

```objectivec
// Available in intersection functions

[[intersection(bounding_box, instancing, world_space_data)]]
IntersectionResult intersectionFunction(float4x3 objToWorld [[object_to_world_transform]],
                                        float4x3 worldToObj [[world_to_object_transform]],
                                        /** other args **/)
{
    // ...
}
```

### Instance transforms 2 — [16:51]

```objectivec
// Available from intersection result

intersection_result<instancing, world_space_data> result = 
    intersector.intersect(/* args */);

if (result.type != intersection_type::none) {
    output.myObjectToWorldTransform = result.object_to_world_transform;
    output.myWorldToObjectTransform = result.world_to_object_transform;
}
```

### Instance transforms 3 — [17:03]

```objectivec
// Available from intersection query

intersection_query<instancing> iq(/* args */);

iq.next()

if(iq.get_committed_intersection_type() != intersection_type::none){
    output.myObjectToWorldTransform = iq.get_committed_object_to_world_transform();
    output.myWorldToObjectTransform = iq.get_committed_world_to_object_transform();
}
```

### Extended limits — [19:17]

```objectivec
// Specify through acceleration structure descriptor

accelDesc.usage = MTLAccelerationStructureUsageExtendedLimits;

// Specify intersector tag

intersector<extended_limits> extendedIntersector;
```

### Sampling time — [22:30]

```objectivec
// Randomly sample time

float time = random(exposure_start, exposure_end);

result = intersector.intersect(ray, acceleration_structure, time);
```

### Motion instance descriptor — [25:54]

```objectivec
descriptor = [MTLInstanceAccelerationStructureDescriptor new];

descriptor.instanceDescriptorType = MTLAccelerationStructureInstanceDescriptorTypeMotion;

// Buffer containing motion instance descriptors
descriptor.instanceDescriptorBuffer = instanceBuffer;
descriptor.instanceCount = instanceCount;

// Buffer containing MTLPackedFloat4x3 transformation matrices
descriptor.motionTransformBuffer = transformsBuffer;
descriptor.motionTransformCount = transformCount;

descriptor.instancedAccelerationStructures = primitiveAccelerationStructures;
```

### Instance motion — [26:33]

```objectivec
// Specify intersector tag

kernel void raytracingKernel(acceleration_structure<instancing, instance_motion> as,
                             /* other args */)
{
    intersector<instancing, instance_motion> intersector;

    // ...
}
```

### Primitive motion 1 — [27:24]

```objectivec
// Collect keyframe vertex buffers

NSMutableArray<MTLMotionKeyframeData*> *vertexBuffers = [NSMutableArray new];

for (NSUInteger i = 0 ; i < keyframeBuffers.count ; i++) {
    MTLMotionKeyframeData *keyframeData = [MTLMotionKeyframeData data];

    keyframeData.buffer = keyframeBuffers[i];

    [vertexBuffers addObject:keyframeData];
}
```

### Primitive motion 2 — [27:39]

```objectivec
// Create motion geometry descriptor

MTLAccelerationStructureMotionTriangleGeometryDescriptor *geometryDescriptor =
    [MTLAccelerationStructureMotionTriangleGeometryDescriptor descriptor];

geometryDescriptor.vertexBuffers = vertexBuffers;
geometryDescriptor.triangleCount = triangleCount;
```

### Primitive motion 3 — [27:57]

```objectivec
// Create acceleration structure descriptor

MTLPrimitiveAccelerationStructureDescriptor *primitiveDescriptor =
    [MTLPrimitiveAccelerationStructureDescriptor descriptor];

primitiveDescriptor.geometryDescriptors = @[ geometryDescriptor ];

primitiveDescriptor.motionKeyframeCount = keyframeCount;
```

### Primitive motion 4 — [28:10]

```objectivec
// Specify intersector tag

kernel void raytracingKernel(acceleration_structure<primitive_motion> as,
                             /* other args */)
{
    intersector<primitive_motion> intersector;

    // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10149/7/C01A5359-2EAC-411E-99A5-8D7DA9C8220B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10149/7/C01A5359-2EAC-411E-99A5-8D7DA9C8220B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10149) — developer.apple.com. Indexed for agent consumption._
