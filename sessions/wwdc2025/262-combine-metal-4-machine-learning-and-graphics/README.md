---
id: "wwdc2025-262"
event: "wwdc2025"
year: 2025
title: "Combine Metal 4 machine learning and graphics"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/262"
topics: ["Graphics & Games", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Combine Metal 4 machine learning and graphics

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-262](https://developer.apple.com/videos/play/wwdc2025/262)

Learn how to seamlessly combine machine learning into your graphics applications using Metal 4. We’ll introduce the tensor resource and ML encoder for running models on the GPU timeline alongside your rendering and compute work. Discover how shader ML lets you embed neural networks directly within your shaders for advanced effects and performance gains. We’ll also show new debugging tools for Metal 4 ML workloads in action using an example app.

**Keywords:** `machine learning`, `metal`, `metal tools`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,281 words)

## Documentation & Resources

- [Customizing a PyTorch operation](https://developer.apple.com/documentation/Metal/customizing-a-pytorch-operation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/customizing-a-pytorch-operation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/customizing-a-pytorch-operation.json
- [Metal Developer Resources](https://developer.apple.com/metal/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/
- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json

## Code Snippets

### Exporting a Core ML package with PyTorch — [8:13]

```python
import coremltools as ct

# define model in PyTorch
# export model to an mlpackage

model_from_export = ct.convert(
    custom_traced_model,
    inputs=[...],
    outputs=[...],
    convert_to='mlprogram',
    minimum_deployment_target=ct.target.macOS16,
)

model_from_export.save('model.mlpackage')
```

### Identifying a network in a Metal package — [9:10]

```objectivec
library = [device newLibraryWithURL:@"myNetwork.mtlpackage"];

functionDescriptor = [MTL4LibraryFunctionDescriptor new]
functionDescriptor.name = @"main";
functionDescriptor.library = library;
```

### Creating a pipeline state — [9:21]

```objectivec
descriptor = [MTL4MachineLearningPipelineDescriptor new];
descriptor.machineLearningFunctionDescriptor = functionDescriptor;

[descriptor setInputDimensions:dimensions
                 atBufferIndex:1];

pipeline = [compiler newMachineLearningPipelineStateWithDescriptor:descriptor
                                                             error:&error];
```

### Dispatching a network — [9:58]

```objectivec
commands = [device newCommandBuffer];
[commands beginCommandBufferWithAllocator:cmdAllocator];
[commands useResidencySet:residencySet];

/* Create intermediate heap */
/* Configure argument table */

encoder = [commands machineLearningCommandEncoder];
[encoder setPipelineState:pipeline];
[encoder setArgumentTable:argTable];
[encoder dispatchNetworkWithIntermediatesHeap:heap];
```

### Creating a heap for intermediate storage — [10:30]

```objectivec
heapDescriptor = [MTLHeapDescriptor new];
heapDescriptor.type = MTLHeapTypePlacement;
heapDescriptor.size = pipeline.intermediatesHeapSize;

heap = [device newHeapWithDescriptor:heapDescriptor];
```

### Submitting commands to the GPU timeline — [10:46]

```objectivec
commands = [device newCommandBuffer];
[commands beginCommandBufferWithAllocator:cmdAllocator];
[commands useResidencySet:residencySet];

/* Create intermediate heap */
/* Configure argument table */

encoder = [commands machineLearningCommandEncoder];
[encoder setPipelineState:pipeline];
[encoder setArgumentTable:argTable];
[encoder dispatchNetworkWithIntermediatesHeap:heap];

[commands endCommandBuffer];
[queue commit:&commands count:1];
```

### Synchronization — [11:18]

```objectivec
[encoder barrierAfterStages:MTLStageMachineLearning
          beforeQueueStages:MTLStageVertex
          visibilityOptions:MTL4VisibilityOptionDevice];
```

### Declaring a fragment shader with tensor inputs — [15:17]

```cpp
// Metal Shading Language 4

#include <metal_tensor>

using namespace metal;

[[fragment]]
float4 shade_frag(tensor<device half, dextents<int, 2>> layer0Weights [[ buffer(0) ]],
                  tensor<device half, dextents<int, 2>> layer1Weights [[ buffer(1) ]],
                  /* other bindings */)
{
    // Creating input tensor
    half inputs[INPUT_WIDTH] = { /* four latent texture samples + UV data */ };

    auto inputTensor = tensor(inputs, extents<int, INPUT_WIDTH, 1>());
    ...
}
```

### Operating on tensors in shaders — [17:12]

```cpp
// Metal Shading Language 4

#include <MetalPerformancePrimitives/MetalPerformancePrimitives.h>

using namespace mpp;

constexpr tensor_ops::matmul2d_descriptor desc(
              /* M, N, K */ 1, HIDDEN_WIDTH, INPUT_WIDTH,
       /* left transpose */ false,
      /* right transpose */ true,
    /* reduced precision */ true);

tensor_ops::matmul2d<desc, execution_thread> op;
op.run(inputTensor, layerN, intermediateN);

for (auto intermediateIndex = 0; intermediateIndex < intermediateN(0); ++intermediateIndex)
{
    intermediateN[intermediateIndex, 0] = max(0.0f, intermediateN[intermediateIndex, 0]);
}
```

### Render using network evaluation — [18:38]

```cpp
half3 baseColor          = half3(outputTensor[0,0], outputTensor[1,0], outputTensor[2,0]);
half3 tangentSpaceNormal = half3(outputTensor[3,0], outputTensor[4,0], outputTensor[5,0]);

half3 worldSpaceNormal = worldSpaceTBN * tangentSpaceNormal;

return baseColor * saturate(dot(worldSpaceNormal, worldSpaceLightDir));
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/262/4/bd3b9963-4a16-4a43-8b3d-e7f17cb31f3c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/262/4/bd3b9963-4a16-4a43-8b3d-e7f17cb31f3c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/262) — developer.apple.com. Indexed for agent consumption._
