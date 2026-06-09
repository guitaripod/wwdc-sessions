---
id: "wwdc2026-252"
event: "wwdc2026"
year: 2026
title: "Design no-code games with Reality Composer Pro 3"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/252"
topics: ["Developer Tools", "Graphics & Games", "Spatial Computing", "Design"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Design no-code games with Reality Composer Pro 3

**Event:** WWDC26 · **Topic:** Design · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-252](https://developer.apple.com/videos/play/wwdc2026/252)

Discover how you can use ScriptGraph in Reality Composer Pro 3 to create no-code 3D content for your apps and games. Learn how to take advantage of visual nodes to build animations, create interactive moments, and incorporate SwiftUI elements to add speech bubbles and other UI to your experience.

**Keywords:** `apple vision pro`, `game design`, `reality composer pro`, `realitykit`, `squirrel game`, `visionos`, `visionos games`, `vision pro`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,789 words)

## Code Snippets

### Squirrel Talk — [17:23]

```swift
// Advanced techniques

if let scene = entity.scene {
    scene.subscribe(forEventName: "squirrelTalk", on: { event in
        if let sayThis: String = try? event.value("sayThis") {
            self.sayThis = sayThis
        }
     } ).store(in: &cancellables)
}

...
} attachments: {
    Attachment(id: "squirrelTalk") {
        SquirrelTalkAttachmentView(text: sayThis)
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/252/6/572c2388-69f6-4e57-9eba-c71b65f5f6ed/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/252/6/572c2388-69f6-4e57-9eba-c71b65f5f6ed/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/252) — developer.apple.com. Indexed for agent consumption._