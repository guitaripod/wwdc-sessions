---
id: "wwdc2026-221"
event: "wwdc2026"
year: 2026
title: "Prepare your tvOS apps for Dynamic Type"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/221"
topics: ["Audio & Video", "Accessibility & Inclusion"]
platforms: ["tvOS"]
hasTranscript: true
---

# Prepare your tvOS apps for Dynamic Type

**Event:** WWDC26 · **Topic:** Accessibility & Inclusion · **Platforms:** tvOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-221](https://developer.apple.com/videos/play/wwdc2026/221)

Dynamic Type empowers people to comfortably read and interact with your app by letting them choose the text size that works best for them. You’ll learn how to get your app ready for Dynamic Type on tvOS through practical techniques for implementing font scaling and adapting your layouts for larger content. You’ll also discover how to optimize your media-focused interfaces like grids and carousels, ensuring a great experience for everyone who relies on different text sizes.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,406 words)

## Documentation & Resources

- [Applying custom fonts to text](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Applying-Custom-Fonts-to-Text
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Applying-Custom-Fonts-to-Text.json
- [Scaling fonts automatically](https://developer.apple.com/documentation/UIKit/scaling-fonts-automatically) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/scaling-fonts-automatically
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/scaling-fonts-automatically.json

## Code Snippets

### Adopt standard text styles — [4:58]

```swift
// Adopt standard text styles

VStack(spacing: 20) {
  Text("Signup information")
    .font(.caption.bold())
    .lineLimit(1)
    .foregroundStyle(.secondary)
    .frame(width: 300, alignment: .leading)
  HStack(alignment: .top, spacing: 40) { 
      //* ... *//
  }
}
```

### Use flexible constraints — [5:10]

```swift
// Adopt standard text styles

VStack(spacing: 20) {
  Text("Signup information")
    .font(.caption.bold())
    .lineLimit(1)
    .foregroundStyle(.secondary)
    .frame(maxWidth: .infinity, alignment: .leading)
  HStack(alignment: .top, spacing: 40) { 
      /* ... */
  }
}
```

### Dynamic Type with text styles in UIKit — [5:55]

```swift
// Hard coded text size in UIKit

titleLabel.font = UIFont.boldSystemFont(ofSize: 28)

// Dynamic Type with text styles in UIKit

titleLabel.font = UIFont.preferredFont(forTextStyle: .headline)
titleLabel.adjustsFontForContentSizeCategory = true
```

### Adapt layout in response to dynamic type — [7:09]

```swift
// A view that shows a collection of movie posters

struct MovieShelf: View {
  @Environment(\.dynamicTypeSize) private var dynamicTypeSize
  var body: some View {
    ScrollView(.horizontal) {
      LazyHStack(spacing: 40) {
        ForEach(Asset.allCases) { asset in
          Button { 
            /* ... */
          } label: {
            asset.portraitImage
            Text(asset.title)
          }
          .containerRelativeFrame(
            .horizontal,
            count: dynamicTypeSize.isAccessibilitySize ? 4 : 6,
            spacing: 40)
        }
      }
    }
  }
}
```

### Provide a conditional layout for when larger sizes are turned on — [8:07]

```swift
// A view that shows content in a card

struct CardContentView: View {
  @Environment(\.dynamicTypeSize) private var dynamicTypeSize
  var asset: Asset

  var body: some View {
    let layout = dynamicTypeSize.isAccessibilitySize ?
      AnyLayout(VStackLayout(alignment: .leading, spacing: 10)) :
      AnyLayout(HStackLayout(alignment: .top, spacing: 10))
    layout {
      /* ... */
    }
  }
}
```

### UIKit adaptive layout that responds to content size changes — [8:31]

```swift
// UIKit adaptive layout that responds to content size changes

class AdaptiveLayoutViewController: UIViewController {
  let stackView = UIStackView()

  override func viewDidLoad() {
    super.viewDidLoad()
    updateLayout()

    let sizeTraits: [UITrait] = [UITraitPreferredContentSizeCategory.self]
    registerForTraitChanges(sizeTraits, action: #selector(updateLayout))
  }

  private func updateLayout() {
    if traitCollection.preferredContentSizeCategory.isAccessibilityCategory {
      stackView.axis = .vertical
    } else {
      stackView.axis = .horizontal
    }
  }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/221/5/ada10ebd-34f8-4f57-92b5-4b3cd6281267/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/221/5/ada10ebd-34f8-4f57-92b5-4b3cd6281267/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/221) — developer.apple.com. Indexed for agent consumption._