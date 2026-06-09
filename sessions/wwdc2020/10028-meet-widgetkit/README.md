---
id: "wwdc2020-10028"
event: "wwdc2020"
year: 2020
title: "Meet WidgetKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10028"
topics: ["Swift", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet WidgetKit

**Event:** WWDC20 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10028](https://developer.apple.com/videos/play/wwdc2020/10028)

Meet WidgetKit: the best way to bring your app’s most useful information directly to the home screen. We'll show you what makes a great widget and take a look at WidgetKit's features and functionality. Learn how to get started creating a widget, and find out how WidgetKit leverages the power of SwiftUI to provide a stateless experience. Discover how to harness your existing proactive technologies to make sure your widget surfaces relevant material. And create a Timeline that ensures your content is always fresh. For more on creating widgets, check out "Build SwiftUI views for widgets" and "The widgets code-along."

**Keywords:** `duration`, `extension`, `glanceable`, `inintents`, `intent`, `intentconfiguration`, `link api`, `multiplatform`, `personalizable`, `placeholder`, `placeholder ui`, `relevance`, `relevant`, `reload policy`, `reloads`, `reloadtimelines`, `score`, `smart stacks`, `snapshot`, `stateless ui`, `staticconfiguration`, `swiftui`, `timeline`, `timelineentryrelevance`, `widget`, `widgetkit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,614 words)

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
- [Building Widgets Using WidgetKit and SwiftUI](https://developer.apple.com/documentation/widgetkit/building_widgets_using_widgetkit_and_swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/widgetkit/building_widgets_using_widgetkit_and_swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/widgetkit/building_widgets_using_widgetkit_and_swiftui.json

## Code Snippets

### StaticConfiguration Widget definition — [11:01]

```swift
@main
public struct SampleWidget: Widget {
    private let kind: String = "SampleWidget"

    public var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind,
                            provider: Provider(),
                            placeholder: PlaceholderView()) { entry in
                                SampleWidgetEntryView(entry: entry)
                            }
        .configurationDisplayName("My Widget")
        .description("This is an example widget.")
    }
}
```

### TimelineProvider example — [15:51]

```swift
public struct Provider: TimelineProvider {

    public func snapshot(with context: Context, 
                         completion: @escaping (SimpleEntry) -> ()) {
        let entry = SimpleEntry(date: Date())
        completion(entry)
    }

    public func timeline(with context: Context, 
                         completion: @escaping (Timeline<Entry>) -> ()) {
        let entry = SimpleEntry(date: Date())
        let timeline = Timeline(entries: [entry, entry], policy: .atEnd)
        completion(timeline)
    }
}
```

### IntentConfiguration Widget definition — [20:45]

```swift
@main
public struct SampleWidget: Widget {
    private let kind: String = "SampleWidget"

    public var body: some WidgetConfiguration {
        IntentConfiguration(kind: kind,
                    intent: ConfigurationIntent.self
                            provider: Provider(),
                            placeholder: PlaceholderView()) { entry in
                                SampleWidgetEntryView(entry: entry)
                            }
        .configurationDisplayName("My Widget")
        .description("This is an example widget.")
    }
}
```

### IntentTimelineProvider example — [20:54]

```swift
public struct Provider: IntentTimelineProvider {

    public func timeline(for configuration: ConfigurationIntent, with context: Context, 
                         completion: @escaping (Timeline<Entry>) -> ()) {
        let entry = SimpleEntry(date: Date(), configuration: configuration)

        // generate a timeline based on the values of the Intent

       completion(timeline)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10028/5/0329D737-A170-472B-97B9-BFD031C7CD41/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10028) — developer.apple.com. Indexed for agent consumption._
