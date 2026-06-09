---
id: "wwdc2021-10259"
event: "wwdc2021"
year: 2021
title: "Your guide to keyboard layout"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10259"
topics: ["Accessibility & Inclusion", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Your guide to keyboard layout

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10259](https://developer.apple.com/videos/play/wwdc2021/10259)

Discover how you can use the Keyboard Layout Guide to manage how keyboards work within your iOS or iPadOS app. Learn how you can avoid writing lengthy code blocks when you use UIKeyboardLayoutGuide and UITrackingLayoutGuide to integrate the keyboard into your interface, helping people have a smoother, more enjoyable experience whenever they use the on-screen keyboard within your app. To get the most out of this session, we recommend familiarity with both Auto Layout and UILayoutGuide.

**Keywords:** `🎹`, `⌨️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,692 words)

## Documentation & Resources

- [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide.json

## Code Snippets

### Using notifications with a custom layout guide — [1:31]

```swift
...
    keyboardGuide.bottomAnchor.constraint(equalTo: view.bottomAnchor).isActive = true
    keyboardGuide.topAnchor.constraint(equalTo: textView.bottomAnchor).isActive = true
    keyboardHeight = keyboardGuide.heightAnchor.constraint(equalToConstant: view.safeAreaInsets.bottom)

    NotificationCenter.default.addObserver(self, selector: #selector(respondToKeyboard), 
                                                     name: UIResponder.keyboardWillShowNotification, 
                                                   object: nil)
}

@objc func respondToKeyboard(notification: Notification) {
    let info = notification.userInfo
    if let endRect = info?[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect {
        var offset = view.bounds.size.height - endRect.origin.y
        if offset == 0.0 {
            offset = view.safeAreaInsets.bottom
        }
        let duration = info?[UIResponder.keyboardAnimationDurationUserInfoKey] as? TimeInterval ?? 2.0
        UIView.animate(withDuration: duration, animations: {
            self.keyboardHeight.constant = offset
            self.view.layoutIfNeeded()
        })
    }
}
```

### Transitioning to keyboardLayoutGuide — [3:09]

```swift
view.keyboardLayoutGuide.topAnchor.constraint(equalToSystemSpacingBelow: textView.bottomAnchor, multiplier: 1.0).isActive = true
```

### Vertical positioning — [6:46]

```swift
let awayFromTopConstraints = [
    view.keyboardLayoutGuide.topAnchor.constraint(equalTo: editView.bottomAnchor),
]
view.keyboardLayoutGuide.setConstraints(awayFromTopConstraints, activeWhenAwayFrom: .top)

let nearTopConstraints = [
    view.safeAreaLayoutGuide.bottomAnchor.constraint(equalTo: editView.bottomAnchor),

]
view.keyboardLayoutGuide.setConstraints(nearTopConstraints, activeWhenNearEdge: .top)
```

### Horizontal positioning — [7:44]

```swift
let awayFromSides = [
    view.keyboardLayoutGuide.centerXAnchor.constraint(equalTo: editView.centerXAnchor),
    imageView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
]
view.keyboardLayoutGuide.setConstraints(awayFromSides, activeWhenAwayFrom: [.leading, .trailing])


let nearTrailingConstraints = [
    view.keyboardLayoutGuide.trailingAnchor.constraint(equalTo: editView.trailingAnchor),
    imageView.leadingAnchor.constraint(
        equalToSystemSpacingAfter: view.safeAreaLayoutGuide.leadingAnchor, multiplier: 1.0)
]
view.keyboardLayoutGuide.setConstraints(nearTrailingConstraints, activeWhenNearEdge: .trailing)

let nearLeadingConstraints = [
    editView.leadingAnchor.constraint(equalTo: view.keyboardLayoutGuide.leadingAnchor),
    view.safeAreaLayoutGuide.trailingAnchor.constraint(
        equalToSystemSpacingAfter: imageView.trailingAnchor, multiplier: 1.0)
]
view.keyboardLayoutGuide.setConstraints(nearLeadingConstraints, activeWhenNearEdge: .leading)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10259/4/F6B7B6EB-8577-4034-9EE3-67BADA64041D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10259/4/F6B7B6EB-8577-4034-9EE3-67BADA64041D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10259) — developer.apple.com. Indexed for agent consumption._
