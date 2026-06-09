---
id: "wwdc2026-278"
event: "wwdc2026"
year: 2026
title: "Modernize your UIKit app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/278"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Modernize your UIKit app

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-278](https://developer.apple.com/videos/play/wwdc2026/278)

Discover the latest updates to UIKit. Learn how to update your iPhone app layouts to work great when resized with iPhone Mirroring and on iPad. Explore new APIs for tab and navigation bars, find out how to prepare your app for new Apple Intelligence capabilities, and get introduced to a skill for your coding agent of choice that helps modernize your codebase.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,429 words)

## Documentation & Resources

- [TN3208: Preparing your app’s launch screen to meet App Store requirements](https://developer.apple.com/documentation/Technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.json
- [TN3210: Optimizing your app for iPhone Mirroring](https://developer.apple.com/documentation/Technotes/tn3210-optimizing-your-app-for-iphone-mirroring) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3210-optimizing-your-app-for-iphone-mirroring
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3210-optimizing-your-app-for-iphone-mirroring.json
- [Make your UIKit app more flexible](https://developer.apple.com/videos/play/wwdc2025/282/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/videos/play/wwdc2025/282/
- [Adapting your app when traits change](https://developer.apple.com/documentation/UIKit/adapting-your-app-when-traits-change) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adapting-your-app-when-traits-change
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adapting-your-app-when-traits-change.json
- [Transitioning to the UIKit scene-based life cycle](https://developer.apple.com/documentation/UIKit/transitioning-to-the-uikit-scene-based-life-cycle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/transitioning-to-the-uikit-scene-based-life-cycle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/transitioning-to-the-uikit-scene-based-life-cycle.json
- [Automatic trait tracking](https://developer.apple.com/documentation/UIKit/automatic-trait-tracking) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/automatic-trait-tracking
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/automatic-trait-tracking.json
- [Human Interface Guidelines: Menus](https://developer.apple.com/design/human-interface-guidelines/menus) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/menus

## Code Snippets

### Use local screen references — [3:24]

```swift
// Use local screen references
// Access the correct screen through a windowScene
let screen = window?.windowScene?.screen

// Pass in local screen references
func generateThumbnail(_ image: UIImage, screen: UIScreen) -> UIImage {
    // existing code, replacing main screen with local screen reference
    // ...
}
```

### Replace screen scale with displayScale — [3:49]

```swift
// Replace the screen's scale with trait collection's displayScale
override func layoutSubviews() {
    super.layoutSubviews()

    // layoutSubviews will be called again automatically when displayScale changes
    let displayScale = traitCollection.displayScale
    // ...
}
```

### Register for trait changes — [4:36]

```swift
// Manually register for trait changes
let displayScaleTrait: [UITrait] = [UITraitDisplayScale.self]
registerForTraitChanges(displayScaleTrait) {
    (view: GalleryView, previousTraitCollection: UITraitCollection) in
    view.cache.invalidate()
}
```

### Monitor effective geometry changes — [5:19]

```swift
// UIWindowSceneDelegate
func windowScene(
    _ windowScene: UIWindowScene,
    didUpdateEffectiveGeometry previousEffectiveGeometry: UIWindowScene.Geometry
) {
    let geometry = windowScene.effectiveGeometry
    let availableSpace = geometry.coordinateSpace.bounds
    // ...
}
```

### Check available space using view bounds — [5:35]

```swift
// Checking available space
override func viewDidLayoutSubviews() {
    super.viewDidLayoutSubviews()

    let availableSpace = view.bounds.size
    // ...
}
```

### Configure motion and location body — [8:12]

```swift
// Configure motion and heading bodies
override func viewDidLoad() {
    super.viewDidLoad()

    motionManager.deviceMotionBody = view
    locationManager.headingBody = view
}
```

### Opt into sidebar layout — [9:51]

```swift
tabBarController.sidebar.preferredPlacement = .sidebar
```

### Check sidebar availability — [10:22]

```swift
tabBarController.sidebar.isAvailable
```

### Set prominent tab identifier — [10:53]

```swift
// Set the prominent tab
let tabs = [
    // ...
]
let tabBarController = UITabBarController(tabs: tabs)
tabBarController.prominentTabIdentifier = "cart"
```

### Customize bar minimization behavior — [11:30]

```swift
// Customize bar minimization behavior
override init(
    nibName nibNameOrNil: String?,
    bundle nibBundleOrNil: Bundle?
) {
    super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)

    navigationItem.barMinimizationBehavior = .always
    navigationItem.barMinimizationSafeAreaAdjustment = .never
}
```

### Export Xcode skills for use in other tools — [15:05]

```bash
xcrun agent skills export
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/278/4/8c3f2e61-52d3-4915-9543-96e2f13adc8b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/278/4/8c3f2e61-52d3-4915-9543-96e2f13adc8b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/278) — developer.apple.com. Indexed for agent consumption._