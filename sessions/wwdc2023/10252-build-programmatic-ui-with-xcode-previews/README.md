---
id: "wwdc2023-10252"
event: "wwdc2023"
year: 2023
title: "Build programmatic UI with Xcode Previews"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10252"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Build programmatic UI with Xcode Previews

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10252](https://developer.apple.com/videos/play/wwdc2023/10252)

Learn how you can use the #Preview macro on Xcode 15 to quickly iterate on your UI code written in SwiftUI, UIKit, or AppKit. Explore a collage of unique workflows for interacting with views right in the canvas, find out how to view multiple variations of UI simultaneously, and discover how you can travel through your widget’s timeline in seconds to test the transitions between entries. We’ll also show you how to add previews to libraries, provide sample assets, and preview your views in your physical devices to leverage their capabilities and existing data.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,326 words)

## Code Snippets

### Basic preview — [1:30]

```swift
#Preview {
    MyView()
}
```

### Previewing a SwiftUI view in a list — [5:05]

```swift
#Preview {
    List {
        CollageView(layout: .twoByTwoGrid)
    }
    .environment(CollageLayoutStore.sample)
}
```

### Previews can have a name and configuration traits — [5:37]

```swift
#Preview(“2x2 Grid”, traits: .landscapeLeft) {
    List {
        CollageView(layout: .twoByTwoGrid)
    }
    .environment(CollageLayoutStore.sample)
}
```

### Previewing UIKit view controllers and views — [5:58]

```swift
#Preview {
    var controller = SavedCollagesController()
    controller.dataSource = CollagesDataStore.sample
    controller.layoutMode = .grid
    return controller
}

#Preview(“Filter View”) {
    var view = CollageFilterDisplayView()
    view.filter = .bloom(amount: 15.0)
    view.imageData = …
    return view
}
```

### Xcode can help suggest a preview — [7:08]

```swift
#Preview {
    FilterEditor()
}
```

### Setting a UIKit preview to start in landscape — [11:30]

```swift
#Preview("All Filters", traits: .landscapeLeft) {
    let viewController = FilterRenderingViewController()
    if let image = UIImage(named: "sample-001")?.cgImage {
        viewController.imageData = image
    }
    viewController.filter = Filter(
        bloomAmount: 1.0,
        vignetteAmount: 1.0,
        saturationAmount: 0.5
    )
    return viewController
}
```

### Previewing a small widget with a timeline provider — [12:20]

```swift
#Preview(as: .systemSmall) {
    FrameWidget()
} timelineProvider: {
    RandomCollageProvider()
}
```

### Updating the navigation title while previewing on device — [25:07]

```swift
.navigationTitle(“Add Collage”)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10252/5/28C78519-19B7-468C-A50B-4960D801E332/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10252/5/28C78519-19B7-468C-A50B-4960D801E332/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10252) — developer.apple.com. Indexed for agent consumption._
