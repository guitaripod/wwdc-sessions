---
id: "wwdc2026-326"
event: "wwdc2026"
year: 2026
title: "Integrate on-device AI models into your app using Core AI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/326"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Integrate on-device AI models into your app using Core AI

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-326](https://developer.apple.com/videos/play/wwdc2026/326)

Discover a curated collection of popular open-source models — including Qwen, Mistral, SAM3, and more — optimized for Apple silicon using the new Core AI Framework. Learn how to download, run, and benchmark models on your Mac, and integrate them into your app with just a few lines of code. Explore a new workflow for model compilation and on-device specialization to speed up first-time model load. Find out how to profile and optimize runtime performance with Core AI tools in Xcode.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,946 words)

## Documentation & Resources

- [Core AI PyTorch Extensions](https://apple.github.io/coreai-torch) _documentation_
- [Core AI Python](https://apple.github.io/coreai-torch/main/coreai-core) _documentation_
- [Core AI Optimization](https://apple.github.io/coreai-optimization) _documentation_
- [Core AI](https://developer.apple.com/documentation/CoreAI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI.json
- [Compiling Core AI models ahead of time](https://developer.apple.com/documentation/CoreAI/compiling-core-ai-models-ahead-of-time) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI/compiling-core-ai-models-ahead-of-time
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI/compiling-core-ai-models-ahead-of-time.json

## Code Snippets

### Load and run SAM3 image segmentation — [11:01]

```swift
import CoreAIImageSegmenter

// Load
let segmenter = try await ImageSegmenter(resourcesAt: sam3ModelURL)

// Use
let response = try await segmenter.segment(image: inputImage, prompt: "flower")
let mask = response.segments.first?.mask
```

### Load a language model and create a session — [11:28]

```swift
import FoundationModels
import CoreAILanguageModels

// Create model instance
let model = try await CoreAILanguageModel(resourcesAt: qwen3ModelURL)

// Create session using the model
let session = LanguageModelSession(model: model)

// Generate response
let response = try await session.respond(to: "...")
```

### Generate structured output with @Generable — [12:29]

```swift
import FoundationModels
import CoreAILanguageModels

@Generable
struct VocabCard {
    let chineseWord: String
    let englishMeaning: String
    let exampleSentence: String
}

let model = try await CoreAILanguageModel(resourcesAt: modelURL)
let session = LanguageModelSession(model: model)
let response = try await session.respond(
    to: "Create a vocab card for flower",
    generating: VocabCard.self
)
let card: VocabCard = response.content
```

### Compile a Core AI model ahead of time — [17:22]

```bash
$ xcrun coreai-build compile MyModel.aimodel --platform iOS
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/326/5/7ff038e2-12cb-4b92-9f49-1d051db7ce5d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/326/5/7ff038e2-12cb-4b92-9f49-1d051db7ce5d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/326) — developer.apple.com. Indexed for agent consumption._