---
id: "wwdc2025-222"
event: "wwdc2025"
year: 2025
title: "Enhance your app’s multilingual experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/222"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Enhance your app’s multilingual experience

**Event:** WWDC25 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-222](https://developer.apple.com/videos/play/wwdc2025/222)

Create a seamless experience for anyone who uses multiple languages. Learn how Language Discovery allows you to optimize your app using a person’s preferred languages. Explore advances in support for right-to-left languages, including Natural Selection for selecting multiple ranges in bidirectional text. We’ll also cover best practices for supporting multilingual scenarios in your app.

**Keywords:** `🌍`, `🌎`, `🌏`, `alternate calendars`, `i18n`, `ltr`, `rtl`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,804 words)

## Documentation & Resources

- [Language Introspector](https://developer.apple.com/documentation/Foundation/language-introspector) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/language-introspector
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/language-introspector.json
- [Human Interface Guidelines: Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/right-to-left
- [Internationalization and Localization Guide](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html

## Code Snippets

### Language discover — [5:35]

```swift
// Language discovery

let preferredLanguages = Locale.preferredLanguages

let preferredLocales = Locale.preferredLocales
```

### Match preferred locales with your app’s available locales — [7:49]

```swift
let preferredLocales = Locale.preferredLocales

// array of available Locale objects to translate from
let availableLocales = getAvailableLocalesForTranslatingFrom()

var matchedLocales: [Locale] = []

for locale in availableLocales {
    for preferredLocale in preferredLocales {
        if locale.language.isEquivalent(to:         preferredLocale.language) {
            matchedLocales.append(locale)
            break
        }
    }
}
```

### Delete text in ranges — [14:57]

```swift
let ranges = textView.selectedRanges.reversed()
for range in ranges {
    textView.textStorage.deleteCharacters(in: range)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/222/6/0c2c6210-4f59-409a-ba23-36a7895563d3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/222/6/0c2c6210-4f59-409a-ba23-36a7895563d3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/222) — developer.apple.com. Indexed for agent consumption._