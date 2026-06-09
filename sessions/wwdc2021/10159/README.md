---
id: "wwdc2021-10159"
event: "wwdc2021"
year: 2021
title: "Explore Core Image kernel improvements"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10159"
topics: ["Audio & Video", "Photos & Camera", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore Core Image kernel improvements

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10159](https://developer.apple.com/videos/play/wwdc2021/10159)

Discover how you can add Core Image kernels written in the Metal Shading Language into your app. We’ll explore how you can use Xcode rules and naming conventions for Core Image kernels written in the Metal Shading Language, and help you make sense of Metal’s Stitchable functions and dynamic library features to benefit Core Image kernels.

**Keywords:** `coreimage`, `filters`, `hardware`, `image`, `image processing`, `metal`, `metal shading language`, `metal tools`, `photos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,288 words)

## Documentation & Resources

- [Core Image](https://developer.apple.com/documentation/CoreImage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreImage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreImage.json

## Code Snippets

### Extern CIKernels — [3:54]

```objectivec
// MyKernels.ci.metal
#include <CoreImage/CoreImage.h> // includes CIKernelMetalLib.h

using namespace metal;

extern "C" float4 myKernel (coreimage::sample_t s, 
                            float param, 
                            coreimage::destination dest) 
{
  float4 result = s;

  // Example code to create striped pattern
	float diagLine = dest.coord().x + dest.coord().y;
	float stripe   = fract(diagLine/20.0 + param*2.0);

  // Color range check
	if((stripe > 0.5) && ((s.r > 1) || (s.g > 1) || (s.b > 1)))
		result = float4(2.0, 0.0, 0.0, 1.0);

	return result;
}
```

### Load your extern CI kernel and apply it to create a new image — [4:32]

```swift
class MyFilter: CIFilter {
    var inputImage: CIImage?
	var inputParam: Float = 0.0
    static var kernel: CIColorKernel = { () -> CIColorKernel in 
	  let url = Bundle.main.url(forResource: "MyKernels", 
                              withExtension: "ci.metallib")!
      let data = try! Data(contentsOf: url)
	  return try! CIColorKernel(functionName: "MyKernel", 
                              fromMetalLibraryData: data)
	}()
	override var outputImage : CIImage? {
      get { guard let input = inputImage else { return nil }
		return MyFilter.kernel.apply(extent:input.extent, 
                                 arguments:[input, inputParam]) }
	}
}
```

### Stitchable CI Kernel — [6:18]

```objectivec
// MyKernels.ci.metal
#include <CoreImage/CoreImage.h> // includes CIKernelMetalLib.h

using namespace metal;

[[stitchable]] float4 myKernel (coreimage::sample_t s, 
                                float param, 
                                coreimage::destination d) 
{
  float4 result = s;

  // Example code to create striped pattern
	float diagLine = dest.coord().x + dest.coord().y;
	float stripe   = fract(diagLine/20.0 + param*2.0);

  // Color range check
	if((stripe > 0.5) && ((s.r > 1) || (s.g > 1) || (s.b > 1)))
		result = float4(2.0, 0.0, 0.0, 1.0);

	return result;
}
```

### Load your stitchable CI kernel and apply it to create a new image — [6:40]

```swift
class MyFilter: CIFilter {
    var inputImage: CIImage?
	var inputParam: Float = 0.0
    static var kernel: CIColorKernel = { () -> CIColorKernel in 
	    let url = Bundle.main.url(forResource: "default", 
                                withExtension: "metallib")!
		let data = try! Data(contentsOf: url)
		return try! CIColorKernel(functionName: "MyKernel", fromMetalLibraryData: data)
	}()
	override var outputImage : CIImage? {
      get { guard let input = inputImage else { return nil }
		return MyFilter.kernel.apply(extent:input.extent, arguments:[input, inputParam]) }
	}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10159/4/40A32E20-B4FF-4586-9C5B-1994F3A585A2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10159/4/40A32E20-B4FF-4586-9C5B-1994F3A585A2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10159) — developer.apple.com. Indexed for agent consumption._