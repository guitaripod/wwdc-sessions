---
id: "wwdc2024-10148"
event: "wwdc2024"
year: 2024
title: "Tailor macOS windows with SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10148"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Tailor macOS windows with SwiftUI

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10148](https://developer.apple.com/videos/play/wwdc2024/10148)

Make your windows feel tailor-made for macOS. Fine-tune your app’s windows for focused purposes, ease of use, and to express functionality. Use SwiftUI to style window toolbars and backgrounds. Arrange your windows with precision, and make smart decisions about restoration and minimization.

**Keywords:** `1984`, `borderless`, `close`, `floating`, `minimize`, `toolbar`, `window`, `windows`, `zoom`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,170 words)

## Documentation & Resources

- [Customizing window styles and state-restoration behavior in macOS](https://developer.apple.com/documentation/SwiftUI/Customizing-window-styles-and-state-restoration-behavior-in-macOS) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Customizing-window-styles-and-state-restoration-behavior-in-macOS
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Customizing-window-styles-and-state-restoration-behavior-in-macOS.json
- [Windows](https://developer.apple.com/documentation/SwiftUI/Windows) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Windows
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Windows.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Destination Video](https://developer.apple.com/documentation/visionOS/destination-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/destination-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/destination-video.json

## Code Snippets

### Style Toolbars - Removing Title — [3:11]

```swift
.toolbar(removing: title)
```

### Style Toolbars - Removing Toolbar Background — [3:14]

```swift
.toolbarBackgroundVisibility(.hidden, for: .windowToolbar)
```

### Refine Behaviors - Adding Container Background — [4:33]

```swift
.containerBackground(.thickMaterial, for: .window)
```

### Refine Behaviors - Minimize Behavior — [5:13]

```swift
.windowMinimizeBehavior(.disabled)
```

### Refine Behaviors - Restoration Behavior — [5:44]

```swift
.restorationBehavior(.disabled)
```

### Adjust Placement - Default Placement — [7:11]

```swift
.defaultWindowPlacement { content, context in
    var size = content.sizeThatFits(.unspecified)
    let displayBounds = context.defaultDisplay.visibleRect
    // modify size based on display bounds
    return WindowPlacement(size: size)
}
```

### Adjust Placement - Ideal Placement — [8:35]

```swift
.windowIdealPlacement { content, context in
    var size = content.sizeThatFits(.unspecified)
    let displayBounds = context.defaultDisplay.visibleRect
    // modify size based on display bounds
    return WindowPlacement(size: size)
}
```

### Borderless Window — [9:48]

```swift
.windowStyle(.plain)
```

### Default Launch Behavior — [9:53]

```swift
.defaultLaunchBehavior(.presented)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10148/4/B76C6719-6B90-4EA9-9EDA-03C08C4A02AA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10148/4/B76C6719-6B90-4EA9-9EDA-03C08C4A02AA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10148) — developer.apple.com. Indexed for agent consumption._
