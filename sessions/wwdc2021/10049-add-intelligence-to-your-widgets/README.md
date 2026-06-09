---
id: "wwdc2021-10049"
event: "wwdc2021"
year: 2021
title: "Add intelligence to your widgets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10049"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Add intelligence to your widgets

**Event:** WWDC21 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10049](https://developer.apple.com/videos/play/wwdc2021/10049)

Discover how to you can add intelligence to your widgets in Smart Stacks. We'll show you how to use the new Widget Suggestions API in tandem with Smart Rotate to create more valuable widget experiences for people throughout the day. Whether you inform the system of new, timely information or teach the system to learn common patterns, adopting these APIs can help people discover your widget and allows you to influence how the system surfaces content from your app around system spaces.

**Keywords:** `annotating relevance`, `app donation`, `behavioral pattern`, `behavioral relevance`, `configuration intent`, `donate`, `donate new array`, `donate to the system`, `duration`, `glanceable`, `ininteraction`, `inrelevanceprovider`, `inrelevantshortcut`, `insert new widget into smart stack`, `insert widget into stack`, `intelligent widget`, `intent-configured widget`, `intent is eligible for widget`, `ipad home screen widget`, `proactive information`, `relevance signal`, `scroll to a widget`, `siri watch face`, `smart rotate`, `smart stack`, `static widget`, `suggestion ui`, `time-based relevance`, `timelineentryrelevance`, `timely`, `user behavior`, `widgetkind`, `widget suggestion`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,239 words)

## Documentation & Resources

- [TimelineEntry](https://developer.apple.com/documentation/WidgetKit/TimelineEntry) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/TimelineEntry
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/TimelineEntry.json
- [Making a configurable widget](https://developer.apple.com/documentation/WidgetKit/Making-a-Configurable-Widget) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Making-a-Configurable-Widget
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Making-a-Configurable-Widget.json

## Code Snippets

### Donate INRelevantShortcuts for Widget Suggestions — [9:14]

```swift
// Donate INRelevantShortcut for Widget Suggestions in app
// User has just made a purchase

var relevantShortcuts: [INRelevantShortcut] = []

let intent = ViewRecentPurchasesIntent()
intent.card = Card(identifier: card.identifier)
intent.category = .all

if let shortcut = INShortcut(intent: intent) {
    let relevantShortcut = INRelevantShortcut(shortcut: shortcut)
    relevantShortcut.shortcutRole = .information
    relevantShortcut.widgetKind = “CardRecentPurchasesWidget”

    let dateProvider = INDateRelevanceProvider(start: Date(), 
                                               end: Date(timeIntervalSinceNow: 1800))
    relevantShortcut.relevanceProviders = [dateProvider]

    relevantShortcuts.append(relevantShortcut)
}

INRelevantShortcutStore.default.setRelevantShortcuts(relevantShortcuts) { (error) in
    if let error = error {
        print("Failed to set relevant shortcuts. \(error))")
    } else {
        print("Relevant shortcuts set.")
    }
}
```

### Adopting TimelineEntryRelevance for Smart Rotate — [12:35]

```swift
// Appending TimelineEntryRelevance to a TimelineEntry in widget extension for Smart Rotate

struct CardRecentPurchasesEntry: TimelineEntry {
    let date: Date
    let relevance: TimelineEntryRelevance?
    let card: IntentCard?
    let category: PurchaseCategory
}

let relevance = TimelineEntryRelevance(score: 16.29, duration: 1800)
let entry = CardRecentPurchasesEntry(date: Date(), relevance: relevance, card: card,
                                     category: category)
```

### Donate INIntents through INInteraction for Widget Suggestions and Smart Rotations — [17:01]

```swift
// Donate INIntent in a card's purchases list in the app

.onAppear {
    let intent = ViewRecentPurchasesIntent()
    intent.card = Card(identifier: card.id.uuidString, displayString: card.name)
    intent.category = .all

    let interaction = INInteraction(intent: intent, response: nil)
    interaction.donate { error in
        if let error = error {
            print(error.localizedDescription)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10049/5/79001019-5F3C-4B12-A9F7-01FCE02A0381/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10049/5/79001019-5F3C-4B12-A9F7-01FCE02A0381/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10049) — developer.apple.com. Indexed for agent consumption._
