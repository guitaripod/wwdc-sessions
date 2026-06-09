---
id: "wwdc2021-10064"
event: "wwdc2021"
year: 2021
title: "Meet the UIKit button system"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10064"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet the UIKit button system

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10064](https://developer.apple.com/videos/play/wwdc2021/10064)

Every app uses Buttons. With iOS 15, you can adopt updated styles to create gorgeous buttons that fit effortlessly into your interface. We'll explore features that make it easier to create different types of buttons, learn how to provide richer interactions, and discover how you can get great buttons when using Mac Catalyst.

**Keywords:** `catalyst`, `menu`, `popdown`, `pop-down`, `popup`, `pop-up`, `switch`, `toggle`, `uibutton`, `uibuttonconfiguration`, `uimenu`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,665 words)

## Documentation & Resources

- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Creating a button with a configuration — [2:13]

```swift
// Create the Sign In button

let signInButton = UIButton(type: .system)
signInButton.configuration = .filled()
signInButton.setTitle("Sign In", for: [])
```

### Customizing a button configuration — [3:20]

```swift
// Create the Add to Cart button

var config = UIButton.Configuration.tinted()
config.title = "Add to Cart"
config.image = UIImage(systemName: "cart.badge.plus")
config.imagePlacement = .trailing
addToCartButton = UIButton(configuration: config,
                           primaryAction: …)
```

### Customizing a button with a configuration update handler — [4:45]

```swift
// Customize image and subtitle with a configurationUpdateHandler

addToCartButton.configurationUpdateHandler = {
    [unowned self] button in

    var config = button.configuration
    config?.image = button.isHighlighted
        ? UIImage(systemName: "cart.fill.badge.plus")
        : UIImage(systemName: "cart.badge.plus")
    config?.subtitle = self.itemQuantityDescription
    button.configuration = config
}
```

### Indicating a configuration needs an update — [5:59]

```swift
// Update addToCartButton when itemQuantityDescription changes

private var itemQuantityDescription: String? {
    didSet {
        addToCartButton.setNeedsUpdateConfiguration()
    }
}
```

### A completely customized button — [8:26]

```swift
// Configure the button background

var config = UIButton.Configuration.filled()
config.buttonSize = .large
config.image = UIImage(systemName: "cart.fill")
config.title = "Checkout"
config.background.backgroundColor = .buttonEmporium

let checkoutButton = UIButton(configuration: config
                              primaryAction: …) 
addToCartButton.configurationUpdateHandler = {
    [unowned self] button in

    var config = button.configuration
    config?.showsActivityIndicator = self.isCartBusy
    button.configuration = config
}
```

### Creating a toggle button — [11:56]

```swift
// Toggle button

// UIAction setup
let stockToggleAction = UIAction(title: "In Stock Only") { _ in
    toggleStock()
}

// The button
let button = UIButton(primaryAction: stockToggleAction)

button.changesSelectionAsPrimaryAction = true

// Initial state
button.isSelected = showingOnlyInStock()
```

### Creating a pop-up button — [14:30]

```swift
// Pop-up button

let colorClosure = { (action: UIAction) in
    updateColor(action.title)
}

let button = UIButton(primaryAction: nil)

button.menu = UIMenu(children: [
    UIAction(title: "Bondi Blue", handler: colorClosure),
    UIAction(title: "Flower Power", state: .on, handler: colorClosure)
])

button.showsMenuAsPrimaryAction = true

button.changesSelectionAsPrimaryAction = true

// Update to the currently set one
updateColor(button.menu?.selectedElements.first?.title)

// Update the selection
(button.menu?.children[selectedColorIndex()] as? UIAction)?.state = .on
```

### Creating a custom single selection menu — [18:18]

```swift
// Single selection menu

// The sort menu
let sortMenu = UIMenu(title: "Sort By", options: .singleSelection, children: [
    UIAction(title: "Title", handler: sortClosure),
    UIAction(title: "Date", handler: sortClosure),
    UIAction(title: "Size", handler: sortClosure)
])

// The top menu
let topMenu = UIMenu(children: [
    UIAction(title: "Refresh", handler: refreshClosure),
    UIAction(title: "Account", handler: accountClosure),
    sortMenu
])

let sortSelectionButton = UIBarButtonItem(primaryAction: nil, menu: topMenu)

updateSorting(sortSelectionButton.menu?.selectedElements.first)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10064/3/5DF3D536-453F-4C11-9BD5-9334BD79D560/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10064/3/5DF3D536-453F-4C11-9BD5-9334BD79D560/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10064) — developer.apple.com. Indexed for agent consumption._
