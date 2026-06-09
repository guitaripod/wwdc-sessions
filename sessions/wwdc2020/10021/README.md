---
id: "wwdc2020-10021"
event: "wwdc2020"
year: 2020
title: "Build Metal-based Core Image kernels with Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10021"
topics: ["Audio & Video", "Developer Tools", "Photos & Camera", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build Metal-based Core Image kernels with Xcode

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10021](https://developer.apple.com/videos/play/wwdc2020/10021)

Learn how to integrate and load Core Image kernels written in the Metal Shading Language into your application, and discover how you can apply these image filters to create unique effects. Explore how to use Xcode rules and naming conventions for Core Image kernels written in Metal Shading Language. We’ll explain how to best use Core Image APIs effectively and optimally with Metal and the Metal Shading Language.

**Keywords:** `coreimage`, `graphics`, `image processing`, `metal`, `performance`, `video`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(846 words)

## Documentation & Resources

- [Core Image](https://developer.apple.com/documentation/CoreImage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreImage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreImage.json

## Code Snippets

### Put your kernels in .ci.metal sources — [3:08]

```swift
// MyKernels.ci.metal
#include <CoreImage/CoreImage.h> // includes CIKernelMetalLib.h
using namespace metal;

extern "C" float4 HDRZebra (coreimage::sample_t s, float time, coreimage::destination dest) 
{
	float diagLine = dest.coord().x + dest.coord().y;
	float zebra = fract(diagLine/20.0 + time*2.0);
	if ((zebra > 0.5) && (s.r > 1 || s.g > 1 || s.b > 1))
		return float4(2.0, 0.0, 0.0, 1.0);
	return s;
}
```

### Loading your kernel and applying it to create a new image — [4:58]

```swift
class HDRZebraFilter: CIFilter {
    var inputImage: CIImage?
	var inputTime: Float = 0.0

    static var kernel: CIColorKernel = { () -> CIColorKernel in 
	    let url = Bundle.main.url(forResource: "MyKernels", 
                                withExtension: "ci.metallib")!
		let data = try! Data(contentsOf: url)
		return try! CIColorKernel(functionName: "HDRzebra",                            fromMetalLibraryData: data)
	}()

  	override var outputImage : CIImage? {
		get {
			guard let input = inputImage else {return nil}
			return HDRZebraFilter.kernel.apply(extent: input.extent, 
											 arguments: [input, inputTime])
		}
	}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10021/7/91A7268C-8211-46D3-B08E-9F554CE138A1/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10021) — developer.apple.com. Indexed for agent consumption._