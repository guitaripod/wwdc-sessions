---
id: "wwdc2024-10214"
event: "wwdc2024"
year: 2024
title: "Squeeze the most out of Apple Pencil"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10214"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Squeeze the most out of Apple Pencil

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10214](https://developer.apple.com/videos/play/wwdc2024/10214)

New in iOS 18, iPadOS 18, and visionOS 2, the PencilKit tool picker gains the ability to have completely custom tools, with custom attributes. Learn how to express your custom drawing experience in the tool picker using the same great tool picking experience available across the system. Discover how to access the new features of the Apple Pencil Pro, including roll angle, the squeeze gesture, and haptic feedback.

**Keywords:** `barrel roll`, `draw`, `finger`, `haptics`, `hover`, `pencil kit`, `roll`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,271 words)

## Documentation & Resources

- [Playing haptic feedback in your app](https://developer.apple.com/documentation/ApplePencil/playing-haptic-feedback-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ApplePencil/playing-haptic-feedback-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ApplePencil/playing-haptic-feedback-in-your-app.json
- [Apple Pencil](https://developer.apple.com/documentation/ApplePencil) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ApplePencil
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ApplePencil.json
- [Configuring the PencilKit tool picker](https://developer.apple.com/documentation/PencilKit/configuring-the-pencilkit-tool-picker) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/configuring-the-pencilkit-tool-picker
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/configuring-the-pencilkit-tool-picker.json
- [Apple Pencil updates](https://developer.apple.com/documentation/Updates/ApplePencil) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/ApplePencil
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/ApplePencil.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Human Interface Guidelines: Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/apple-pencil-and-scribble

## Code Snippets

### Respond to squeeze in UIKit — [10:24]

```swift
class MyViewController: UIViewController, UIPencilInteractionDelegate {

    func pencilInteraction(_ interaction: UIPencilInteraction, 
               didReceiveSqueeze squeeze: UIPencilInteraction.Squeeze) {

        if UIPencilInteraction.preferredSqueezeAction == .showContextualPalette &&
           squeeze.phase == .ended {
           let anchorPoint = squeeze.hoverPose?.location ?? myDefaultLocation
           presentMyContextualPaletteAtPosition(anchorPoint)
        }
    }
}
```

### Respond to squeeze in SwiftUI — [10:46]

```swift
@Environment(\.preferredPencilSqueezeAction) var preferredAction
@State var contextualPalettePresented = false
@State var contextualPaletteAnchor = MyPaletteAnchor.default

var body: some View {
    MyView()
        .onPencilSqueeze { phase in
            if preferredAction == .showContextualPalette, case let .ended(value) = phase {
                if let anchorPoint = value.hoverPose?.anchor {
                    contextualPaletteAnchor = .point(anchorPoint)
                }
                contextualPalettePresented = true
            }
        }
}
```

### Provide canvas feedback in UIKit — [11:50]

```swift
class MyViewController: UIViewController {
    @ViewLoading var feedbackGenerator: UICanvasFeedbackGenerator

    override func viewDidLoad() {
        super.viewDidLoad()
        feedbackGenerator = UICanvasFeedbackGenerator(view: view)
    }

    func dragAlignedToGuide(_ sender: MyDragGesture) {
        feedbackGenerator.alignmentOccurred(at: sender.location(in: view))
    }

    func snappedToShape(_ sender: MyDrawGesture) {
        feedbackGenerator.pathCompleted(at: sender.location(in: view))
    }
}
```

### Provide canvas feedback in SwiftUI — [12:29]

```swift
@State var dragAlignedToGuide = 0
@State var snappedToShape = 0
 var body: some View {
    MyView()
        .sensoryFeedback(.alignment, trigger: dragAlignedToGuide)
        .sensoryFeedback(.pathComplete, trigger: snappedToShape)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10214/4/AFB648F1-CAD7-4F62-8916-9DF4372C33C4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10214/4/AFB648F1-CAD7-4F62-8916-9DF4372C33C4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10214) — developer.apple.com. Indexed for agent consumption._
