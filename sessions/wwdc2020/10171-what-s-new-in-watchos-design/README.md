---
id: "wwdc2020-10171"
event: "wwdc2020"
year: 2020
title: "What's new in watchOS design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10171"
topics: ["Design"]
platforms: ["watchOS"]
hasTranscript: true
---

# What's new in watchOS design

**Event:** WWDC20 · **Topic:** Design · **Platforms:** watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10171](https://developer.apple.com/videos/play/wwdc2020/10171)

Great watchOS apps are simple and direct. Actions should be discoverable, predictable and relevant. This session covers effective strategies for displaying actions in your watchOS app, whether they are primary buttons that begin core tasks, or contextual actions that might be less commonly used but are still important to offer. For more on implementing actions with the latest UI frameworks, check out "SwiftUI on watchOS."

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,356 words)

## Documentation & Resources

- [Building a watchOS app](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/building_a_watchos_app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/building_a_watchos_app.json
- [Designing for watchOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-watchos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/Human-Interface-Guidelines/designing-for-watchos

## Code Snippets

### Picker — [5:42]

```swift
List {
    Picker(selection: $viewing
           title: Text("Viewing")) {
       // Viewing options
    }
    // Stocks 
}
```

### onDelete Modifier — [6:27]

```swift
List {
    ForEach(model.locations) {
        ClockCell(location: $0)
    }
    .onDelete { deleteClock(index: $0) }
}
```

### Toolbar — [13:13]

```swift
.toolbar {
    Button(action: newMessage) {
        Label("New Message", 
              systemImage: "square.and.pencil")
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10171/7/6847699B-2742-45B0-8651-9D832223ACFA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10171) — developer.apple.com. Indexed for agent consumption._
