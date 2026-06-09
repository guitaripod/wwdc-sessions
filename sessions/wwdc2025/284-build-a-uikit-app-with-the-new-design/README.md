---
id: "wwdc2025-284"
event: "wwdc2025"
year: 2025
title: "Build a UIKit app with the new design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/284"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build a UIKit app with the new design

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-284](https://developer.apple.com/videos/play/wwdc2025/284)

Update your UIKit app to take full advantage of the new design system. We’ll dive into key changes to tab views, split views, bars, presentations, search, and controls, and show you how to use Liquid Glass in your custom UI. To get the most out of this video, we recommend first watching “Get to know the new design system” for general design guidance.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,347 words)

## Documentation & Resources

- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TechnologyOverviews/adopting-liquid-glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TechnologyOverviews/adopting-liquid-glass.json
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines

## Code Snippets

### Minimize tab bar on scroll — [2:31]

```swift
// Minimize tab bar on scroll

tabBarController.tabBarMinimizeBehavior = .onScrollDown
```

### Add a bottom accessory — [3:08]

```swift
// Add a bottom accessory

let nowPlayingView = NowPlayingView()
let accessory = UITabAccessory(contentView: nowPlayingView)
tabBarController.bottomAccessory = accessory
```

### Update the accessory with the tabAccessoryEnvironment trait — [3:35]

```swift
// Update the accessory with the trait

registerForTraitChanges([UITraitTabAccessoryEnvironment.self]) { (view: MiniPlayerView, _) in
    let isInline = view.traitCollection.tabAccessoryEnvironment == .inline
    view.updatePlayerAppearance(inline: isInline)
}

// Automatic trait tracking with updateProperties()
override func updateProperties() {
    super.updateProperties()
    let isInline = traitCollection.tabAccessoryEnvironment == .inline
    updatePlayerAppearance(inline: isInline)
}
```

### Extend content under the sidebar — [5:51]

```swift
// Extend content underneath the sidebar

let posterImageView = UIImageView(image: ...)

let extensionView = UIBackgroundExtensionView()
extensionView.contentView = posterImageView
view.addSubview(extensionView)

let detailsView = ShowDetailsView()
view.addSubview(detailsView)
```

### Adjust the effect layout — [6:51]

```swift
// Adjust the effect layout

let posterImageView = UIImageView(image: ...)

let extensionView = UIBackgroundExtensionView()
extensionView.contentView = posterImageView
extensionView.automaticallyPlacesContentView = false
view.addSubview(extensionView)

posterImageView.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    posterImageView.topAnchor.constraint(equalTo: extensionView.topAnchor),
    posterImageView.leadingAnchor.constraint(equalTo: extensionView.safeAreaLayoutGuide.leadingAnchor),
    posterImageView.trailingAnchor.constraint(equalTo: extensionView.safeAreaLayoutGuide.trailingAnchor),
    posterImageView.bottomAnchor.constraint(equalTo: extensionView.safeAreaLayoutGuide.bottomAnchor),
])
```

### Custom grouping — [8:38]

```swift
// Custom grouping

navigationItem.rightBarButtonItems = [
    doneButton,
    flagButton,
    folderButton,
    infoButton,
    .fixedSpace(0),
    shareButton,
    selectButton
]
```

### UIBarButtonItem tint color and style — [8:53]

```swift
// Tint color and style

let flagButton = UIBarButtonItem(image: UIImage(systemName: "flag.fill"))
flagButton.tintColor = .systemOrange
flagButton.style = .prominent
```

### Toolbar with evenly distributed items in a single background — [9:10]

```swift
// Toolbar with evenly distributed items, grouped in a single background.

let flexibleSpace = UIBarButtonItem.flexibleSpace()
flexibleSpace.hidesSharedBackground = false

toolbarItems = [
   .init(image: UIImage(systemName: "location")),
   flexibleSpace,
   .init(image: UIImage(systemName: "number")),
   flexibleSpace,
   .init(image: UIImage(systemName: "camera")),
   flexibleSpace,
   .init(image: UIImage(systemName: "trash")),
]
```

### Titles and subtitles — [10:15]

```swift
// Titles and subtitles

navigationItem.title = "Inbox"
navigationItem.subtitle = "49 Unread"
```

### Large subtitle view — [10:27]

```swift
// Titles and subtitles

navigationItem.title = "Inbox"
navigationItem.largeSubtitleView = filterButton
```

### Edge effect for a custom container — [11:20]

```swift
// Edge effect’s custom container

let interaction = UIScrollEdgeElementContainerInteraction()
interaction.scrollView = contentScrollView
interaction.edge = .bottom

buttonsContainerView.addInteraction(interaction)
```

### Hard edge effect style — [11:48]

```swift
// Hard edge effect style

scrollView.topEdgeEffect.style = .hard
```

### Morph popover from its source button — [13:55]

```swift
// Morph popover from its source button

viewController.popoverPresentationController?.sourceItem = barButtonItem
```

### Morph sheet from bar button — [14:07]

```swift
// Morph sheet from bar button

viewController.preferredTransition = .zoom { _ in 
     folderBarButtonItem
}
```

### Source item for action sheets — [14:46]

```swift
// Setting source item for action sheets

alertController.popoverPresentationController?.sourceItem = barButtonItem
```

### Placing search in the toolbar — [15:36]

