---
id: "wwdc2023-10027"
event: "wwdc2023"
year: 2023
title: "Bring widgets to new places"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10027"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Bring widgets to new places

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10027](https://developer.apple.com/videos/play/wwdc2023/10027)

The widget ecosystem is expanding: Discover how you can use the latest WidgetKit APIs to make your widget look great everywhere. We’ll show you how to identify your widget’s background, adjust layout dynamically, and prepare colors for vibrant rendering so that your widget can sit seamlessly in any environment.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,197 words)

## Code Snippets

### SafeAreasWidget — [2:08]

```swift
struct SafeAreasWidgetView: View {
    @Environment(\.widgetContentMargins) var margins

    var body: some View {
        ZStack {
            Color.blue
            Group {
                Color.lightBlue
                Text("Hello, world!")
            }
                .padding(margins) 
        }
    }
}

struct SafeAreasWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(...) {_ in
            SafeAreasWidgetView()
        }
        .contentMarginsDisabled()
    }
}
```

### EmojiRangerWidget systemSmall — [3:19]

```swift
struct EmojiRangerWidgetEntryView: View {
    var entry: Provider.Entry

    @Environment(\.widgetFamily) var family

    var body: some View {
        switch family {
        case .systemSmall:
            ZStack {
                AvatarView(entry.hero)
                    .widgetURL(entry.hero.url)
                    .foregroundColor(.white)
            }
            .containerBackground(for: .widget) {
                Color.gameBackground
            }
        }
        // additional cases
    }
}
```

### EmojiRangerWidget accessoryRectangular — [3:48]

```swift
var body: some View {
    switch family {
    case .accessoryRectangular:
        HStack(alignment: .center, spacing: 0) {
            VStack(alignment: .leading) {
                Text(entry.hero.name)
                    .font(.headline)
                    .widgetAccentable()
                Text("Level \(entry.hero.level)")
                Text(entry.hero.fullHealthDate, style: .timer)
            }.frame(maxWidth: .infinity, alignment: .leading)
            Avatar(hero: entry.hero, includeBackground: false)
        }
        .containerBackground(for: .widget) {
            Color.gameBackground
        }
    // additional cases
}
```

### PhotoWidget — [4:22]

```swift
struct PhotoWidget: Widget {
    public var body: some WidgetConfiguration {
        StaticConfiguration(...) { entry in
            PhotoWidgetView(entry: entry)
        }
        .containerBackgroundRemovable(false)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10027/4/7DEB1A11-79AB-4C43-B6F7-B7525FC746B6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10027/4/7DEB1A11-79AB-4C43-B6F7-B7525FC746B6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10027) — developer.apple.com. Indexed for agent consumption._