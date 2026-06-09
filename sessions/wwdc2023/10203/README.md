---
id: "wwdc2023-10203"
event: "wwdc2023"
year: 2023
title: "Develop your first immersive app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10203"
topics: ["Essentials", "Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Develop your first immersive app

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10203](https://developer.apple.com/videos/play/wwdc2023/10203)

Find out how you can build immersive apps for visionOS using Xcode and Reality Composer Pro. We’ll show you how to get started with a new visionOS project, use Xcode Previews for your SwiftUI development, and take advantage of RealityKit and RealityView to render 3D content. 

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,712 words)

## Code Snippets

### Glass background effect — [6:54]

```swift
VStack {
    Toggle("Enlarge RealityView Content", isOn: $enlarge)
        .toggleStyle(.button)
}
.padding()
.glassBackgroundEffect()
```

### RealityView — [7:28]

```swift
RealityView { content in
    // Add the initial RealityKit content
    if let scene = try? await Entity(named: "Scene", in: realityKitContentBundle) {
        content.add(scene)
    }
} update: { content in
    // Update the RealityKit content when SwiftUI state changes
    if let scene = content.entities.first {
        let uniformScale: Float = enlarge ? 1.4 : 1.0
        scene.transform.scale = [uniformScale, uniformScale, uniformScale]
    }
}
.gesture(TapGesture().targetedToAnyEntity().onEnded { _ in
    enlarge.toggle()
})
```

### ImmersiveView — [20:31]

```swift
// MyFirstImmersiveApp.swift

@main
struct MyFirstImmersiveApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }.windowStyle(.volumetric)

        ImmersiveSpace(id: "ImmersiveSpace") {
            ImmersiveView()
        }
    }
}
```

### Size that fits — [22:58]

```swift
#Preview {
    ImmersiveView()
        .previewLayout(.sizeThatFits)
}
```

### openImmersiveSpace — [23:48]

```swift
struct ContentView: View {

    @Environment(\.openImmersiveSpace) var openImmersiveSpace

    var body: some View {
        Button("Open") {
            Task {
                await openImmersiveSpace(id: "ImmersiveSpace")
            }
        }
    }
}
```

### Entity targeting — [25:48]

```swift
import SwiftUI
import RealityKit

struct ContentView: View {
    var body: some View {
        RealityView { content in
            // For entity targeting to work, entities must have a CollisionComponent
            // and an InputTargetComponent!
        }
        .gesture(TapGesture().targetedToAnyEntity().onEnded { value in
            print("Tapped entity \(value.entity)!")
        })
    }
}
```

### Move animation — [28:56]

```swift
.gesture(TapGesture().targetedToAnyEntity().onEnded { value in
    var transform = value.entity.transform
    transform.translation += SIMD3(0.1, 0, -0.1)
    value.entity.move(
        to: transform,
        relativeTo: nil,
        duration: 3,
        timingFunction: .easeInOut
    )
})
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10203/6/469019B0-281D-4B3E-BAE3-B9302B204739/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10203/6/469019B0-281D-4B3E-BAE3-B9302B204739/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10203) — developer.apple.com. Indexed for agent consumption._