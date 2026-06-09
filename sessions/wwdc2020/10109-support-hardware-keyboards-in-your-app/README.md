---
id: "wwdc2020-10109"
event: "wwdc2020"
year: 2020
title: "Support hardware keyboards in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10109"
topics: ["SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Support hardware keyboards in your app

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10109](https://developer.apple.com/videos/play/wwdc2020/10109)

When people use hardware keyboards with your app, they’re not only getting a more tactile and familiar typing experience — they can quickly navigate or use keyboard shortcuts, too. Discover how you can best support hardware keyboards for your iPadOS and Mac Catalyst apps: We’ll demystify the responder chain and show you best practices for implementing custom keyboard shortcuts. Learn how easy it is to get up and running with common system keyboard shortcuts, use modifier flags with gesture recognizers, and leverage the raw keyboard event API to respond to key down and key up events.

**Keywords:** `accelerators`, `event`, `magic keyboard`, `menu`, `shortcuts`, `text`, `uieventtype`, `uitextinput`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,923 words)

## Documentation & Resources

- [Adding hardware keyboard support to your app](https://developer.apple.com/documentation/UIKit/adding-hardware-keyboard-support-to-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-hardware-keyboard-support-to-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-hardware-keyboard-support-to-your-app.json
- [UIResponderStandardEditActions](https://developer.apple.com/documentation/UIKit/UIResponderStandardEditActions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIResponderStandardEditActions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIResponderStandardEditActions.json

## Code Snippets

### PlayerViewController — [0:01]

```swift
class PlayerViewController: UIViewController {

    override var canBecomeFirstResponder: Bool {
        return true 
    }

    override func viewDidAppear(_ animated: Bool) {
        becomeFirstResponder()
    }

    override var keyCommands: [UIKeyCommand]? {
        return [
            UIKeyCommand(title: NSLocalizedString("PLAY_PAUSE", comment: "…"),
                        action: #selector(playPause),
                         input: " ")
        ]
    }
}
```

### SongListTableViewController — [0:02]

```swift
class SongListTableViewController: UITableViewController {

    override var canBecomeFirstResponder: Bool {
        return true
    }

    override func viewDidAppear(_ animated: Bool) {
        becomeFirstResponder()
    }

    /* UIResponderStandardEditActions */

    override func selectAll(_ sender: Any?) { … }

    override func copy(_ sender: Any?) { … }

    override func paste(_ sender: Any?) { … }

}
```

### UIKeyCommand — [0:03]

```swift
class UIKeyCommand : UICommand {
    ...
}

override func buildMenu(with builder: UIMenuBuilder) {
    builder.replaceChildren(ofMenu: .file) { children in
        return [ UIKeyCommand() ] + children
    }
}
```

### Extending selection with keyboard — [0:04]

```swift
optional func tableView(_ tableView: UITableView,
       shouldBeginMultipleSelectionInteractionAt indexPath: IndexPath) -> Bool

optional func tableView(_ tableView: UITableView,
       didBeginMultipleSelectionInteractionAt indexPath: IndexPath)
```

### recognizedDragGesture — [0:05]

```swift
func recognizedDragGesture(_ panGesture: UIPanGestureRecognizer) {

    if panGesture.modifierFlags.contains(.command) {
        snapToGrid = true
    } else if panGesture.modifierFlags.contains(.shift) {
        constrainAspectRatio = true
    }

    ...
}
```

### Responding to raw keyboard events — [0:06]

```swift
class UIResponder: NSObject {
    func pressesBegan(_ presses: Set<UIPress>,
                     with event: UIPressesEvent)

    func pressesEnded(_ presses: Set<UIPress>,
                     with event: UIPressesEvent)
}
```

### CanvasViewController — [0:07]

```swift
class CanvasViewController: UIViewController {

     override func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
         for press in presses {
             guard let key = press.key else { continue }
             switch key.keyCode {
             case .keyboardUpArrow: startMoveUp()
             case .keyboardDownArrow: startMoveDown()
                 …
             }
     }
     }

     override func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
         stopMoving()
     }

}
```

### CanvasViewController modifier flags — [0:08]

```swift
class CanvasViewController: UIViewController {

    override func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
        var selectWhileMoving = false
        for press in presses {
            guard let key = press.key else { continue }
            if key.modifierFlags.contains(.shift) {
                selectWhileMoving = true
            }

            switch key.keyCode {
            case .keyboardUpArrow: startMoveUp()

            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10109/2/B152D3FD-187C-4D34-80ED-152B996E5F6D/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10109) — developer.apple.com. Indexed for agent consumption._
