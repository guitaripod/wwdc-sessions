---
id: "wwdc2025-243"
event: "wwdc2025"
year: 2025
title: "What’s new in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/243"
topics: ["Privacy & Security", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What’s new in UIKit

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-243](https://developer.apple.com/videos/play/wwdc2025/243)

Modernize your app with the latest APIs in UIKit, including enhanced menu bar support, automatic observation tracking, a new UI update method, and improvements to animations. We’ll also cover how you can include SwiftUI scenes in your UIKit app and explore SF Symbols, HDR color pickers, and more.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,309 words)

## Documentation & Resources

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines
- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/UIKit.json

## Code Snippets

### Main menu system configuration — [4:56]

```swift
// Main menu system configuration

var config = UIMainMenuSystem.Configuration()

// Declare support for default commands, like printing
config.printingPreference = .included

// Opt out of default commands, like inspector
config.inspectorPreference = .removed

// Configure the Find commands to be a single "Search" element
config.findingConfiguration.style = .search
```

### Main menu system build configuration — [5:39]

```swift
// Main menu system configuration

// Have the main menu system build using this configuration, and make custom additions.
// Call this early, e.g. in application(_:didFinishLaunchingWithOptions:), and call it once
UIMainMenuSystem.shared.setBuildConfiguration(config) { builder in
    builder.insertElements([...], afterCommand: #selector(copy(_:)))

    let deleteKeyCommand = UIKeyCommand(...)
    builder.replace(command: #selector(delete(_:)), withElements: [deleteKeyCommand])
}
```

### Keyboard shortcut repeatability — [7:01]

```swift
// Keyboard shortcut repeatability

let keyCommand = UIKeyCommand(...)
keyCommand.repeatBehavior = .nonRepeatable
```

### Focus-based deferred menu elements (App Delegate) — [7:43]

```swift
// Focus-based deferred menu elements

extension UIDeferredMenuElement.Identifier {
    static let browserHistory: Self = .init(rawValue: "com.example.deferred-element.history")
}

// Create a focus-based deferred element that will display browser history
let historyDeferredElement = UIDeferredMenuElement.usingFocus(
    identifier: .browserHistory,
    shouldCacheItems: false
)

// Insert it into the app’s custom History menu when building the main menu
builder.insertElements([historyDeferredElement], atEndOfMenu: .history)
```

### Focus-based deferred menu elements (View Controller) — [8:06]

```swift
// Focus-based deferred menu elements

class BrowserViewController: UIViewController {

    // ...

    override func provider(
        for deferredElement: UIDeferredMenuElement
    ) -> UIDeferredMenuElement.Provider? {
        if deferredElement.identifier == .browserHistory {
            return UIDeferredMenuElement.Provider { completion in
                let browserHistoryMenuElements = profile.browserHistoryElements()
                completion(browserHistoryMenuElements)
            }
        }
        return nil
    }
}
```

### Using an Observable object and automatic observation tracking — [10:54]

```swift
// Using an Observable object and automatic observation tracking

@Observable class UnreadMessagesModel {
    var showStatus: Bool
    var statusText: String
}

class MessageListViewController: UIViewController {
    var unreadMessagesModel: UnreadMessagesModel

    var statusLabel: UILabel

    override func viewWillLayoutSubviews() {
        super.viewWillLayoutSubviews()

        statusLabel.alpha = unreadMessagesModel.showStatus ? 1.0 : 0.0
        statusLabel.text = unreadMessagesModel.statusText
    }
}
```

### Configuring a UICollectionView cell with automatic observation tracking — [11:48]

```swift
// Configuring a UICollectionView cell with automatic observation tracking

@Observable class ListItemModel {
    var icon: UIImage
    var title: String
    var subtitle: String
}

func collectionView(
    _ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath
) -> UICollectionViewCell {
    let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
    let listItemModel = listItemModel(for: indexPath)
    cell.configurationUpdateHandler = { cell, state in
        var content = UIListContentConfiguration.subtitleCell()
        content.image = listItemModel.icon
        content.text = listItemModel.title
        content.secondaryText = listItemModel.subtitle
        cell.contentConfiguration = content
    }
    return cell
}
```

### Using automatic observation tracking and updateProperties() — [13:27]

