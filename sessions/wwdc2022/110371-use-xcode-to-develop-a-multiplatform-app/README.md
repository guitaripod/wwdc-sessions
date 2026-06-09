---
id: "wwdc2022-110371"
event: "wwdc2022"
year: 2022
title: "Use Xcode to develop a multiplatform app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110371"
topics: ["Essentials", "Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Use Xcode to develop a multiplatform app

**Event:** WWDC22 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110371](https://developer.apple.com/videos/play/wwdc2022/110371)

Learn how you can build apps for multiple Apple platforms using Xcode 14. We'll show you how to streamline app targets, maintain a common codebase, and share settings by default. We'll also explore how you can customize your app for each platform through conditionalizing your settings and code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,677 words)

## Code Snippets

### canImport — [8:48]

```swift
#if canImport(ARKit)
import ARKit
#endif
```

### Condition Property — [10:02]

```swift
#if os(iOS)
@Environment(\.editMode) private var editMode
#endif
```

### Condition View Modifier — [10:13]

```swift
#if os(iOS)
.onChange(of: editMode?.wrappedValue) { newValue in
    if newValue?.isEditing == false {
        selection.removeAll()
    }
}
#endif
```

### Condition View — [10:19]

```swift
#if os(iOS)
EditButton()
#endif
```

### Computed Property — [11:48]

```swift
var thumnailSize: Double {
    #if os(iOS)
    return 120
    #else
    return 80
    #endif
}
```

### Menu Bar Extra — [12:37]

```swift
#if os(macOS)
MenuBarExtra {
    MiniTruckView(model: model)
} label: {
    Label("Food Truck", systemImage: "box.truck")
}
.menuBarExtraStyle(.window)
#endif
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110371/4/F41F7DFC-33C6-4BFA-9CC0-D212E30E6599/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110371/4/F41F7DFC-33C6-4BFA-9CC0-D212E30E6599/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110371) — developer.apple.com. Indexed for agent consumption._
