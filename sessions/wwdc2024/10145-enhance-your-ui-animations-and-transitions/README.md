---
id: "wwdc2024-10145"
event: "wwdc2024"
year: 2024
title: "Enhance your UI animations and transitions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10145"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance your UI animations and transitions

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10145](https://developer.apple.com/videos/play/wwdc2024/10145)

Explore how to adopt the zoom transition in navigation and presentations to increase the sense of continuity in your app, and learn how to animate UIKit views with SwiftUI animations to make it easier to build animations that feel continuous.

**Keywords:** `bracelets`, `friendship`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,257 words)

## Documentation & Resources

- [Unifying your app’s animations](https://developer.apple.com/documentation/SwiftUI/Unifying-your-app-s-animations) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Unifying-your-app-s-animations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Unifying-your-app-s-animations.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### Zoom transition in SwiftUI — [2:10]

```swift
NavigationLink {
    BraceletEditor(bracelet)
        .navigationTransitionStyle(
            .zoom(
                sourceID: bracelet.id,
                in: braceletList
            )
        )
} label: {
    BraceletPreview(bracelet)
}
.matchedTransitionSource(
    id: bracelet.id,
    in: braceletList
)
```

### Zoom transition in UIKit — [3:02]

```swift
func showEditor(for bracelet: Bracelet) {
    let braceletEditor = BraceletEditor(bracelet)
    braceletEditor.preferredTransition = .zoom { context in
        let editor = context.zoomedViewController
            as! BraceletEditor
        return cell(for: editor.bracelet)
    }
    navigationController?.pushViewController(braceletEditor, animated: true)
}
```

### Animate UIView with SwiftUI animation — [8:39]

```swift
UIView.animate(.spring(duration: 0.5)) {
    bead.center = endOfBracelet
}
```

### Animating representables — [9:56]

```swift
struct BeadBoxWrapper: UIViewRepresentable {
    @Binding var isOpen: Bool

    func updateUIView(_ box: BeadBox, context: Context) {
        context.animate {
            box.lid.center.y = isOpen ? -100 : 100
		    }
    }
}

struct BraceletEditor: View {
    @State private var isBeadBoxOpen = false
    var body: some View {
        BeadBoxWrapper($isBeadBoxOpen.animated())
            .onTapGesture {
                isBeadBoxOpen.toggle()
            }
    }
}
```

### Gesture-driven animations — [11:39]

```swift
switch gesture.state {
case .changed:
    UIView.animate(.interactiveSpring) {
        bead.center = gesture.translation
    }

case .ended:
    UIView.animate(.spring) {
        bead.center = endOfBracelet
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10145/4/53B7DA20-6508-44CC-9BC6-86943CE6BF32/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10145/4/53B7DA20-6508-44CC-9BC6-86943CE6BF32/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10145) — developer.apple.com. Indexed for agent consumption._
