---
id: "wwdc2020-10681"
event: "wwdc2020"
year: 2020
title: "Swan's Quest, Chapter 1: Voices in the dark"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10681"
topics: ["Accessibility & Inclusion", "Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Swan's Quest, Chapter 1: Voices in the dark

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10681](https://developer.apple.com/videos/play/wwdc2020/10681)

Swift Playgrounds presents "Swan’s Quest,” an interactive adventure in four chapters for all ages. In this chapter, our Hero must navigate a dark cave — and the only way to light the torches is to make them accessible. Learn about VoiceOver and write interesting audio descriptions. You just might help our Hero find their way out… and get a clue for the next challenge. Swan’s Quest was created for Swift Playgrounds on iPad and Mac, combining frameworks and resources which power the educational experiences in many of our playgrounds, including Sonic Workshop, Sensor Arcade, and Augmented Reality. To learn more about building your own playgrounds, be sure to watch "Create Swift Playgrounds content for iPad and Mac". And don’t forget to stop by the Developer Forums and let us know what you thought of Swan’s Quest.

**Keywords:** `accessibility`, `swan's quest`, `swans quest`, `swift playgrounds`, `swift playgrounds challenge`, `voiceover`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,061 words)

## Documentation & Resources

- [Quest Create playground book](https://developer.apple.com/sample-code/swift/swans-quest/quest-create.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/quest-create.zip
- [Swan's Quest: Voices in the dark playground book](https://developer.apple.com/sample-code/swift/swans-quest/voices-in-the-dark.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/voices-in-the-dark.zip

## Code Snippets

### Graphic.swift — [12:21]

```swift
//  Graphic.swift

open class BaseGraphic: InternalGraphic {

    public var accessibilityHints: AccessibilityHints?

    // ...
}
```

### AccessibilityHints.swift — [12:32]

```swift
//  AccessibilityHints.swift

public struct AccessibilityHints: Codable {

   /// Indicates a graphic should be treated as a UIAccessibilityElement by VoiceOver.
   public var makeAccessibilityElement: Bool = false

   /// Label spoken by VoiceOver for the accessible graphic (a localized character name).
   public var accessibilityLabel: String?

   // ... 

}
```

### Make an Accessible Graphic — [12:45]

```swift
// Make an Accessible Graphic

import SPCCore
import SPCAccessibility

let hints = AccessibilityHints(makeAccessibilityElement: true, 
                               accessibilityLabel: "Activate button to start the party")

let graphic = Graphic(name: "Let's get it Started")
graphic.accessibilityHints = hints
```

### Activating torch1 and torch2 — [13:51]

```swift
// activate torch1 and torch2

cave.torch1.accessibilityHints = AccessibilityHints(makeAccessibilityElement: true, 
        accessibilityLabel: "Torch next to a stairwell, where dripping water can be heard.")
cave.torch2.accessibilityHints = AccessibilityHints(makeAccessibilityElement: true, 
        accessibilityLabel: "Right before the edge of the platform—be careful!")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10681/2/75903D9E-3E93-4132-B19F-B20AEB99018F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10681) — developer.apple.com. Indexed for agent consumption._
