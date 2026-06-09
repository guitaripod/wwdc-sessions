---
id: "wwdc2021-10040"
event: "wwdc2021"
year: 2021
title: "Detect people, faces, and poses using Vision"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10040"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Detect people, faces, and poses using Vision

**Event:** WWDC21 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10040](https://developer.apple.com/videos/play/wwdc2021/10040)

Discover the latest updates to the Vision framework to help your apps detect people, faces, and poses. Meet the Person Segmentation API, which helps your app separate people in images from their surroundings, and explore the latest contiguous metrics for tracking pitch, yaw, and the roll of the human head. And learn how these capabilities can be combined with other APIs like Core Image to deliver anything from simple virtual backgrounds to rich offline compositing in an image-editing app. To get the most out of this session, we recommend watching “Detect Body and Hand Pose with Vision” from WWDC20 and “Understanding Images in Vision Framework” from WWDC19. To learn even more about people analysis, see “Detect Body and Hand Pose with Vision” from WWDC20 and “Understanding Images in Vision Framework” from WWDC19.

**Keywords:** `ai`, `body pose`, `computer vision`, `core ml`, `face capture quality`, `face detection`, `face landmarks`, `hand pose`, `machine learning`, `person segmentation`, `segmentation`, `vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,751 words)

## Documentation & Resources

- [Applying Matte Effects to People in Images and Video](https://developer.apple.com/documentation/Vision/applying-matte-effects-to-people-in-images-and-video) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision/applying-matte-effects-to-people-in-images-and-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision/applying-matte-effects-to-people-in-images-and-video.json
- [Vision](https://developer.apple.com/documentation/Vision) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision.json

## Code Snippets

### Get segmentation mask from an image — [8:13]

```swift
// Create request 
let request = VNGeneratePersonSegmentationRequest()

// Create request handler
let requestHandler = VNImageRequestHandler(url: imageURL, options: options)

// Process request
try requestHandler.perform([request])

// Review results
let mask = request.results!.first!
let maskBuffer = mask.pixelBuffer
```

### Configuring the segmentation request — [8:33]

```swift
let request = VNGeneratePersonSegmentationRequest()

request.revision = 
VNGeneratePersonSegmentationRequestRevision1

request.qualityLevel = 
VNGeneratePersonSegmentationRequest.QualityLevel.accurate

request.outputPixelFormat = 
kCVPixelFormatType_OneComponent8
```

### Applying a segmentation mask — [12:24]

```swift
let input = CIImage?(contentsOf: imageUrl)!
let mask = CIImage(cvPixelBuffer: maskBuffer)
let background = CIImage?(contentsOf: backgroundImageUrl)!

let maskScaleX = input.extent.width / mask.extent.width
let maskScaleY = input.extent.height / mask.extent.height
let maskScaled = mask.transformed(by: __CGAffineTransformMake(
                                  maskScaleX, 0, 0, maskScaleY, 0, 0))

let backgroundScaleX = input.extent.width / background.extent.width
let backgroundScaleY = input.extent.height / background.extent.height
let backgroundScaled = background.transformed(by: __CGAffineTransformMake(
                          backgroundScaleX, 0, 0, backgroundScaleY, 0, 0))

let blendFilter = CIFilter.blendWithRedMask()
blendFilter.inputImage = input
blendFilter.backgroundImage = backgroundScaled 
blendFilter.maskImage = maskScaled

let blendedImage = blendFilter.outputImage
```

### Segmentation from AVCapture — [14:37]

```swift
private let photoOutput = AVCapturePhotoOutput()
…
if self.photoOutput.isPortraitEffectsMatteDeliverySupported {
   self.photoOutput.isPortraitEffectsMatteDeliveryEnabled = true
}

open class AVCapturePhoto {
…
var portraitEffectsMatte: AVPortraitEffectsMatte? { get } // nil if no people in the scene
…
}
```

### Segmentation in ARKit — [14:58]

```swift
if ARWorldTrackingConfiguration.supportsFrameSemantics(.personSegmentationWithDepth) {
// Proceed with getting Person Segmentation Mask
…
}

open class ARFrame {
…
var segmentationBuffer: CVPixelBuffer? { get }
…
}
```

### Segmentation in CoreImage — [15:31]

```swift
let input = CIImage?(contentsOf: imageUrl)!

let segmentationFilter = CIFilter.personSegmentation()
segmentationFilter.inputImage = input

let mask = segmentationFilter.outputImage
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10040/3/F855147A-D789-4E63-81CE-5050A5A3DB14/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10040/3/F855147A-D789-4E63-81CE-5050A5A3DB14/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10040) — developer.apple.com. Indexed for agent consumption._
