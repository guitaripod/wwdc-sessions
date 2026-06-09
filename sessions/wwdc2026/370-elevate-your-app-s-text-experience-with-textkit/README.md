---
id: "wwdc2026-370"
event: "wwdc2026"
year: 2026
title: "Elevate your app’s text experience with TextKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/370"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Elevate your app’s text experience with TextKit

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-370](https://developer.apple.com/videos/play/wwdc2026/370)

Discover how to combine the convenience of built-in text views with the control of TextKit. We’ll show you how new APIs make it easy to extend UITextView and NSTextView with custom behaviors like line numbers and collapsible sections. We’ll also explore the TextKit architecture and walk through new caching and reuse policies for text attachments. To get the most out of this session, watch “Meet TextKit 2” from WWDC21 and “What’s New in TextKit and text views” from WWDC22.

**Keywords:** `screenshots`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,189 words)

## Documentation & Resources

- [Enriching your text in text views](https://developer.apple.com/documentation/UIKit/enriching-your-text-in-text-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/enriching-your-text-in-text-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/enriching-your-text-in-text-views.json
- [TextKit](https://developer.apple.com/documentation/AppKit/textkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/textkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/textkit.json

## Code Snippets

### NSTextViewportRenderingSurface conformance — [9:47]

```swift
class MyView: UIView, NSTextViewportRenderingSurface {}
```

### NSTextViewportRenderingSurfaceKey and NSMapTable — [10:25]

```swift
class MyView: UIView, NSTextViewportRenderingSurface {}

var cache: NSMapTable<NSTextLayoutFragment, MyView>
```

### UITextView/NSTextView in SwiftUI via ViewRepresentable — [12:39]

```swift
// Using a TextView in SwiftUI

import SwiftUI

struct MyTextView: View {
    var body: some View { TextViewRepresentable() }
}

#if os(macOS)
struct TextViewRepresentable: NSViewRepresentable {
    func makeNSView(context: Context) -> NSTextView { 
      NSTextView() 
    }
    func updateNSView(_ nsView: NSTextView, context: Context) {
    }
}
#else
struct TextViewRepresentable: UIViewRepresentable {
    func makeUIView(context: Context) -> UITextView {
        UITextView() 
    }
    func updateUIView(_ uiView: UITextView, context: Context) {
    }
}
#endif
```

### ContainerView with TextView and line number view — [13:33]

```swift
// Create a text view subclass for a code editor

import UIKit

class TextView: UITextView {}

class ContainerView: UIView {
    let textView = TextView()
    let lineNumberView = UIView()

    textView.font = UIFont.monospacedSystemFont
}
```

### Three NSTextViewportLayoutControllerDelegate overrides — [14:42]

```swift
// Override viewport controller delegate methods

class TextView: UITextView {
    // Set up
		override func textViewportLayoutControllerWillLayout(_ textViewportLayoutController: NSTextViewportLayoutController) {
    	super.textViewportLayoutControllerWillLayout(textViewportLayoutController)
      //...
    }

    // Get paragraph bounds
    override func textViewportLayoutController (_ textViewportLayoutController: NSTextViewportLayoutController, configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment) {
			super.textViewportLayoutController(textViewportLayoutController, configureRenderingSurfaceFor: textLayoutFragment)
      //...
    }

    // Share accumulated info back to ContainerView
		override func textViewportLayoutControllerDidLayout (_ textViewportLayoutController: NSTextViewportLayoutController) {
		  super.textViewportLayoutControllerDidLayout(textViewportLayoutController)
      //...
    }
}
```

### startingLineNumber(for:) using enumerateTextElements — [15:59]

```swift
func startingLineNumber(for viewportRange: NSTextRange?) -> Int {
    guard let viewportRange,
          let storage = textLayoutManager?.textContentManager
              as? NSTextContentStorage else { return 0 }
    let startLocation = storage.documentRange.location
    var count = 1
    storage.enumerateTextElements(from: startLocation) { element in
        guard let range = element.elementRange else { return true }
        if range.location.compare(viewportRange.location)
            != .orderedAscending { return false }
        count += 1
        return true
    }
    return count
}
```

### DidLayout: convert frames to viewport coordinates — [17:02]

```swift
// Override viewport controller delegate methods

class TextView: UITextView {
    private var lines: [CGRect] = []
    private var startingLineNumber = 0
    var onDidLayout: ((Int, [CGRect]) -> Void)?

    // Share accumulated info back to ContainerView
		override func textViewportLayoutControllerDidLayout (_ textViewportLayoutController: NSTextViewportLayoutController) {
        super.textViewportLayoutControllerDidLayout(controller)
        let origin = controller.viewportBounds.origin
        onDidLayout?(startingLineNumber, lines.map {$0.offsetBy(dx: 0, dy: -origin.y) })
    }
}
```

### Draw line numbers in ContainerView closure — [17:16]

```swift
// Draw line numbers in the ContainerView

class ContainerView: UIView {
    let textView = TextView()
    let lineNumberView = UIView()
    func setup() {
        textView.onDidLayout = {startingLineNumber, lines in
            let attributes: [NSAttributedString.Key: Any] = [
                .font: UIFont.monospacedSystemFont(ofSize: 11, weight: .regular),
                .foregroundColor: UIColor.secondaryLabel
            ]
            for (i, frame) in lines.enumerated() {
                let number = "\(startingLineNumber + i)" as NSString
                number.draw(at: CGPoint(x: 8, y: frame.minY),
                    withAttributes: attributes)
            }
        }
    }
}
```

### Collapsible sections: full TextView class — [19:22]

```swift
// Add collapsible sections to your text view

class TextView: UITextView, NSTextContentStorageDelegate {
    var collapsedSections: Set<Int> = []

    // Set up
		override func textViewportLayoutControllerWillLayout(_ textViewportLayoutController: NSTextViewportLayoutController) {
    	super.textViewportLayoutControllerWillLayout(textViewportLayoutController)
      //...
    }

    // Get paragraph bounds
    override func textViewportLayoutController (_ textViewportLayoutController: NSTextViewportLayoutController, configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment) {
			super.textViewportLayoutController(textViewportLayoutController, configureRenderingSurfaceFor: textLayoutFragment)
      //...
    }

    // Share accumulated info back to ContainerView
		override func textViewportLayoutControllerDidLayout (_ textViewportLayoutController: NSTextViewportLayoutController) {
		  super.textViewportLayoutControllerDidLayout(textViewportLayoutController)
      //...
    }

    // Skip layout for paragraphs marked as collapsed
    func textContentManager(shouldEnumerate textElement: NSTextElement, options: NSTextContentManager.EnumerationOptions) -> Bool {
      //...
    }

    // Handle section collapse toggling
    func toggleSection(headerOffset: Int) {
        if collapsedSections.contains(headerOffset) {
            collapsedSections.remove(headerOffset)
        } else {
            collapsedSections.insert(headerOffset)
        }
        guard let textLayoutManager = textLayoutManager else { return }

        let textViewportLayoutController = textLayoutManager.textViewportLayoutController
        textViewportLayoutController.delegate?.textViewportLayoutControllerReceivedSetNeedsLayout?(textViewportLayoutController)
    }
}
```

### Text attachment view provider reuse policy — [22:06]

```swift
// Cache text attachment view providers

import UIKit

class ViewController: UIViewController {

    var textView: UITextView

    func setupTextView() {
        textView = UITextView()
        textView.register(
            [.onEditingInlineParagraphs],
            forTextAttachmentViewProviderType: AnimatedAttachmentViewProvider.self
        )
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/370) — developer.apple.com. Indexed for agent consumption._
