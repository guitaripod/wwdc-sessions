---
id: "wwdc2025-276"
event: "wwdc2025"
year: 2025
title: "What’s new in BNNS Graph"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/276"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in BNNS Graph

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-276](https://developer.apple.com/videos/play/wwdc2025/276)

The BNNS Graph Builder API now enables developers to write graphs of operations using the familiar Swift language to generate pre- and post-processing routines and small machine-learning models. BNNS compiles graphs ahead of execution and supports real-time and latency-sensitive use cases such as audio processing. In this session, we revisit last year’s bit-crusher example and simplify the Swift component by removing the reliance on a separate Python file and instead implement the audio effect entirely in Swift. The BNNS Graph Builder API is also suited to pre-processing image data before passing that data to a machine learning model. The session also includes a demonstration of clipping the transparent pixels from an image with an alpha channel.

**Keywords:** `bnns`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,127 words)

## Documentation & Resources

- [vImage.PixelBuffer](https://developer.apple.com/documentation/Accelerate/vImage/PixelBuffer) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accelerate/vImage/PixelBuffer
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accelerate/vImage/PixelBuffer.json
- [BNNS](https://developer.apple.com/documentation/Accelerate/bnns-library) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accelerate/bnns-library
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accelerate/bnns-library.json
- [Supporting real-time ML inference on the CPU](https://developer.apple.com/documentation/Accelerate/supporting-real-time-ml-inference-on-the-cpu) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accelerate/supporting-real-time-ml-inference-on-the-cpu
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accelerate/supporting-real-time-ml-inference-on-the-cpu.json

## Code Snippets

### Introduction to BNNSGraphBuilder — [8:31]

```swift
import Accelerate



func demo() throws {

    let context = try BNNSGraph.makeContext {
        builder in

        let x = builder.argument(name: "x",
                                 dataType: Float.self,
                                 shape: [8])
        let y = builder.argument(name: "y",
                                 dataType: Float.self,
                                 shape: [8])

        let product = x * y
        let mean = product.mean(axes: [0], keepDimensions: true)

        // Prints "shape: [1] | stride: [1]".
        print("mean", mean)

        return [ product, mean]
    }

    var args = context.argumentNames().map {
        name in
        return context.tensor(argument: name,
                              fillKnownDynamicShapes: false)!
    }

    // Output arguments
    args[0].allocate(as: Float.self, count: 8)
    args[1].allocate(as: Float.self, count: 1)

    // Input arguments
    args[2].allocate(
        initializingFrom: [1, 2, 3, 4, 5, 6, 7, 8] as [Float])
    args[3].allocate(
        initializingFrom: [8, 7, 6, 5, 4, 3, 2, 1] as [Float])

        try context.executeFunction(arguments: &args)

    // [8.0, 14.0, 18.0, 20.0, 20.0, 18.0, 14.0, 8.0]
    print(args[0].makeArray(of: Float.self))

    // [15.0]
    print(args[1].makeArray(of: Float.self))

    args.forEach {
        $0.deallocate()
    }
}
```

### Strong typing — [12:04]

```swift
// Performs `result = mask0 .< mask1 ? bases.pow(exponents) : 0

let context = try BNNSGraph.makeContext {
    builder in

    let mask0 = builder.argument(dataType: Float16.self,
                                 shape: [-1])
    let mask1 = builder.argument(dataType: Float16.self,
                                 shape: [-1])

    let bases = builder.argument(dataType: Float16.self,
                                 shape: [-1])
    let exponents = builder.argument(dataType: Int32.self,
                                     shape: [-1])

    // `mask` contains Boolean values.
    let mask = mask0 .< mask1

    // Cast integer exponents to FP16.
    var result = bases.pow(y: exponents.cast(to: Float16.self))
    result = result * mask.cast(to: Float16.self)

    return [result]
}
```

### Slicing — [14:15]

```swift
let srcImage = #imageLiteral(resourceName: "squirrel.jpeg").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 32,
    bitsPerPixel: 32 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(alpha: .none,
                             component: .float,
                             byteOrder: .order32Host))!

let source = try vImage.PixelBuffer(cgImage: srcImage,
                                    cgImageFormat: &cgImageFormat,
                                    pixelFormat: vImage.InterleavedFx3.self)

let cropSize = 640
let horizontalMargin = (source.width - cropSize) / 2
let verticalMargin = (source.height - cropSize) / 2

let destination = vImage.PixelBuffer(size: .init(width: cropSize,
                                                 height: cropSize),
                                     pixelFormat: vImage.InterleavedFx3.self)

let context = try BNNSGraph.makeContext {
    builder in

    let src = builder.argument(name: "source",
                               dataType: Float.self,
                               shape: [ -1, -1, 3])

    let result = src [
        BNNSGraph.Builder.SliceRange(startIndex: verticalMargin,
                                     endIndex: -verticalMargin),
        BNNSGraph.Builder.SliceRange(startIndex: horizontalMargin,
                                     endIndex: -horizontalMargin),
        BNNSGraph.Builder.SliceRange.fillAll
    ]

    return [result]
}

source.withBNNSTensor { src in
    destination.withBNNSTensor { dst in

        var args = [dst, src]

        print(src)
        print(dst)

        try! context.executeFunction(arguments: &args)
    }
}

let result = destination.makeCGImage(cgImageFormat: cgImageFormat)
```

### Preprocessing by thresholding on mean — [17:31]

```swift
let srcImage = #imageLiteral(resourceName: "birds.jpeg").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 16,
    bitsPerPixel: 16,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(rawValue: CGBitmapInfo.byteOrder16Little.rawValue |
                             CGBitmapInfo.floatComponents.rawValue |
                             CGImageAlphaInfo.none.rawValue))!

let source = try! vImage.PixelBuffer<vImage.Planar16F>(cgImage: srcImage,
                                                       cgImageFormat: &cgImageFormat)
let destination = vImage.PixelBuffer<vImage.Planar16F>(size: source.size)

let context = try BNNSGraph.makeContext {
    builder in

    let src = builder.argument(name: "source",
                               dataType: Float16.self,
                               shape: [-1, -1, 1])

    let mean = src.mean(axes: [0, 1], keepDimensions: false)

    let thresholded = src .> mean

    let result = thresholded.cast(to: Float16.self)

    return [result]
}

source.withBNNSTensor { src in
    destination.withBNNSTensor { dst in

        var args = [dst, src]

        try! context.executeFunction(arguments: &args)
    }
}

let result = destination.makeCGImage(cgImageFormat: cgImageFormat)
```

### Postprocessing — [19:04]

```swift
func postProcess(result: BNNSTensor, k: Int) throws -> ([Float32], [Int32]) {

    let context = try BNNSGraph.makeContext {
        builder in

        let x = builder.argument(dataType: Float32.self,
                                 shape: [-1])

        let softmax = x.softmax(axis: 1)

        let topk = softmax.topK(k, axis: 1, findLargest: true)

        return [topk.values, topk.indices]
    }

    let indices = context.allocateTensor(argument: context.argumentNames()[0],
                                         fillKnownDynamicShapes: false)!
    let values = context.allocateTensor(argument: context.argumentNames()[1],
                                        fillKnownDynamicShapes: false)!

    var arguments = [values, indices, result]

    try context.executeFunction(arguments: &arguments)

    return (values.makeArray(of: Float32.self), indices.makeArray(of: Int32.self))
}
```

### Bitcrusher in PyTorch — [21:03]

```python
import coremltools as ct
from coremltools.converters.mil import Builder as mb
from coremltools.converters.mil.mil import (
    get_new_symbol
)

import torch
import torch.nn as nn
import torch.nn.functional as F

class BitcrusherModel(nn.Module):
    def __init__(self):
        super(BitcrusherModel, self).__init__()

    def forward(self, source, resolution, saturationGain, dryWet):
        # saturation
        destination = source * saturationGain
        destination = F.tanh(destination)

        # quantization
        destination = destination * resolution
        destination = torch.round(destination)
        destination = destination / resolution

        # mix
        destination = destination * dryWet
        destination = 1.0 - dryWet
        source = source * dryWet

        destination = destination + source

        return destination
```

### Bitcrusher in Swift — [21:03]

```swift
typealias BITCRUSHER_PRECISION = Float16

let context = try! BNNSGraph.makeContext {
    builder in

    var source = builder.argument(name: "source",
                                  dataType: BITCRUSHER_PRECISION.self,
                                  shape: [sampleCount, 1, 1])

    let resolution = builder.argument(name: "resolution",
                                      dataType: BITCRUSHER_PRECISION.self,
                                      shape: [1, 1, 1])

    let saturationGain = builder.argument(name: "saturationGain",
                                          dataType: BITCRUSHER_PRECISION.self,
                                          shape: [1, 1, 1])

    var dryWet = builder.argument(name: "dryWet",
                                  dataType: BITCRUSHER_PRECISION.self,
                                  shape: [1, 1, 1])

    // saturation
    var destination = source * saturationGain
    destination = destination.tanh()

    // quantization

    destination = destination * resolution
    destination = destination.round()
    destination = destination / resolution

    // mix
    destination = destination * dryWet
    dryWet = BITCRUSHER_PRECISION(1) - dryWet
    source = source * dryWet

    destination = destination + source

    return [destination]
}
```

### Changing precision — [22:34]

```swift
typealias BITCRUSHER_PRECISION = Float16

let context = try! BNNSGraph.makeContext {
    builder in

    var source = builder.argument(name: "source",
                                  dataType: BITCRUSHER_PRECISION.self,
                                  shape: [sampleCount, 1, 1])

    let resolution = builder.argument(name: "resolution",
                                      dataType: BITCRUSHER_PRECISION.self,
                                      shape: [1, 1, 1])

    let saturationGain = builder.argument(name: "saturationGain",
                                          dataType: BITCRUSHER_PRECISION.self,
                                          shape: [1, 1, 1])

    var dryWet = builder.argument(name: "dryWet",
                                  dataType: BITCRUSHER_PRECISION.self,
                                  shape: [1, 1, 1])

    // saturation
    var destination = source * saturationGain
    destination = destination.tanh()

    // quantization

    destination = destination * resolution
    destination = destination.round()
    destination = destination / resolution

    // mix
    destination = destination * dryWet
    dryWet = BITCRUSHER_PRECISION(1) - dryWet
    source = source * dryWet

    destination = destination + source

    return [destination]
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/276/4/68973e7e-a4db-44eb-9c9f-f90f3dde4a75/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/276/4/68973e7e-a4db-44eb-9c9f-f90f3dde4a75/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/276) — developer.apple.com. Indexed for agent consumption._