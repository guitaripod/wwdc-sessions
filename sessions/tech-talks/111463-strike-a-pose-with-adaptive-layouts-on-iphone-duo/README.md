---
id: "tech-talks-111463"
event: "tech-talks"
year: 2026
title: "Strike a pose with adaptive layouts on iPhone Duo"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111463"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["iOS"]
hasTranscript: true
---

# Strike a pose with adaptive layouts on iPhone Duo

**Event:** Tech Talks · **Topic:** Design · **Platforms:** iOS · **Published:** 2026-09-09 · **Session:** [tech-talks-111463](https://developer.apple.com/videos/play/tech-talks/111463)

Learn how to create responsive, flexible layouts that work great on iPhone Duo. Explore displacement design patterns that keep content visible and reachable as people open and close their iPhone Duo. Discover how to use arrangement views in SwiftUI and UIKit to build split and overlay presentations, and find out how to query reserved regions to tailor layouts around the hinge and cameras.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,764 words)

## Code Snippets

### Query reserved regions in SwiftUI — [6:46]

```swift
// SwiftUI
GeometryReader { proxy in
  let regions = proxy.reservedRegions(
    kind: .division)
}
```

### Query reserved regions in UIKit — [7:03]

```swift
// UIKit
let regions = view.reservedRegions(
  kind: .division)

// Query the frame to incorporate it into your own layout
let frames = regions.map(\.frame)
```

### Include inactive regions — [7:22]

```swift
// SwiftUI
GeometryReader { proxy in
  let regions = proxy.reservedRegions(
    kind: .division, options: .includeInactive)

  let frames = regions.map(\.frame)
  // ...
}
```

### Query occlusion regions — [8:07]

```swift
// SwiftUI
GeometryReader { proxy in
  let regions = proxy.reservedRegions(
    kind: .occlusion)

  let frames = regions.map(\.frame)
  // ...
}
```

### Add an ArrangementView — [11:23]

```swift
// SwiftUI
var body: some View {
  NavigationStack {
    ArrangementView {
      PlayerView()
    } secondary: {
      UpNextView()
    }
  }
}
```

### Add a UIArrangementViewController — [11:26]

```swift
// UIKit
let arrangementVC = UIArrangementViewController()
let navController = UINavigationController(rootViewController: arrangementVC)

let playerVC = PlayerViewController()
arrangementVC.setViewController(playerVC, for: .primary)

let upNextVC = UpNextViewController()
arrangementVC.setViewController(upNextVC, for: .secondary)
```

### Specify the split arrangement style — [12:00]

```swift
// SwiftUI
var body: some View {
  NavigationStack {
    ArrangementView {
      PlayerView()
    } secondary: {
      UpNextView()
    }
    .arrangementViewStyle(.split)
  }
}
```

### Restrict the split to one axis — [12:41]

```swift
// SwiftUI
var body: some View {
  NavigationStack {
    ArrangementView {
      PlayerView()
    } secondary: {
      UpNextView()
    }
    .arrangementViewStyle(
      .split.axes(.horizontal))
  }
}
```

### Update the arrangement in UIKit — [13:07]

```swift
// UIKit
let arrangementVC = UIArrangementViewController()

// ...

arrangementVC.updateArrangement(.split.axes(.horizontal))
```

### Switch to the overlay arrangement — [13:26]

```swift
// SwiftUI
var body: some View {
  NavigationStack {
    ArrangementView {
      UpNextView()
    } secondary: {
      PlayerView()
    }
    .arrangementViewStyle(.overlay)
  }
}
```

### Respond to the overlay Z index — [14:07]

```swift
// SwiftUI
enum UpNextMinimization {
  case collapsed; case expanded
}

struct UpNextView: View {
  @Environment(\.overlayArrangementZIndex)
  private var zIndex: Int

  var body: some View {
    UpNextList(minimization: minimization)
  }

  var minimization: UpNextMinimization {
    zIndex > 0 ? .collapsed : .expanded
  }
}
```

### Read the Z index in UIKit — [14:21]

```swift
// UIKit
let arrangementVC = UIArrangementViewController()

// ...

let primaryState = arrangementVC.state(for: .primary)
myModel.minimization = (primaryState?.zIndex ?? 0) > 0
  ? .collapsed : .expanded
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111463/1/dcd8d7bb-94d3-4f48-bd2b-e3a6e10fec1e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111463/1/dcd8d7bb-94d3-4f48-bd2b-e3a6e10fec1e/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111463) — developer.apple.com. Indexed for agent consumption._
