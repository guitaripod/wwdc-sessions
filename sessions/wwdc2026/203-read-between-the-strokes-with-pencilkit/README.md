---
id: "wwdc2026-203"
event: "wwdc2026"
year: 2026
title: "Read between the strokes with PencilKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/203"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Read between the strokes with PencilKit

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-203](https://developer.apple.com/videos/play/wwdc2026/203)

Unlock handwriting recognition in your apps using the same powerful technology behind Apple apps like Freeform and Notes. Discover how to use handwriting recognition across a wide range of alphabets and languages, and explore new capabilities for integrating PencilKit into a wider variety of apps.

**Keywords:** `🎈`, `pencil`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,641 words)

## Documentation & Resources

- [Controlling stroke rendering for animation and editing](https://developer.apple.com/documentation/PencilKit/controlling-stroke-rendering-for-animation-and-editing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/controlling-stroke-rendering-for-animation-and-editing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/controlling-stroke-rendering-for-animation-and-editing.json
- [Recognizing handwriting and converting it to text](https://developer.apple.com/documentation/PencilKit/recognizing-handwriting-and-converting-to-text) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/recognizing-handwriting-and-converting-to-text
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/recognizing-handwriting-and-converting-to-text.json
- [Building a handwriting recognition experience with PencilKit](https://developer.apple.com/documentation/PencilKit/building-a-handwriting-recognition-experience-with-pencilkit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/building-a-handwriting-recognition-experience-with-pencilkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/building-a-handwriting-recognition-experience-with-pencilkit.json
- [PencilKit](https://developer.apple.com/documentation/PencilKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit.json

## Code Snippets

### Recognized text — [3:53]

```swift
import PencilKit

let recognizer = PKStrokeRecognizer()
await recognizer.updateDrawing(drawing)
myLabel.text = await recognizer.recognizedText()
```

### Indexable content — [5:22]

```swift
import PencilKit

let recognizer = PKStrokeRecognizer()
await recognizer.updateDrawing(drawing)
if let indexedContent = await recognizer.indexableContent {
    index(text: indexedContent)
}
```

### Find text — [6:58]

```swift
import PencilKit

let recognizer = PKStrokeRecognizer()
await recognizer.updateDrawing(drawing)
let results = await recognizer.search("apple")
for result in results {
    highlight(bounds: result.bounds)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/203/4/eb979cd5-af5b-4091-87ec-4839e8d131b9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/203/4/eb979cd5-af5b-4091-87ec-4839e8d131b9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/203) — developer.apple.com. Indexed for agent consumption._
