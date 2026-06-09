---
id: "tech-talks-10857"
event: "tech-talks"
year: 2020
title: "Demystify and eliminate hitches in the render phase"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/10857"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Demystify and eliminate hitches in the render phase

**Event:** Tech Talks · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-12-21 · **Session:** [tech-talks-10857](https://developer.apple.com/videos/play/tech-talks/10857)

When you implement complex view hierarchies in your app, you may run into animation hitches. Demystify how your views are turned into pixels during the render phase, and learn how to use Instruments to uncover issues in this part of the render loop. Discover how to eliminate offscreen passes and leverage Xcode optimization opportunities in order to provide a great experience when using your app.

**Keywords:** `animation hitches`, `hitches`, `render phase`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,166 words)

## Code Snippets

### Shadow Path — [0:01]

```swift
// Setup shadow properties
view.layer.shadowColor = UIColor.black.cgColor
view.layer.shadowOpacity = 0.5

// Set a shadow path on a basic layer
view.layer.shadowPath = UIBezierPath(roundedRect: view.layer.bounds, 
                                     cornerRadius: view.layer.cornerRadius).cgPath
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/10857/2/25CEDA38-B91E-45A8-A305-76B8025F8320/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/10857/2/25CEDA38-B91E-45A8-A305-76B8025F8320/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/10857) — developer.apple.com. Indexed for agent consumption._
