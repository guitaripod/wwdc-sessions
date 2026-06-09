---
id: "wwdc2022-10017"
event: "wwdc2022"
year: 2022
title: "Explore the machine learning development experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10017"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore the machine learning development experience

**Event:** WWDC22 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10017](https://developer.apple.com/videos/play/wwdc2022/10017)

Learn how to bring great machine learning (ML) based experiences to your app. We'll take you through model discovery, conversion, and training and provide tips and best practices for ML. We'll share considerations to take into account as you begin your ML journey, demonstrate techniques for evaluating model performance, and explore how you can tune models to achieve real-time performance on device. To learn more about the techniques covered in this session, watch "Optimize your Core ML usage" and "Accelerate machine learning with Metal" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,351 words)

## Documentation & Resources

- [Core ML Converters](https://coremltools.readme.io/docs) _documentation_
- [Core ML Tools PyTorch Conversion Documentation](https://coremltools.readme.io/docs/pytorch-conversion) _documentation_
- [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/CoreML/integrating-a-core-ml-model-into-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreML/integrating-a-core-ml-model-into-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreML/integrating-a-core-ml-model-into-your-app.json
- [Core ML](https://developer.apple.com/documentation/CoreML) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreML
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreML.json

## Code Snippets

### Colorization pre-processing — [3:06]

```python
from skimage import color

in_lab = color.rgb2lab(in_rgb)
in_l = in_lab[:,:,0]
```

### Colorization post-processing — [3:39]

```python
from skimage import color
import numpy as np
import torch

out_lab = torch.cat((in_l, out_ab), dim=1)
out_rgb = color.lab2rgb(out_lab.data.numpy()[0,…].transpose((1,2,0)))
```

### Convert colorizer model to Core ML — [3:56]

```python
import coremltools as ct
import torch
import Colorizer

torch_model = Colorizer().eval()

example_input = torch.rand([1, 1, 256, 256])
traced_model = torch.jit.trace(torch_model, example_input)

coreml_model = ct.convert(traced_model, 
                          inputs=[ct.TensorType(name="input", shape=example_input.shape)])

coreml_model.save("Colorizer.mlpackage")
```

### Core ML model verification using Core ML Tools — [4:26]

```python
import coremltools as ct
from PIL import Image
from skimage import color

in_img = Image.open(“image.png").convert("RGB")
in_rgb = np.array(in_img)
in_lab = color.rgb2lab(in_rgb, channel_axis=2)

lab_components = np.split(in_lab, indices_or_sections=3, axis=-1)
(in_l, _, _) = [
    np.expand_dims(array.transpose((2, 0, 1)).astype(np.float32), 0)
    for array in lab_components
]
out_ab = coreml_model.predict({"input": in_l})[0]

out_lab = np.squeeze(np.concatenate([in_l, out_ab], axis=1), axis=0).transpose((1, 2, 0))
out_rgb = color.lab2rgb(out_lab, channel_axis=2).astype(np.uint8)
out_img = Image.fromarray(out_rgb)
```

### Colorization in Swift — [7:11]

```swift
import CoreImage
import CoreML

func colorize(image inputImage: CIImage) throws -> CIImage {

    let lightness: CIImage = extractLightness(from: inputImage)

    let modelInput = try ColorizerInput(inputWith: lightness.cgImage!)

    let modelOutput: ColorizerOutput = try colorizer.prediction(input: modelInput)

    let (aChannel, bChannel): (CIImage, CIImage) = extractColorChannels(from: modelOutput)

    let colorizedImage = reconstructRGBImage(l: lightness, a: aChannel, b: bChannel)
    return colorizedImage
}
```

### Extract lightness from RGB image using Core Image — [7:41]

```swift
import CoreImage.CIFilterBuiltins

func extractLightness(from inputImage: CIImage) -> CIImage {

    let rgbToLabFilter = CIFilter.convertRGBtoLab()
    rgbToLabFilter.inputImage = inputImage
    rgbToLabFilter.normalize = true
    let labImage = rgbToLabFilter.outputImage

    let matrixFilter = CIFilter.colorMatrix()
    matrixFilter.inputImage = labImage
    matrixFilter.rVector = CIVector(x: 1, y: 0, z: 0)
    matrixFilter.gVector = CIVector(x: 1, y: 0, z: 0)
    matrixFilter.bVector = CIVector(x: 1, y: 0, z: 0)
    let lightness = matrixFilter.outputImage!
    return lightness
}
```

### Create two color channel CIImages from model output — [8:31]

```swift
func extractColorChannels(from output: ColorizerOutput) -> (CIImage, CIImage) {

    let outA: [Float] = output.output_aShapedArray.scalars
    let outB: [Float] = output.output_bShapedArray.scalars
    let dataA = Data(bytes: outA, count: outA.count * MemoryLayout<Float>.stride)
    let dataB = Data(bytes: outB, count: outB.count * MemoryLayout<Float>.stride)

    let outImageA = CIImage(bitmapData: dataA,
        bytesPerRow: 4 * 256,
        size: CGSize(width: 256, height: 256),
        format: CIFormat.Lh,
        colorSpace: CGColorSpaceCreateDeviceGray())
    let outImageB = CIImage(bitmapData: dataB,
        bytesPerRow: 4 * 256,
        size: CGSize(width: 256, height: 256),
        format: CIFormat.Lh,
        colorSpace: CGColorSpaceCreateDeviceGray())
   return (outImageA, outImageB)
}
```

### Reconstruct RGB image from Lab images — [8:51]

```swift
func reconstructRGBImage(l lightness: CIImage,
                         a aChannel: CIImage,
                         b bChannel: CIImage) -> CIImage {
    guard
        let kernel = try? CIKernel.kernels(withMetalString: source)[0] as? CIColorKernel,
        let kernelOutputImage = kernel.apply(extent: lightness.extent,
                                             arguments: [lightness, aChannel, bChannel])
    else { fatalError() }

    let labToRGBFilter = CIFilter.convertLabToRGBFilter()
    labToRGBFilter.inputImage = kernelOutputImage
    labToRGBFilter.normalize = true
    let rgbImage = labToRGBFilter.outputImage!
    return rgbImage
}
```

### Custom CIKernel to combine L, a* and b* channels. — [9:08]

```swift
let source = """
#include <CoreImage/CoreImage.h>
[[stichable]] float4 labCombine(coreimage::sample_t imL, coreimage::sample_t imA, coreimage::sample_t imB)
{
   return float4(imL.r, imA.r, imB.r, imL.a);
}
"""
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10017/3/6F4C9F52-725A-4AD2-83BD-A3D43D29A914/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10017/3/6F4C9F52-725A-4AD2-83BD-A3D43D29A914/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10017) — developer.apple.com. Indexed for agent consumption._
