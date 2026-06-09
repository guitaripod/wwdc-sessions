---
id: "wwdc2022-10050"
event: "wwdc2022"
year: 2022
title: "Complications and widgets: Reloaded"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10050"
topics: ["Essentials", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "watchOS"]
hasTranscript: true
---

# Complications and widgets: Reloaded

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10050](https://developer.apple.com/videos/play/wwdc2022/10050)

Our widgets code-along returns as we adventure onto the watchOS and iOS Lock Screen. Learn about the latest improvements to WidgetKit that help power complex complications on watchOS and can help you create Lock Screen widgets for iPhone. We’ll show you how to incorporate the latest SwiftUI views to provide great glanceable data, explore how each platform renders content, and learn how you can customize the design and feel of your content within a widget or complication.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,328 words)

## Documentation & Resources

- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications.json
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations.json
- [WidgetKit](https://developer.apple.com/documentation/WidgetKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit.json

## Code Snippets

### widgetAccentable — [4:07]

```swift
VStack(alignment: .leading) {
    Text("Headline")
        .font(.headline)
        .widgetAccentable()
    Text("Body 1")
    Text("Body 2")
}.frame(maxWidth: .infinity, alignment: .leading)
```

### AccessoryWidgetBackground — [5:24]

```swift
ZStack {
     AccessoryWidgetBackground()
     VStack {
        Text("MON")
        Text("6")
         .font(.title)
    }
}
```

### Xcode Previews — [9:02]

```swift
EmojiRangerWidgetEntryView(entry: SimpleEntry(date: Date(), relevance: nil, character: .spouty))
                .previewContext(WidgetPreviewContext(family: .accessoryCircular))
                .previewDisplayName("Circular")
            EmojiRangerWidgetEntryView(entry: SimpleEntry(date: Date(), relevance: nil, character: .spouty))
                .previewContext(WidgetPreviewContext(family: .accessoryRectangular))
                .previewDisplayName("Rectangular")
            EmojiRangerWidgetEntryView(entry: SimpleEntry(date: Date(), relevance: nil, character: .spouty))
                .previewContext(WidgetPreviewContext(family: .accessoryInline))
                .previewDisplayName("Inline")

#if os(iOS)
```

### recommendations method — [9:38]

```swift
return recommendedIntents()
.map { intent in
    return IntentRecommendation(intent: intent, description: intent.hero!.displayString)
}
```

### ProgressView — [11:05]

```swift
ProgressView(interval: entry.character.injuryDate...entry.character.fullHealthDate,
             countdown: false,
             label: { Text(entry.character.name) },
             currentValueLabel: {
    Avatar(character: entry.character, includeBackground: false)
})
.progressViewStyle(.circular)
```

### Rectangular — [11:26]

```swift
case .accessoryRectangular:
HStack(alignment: .center, spacing: 0) {
    VStack(alignment: .leading) {
        Text(entry.character.name)

        Text("Level \(entry.character.level)")
        Text(entry.character.fullHealthDate, style: .timer)
    }.frame(maxWidth: .infinity, alignment: .leading)
    Avatar(character: entry.character, includeBackground: false)
}
```

### ViewThatFits — [14:03]

```swift
ViewThatFits {
    Text("\(entry.character.name) is resting, combat-ready in \(entry.character.fullHealthDate, style: .relative)")
    Text("\(entry.character.name) ready in \(entry.character.fullHealthDate, style: .timer)")
    Text("\(entry.character.avatar) \(entry.character.fullHealthDate, style: .timer)")
}
```

### isLuminanceReduced — [16:18]

```swift
@Environment(\.isLuminanceReduced)
var isLuminanceReduced

var body: some View {
    if isLuminanceReduced {
        Text("🙈").font(.title)
    } else {
        Text("🐵").font(.title)
    }
}
```

### privacySensitive — [16:52]

```swift
VStack(spacing: -2) {
    Image(systemName: "heart")
        .font(.caption.bold())
        .widgetAccentable()
    Text("\(currentHeartRate)")
        .font(.title)
        .privacySensitive()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10050/5/358B551F-283C-4CD1-8172-DAC014727969/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10050/5/358B551F-283C-4CD1-8172-DAC014727969/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10050) — developer.apple.com. Indexed for agent consumption._