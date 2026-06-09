---
id: "wwdc2026-310"
event: "wwdc2026"
year: 2026
title: "What’s new in Shortcuts"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/310"
topics: ["AI & Machine Learning", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Shortcuts

**Event:** WWDC26 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-310](https://developer.apple.com/videos/play/wwdc2026/310)

Explore techniques to build powerful shortcuts using your app’s content. New automations unlock additional ways to integrate your app with the system. Refine how your App Entity is presented to LLMs using the new “Use Model” transcript feature. Store rich information from your app inside shortcuts that is synced across devices. Learn how to combine these features to create intelligent, powerful automations that integrate seamlessly with content and features from your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,704 words)

## Documentation & Resources

- [Shortcuts](https://developer.apple.com/shortcuts/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/shortcuts/
- [Notifications](https://developer.apple.com/design/Human-Interface-Guidelines/notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/Human-Interface-Guidelines/notifications

## Code Snippets

### Soup Entity Example — [6:12]

```swift
// MARK: - Soup Entity

import AppIntents

struct SoupEntity: AppEntity, Identifiable {
    static var typeDisplayRepresentation = TypeDisplayRepresentation(
        name: "Soup",
        numericFormat: "\(placeholder: .int) soups"
    )
    static var defaultQuery = SoupEntityQuery()

    var id: Soup.ID

    @Property var name: String

    @Property(title: "Available Today")
    var isAvailableToday: Bool

    @Property(title: "Ingredients")
    var ingredients: String

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)", subtitle: SoupStore.description(for: id))
    }
}
```

### Soup Entity Example — [10:05]

```swift
// MARK: - Soup Entity

import AppIntents

struct SoupEntity: AppEntity, Identifiable {
    static var typeDisplayRepresentation = TypeDisplayRepresentation(
        name: "Soup",
        numericFormat: "\(placeholder: .int) soups"
    )
    static var defaultQuery = SoupEntityQuery()

    var id: Soup.ID

    @Property var name: String

    @Property(title: "Available Today")
    var isAvailableToday: Bool

    @Property(title: "Ingredients")
    var ingredients: String

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)", subtitle: SoupStore.description(for: id))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/310/4/50ce70ab-88da-49ff-8c57-d9136d231e76/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/310/4/50ce70ab-88da-49ff-8c57-d9136d231e76/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/310) — developer.apple.com. Indexed for agent consumption._