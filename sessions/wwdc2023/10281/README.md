---
id: "wwdc2023-10281"
event: "wwdc2023"
year: 2023
title: "Keep up with the keyboard"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10281"
topics: ["App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Keep up with the keyboard

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10281](https://developer.apple.com/videos/play/wwdc2023/10281)

Each year, the keyboard evolves to support an increasing range of languages, sizes, and features. Discover how you can design your app to keep up with the keyboard, regardless of how it appears on a device. We’ll show you how to create frictionless text entry and share important architectural changes to help you understand how the keyboard works within the system.

**Keywords:** `inline predictions`, `keyboard layout guide`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,717 words)

## Documentation & Resources

- [Adding a search interface to your app](https://developer.apple.com/documentation/SwiftUI/Adding-a-search-interface-to-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Adding-a-search-interface-to-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Adding-a-search-interface-to-your-app.json
- [FocusState](https://developer.apple.com/documentation/SwiftUI/FocusState) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/FocusState
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/FocusState.json
- [SafeAreaRegions](https://developer.apple.com/documentation/SwiftUI/SafeAreaRegions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/SafeAreaRegions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/SafeAreaRegions.json
- [Human Interface Guidelines: Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/keyboards
- [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide.json

## Code Snippets

### Keyboard layout guide — [6:21]

```swift
view.keyboardLayoutGuide.topAnchor.constraint(equalTo: textView.bottomAnchor).isActive = true
```

### usesBottomSafeArea — [7:56]

```swift
// Example of using usesBottomSafeArea to create keyboard and text view aligned with safe area

view.keyboardLayoutGuide.usesBottomSafeArea = false

textField.topAnchor.constraint(equalToSystemSpacingBelow: backdrop.topAnchor, multiplier: 1.0).isActive = true

view.keyboardLayoutGuide.topAnchor.constraint(greaterThanOrEqualToSystemSpacingBelow: textField.bottomAnchor, multiplier: 1.0).isActive = true

view.keyboardLayoutGuide.topAnchor.constraint(equalTo: backdrop.bottomAnchor).isActive = true

view.safeAreaLayoutGuide.bottomAnchor.constraint(greaterThanOrEqualTo: textField.bottomAnchor).isActive = true
```

### Keyboard dismiss padding — [9:40]

```swift
var dismissPadding = aboveKeyboardView.bounds.size.height

view.keyboardLayoutGuide.keyboardDismissPadding = dismissPadding
```

### Handle willShow or hideKeyboard notifications — [12:11]

```swift
func handleWillShowOrHideKeyboardNotification(notification: NSNotification) {
    // Retrieve the UIScreen object from the notification (Added iOS 16.1)
    guard let screen = notification.object as? UIScreen else { return }

    // Determine if the notification’s screen corresponds to your view’s screen
    guard(screen.isEqual(view.window?.screen)) else { return }

    // Calculate intersection with keyboard
    let endFrameKey = UIResponder.keyboardFrameEndUserInfoKey

    // Get the ending screen position of the keyboard
    guard let keyboardFrameEnd = userInfo[endFrameKey] as? CGRect else { return }

    let fromCoordinateSpace: UICoordinateSpace = screen.coordinateSpace
    let toCoordinateSpace: UICoordinateSpace = view

    // Convert from the screen coordinate space to your local coordinate space
    let convertedKeyboardFrameEnd = fromCoordinateSpace.convert(keyboardFrameEnd, to: toCoordinateSpace)

    // Calculate offset for view adjustment
    var bottomOffset = view.safeAreaInsets.bottom

    // Get the intersection between the keyboard's frame and the view's bounds
    let viewIntersection = view.bounds.intersection(convertedKeyboardFrameEnd)

    // Check whether the keyboard intersects your view before adjusting your offset.
    if !viewIntersection.isEmpty {
        // Set the offset to the height of the intersection
        bottomOffset = viewIntersection.size.height
    }

    // Use the new offset to adjust your UI
    movingBottomConstraint.constant = bottomOffset

    // Adjust view layouts and animate using information in notification

    ...

}
```

### Inline predictions — [14:38]

```swift
@MainActor public protocol UITextInputTraits : NSObjectProtocol {
    // Controls whether inline text prediction is enabled or disabled during typing
    @available(iOS, introduced: 17.0)
    optional var inlinePredictionType: UITextInlinePredictionType { get set }
}

public enum UITextInlinePredictionType : Int, @unchecked Sendable {
    case `default` = 0
    case no = 1
    case yes = 2
}

let textView = UITextView(frame: frame)
textView.inlinePredictionType = .yes
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10281/5/28D03695-D3A4-41FB-9F95-B97A11BF249B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10281/5/28D03695-D3A4-41FB-9F95-B97A11BF249B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10281) — developer.apple.com. Indexed for agent consumption._