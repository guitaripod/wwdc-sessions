---
id: "wwdc2020-10649"
event: "wwdc2020"
year: 2020
title: "Add custom views and modifiers to the Xcode Library"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10649"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Add custom views and modifiers to the Xcode Library

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10649](https://developer.apple.com/videos/play/wwdc2020/10649)

The Xcode Library is an easy way for you to discover available SwiftUI views and drag and drop them to the Xcode Previews canvas, enabling rich visual editing of your app. We’ll show you how to extend the content of the Xcode Library with your own views and modifiers, optimizing for reusability and discoverability within your app or Swift packages.

For more on Xcode Previews, check out "Structure your app for SwiftUI previews", and "Visually edit SwiftUI views".

**Keywords:** `library`, `modifiers`, `swiftui`, `views`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,283 words)

## Code Snippets

### LibraryContentProvider — [1:57]

```swift
public protocol LibraryContentProvider {
  @LibraryContentBuilder
  var views: [LibraryItem] { get }

  @LibraryContentBuilder
  public func modifiers(base: ModifierBase) -> [LibraryItem]
}
```

### LibraryItem — [2:32]

```swift
LibraryItem(
  SmoothieRowView(smoothie: .lemonberry),
  visible: true,
  title: "Smoothie Row View",
  category: .control
)
```

### LibraryContent — [3:22]

```swift
struct LibraryContent: LibraryContentProvider {
    @LibraryContentBuilder
    var views: [LibraryItem] {
        LibraryItem(
            SmoothieRowView(smoothie: .lemonberry),
            category: .control
        )

        LibraryItem(
            SmoothieRowView(smoothie: .lemonberry, showNearbyPopularity: true),
            title: "Smoothie Row View With Popularity",
            category: .control
        )
    }
}
```

### Image extension — [8:57]

```swift
extension Image {
    func resizedToFill(width: CGFloat, height: CGFloat) -> some View {
        return self
            .resizable()
            .aspectRatio(contentMode: .fill)
            .frame(width: width, height: height)
    }
}
```

### Modifiers — [9:17]

```swift
@LibraryContentBuilder
func modifiers(base: Image) -> [LibraryItem] {
    LibraryItem(
        base.resizedToFill(width: 100.0, height: 100.0)
    )
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10649/5/904EDE80-6092-4438-85F6-0660C7586D01/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10649) — developer.apple.com. Indexed for agent consumption._