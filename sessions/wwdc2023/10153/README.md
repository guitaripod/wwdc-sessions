---
id: "wwdc2023-10153"
event: "wwdc2023"
year: 2023
title: "Unlock the power of grammatical agreement"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10153"
topics: ["Accessibility & Inclusion", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Unlock the power of grammatical agreement

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10153](https://developer.apple.com/videos/play/wwdc2023/10153)

Discover how you can use automatic grammatical agreement in your apps and games to create inclusive and more natural-sounding expressions. We’ll share best practices for working with Foundation, showcase examples in multiple languages, and demonstrate how to use these APIs to enhance the user experience for your apps.

For an introduction to automatic grammatical agreement, watch “What’s new in Foundation” from WWDC21.

**Keywords:** `agreewithargument`, `i18n`, `inflect`, `internationalization`, `l10n`, `localization`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,384 words)

## Documentation & Resources

- [NSMorphology](https://developer.apple.com/documentation/Foundation/NSMorphology) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/NSMorphology
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/NSMorphology.json
- [NSInflectionRule](https://developer.apple.com/documentation/Foundation/NSInflectionRule) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/NSInflectionRule
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/NSInflectionRule.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### agreeWithConcept — [4:08]

```swift
// Formatting the string

var options = AttributedString.LocalizationOptions()
options.concepts = [.localizedPhrase(food.localizedName)]

let size = AttributedString(localized: "small", options: options)
```

### Preferred terms of address — [8:45]

```swift
// A person who is delivering the food order

struct DeliveryPerson {

    // The person's preferred name
    var name: String

    // An avatar for the delivery person
    var avatar: Image

    // The person's preferred terms of address. This list may contain more than
    // one option, we will use the first applicable one for the language that's
    // used in the UI.
    var preferredTermsOfAddress: [TermOfAddress]
}

// Formatting the message in Swift

var options = AttributedString.LocalizationOptions()
options.concepts = [.termsOfAddress(person.preferredTermsOfAddress)]

let message = AttributedString(localized:  "\(person.name) is on ^[their](referentConcept: 1) way.”, options: options)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10153/6/A7A21FC4-917F-4A51-B18C-89DB54EBD3B7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10153/6/A7A21FC4-917F-4A51-B18C-89DB54EBD3B7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10153) — developer.apple.com. Indexed for agent consumption._