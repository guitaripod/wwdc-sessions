---
id: "wwdc2021-10231"
event: "wwdc2021"
year: 2021
title: "Donate intents and expand your app’s presence"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10231"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "watchOS"]
hasTranscript: true
---

# Donate intents and expand your app’s presence

**Event:** WWDC21 · **Topic:** App Services · **Platforms:** iOS, iPadOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10231](https://developer.apple.com/videos/play/wwdc2021/10231)

Discover how you can make key parts of your app available for someone at exactly the right moment — without them ever needing to open it. Learn how to craft and donate intents to the system, helping you surface relevant and contextual information about your app in Siri, Focus, Shortcuts, the Smart Stack, and more. We’ll explore how the system intelligently identifies information and show you techniques for structuring intents to help increase engagement and visibility for your app.

**Keywords:** `intelligence`, `intent`, `shortcuts`, `shortcuts app`, `sirikit`, `sirikit media intents`, `suggestions`, `system intelligence`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,095 words)

## Documentation & Resources

- [Donating Shortcuts](https://developer.apple.com/documentation/SiriKit/donating-shortcuts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/donating-shortcuts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/donating-shortcuts.json

## Code Snippets

### Intent donation example — [0:01]

```swift
// Donate your intent.

let intent = CheckWeatherIntent()
intent.location = weatherLocation

let interaction = INInteraction(intent: intent, response: nil)
interaction.donate { (error) in
    // Handle the error.
}
```

### Intent deletion example — [0:02]

```swift
// Donate your intent.
let interaction = INInteraction(intent: intent, response: response)
interaction.identifier = "68753A44-4D6F-1226-9C60-0050E4C00067"
interaction.groupIdentifier = "san-diego"
interaction.donate { (error) in
    // Handle the error.
}

// Delete individual donations.
INInteraction.delete(with: ["68753A44-4D6F-1226-9C60-0050E4C00067"]) { (error) in
    // Handle the error.
}

// Delete group donations.
INInteraction.delete(with: "san-diego") { (error) in
    // Handle the error.
}
```

### Intent donation example 2 — [0:03]

```swift
// Donate your intent.

let intent = OrderCoffeeIntent()
intent.item = item
intent.size = size
intent.date = date

let interaction = INInteraction(intent: intent, response: nil)
interaction.donate { (error) in
    // Handle the error.
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10231/3/E4613D08-78BF-4C2F-AE4E-E1A4B7A68D78/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10231/3/E4613D08-78BF-4C2F-AE4E-E1A4B7A68D78/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10231) — developer.apple.com. Indexed for agent consumption._