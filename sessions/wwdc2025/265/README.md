---
id: "wwdc2025-265"
event: "wwdc2025"
year: 2025
title: "Dive deeper into Writing Tools"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/265"
topics: ["App Services", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Dive deeper into Writing Tools

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-265](https://developer.apple.com/videos/play/wwdc2025/265)

With Writing Tools, people can proofread, rewrite, and transform text directly within your app. Learn advanced techniques to customize Writing Tools for your app. Explore formatting options and how they work with rich text editing. If you have a custom text engine, learn how to seamlessly integrate the complete Writing Tools experience, allowing edits directly within the text view.

**Keywords:** `nsservices`, `nstextview`, `textkit`, `uitextview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,196 words)

## Documentation & Resources

- [Enhancing your custom text engine with Writing Tools](https://developer.apple.com/documentation/AppKit/enhancing-your-custom-text-engine-with-writing-tools) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/enhancing-your-custom-text-engine-with-writing-tools
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/enhancing-your-custom-text-engine-with-writing-tools.json
- [Writing Tools](https://developer.apple.com/documentation/UIKit/writing-tools) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/writing-tools
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/writing-tools.json

## Code Snippets

### Attach a coordinator to the view (UIKit) — [11:46]

```swift
// Attach a coordinator to the view
// UIKit

func configureWritingTools() {
    guard UIWritingToolsCoordinator.isWritingToolsAvailable else { return }

    let coordinator = UIWritingToolsCoordinator(delegate: self)
    addInteraction(coordinator)
}
```

### Attach a coordinator to the view (AppKit) — [12:02]

```swift
// Attach a coordinator to the view
// AppKit

func configureWritingTools() {
    guard NSWritingToolsCoordinator.isWritingToolsAvailable else { return }

    let coordinator = NSWritingToolsCoordinator(delegate: self)

    coordinator.preferredBehavior = .complete
    coordinator.preferredResultOptions = [.richText, .list]
    writingToolsCoordinator = coordinator
}
```

### Prepare the context — [13:06]

```swift
// Prepare the context

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        requestsContextsFor scope: NSWritingToolsCoordinator.ContextScope,
        completion: @escaping ([NSWritingToolsCoordinator.Context]) -> Void) {

    var contexts = [NSWritingToolsCoordinator.Context]()

    switch scope {
    case .userSelection:
        let context = getContextObjectForSelection()
        contexts.append(context)
        break
        // other cases…
    }

    // Save references to the contexts for later delegate calls.
    storeContexts(contexts)
    completion(contexts)
}
```

### Respond to text changes from Writing Tools and update selected range — [13:48]

```swift
// Respond to text changes from Writing Tools

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        replace range: NSRange,
        in context: NSWritingToolsCoordinator.Context,
        proposedText replacementText: NSAttributedString,
        reason: NSWritingToolsCoordinator.TextReplacementReason,
        animationParameters: NSWritingToolsCoordinator.AnimationParameters?,
        completion: @escaping (NSAttributedString?) -> Void) {
}

// Update selected range

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        select ranges: [NSValue],
        in context: NSWritingToolsCoordinator.Context,
        completion: @escaping () -> Void) {
}
```

### Generate preview for animation (AppKit) — [14:41]

```swift
// Generate preview for animation (macOS)

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        requestsPreviewFor textAnimation: NSWritingToolsCoordinator.TextAnimation,
        of range: NSRange,
        in context: NSWritingToolsCoordinator.Context,
        completion: @escaping ([NSTextPreview]?) -> Void) {
}

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        requestsPreviewFor rect: NSRect,
        in context: NSWritingToolsCoordinator.Context,
        completion: @escaping (NSTextPreview?) -> Void) {
}
```

### Generate preview for animation (UIKit) — [14:58]

```swift
// Generate preview for animation (iOS)

func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator,
        requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation,
        of range: NSRange,
        in context: UIWritingToolsCoordinator.Context,
        completion: @escaping (UITargetedPreview?) -> Void) {
}
```

### Delegate callbacks before and after animation — [15:08]

```swift
// Generate preview for animation

func writingToolsCoordinator(
    _ writingToolsCoordinator: NSWritingToolsCoordinator,
    prepareFor textAnimation: NSWritingToolsCoordinator.TextAnimation,
    for range: NSRange,
    in context: NSWritingToolsCoordinator.Context,
    completion: @escaping () -> Void) {

    // Hide the specific range of text from the text view
}

func writingToolsCoordinator(
    _ writingToolsCoordinator: NSWritingToolsCoordinator,
    finish textAnimation: NSWritingToolsCoordinator.TextAnimation,
    for range: NSRange,
    in context: NSWritingToolsCoordinator.Context,
    completion: @escaping () -> Void) {

    // Show the specific range of text again
}
```

### Delegate callbacks to show proofreading marks — [15:39]

```swift
// Create proofreading marks

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        requestsUnderlinePathsFor range: NSRange,
        in context: NSWritingToolsCoordinator.Context,
        completion: @escaping ([NSBezierPath]) -> Void) {
}

func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator,
        requestsBoundingBezierPathsFor range: NSRange,
        in context: NSWritingToolsCoordinator.Context,
        completion: @escaping ([NSBezierPath]) -> Void) {
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/265/4/65bf71d2-6fef-47fe-8239-405d7ad9db8d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/265/4/65bf71d2-6fef-47fe-8239-405d7ad9db8d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/265) — developer.apple.com. Indexed for agent consumption._