```swift
// Place search bar in a toolbar

toolbarItems = [
    navigationItem.searchBarPlacementBarButtonItem,
    .flexibleSpace(),
    addButton
]
```

### Universally accessible search on iPad — [16:01]

```swift
// Place search at the trailing edge of the navigation bar

navigationItem.searchBarPlacementAllowsExternalIntegration = true
```

### Activate the search field when search bar is tapped — [16:47]

```swift
// Activate the search field when search bar is tapped

searchTab.automaticallyActivatesSearch = true
```

### Search as a dedicated view — [17:03]

```swift
// Search as a dedicated view

navigationItem.preferredSearchBarPlacement = .integratedCentered
```

### Buttons — [17:52]

```swift
// Standard glass
button.configuration = .glass()

// Prominent glass
tintedButton.configuration = .prominentGlass()
```

### Neutral slider with 5 ticks and a neutral value — [18:16]

```swift
// Neutral slider with 5 ticks and a neutral value
slider.trackConfiguration = .init(allowsTickValuesOnly: true,
                                  neutralValue: 0.2,
                                  numberOfTicks: 5)
```

### Thumbless slider — [18:59]

```swift
// Thumbless slider
slider.sliderStyle = .thumbless
```

### Glass for custom views — [20:28]

```swift
// Adopting glass for custom views

let effectView = UIVisualEffectView()
addSubview(effectView)

let glassEffect = UIGlassEffect()
// Animating setting the effect results in a materialize animation
UIView.animate {
    effectView.effect = glassEffect
}
```

### Custom corner configuration — [20:49]

```swift
// Custom corner configuration

UIView.animate {
    effectView.cornerConfiguration = .fixed(8)
}
```

### Dark mode — [20:54]

```swift
// Adapting to dark mode

UIView.animate {
    view.overrideUserInterfaceStyle = .dark
}
```

### Adding glass to an existing glass container — [21:02]

```swift
// Adding glass to an existing glass container

let container = UIVisualEffectView()
container.effect = UIGlassEffect()

container.contentView.addSubview(effectView)
```

### Container relative corners — [21:08]

```swift
// Container relative corners

UIView.animate {
    effectView.cornerConfiguration = .containerRelative()
    effectView.frame.origin = CGPoint(x: 10, y: 10)
}
```

### Container relative corners, animated — [21:23]

```swift
// Container relative corners

UIView.animate {
    effectView.frame.origin = CGPoint(x: 30, y: 30)
}
```

### Glass adapts based on its size — [21:30]

```swift
// Glass adapts based on its size

UIView.animate {
    view.overrideUserInterfaceStyle = .light
    effectView.bounds.size = CGSize(width: 250, height: 88)
}

UIView.animate {
    effectView.bounds.size = CGSize(width: 150, height: 44)
}
```

### Adding content to glass views — [21:49]

```swift
// Adding content to glass views

let label = UILabel()
label.text = "WWDC25"
label.textColor = .secondaryLabel

effectView.contentView.addSubview(label)
```

### Applying tint color to glass — [22:15]

```swift
// Applying tint color to glass

let glassEffect = UIGlassEffect()
glassEffect.tintColor = .systemBlue

UIView.animate {
    effectView.effect = glassEffect
    label.textColor = .label
}
```

### Using custom colors with glass — [22:33]

```swift
// Using custom colors with glass

let glassEffect = UIGlassEffect()
glassEffect.tintColor = UIColor(displayP3Red: r,
                                green: g,
                                blue: b,
                                alpha: 1)

UIView.animate {
    effectView.effect = glassEffect
    // Animate out the label
    label.alpha = 0
}
```

### Enabling interactive glass behavior — [23:03]

```swift
// Enabling interactive glass behavior

let glassEffect = UIGlassEffect()
glassEffect.isInteractive = true

effectView.effect = glassEffect
```

### Animating glass out using dematerialize animation — [23:20]

```swift
// Animating glass out using dematerialize animation

UIView.animate {
    effectView.effect = nil
}
```

### Adding glass elements to a container — [23:52]

```swift
// Adding glass elements to a container

let container = UIGlassContainerEffect()
let containerView = UIVisualEffectView(effect: container)

let glassEffect = UIGlassEffect()
let view1 = UIVisualEffectView(effect: glassEffect)
let view2 = UIVisualEffectView(effect: glassEffect)

containerEffectView.contentView.addSubview(view1)
containerEffectView.contentView.addSubview(view2)
```

### Adjusting the container spacing — [24:12]

```swift
// Adjusting the container spacing

let containerEffect = UIGlassContainerEffect()
containerEffect.spacing = 20
containerEffectView.effect = containerEffect
```

### Merging two glass views — [24:27]

```swift
// Merging two glass views

UIView.animate {
    view1.frame = finalFrame
    view2.frame = finalFrame
}
```

### Dividing glass into multiple views — [24:33]

```swift
// Dividing glass into multiple views

UIView.performWithoutAnimation {
    for view in finalViews {
        containerEffectView.contentView.addSubview(view)
        view.frame = startFrame
    }
}

UIView.animate {
    for view in finalViews {
        view.frame = finalFrame(for: view)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/284/4/afb20876-65b2-4aeb-bd50-66e4df1b2281/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/284/4/afb20876-65b2-4aeb-bd50-66e4df1b2281/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/284) — developer.apple.com. Indexed for agent consumption._
