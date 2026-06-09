---
id: "wwdc2026-256"
event: "wwdc2026"
year: 2026
title: "Discover generated subtitles and subtitle styles"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/256"
topics: ["Accessibility & Inclusion", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Discover generated subtitles and subtitle styles

**Event:** WWDC26 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-256](https://developer.apple.com/videos/play/wwdc2026/256)

Make your video content more accessible with generated subtitles — a powerful new feature that can transcribe spoken audio or translate subtitles from another language, using on-device models. Explore caption style preview, which lets people customize and preview subtitle styles during playback, and dive into implementation details for AVKit, AVPlayerLayer, and the Media Accessibility framework.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,378 words)

## Documentation & Resources

- [What's new in HTTP Live Streaming](https://developer.apple.com/streaming/Whats-new-HLS.pdf) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/Whats-new-HLS.pdf

## Code Snippets

### Implement subtitle style preview — [7:43]

```swift
// Implement subtitle style preview

import AVFoundation
import MediaAccessibility

func updateProfileList() {
    subtitleStyleProfileIDs = MACaptionAppearanceCopyProfileIDs() as? [String] ?? []
}

func showPreviewStyle(subtitleStyleProfileID: String) {
    playerLayer.setCaptionPreviewProfileID(subtitleStyleProfileID, position: .zero, text: nil)
}

func stopPreviewStyle() {
    playerLayer.stopShowingCaptionPreview()
}

func setSubtitleStyle(subtitleStyleProfileID: CFString) {
    MACaptionAppearanceSetActiveProfileID(subtitleStyleProfileID)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/256/4/d28efb5e-5550-468d-b1d1-caec51ce55e6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/256/4/d28efb5e-5550-468d-b1d1-caec51ce55e6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/256) — developer.apple.com. Indexed for agent consumption._