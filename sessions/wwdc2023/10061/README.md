---
id: "wwdc2023-10061"
event: "wwdc2023"
year: 2023
title: "Verify app dependencies with digital signatures"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10061"
topics: ["App Services", "Essentials", "System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Verify app dependencies with digital signatures

**Event:** WWDC23 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10061](https://developer.apple.com/videos/play/wwdc2023/10061)

Discover how you can help secure your app’s dependencies. We’ll show you how Xcode can automatically verify any signed XCFrameworks you include within a project. Learn how code signatures work, the benefits they provide to help protect your software supply chain, and how SDK developers can sign their XCFrameworks to help keep your apps secure.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,149 words)

## Documentation & Resources

- [Verifying the origin of your XCFrameworks](https://developer.apple.com/documentation/Xcode/verifying-the-origin-of-your-xcframeworks) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/verifying-the-origin-of-your-xcframeworks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/verifying-the-origin-of-your-xcframeworks.json

## Code Snippets

### Signing an XCFramework — [14:37]

```bash
codesign --timestamp -v --sign "Apple Distribution: Truck to Table (UA527FUGW7)" BirdFeeder.xcframework
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10061/4/69744A23-9D87-4A87-B1D5-DC13BE88274F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10061/4/69744A23-9D87-4A87-B1D5-DC13BE88274F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10061) — developer.apple.com. Indexed for agent consumption._