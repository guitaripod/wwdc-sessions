---
id: "wwdc2025-317"
event: "wwdc2025"
year: 2025
title: "What’s new in visionOS 26"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/317"
topics: ["Audio & Video", "Business & Education", "Design", "Graphics & Games", "Photos & Camera", "Safari & Web", "SwiftUI & UI Frameworks", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# What’s new in visionOS 26

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-317](https://developer.apple.com/videos/play/wwdc2025/317)

Explore exciting new features in visionOS 26. Discover enhanced volumetric APIs and learn how you can combine the power of SwiftUI, RealityKit and ARKit. Find out how you can build more engaging apps and games using faster hand tracking and input from spatial accessories. Get a sneak peek at updates to SharePlay, Compositor Services, immersive media, spatial web, Enterprise APIs, and much more.

**Keywords:** `arkit`, `audio`, `audio &amp; video`, `business`, `businessconnect`, `compositorservices`, `enterprise`, `games`, `immersive`, `occlusion`, `quicklook`, `quick look`, `realitykit`, `realitykit audio`, `safari`, `safari &amp; web`, `shareplay`, `spatial`, `spatial accessories`, `spatial audio`, `spatial computing`, `swiftui`, `tabletopkit`, `video`, `visionos`, `web`, `widgetkit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,044 words)

## Documentation & Resources

- [Petite Asteroids: Building a volumetric visionOS game](https://developer.apple.com/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game.json
- [Canyon Crosser: Building a volumetric hike-planning app](https://developer.apple.com/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app.json
- [TabletopKit](https://developer.apple.com/documentation/TabletopKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TabletopKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TabletopKit.json

## Code Snippets

### DepthAlignment — [2:25]

```swift
// Layout types back align views by default

struct LandmarkProfile: View {

    var body: some View {
       VStackLayout().depthAlignment(.front) {
            ResizableLandmarkModel()
            LandmarkNameCard()
        }
    }
}
```

### rotation3DLayout — [2:41]

```swift
// Rotate using any axis or angle

struct PlaneStack: View {

    var body: some View {
        VStack {
            ToyPlaneModel()
            ToyPlaneModel()
              .rotation3DLayout(angle, axis: .z)
            ToyPlaneModel()
        }
    }
}
```

### Dynamic Bounds Restrictions — [4:22]

```swift
// Dynamic Bounds Restrictions

struct ContentView: View, Animatable {

    var body: some View {
        VStackLayout().depthAlignment(.front) {
            // . . .
        }
        .preferredWindowClippingMargins(.all, 400)
    }
}
```

### Model3D manipulable view modifier — [5:05]

```swift
// Apply the manipulable view modifier to each Model3D block per 3D object

struct RockView: View {
    var body: some View {
        RockLayout {
            ForEach(rocks) { rock in
                Model3D(named: rock.name, bundle: realityKitContentBundle) {
                    model in
                    model.model?
                        .resizable()
                        .scaledToFit3D()
                }
                .manipulable()
            }
        }
    }
}
```

### ManipulationComponent — [5:14]

```swift
// Add a ManipulationComponent to each entity in your scene

struct RealityKitObjectManipulation: View {
    var body: some View {
        RealityView {ccontent in
            let rocks = await loadRockEntities()
            arrangeRocks(rocks)
            for rock in rocks {
                ManipulationComponent.configureEntity(rock)
                content.add(rock)
            }
        }
    }
}
```

### QuickLook3DView — [5:18]

```swift
// Preview multiple 3D models simultaneously in your space with Quick Look and 
// get object manipulation on each of them by default

struct QuickLook3DView: View {

    let url: URL
    var body: some View {
        VStack {
            Button("View in your space") {
                _ = PreviewApplication.open(urls: [url])
            }
        }
    }
}
```

### Gestures on entities — [6:36]

```swift
// Gestures on entities
struct GestureExample: View {
    @GestureState private var dragMountain: Float = 0
    @GestureState private var dragTerrain: Float = 0
		var body: some View {
        RealityView { content in
            let drag1 = GestureComponent(
                DragGesture().updating($dragMountain) { value, offset, _ in
                    offset = Float(value.translation.width)
                })
            let drag2 = GestureComponent(
                DragGesture().updating($dragTerrain) {evalue, offset, _ in
                    offset = Float(value.translation.width)
                })
            mountain.components.set(drag1)
            terrain.components.set(drag2)
        } update: { content in
            // . . .
        }
    }
}
```

### Attachments on entities — [6:55]

```swift
// Attachments on entities

struct AttachmentComponentExample: View {
    var body: some View {
        RealityView { content in
            // ... Load the mountain entity

            // Create an AttachmentComponent with any SwiftUI View
            let attachmentComponent = ViewAttachmentComponent(
                rootView: NameSign()
            )
            mountain.components.set(attachmentComponent)
        }
    }
}
```

### SwiftUI restoration APIs — [13:43]

```swift
var body: some Scene {
    // . . .
    WindowGroup(id: "Editor") {
        EditorView()
    }

    Window("Inspector", id: "Inspector") {
        InspectorView()
    }
    // Prevent the inspector window from being launched on its own without an
    // editor window present.
    .defaultLaunchBehavior(.suppressed)
    // Prevent the inspector window from being persisted and restored across
    // different process or boot sessions.
    .restorationBehavior(.disabled)
}
```

### Look to scroll — [33:45]

```swift
// SwiftUI
var body: some View {
    ScrollView {
        HikeDetails()
    }
    .scrollInputBehavior(.enabled, for: .look)
}


// UIKit
let scrollView: UIScrollView = {
    let scroll = UIScrollView()
    scroll.lookToScrollAxes = .vertical
    return scroll
}()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/317/4/4700af86-65f4-429a-b0a7-7dd18247c03d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/317/4/4700af86-65f4-429a-b0a7-7dd18247c03d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/317) — developer.apple.com. Indexed for agent consumption._
