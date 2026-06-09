---
id: "wwdc2025-310"
event: "wwdc2025"
year: 2025
title: "Build an AppKit app with the new design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/310"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Build an AppKit app with the new design

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-310](https://developer.apple.com/videos/play/wwdc2025/310)

Update your AppKit app to take full advantage of the new design system. We’ll dive into key changes to tab views, split views, bars, presentations, search, and controls, and show you how to use Liquid Glass in your custom UI. To get the most out of this video, we recommend first watching “Get to know the new design system” for general design guidance.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,314 words)

## Documentation & Resources

- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TechnologyOverviews/adopting-liquid-glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TechnologyOverviews/adopting-liquid-glass.json
- [Human Interface Guidelines: Designing for macOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-macos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/Human-Interface-Guidelines/designing-for-macos

## Code Snippets

### Removing toolbar item glass — [3:11]

```swift
// Removing toolbar item glass

toolbarItem.isBordered = false
```

### Tinted toolbar controls — [3:30]

```swift
// Tints the glass with the accent color.
toolbarItem.style = .prominent

// Tints the glass with a specific color.
toolbarItem.backgroundTintColor = .systemGreen
```

### Toolbar badges — [3:58]

```swift
// Numeric badge
NSItemBadge.count(4)

// Text badge
NSItemBadge.text("New")

// Badge indicator
NSItemBadge.indicator
```

### Content under the sidebar — [5:25]

```swift
// Content under the sidebar

splitViewItem.automaticallyAdjustsSafeAreaInsets = true
```

### Avoiding a window corner — [8:47]

```swift
// Avoiding a window corner


func updateConstraints() {
    guard !installedButtonConstraints else { return }

    let safeArea = layoutGuide(for: .safeArea(cornerAdaptation: .horizontal))

    NSLayoutConstraint.activate([
        safeArea.leadingAnchor.constraint(equalTo: button.leadingAnchor),
        safeArea.trailingAnchor.constraint(greaterThanOrEqualTo: button.trailingAnchor),
        safeArea.bottomAnchor.constraint(equalTo: button.bottomAnchor)
    ])
    installedButtonConstraints = true
}
```

### Levels of prominence — [15:31]

```swift
// Create buttons with varying levels of prominence

// Prefer a “secondary” tinted appearance for the shuffle and enqueue buttons
shuffleButton.tintProminence = .secondary
playNextButton.tintProminence = .secondary

// The "play" will automatically use primary prominence because it is the default button
playButton.keyEquivalent = "\r"
```

### Adopting NSGlassEffectView — [18:42]

```swift
// Adopting NSGlassEffectView

let userInfoView = UserInfoView()
let activityPickerView = ActivityPickerView()

let userInfoGlass = NSGlassEffectView()
userInfoGlass.contentView = userInfoView

let activityPickerGlass = NSGlassEffectView()
activityPickerGlass.contentView = activityPickerView

let stack = NSStackView(views: [userInfoGlass, 
                                activityPickerGlass])
stack.orientation = .horizontal
```

### Adopting NSGlassEffectContainerView — [21:03]

```swift
// Adopting NSGlassEffectContainerView

let userInfoView = UserInfoView()
let activityPickerView = ActivityPickerView()

let userInfoGlass = NSGlassEffectView()
userInfoGlass.contentView = userInfoView
userInfoGlass.cornerRadius = 999

let activityPickerGlass = NSGlassEffectView()
activityPickerGlass.contentView = activityPickerView
activityPickerGlass.cornerRadius = 999

let stack = NSStackView(views: [userInfoGlass, 
                                activityPickerGlass])
stack.orientation = .horizontal

let glassContainer = NSGlassEffectContainerView()
glassContainer.contentView = stack
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/310/5/97dc5fb5-f986-4d12-beb4-c3a389390d36/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/310/5/97dc5fb5-f986-4d12-beb4-c3a389390d36/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/310) — developer.apple.com. Indexed for agent consumption._