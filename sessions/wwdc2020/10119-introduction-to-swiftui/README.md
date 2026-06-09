---
id: "wwdc2020-10119"
event: "wwdc2020"
year: 2020
title: "Introduction to SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10119"
topics: ["Developer Tools", "Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Introduction to SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10119](https://developer.apple.com/videos/play/wwdc2020/10119)

Explore the world of declarative-style programming: Discover how to build a fully-functioning SwiftUI app from scratch as we explain the benefits of writing declarative code and how SwiftUI and Xcode can combine forces to help you build great apps, faster.

**Keywords:** `animation`, `.aspectratio`, `canvas`, `compositional ui`, `corner radius`, `dark mode`, `declarative syntax`, `declarative ui`, `dependency management`, `derived value`, `horizontal stack`, `hstack`, `inspector`, `leading alignment`, `library`, `live mode`, `localization`, `model`, `modifiers`, `multiplatform app template`, `navigationview`, `padding`, `preview on device`, `previews`, `.resizable`, `resume updating preview`, `sfsymbol`, `source of truth`, `spacer`, `state variable`, `swift`, `text`, `vertical stack`, `view`, `views`, `vstack`, `xcode library`, `zoom state`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(7,357 words)

## Documentation & Resources

- [SwiftUI](https://developer.apple.com/documentation/SwiftUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI.json

## Code Snippets

### Views are lightweight — [17:18]

```swift
struct SandwichDetail: View {
    let sandwich: Sandwich

    var body: some View {
        Image(sandwich.imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
    }
}
```

### Views are composed — [18:30]

```swift
struct SandwichDetail: View {
    let sandwich: Sandwich

    var body: some View {
        Image(sandwich.imageName)
            .resizable()
            .aspectRatio(contentMode: .fit)
    }
}
```

### View are dynamic — [19:52]

```swift
struct SandwichDetail: View {
    let sandwich: Sandwich
    @State private var zoomed = false

    var body: some View {
        Image(sandwich.imageName)
            .resizable()
            .aspectRatio(contentMode: zoomed ? .fill : .fit)
            .onTapGesture { zoomed.toggle() }
    }
}
```

### Where is truth? — [21:40]

```swift
struct SandwichDetail: View {
    let sandwich: Sandwich
    @State private var zoomed = false

    var body: some View {
        Image(sandwich.imageName)
            .resizable()
            .aspectRatio(contentMode: zoomed ? .fill : .fit)
            .onTapGesture { zoomed.toggle() }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10119/7/C3E13536-E82C-4A52-B2E6-1D04D0991648/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10119) — developer.apple.com. Indexed for agent consumption._
