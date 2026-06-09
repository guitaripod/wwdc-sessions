---
id: "wwdc2023-10053"
event: "wwdc2023"
year: 2023
title: "What’s new in privacy"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10053"
topics: ["Spatial Computing", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in privacy

**Event:** WWDC23 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10053](https://developer.apple.com/videos/play/wwdc2023/10053)

At Apple, we believe that privacy is a fundamental human right. Learn about new technologies on Apple platforms that make it easier for you to implement essential privacy patterns that build customer trust in your app. Discover privacy improvements for Apple’s platforms, as well as a study of how privacy shaped the software architecture and design for the input model on visionOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,337 words)

## Documentation & Resources

- [App Sandbox](https://developer.apple.com/documentation/Security/app-sandbox) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Security/app-sandbox
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Security/app-sandbox.json
- [Detecting sensitive content in media and providing intervention options](https://developer.apple.com/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SensitiveContentAnalysis/detecting-nudity-in-media-and-providing-intervention-options.json

## Code Snippets

### Detect sensitive content — [16:00]

```swift
// Analyzing photos

let analyzer = SCSensitivityAnalyzer()
let policy = analyzer.analysisPolicy

let result = try await analyzer.analyzeImage(at: url)
let result = try await analyzer.analyzeImage(image.cgImage!)

// Analyzing videos
let handler = analyzer.videoAnalysis(forFileAt: url)
let result = try await handler.hasSensitiveContent()

if result.isSensitive {
    intervene(policy)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10053/4/8CAD0D27-5BB4-4640-9746-4DCBD46161DF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10053/4/8CAD0D27-5BB4-4640-9746-4DCBD46161DF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10053) — developer.apple.com. Indexed for agent consumption._