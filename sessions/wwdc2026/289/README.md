---
id: "wwdc2026-289"
event: "wwdc2026"
year: 2026
title: "Modernize your AppKit app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/289"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Modernize your AppKit app

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-289](https://developer.apple.com/videos/play/wwdc2026/289)

Bring your AppKit app up to date with modern macOS conventions. Dive into handling input with control events and gesture recognizers, moving beyond traditional tracking loops. Enhance keyboard navigation in your app, implement graceful state restoration after restarts, and take advantage of new corner concentricity APIs that let your interface blend seamlessly with the macOS aesthetic.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,486 words)

## Documentation & Resources

- [Use SwiftUI with AppKit](https://developer.apple.com/videos/play/wwdc2022/10075/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/videos/play/wwdc2022/10075/
- [Restoring your app’s state with AppKit](https://developer.apple.com/documentation/AppKit/restoring-your-app-s-state-with-appkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/restoring-your-app-s-state-with-appkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/restoring-your-app-s-state-with-appkit.json
- [Gestures](https://developer.apple.com/documentation/AppKit/gestures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/gestures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/gestures.json
- [TN3212: Adopting gesture recognizers for Sidecar touch support](https://developer.apple.com/documentation/Technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.json
- [NSControl.Events](https://developer.apple.com/documentation/AppKit/NSControl/Events) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/NSControl/Events
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/NSControl/Events.json

## Code Snippets

### Modern dragging delegate — [3:35]

```swift
// Modern dragging delegate methods
func tableView(_ tableView: NSTableView,
        pasteboardWriterForRow row: Int) -> (any NSPasteboardWriting)? {
    let pasteboardItem = NSPasteboardItem()
    pasteboardItem.setString(..., forType: .string)
    return pasteboardItem
}
```

### Control events — [4:55]

```swift
// Use control events
let button = NSButton()
button.addTarget(
    self,
    action: #selector(trackingEndedOutsideHandler),
    for: .trackingEndedOutside
)
```

### hitTest override — [5:44]

```swift
override func hitTest(_ point: NSPoint) -> NSView? {
    return nil
}
```

### autorecalculatesKeyViewLoop — [6:24]

```swift
window.autorecalculatesKeyViewLoop = true
```

### Expanded interface delegate — setup — [7:37]

```swift
// Set the expanded interface delegate
@main class LightAppDelegate: NSObject, NSApplicationDelegate {
    lazy var lightStatusItem: NSStatusItem = { ... }()

    func applicationDidFinishLaunching(_ notification: Notification) {
        // ...
        lightStatusItem.expandedInterfaceDelegate = self
    }
}
```

### Expanded interface delegate — methods — [7:52]

```swift
// Implement the delegate methods
extension LightAppDelegate: NSStatusItemExpandedInterfaceDelegate {
    // ...
    func statusItem(_ statusItem: NSStatusItem, didBegin session:
                    NSStatusItemExpandedInterfaceSession) {
        // Show window
    }
    func statusItemDidEndExpandedInterfaceSession(
        _ statusItem: NSStatusItem, animated: Bool) {
        // Hide window
    }
    func selectedAction() {
        // Take the action
        // Cancel session to request window dismissal
        lightStatusItem.expandedInterfaceSession?.cancel()
    }
}
```

### Expanded interface delegate — cancel — [8:16]

```swift
// Cancel the session when dismissing
extension LightAppDelegate: NSStatusItemExpandedInterfaceDelegate {
    // ...
    func statusItem(_ statusItem: NSStatusItem, didBegin session:
                    NSStatusItemExpandedInterfaceSession) {
        // Show window
    }
    func statusItemDidEndExpandedInterfaceSession(
        _ statusItem: NSStatusItem, animated: Bool) {
        // Hide window
    }
    func selectedAction() {
        // Take the action
        // Cancel session to request window dismissal
        lightStatusItem.expandedInterfaceSession?.cancel()
    }
}
```

### preventsApplicationTerminationWhenModal — [9:45]

```swift
window.preventsApplicationTerminationWhenModal = false
```

### Set window identifiers for state restoration — [10:18]

```swift
// Set window identifiers for state restoration
@MainActor class MainWindowController: NSWindowController, NSWindowDelegate {
    // ...
    convenience init() {
        let window = NSWindow( ... )
        // ...
        window.identifier = NSUserInterfaceItemIdentifier(WindowIdentifiers.mainWindow)
        window.setFrameAutosaveName(WindowIdentifiers.mainWindow)
        window.isRestorable = true
        window.restorationClass = WindowRestorationHandler.self
        // ...
    }
}
```

### encodeRestorableState — [11:04]

```swift
// Preserve state to recreate the UI
@MainActor class MainWindowController: NSWindowController, NSWindowDelegate {
    // ...
    override func encodeRestorableState(with coder: NSCoder) {
        super.encodeRestorableState(with: coder)
        // ...
        coder.encode(selectedProduct?.identifier.uuid,
                    forKey: RestorationKeys.productIdentifier)
        // ...
    }
    // ...
}
```

### invalidateRestorableState — [11:50]

```swift
// Invalidate restorable state when the view hierarchy changes
@MainActor class MainWindowController: NSWindowController, NSWindowDelegate {
    // ...
    convenience init() {
        // ...
        splitViewController.onProductSelected = { [weak self] product in
            self?.invalidateRestorableState()
        }
    }
}
```

### restoreWindow(withIdentifier:) — [12:26]

```swift
// Restore windows
class WindowRestorationHandler: NSObject, NSWindowRestoration {
    static func restoreWindow(
        withIdentifier identifier: NSUserInterfaceItemIdentifier,
        state: NSCoder,
        completionHandler: @escaping (NSWindow?, Error?) -> Void
    ) {
        //...
        if identifier == .mainWindow, let window = appDelegate.mainWindowController?.window {
            completionHandler(window, nil)
        } else if identifier == .imageWindow {
            let controller = ImageWindowController()
            appDelegate.imageWindowControllers.append(controller)
            completionHandler(controller.window, nil)
        } else {
            completionHandler(nil, error)
        }
    }
}
```

### restoreState — [13:29]

```swift
// Restore window UI
@MainActor class MainWindowController: NSWindowController, NSWindowDelegate {
    //...
    override func restoreState(with coder: NSCoder) {
        super.restoreState(with: coder)
        if let productId = coder.decodeObject(
            of: [NSString.self],
            forKey: RestorationKeys.productIdentifier) as? String {
            splitViewController?.selectedProductId = productId
        }
        //...
    }
}
```

### cornerConfiguration — [16:11]

```swift
// Subclass NSView to override cornerConfiguration
class LocalWeatherView: NSView {
    // ...
    override var cornerConfiguration: NSViewCornerConfiguration? {
        let radius: NSViewCornerRadius = .containerConcentric(minimumCornerRadius)
        return .uniformCorners(radius: radius)
    }
    // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/289/5/6a2a7cfa-56a1-4cbb-ae54-1f229e1708ae/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/289/5/6a2a7cfa-56a1-4cbb-ae54-1f229e1708ae/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/289) — developer.apple.com. Indexed for agent consumption._