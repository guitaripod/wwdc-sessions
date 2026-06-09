---
id: "wwdc2025-278"
event: "wwdc2025"
year: 2025
title: "What’s new in widgets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/278"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in widgets

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-278](https://developer.apple.com/videos/play/wwdc2025/278)

WidgetKit elevates your app with updates to widgets, Live Activities, and controls. Learn how to bring your widgets to visionOS, take them on the road with CarPlay, and make them look their best with accented rendering modes. Plus, find out how relevant widgets can be surfaced in the Smart Stack on watchOS, and discover how push notifications can be used to keep your widgets up to date.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,796 words)

## Documentation & Resources

- [Updating widgets with WidgetKit push notifications](https://developer.apple.com/documentation/WidgetKit/Updating-widgets-with-widgetkit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Updating-widgets-with-widgetkit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Updating-widgets-with-widgetkit-push-notifications.json
- [Updating your widgets for visionOS](https://developer.apple.com/documentation/WidgetKit/Updating-your-widgets-for-visionOS) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Updating-your-widgets-for-visionOS
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Updating-your-widgets-for-visionOS.json
- [Optimizing your widget for accented rendering mode and Liquid Glass](https://developer.apple.com/documentation/WidgetKit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.json
- [RelevanceKit](https://developer.apple.com/documentation/RelevanceKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RelevanceKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RelevanceKit.json
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks.json

## Code Snippets

### Observe .widgetRenderingMode — [2:44]

```swift
struct MostFrequentBeverageWidgetView: View {
    @Environment(\.widgetRenderingMode) var renderingMode

    var entry: Entry

    var body: some View {
        ZStack {
            if renderingMode == .fullColor {
                Image(entry.beverageImage)
                    .resizable()
                    .aspectRatio(contentMode: .fill)

                LinearGradient(gradient: Gradient(colors: [.clear, .clear, .black.opacity(0.8)]), startPoint: .top, endPoint: .bottom)
            }

            VStack {
                if renderingMode == .accented {
                    Image(entry.beverageImage)
                        .resizable()
                        .widgetAccentedRenderingMode(.desaturated)
                        .aspectRatio(contentMode: .fill)
                }

                BeverageTextView()
            }
        }
    }
}
```

### visionOS Widget Configuration — [6:08]

```swift
struct CaffeineTrackerWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: "BaristaWidget",
            provider: Provider()
        ) { entry in
            CaffeineTrackerWidgetView(entry: entry)
        }
        .configurationDisplayName("Caffeine Tracker")
        .description("A widget tracking your caffeine intake during the day.")
        .supportedMountingStyles([.elevated])
        .widgetTexture(.paper)
        .supportedFamilies([.systemExtraLargePortrait])
    }
}
```

### LevelOfDetail - CaffeineTrackerWidgetView — [8:56]

```swift
struct CaffeineTrackerWidgetView : View {
    @Environment(\.levelOfDetail) var levelOfDetail

    var entry: CaffeineLogEntry

    var body: some View {
        VStack(alignment: .leading) {
            TotalCaffeineView(entry: entry)

            if let log = entry.log {
                LastDrinkView(log: log)
            }

            if levelOfDetail == .default {
                LogDrinkView()
            }
        }
    }
}
```

### LevelOfDetail - TotalCaffeineView — [9:46]

```swift
struct TotalCaffeineView: View {
    @Environment(\.levelOfDetail) var levelOfDetail

    let entry: CaffeineLogEntry

    var body: some View {
        VStack {
            Text("Total Caffeine")
                .font(.caption)

            Text(totalCaffeine.formatted())
                .font(caffeineFont)
        }
    }

    var caffeineFont: Font {
        if levelOfDetail == .simplified {
            .largeTitle
        } else {
            .title
        }
    }

    var totalCaffeine: Measurement<UnitMass> {
        entry.totalCaffeine
    }
}
```

### Add .supplementalActivityFamilies — [11:49]

```swift
struct ShopOrderLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: Attributes.self) { context in
            ActivityView(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    ExpandedView(context: context)
                }
            } compactLeading: {
                LeadingView(context: context)
            } compactTrailing: {
                TrailingView(context: context)
            } minimal: {
                MinimalView(context: context)
            }
        }
        .supplementalActivityFamilies([.small])
    }
}
```

### Add .activityFamily — [12:27]

```swift
struct ActivityView: View {
    @Environment(\.activityFamily) var activityFamily
    var context: ActivityViewContext<Attributes>

    var body: some View {
        switch activityFamily {
        case .small:
            ShopOrderSmallView(context: context)
        default:
            ShopOrderView(context: context)
        }
    }
}
```

### Define relevance widget with RelevanceConfiguration — [16:20]

```swift
struct HappyHourRelevanceWidget: Widget {
    var body: some WidgetConfiguration {
        RelevanceConfiguration(
            kind: "HappyHour",
            provider: Provider()
        ) { entry in
            WidgetView(entry: entry)
        }
    }
}
```

### Implement RelevanceEntriesProvider — [16:41]

```swift
struct Provider: RelevanceEntriesProvider {
    func placeholder(context: Context) -> Entry {
        Entry()
    }

    func relevance() async -> WidgetRelevance<Configuration> {
        let configs = await fetchConfigs()
        var attributes: [WidgetRelevanceAttribute<Configuration>] = []

        for config in configs {
            attributes.append(WidgetRelevanceAttribute(
                configuration: config,
                context: .date(interval: config.interval, kind: .default)))
        }

        return WidgetRelevance(attributes)
    }

    func entry(configuration: Configuration,
               context: RelevanceEntriesProviderContext) async throws -> Entry {
        Entry(shop: configuration.shop, timeRange: configuration.timeRange)
    }
}
```

### Handle push token and widget configuration changes — [21:13]

```swift
struct CaffeineTrackerPushHandler: WidgetPushHandler {
    func pushTokenDidChange(_ pushInfo: WidgetPushInfo, widgets: [WidgetInfo]) {
        // Send push token and subscription info to server
    }
}
```

### Add pushHandler to WidgetConfiguration — [21:30]

```swift
struct CaffeineTrackerWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: Constants.widgetKind,
            provider: Provider()
        ) { entry in
            CaffeineTrackerWidgetView(entry: entry)
        }
        .configurationDisplayName("Caffeine Tracker")
        .pushHandler(CaffeineTrackerPushHandler.self)
    }
}
```

### Push Notification Request Body — [22:29]

```json
{
    "aps": {
        "content-changed": true
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/278/6/2b85cabe-2b0a-4290-a667-9170e4b5ae18/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/278/6/2b85cabe-2b0a-4290-a667-9170e4b5ae18/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/278) — developer.apple.com. Indexed for agent consumption._