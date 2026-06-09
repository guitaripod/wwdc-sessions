---
id: "wwdc2025-225"
event: "wwdc2025"
year: 2025
title: "Code-along: Explore localization with Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/225"
topics: ["Developer Tools", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Code-along: Explore localization with Xcode

**Event:** WWDC25 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-225](https://developer.apple.com/videos/play/wwdc2025/225)

Learn how to localize your app into additional languages using Xcode. We’ll walk step-by-step through the process of creating a String Catalog, translating text, and exchanging files with external translators. You’ll learn best practices for providing necessary context to translators and how Xcode can help to provide this information automatically. For larger projects, we’ll also dive into techniques to manage complexity and streamline string management using type-safe Swift code.

**Keywords:** `automatic  comment generation`, `l10n`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,074 words)

## Documentation & Resources

- [Localizing Landmarks](https://developer.apple.com/documentation/Xcode/localizing-landmarks) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localizing-landmarks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localizing-landmarks.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### Localizable strings — [1:34]

```swift
// import SwiftUI
Text("Featured Landmark", comment: "Big headline in the hero image of featured landmarks.")

Button("Keep") { }

// import Foundation
String(localized: "New Collection", comment: "Default name for a new user-created collection.")
```

### Adding a comment — [6:00]

```swift
Text("Delete",
comment: "Delete button shown in an alert asking for confirmation to delete the collection.")

String(localized: "Shared by Friends", comment: "Subtitle of post that was shared by friends.")
```

### XLIFF file — [9:13]

```xml
// Field for automatically generated comments in the XLIFF

<trans-unit id="Grand Canyon" xml:space="preserve">
<source>Grand Canyon</source>
<target state="new">Grand Canyon</target>
<note from="auto-generated">Suggestion for searching landmarks</note>
</trans-unit>
```

### Localized String in the main app and a Swift Package or Framework — [9:58]

```swift
// Localized String in the main app:
Text("My Collections", 
comment: "Section title above user-created collections.")

// Localized String in a Swift Package or Framework
Text("My Collections", 
bundle: #bundle, 
comment: "Section title above user-created collections.")
```

### Localized String with a tableName parameter — [10:56]

```swift
// Localized String in the main app:
Text("My Collections",
tableName: "Discover",
comment: "Section title above user-created collections.")

// Localized String in a Swift Package or Framework
Text("My Collections",
tableName: "Discover",
bundle: #bundle, 
comment: "Section title above user-created collections.")
```

### Symbol usage — [17:31]

```swift
// Symbol usage in SwiftUI
Text(.introductionTitle)

.navigationSubtitle(.subtitle(friendsPosts: 42))


// Symbol usage in Foundation
String(localized: .curatedCollection)


// Working with generated symbols in your own types
struct CollectionDetailEditingView: View {
    let title: LocalizedStringResource

    init(title: LocalizedStringResource) {
        self.title = title
    }
}
CollectionDetailEditingView(title: .editingTitle)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/225/5/24973a20-a8c9-4ec6-ad29-6adfde87ea5c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/225/5/24973a20-a8c9-4ec6-ad29-6adfde87ea5c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/225) — developer.apple.com. Indexed for agent consumption._
