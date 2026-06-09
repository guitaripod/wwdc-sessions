---
id: "wwdc2022-10140"
event: "wwdc2022"
year: 2022
title: "What's new in SharePlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10140"
topics: ["Audio & Video", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# What's new in SharePlay

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10140](https://developer.apple.com/videos/play/wwdc2022/10140)

Join us as we share the latest updates to SharePlay. We’ll show you how you can start SharePlay sessions right from your app, take you through improvements to APIs to create richer experiences, and check out enhancements to GroupSessionMessenger. We’ll also explore best practices for adding SharePlay to your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,281 words)

## Documentation & Resources

- [Human Interface Guidelines: SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay/overview/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/shareplay/overview/
- [SharePlay for Developers](https://developer.apple.com/shareplay/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/shareplay/

## Code Snippets

### Register GroupActivity — [2:06]

```swift
// Register GroupActivity
let itemProvider = NSItemProvider()
itemProvider.registerGroupActivity(WatchTogether())

// Provide the ItemProvider to the ShareSheet
let configuration = UIActivityItemsConfiguration(itemProviders: [itemProvider])

UIActivityViewController(activityItemsConfiguration: configuration)
```

### Not as prominent — [2:14]

```swift
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)

// Show SharePlay non-prominently
shareSheet.allowsProminentActivity = false
```

### Exclude — [2:15]

```swift
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)

// Exclude SharePlay activity
shareSheet.excludedActivityTypes = [.sharePlay]
```

### Show your own button to start SharePlay — [2:44]

```swift
let controller = GroupActivitySharingController(WatchTogetherActivity())
present(controller, animated: true)
```

### Stroke Gesture — [8:21]

```swift
var strokeGesture: some Gesture {
    DragGesture()
        .onChanged { value in
            canvas.addPointToActiveStroke(value.location)
        }
        .onEnded { value in
            canvas.addPointToActiveStroke(value.location)
            canvas.finishStroke()
        }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10140/3/7F5B5E00-19E6-4DBE-A169-044C9D0418F0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10140/3/7F5B5E00-19E6-4DBE-A169-044C9D0418F0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10140) — developer.apple.com. Indexed for agent consumption._