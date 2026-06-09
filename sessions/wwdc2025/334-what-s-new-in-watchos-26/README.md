---
id: "wwdc2025-334"
event: "wwdc2025"
year: 2025
title: "What’s new in watchOS 26"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/334"
topics: ["Health & Fitness", "Maps & Location", "SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# What’s new in watchOS 26

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-334](https://developer.apple.com/videos/play/wwdc2025/334)

Discover the new features in watchOS 26 and learn how to integrate them into your watchOS and iOS apps. Explore the ARM64 architecture, and dive into the new design system. We’ll also share updates for widgets and insights on how to bring controls to Apple Watch.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,757 words)

## Documentation & Resources

- [Workouts and activity rings](https://developer.apple.com/documentation/HealthKit/workouts-and-activity-rings) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/workouts-and-activity-rings
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/workouts-and-activity-rings.json
- [Creating controls to perform actions across the system](https://developer.apple.com/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system.json
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Converting-A-ClockKit-App
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Converting-A-ClockKit-App.json
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks.json
- [Making a configurable widget](https://developer.apple.com/documentation/WidgetKit/Making-a-Configurable-Widget) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Making-a-Configurable-Widget
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Making-a-Configurable-Widget.json
- [MapKit](https://developer.apple.com/documentation/MapKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKit.json

## Code Snippets

### Make a widget configurable — [6:53]

```swift
// In the AppIntentTimelineProvider
func recommendations() -> [AppIntentRecommendation<BeachConfigurationIntent>] {
  return []
}
```

### Support earlier versions of watchOS with a configurable widget — [7:06]

```swift
// In the AppIntentTimelineProvider
func recommendations() -> [AppIntentRecommendation<BeachConfigurationIntent>] {
  if #available(watchOS 26, *) {
    // Return an empty array to allow configuration of the widget in watchOS 12+
    return []
  } else {
    // Return array of recommendations for preconfigured widgets before watchOS 12
    return recommendedBeaches
  }
}
```

### Use AppIntentControlConfiguration to make a control configurable — [7:46]

```swift
struct ConfigurableMeditationControl: ControlWidget {
  var body: some ControlWidgetConfiguration {
    AppIntentControlConfiguration(
      kind: WidgetKinds.configurableMeditationControl,
      provider: Provider()
    ) { value in
      // Provide the control's content
    }
    .displayName("Ocean Meditation")
    .description("Meditation with optional ocean sounds.")
    .promptsForUserConfiguration()
  }
}
```

### Use AppIntentControlValueProvider for a configurable control — [7:56]

```swift
extension ConfigurableMeditationControl {
  struct Provider: AppIntentControlValueProvider {
    func previewValue(configuration: TimerConfiguration) -> Value {
      // Return the value to show in the add sheet
    }

    func currentValue(configuration: TimerConfiguration) async throws -> Value {
      // Return the control's value
    }
  }
}
```

### Relevance for a point-of-interest category — [10:53]

```swift
func relevance() async -> WidgetRelevance<Void> {
  guard let context = RelevantContext.location(category: .beach) else {
    return WidgetRelevance<Void>([])
  }
  return WidgetRelevance([WidgetRelevanceAttribute(context: context)])
}
```

### Implement the relevance method in the RelevanceEntriesProvider — [14:37]

```swift
struct BeachEventRelevanceProvider: RelevanceEntriesProvider {
  let store: BeachEventStore

  func relevance() async -> WidgetRelevance<BeachEventConfigurationIntent> {
    // Associate configuration intents with RelevantContexts
    let attributes = events.map { event in
      WidgetRelevanceAttribute(
        configuration: BeachEventConfigurationIntent(event: event),
        context: .date(interval: event.date, kind: .default)
      )
    }

    return WidgetRelevance(attributes)
  }
}
```

### Create a RelevanceEntry when the widget is relevant — [15:09]

```swift
struct BeachEventRelevanceProvider: RelevanceEntriesProvider {
  func relevance() async -> WidgetRelevance<BeachEventConfigurationIntent> {
    // Return relevance information for the widget
  }

  func entry(
    configuration: BeachEventConfigurationIntent,
    context: Context
  ) async throws -> BeachEventRelevanceEntry {
    if context.isPreview {
      return .previewEntry
    }
    return BeachEventRelevanceEntry(
      event: configuration.event
    )
  }
}
```

### Create a placeholder entry to display when the widget is loading — [15:55]

```swift
struct BeachEventRelevanceProvider: RelevanceEntriesProvider {
  func relevance() async -> WidgetRelevance<BeachEventConfigurationIntent> {
    // Return relevance information for the widget
  }

  func entry(
    configuration: BeachEventConfigurationIntent,
    context: Context
  ) async throws -> BeachEventRelevanceEntry {
    // Return the entry for the configuration
  }

  func placeholder(context: Context) -> BeachEventRelevanceEntry {
    BeachEventRelevanceEntry.placeholderEntry
  }
}
```

### Use a RelevanceConfiguration to create a relevant widget — [16:27]

```swift
struct BeachEventWidget: Widget {
  private let model = BeachEventStore.shared

  var body: some WidgetConfiguration {
    RelevanceConfiguration
      kind: "BeachWidget
      provider: BeachEventRelevanceProvider(store: model)
    ) { entry in
      BeachWidgetView(entry: entry)
    }
    .configurationDisplayName("Beach Events")
    .description("Events at the beach")
  }
}
```

### Use associatedKind to relate the relevant widget to the timeline widget — [17:31]

```swift
struct BeachEventWidget: Widget {
  private let model = BeachEventStore.shared

  var body: some WidgetConfiguration {
    RelevanceConfiguration
      kind: "BeachWidget
      provider: BeachEventRelevanceProvider(store: model)
    ) { entry in
      BeachWidgetView(entry: entry)
    }
    .configurationDisplayName("Beach Events")
    .description("Events at the beach")
    .associatedKind(WidgetKinds.beachEventsTimeline)
  }
}
```

### Create a Preview with relevanceEntries — [18:06]

```swift
#Preview("Entries") {
  BeachEventWidget()
} relevanceEntries: {
  BeachEventRelevanceEntry.previewShorebirds
  BeachEventRelevanceEntry.previewMeditation
}
```

### Create a Preview with relevance — [18:26]

```swift
#Preview("Provider and Relevance") {
  BeachEventWidget()
} relevanceProvider: {
  BeachEventRelevanceProvider(store: .preview)
} relevance: {
  let configurations: [BeachEventConfigurationIntent] = [
    .previewSurfing,
    .previewMeditation,
    .previewWalk
  ]
  let attributes = configurations.map {
    WidgetRelevanceAttribute(
      configuration: $0,
      context: .date($0.event.startDate, kind: .default)
    )
  }
  return WidgetRelevance(attributes)
}
```

### Create a Preview with a relevanceProvider — [18:47]

```swift
#Preview("Provider") {
  BeachEventWidget()
} relevanceProvider: {
  BeachEventRelevanceProvider(store: .preview)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/334/6/578bf261-7e37-4689-a465-bd1300c0f908/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/334/6/578bf261-7e37-4689-a465-bd1300c0f908/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/334) — developer.apple.com. Indexed for agent consumption._
