---
id: "wwdc2025-282"
event: "wwdc2025"
year: 2025
title: "Make your UIKit app more flexible"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/282"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Make your UIKit app more flexible

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-282](https://developer.apple.com/videos/play/wwdc2025/282)

Find out how your UIKit app can become more flexible on iPhone, iPad, Mac, and Apple Vision Pro by using scenes and container view controllers. Learn to unlock your app’s full potential by transitioning from an app-centric to a scene-based lifecycle, including enhanced window resizing and improved multitasking. Explore enhancements to UISplitViewController, such as interactive column resizing and first-class support for inspector columns. And make your views and controls more adaptive by adopting new layout APIs.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,241 words)

## Documentation & Resources

- [TN3187: Migrating to the UIKit scene-based life cycle](https://developer.apple.com/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3187-Migrating-to-the-UIKit-scene-based-life-cycle.json
- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/UIKit.json

## Code Snippets

### Specify the scene configuration — [3:02]

```swift
// Specify the scene configuration

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication,
                     configurationForConnecting sceneSession: UISceneSession,
                     options: UIScene.ConnectionOptions) -> UISceneConfiguration {

        if sceneSession.role == .windowExternalDisplayNonInteractive {
            return UISceneConfiguration(name: "Timer Scene",
                                        sessionRole: sceneSession.role)
        } else {
            return UISceneConfiguration(name: "Main Scene",
                                        sessionRole: sceneSession.role)
        }
    }
}
```

### Configure the UI — [3:30]

```swift
// Configure the UI

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    var timerModel = TimerModel()

    func scene(_ scene: UIScene,
               willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {

        let windowScene = scene as! UIWindowScene
        let window = UIWindow(windowScene: windowScene)
        window.rootViewController = TimerViewController(model: timerModel)
        window.makeKeyAndVisible()
        self.window = window
    }
}
```

### Handle life cycle events — [3:56]

```swift
// Handle life cycle events

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    var timerModel = TimerModel()

    // ...

    func sceneDidEnterBackground(_ scene: UIScene) {
        timerModel.pause()
    }
}
```

### Restore UI state — [4:09]

```swift
// Restore UI state

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    var timerModel = TimerModel()

    // ...

    func stateRestorationActivity(for scene: UIScene) -> NSUserActivity? {
        let userActivity = NSUserActivity(activityType: "com.example.timer.ui-state")
        userActivity.userInfo = ["selectedTimeFormat": timerModel.selectedTimeFormat]
        return userActivity
    }

    func scene(_ scene: UIScene restoreInteractionStateWith userActivity: NSUserActivity) {
        if let selectedTimeFormat = userActivity?["selectedTimeFormat"] as? String {
            timerModel.selectedTimeFormat = selectedTimeFormat
        }

}
```

### Adapt for the split view controller layout environment — [4:46]

```swift
// Adapt for the split view controller layout environment

override func updateConfiguration(using state: UICellConfigurationState) {

    // ...

    if state.traitCollection.splitViewControllerLayoutEnvironment == .collapsed {
        accessories = [.disclosureIndicator()]
    } else {
        accessories = []
    }
}
```

### Customize the minimum, maximum, and preferred column widths — [6:11]

```swift
// Customize the minimum, maximum, and preferred column widths

let splitViewController = // ...

splitViewController.minimumPrimaryColumnWidth = 200.0
splitViewController.maximumPrimaryColumnWidth = 400.0
splitViewController.preferredSupplementaryColumnWidth = 500.0
```

### Show an inspector column — [7:37]

```swift
// Show an inspector column

let splitViewController = // ... 
splitViewController.setViewController(inspectorViewController, for: .inspector)

splitViewController.show(.inspector)
```

### Managing tab groups — [9:19]

```swift
// Managing tab groups

let group = UITabGroup(title: "Library", ...)
group.managingNavigationController = UINavigationController()

// ...

// MARK: - UITabBarControllerDelegate

func tabBarController(
    _ tabBarController: UITabBarController,
    displayedViewControllersFor tab: UITab,
    proposedViewControllers: [UIViewController]) -> [UIViewController] {

    if tab.identifier == "Library" && !self.allowsSelectingLibraryTab {
        return []
    } else {
        return proposedViewControllers
    }
}
```

### Preferred minimum size — [10:25]

```swift
// Specify a preferred minimum size

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func scene(_ scene: UIScene,
               willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {

        let windowScene = scene as! UIWindowScene
        windowScene.sizeRestrictions?.minimumSize.width = 500.0
    }
}
```

### Position content using the layout margins guide — [11:57]

```swift
// Position content using the layout margins guide

let containerView = // ...
let contentView = // ...

let contentGuide = containerView.layoutMarginsGuide

NSLayoutConstraint.activate([
    contentView.topAnchor.constraint(equalTo: contentGuide.topAnchor),
    contentView.leadingAnchor.constraint(equalTo: contentGuide.leadingAnchor),
    contentView.bottomAnchor.constraint(equalTo: contentGuide.bottomAnchor)
    contentView.trailingAnchor.constraint(equalTo: contentGuide.trailingAnchor)
])
```

### Specify the window control style — [12:34]

```swift
// Specify the window control style

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func preferredWindowingControlStyle(
        for scene: UIWindowScene) -> UIWindowScene.WindowingControlStyle {
        return .unified
    }
}
```

### Respect the window control area — [13:04]

```swift
// Respect the window control area

let containerView = // ...
let contentView = // ...

let contentGuide = containerView.layoutGuide(for: .margins(cornerAdaptation: .horizontal)

NSLayoutConstraint.activate([
    contentView.topAnchor.constraint(equalTo: contentGuide.topAnchor),
    contentView.leadingAnchor.constraint(equalTo: contentGuide.leadingAnchor),
    contentView.bottomAnchor.constraint(equalTo: contentGuide.bottomAnchor),
    contentView.trailingAnchor.constraint(equalTo: contentGuide.trailingAnchor)
])
```

### Request orientation lock — [13:57]

```swift
// Request orientation lock

class RaceViewController: UIViewController {

    override var prefersInterfaceOrientationLocked: Bool {
        return isDriving
    }

    // ...

    var isDriving: Bool = false {
        didSet {
            if isDriving != oldValue {
                setNeedsUpdateOfPrefersInterfaceOrientationLocked()
            }
        }
    }
}
```

### Observe the interface orientation lock — [14:18]

```swift
// Observe the interface orientation lock

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var game = Game()

    func windowScene(
        _ windowScene: UIWindowScene,
        didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

        let wasLocked = previousGeometry.isInterfaceOrientationLocked
        let isLocked = windowScene.effectiveGeometry.isInterfaceOrientationLocked

        if wasLocked != isLocked {
    game.pauseIfNeeded(isInterfaceOrientationLocked: isLocked)
        }
    }
}
```

### Query whether the scene is resizing — [14:44]

```swift
// Query whether the scene is resizing

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var gameAssetManager = GameAssetManager()
    var previousSceneSize = CGSize.zero

    func windowScene(
        _ windowScene: UIWindowScene,
        didUpdateEffectiveGeometry previousGeometry: UIWindowScene.Geometry) {

        let geometry = windowScene.effectiveGeometry
        let sceneSize = geometry.coordinateSpace.bounds.size

        if !geometry.isInteractivelyResizing && sceneSize != previousSceneSize {
            previousSceneSize = sceneSize
            gameAssetManager.updateAssets(sceneSize: sceneSize)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/282/4/24e46505-a3b3-4027-ac3f-0bd2b53dcdeb/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/282/4/24e46505-a3b3-4027-ac3f-0bd2b53dcdeb/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/282) — developer.apple.com. Indexed for agent consumption._
