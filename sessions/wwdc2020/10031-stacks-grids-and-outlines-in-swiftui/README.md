---
id: "wwdc2020-10031"
event: "wwdc2020"
year: 2020
title: "Stacks, Grids, and Outlines in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10031"
topics: ["Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Stacks, Grids, and Outlines in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10031](https://developer.apple.com/videos/play/wwdc2020/10031)

Display detailed data in your SwiftUI apps more quickly and efficiently with improved stacks and new list and outline views. Now available on iOS and iPadOS for the first time, outlines are a new multi-platform tool for expressing hierarchical data that work alongside stacks and lists. Learn how to use new and improved tools in SwiftUI to display more content on screen when using table views, create smooth-scrolling and responsive stacks, and build out list views for content that needs more than a vStack can provide. Take your layout options even further with the new grid view, as well as disclosure groups. To get the most out of this video, we recommend first checking out “SwiftUI App Essentials,” which provides an overview of everything new in SwiftUI for 2020. If you’re brand-new to coding with SwiftUI, we also suggest watching 2019’s “SwiftUI Essentials” talk.

**Keywords:** `children key path`, `disclosuregroup`, `disclosure groups`, `disclosure triangle`, `forms`, `griditem`, `group`, `hierarchical data`, `hstack`, `isexpanded`, `label`, `layout primitives`, `lazygrid`, `lazyhgrid`, `lazyhstack`, `lazyvgrid`, `lazyvstack`, `liststyle`, `outlinegroup`, `outline groups`, `scrolling`, `selection`, `sidebar`, `tree structure data`, `vstack`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,885 words)

## Documentation & Resources

- [View Layout and Presentation](https://developer.apple.com/documentation/swiftui/layout-fundamentals) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/layout-fundamentals
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/layout-fundamentals.json

## Code Snippets

### Sandwich and HeroView — [2:08]

```swift
// Sandwich model and gallery item view

struct Sandwich: Identifiable {
    var id = UUID()
    var name: String
    var rating: Int
    var heroImage: Image { … }
}

struct HeroView: View {
    var sandwich: Sandwich
    var body: some View {
        sandwich.heroImage
            .resizable()
            .aspectRatio(contentMode: .fit)
            .overlay(BannerView(sandwich: sandwich))
    }
}
```

### Sandwich Info Banner — [2:26]

```swift
// Banner overlay view for sandwich info

struct BannerView: View {
    var sandwich: Sandwich
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Spacer()
            TitleView(title: sandwich.name)
            RatingView(rating: sandwich.rating)
        }
        .padding(…)
        .background(…)
    }
}
```

### Sandwich Rating View — [2:34]

```swift
// Sandwich rating view

struct RatingView: View {
    var rating: Int
    var body: some View {
        HStack {
            ForEach(0..<5) { starIndex in
                StarImage(isFilled: rating > starIndex)
            }
            Spacer()
        }
    }
}
```

### Scrollable Stack of HeroViews — [2:39]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

ScrollView {
    VStack(spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Scrollable Stack of HeroViews — [3:53]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

ScrollView {
    VStack(spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Scrollable Lazy Stack of HeroViews — [3:57]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

ScrollView {
    LazyVStack(spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Scrollable Lazy Stack of HeroViews — [6:09]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

ScrollView {
    LazyVStack(spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Three-Column Grid of Sandwiches — [6:18]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

// Define grid columns
var columns = [
    GridItem(spacing: 0),
    GridItem(spacing: 0),
    GridItem(spacing: 0)
]

ScrollView {
    LazyVGrid(columns: columns, spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Adaptive Grid of Sandwiches — [7:13]

```swift
// Fetch sandwiches from the sandwich store
let sandwiches: [Sandwich] = …

// Define grid columns
var columns = [
    GridItem(.adaptive(minimum: 300), spacing: 0)
]

ScrollView {
    LazyVGrid(columns: columns, spacing: 0) {
        ForEach(sandwiches) { sandwich in
            HeroView(sandwich: sandwich)
        }
    }
}
```

### Outline of GraphicRows — [8:47]

```swift
struct GraphicsList: View {
    var graphics: [Graphic]
    var body: some View {
        List(
            graphics,
            children: \.children
        ) { graphic in
            GraphicRow(graphic)
        }
        .listStyle(SidebarListStyle())
    }
}
```

### Customizing your outlines — [9:52]

```swift
// Customizing your outlines

List {
    ForEach(canvases) { canvas in
        Section(header: Text(canvas.name)) {
            OutlineGroup(canvas.graphics, children: \.children)
            { graphic in
                GraphicRow(graphic)
            }
        }
    }
}
```

### DisclosureGroup — [13:10]

```swift
// Progressive display of information
Form {
    DisclosureGroup(isExpanded: $areFillControlsShowing) {
       Toggle("Fill shape?", isOn: isFilled)
       ColorRow("Fill color", color: fillColor)
    } label: {
       Label("Fill", …)
    }
    …
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10031/4/CC07F299-2B37-486D-9BA2-F305684689A2/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10031) — developer.apple.com. Indexed for agent consumption._
