---
id: "wwdc2021-10120"
event: "wwdc2021"
year: 2021
title: "Support Full Keyboard Access in your iOS app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10120"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Support Full Keyboard Access in your iOS app

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10120](https://developer.apple.com/videos/play/wwdc2021/10120)

iPhone and iPad support numerous input modes for those with motor impairments, including touch interaction modification, Switch Control, and Full Keyboard Access. We’ll explore how people can interact with their devices solely through keyboard input, working through a real-life example to discover key APIs. We’ll also take you through some best practices for supporting motor accessibility when you integrate Full Keyboard Access in your apps.

**Keywords:** `accessibility element`, `accessibilitylabel`, `accessibility label`, `accessibility path`, `accessibiltypath`, `accessible input`, `alternative input`, `assistive technology`, `assistivetouch`, `custom action`, `custom keyboard shortcut`, `focus`, `focus engine`, `full keyboard access`, `gestures`, `interaction commands`, `interaction via keyboard`, `isaccessibilityelement`, `keyboard`, `keyboard as input`, `keyboard shortcut`, `motor accessibility`, `motor impairment`, `navigation commands`, `switch control`, `tab z`, `uiaccessibility`, `uiaccessibilitycustomaction`, `uikeycommand`, `uimenu`, `user input label`, `voice control`, `voice over`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,598 words)

## Documentation & Resources

- [Accessibility for Developers](https://developer.apple.com/accessibility/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/accessibility/

## Code Snippets

### Accessibility custom actions — [7:06]

```swift
// Accessibility custom actions

let addAction = UIAccessibilityCustomAction(
    name: gameLocString("add"), image: UIImage(systemName: "plus.square")) { _ in
            self.addCard()
            return true
        }

let pinAction = UIAccessibilityCustomAction(
    name: gameLocString("pin"), image: UIImage(systemName: "pin.fill")) { _ in
            self.pinCard()
            return true
        }

cardView.accessibilityCustomActions = [addAction, pinAction]
```

### Keyboard shortcuts: buildMenu — [8:39]

```swift
// Keyboard shortcuts

// In AppDelegate.swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    guard builder.system == .main else {
        return
    }

    let pinCommand = UIKeyCommand(title: gameLocString("pin"), image: UIImage(systemName:
        "pin.fill"), action:#selector(GameViewController.pinFocusedCard), input: "P",
        discoverabilityTitle:gameLocString("pin.card"))      
    let addCommand = UIKeyCommand(title: gameLocString("add"), image: UIImage(systemName: 
        "plus.square"), action: #selector(GameViewController.addFocusedCard), input: "A",
        discoverabilityTitle: gameLocString("add.card"))
    let identifier = UIMenu.Identifier("gameplay_menu")
    let menu = UIMenu.init(title: gameLocString("gameplay"), image:  UIImage(systemName
        "rectangle.grid.3x2"), identifier: identifier, children: [addCommand, pinCommand]);

    builder.insertSibling(menu, afterMenu: .view)
}
```

### Keyboard shortcuts: canPerformAction — [9:22]

```swift
// Keyboard shortcuts

// In GameViewController.swift
override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
    if action == #selector(addFocusedCard) || action == #selector(pinFocusedCard) {
        return self.focusedCard != .none
    }
    return super.canPerformAction(action, withSender: sender)
}
```

### Accessibility elements — [10:35]

```swift
itemView.isAccessibilityElement = true
itemView.accessibilityLabel = gameLocString(for: item)
```

### Responding to user interaction — [11:01]

```swift
itemView.accessibilityRespondsToUserInteraction = false
```

### Supporting accessible input — [13:41]

```swift
self.accessibilityUserInputLabels = [
gameLocString("settings"),
gameLocString("prefs"),
gameLocString("preferences"),
gameLocString("gear")];
```

### Accessibility path — [14:52]

```swift
// Accessibility path

let rect = circleLevelButton.convert(levelButton.bounds, to: nil)

circleLevelButton.accessibilityPath = UIBezierPath(ovalIn: rect)


// If your button is in a scroll view, it’s generally better to
// override accessibilityPath and/or accessibilityFrame
extension CircleButton {
    open override var accessibilityPath: UIBezierPath? {
        get {
            let rect = self.convert(self.bounds, to: nil)
            return UIBezierPath(ovalIn: rect)
        }
        set {
            // no-op
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10120/11/284E99F6-0E62-4027-AE02-86A26EEBEC07/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10120/11/284E99F6-0E62-4027-AE02-86A26EEBEC07/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10120) — developer.apple.com. Indexed for agent consumption._