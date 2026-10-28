---
id: "tech-talks-111468"
event: "tech-talks"
year: 2026
title: "Bring Touch to your Mac app"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111468"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Bring Touch to your Mac app

**Event:** Tech Talks · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2026-10-28 · **Session:** [tech-talks-111468](https://developer.apple.com/videos/play/tech-talks/111468)

Discover how to add touch capabilities to your Mac app. Explore how to transition from classic mouse tracking APIs to modern gesture recognizers and touch-native controls. Find out how to optimize hit targets, implement multi-touch interactions, and manage system gestures to deliver an incredible touch experience. To get the most out of this session, watch Design for Touch on Mac.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,137 words)

## Code Snippets

### Custom button that overrides mouseDown — [2:08]

```swift
// Custom button to detect start and end of tracking
class IgnitionButton: NSButton {
    var delegate: IgnitionButtonDelegate?

    override func mouseDown(with event: NSEvent) {
        delegate?.buttonDidStartTracking()
        super.mouseDown(with: event)
        delegate?.buttonDidEndTracking()
    }
}
```

### Use NSControl events to detect tracking — [2:24]

```swift
// Use NSControl events to detect start and end of tracking
ignitionButton.addTarget(
    self,
    action: #selector(buttonDidStartTracking),
    for: [.trackingBegan, .trackingEntered]
)

ignitionButton.addTarget(
    self,
    action: #selector(buttonDidEndTracking),
    for: [.trackingExited, .trackingEndedInside]
)

ignitionButton.addTarget(
    self,
    action: #selector(buttonCancelledTracking),
    for: .trackingCancelled
)
```

### Mouse tracking loop — [3:13]

```swift
let eventMask: NSEvent.EventTypeMask = [.leftMouseDragged, .leftMouseUp]
while true {
    let nextEvent = NSApp.nextEvent(
        matching: eventMask,
        until: .distantFuture,
        inMode: .eventTracking,
        dequeue: true)
    if let nextEvent, nextEvent.type == .leftMouseUp {
        break
    }
}
```

### Refactored tracking functions — [4:11]

```swift
// Refactored tracking functions
func startTracking(at viewLocation: NSPoint) { /* ... */ }

func continueTracking(at viewLocation: NSPoint) { /* ... */ }

func endTracking(at viewLocation: NSPoint) { /* ... */ }

func cancelTracking() { /* ... */ }
```

### Add a touch-only pan gesture recognizer — [4:24]

```swift
// Add touch-only pan gesture recognizer
let touchRecognizer = NSPanGestureRecognizer(
    target: self,
    action: #selector(touchPan)
)

touchRecognizer.buttonMask = 0x0
touchRecognizer.allowedTouchTypes = .direct

wiringPanelView.addGestureRecognizer(touchRecognizer)
```

### Pan gesture recognizer action — [4:52]

```swift
// Pan gesture recognizer action function
@objc func touchPan(_ recognizer: NSPanGestureRecognizer) {
    switch recognizer.state {
    case .began:
        startTracking(at: recognizer.location(in: wiringPanelView))
    case .changed:
        continueTracking(at: recognizer.location(in: wiringPanelView))
    case .ended:
        endTracking(at: recognizer.location(in: wiringPanelView))
    case .cancelled:
        cancelTracking()
    default:
        break
    }
}
```

### Expand hit targets for touch — [5:37]

```swift
// Refactored tracking functions with expanded hit targets
func startTracking(at viewLocation: NSPoint, expandHitRect: Bool = false) {
    for node in nodes {
        if point(viewLocation, in: node.frame, expandForTouch: expandHitRect) {
            trackingNode = node
            trackingLocation = viewLocation
            return
        }
    }
}

func point(_ point: NSPoint, in rect: NSRect, expandForTouch: Bool = false) -> Bool {
    if expandForTouch {
        // Expand to minimum size of 36 points on each axis
    } else {
        // Nothing to do for mouse
    }
    return NSPointInRect(point, rect)
}

@objc func touchPan(_ recognizer: NSPanGestureRecognizer) {
    switch recognizer.state {
    case .began:
        startTracking(at: recognizer.location(in: wiringPanelView), expandHitRect: true)
    // ...
    default:
        break
    }
}
```

### Require two touches for scrolling — [6:40]

```swift
// Modify touch scrolling properties
decoratingView.enclosingScrollView?.minimumNumberOfTouchesForScrolling = 2
```

### Allow simultaneous slider interaction — [7:48]

```swift
// Simultaneous sliders
stoveControlsView.exclusiveGestureBehavior = .notExclusive
```

### Disable system gestures — [8:25]

```swift
// Disabling system gestures
stoveControlsView.window?.disablesDirectTouchSystemGestures = true

// Mac Catalyst API
extension UIViewController {
    var prefersDirectTouchSystemGesturesDisabled: Bool { get }
}

// SwiftUI API
View.directTouchSystemGesturesDisabled()
```

### Declare touch-native support in Info.plist — [11:47]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- ... -->
    <key>NSIsTouchNative</key>
    <true/>
    <!-- ... -->
</dict>
</plist>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111468/1/9a1f840e-293f-4007-a9a7-39544c36176c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111468/1/9a1f840e-293f-4007-a9a7-39544c36176c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111468) — developer.apple.com. Indexed for agent consumption._