```swift
// Using automatic observation tracking and updateProperties()

@Observable class BadgeModel {
   var badgeCount: Int?
}

class MyViewController: UIViewController {
   var model: BadgeModel
   let folderButton: UIBarButtonItem

    override func updateProperties() {
        super.updateProperties()

        if let badgeCount = model.badgeCount {
            folderButton.badge = .count(badgeCount)
        } else {
            folderButton.badge = nil
        }
   }
}
```

### Using the flushUpdates animation option to automatically animate updates — [16:57]

```swift
// Using the flushUpdates animation option to automatically animate updates

// Automatically animate changes with Observable objects
UIView.animate(options: .flushUpdates) {
    model.badgeColor = .red
}
```

### Automatically animate changes to Auto Layout constraints with flushUpdates — [17:23]

```swift
// Automatically animate changes to Auto Layout constraints
UIView.animate(options: .flushUpdates) {
    // Change the constant of a NSLayoutConstraint
    topSpacingConstraint.constant = 20

    // Change which constraints are active
    leadingEdgeConstraint.isActive = false
    trailingEdgeConstraint.isActive = true
}
```

### Setting up a UIHostingSceneDelegate — [18:07]

```swift
// Setting up a UIHostingSceneDelegate

import UIKit
import SwiftUI

class ZenGardenSceneDelegate: UIResponder, UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "zengarden") {
            ZenGardenView()
        }

        #if os(visionOS)
        ImmersiveSpace(id: "zengardenspace") {
            ZenGardenSpace()
        }
        .immersionStyle(selection: .constant(.full),
                        in: .mixed, .progressive, .full)
        #endif 
    }
}
```

### Using a UIHostingSceneDelegate — [18:28]

```swift
// Using a UIHostingSceneDelegate 

func application(_ application: UIApplication,
    configurationForConnecting connectingSceneSession: UISceneSession,
    options: UIScene.ConnectionOptions) -> UISceneConfiguration {

    let configuration = UISceneConfiguration(name: "Zen Garden Scene",
                                             sessionRole: connectingSceneSession.role)

    configuration.delegateClass = ZenGardenSceneDelegate.self
    return configuration
}
```

### Requesting a scene — [18:41]

```swift
// Requesting a scene

func openZenGardenSpace() {
    let request = UISceneSessionActivationRequest(
        hostingDelegateClass: ZenGardenSceneDelegate.self,
        id: “zengardenspace")!

    UIApplication.shared.activateSceneSession(for: request)
}
```

### HDR color support — [19:18]

```swift
// Create an HDR red relative to a 2.5x peak white
let hdrRed = UIColor(red: 1.0, green: 0.0, blue: 0.0, alpha: 1.0, linearExposure: 2.5)
```

### HDR color picking — [19:50]

```swift
// Support picking HDR colors relative to a 
// maximum peak white of 2x
colorPickerController.maximumLinearExposure = 2.0
```

### Mixing SDR and HDR content — [20:06]

```swift
// Mixing SDR and HDR content

registerForTraitChanges([UITraitHDRHeadroomUsageLimit.self]) { traitEnvironment, previousTraitCollection in
    let currentHeadroomLimit = traitEnvironment.traitCollection.hdrHeadroomUsageLimit
    // Update HDR usage based on currentHeadroomLimit’s value
}
```

### Adopting Swift notifications — [20:54]

```swift
// Adopting Swift notifications

override func viewDidLoad() {
    super.viewDidLoad()

    let keyboardObserver = NotificationCenter.default.addObserver(
        of: UIScreen.self
        for: .keyboardWillShow
    ) { message in
        UIView.animate(
            withDuration: message.animationDuration, delay: 0, options: .flushUpdates
        ) {
            // Use message.endFrame to animate the layout of views with the keyboard
            let keyboardOverlap = view.bounds.maxY - message.endFrame.minY
            bottomConstraint.constant = keyboardOverlap
        }
    }
}
```

### Using a symbol content transition to automatically animate symbol updates — [24:26]

```swift
// Using a symbol content transition to automatically animate symbol updates

var configuration = UIButton.Configuration.plain()
configuration.symbolContentTransition = UISymbolContentTransition(.replace)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/243/4/9d493d7f-4ae0-47d2-9b97-c3ad66cdf3c4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/243/4/9d493d7f-4ae0-47d2-9b97-c3ad66cdf3c4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/243) — developer.apple.com. Indexed for agent consumption._
