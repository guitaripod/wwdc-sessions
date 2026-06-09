---
id: "wwdc2021-10053"
event: "wwdc2021"
year: 2021
title: "Qualities of a great Mac Catalyst app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10053"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Qualities of a great Mac Catalyst app

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10053](https://developer.apple.com/videos/play/wwdc2021/10053)

Discover best practices, tools, and techniques to help craft the best possible Mac Catalyst app. We’ll take you through key considerations when you bring your iPad app to macOS, explore detailed code examples for refining your interface and experience, and show you how to distribute your Mac app to everyone.

To get the most out of this session, we recommend a basic familiarity with Mac Catalyst. Watch “What’s new in Mac Catalyst” from WWDC21 to get an overview of the latest features for bringing your iPad app to Mac. And for more on improving your macOS experience, watch “Optimize the interface of your Mac Catalyst app” from WWDC20.

**Keywords:** `continuity camera`, `controls`, `distribution`, `idiom`, `responder chain`, `scenes`, `sharing`, `state restoration`, `toolbar`, `unscaled`, `user activity`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,465 words)

## Documentation & Resources

- [Building and improving your app with Mac Catalyst](https://developer.apple.com/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst.json
- [Bring an iPad App to the Mac with Mac Catalyst](https://developer.apple.com/tutorials/Mac-Catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/tutorials/Mac-Catalyst
- [Accessibility design for Mac Catalyst](https://developer.apple.com/documentation/Accessibility/accessibility_design_for_mac_catalyst) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/accessibility_design_for_mac_catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/accessibility_design_for_mac_catalyst.json
- [Human Interface Guidelines: Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/mac-catalyst
- [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/mac-catalyst.json
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.json

## Code Snippets

### System button — [6:50]

```swift
let button = UIButton(type: .system)
button.setTitle("Button", for: .normal)
```

### Pull-down button — [7:06]

```swift
button.menu = UIMenu(...)
button.showsMenuAsPrimaryAction = true
```

### Pop-up button — [7:44]

```swift
button.menu = UIMenu(...)
button.showsMenuAsPrimaryAction = true
button.changesSelectionAsPrimaryAction = true
```

### Checkbox — [8:24]

```swift
let checkbox = UISwitch()
if checkbox.style == .checkbox {
    checkbox.title = "Checkbox"
}
```

### Delegating actions — [13:20]

```swift
final class MyView: UIView {
    override func target(forAction action: Selector, withSender sender: Any?) -> Any? {
        if action == #selector(Model.setAsFavorite(_:)) {
            return myModel
        } else {
            return super.target(forAction: action, withSender: sender)
        }
    }
}
```

### Requesting a new scene — [14:43]

```swift
let viewDetailActivityType = "viewDetail"
let itemIDKey = "itemID"

final class MyView: UIView {
    @objc func viewDoubleClicked(_ sender: Any?) {
        let userActivity = NSUserActivity(activityType: viewDetailActivityType)
        userActivity.userInfo = [itemIDKey: selectedItem.itemID]
        UIApplication.shared.requestSceneSessionActivation(nil,
            userActivity: userActivity,
            options: nil,
            errorHandler: { error in //...
        })
    }
    //...
}
```

### Responding to a new scene request — [15:57]

```swift
let viewDetailActivityType = "viewDetail"

final class AppDelegate: UIApplicationDelegate {
    func application(_ application: UIApplication, 
        configurationForConnecting session: UISceneSession, 
        options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        if let activity = options.userActivities.first {
            if activity.activityType == viewDetailActivityType {
                return UISceneConfiguration(name: "DetailViewer", sessionRole:session.role)
            }
        }
        return UISceneConfiguration(name: "Default Configuration",
            sessionRole: session.role)
    }
    //...
}
```

### Setting item ID on new scene's root view controller — [17:13]

```swift
let itemIDKey = "itemID"

final class SceneDelegate: UIWindowSceneDelegate {
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
        options: UIScene.ConnectionOptions) {
        if let userActivity = connectionOptions.userActivities.first {
            if let itemId = userActivity.userInfo?[itemIDKey] as? ItemIDType {
               // Set item ID on new view controller
            }
        }
        //...
    }
    //...
```

### Saving state for later restoration — [17:47]

```swift
final class SceneDelegate: UIWindowSceneDelegate {
    func stateRestorationActivity(for scene: UIScene) -> NSUserActivity? {
        //...
    }
}
```

### State restoration — [17:57]

```swift
final class AppDelegate: UIApplicationDelegate {
    func application(_ application: UIApplication, 
        configurationForConnecting session: UISceneSession, 
        options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        //...
    }
}
```

### Handle both new scene requests and state restoration — [18:42]

```swift
let itemIDKey = "itemID"

final class SceneDelegate: UIWindowSceneDelegate {
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
        options connectionOptions: UIScene.ConnectionOptions) {
        if let userActivity = connectionOptions.userActivities.first ??
            session.stateRestorationActivity {
            if let itemId = userActivity.userInfo?[itemIDKey] as? ItemIDType {
               // Set item ID on new view controller
            }
        }
    }
}
```

### Provide sharing configuration for the scene — [20:20]

```swift
final class RootViewController: UIViewController {
    override var activityItemsConfiguration: UIActivityItemsConfigurationReading? {
      get { UIActivityItemsConfiguration(objects: [image]) }
      //...
    }
}
```

### Support sharing through context menu — [20:56]

```swift
final class MyView: UIView {
    override var activityItemsConfiguration: UIActivityItemsConfigurationReading? {
      get { UIActivityItemsConfiguration(objects: images) }
      //...
    }

    func viewDidLoad() {
      let contextMenuInteraction = UIContextMenuInteraction(delegate: self)
      addInteraction(contextMenuInteraction)
    }
}
```

### Supporting continuity camera — [22:08]

```swift
final class MyView: UIView {
override var pasteConfiguration: UIPasteConfiguration? {
  get { UIPasteConfiguration(forAcceptingClass: UIImage.self) }
  //...
}

func willMove(toWindow: UIWindow) {
   addInteraction(contextMenuInteraction)
}

override func paste(itemProviders: [NSItemProvider]) {
   for itemProvider in itemProviders {
        if itemProvider.canLoadObject(ofClass: UIImage.self) {
            if let image = try? await itemProvider.loadObject(ofClass:UIImage.self) {
                insertImage(image)
            }          
            //...
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10053/3/2422D003-327B-45A7-95E1-047C49B735B3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10053/3/2422D003-327B-45A7-95E1-047C49B735B3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10053) — developer.apple.com. Indexed for agent consumption._