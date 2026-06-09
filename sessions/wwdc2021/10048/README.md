---
id: "wwdc2021-10048"
event: "wwdc2021"
year: 2021
title: "Principles of great widgets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10048"
topics: ["Essentials", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Principles of great widgets

**Event:** WWDC21 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10048](https://developer.apple.com/videos/play/wwdc2021/10048)

Explore the foundations of great widgets by keeping them relevant and customizable. Learn how to keep widgets up to date with timeline entries and TimelineReloadPolicies. Discover how to adapt your widget to different presentation environments and physical location. And lastly, find out how to create customizable widgets that someone can personalize to their liking.

**Keywords:** `afterdate`, `atend`, `budget`, `cllocationmanager`, `configurable parameters`, `customizable`, `customization`, `extension`, `extra large widget`, `full privacy redaction`, `intentconfiguration`, `intenttimelineprovider`, `isauthorizedforwidgetupdates`, `keep widget up to date`, `location changes`, `never`, `new ipad widget`, `notifications`, `nswidgetuseslocation`, `partial privacy redaction`, `presentation`, `.privacysensitive`, `relevant`, `reload policy`, `reloads`, `staticconfiguration`, `static configuration`, `swiftui`, `.systemextralarge`, `system extra large`, `timeline`, `timelineprovider`, `timelinereloadpolicy`, `update`, `widgetcenter`, `widgetcenter reload api`, `widget configuration platter`, `widget kind`, `widgetkit`, `widget lock screen`, `widgets`, `widget update`, `xcode previews`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,269 words)

## Documentation & Resources

- [Making a configurable widget](https://developer.apple.com/documentation/WidgetKit/Making-a-Configurable-Widget) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Making-a-Configurable-Widget
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Making-a-Configurable-Widget.json
- [Keeping a widget up to date](https://developer.apple.com/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date.json

## Code Snippets

### Xcode Previews for Widget Views with Color Scheme Overrides — [15:46]

```swift
struct MyWidgetEntryView : View {
    var date: Date

    var body: some View {
        ZStack {
            Rectangle().fill(BackgroundStyle())
            VStack {
                Text("Hello")
            }
        }
    }
}

struct MyWidget_Previews: PreviewProvider {
    static var previews: some View {
        MyWidgetEntryView(date: Date())
            .previewContext(WidgetPreviewContext(family: .systemSmall))
            .environment(\.colorScheme, .dark)
    }
}
```

### Widget Partial Privacy Redactions - Banking Example — [16:34]

```swift
struct MyWidgetEntryView : View {

    var body: some View {
        ZStack {
            Rectangle().fill(BackgroundStyle())
            VStack(alignment: .leading) {
                Text("Balance")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .foregroundColor(Color.blue)
                Text("$128.45")
                    .privacySensitive()
                    .font(.title2)
                    .foregroundColor(Color.gray)
            }
        }
    }
}
```

### WidgetBundle Example — [23:08]

```swift
struct IndividualSymbolWidget : Widget {
    var body: some WidgetConfiguration {
    …
}
}

struct StocksOverviewWidget : Widget {
    var body: some WidgetConfiguration {
    …
    }
}

@main
struct MyWidgetBundle: WidgetBundle {
    var body: some Widget {
        // Order of these widgets defines the order in the Widget Gallery
        IndividualSymbolWidget()
        StocksOverviewWidget()
    }
}
```

### Static Widget Configuration Example — [25:43]

```swift
@main
public struct SampleWidget: Widget {
    public var body: some WidgetConfiguration {
        StaticConfiguration(kind: "com.sample.myStaticSampleWidgetKind",
                            provider: Provider()) { entry in
                                SampleWidgetEntryView(entry: entry)
                            }
        .configurationDisplayName("My Widget")
        .description("This is an example widget.")
    }
}

public struct Provider: TimelineProvider {
    public func timeline(with context: Context,
                         completion: @escaping (Timeline<Entry>) -> ()) {
        let entry = SimpleEntry(date: Date())
        // TODO: Generate a timeline entry
        completion(timeline)
    }
}
```

### Intent Widget Configuration Example — [25:55]

```swift
@main
public struct SampleWidget: Widget {
    public var body: some WidgetConfiguration {
        IntentConfiguration(kind: "com.sample.myIntentSampleWidgetKind",
                            intent: SampleConfigurationIntent.self
                            provider: Provider()) { entry in
                                SampleWidgetEntryView(entry: entry)
                            }
        .configurationDisplayName("My Widget")
        .description("This is an example widget.")
    }
}

public struct Provider: IntentTimelineProvider {
    public func timeline(for configuration: SampleConfigurationIntent, with context: Context,
                         completion: @escaping (Timeline<Entry>) -> ()) {
        let entry = SimpleEntry(date: Date(), configuration: configuration)
        // generate a timeline
        completion(timeline)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10048/6/DE8F1516-0148-4630-A824-44F1BA28F5AA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10048/6/DE8F1516-0148-4630-A824-44F1BA28F5AA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10048) — developer.apple.com. Indexed for agent consumption._