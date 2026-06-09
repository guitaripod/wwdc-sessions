---
id: "wwdc2021-10260"
event: "wwdc2021"
year: 2021
title: "Focus on iPad keyboard navigation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10260"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Focus on iPad keyboard navigation

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10260](https://developer.apple.com/videos/play/wwdc2021/10260)

Improve the keyboard experience in your iPad and Mac Catalyst app. Discover how you can accelerate access to key features with the hardware keyboard, and navigate through your views and view controllers. Learn how to customize which elements are keyboard navigable, as well as how to customize the tab loop.

**Keywords:** `commands`, `environment`, `focus`, `groups`, `ipad`, `item`, `key`, `keyboard`, `navigation`, `productivity`, `sidebar.`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,999 words)

## Documentation & Resources

- [Navigating an app’s user interface using a keyboard](https://developer.apple.com/documentation/UIKit/navigating-an-app-s-user-interface-using-a-keyboard) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/navigating-an-app-s-user-interface-using-a-keyboard
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/navigating-an-app-s-user-interface-using-a-keyboard.json
- [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide.json
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/UIKit/about-focus-interactions-for-apple-tv) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/about-focus-interactions-for-apple-tv
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/about-focus-interactions-for-apple-tv.json
- [Adding hardware keyboard support to your app](https://developer.apple.com/documentation/UIKit/adding-hardware-keyboard-support-to-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-hardware-keyboard-support-to-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-hardware-keyboard-support-to-your-app.json
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.json
- [Implementing Advanced Text Input Features](https://developer.apple.com/sample-code/wwdc/2017/Implementing-Advanced-Text-Input-Features.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/wwdc/2017/Implementing-Advanced-Text-Input-Features.zip
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### canBecomeFocused — [3:01]

```swift
override var canBecomeFocused: Bool { true }
```

### allowsFocus — [4:00]

```swift
class MyViewController: UICollectionViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        self.collectionView.allowsFocus = true
    }
}
```

### canFocusItemAtIndexPath — [4:23]

```swift
class MyCollectionViewDelegate: NSObject, UICollectionViewDelegate {
    func collectionView(_ collectionView: UICollectionView,
                canFocusItemAt indexPath: IndexPath) -> Bool {
        return true
    }
}
```

### UIFocusDebugger checkFocusability(for:) — [4:40]

```bash
po UIFocusDebugger.checkFocusability(for:)
```

### UIFocusHaloEffect — [5:48]

```swift
let focusEffect = UIFocusHaloEffect(roundedRect: self.bounds, cornerRadius: self.layer.cornerRadius, curve: .continuous)
self.focusEffect = focusEffect
```

### ReferenceView and ContainerView — [6:03]

```swift
let focusEffect = UIFocusHaloEffect(roundedRect: self.bounds, cornerRadius: self.layer.cornerRadius, curve: .continuous)

// make sure the effect is added right above the image view
focusEffect.referenceView = self.imageView

// make sure the effect is added to our scroll view
focusEffect.containerView = self.scrollView

self.focusEffect = focusEffect
```

### Custom focus effects — [7:43]

```swift
init(frame: CGRect) {
   super.init(frame: frame)
   self.focusEffect = nil
}

func didUpdateFocus(in context: UIFocusUpdateContext, withAnimationCoordinator coordinator: UIFocusAnimationCoordinator) {
    if context.nextFocusedItem == self {
        // This view is focused. Customize its appearance.
    }
    else if context.previouslyFocusedItem == self {
        // This view was focused.
    }
}
```

### Selection Follows Focus — [9:08]

```swift
var selectionFollowsFocus: Bool
```

### Selection Follows Focus for Item at Index Path — [9:16]

```swift
func collectionView(_ collectionView: UICollectionView, selectionFollowsFocusForItemAt indexPath: IndexPath) -> Bool {
    return self.action(for: indexPath).type != .showAlert
}
```

### Focus Group Identifier — [12:12]

```swift
self.focusGroupIdentifier = "com.myapp.groups.sidebar"
```

### UIFocusGroupPriority — [12:52]

```swift
extension UIFocusGroupPriority {
    public static let ignored: UIFocusGroupPriority // 0
    public static let previouslyFocused: UIFocusGroupPriority // 1000
    public static let prioritized: UIFocusGroupPriority // 2000
    public static let currentlyFocused: UIFocusGroupPriority // NSIntegerMax
}
```

### Focus Group Priority on a cell — [13:40]

```swift
// Customizing an item’s focus group priority

func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    let cell = ...
    if self.isCallToActionCell(at: indexPath) {
        // This cell is not as important as a selected cell but should
        // be chosen over the last focused cell in this group.
        cell.focusGroupPriority = .previouslyFocused + 10
    }
    return cell
}
```

### UIFocusDebugger checkFocusGroupTree(for:) — [15:46]

```bash
po UIFocusDebugger.checkFocusGroupTree(for:)
```

### wantsPriorityOverSystemBehavior — [19:16]

```swift
keyCommand.wantsPriorityOverSystemBehavior = true
```

### pressesBegan — [19:36]

```swift
override func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
    if (/* check presses of interest */) {
        // handle the press
    }
    else {
        super.pressesBegan(presses, with: event)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10260/4/E0BC9390-870B-4D59-9A0C-74941EAF4E36/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10260/4/E0BC9390-870B-4D59-9A0C-74941EAF4E36/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10260) — developer.apple.com. Indexed for agent consumption._