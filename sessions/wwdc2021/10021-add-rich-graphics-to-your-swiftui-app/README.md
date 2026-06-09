---
id: "wwdc2021-10021"
event: "wwdc2021"
year: 2021
title: "Add rich graphics to your SwiftUI app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10021"
topics: ["Graphics & Games", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Add rich graphics to your SwiftUI app

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10021](https://developer.apple.com/videos/play/wwdc2021/10021)

Learn how you can bring your graphics to life with SwiftUI. We’ll begin by working with safe areas, including the keyboard safe area, and learn how to design beautiful, edge-to-edge graphics that won’t underlap the on-screen keyboard. We’ll also explore the materials and vibrancy you can use in SwiftUI to create easily customizable backgrounds and controls, and go over graphics APIs like drawingGroup and the all new canvas. With these tools, it’s simpler than ever to design fully interactive and interruptible animations and graphics in SwiftUI.

**Keywords:** `accessibility`, `.accessibilityaction`, `accessibility actions`, `accessibilitylabel`, `.accessibilityrepresentation`, `animation`, `.animation`, `background`, `background shape`, `background styles`, `bezier curve`, `blend`, `blendmode`, `blend mode`, `blur`, `blur styles`, `canvas`, `cgrect`, `clip background`, `colors app`, `complex particle system`, `containerview`, `context.draw`, `context.fill`, `context.resolve`, `controls`, `drawing`, `drawing an image`, `.drawinggroup`, `emoji`, `.foregroundstyle`, `foreground styles`, `geometryreader`, `gradient`, `graphics`, `.ignoressafearea`, `.ignoressafearea(.keyboard)`, `image`, `innercontext`, `interactive`, `interruptible`, `ios`, `ipados`, `keyboard safe area`, `macos`, `materials`, `model view`, `opacity`, `path`, `performance`, `primary`, `quaternary`, `regularmaterial`, `resolve image`, `safe area`, `.safeareainset`, `safe area inset`, `schedule`, `secondary`, `shading`, `standard shape`, `styles`, `swiftui`, `tap gesture`, `tertiary`, `text styles`, `thinmaterial`, `time in seconds`, `timeline context`, `timelineview`, `timeline view`, `transform`, `tvos`, `vibrancy`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,446 words)

## Documentation & Resources

- [Add rich graphics to your SwiftUI app](https://developer.apple.com/documentation/SwiftUI/add-rich-graphics-to-your-swiftui-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/add-rich-graphics-to-your-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/add-rich-graphics-to-your-swiftui-app.json
- [Composing SwiftUI gestures](https://developer.apple.com/documentation/SwiftUI/Composing-SwiftUI-Gestures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Composing-SwiftUI-Gestures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Composing-SwiftUI-Gestures.json
- [Adding interactivity with gestures](https://developer.apple.com/documentation/SwiftUI/Adding-Interactivity-with-Gestures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Adding-Interactivity-with-Gestures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Adding-Interactivity-with-Gestures.json
- [GestureState](https://developer.apple.com/documentation/SwiftUI/GestureState) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/GestureState
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/GestureState.json

## Code Snippets

### Ignoring safe areas — [3:53]

```swift
// Ignore all safe areas
ContentView()
    .ignoresSafeArea()

// Ignore keyboard only
ContentView()
    .ignoresSafeArea(.keyboard)
```

### Foreground Styles — [7:08]

```swift
VStack {
    Text("Primary")
        .foregroundStyle(.primary)
    Text("Secondary")
        .foregroundStyle(.secondary)
    Text("Tertiary")
        .foregroundStyle(.tertiary)
    Text("Quaternary")
        .foregroundStyle(.quaternary)
}
```

### Purple Foreground Styles — [7:35]

```swift
VStack {
    Text("Primary")
        .foregroundStyle(.primary)
    Text("Secondary")
        .foregroundStyle(.secondary)
    Text("Tertiary")
        .foregroundStyle(.tertiary)
    Text("Quaternary")
        .foregroundStyle(.quaternary)
}
.foregroundStyle(.purple)
```

### Blue Gradient Foreground Styles — [7:41]

```swift
let blueGradient = LinearGradient(
    colors: [.blue, .teal], startPoint: .leading, endPoint: .trailing)
VStack {
    Text("Primary")
        .foregroundStyle(.primary)
    Text("Secondary")
        .foregroundStyle(.secondary)
    Text("Tertiary")
        .foregroundStyle(.tertiary)
    Text("Quaternary")
        .foregroundStyle(.quaternary)
}
.foregroundStyle(blueGradient)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10021/8/16B955CA-C8EE-4062-9495-C6571401B563/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10021/8/16B955CA-C8EE-4062-9495-C6571401B563/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10021) — developer.apple.com. Indexed for agent consumption._
