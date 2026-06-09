---
id: "wwdc2026-237"
event: "wwdc2026"
year: 2026
title: "What’s new in image understanding"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/237"
topics: ["App Services", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in image understanding

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-237](https://developer.apple.com/videos/play/wwdc2026/237)

Unlock powerful image understanding with the latest Vision framework and Foundation Models framework updates. The new tap-to-segment request lets you segment images in new ways, and Vision now supports watchOS. Combine the new image support in Apple Foundation Model together with OCR, barcode scanning and your own tools to deliver LLM-powered visual understanding in your app.

**Keywords:** `ai`, `machine learning &amp; vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,243 words)

## Documentation & Resources

- [Segmenting objects using taps, scribbles or rectangles](https://developer.apple.com/documentation/Vision/segmenting-objects-using-taps-scribbles-or-rectangles) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision/segmenting-objects-using-taps-scribbles-or-rectangles
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision/segmenting-objects-using-taps-scribbles-or-rectangles.json
- [Implementing saliency-based image cropping in iOS and watchOS](https://developer.apple.com/documentation/Vision/implementing-saliency-based-image-cropping-in-iOS-and-watchOS) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision/implementing-saliency-based-image-cropping-in-iOS-and-watchOS
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision/implementing-saliency-based-image-cropping-in-iOS-and-watchOS.json

## Code Snippets

### Segment images (tap-to-segment) — [4:15]

```swift
// Generate a segmentation mask of an object with a seed point
let handler = ImageRequestHandler(image)
let request = GenerateIterativeSegmentationRequest(seed: point)
let observation = try await handler.perform(request)
let mask = observation?.pixelBuffer

// Refine the mask with a new point
request.addIncludedPoint(newPoint)
let refinedObservation = try await handler.perform(request)
```

### Generate an image caption with Foundation Models — [6:41]

```swift
// Generate an image caption with Foundation Models
import FoundationModels

let prompt = Prompt {
    "Generate a caption for this image"
    Attachment(image)
}
let response = try await session.respond(to: prompt)
let caption = response.content
```

### Create an image-based tool — [9:55]

```swift
// Create an image-based tool
struct PlantIdentifierTool: Tool {
    @SessionProperty(\.history) var history

    @Generable
    struct Arguments {
        var image: ImageReference
    }

    func call(arguments: Arguments) async throws -> String {
        let imageReference = arguments.image
        let transcript = Transcript(history)
        guard let imageAttachment = imageReference.resolve(in: transcript) else {
            throw AppError.imageNotFound
        }
        let image = try imageAttachment.pixelBuffer()
        return classifyPlant(image)
    }
}
```

### Use Vision tools — [12:09]

```swift
// Use Vision tools
import FoundationModels
import Vision

let session = LanguageModelSession(model: model, tools: [BarcodeReaderTool()])
let response = try await session.respond(generating: EventInfo.self) {
    "Get the date, location, and website from this flyer"
    Attachment(image)
        .label("flyer")
}
```

### Create a crop that highlights a prominent subject (watchOS / saliency) — [13:54]

```swift
// Create a crop that highlights a prominent subject
func generateImageCrop(in image: CGImage) async throws -> NormalizedRect? {
    let request = GenerateObjectnessBasedSaliencyImageRequest()
    let observation = try await request.perform(on: image)
    let prominentObjects = observation.salientObjects
    return prominentObjects.first
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/237/6/a3bdea1e-5c1d-44bc-8c21-9e1958774bd3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/237/6/a3bdea1e-5c1d-44bc-8c21-9e1958774bd3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/237) — developer.apple.com. Indexed for agent consumption._