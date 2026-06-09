---
id: "wwdc2020-10009"
event: "wwdc2020"
year: 2020
title: "Edit and play back HDR video with AVFoundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10009"
topics: ["Developer Tools", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Edit and play back HDR video with AVFoundation

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10009](https://developer.apple.com/videos/play/wwdc2020/10009)

Find out how you can support HDR editing and playback in your macOS app, and how you can determine if a specific hardware configuration is eligible for HDR playback. We'll show you how to use AVMutableVideoComposition with the built-in compositor and easily edit HDR content, explain how you can use Core Image's built-in image filters to create your own AVMutableVideoComposition, and demonstrate how to create and use a custom compositor to enable HDR editing.

**Keywords:** `metal`, `performance`, `prores`, `video`, `videotoolbox`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,350 words)

## Documentation & Resources

- [Editing and playing HDR video](https://developer.apple.com/documentation/AVFoundation/editing-and-playing-hdr-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/editing-and-playing-hdr-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/editing-and-playing-hdr-video.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Create AVVideoComposition with custom compositor class — [6:43]

```swift
// Create AVVideoComposition with custom compositor class
let videoComposition = AVMutableVideoComposition()

videoComposition.instructions = [videoCompositionInstruction]
videoComposition.frameDuration = CMTimeMake(value: 1, timescale: 30)
videoComposition.renderSize = assetSize
```

### Create AVVideoComposition using “applyingCIFiltersWithHandler” — [9:55]

```swift
// Create AVVideoComposition using “applyingCIFiltersWithHandler”

let videoComposition = 
 AVMutableVideoComposition(asset: asset, 
 applyingCIFiltersWithHandler: {
     (request: AVAsynchronousCIImageFilteringRequest) -> Void in

     let ciFilter = CIFilter(name: “CIZoomBlur”)

     ciFilter!.setValue(request.sourceImage, forKey: kCIInputImageKey)

         request.finish(with: ciFilter!.outputImage!, context: nil)
     })
```

### First CIKernel — [10:57]

```objectivec
// HDRHighlight.metal

#include <metal_stdlib>
#include <CoreImage/CoreImage.h>
using namespace metal;

extern “C” float4 HDRHighlight(coreimage::sample_t s, coreimage::destination dest) {       

    if (s.r > 1.0 || s.g > 1.0 || s.b > 1.0)
		return float4(2.0, 0.0, 0.0, 1.0);
	else
		return s;
}
```

### Color Inverter CI Kernel — [11:22]

```objectivec
// ColorInverter.metal - not HDR ready

#include <metal_stdlib>
#include <CoreImage/CoreImage.h>
using namespace metal;

extern “C” float4 ColorInverter(coreimage::sample_t s, coreimage::destination dest) {       

	return float4(1.0 - s.r, 1.0 - s.g, 1.0 - s.b, 1.0);
}
```

### Custom compositor class — [12:23]

```swift
// Custom compositor class
class SampleCustomCompositor: NSObject, AVVideoCompositing {
…
}


// Create AVVideoComposition with custom compositor class
let videoComposition = AVMutableVideoComposition()

videoComposition.instructions = [videoCompositionInstruction]
videoComposition.frameDuration = CMTimeMake(value: 1, timescale: 30)
videoComposition.renderSize = assetSize

videoComposition.customVideoCompositorClass = SampleCustomCompositor.self
```

### Setting custom compositor to support HDR — [13:58]

```swift
// Setting custom compositor to support HDR

class SampleCustomCompositor: NSObject, AVVideoCompositing {
	var sourcePixelBufferAttributes: [String : Any]? =
    [kCVPixelBufferPixelFormatTypeKey as String:
                    [kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange]]

	var requiredPixelBufferAttributesForRenderContext: [String : Any] =
			[kCVPixelBufferPixelFormatTypeKey as String: 
                            [kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange]]

	var supportsHDRSourceFrames = true
    var supportsWideColorSourceFrames = true

	func startRequest(_ request: AVAsynchronousVideoCompositionRequest) {
			 ...
	}

	func renderContextChanged(_ newRenderContext: AVVideoCompositionRenderContext) {
	}
}
```

### AVPlayer API definition — [21:01]

```swift
// API definition 
extension AVPlayer {
    @available(macOS 10.15, *)
    open class var eligibleForHDRPlayback: Bool { get }
}
```

### AVPlayer API definition 2 — [21:41]

```swift
// API definition 
extension AVPlayer {
    @available(macOS 10.15, *)
    open class var eligibleForHDRPlayback: Bool { get }
}

// Set video composition color properties based on HDR playback eligibility 
if AVPlayer.eligibleForHDRPlayback {
     videoComposition.colorPrimaries = AVVideoColorPrimaries_ITU_R_2020
	 videoComposition.colorTransferFunction = AVVideoTransferFunction_ITU_R_2100_HLG
	 videoComposition.colorYCbCrMatrix = AVVideoYCbCrMatrix_ITU_R_2020
}
else {
	 videoComposition.colorPrimaries = AVVideoColorPrimaries_ITU_R_709_2
	 videoComposition.colorTransferFunction = AVVideoTransferFunction_ITU_R_709_2
	 videoComposition.colorYCbCrMatrix = AVVideoYCbCrMatrix_ITU_R_709_2
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10009/8/2BA74921-CA85-43BC-8CDD-0C0236B7A44F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10009) — developer.apple.com. Indexed for agent consumption._
