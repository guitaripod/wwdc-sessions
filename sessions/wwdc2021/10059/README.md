---
id: "wwdc2021-10059"
event: "wwdc2021"
year: 2021
title: "What's new in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10059"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in UIKit

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10059](https://developer.apple.com/videos/play/wwdc2021/10059)

Discover the latest updates and improvements to UIKit and learn how to build better iPadOS, iOS, and Mac Catalyst apps. We’ll take you through UI refinements, productivity updates, and API enhancements, and help you explore performance improvements and security & privacy features.

**Keywords:** `aqua`, `async`, `cocoa`, `collection view`, `color picker`, `content size categories`, `context menus`, `copy and paste`, `date picker`, `drag &amp; drop`, `dynamic type`, `ios`, `ipados`, `keyboard navigation`, `keyboard shortcuts`, `mac catalyst`, `multitasking`, `multi-window`, `paste`, `pasteboard`, `pointer`, `privacy`, `sf symbols`, `shortcuts`, `state restoration`, `symbols`, `table view`, `uibutton`, `uicolor`, `uicolorpicker`, `uicontextmenuinteraction`, `uidatepicker`, `uiimage`, `uipasteboard`, `uiscene`, `uitabbar`, `uitoolbar`, `uiwindowscene`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,914 words)

## Documentation & Resources

- [Introducing Private Click Measurement, PCM](https://webkit.org/blog/11529/introducing-private-click-measurement-pcm/) _documentation_
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Building an "Open in New Window" action — [1:41]

```swift
// Building an "Open in New Window" action

let newSceneAction = UIWindowScene.ActivationAction({ _ in

    // Create the user activity that represents the new scene content
    let userActivity = NSUserActivity(activityType: "com.myapp.detailscene")

    // Return the activation configuration
    return UIWindowScene.ActivationConfiguration(userActivity: userActivity)

})
```

### UIMenuBuilder — [3:06]

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {

    override func buildMenu(with builder: UIMenuBuilder) {

        // Use the builder to modify the main menu...
    }
}
```

### UIBarAppearance — [6:26]

```swift
let appearance = UITabBarAppearance()
appearance.backgroundEffect = nil
appearance.backgroundColor = .blue

tabBar.scrollEdgeAppearance = appearance


let scrollView = ... // Content scroll view in your app
viewController.setContentScrollView(scrollView, for: .bottom)
```

### Creating a button with UIButton.Configuration — [11:31]

```swift
// Creating a button with UIButton.Configuration

var config = UIButton.Configuration.tinted()

config.title = "Add to Cart"
config.image = UIImage(systemName: "cart.badge.plus")
config.imagePlacement = .trailing
config.buttonSize = .large
config.cornerStyle = .capsule

self.addToCartButton = UIButton(configuration: config)
```

### Using a hierarchical color symbol — [13:30]

```swift
// Using a hierarchical color symbol

let configuration = UIImage.SymbolConfiguration(
    hierarchicalColor: UIColor.systemOrange
)

let image = UIImage(
    systemName: "sun.max.circle.fill",
    withConfiguration: configuration
)
```

### New UICollectionViewCell.configurationUpdateHandler closures — [19:30]

```swift
// New UICollectionViewCell.configurationUpdateHandler closures

let cell: UICollectionViewCell = ...

cell.configurationUpdateHandler = { cell, state in
    var content = UIListContentConfiguration.cell().updated(for: state)
    content.text = "Hello world!"
    if state.isDisabled {
        content.textProperties.color = .systemGray
    }
    cell.contentConfiguration = content
}
```

### Image display preparation — [21:01]

```swift
// Image display preparation

if let image = UIImage(contentsOfFile: pathToImage) {
    // Prepare the image for display asynchronously.
    Task {
        let preparedImage = await image.byPreparingForDisplay()

        imageView.image = preparedImage
    }
}
```

### Image thumbnailing — [21:29]

```swift
// Image thumbnailing

if let bigImage = UIImage(contentsOfFile: pathToBigImage) {
    // Prepare the thumbnail asynchronously.
    Task {
        let smallImage = await bigImage.byPreparingThumbnail(ofSize: smallSize)

        imageView.image = smallImage
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10059/5/A2B84844-AAFE-437F-B1A2-7D4CC79957E2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10059/5/A2B84844-AAFE-437F-B1A2-7D4CC79957E2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10059) — developer.apple.com. Indexed for agent consumption._