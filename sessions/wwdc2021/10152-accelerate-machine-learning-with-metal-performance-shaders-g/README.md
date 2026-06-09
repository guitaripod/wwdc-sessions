---
id: "wwdc2021-10152"
event: "wwdc2021"
year: 2021
title: "Accelerate machine learning with Metal Performance Shaders Graph"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10152"
topics: ["AI & Machine Learning", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Accelerate machine learning with Metal Performance Shaders Graph

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10152](https://developer.apple.com/videos/play/wwdc2021/10152)

Metal Performance Shaders Graph is a compute engine that helps you build, compile, and execute customized multidimensional graphs for linear algebra, machine learning, computer vision, and image processing. Discover how MPSGraph can accelerate the popular TensorFlow platform through a Metal backend for Apple products. Learn how to add control flow to your graphs, manage the graph compilation for optimal performance, and use the MPSGraph operations to accelerate the hardest compute applications with only a few lines of code.

**Keywords:** `machine learning`, `metal`, `metal shading language`, `optimization`, `performance`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,169 words)

## Documentation & Resources

- [Training a Neural Network with Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders/training-a-neural-network-with-metal-performance-shaders) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders/training-a-neural-network-with-metal-performance-shaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders/training-a-neural-network-with-metal-performance-shaders.json
- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Control dependencies 1 — [8:35]

```swift
// Execute the graph
let results = graph.run(feeds: [inputTensor: inputs],
                        targetTensors: [exp],
                        targetOperations: [assign])
```

### Control dependencies 2 — [9:01]

```swift
// Create control dependency

let exp = graph.controlDependency(with: [assign],
                                  dependentBlock: { 
                                      return [graph.exponent(with: input, 
                                                             name: nil)]
                                  },
                                  name: nil)

// Execute the graph

let results = graph.run(feeds: [inputTensor: inputs],
                        targetTensors: [exp],
                        targetOperations: nil)
```

### Evaluation method — [14:42]

```swift
// Create the graph

let placeholder0 = graph.placeholder(shape: [1, 3], 
                                     dataType: .float32, 
                                     name: nil)

let placeholder1 = graph.placeholder(shape: [2, 1], 
                                     dataType: .float32, 
                                     name: nil)

let addTensor = graph.addition(placeholder0, 
                               placeholder1, 
                               name: nil)

// Compile the graph into an executable

let executable = graph.compile(with: nil,
                               feeds: [placeholder0: MPSGraphShapedType(shape: [1, 3], 
                                                                        dataType: .float32),
                                       placeholder1: MPSGraphShapedType(shape: [2, 1], 
                                                                        dataType: .float32)],
                               targetTensors: [addTensor],
                               targetOperations: nil,
                               compilationDescriptor: nil)

// Execute the graph into an executable

let fetch = executable.run(with: commandQueue,
                           inputs: [MPSGraphTensorData(input0),        
                                    MPSGraphTensorData(input1)],
                           results: nil,
                           executionDescriptor: nil)
```

### Disabling the type inference pass — [16:38]

```swift
// Create the graph compilation descriptor

let descriptor = MPSGraphCompilationDescriptor()

// Disable type inference

descriptor.disableTypeInference()

// Compile the graph into an executable

let executable = graph.compile(with: nil,
                               feeds: /* feeds */,
                               targetTensors: /* target tensors */,
                               targetOperations: nil,
                               compilationDescriptor: descriptor)

// execute the graph
```

### If/else in batch normalization — [19:22]

```swift
// Different behavior during inference and training

let results = graph.if(isTraining,
                       then: { ... },    // compute mean and variance
                       else: { ... },    // use running_mean and running_variance
                       name: nil)
```

### If/else — [19:46]

```swift
let predicate = graph.lessThan(a, 
                               b, 
                               name: nil)

let results = graph.if(predicate,
    then: {[
        graph.addition(a, 
                       b, 
                       name: nil)
    ]},
    else: {[
        graph.subtraction(a, 
                          b, 
                          name: nil)
    ]},
    name: nil)
```

### For loop 1 — [20:58]

```swift
var result = input0

for i in 0..<4 {
    result *= input1
}
```

### For Loop 2 — [21:12]

```swift
// Initialize inputs

let input0 = graph.placeholder(shape: [], 
                               dataType: .int32, 
                               name: nil)

let input1 = graph.placeholder(shape: [], 
                               dataType: .int32, 
                               name: nil)

let numberOfIterations = graph.constant(4, 
                                        shape: [], 
                                        dataType: .int32)
```

### For Loop 3 — [21:33]

```swift
// Define Body

let body = {
    (index: MPSGraphTensor, iterationArguments: [MPSGraphTensor]) -> [MPSGraphTensor] in
        let iterationResult = graph.multiplication(iterationArguments[0], input1, name: nil)
        return [iterationResult]
}
```

### For Loop 4 — [21:52]

```swift
// Create for loop operation

let result = graph.for(numberOfIterations: numberOfIterations,
                       initialIterationArguments: [input0],
                       body: body)
```

### While loop 1 — [22:51]

```swift
var result = initialValue

while result < threshold {
    result *= multiplier
}
```

### While loop 2 — [23:01]

```swift
// Evaluate condition

let condition = {
    (inputs: [MPSGraphTensor], returnTensors: NSMutableArray) -> MPSGraphTensor in
        let predicate = graph.lessThan(inputs[0], threshold, name: nil)
        returnTensors.add(inputs[0])
        return predicate
}
```

### While loop 3 — [23:22]

```swift
// Define body

let body = {
    (inputs: [MPSGraphTensor]) -> [MPSGraphTensor] in
        let iterationResult = graph.multiplication(inputs[0], multiplier, name: nil)
        return [iterationResult]
}
```

### While loop 4 — [23:33]

```swift
// Create while loop operation

let results = graph.while(initialInputs: [initialValue],
                          before: condition,
                          after: body,
                          name: nil)
```

### Edge filter — [25:00]

```swift
// Apply the laplacian edge filter on the source image

let edges = graph.stencil(with: source, 
                          weights: laplacianWeights, 
                          descriptor: desc, 
                          name: nil)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10152/6/38BC0CF8-718D-4950-9CC4-B64396F5FFDD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10152/6/38BC0CF8-718D-4950-9CC4-B64396F5FFDD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10152) — developer.apple.com. Indexed for agent consumption._
