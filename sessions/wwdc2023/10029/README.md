---
id: "wwdc2023-10029"
event: "wwdc2023"
year: 2023
title: "Build widgets for the Smart Stack on Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10029"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Build widgets for the Smart Stack on Apple Watch

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10029](https://developer.apple.com/videos/play/wwdc2023/10029)

Follow along as we build a widget for the Smart Stack on watchOS 10 using the latest SwiftUI and WidgetKit APIs. Learn tips, techniques, and best practices for creating widgets that show relevant information on Apple Watch.

**Keywords:** `watchos`, `watchos 10`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,850 words)

## Documentation & Resources

- [Updating your app and widgets for watchOS 10](https://developer.apple.com/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10.json
- [WidgetKit](https://developer.apple.com/documentation/WidgetKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit.json
- [Human Interface Guidelines: Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/widgets

## Code Snippets

### TimelineEntry — [4:15]

```swift
struct SimpleEntry: TimelineEntry {
    var date: Date
    var configuration: ConfigurationAppIntent
    var backyard: Backyard

    var bird: Bird? {
        return backyard.visitorEventForDate(date: date)?.bird
    }

    var waterDuration: Duration {
        return Duration.seconds(abs(self.date.distance(to: self.backyard.waterRefillDate)))
    }

    var foodDuration: Duration {
        return Duration.seconds(abs(self.date.distance(to: self.backyard.foodRefillDate)))
    }

    var relevance: TimelineEntryRelevance? {
        if let visitor = backyard.visitorEventForDate(date: date) {
            return TimelineEntryRelevance(score: 10, duration: visitor.endDate.timeIntervalSince(date))
        }
        return TimelineEntryRelevance(score: 0)
    }
}
```

### placeholder function — [7:50]

```swift
func placeholder(in context: Context) -> SimpleEntry {
  return SimpleEntry(date: Date(), configuration: ConfigurationAppIntent(), backyard: Backyard.anyBackyard(modelContext: modelContext))
}
```

### snapshot function — [8:15]

```swift
func snapshot(for configuration: ConfigurationAppIntent, in context: Context) async -> SimpleEntry {
  if let backyard = Backyard.backyardForID(modelContext: modelContext, backyardID: configuration.backyardID) {
    if let event = backyard.visitorEvents.first {
      return SimpleEntry(date: event.startDate, configuration: configuration, backyard: backyard)
    } else {
      return SimpleEntry(date: Date(), configuration: configuration, backyard: backyard)
    }
  }

  let yard = Backyard.anyBackyard(modelContext: modelContext)
  return SimpleEntry(date: Date(), configuration: ConfigurationAppIntent(), backyard: yard)
}
```

### Widget Entry View — [10:26]

```swift
struct BackyardBirdsWidgetEntryView: View {
    @Environment(\.widgetFamily) private var family
    var entry: SimpleEntry

    var body: some View {
        switch family {
        case .accessoryRectangular:
            RectangularBackyardView(entry: entry)
        default:
            Text(entry.date, style: .time)
        }
    }
}
```

### Backyard Rectangular View — [11:23]

```swift
struct RectangularBackyardView: View {
    var entry: SimpleEntry

    var body: some View {
        HStack {
            if let bird = entry.bird {
                ComposedBird(bird: bird)
                    .scaledToFit()
                    .widgetAccentable()
                    .frame(width: 50, height: 50)
                VStack(alignment: .leading) {
                    Text(bird.speciesName)
                        .font(.headline)
                        .foregroundStyle(bird.colors.wing.color)
                        .widgetAccentable()
                        .minimumScaleFactor(0.75)
                    Text(entry.backyard.name)
                        .minimumScaleFactor(0.75)
                    HStack {
                        Image(systemName: "drop.fill")
                        Text(entry.waterDuration, format: remainingHoursFormatter)
                        Image(systemName: "fork.knife")
                        Text(entry.foodDuration, format: remainingHoursFormatter)
                    }
                    .imageScale(.small)
                    .minimumScaleFactor(0.75)
                    .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity, alignment: .leading)
            } else {
                Image(.fountainFill)
                    .foregroundStyle(entry.backyard.backgroundColor)
                    .imageScale(.large)
                    .scaledToFit()
                    .widgetAccentable()
                    .frame(width: 50, height: 50)
                VStack(alignment: .leading) {
                    Text(entry.backyard.name)
                        .font(.headline)
                        .foregroundStyle(entry.backyard.backgroundColor)
                        .widgetAccentable()
                        .minimumScaleFactor(0.75)
                    HStack {
                        Image(systemName: "drop.fill")
                        Text(entry.waterDuration, format: remainingHoursFormatter)
                        Image(systemName: "fork.knife")
                        Text(entry.foodDuration, format: remainingHoursFormatter)
                    }
                    .imageScale(.small)
                    .minimumScaleFactor(0.75)
                    Text("\(entry.backyard.historicalEvents.count) visitors")
                        .minimumScaleFactor(0.75)
                        .foregroundStyle(.secondary)
                }
                .frame(maxWidth: .infinity, alignment: .leading)
            }
        }
        .containerBackground(entry.backyard.backgroundColor.gradient, for: .widget)
    }
}
```

### Timeline Function — [16:30]

```swift
func timeline(for configuration: ConfigurationAppIntent, in context: Context) async -> Timeline<SimpleEntry> {
  var entries: [SimpleEntry] = []

  if let backyard = Backyard.backyardForID(modelContext: modelContext, backyardID: configuration.backyardID) {
    for event in backyard.visitorEvents {
      let entry = SimpleEntry(date: event.startDate, configuration: configuration, backyard: backyard)
      entries.append(entry)
      let afterEntry = SimpleEntry(date: event.endDate, configuration: configuration, backyard: backyard)
      entries.append(afterEntry)
    }
  }
  return Timeline(entries: entries, policy: .atEnd)
}
```

### Recommendations Function — [18:35]

```swift
func recommendations() -> [AppIntentRecommendation<ConfigurationAppIntent>] {
  var recs = [AppIntentRecommendation<ConfigurationAppIntent>]()

  for backyard in Backyard.allBackyards(modelContext: modelContext) {
    let configIntent = ConfigurationAppIntent()
    configIntent.backyardID = backyard.id.uuidString
    let gardenRecommendation = AppIntentRecommendation(intent: configIntent, description: backyard.name)
    recs.append(gardenRecommendation)
  }

  return recs
}
```

### Relevant Intents Function — [20:47]

```swift
func updateBackyardRelevantIntents() async {
    let modelContext = ModelContext(DataGeneration.container)
    var relevantIntents = [RelevantIntent]()

    for backyard in Backyard.allBackyards(modelContext: modelContext) {

        let configIntent = ConfigurationAppIntent()
        configIntent.backyardID = backyard.id.uuidString
        let relevantFoodDateContext = RelevantContext.date(from: backyard.lowSuppliesDate(for: .food), to: backyard.expectedEmptyDate(for: .food))
        let relevantFoodIntent = RelevantIntent(configIntent, widgetKind: "BackyardVisitorsWidget", relevance: relevantFoodDateContext)
        relevantIntents.append(relevantFoodIntent)

        let relevantWaterDateContext = RelevantContext.date(from: backyard.lowSuppliesDate(for: .water), to: backyard.expectedEmptyDate(for: .water))
        let relevantWaterIntent = RelevantIntent(configIntent, widgetKind: "BackyardVisitorsWidget", relevance: relevantWaterDateContext)
        relevantIntents.append(relevantWaterIntent)
    }

    do {
        try await RelevantIntentManager.shared.updateRelevantIntents(relevantIntents)
    } catch { }
}
```

### Update Relevant Intents — [23:00]

```swift
Task {
  await updateBackyardRelevantIntents()
  WidgetCenter.shared.reloadTimelines(ofKind: "BackyardVisitorsWidget")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10029/5/A6F20D9A-932C-44D8-99FA-FBFE3D6E5CBE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10029/5/A6F20D9A-932C-44D8-99FA-FBFE3D6E5CBE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10029) — developer.apple.com. Indexed for agent consumption._