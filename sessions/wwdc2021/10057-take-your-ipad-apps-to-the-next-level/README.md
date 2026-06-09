---
id: "wwdc2021-10057"
event: "wwdc2021"
year: 2021
title: "Take your iPad apps to the next level"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10057"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Take your iPad apps to the next level

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10057](https://developer.apple.com/videos/play/wwdc2021/10057)

Make even better iPad apps: Learn how you can adopt prominent scenes for uninterrupted, focused interactions. Help people stay engaged and fast with keyboard shortcuts and the keyboard shortcut interface. Explore how the latest in pointer enhancements can help your app boost productivity.

**Keywords:** `keyboard`, `main menu`, `menu`, `menu bar`, `menu system`, `mouse`, `pointer`, `print`, `responder`, `scene`, `shortcut`, `trackpad`, `uicommand`, `uikeycommand`, `uimenubuilder`, `uimenu printing`, `uipointerinteraction`, `uiwindowscene`, `window`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,008 words)

## Documentation & Resources

- [Adding hardware keyboard support to your app](https://developer.apple.com/documentation/UIKit/adding-hardware-keyboard-support-to-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-hardware-keyboard-support-to-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-hardware-keyboard-support-to-your-app.json
- [Enhancing your iPad app with pointer interactions](https://developer.apple.com/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions.json
- [Human Interface Guidelines: Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/pointing-devices
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.json
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Build an "Open in New Window" action — [4:56]

```swift
let <#newSceneAction#> = UIWindowScene.ActivationAction({ _ in

    // Create the user activity that represents the new scene content.
    let userActivity = NSUserActivity(activityType: <#User Activity Type#>)

    // Return the activation configuration.
    return UIWindowScene.ActivationConfiguration(userActivity: userActivity)

})
```

### Use an alternate action with UIWindowScene.ActivationAction — [5:43]

```swift
// Create an action to use when multiple scenes are not available.
let alternateAction = UIAction(title: <#Alternate Action Title#>,
                               image: <#Alternate Action Image#>,
                             handler: { _ in
    <#Perform Alternate Action#>
})

// Create the scene activation action with the alternate.
let newSceneAction = UIWindowScene.ActivationAction(alternate: alternateAction) { _ in

    // Create the user activity that represents the new scene content.
    let userActivity = NSUserActivity(activityType: <#Scene Activity Type#>)

    // Return the activation configuration.
    return UIWindowScene.ActivationConfiguration(userActivity: userActivity)
}
```

### Present a scene from a collection view with a gesture — [6:58]

```swift
func collectionView(_ collectionView: UICollectionView,
                    sceneActivationConfigurationForItemAt indexPath: IndexPath,
                    point: CGPoint) -> UIWindowScene.ActivationConfiguration? {

    // Get the item's user activity.
    guard let itemActivity = <#User Activity#> else {
        // Return nil if item can’t be opened in a dedicated scene.
        return nil
    }

    // Return the activation configuration.
    return UIWindowScene.ActivationConfiguration(userActivity: itemActivity)
}
```

### Present a scene from a custom view with a gesture — [7:28]

```swift
// Create an activation interaction.
let newSceneInteraction = UIWindowScene.ActivationInteraction { interaction, point in
    // Get the activity for specific point in view.
    guard let userActivity = <#User Activity#> else { return nil }

    // Return an activation configuration.
    return UIWindowScene.ActivationConfiguration(userActivity: userActivity)

} errorHandler: { error in
    // Present the content in another manner.
    <#Present Content#>
}

// Add interaction to the view.
<#View#>.addInteraction(newSceneInteraction)
```

### Customize scene transition preview — [8:53]

```swift
// Create the activation configuration.
let itemActivity = NSUserActivity(activityType: <#User Activity Type#>)
let configuration = UIWindowScene.ActivationConfiguration(userActivity: itemActivity)

// If the cell has a subview to use as the preview, create the custom preview.
if let cell = collectionView.cellForItem(at: indexPath) as? <#Expected Cell Class#> {
    configuration.preview = UITargetedPreview(view: cell.<#Subview For Preview#>)
}

// Return the activation configuration.
return configuration
```

### Save scene state — [10:18]

```swift
func stateRestorationActivity(for scene: UIScene) -> NSUserActivity? {
    guard let viewController = self.window?.rootViewController as? <#Expected View Controller Class#> else {
        return nil
    }

    let stateActivity = NSUserActivity(activityType: <#State Restoration Activity Type#>)

    stateActivity.addUserInfoEntries(from: [
        // Save content of a text field.
        <#Content Key#>: viewController.<#Text Field#>.text
    ])

    return stateActivity
}
```

### Save scene state with interaction state — [11:16]

```swift
func stateRestorationActivity(for scene: UIScene) -> NSUserActivity? {
    guard let viewController = self.window?.rootViewController as? <#Expected View Controller Class#> else {
        return nil
    }

    let stateActivity = NSUserActivity(activityType: <#State Restoration Activity Type#>)

    stateActivity.addUserInfoEntries(from: [
        // Save content of a text field.
        <#Content Key#>: viewController.<#Text Field#>.text,

        // Save interaction state of a text field.
        <#Interaction State Key#>: viewController.<#Text Field#>.interactionState
    ])

    return stateActivity
}
```

### Restore scene state — [12:13]

```swift
func scene(_ scene: UIScene, restoreInteractionState stateRestorationActivity: NSUserActivity) {
    guard let viewController = window?.rootViewController as? <#Expected View Controller Class#>,
          let userInfo = stateRestorationActivity.userInfo
    else { return }

    if let content = userInfo[<#Content Key#>] as? String {
        // Restore the content first.
        viewController.<#Text Field#>.text = content

        // Then, restore the text field’s interaction state.
        if let interactionState = userInfo[<#Interaction State Key#>] {
            viewController.<#Text Field#>.interactionState = interactionState
        }
    }
}
```

### Restore scene state asynchronously — [13:15]

```swift
func scene(_ scene: UIScene, restoreInteractionState stateRestorationActivity: NSUserActivity) {
    guard let viewController = window?.rootViewController as? <#Expected View Controller Class#> else { return }

    // Request an extension.
    scene.extendStateRestoration()

    // Fetch content asynchronously.
    <#self.someAsyncFunction#> { result in
        <#Restore Content#>

        // Signal that state has been restored.
        scene.completeStateRestoration()
    }
}
```

### Modify the main menu — [17:15]

```swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)

    // Ensure the builder is modifying the main menu.
    guard builder.system == .main else { return }

    // Use the builder to modify the main menu...
}
```

### Add key commands to the main menu — [17:37]

```swift
// Create a menu with key commands.
let tabMenu = UIMenu(options: .displayInline, children: [
    UIKeyCommand(title: NSLocalizedString("New Tab", ...),
                 action: #selector(BrowserViewController.newTab(_:)),
                 input: "t",
                 modifierFlags: .command),
    UIKeyCommand(...)
])

// Insert tabMenu into the File menu.
builder.insertChild(tabMenu, atStartOfMenu: .file)
```

### Add a custom menu category — [18:19]

```swift
// Create a "Bookmarks" menu.
let bookmarksMenu = UIMenu(title: NSLocalizedString("Bookmarks", ...),
                           children: [...])

// Insert the Bookmarks menu into the root menu, after View.
builder.insertSibling(bookmarksMenu, afterMenu: .view)

// Insert another menu into the Bookmarks menu.
let sortBookmarksMenu = UIMenu(...)
builder.insertChild(sortBookmarksMenu, atEndOfMenu: bookmarksMenu.identifier)
```

### Customizing key command performability — [22:38]

```swift
override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
    if action == #selector(closeTab(_:)) {
        return !openTabs.isEmpty
    } else {
        return super.canPerformAction(action, withSender: sender)
    }
}
```

### Customizing key command appearance — [23:26]

```swift
override func validate(_ command: UICommand) {
    if command.action == #selector(toggleBookmark(_:)) {
        if currentTab.isInBookmarks {
            command.title = NSLocalizedString("Add to Bookmarks", ...)
        } else {
            command.title = NSLocalizedString("Remove from Bookmarks", ...)
        }
    } else {
        return super.validate(command)
    }
}
```

### Supporting multi-selection using UIBandSelectionInteraction — [28:47]

```swift
// Support multi-selection using UIBandSelectionInteraction.

let selectionInteraction = UIBandSelectionInteraction { [weak self] interaction in
    guard let strongSelf = self else { return }

    // Handle selection by responding to interaction state.
    if interaction.state == .selecting {
        strongSelf.selectItemsInRect(interaction.selectionRect)
    } 
    else if interaction.state == .ended {
        strongSelf.finalizeSelection()
    }
}

view.addInteraction(selectionInteraction)
```

### Customizing a predefined pointer accessory position — [33:01]

```swift
var position = UIPointerAccessory.Position.topRight
position.offset = 40.0
```

### Creating a custom pointer accessory position — [33:14]

```swift
let position = UIPointerAccessory.Position(offset: 23.0, angle: .pi * 1.25)
```

### Pointer Accessories — [33:27]

```swift
// Attach two arrow accessories to a lift pointer effect.

func pointerInteraction(_ interaction: UIPointerInteraction, styleFor region: UIPointerRegion) -> UIPointerStyle?
{
    let preview = UITargetedPreview(view: self)
    let style = UIPointerStyle(effect: .lift(preview))

    if #available(iOS 15.0, *) {
        style.accessories = [
            .arrow(.left),
            .arrow(.right)
        ]
    }

    return style
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10057/7/5399C1AB-B62F-4A83-8AA1-FCBFDAFFBF44/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10057/7/5399C1AB-B62F-4A83-8AA1-FCBFDAFFBF44/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10057) — developer.apple.com. Indexed for agent consumption._
