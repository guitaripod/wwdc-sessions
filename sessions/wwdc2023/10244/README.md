---
id: "wwdc2023-10244"
event: "wwdc2023"
year: 2023
title: "Create rich documentation with Swift-DocC"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10244"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Create rich documentation with Swift-DocC

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10244](https://developer.apple.com/videos/play/wwdc2023/10244)

Learn how you can take advantage of the latest features in Swift-DocC to create rich and detailed documentation for your app or framework. We’ll show you how to use the Xcode 15 Documentation Preview editor to efficiently iterate on your existing project’s documentation, and explore expanded authoring capabilities like grid-based layouts, video support, and custom themes.

To get the most out of this session, you should have a working knowledge of the basics of Swift-DocC documentation.

**Keywords:** `🦥`, `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,891 words)

## Documentation & Resources

- [DocC](https://developer.apple.com/documentation/docc) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json

## Code Snippets

### Documenting a Swift extension — [8:52]

```swift
import SwiftUI

/// An extension that facilitates the display of sloths in user interfaces.
public extension Image {
    /// Create an image from the given sloth.
    ///
    /// Use this initializer to display an image representation of a
    /// given sloth.
    ///
    /// ```swift
    /// let iceSloth = Sloth(name: "Super Sloth", color: .blue, power: .ice)
    ///
    /// var body: some View {
    ///     Image(iceSloth)
    ///         .resizable()
    ///         .aspectRatio(contentMode: .fit)
    ///     Text(iceSloth.name)
    /// }
    /// ```
    ///
    /// ![A screenshot of an ice sloth, with the text Super Sloth underneath.](iceSloth)
    ///
    /// This initializer is useful for displaying static sloth images.
    /// To create an interactive view containing a sloth, use ``SlothView``.
    init(_ sloth: Sloth) {
        self.init("\(sloth.power)-sloth")
    }
}
```

### Creating a grid-based layout — [16:31]

```markdown
@Row {
    @Column(size: 2) {
        First, you customize your sloth by picking its 
        ``Sloth/power-swift.property``. The power of your sloth influences
        its abilities and how well they cope in their environment. The app
        displays a picker view that showcases the available powers and
        previews your sloth for the selected power.
    }

    @Column {
        ![A screenshot of the power picker user interface with four powers displayed – ice, fire, wind, and lightning](slothy-powerPicker)
    }
}

@Row {
    @Column {
        ![A screenshot of the sloth status user interface that indicates the the amount of sleep, fun, and exercise a given sloth is in need of.](slothy-status)
    }

    @Column(size: 2) {
        Once you've customized your sloth, it's ready to ready to thrive.
        You'll find that sloths will happily munch on a leaf, but may not be as 
        receptive to working out. Use the activity picker to send some
        encouragement.
    }
}
```

### Creating a tab navigator — [18:16]

```markdown
@TabNavigator {
    @Tab("English") {
        ![Two screenshots showing the Slothy app rendering with English language content. The first screenshot shows a sloth map and the second screenshot shows a sloth power picker.](slothy-localization_eng)
    }

    @Tab("Chinese") {
        ![Two screenshots showing the Slothy app rendering with Chinese language content. The first screenshot shows a sloth map and the second screenshot shows a sloth power picker.](slothy-localization_zh)
    }

    @Tab("Spanish") {
        ![Two screenshots showing the Slothy app rendering with Spanish language content. The first screenshot shows a sloth map and the second screenshot shows a sloth power picker.](slothy-localization_es)
    }
}
```

### Adding a video — [19:07]

```markdown
@Video(poster: "slothy-hero-poster", source: "slothy-hero", alt: "An animated video showing two screens in the Slothy app. The first screenshot shows a sloth map and the second screenshot shows a sloth power picker.")
```

### Specifying a page's "Call to Action" link — [19:50]

```markdown
@Metadata {
    @CallToAction(purpose: link, url: "https://example.com/slothy-repository")
}
```

### Specifying a page's kind as "Sample Code" — [20:29]

```markdown
@Metadata {
    @CallToAction(purpose: link, url: "https://example.com/slothy-repository")
    @PageKind(sampleCode)
}
```

### Using the "Links" directive to feature content — [21:55]

```markdown
@Links(visualStyle: detailedGrid) {
    - <doc:GettingStarted>
    - <doc:SlothySample>
}
```

### Specifying a page's card image — [22:55]

```markdown
@Metadata {
    @PageImage(
        purpose: card, 
        source: "slothy-card", 
        alt: "Two screenshots showing the Slothy app. The first screenshot shows a sloth map and the second screenshot shows a sloth power picker.")
}
```

### Specifying a page's icon image — [23:41]

```markdown
@Metadata {
    @PageImage(
        purpose: icon, 
        source: "slothCreator-icon", 
        alt: "A technology icon representing the SlothCreator framework.")
}
```

### Specifying a page's color — [23:42]

```markdown
@Metadata {
    @PageColor(green)
}
```

### theme-settings.json — [27:04]

```json
{
    "theme": {
        "color": {
            "standard-green": "#83ac38"
        },
        "typography": {
            "html-font": "serif"
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10244/4/6BE389F4-2F7E-4D0C-A6B6-25C8306D816E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10244/4/6BE389F4-2F7E-4D0C-A6B6-25C8306D816E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10244) — developer.apple.com. Indexed for agent consumption._