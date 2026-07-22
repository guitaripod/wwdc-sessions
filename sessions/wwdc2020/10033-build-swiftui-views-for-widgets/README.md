---
id: "wwdc2020-10033"
event: "wwdc2020"
year: 2020
title: "Build SwiftUI views for widgets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10033"
topics: ["App Services", "Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build SwiftUI views for widgets

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10033](https://developer.apple.com/videos/play/wwdc2020/10033)

Widgets are bite-sized pieces of information from your app that someone can choose to place on their home screen or Today view. Discover the process of building the views for a widget from scratch using SwiftUI. Brush up on the syntax that you’ll need for widget-specific construction and learn how to incorporate those commands and customize your widget’s interface for a great glanceable experience. To learn more about widgets, be sure to check out "Meet WidgetKit" and "Widgets Code-along".

**Keywords:** `alignment`, `canvas`, `containerrelativeshape`, `corner radii`, `corner radius`, `declarative`, `dynamic type`, `family`, `hstack`, `lazy shape`, `leading edge`, `placeholder`, `preview`, `spacer`, `swiftui`, `system large`, `system medium`, `system small`, `views`, `vstack`, `widgetkit`, `widgets`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,354 words)

## Documentation & Resources

- [WidgetKit](https://developer.apple.com/documentation/WidgetKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit.json
- [Keeping a widget up to date](https://developer.apple.com/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date.json
- [Creating a widget extension](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Creating-a-Widget-Extension
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Creating-a-Widget-Extension.json
- [Learn more about creating widgets](https://developer.apple.com/widgets/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/widgets/
- [Human Interface Guidelines: Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/widgets
- [Building Widgets Using WidgetKit and SwiftUI](https://developer.apple.com/documentation/WidgetKit/building-widgets-using-widgetkit-and-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/building-widgets-using-widgetkit-and-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/building-widgets-using-widgetkit-and-swiftui.json

## Code Snippets

### Concentric corner radius with ContainerRelativeShape — [18:40]

```swift
// Concentric corner radius with ContainerRelativeShape

struct PillView : View {
    var title: Text
    var color: Color

    var body: some View {
        Text(title)
            .background(ContainerRelativeShape().fill(color))
    }
}
```

### Displaying date and time — [19:09]

```swift
// Displaying date and time

// June 3, 2019
Text(event.startDate, style: .date)

// 11:23PM
Text(event.startDate, style: .time)

// 9:30AM - 3:30PM
Text(event.startDate...event.endDate)

// +2 hours
// -3 months
Text(event.startDate, style: .offset)

// 2 hours, 23 minutes – Automatically updating as time pass
Text(event.startDate, style: .relative)

// 36:59:01 – Automatically updating as time pass
Text(event.startDate, style: .timer)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10033/5/062E0EF4-4132-4E4F-A5E9-807F30DCCBCC/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10033) — developer.apple.com. Indexed for agent consumption._
