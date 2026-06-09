---
id: "wwdc2023-10113"
event: "wwdc2023"
year: 2023
title: "Take SwiftUI to the next dimension"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10113"
topics: ["Spatial Computing", "SwiftUI & UI Frameworks"]
hasTranscript: true
---

# Take SwiftUI to the next dimension

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Published:** 2023-06-07 · **Session:** [wwdc2023-10113](https://developer.apple.com/videos/play/wwdc2023/10113)

Get ready to add depth and dimension to your visionOS apps. Find out how to bring three-dimensional objects to your app using volumes, get to know the Model 3D API, and learn how to position and animate content. We’ll also show you how to use UI attachments in RealityView and support gestures in your content.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,543 words)

## Code Snippets

### MoonView — [3:35]

```swift
struct MoonView {
  var body: some View {
    Model3D(named: "Moon") { phase in
      switch phase {
      case .empty:
        ProgressView()
      case let .failure(error):
        Text(error.localizedDescription)
      case let .success(model):
        model
          .resizable()
          .scaledToFit()
      }
    }
  }
}
```

### Manipulation Gesture — [17:26]

```swift
// Gesture combining dragging, magnification, and 3D rotation all at once.
var manipulationGesture: some Gesture<AffineTransform3D> {
    DragGesture()
        .simultaneously(with: MagnifyGesture())
        .simultaneously(with: RotateGesture3D())
        .map { gesture in
            let (translation, scale, rotation) = gesture.components()

            return AffineTransform3D(
                scale: scale,
                rotation: rotation,
                translation: translation
            )
        }
}

// Helper for extracting translation, magnification, and rotation.
extension SimultaneousGesture<
    SimultaneousGesture<DragGesture, MagnifyGesture>,
    RotateGesture3D>.Value {
    func components() -> (Vector3D, Size3D, Rotation3D) {
        let translation = self.first?.first?.translation3D ?? .zero
        let magnification = self.first?.second?.magnification ?? 1
        let size = Size3D(width: magnification, height: magnification, depth: magnification)
        let rotation = self.second?.rotation ?? .identity
        return (translation, size, rotation)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10113/5/00AAFA9F-AFE8-473B-BAB6-201545F4DF62/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10113/5/00AAFA9F-AFE8-473B-BAB6-201545F4DF62/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10113) — developer.apple.com. Indexed for agent consumption._