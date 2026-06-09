---
id: "wwdc2021-10061"
event: "wwdc2021"
year: 2021
title: "Meet TextKit 2"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10061"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet TextKit 2

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10061](https://developer.apple.com/videos/play/wwdc2021/10061)

Meet TextKit 2: Apple’s next-generation text engine, redesigned for improved correctness, safety, and performance. Discover how TextKit 2 can help you provide a better text experience for international audiences, create more diverse layouts by mixing text content with visual content, and ensure smooth scrolling performance. We’ll introduce the latest APIs, dive into some practical examples, and provide guidance for modernizing your apps.

**Keywords:** `appkit`, `banana`, `bananaphone`, `edit`, `nstextview`, `text`, `textedit`, `uikit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,767 words)

## Documentation & Resources

- [Using TextKit 2 to interact with text](https://developer.apple.com/documentation/UIKit/using-textkit-2-to-interact-with-text) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/using-textkit-2-to-interact-with-text
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/using-textkit-2-to-interact-with-text.json
- [TextKit](https://developer.apple.com/documentation/AppKit/textkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/textkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/textkit.json

## Code Snippets

### Responding to layout updates: textViewportLayoutControllerWillLayout() — [32:22]

```swift
func textViewportLayoutControllerWillLayout(_ controller: NSTextViewportLayoutController) {
    contentLayer.sublayers = nil
    CATransaction.begin()
}
```

### Responding to layout updates: textViewportLayoutController(_:configureRenderingSurfaceFor:) — [32:47]

```swift
private func animate(_ layer: CALayer, from source: CGPoint, to destination: CGPoint) {
    let animation = CABasicAnimation(keyPath: "position")
    animation.fromValue = source
    animation.toValue = destination
    animation.duration = slowAnimations ? 2.0 : 0.3
    layer.add(animation, forKey: nil)
}

private func findOrCreateLayer(_ textLayoutFragment: NSTextLayoutFragment) -> (TextLayoutFragmentLayer, Bool) {
    if let layer = fragmentLayerMap.object(forKey: textLayoutFragment) as? TextLayoutFragmentLayer {
        return (layer, false)
    } else {
        let layer = TextLayoutFragmentLayer(layoutFragment: textLayoutFragment, padding: padding)
        fragmentLayerMap.setObject(layer, forKey: textLayoutFragment)
        return (layer, true)
    }
}

func textViewportLayoutController(_ controller: NSTextViewportLayoutController,
                                  configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment) {
    let (layer, layerIsNew) = findOrCreateLayer(textLayoutFragment)
    if !layerIsNew {
        let oldPosition = layer.position
        let oldBounds = layer.bounds
        layer.updateGeometry()
        if oldBounds != layer.bounds {
            layer.setNeedsDisplay()
        }
        if oldPosition != layer.position {
            animate(layer, from: oldPosition, to: layer.position)
        }
    }
    if layer.showLayerFrames != showLayerFrames {
        layer.showLayerFrames = showLayerFrames
        layer.setNeedsDisplay()
    }

    contentLayer.addSublayer(layer)
}
```

### Responding to layout updates: textViewportLayoutControllerDidLayout() — [33:10]

```swift
func textViewportLayoutControllerDidLayout(_ controller: NSTextViewportLayoutController) {
    CATransaction.commit()
    updateSelectionHighlights()
    updateContentSizeIfNeeded()
    adjustViewportOffsetIfNeeded()
}
```

### Overriding text attributes for comments — [33:47]

```swift
func textContentStorage(_ textContentStorage: NSTextContentStorage, textParagraphWith range: NSRange) -> NSTextParagraph? {
    // In this method, we'll inject some attributes for display, without modifying the text storage directly.
    var paragraphWithDisplayAttributes: NSTextParagraph? = nil

    // First, get a copy of the paragraph from the original text storage.
    let originalText = textContentStorage.textStorage!.attributedSubstring(from: range)
    if originalText.attribute(.commentDepth, at: 0, effectiveRange: nil) != nil {
        // Use white colored text to make our comments visible against the bright background.
        let displayAttributes: [NSAttributedString.Key: AnyObject] = [.font: commentFont, .foregroundColor: commentColor]
        let textWithDisplayAttributes = NSMutableAttributedString(attributedString: originalText)
        // Use the display attributes for the text of the comment itself, without the reaction.
        // The last character is the newline, second to last is the attachment character for the reaction.
        let rangeForDisplayAttributes = NSRange(location: 0, length: textWithDisplayAttributes.length - 2)
        textWithDisplayAttributes.addAttributes(displayAttributes, range: rangeForDisplayAttributes)

        // Create our new paragraph with our display attributes.
        paragraphWithDisplayAttributes = NSTextParagraph(attributedString: textWithDisplayAttributes)
    } else {
        return nil
    }
    // If the original paragraph wasn't a comment, this return value will be nil.
    // The text content storage will use the original paragraph in this case.
    return paragraphWithDisplayAttributes
}
```

### Hiding comments — [34:06]

```swift
func textContentManager(_ textContentManager: NSTextContentManager,
                        shouldEnumerate textElement: NSTextElement,
                        with options: NSTextElementProviderEnumerationOptions) -> Bool {
    // The text content manager calls this method to determine whether each text element should be enumerated for layout.
    // To hide comments, tell the text content manager not to enumerate this element if it's a comment.
    if !showComments {
        if let paragraph = textElement as? NSTextParagraph {
            let commentDepthValue = paragraph.attributedString.attribute(.commentDepth, at: 0, effectiveRange: nil)
            if commentDepthValue != nil {
                return false
            }
        }
    }
    return true
}
```

### Generating special layout fragments for comments — [34:28]

```swift
func textLayoutManager(_ textLayoutManager: NSTextLayoutManager,
                       textLayoutFragmentFor location: NSTextLocation,
                       in textElement: NSTextElement) -> NSTextLayoutFragment {
    let index = textLayoutManager.offset(from: textLayoutManager.documentRange.location, to: location)
    // swiftlint:disable force_cast
    let commentDepthValue = textContentStorage!.textStorage!.attribute(.commentDepth, at: index, effectiveRange: nil) as! NSNumber?
    if commentDepthValue != nil {
        let layoutFragment = BubbleLayoutFragment(textElement: textElement, range: textElement.elementRange)
        layoutFragment.commentDepth = commentDepthValue!.uintValue
        return layoutFragment
    } else {
        return NSTextLayoutFragment(textElement: textElement, range: textElement.elementRange)
    }
}
```

### Drawing the comment bubble — [34:58]

```swift
var commentDepth: UInt = 0

private var tightTextBounds: CGRect {
    var fragmentTextBounds = CGRect.null
    for lineFragment in textLineFragments {
        let lineFragmentBounds = lineFragment.typographicBounds
        if fragmentTextBounds.isNull {
            fragmentTextBounds = lineFragmentBounds
        } else {
            fragmentTextBounds = fragmentTextBounds.union(lineFragmentBounds)
        }
    }
    return fragmentTextBounds
}

// Return the bounding rect of the chat bubble, in the space of the first line fragment.
private var bubbleRect: CGRect { return tightTextBounds.insetBy(dx: -3, dy: -3) }

private var bubbleCornerRadius: CGFloat { return 20 }

private var bubbleColor: Color { return .systemIndigo }

private func createBubblePath(with ctx: CGContext) -> CGPath {
    let bubbleRect = self.bubbleRect
    let rect = min(bubbleCornerRadius, bubbleRect.size.height / 2, bubbleRect.size.width / 2)
    return CGPath(roundedRect: bubbleRect, cornerWidth: rect, cornerHeight: rect, transform: nil)
}

override var renderingSurfaceBounds: CGRect {
    return bubbleRect.union(super.renderingSurfaceBounds)
}

override func draw(at renderingOrigin: CGPoint, in ctx: CGContext) {
    // Draw the bubble and debug outline.
    ctx.saveGState()
    let bubblePath = createBubblePath(with: ctx)
    ctx.addPath(bubblePath)
    ctx.setFillColor(bubbleColor.cgColor)
    ctx.fillPath()
    ctx.restoreGState()

    // Draw the text on top.
    super.draw(at: renderingOrigin, in: ctx)
}
```

### Opting NSTextView in to TextKit 2 — [37:26]

```swift
var scrollView: NSScrollView!
var containerSize = CGSize.zero
var textContainer = NSTextContainer()

// Important: Keep a reference to text storage since NSTextView weakly references it.
var textContentStorage = NSTextContentStorage()

override func viewDidLoad() {
    super.viewDidLoad()

    scrollView =
        NSScrollView(frame: NSRect(origin: CGPoint(),
                                   size: CGSize(width: view.bounds.width, height: view.bounds.height)))
    scrollView.translatesAutoresizingMaskIntoConstraints = false
    view.addSubview(scrollView)

    NSLayoutConstraint.activate([
        scrollView.leadingAnchor.constraint(equalTo: (view.leadingAnchor)),
        scrollView.trailingAnchor.constraint(equalTo: (view.trailingAnchor)),
        scrollView.topAnchor.constraint(equalTo: (view.topAnchor)),
        scrollView.bottomAnchor.constraint(equalTo: (view.bottomAnchor))
        ])

    setUpScrollView(scrollsHorizontally: false)
}

func setUpScrollView(scrollsHorizontally: Bool) {
    scrollView.borderType = .noBorder
    scrollView.hasVerticalScroller = true
    scrollView.hasHorizontalScroller = scrollsHorizontally

    setUpTextContainer(scrollsHorizontally: scrollsHorizontally)
    setUpTextView(scrollsHorizontally: scrollsHorizontally)
}

func setUpTextContainer(scrollsHorizontally: Bool) {
    let contentSize = scrollView.contentSize
    if scrollsHorizontally {
        containerSize = NSSize(width: CGFloat.greatestFiniteMagnitude, height: CGFloat.greatestFiniteMagnitude)
        textContainer.containerSize = containerSize
        textContainer.widthTracksTextView = false
    }
    else {
        containerSize = NSSize(width: contentSize.width, height: CGFloat.greatestFiniteMagnitude)
        textContainer.containerSize = containerSize
        textContainer.widthTracksTextView = true
    }
}

func setUpTextView(scrollsHorizontally: Bool) {
    let textLayoutManager = NSTextLayoutManager()
    textLayoutManager.textContainer = textContainer

    textContentStorage.addTextLayoutManager(textLayoutManager)

    // Workaround: Pass textLayoutManager.textContainer to the NSTextView initializer
    let textView = NSTextView(frame: scrollView.contentView.bounds, textContainer: textLayoutManager.textContainer)

    textView.isEditable = true
    textView.isSelectable = true
    textView.minSize = CGSize()
    textView.maxSize = containerSize
    textView.isVerticallyResizable = true
    textView.isHorizontallyResizable = scrollsHorizontally
    textContentStorage.performEditingTransaction {
        textView.textStorage?.append(NSAttributedString(string: "Text content..."))
    }
    scrollView.documentView = textView
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10061/4/D12F25A4-D409-4DDA-9DCF-72C97E9875C3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10061/4/D12F25A4-D409-4DDA-9DCF-72C97E9875C3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10061) — developer.apple.com. Indexed for agent consumption._