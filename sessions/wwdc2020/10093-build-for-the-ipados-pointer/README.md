---
id: "wwdc2020-10093"
event: "wwdc2020"
year: 2020
title: "Build for the iPadOS pointer"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10093"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build for the iPadOS pointer

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10093](https://developer.apple.com/videos/play/wwdc2020/10093)

Help people who use iPad with a Magic Keyboard, mouse, trackpad or other input device get the most out of your app. We’ll show you how to add customizations to the pointer on iPad using pointer interaction APIs, create pointer effects for your buttons and custom views, and change the pointer shape in specific areas of your app to highlight them. To learn more about pointer interactions on iPad and to get the most out of this session, we recommend also watching “Design for the iPadOS pointer” and “Handle trackpad and mouse input.”

**Keywords:** `better ipad`, `cursor`, `dynamic`, `keyboard`, `magic`, `magic keyboard`, `mouse`, `pointer`, `trackpad`, `uikit`, `uitouch`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,863 words)

## Documentation & Resources

- [Enhancing your iPad app with pointer interactions](https://developer.apple.com/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/enhancing-your-ipad-app-with-pointer-interactions.json

## Code Snippets

### UIButton Pointer Effects — [6:04]

```swift
// Enable the button's built-in pointer interaction.
myButton.isPointerInteractionEnabled = true

// Customize the default interaction effect.
myButton.pointerStyleProvider = { button, proposedEffect, proposedShape -> UIPointerStyle? in
		// In this example, we'll switch to using the .lift effect by creating a new
    // UIPointerEffect with the .lift type using the proposedEffect's preview.
    return UIPointerStyle(effect: .lift(proposedEffect.preview), shape: proposedShape)
}
```

### Pointer Content Effect — [7:05]

```swift
// Create a UIPointerStyle that applies the .highlight effect. 

// Outset the view's frame so the pointer shape has some generous padding around the view's contents.
// Note that this frame must be in the provided UITargetedPreview's container's coordinate space. 
// In the majority of cases (where the preview doesn't have a custom container), this is just the view's superview.
let rect = myView.frame.insetBy(dx: -8.0, dy: -4.0)
let preview = UITargetedPreview(view: myView)

return UIPointerStyle(effect: .highlight(preview), shape: .roundedRect(rect))
```

### Pointer Shape Customization — [8:02]

```swift
// Create a UIPointerStyle that changes the pointer into a vertical beam. 

let beamLength = myFont.lineHeight
return UIPointerStyle(shape: .verticalBeam(length: beamLength), constrainedAxes: .vertical)
```

### UIPointerInteraction Region Entrance Animation — [21:31]

```swift
func pointerInteraction(_ interaction: UIPointerInteraction, 
                          willEnter region: UIPointerRegion, 
                          animator: UIPointerInteractionAnimating) {

     // Fade out separator when entering region.
     animator.addAnimations {
          self.separatorView.alpha = 0.0
     }
}
```

### UIPointerInteraction Region Exit Animation — [21:51]

```swift
func pointerInteraction(_ interaction: UIPointerInteraction, 
                          willExit region: UIPointerRegion, 
                          animator: UIPointerInteractionAnimating) {

     // Fade separator back in when exiting region.
     animator.addAnimations {
          self.separatorView.alpha = 1.0
     }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10093/4/3B8A69F7-49AD-49B5-AFD5-1F1AF706199D/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10093) — developer.apple.com. Indexed for agent consumption._
