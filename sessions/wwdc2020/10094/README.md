---
id: "wwdc2020-10094"
event: "wwdc2020"
year: 2020
title: "Handle trackpad and mouse input"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10094"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Handle trackpad and mouse input

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10094](https://developer.apple.com/videos/play/wwdc2020/10094)

Provide a more versatile experience when you optimize your iPad or Mac Catalyst app for indirect input from trackpads and mice. Discover how to make your app responsive to new events from these devices. Learn how to work with pointer movement, enable pointer locking, handle scroll input and trackpad gestures, and accept or reject events on your gesture recognizers. We’ll also show you how to implement advanced features like changing gesture behaviors with keyboard modifiers or pointing device buttons to delight pro users and bring a richer experience to your app.

To learn more about pointer-based interactions and to get the most out of this session, we recommend watching “Build for the iPadOS pointer,” “Bring keyboard and mouse gaming to iPad,” and “Support hardware keyboards in your app.”

**Keywords:** `catalyst`, `event`, `magic keyboard`, `mouse`, `trackpad`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,238 words)

## Code Snippets

### UIHoverGestureRecognizer — [1:49]

```swift
let controlsHover = UIHoverGestureRecognizer(target: self, action: #selector(handleHover))

@objc func handleHover(_ recognizer: UIHoverGestureRecognizer) {
    switch recognizer.state {
    case .began:
        // Pointer entered our view - show controls
        self.showsPlaybackControls = true
    case .ended:
        // Pointer exited our view - hide controls
        self.showsPlaybackControls = false
    default:
        break
    }
}
```

### prefersPointerLocked — [5:33]

```swift
class GameViewController: UIViewController {

    var shouldLockPointer: Bool = true

    override var prefersPointerLocked: Bool {
        return self.shouldLockPointer
    }

    func disablePointerLock() {
        self.shouldLockPointer = false
        self.setNeedsUpdateOfPrefersPointerLocked()
    }
}
```

### UIPointerLockState.isLocked — [5:53]

```swift
if let pointerLockState = self.window.windowScene?.pointerLockState {
    self.observer = notificationCenter.addObserver(forName: UIPointerLockState.didChangeNotification,
                                                   object: pointerLockState,
                                                   queue: OperationQueue.main) { (note) in
        guard let lockState = note.object as? UIPointerLockState else { return }
        gameEngine.performExpensiveOperationWhile(lockState.isLocked)
    }
}
```

### UIPanGestureRecognizer.allowedScrollTypesMask — [9:54]

```swift
// Enable scroll input for touch surface devices

self.drawerPan.allowedScrollTypesMask = [.continuous]


// Enable scroll input for scroll wheel devices as well

self.pullToRefreshPan.allowedScrollTypesMask = [.all]
```

### Requiring a 3rd mouse button click — [14:48]

```swift
self.thirdMouseButtonTap.buttonMaskRequired = .button(3)
```

### Changing response for .alternate keyboard modifier — [15:07]

```swift
func handleHover(_ recognizer: UIHoverGestureRecognizer) {

    // Show chapter controls if alt is pressed
    let showChapterControls = recognizer.modifierFlags.contains(.alternate)

    // ...
}
```

### Only handle secondary clicks — [16:38]

```swift
class SecondaryClickGesture: UIGestureRecognizer {

    override func shouldReceive(_ event: UIEvent) -> Bool {
        // Must look at the event’s mask, not the gesture’s 
        return event.buttonMask == .secondary
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent) {
        // Touch handling code ...
    }
}
```

### Only handle secondary clicks or control clicks — [17:36]

```swift
class SecondaryClickGesture: UIGestureRecognizer {

    override func shouldReceive(_ event: UIEvent) -> Bool {
        // Must look at the event’s properties, not the gesture’s
        let secondaryClick = event.buttonMask == .secondary

        let controlClick = event.buttonMask == .primary && event.modifierFlags == .control 

        return secondaryClick || controlClick
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent) {
        // Touch handling code ...
    }
}
```

### Only receive hover events with the .alternate modifier pressed — [18:10]

```swift
let ccHover = UIHoverGestureRecognizer(target: self, 
                                       action: #selector(handleClosedCaptionHover))

ccHover.delegate = self

func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
                       shouldReceive event: UIEvent) -> Bool {

    if gestureRecognizer == self.closedCaptionHover {
        return event.modifierFlags.contains(.alternate)
    }

    return true
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10094/3/856B2AFB-E481-490E-A7AC-9446F47C0CFA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10094) — developer.apple.com. Indexed for agent consumption._