---
id: "wwdc2021-10349"
event: "wwdc2021"
year: 2021
title: "SF Symbols in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10349"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# SF Symbols in SwiftUI

**Event:** WWDC21 · **Topic:** Design · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10349](https://developer.apple.com/videos/play/wwdc2021/10349)

Discover how you can incorporate SF Symbols into your SwiftUI app. We’ll explore basic techniques for presenting symbols, customizing their size, and showing different variants. We’ll also take you through the latest updates to symbol colorization and help you pick the right tool for your app’s needs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,755 words)

## Documentation & Resources

- [Download SF Symbols](https://developer.apple.com/sf-symbols/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sf-symbols/
- [Human Interface Guidelines: SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/sf-symbols

## Code Snippets

### Creating Symbols — [0:45]

```swift
// System symbol image
Image(systemName: "heart")

// System symbol label
Label("Heart", systemImage: "heart")

// Custom symbol image
Image("queen.heart")

// Custom symbol label
Label("Queen of Hearts", image: "queen.heart")
```

### Accessibility Label — [2:33]

```swift
Image(systemName: "heart")
    .accessibilityLabel("Ace of Hearts")

Image(systemName: "person.circle")
    .accessibilityLabel("Profile")

Image("queen.heart")

// Localizeable.strings
"queen.heart" = "Queen of Hearts";
```

### Symbol in Text — [2:59]

```swift
Text("""
    Thalia, Paul, and
    3 others \(Image(systemName: "chevron.forward"))
""")
```

### Customizing Color — [3:14]

```swift
Label("Heart", systemImage: "heart")

Label("Heart", systemImage: "heart")
    .foregroundStyle(.red)

Label("Heart", systemImage: "heart")
    .foregroundStyle(.tint)

Label("Heart", systemImage: "heart")
    .foregroundStyle(.secondary)
```

### Customizing Font — [3:51]

```swift
Label("Heart", systemImage: "heart")
    .font(.body)

Label("Heart", systemImage: "heart")
    .font(.caption)

Label("Heart", systemImage: "heart")
    .font(.system(size: 10))
```

### Customizing Scale — [4:08]

```swift
Label("Heart", systemImage: "heart")
    .imageScale(.large)

Label("Heart", systemImage: "heart")
    .imageScale(.medium)

Label("Heart", systemImage: "heart")
    .imageScale(.small)
```

### Customizing Variants — [4:23]

```swift
TabView {
    Text("Cards").tabItem {
        Label("Cards", systemImage: "rectangle.portrait.on.rectangle.portrait")
    }
    Text("Rules").tabItem {
        Label("Rules", systemImage: "character.book.closed")
    }
    Text("Profile").tabItem {
        Label("Profile", systemImage: "person.circle")
    }
    Text("Magic").tabItem {
        Label("Magic", systemImage: "sparkles")
    }
}
```

### Monochrome — [5:12]

```swift
List {
    Label("Ace of Hearts", systemImage: "suit.heart")
    Label("Ace of Spades", systemImage: "suit.spade")
    Label("Ace of Diamonds", systemImage: "suit.diamond")
    Label("Ace of Clubs", systemImage: "suit.club")
    Label("Queen of Hearts", image: "queen.heart")
}
.symbolVariant(.fill)
```

### Multicolor — [6:41]

```swift
List {
    Label("Ace of Hearts", systemImage: "suit.heart")
    Label("Ace of Spades", systemImage: "suit.spade")
    Label("Ace of Diamonds", systemImage: "suit.diamond")
    Label("Ace of Clubs", systemImage: "suit.club")
    Label("Queen of Hearts", image: "queen.heart")
}
.symbolVariant(.fill)
.symbolRenderingMode(.multicolor)
```

### Hierarchical Rendering Mode — [7:10]

```swift
HStack {
    Button(action: {}) {
        Image(systemName: "square.3.stack.3d.top.fill")
    }
    Button(action: {}) {
        Image(systemName: "square.3.stack.3d.bottom.fill")
    }
}
.symbolRenderingMode(.hierarchical)
```

### Palette Rendering Mode — [7:50]

```swift
Button(action: {}) {
    Image(systemName: "arrow.uturn.backward")
}
.symbolVariant(.circle.fill)
.foregroundStyle(.white, .yellow, .red)
```

### Advanced Foreground Styles — [9:00]

```swift
Button(action: {}) {
    Image(systemName: "arrow.uturn.backward")
}
.symbolVariant(.circle.fill)
.foregroundStyle(.white, .red)

Button(action: {}) {
    Image(systemName: "arrow.uturn.backward")
}
.symbolVariant(.circle.fill)
.foregroundStyle(.white, .secondary)

Button(action: {}) {
    Image(systemName: "arrow.uturn.backward")
}
.symbolVariant(.circle.fill)
.foregroundStyle(.red, .regularMaterial)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10349/4/5C81F023-9887-405D-AF78-7FBD8FACEDEF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10349/4/5C81F023-9887-405D-AF78-7FBD8FACEDEF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10349) — developer.apple.com. Indexed for agent consumption._
