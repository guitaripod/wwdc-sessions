---
id: "tech-talks-111461"
event: "tech-talks"
year: 2026
title: "Prepare your app for iPhone Duo"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111461"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS"]
hasTranscript: true
---

# Prepare your app for iPhone Duo

**Event:** Tech Talks · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS · **Published:** 2026-09-09 · **Session:** [tech-talks-111461](https://developer.apple.com/videos/play/tech-talks/111461)

Learn how to update and optimize your app for the foldable display of iPhone Duo. Discover how to opt in to the full-screen experience, adopt flexible layout best practices, and simulate poses in Device Hub with Xcode. Find out how to use size classes instead of interface orientation, handle asymmetric safe areas, and test Split View multitasking to ensure your app shines in all the ways people use it.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,580 words)

## Code Snippets

### Read size classes — [2:59]

```swift
// SwiftUI
@Environment(\.horizontalSizeClass)
private var horizontalSizeClass

@Environment(\.verticalSizeClass)
private var verticalSizeClass

// UIKit
traitCollection.horizontalSizeClass
traitCollection.verticalSizeClass
```

### Access the screen from the window scene — [4:16]

```swift
// Avoid referencing the main screen on a two-display device.
// Access the screen dynamically from the window scene instead.
let screen = window?.windowScene?.screen
```

### Match the screen corners with Concentricity — [4:30]

```swift
// SwiftUI
ConcentricRectangle()
    .fill(Color.green)
    .padding(8.0)
    .ignoresSafeArea()

// UIKit
// UICornerConfiguration
```

### Show a sidebar on the inner display — [5:44]

```swift
// SwiftUI
TabView { … }
    .defaultTabBarPlacement(.sidebar)

// UIKit
tabBarController.sidebar.preferredPlacement = .sidebar
```

### Align foreground content to the safe area — [6:52]

```swift
// UIKit
foreground.frame = view.bounds.inset(by: view.safeAreaInsets)
```

### Let background content extend past the safe area — [7:07]

```swift
// SwiftUI
.ignoresSafeArea()

// UIKit
backgroundView.frame = view.bounds
```

### Handle asymmetric safe area insets — [7:30]

```swift
// Avoid assuming insets on opposite sides are equal
let width = view.bounds.width - view.safeAreaInsets.left * 2

// Handle each side independently
let width = view.bounds.inset(by: view.safeAreaInsets).width
```

### Replace main screen references — [9:25]

```swift
func updateThumbnail(from image: UIImage) {
    // Before
    let screenScale = UIScreen.main.scale

    // After
    let screenScale = traitCollection.displayScale
    // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111461/1/e852bda6-e8c0-400d-8c6d-a37cb19ae254/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111461/1/e852bda6-e8c0-400d-8c6d-a37cb19ae254/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111461) — developer.apple.com. Indexed for agent consumption._
