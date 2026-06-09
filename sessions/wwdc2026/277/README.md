---
id: "wwdc2026-277"
event: "wwdc2026"
year: 2026
title: "WidgetKit foundations"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/277"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# WidgetKit foundations

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-277](https://developer.apple.com/videos/play/wwdc2026/277)

Widgets highlight your app’s most important content across the system, providing people with another opportunity to engage. Discover the different types of widgets and explore the qualities that make them memorable. Learn how to create widgets, keep them up to date, and offer ways for people to customize them through App Intents and dynamic styling.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,271 words)

## Code Snippets

### DailyReadingGoalWidget — [3:50]

```swift
struct DailyReadingGoalWidget: Widget {
    let kind = "DailyReadingGoalWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: kind,
            provider: DailyReadingGoalProvider()
        ) { entry in
            DailyReadingGoalView(book: entry.book,
                                 message: entry.message,
                                 timeOfDay: entry.timeOfDay)
            .environment(\.colorScheme, .dark)
            .containerBackground(for: .widget) {
                Background()
            }
        }
    }
}
```

### Supported Families — [12:25]

```swift
struct DailyReadingGoalWidget: Widget {
    let kind = "DailyReadingGoalWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: kind,
            provider: DailyReadingGoalProvider()
        ) { entry in
            DailyReadingGoalView(book: entry.book,
                                 message: entry.message,
                                 timeOfDay: entry.timeOfDay)
            .environment(\.colorScheme, .dark)
            .containerBackground(for: .widget) {
                Background()
            }
        }
        .supportedFamilies([.systemMedium])
    }
}
```

### Adding deep links — [14:03]

```swift
struct DailyReadingGoalWidget: Widget {
    let kind = "DailyReadingGoalWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: kind,
            provider: DailyReadingGoalProvider()
        ) { entry in
            DailyReadingGoalView(book: entry.book,
                                 message: entry.message,
                                 timeOfDay: entry.timeOfDay)
            .environment(\.colorScheme, .dark)
            .containerBackground(for: .widget) {
                Background()
            }
            .widgetURL(URL(string: "bookclub://reading/\(book.bookID)"))
        }
        .supportedFamilies([.systemMedium])
    }
}
```

### Accented rendering mode — [18:17]

```swift
struct BookCoverImage: View {
    let imageName: String

    var body: some View {
        Image(imageName: bundle: .main)
            .widgetAccentedRenderingMode(.fullColor)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/277/4/e9dd0c7d-3a2e-4cf3-9e65-c9cba19d3616/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/277/4/e9dd0c7d-3a2e-4cf3-9e65-c9cba19d3616/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/277) — developer.apple.com. Indexed for agent consumption._