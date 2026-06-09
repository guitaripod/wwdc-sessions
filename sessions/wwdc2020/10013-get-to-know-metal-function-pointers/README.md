---
id: "wwdc2020-10013"
event: "wwdc2020"
year: 2020
title: "Get to know Metal function pointers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10013"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Get to know Metal function pointers

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10013](https://developer.apple.com/videos/play/wwdc2020/10013)

Metal is a low-level, low-overhead hardware-accelerated graphics framework and shader application programming interface for producing stunning visual effects in applications. Discover how to make your shaders written in Metal Shading Language more programmable and extensible by using function pointers. Learn how to take advantage of this new feature for dynamic flow control in Metal shaders. Discover how to use function pointers to specify custom intersection functions in your ray tracing application. We’ll explain how function pointers allow several compilations models so you can balance GPU pipeline size against runtime performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,169 words)

## Documentation & Resources

- [Modern rendering with Metal](https://developer.apple.com/documentation/Metal/modern-rendering-with-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/modern-rendering-with-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/modern-rendering-with-metal.json
- [Accelerating ray tracing and motion blur using Metal](https://developer.apple.com/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal.json
- [Metal for Accelerating Ray Tracing](https://developer.apple.com/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/metal/metal_sample_code_library/accelerating_ray_tracing_using_metal.json
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

### Our simple Path Tracer in Metal Shading Language: — [3:09]

```objectivec
float3 shade(...);

[[kernel]] void rtKernel(...
                         device Material *materials,
                         constant Light &light)
{
    // ...

    device Material &material = materials[intersection.geometry_id];
    float3 result = shade(ray, triangleIntersectionData, material, light);

    // ...
}
```

### Our shading function — [3:30]

```objectivec
float3 shade(...)
{
    Lighting lighting = LightingFromLight(light, triangleIntersectionData);

    return CalculateLightingForMaterial(material, lighting, triangleIntersectionData);
}
```

### Declare a function as visible — [4:59]

```objectivec
[[visible]]
Lighting Area(Light light, TriangleIntersectionData triangleIntersectionData)
{
    Lighting result;

    // Clever math code ...

    return result;
}
```

### Single compilation pipeline on CPU — [5:30]

```swift
// Single compilation configuration
let linkedFunctions = MTLLinkedFunctions()
linkedFunctions.functions = [area, spot, sphere, hair, glass, skin]
computeDescriptor.linkedFunctions = linkedFunctions

// Pipeline creation
let pipeline = try device.makeComputePipelineState(descriptor: computeDescriptor,
                                                   options: [],
                                                   reflection: nil)
```

### Introducing MTLFunctionDescriptor — [7:43]

```swift
// Create by function descriptor:
let functionDescriptor = MTLFunctionDescriptor()
functionDescriptor.name = "Area"
// More configuration goes here
let areaBinaryFunction = try library.makeFunction(descriptor: functionDescriptor)
```

### Binary pre–compilation — [8:08]

```swift
// Create and compile by function descriptor:
let functionDescriptor = MTLFunctionDescriptor()
functionDescriptor.name = "Area"
functionDescriptor.options = MTLFunctionOptions.compileToBinary
let areaBinaryFunction = try library.makeFunction(descriptor: functionDescriptor)
```

### Binary functions — [8:20]

```swift
// Specify binary functions on compute pipeline descriptor
let linkedFunctions = MTLLinkedFunctions()
linkedFunctions.functions = [spot, sphere, hair, glass, skin]
linkedFunctions.binaryFunctions = [areaBinaryFunction]
computeDescriptor.linkedFunctions = linkedFunctions

// Pipeline creation
let pipeline = try device.makeComputePipelineState(descriptor: computeDescriptor,
                                                   options: [],
                                                   reflection: nil)
```

### Incremental compilation pipeline — [11:04]

```swift
// Create initial pipeline with option
computeDescriptor.supportAddingBinaryFunctions = true

// Create and compile by function descriptor
let functionDescriptor = MTLFunctionDescriptor()
functionDescriptor.name = "Wood"
functionDescriptor.options = MTLFunctionOptions.compileToBinary
let wood = try library.makeFunction(descriptor: functionDescriptor)

// Create new pipeline from existing pipeline
let newPipeline =
   try pipeline.makeComputePipelineStateWithAdditionalBinaryFunctions(functions: [wood])
```

### Visible function tables on the GPU — [12:22]

```objectivec
// Helper using declaration in Metal
using LightingFunction = Lighting(Light, TriangleIntersectionData);
using MaterialFunction = float3(Material, Lighting, TriangleIntersectionData);

// Specify tables as kernel parameters
visible_function_table<LightingFunction> lightingFunctions [[buffer(1)]],
visible_function_table<MaterialFunction> materialFunctions [[buffer(2)]],

// Access via index
LightingFunction *lightingFunction = lightingFunctions[light.index];
Lighting lighting = lightingFunction(light, triangleIntersection);
return materialFunctions[material.index](material, lighting, triangleIntersection);
```

### Visible function tables on the CPU — [12:49]

```swift
// Initialize descriptor
let vftDescriptor = MTLVisibleFunctionTableDescriptor()
vftDescriptor.functionCount = 3
let lightingFunctionTable = pipeline.makeVisibleFunctionTable(descriptor: vftDescriptor)!

// Find and set functions by handle
let functionHandle = pipeline.functionHandle(function: spot)!
lightingFunctionTable.setFunction(functionHandle, index:0)

// Find and set functions by handle
computeCommandEncoder.setVisibleFunctionTable(lightingFunctionTable, bufferIndex:1)
argumentEncoder.setVisibleFunctionTable(lightingFunctionTable, index:1)
```

### Function groups on GPU — [14:23]

```objectivec
// Add function groups to our shading function
float3 shade(...)
{
    LightingFunction *lightingFunction = lightingFunctions[light.index];
    [[function_groups("lighting")]] Lighting lighting = lightingFunction(light,
triangleIntersection);

    MaterialFunction *materialFunction = materialFunctions[material.index];
    [[function_groups("material")]] float3 result = materialFunction(material, lighting, triangleIntersection);
    return result;
}
```

### Function groups on CPU — [14:49]

```swift
// Function Group configuration
let linkedFunctions = MTLLinkedFunctions()
linkedFunctions.functions = [area, spot, sphere, hair, glass, skin]
linkedFunctions.groups = ["lighting" : [area, spot, sphere ],
                          "material" : [hair, glass, skin ] ]
computeDescriptor.linkedFunctions = linkedFunctions
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10013/4/17EAECF9-AE48-4108-B8E1-7214F30DC9AC/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10013) — developer.apple.com. Indexed for agent consumption._
