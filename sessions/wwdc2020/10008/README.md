---
id: "wwdc2020-10008"
event: "wwdc2020"
year: 2020
title: "Optimize the Core Image pipeline for your video app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10008"
topics: ["Developer Tools", "Graphics & Games", "Photos & Camera", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Optimize the Core Image pipeline for your video app

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10008](https://developer.apple.com/videos/play/wwdc2020/10008)

Explore how you can harness the processing power of Core Image and optimize video performance within your app. We’ll show you how to build your Core Image pipeline for applying effects to your video in your apps: Discover how to reduce your app’s memory footprint when using CIContext, and learn best practices for using AVPlayView or MTKView view classes for video playback with Core Image filters. Additionally, find out why you should write your own custom kernels in the Metal Shading Language, and learn performance tips for optimal usage of Metal command queues in your Core Image pipeline.

**Keywords:** `coreimage`, `graphics`, `image processing`, `metal`, `performance`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,333 words)

## Documentation & Resources

- [Core Image](https://developer.apple.com/documentation/CoreImage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreImage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreImage.json

## Code Snippets

### Creating CIContext — [0:52]

```swift
let context =  CIContext(options: [
    .cacheIntermediates : false,
    .name : ”MyAppView”
])
```

### Creating CIContext 2 — [1:26]

```swift
let context =  CIContext(MTLCommandQueue : queue, options: […])
```

### Use builtins Whenever possible — [2:59]

```swift
import CoreImage.CIFilterBuiltins

func motionBlur(inputImage: CIImage) -> CIImage? {
    let motionBlurFilter = CIFilter.motionBlur()
    motionBlurFilter.inputImage = inputImage
    motionBlurFilter.angle = 0
    motionBlurFilter.radius = 20
    return motionBlurFilter.outputImage
}
```

### Put your kernels in .ci.metal sources — [3:56]

```objectivec
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

### Using AVPlayer View — [5:50]

```swift
let videoComposition = AVMutableVideoComposition(
    asset: asset,      applyingCIFiltersWithHandler:
    { (request: AVAsynchronousCIImageFilteringRequest) -> Void in
        let filter = HDRZebraFilter()         filter.inputImage = request.sourceImage
        let output = filter.outputImage

        if (output != nil) {
            request.finish(with: output, context: myCtx)
        }
        else { request.finish(with: err) }
    }
)
```

### Using MTKView — [7:01]

```swift
class MyView : MTKView {
var context: CIContext
var commandQueue : MTLCommandQueue

override init(frame frameRect: CGRect, device: MTLDevice?) {
    let dev = device ?? MTLCreateSystemDefaultDevice()!
    context = CIContext(mtlDevice: dev, options: [.cacheIntermediates : false] )
    commandQueue = dev.makeCommandQueue()!

    super.init(frame: frameRect, device: dev)

    framebufferOnly = false  // allow Core Image to use Metal Compute
    colorPixelFormat = MTLPixelFormat.rgba16Float
    if let caml = layer as? CAMetalLayer {
        caml.wantsExtendedDynamicRangeContent = true
    }
}
```

### Using MTKView 2 — [7:29]

```swift
func draw(in view: MTKView) {

     let size = self.convertToBacking(self.bounds.size)
     let rd = CIRenderDestination(width: Int(size.width),
                                  height: Int(size.height),
                                  pixelFormat: colorPixelFormat,
                                  commandBuffer: nil)
               { () -> MTLTexture in return view.currentDrawable!.texture }

     context.startTask(toRender:image, from:rect, to:rd, at:point)

     // Present the current drawable
     let cmdBuf = commandQueue.makeCommandBuffer()!
     cmdBuf.present(view.currentDrawable!)
     cmdBuf.commit()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10008/6/42FB3921-E69F-4E23-8E73-1AD4191B5877/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10008) — developer.apple.com. Indexed for agent consumption._