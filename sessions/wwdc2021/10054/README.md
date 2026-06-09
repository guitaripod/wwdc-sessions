---
id: "wwdc2021-10054"
event: "wwdc2021"
year: 2021
title: "What's new in AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10054"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# What's new in AppKit

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10054](https://developer.apple.com/videos/play/wwdc2021/10054)

Explore the latest advancements in Mac app development with AppKit. We’ll show how you can enhance your app’s design with new control features and SF Symbols 3, build powerful text experiences using TextKit 2, and harness the latest Swift features in your app.

**Keywords:** `aqua`, `cocoa`, `shortcuts`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,363 words)

## Documentation & Resources

- [Introducing SF Symbols](https://developer.apple.com/wwdc19/206) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/wwdc19/206
- [Human Interface Guidelines: SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/sf-symbols
- [AppKit](https://developer.apple.com/documentation/AppKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit.json

## Code Snippets

### Determining a button's background style — [4:18]

```swift
class NSButtonCell {
    /*
        Use to adjust your drawing for the underlying state of the bezel

        Returns .normal for colorless states

        Returns .emphasized for colorful/emphasis states
    */
    var interiorBackgroundStyle: NSBackgroundStyle
}
```

### Pick a color — [14:40]

```swift
@IBAction func pickColor(_ sender: Any?) {
    Task {
        guard let color = await NSColorSampler().sample() else { return }
        textField.textColor = color
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10054/7/D3581025-DC73-47FB-98A0-0C9599FAD509/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10054/7/D3581025-DC73-47FB-98A0-0C9599FAD509/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10054) — developer.apple.com. Indexed for agent consumption._