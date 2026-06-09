---
id: "wwdc2021-10229"
event: "wwdc2021"
year: 2021
title: "Discover compilation workflows in Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10229"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Discover compilation workflows in Metal

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10229](https://developer.apple.com/videos/play/wwdc2021/10229)

The Metal shading language is a powerful C++ based language that allows apps to render stunning effects while maintaining a flexible shader development pipeline. Discover how to more easily build and extend your render pipelines using Dynamic Libraries and Function Pointers. We’ll also show you how to accelerate your shader compilation at runtime with Binary Function Archives, Function Linking, and Function Stitching.

**Keywords:** `compilation`, `compiler`, `metal`, `metal shading language`, `metal tools`, `performance`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,514 words)

## Documentation & Resources

- [Shader libraries](https://developer.apple.com/documentation/Metal/shader-libraries) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/shader-libraries
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/shader-libraries.json
- [Creating a Metal dynamic library](https://developer.apple.com/documentation/Metal/creating-a-metal-dynamic-library) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/creating-a-metal-dynamic-library
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/creating-a-metal-dynamic-library.json
- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/Metal-Feature-Set-Tables.pdf
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Shading language — [5:38]

```objectivec
// Declare external functions

extern float4 foo(FragmentInput input);
extern float4 bar(FragmentInput input);

// Use functions in shader

fragment float4 main(FragmentInput input [[stage_in]])
{
    switch(condition(input)) 
    {
        case 0: 
            return foo(input);
        case 1:
            return bar(input);
    }
}
```

### Declare and instantiate visible functions — [9:01]

```objectivec
// Declare a descriptor and set CompileToBinary options

MTLFunctionDescriptor* functionDescriptor = [MTLFunctionDescriptor new];
functionDescriptor.options = MTLFunctionOptionCompileToBinary;

// Backend compile the function

functionDescriptor.name = @"foo";
id<MTLFunction> foo = [library newFunctionWithDescriptor:functionDescriptor
```

### Configure pipeline descriptor — [9:30]

```objectivec
// Provide a list of functions that the pipeline stage may call

// AIR functions

renderPipeDesc.fragmentLinkedFunctions.functions = @[foo, bar, baz];

// Binary functions

renderPipeDesc.fragmentLinkedFunctions.binaryFunctions = @[foo, bar, baz];
```

### Create and populate visible function table — [10:47]

```objectivec
// Create visible function table

    [renderPipeline newVisibleFunctionTableWithDescriptor:stage:];

// Create function handles

    [renderPipeline functionHandleWithFunction:stage:];

// Insert handles into table

    [visibleFunctionTable setFunction:atIndex:];
```

### Encoding and calling function pointers — [11:21]

```objectivec
// Bind visible function table objects to each stage

    [renderCommandEncoder setFragmentVisibleFunctionTable:atBufferIndex:];

// Usage in shader

   fragment float4 shaderFunc(FragmentData vo[[stage_in]],
                              visible_function_table<float4(float3)>materials[[buffer(0)]])
   {
   		 //...

       return materials[materialSelector](coord);
   }
```

### Incremental pipeline creation — [12:20]

```objectivec
// Enable incrementally adding binary functions per stage

renderPipeDesc.supportAddingFragmentBinaryFunctions = YES;

// Create render pipeline functions descriptor

MTLRenderPipelineFunctionsDescriptor extraDesc;
extraDesc.fragmentAdditionalBinaryFunctions = @[bat];

// Instantiate render pipeline state

id<MTLRenderPipelineState> renderPipeline2 =
  [renderPipeline1 newRenderPipelineStateWithAdditionalBinaryFunctions:extraDesc
```

### Stitching process — [20:30]

```objectivec
[[stitchable]] int FunctionA(device int*, int) {…}
[[stitchable]] int FunctionC(int, int) {…}

[[stitchable]]
int ResultFunction(device int* Input0,
                   int Input1, 
                   int Input2)
{
  int N0 = FunctionA(Input0, Input1);
  int N1 = FunctionA(Input0, Input2);
  int N2 = FunctionC(N0, N1);    
  return N2;
}
```

### Creating the graph — [21:32]

```objectivec
// Create input nodes

  inputs[0] = [[MTLFunctionStitchingInputNode alloc] initWithArgumentIndex:0];

// Create function nodes

  n0 = [[MTLFunctionStitchingFunctionNode alloc] initWithName:@"FunctionA"
                                                    arguments:@[inputs[0], inputs[1]]
                                          controlDependencies:@[]];
  n1 = [[MTLFunctionStitchingFunctionNode alloc] initWithName:@"FunctionA"
                                                    arguments:@[inputs[0], inputs[2]]
                                          controlDependencies:@[]];
  n2 = [[MTLFunctionStitchingFunctionNode alloc] initWithName:@"FunctionC"
                                                    arguments:@[n0, n1]
                                          controlDependencies:@[]];

// Create graph

  graph = [[MTLFunctionStitchingGraph alloc] initWithFunctionName:@"ResultFunction"
                                                            nodes:@[n0, n1]
                                                       outputNode:n2
                                                       attributes:@[]];
```

### Configure stitched library descriptor — [22:18]

```objectivec
// Configure stitched library descriptor

  MTLStitchedLibraryDescriptor* descriptor = [MTLStitchedLibraryDescriptor new];

  descriptor.functions      = @[stitchableFunctions];
  descriptor.functionGraphs = @[graph];

// Create stitched function

  id<MTLLibrary> lib = [device newLibraryWithDescriptor:descriptor 
                                                  error:&error];

  id<MTLFunction> stitchedFunction = [lib newFunctionWithName:@"ResultFunction"];
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10229/3/B5993DB1-3978-4019-B109-364AE2E6F14A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10229/3/B5993DB1-3978-4019-B109-364AE2E6F14A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10229) — developer.apple.com. Indexed for agent consumption._
