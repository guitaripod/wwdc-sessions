---
id: "wwdc2026-212"
event: "wwdc2026"
year: 2026
title: "Rev up your CarPlay app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/212"
topics: ["System Services"]
platforms: ["iOS"]
hasTranscript: true
---

# Rev up your CarPlay app

**Event:** WWDC26 · **Topic:** System Services · **Platforms:** iOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-212](https://developer.apple.com/videos/play/wwdc2026/212)

Explore new features for your CarPlay audio, navigation, voice-based conversational apps, and more. Discover how to create CarPlay video apps so people can browse and watch their favorite videos in supported vehicles when parked. Learn how to integrate thumbnails, media information, and voice controls in your CarPlay app.

**Keywords:** `🚗`, `🚙`, `car`, `instrument cluster`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,617 words)

## Documentation & Resources

- [CarPlay for developers](https://developer.apple.com/carplay) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/carplay

## Code Snippets

### Disable the MiniPlayer — [6:45]

```swift
// Disable the MiniPlayer

CPNowPlayingTemplate.shared.allowsMiniPlayer = false
```

### Enable route sharing — [15:06]

```swift
// Enable route sharing

func mapTemplateShouldProvideRouteSharing(_ mapTemplate: CPMapTemplate) -> Bool { true }
```

### Disable route sharing for this trip — [15:12]

```swift
// Disable route sharing for this trip

trip.routeSegmentsAvailableForRegion = false
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/212/4/c594f5de-1012-4f5a-bad4-95ca200f5f58/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/212/4/c594f5de-1012-4f5a-bad4-95ca200f5f58/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/212) — developer.apple.com. Indexed for agent consumption._