---
id: "wwdc2021-10002"
event: "wwdc2021"
year: 2021
title: "What's new in watchOS 8"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10002"
topics: ["Essentials", "Health & Fitness", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["watchOS"]
hasTranscript: true
---

# What's new in watchOS 8

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10002](https://developer.apple.com/videos/play/wwdc2021/10002)

watchOS 8 brings all-new opportunities to keep people up to date on their watch face. With new APIs for the Always-On Retina display and updating complications from Bluetooth devices and background delivery of HealthKit data, it's never been easier to keep your app up to date. Learn about region-based user notifications to leverage location in your app. Explore all the new enhancements to SwiftUI and watchOS that will get you excited to build your next Watch app.

**Keywords:** `🥃`, `⌚️`, `altimeter`, `always-on`, `bluetooth`, `healthkit`, `isluminancereduced`, `location button`, `luminance reduced`, `respiratory rate`, `timeline`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,702 words)

## Documentation & Resources

- [UNLocationNotificationTrigger](https://developer.apple.com/documentation/UserNotifications/UNLocationNotificationTrigger) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/UNLocationNotificationTrigger
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/UNLocationNotificationTrigger.json
- [Updating watchOS apps with timelines](https://developer.apple.com/documentation/watchOS-Apps/updating-watchos-apps-with-timelines) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/updating-watchos-apps-with-timelines
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/updating-watchos-apps-with-timelines.json
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state.json

## Code Snippets

### isLuminanceReduced Environment Property — [2:49]

```swift
@Environment(\.isLuminanceReduced) var isLuminanceReduced
```

### isLuminanceReduced ContentView Preview — [3:01]

```swift
ContentView().environment(\.isLuminanceReduced, true)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10002/4/6AE5C57E-FF72-4A1C-B627-40969B18D70D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10002/4/6AE5C57E-FF72-4A1C-B627-40969B18D70D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10002) — developer.apple.com. Indexed for agent consumption._
