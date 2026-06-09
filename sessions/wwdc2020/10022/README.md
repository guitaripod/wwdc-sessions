---
id: "wwdc2020-10022"
event: "wwdc2020"
year: 2020
title: "Create a seamless speech experience in your apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10022"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Create a seamless speech experience in your apps

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10022](https://developer.apple.com/videos/play/wwdc2020/10022)

Augment your app’s accessibility experience with speech synthesis: Discover the best times and places to add speech APIs so that everyone who uses your app can benefit. Learn how to use AVSpeechSynthesizer to complement assistive technologies like VoiceOver, and when to implement alternative APIs. And we’ll show you how to route audio to the appropriate source and create apps that integrate speech seamlessly for all who need or want it.

To get the most out of this session, you should be familiar with AVFoundation and the basics of speech synthesis. For an overview, watch “AVSpeechSynthesizer: Making iOS Talk.”

**Keywords:** `aac`, `alternative and augmentative communication`, `assistive technology`, `avspeechsynthesizer`, `avspeechutterance`, `speaking rate`, `speech properties`, `speech request`, `spoken content`, `utterance`, `voice technology`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,423 words)

## Documentation & Resources

- [Accessibility for UIKit](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/accessibility-for-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/accessibility-for-uikit.json

## Code Snippets

### Post an Announcement to the Running Assistive Technology — [1:25]

```swift
UIAccessibility.post(notification: .announcement, argument: "Hello World")
```

### Getting Started with AVSpeechSynthesizer — [2:55]

```swift
self.synthesizer = AVSpeechSynthesizer()
let utterance = AVSpeechUtterance(string: "Hello World")
self.synthesizer.speak(utterance)
```

### Respecting the Currently Running Assistive Technology's Speech Settings — [4:08]

```swift
self.synthesizer = AVSpeechSynthesizer()
let utterance = AVSpeechUtterance(string: "Hello World")
utterance.prefersAssistiveTechnologySettings = true
self.synthesizer.speak(utterance)
```

### Customizing Speech - Choosing a Voice — [5:42]

```swift
let utterance = AVSpeechUtterance(string: "Hello World")

// Choose a voice using a language code
utterance.voice = AVSpeechSynthesisVoice(language: "en-US")

// Choose a voice using an identifier
utterance.voice = AVSpeechSynthesisVoice(identifier: AVSpeechSynthesisVoiceIdentifierAlex)

// Get a list of installed voices
let voices = AVSpeechSynthesisVoice.speechVoices()
```

### Customizing Speech - Pitch and Rate — [6:16]

```swift
let utterance = AVSpeechUtterance(string: "Hello World")

// Choose a rate between 0 and 1, 0.5 is the default rate
utterance.rate = 0.75

// Choose a pitch multiplier between 0.5 and 2, 1 is the default multiplier
utterance.pitchMultiplier = 1.5

// Choose a volume between 0 and 1, 1 is the default value
utterance.volume = 0.5
```

### Mix Speech With an Outgoing Call — [6:34]

```swift
self.synthesizer = AVSpeechSynthesizer()
self.synthesizer.mixToTelephonyUplink = true
```

### Opting Speech Out of Application's Audio Session — [7:02]

```swift
self.synthesizer = AVSpeechSynthesizer()
self.synthesizer.usesApplicationAudioSession = false
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10022/3/286D1613-442C-41FD-A8D9-B7E7E0AC8758/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10022) — developer.apple.com. Indexed for agent consumption._