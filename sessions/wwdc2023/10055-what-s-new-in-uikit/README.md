---
id: "wwdc2023-10055"
event: "wwdc2023"
year: 2023
title: "What’s new in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10055"
topics: ["App Services", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What’s new in UIKit

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10055](https://developer.apple.com/videos/play/wwdc2023/10055)

Explore enhancements and updates to UIKit and learn how to build better iOS, iPadOS, and Mac Catalyst apps. We’ll show you the latest features and improvements in UIKit and share API refinements, performance improvements, and much more.

**Keywords:** `🎨`, `🧑🏻‍🎨`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,832 words)

## Documentation & Resources

- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/UIKit.json

## Code Snippets

### Using Xcode previews with view controllers — [1:31]

```swift
class LibraryViewController: UIViewController {
    // ...
}

#Preview("Library") {
    let controller = LibraryViewController()
    controller.displayCuratedContent = true
    return controller
}
```

### Using Xcode previews with views — [1:48]

```swift
class SlideshowView: UIView {
    // ...
}

#Preview("Memories") {
    let view = SlideshowView()
    view.title = "Memories"
    view.subtitle = "Highlights from the past year"
    view.images = ...
    return view
}
```

### Setting up UIContentUnavailableConfiguration — [8:19]

```swift
var config = UIContentUnavailableConfiguration.empty()

config.image = UIImage(systemName: "star.fill")
config.text = "No Favorites"
config.secondaryText =
    "Your favorite translations will appear here."

viewController.contentUnavailableConfiguration = config
```

### Using UIContentUnavailableConfiguration with SwiftUI — [8:56]

```swift
let config = UIHostingConfiguration {
    VStack {
        ProgressView(value: progress)
        Text("Downloading file...")
            .foregroundStyle(.secondary)
    }
}
viewController.contentUnavailableConfiguration = config
```

### Using UIContentUnavailableConfiguration for search results — [9:21]

```swift
override func updateContentUnavailableConfiguration(
    using state: UIContentUnavailableConfigurationState
) {
    var config: UIContentUnavailableConfiguration?
    if searchResults.isEmpty {
        config = .search()
    }
    contentUnavailableConfiguration = config
}

// Update search results for query
searchResults = backingStore.results(for: query)
setNeedsUpdateContentUnavailableConfiguration()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10055/4/7F22FD85-1611-456E-875B-966A87E16636/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10055/4/7F22FD85-1611-456E-875B-966A87E16636/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10055) — developer.apple.com. Indexed for agent consumption._
