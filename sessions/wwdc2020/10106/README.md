---
id: "wwdc2020-10106"
event: "wwdc2020"
year: 2020
title: "Meet Scribble for iPad"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10106"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet Scribble for iPad

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10106](https://developer.apple.com/videos/play/wwdc2020/10106)

Scribble offers a lightweight, ergonomic, and enjoyable way of entering text on iPad with Apple Pencil. Discover how people can take advantage of Scribble and handwritten text in apps that use standard text input controls or that implement a custom text editing experience. You’ll learn how it integrates into TextKit, and when you’ll need to adopt the new UIScribbleInteraction and UIIndirectScribbleInteraction APIs to provide a delightful and consistent experience with Scribble in your app.

To get the most out of this session, you should be familiar with UIKit text input controls, as well as keyboard input technologies. To get started, watch “Keyboard Input in iOS”. If you’re building a custom text editor, you should be familiar with the UITextInput protocol, TextKit, and related text input APIs. For more information, we recommend checking out “TextKit Best Practices” and “The Keys to a Better Text Input Experience.” And for design guidelines on pencil-based interaction, check out “Apple Pencil Design Essentials.”

**Keywords:** `cursive`, `handwriting`, `recognition`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,151 words)

## Documentation & Resources

- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/PencilKit/customizing-scribble-with-interactions) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/customizing-scribble-with-interactions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/customizing-scribble-with-interactions.json

## Code Snippets

### isHandlingWriting Example — [9:15]

```swift
func updateSearchCompletion() {
    customSearchField.hideCompletionText = interaction.isHandlingWriting
}
```

### UIScribbleInteraction.isPencilInputExpected — [9:35]

```swift
override func viewDidAppear(_ animated: Bool) {
    if UIScribbleInteraction.isPencilInputExpected {
        let lineHeight = textField.font?.lineHeight ?? 17.0
        let heightForScribble = lineHeight * 4.0
        heightConstraint.constant = heightForScribble
    }
}
```

### scribbleInteractionDidFinishWriting — [9:51]

```swift
func scribbleInteractionDidFinishWriting(_ interaction: UIScribbleInteraction) {
    let lineHeight = textField.font?.lineHeight ?? 17.0
    let heightForScribble = lineHeight * 4.0
    heightConstraint.constant = heightForScribble
}
```

### Should Begin — [10:08]

```swift
func scribbleInteraction(_ interaction: UIScribbleInteraction,
                         shouldBeginAt location: CGPoint) -> Bool {
    return !appIsInDrawingMode()
}
```

### Install UIIndirectScribbleInteraction in Engraving Field — [11:41]

```swift
override init(frame: CGRect) {
    super.init(frame: frame)
    indirectScribbleInteraction = UIIndirectScribbleInteraction(delegate: self)
    addInteraction(indirectScribbleInteraction)
    ...
}
```

### Request Elements — [11:48]

```swift
func indirectScribbleInteraction(_ interaction: UIInteraction,
                                 requestElementsIn rect: CGRect,
                                 completion: @escaping ([ElementIdentifier]) -> Void) {
    completion(["EngravingIdentifier"])
}
```

### Frame for element — [12:14]

```swift
func indirectScribbleInteraction(_ interaction: UIInteraction,
                                 frameForElement elementIdentifier: String) -> CGRect {
    return bounds
}
```

### Focus Element if Needed — [12:28]

```swift
func indirectScribbleInteraction(_ interaction: UIInteraction,
                                 focusElementIfNeeded elementIdentifier: String,
                                 referencePoint focusReferencePoint: CGPoint,
                                 completion: @escaping ((UIResponder & UITextInput)?) -> Void)
{
    if editingTextField == nil {
        createTextField()
    }
    editingTextField?.becomeFirstResponder()

    completion(editingTextField)
}
```

### Is Element Focused — [12:57]

```swift
func indirectScribbleInteraction(_ interaction: UIInteraction,
                                 isElementFocused elementIdentifier: String) -> Bool {
    // Indicate if our only element is currently installed and focused
    return editingTextField?.isFirstResponder ?? false
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10106/4/AD9A0416-4A7E-4ED7-86AD-8EEEF7199216/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10106) — developer.apple.com. Indexed for agent consumption._