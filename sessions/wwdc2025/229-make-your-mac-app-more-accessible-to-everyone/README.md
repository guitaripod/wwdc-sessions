---
id: "wwdc2025-229"
event: "wwdc2025"
year: 2025
title: "Make your Mac app more accessible to everyone"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/229"
topics: ["Accessibility & Inclusion"]
platforms: ["macOS"]
hasTranscript: true
---

# Make your Mac app more accessible to everyone

**Event:** WWDC25 · **Topic:** Accessibility & Inclusion · **Platforms:** macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-229](https://developer.apple.com/videos/play/wwdc2025/229)

Learn how to integrate accessibility features that take full advantage of the power and flexibility of macOS. Go beyond the basics to learn how to support VoiceOver and Voice Control, improve the layout of your views, explore how assistive technologies navigate your content, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,919 words)

## Documentation & Resources

- [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility
- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json

## Code Snippets

### Contain subviews within accessibility container — [4:15]

```swift
// Contain subviews within accessibility container

import SwiftUI

struct ContentView: View {
  var body: some View {
    VStack {
      FirstView()
      SecondView()
    }
    .accessibilityElement(children: .contain)
  }
}
```

### Combine subviews into one accessibility element — [4:23]

```swift
// Combine subviews into one accessibility element

import SwiftUI

struct ContentView: View {
  var body: some View {
    VStack {
      FirstView()
      SecondView()
    }
    .accessibilityElement(children: .combine)
  }
}
```

### Hide subviews from accessibility — [4:33]

```swift
// Hide subviews from accessibility

import SwiftUI

struct ContentView: View {
  var body: some View {
    VStack {
      FirstView()
      SecondView()
    }
    .accessibilityElement(children: .ignore)
  }
}
```

### Contain style presets in accessibility container — [5:12]

```swift
// Contain style presets in accessibility container

import SwiftUI

struct FormattingInspectorView: View {
  var body: some View {
    Form {
      VStack {
        StylePresetView(type: .title)
        StylePresetView(type: .heading)
        StylePresetView(type: .subHeading)
        StylePresetView(type: .body)
      }
      .accessibilityElement(children: .contain)
      .accessibilityLabel("Style Presets")
    }
  }
}
```

### Merge Title View and Button into one accessibility element — [6:21]

```swift
// Merge Title View and Button into one accessibility element

import SwiftUI

struct StylePresetView: View {
  let preset: StylePreset

  var body: some View {
    HStack {
      PresetTitleView(preset: preset)
      Button("Apply") { /* ... */ }
    }
    .accessibilityElement(children: .combine)
  }
}
```

### Set the order of accessibility elements — [7:01]

```swift
// Set the order of accessibility elements

import SwiftUI

struct BookDetailsView: View {
  let book: Book

  var body: some View {
    VStack {
      Text(book.author)
      Text(book.title)
        .accessibilitySortPriority(1)
      DescriptionView(book: book)
    }
    .accessibilityElement(children: .combine)
  }
}
```

### Add an accessibility rotor for bookmarked pages — [8:43]

```swift
// Add an accessibility rotor for bookmarked pages

import SwiftUI

struct PagesView: View {
  @Binding var pages: [Page]

  var body: some View {
    List(pages) { page in
      PageListItemView(page: page)
    }
    .accessibilityRotor("Bookmarks") {
      ForEach(pages) { page in
        if page.isBookmarked {
          AccessibilityRotorEntry(page.title, id: page.id)
        }
      }
    }
  }
}
```

### Set the default VoiceOver focus — [9:33]

```swift
// Set the default VoiceOver focus

struct MyView: View {
  @AccessibilityFocusState(for: .voiceOver) var focusedForVoiceOver

  var body: some View {
    FirstView()
    SecondView()
      .accessibilityDefaultFocus($focusedForVoiceOver, true)
    ThirdView()
  }
}
```

### Add an accessibility action to bookmark the page — [10:28]

```swift
// Add an accessibility action to bookmark the page

import SwiftUI

struct PageListItemView: View {
  var page: Page

  var body: some View {
    VStack() {
      ThumbnailView(page: page)
      Text(page.title)
    }
    .onHover { /* ... */ }
    .accessibilityAction(named: page.isBookmarked ? "Remove Bookmark" : "Bookmark") {
      page.isBookmarked.toggle()
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/229/5/85268a8c-59ed-4f8c-942d-8835f8a76dd3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/229/5/85268a8c-59ed-4f8c-942d-8835f8a76dd3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/229) — developer.apple.com. Indexed for agent consumption._
