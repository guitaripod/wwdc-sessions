---
id: "wwdc2023-10028"
event: "wwdc2023"
year: 2023
title: "Bring widgets to life"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10028"
topics: ["Essentials", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring widgets to life

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10028](https://developer.apple.com/videos/play/wwdc2023/10028)

Learn how to make animated and interactive widgets for your apps and games. We’ll show you how to tweak animations for entry transitions and add interactivity using SwiftUI Button and Toggle so that you can create powerful moments right from the Home Screen and Lock Screen.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,483 words)

## Code Snippets

### Usage for the container background modifier — [3:54]

```swift
.containerBackground(for: .widget) {
    Color.cosmicLatte
}
```

### Define a preview for the caffeine tracker widget — [4:22]

```swift
#Preview(as: WidgetFamily.systemSmall) {
    CaffeineTrackerWidget()
} timeline: {
    CaffeineLogEntry.log1
    CaffeineLogEntry.log2
    CaffeineLogEntry.log3
    CaffeineLogEntry.log4
}
```

### Add a numeric text content transition — [5:41]

```swift
struct TotalCaffeineView: View {
    let totalCaffeine: Measurement<UnitMass>

    var body: some View {
        VStack(alignment: .leading) {
            Text("Total Caffeine")
                .font(.caption)

            Text(totalCaffeine.formatted())
                .font(.title)
                .minimumScaleFactor(0.8)
                .contentTransition(.numericText(value: totalCaffeine.value))
        }
        .foregroundColor(.espresso)
        .bold()
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

### Set up transition on LastDrinkView — [6:21]

```swift
struct LastDrinkView: View {
    let log: CaffeineLog

    var body: some View {
        VStack(alignment: .leading) {
            Text(log.drink.name)
                .bold()
            Text("\(log.date, format: Self.dateFormatStyle) · \(caffeineAmount)")
        }
        .font(.caption)
        .id(log)
        .transition(.push(from: .bottom))
    }

    var caffeineAmount: String {
        log.drink.caffeine.formatted()
    }

    static var dateFormatStyle = Date.FormatStyle(
        date: .omitted, time: .shortened)
}
```

### Configuring animation for the transition — [7:18]

```swift
struct LastDrinkView: View {
    let log: CaffeineLog

    var body: some View {
        VStack(alignment: .leading) {
            Text(log.drink.name)
                .bold()
            Text("\(log.date, format: Self.dateFormatStyle) · \(caffeineAmount)")
        }
        .font(.caption)
        .id(log)
        .transition(.push(from: .bottom))
        .animation(.smooth(duration: 1.8), value: log)
    }

    var caffeineAmount: String {
        log.drink.caffeine.formatted()
    }

    static var dateFormatStyle = Date.FormatStyle(
        date: .omitted, time: .shortened)
}
```

### Reload the timeline for a widget — [9:18]

```swift
WidgetCenter.shared.reloadTimelines(ofKind: "LocationForecast")
```

### App intent to log a caffeine drink — [13:06]

```swift
import AppIntents

struct LogDrinkIntent: AppIntent {
    static var title: LocalizedStringResource = "Log a drink"
    static var description = IntentDescription("Log a drink and its caffeine amount.")

    @Parameter(title: "Drink", optionsProvider: DrinksOptionsProvider())
    var drink: Drink

    init() {}

    init(drink: Drink) {
        self.drink = drink
    }

    func perform() async throws -> some IntentResult {
        await DrinksLogStore.shared.log(drink: drink)
        return .result()
    }
}
```

### Create view to log a new drink — [15:10]

```swift
struct LogDrinkView: View {
    var body: some View {
        Button(intent: LogDrinkIntent(drink: .espresso)) {
            Label("Espresso", systemImage: "plus")
                .font(.caption)
        }
        .tint(.espresso)
    }
}
```

### Use the invalidatable content modifier — [16:28]

```swift
struct TotalCaffeineView: View {
    let totalCaffeine: Measurement<UnitMass>

    var body: some View {
        VStack(alignment: .leading) {
            Text("Total Caffeine")
                .font(.caption)

            Text(totalCaffeine.formatted())
                .font(.title)
                .minimumScaleFactor(0.8)
                .contentTransition(.numericText(value: totalCaffeine.value))
                .invalidatableContent()
        }
        .foregroundColor(.espresso)
        .bold()
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10028/4/3BBB0693-B39D-476B-AC4A-2F1A8BB53FCE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10028/4/3BBB0693-B39D-476B-AC4A-2F1A8BB53FCE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10028) — developer.apple.com. Indexed for agent consumption._