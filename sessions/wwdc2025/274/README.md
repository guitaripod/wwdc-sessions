---
id: "wwdc2025-274"
event: "wwdc2025"
year: 2025
title: "Better together: SwiftUI and RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/274"
topics: ["Design", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Better together: SwiftUI and RealityKit

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-274](https://developer.apple.com/videos/play/wwdc2025/274)

Discover how to seamlessly blend SwiftUI and RealityKit in visionOS 26. We’ll explore enhancements to Model3D, including animation and ConfigurationCatalog support, and demonstrate smooth transitions to RealityView. You’ll learn how to leverage SwiftUI animations to drive RealityKit component changes, implement interactive manipulation, use new SwiftUI components for richer interactions, and observe RealityKit changes from your SwiftUI code. We’ll also cover how to use unified coordinate conversion for cross-framework coordinate transformations.


## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,181 words)

## Documentation & Resources

- [Rendering hover effects in Metal immersive apps](https://developer.apple.com/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps.json
- [Canyon Crosser: Building a volumetric hike-planning app](https://developer.apple.com/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app.json

## Code Snippets

### Sparky in Model3D — [1:42]

```swift
struct ContentView: View {
  var body: some View {
    Model3D(named: "sparky")
  }
}
```

### Sparky in Model3D with a name sign — [1:52]

```swift
struct ContentView: View {
  var body: some View {
    HStack {
      NameSign()
      Model3D(named: "sparky")
    }
  }
}
```

### Display a model asset in a Model3D and present playback controls​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [3:18]

```swift
struct RobotView: View {
  @State private var asset: Model3DAsset?
  var body: some View {
    if asset == nil {
      ProgressView().task { asset = try? await Model3DAsset(named: "sparky") }
    }
  }
}
```

### Display a model asset in a Model3D and present playback controls​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [3:34]

```swift
struct RobotView: View {
  @State private var asset: Model3DAsset?
  var body: some View {
    if asset == nil {
      ProgressView().task { asset = try? await Model3DAsset(named: "sparky") }
    } else if let asset {
      VStack {
        Model3D(asset: asset)
        AnimationPicker(asset: asset)
      }
    }
  }
}
```

### Display a model asset in a Model3D and present playback controls​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [4:03]

```swift
struct RobotView: View {
  @State private var asset: Model3DAsset?
  var body: some View {
    if asset == nil {
      ProgressView().task { asset = try? await Model3DAsset(named: "sparky") }
    } else if let asset {
      VStack {
        Model3D(asset: asset)
        AnimationPicker(asset: asset)
        if let animationController = asset.animationPlaybackController {
          RobotAnimationControls(playbackController: animationController)
        }
      }
    }
  }
}
```

### Pause, resume, stop, and change the move the play head in the animation​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [4:32]

```swift
struct RobotAnimationControls: View {
  @Bindable var controller: AnimationPlaybackController

  var body: some View {
    HStack {
      Button(controller.isPlaying ? "Pause" : "Play") {
        if controller.isPlaying { controller.pause() }
        else { controller.resume() }
      }

      Slider(
        value: $controller.time,
        in: 0...controller.duration
      ).id(controller)
    }
  }
}
```

### Load a Model3D using a ConfigurationCatalog​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [5:41]

```swift
struct ConfigCatalogExample: View {
  @State private var configCatalog: Entity.ConfigurationCatalog?
  @State private var configurations = [String: String]()
  @State private var showConfig = false
  var body: some View {
    if let configCatalog {
      Model3D(from: configCatalog, configurations: configurations)
        .popover(isPresented: $showConfig, arrowEdge: .leading) {
          ConfigPicker(
            name: "outfits",
            configCatalog: configCatalog,
            chosenConfig: $configurations["outfits"])
        }
    } else {
      ProgressView()
        .task {
          await loadConfigurationCatalog()
        }
    }
  }
}
```

### Switching from Model3D to RealityView — [6:51]

```swift
struct RobotView: View {
  let url: URL = Bundle.main.url(forResource: "sparky", withExtension: "reality")!

  var body: some View {
    HStack {
      NameSign()
      RealityView { content in
        if let sparky = try? await Entity(contentsOf: url) {
          content.add(sparky)
        }
      }
    }
  }
}
```

### Switching from Model3D to RealityView with layout behavior — [7:25]

```swift
struct RobotView: View {
  let url: URL = Bundle.main.url(forResource: "sparky", withExtension: "reality")!

  var body: some View {
    HStack {
      NameSign()
      RealityView { content in
        if let sparky = try? await Entity(contentsOf: url) {
          content.add(sparky)
        }
      }
      .realityViewLayoutBehavior(.fixedSize)
    }
  }
}
```

### Switching from Model3D to RealityView with layout behavior and RealityKit animation — [8:48]

```swift
struct RobotView: View {
  let url: URL = Bundle.main.url(forResource: "sparky", withExtension: "reality")!

  var body: some View {
    HStack {
      NameSign()
      RealityView { content in
        if let sparky = try? await Entity(contentsOf: url) {
          content.add(sparky)
          sparky.playAnimation(getAnimation())
        }
      }
      .realityViewLayoutBehavior(.fixedSize)
    }
  }
}
```

### Add 2 particle emitters; one to each side of the robot's head — [10:34]

```swift
func setupSparks(robotHead: Entity) {
  let leftSparks = Entity()
  let rightSparks = Entity()

  robotHead.addChild(leftSparks)
  robotHead.addChild(rightSparks)

  rightSparks.components.set(sparksComponent())
  leftSparks.components.set(sparksComponent())

  leftSparks.transform.rotation = simd_quatf(Rotation3D(
    angle: .degrees(180),
    axis: .y))

  leftSparks.transform.translation = leftEarOffset()
  rightSparks.transform.translation = rightEarOffset()
}

// Create and configure the ParticleEmitterComponent
func sparksComponent() -> ParticleEmitterComponent { ... }
```

### Apply the manipulable view modifier — [12:30]

```swift
struct RobotView: View {
  let url: URL
  var body: some View {
    HStack {
      NameSign()
      Model3D(url: url)
        .manipulable()
    }
  }
}
```

### Allow translate, 1- and 2-handed rotation, but not scaling — [12:33]

```swift
struct RobotView: View {
  let url: URL
  var body: some View {
    HStack {
      NameSign()
      Model3D(url: url)
        .manipulable(
          operations: [.translation,
                       .primaryRotation,
                       .secondaryRotation]
       )
    }
  }
}
```

### The model feels heavy with high inertia — [12:41]

```swift
struct RobotView: View {
  let url: URL
  var body: some View {
    HStack {
      NameSign()
      Model3D(url: url)
        .manipulable(inertia: .high)
    }
  }
}
```

### Add a ManipulationComponent to an entity​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [13:18]

```swift
RealityView { content in
  let sparky = await loadSparky()
  content.add(sparky)
  ManipulationComponent.configureEntity(sparky)
}
```

### Add a ManipulationComponent to an entity​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ with configuration — [13:52]

```swift
RealityView { content in
  let sparky = await loadSparky()
  content.add(sparky)
  ManipulationComponent.configureEntity(
    sparky,
    hoverEffect: .spotlight(.init(color: .purple)),
    allowedInputTypes: .all,
    collisionShapes: myCollisionShapes()
  )
}
```

### Manipulation interaction events — [14:08]

```swift
public enum ManipulationEvents {

  /// When an interaction is about to begin on a ManipulationComponent's entity
  public struct WillBegin: Event { }

  /// When an entity's transform was updated during a ManipulationComponent
  public struct DidUpdateTransform: Event { }

  /// When an entity was released
  public struct WillRelease: Event { }

  /// When the object has reached its destination and will no longer be updated
  public struct WillEnd: Event { }

  /// When the object is directly handed off from one hand to another
  public struct DidHandOff: Event { }
}
```

### Replace the standard sounds with custom ones — [14:32]

```swift
RealityView { content in
  let sparky = await loadSparky()
  content.add(sparky)

  var manipulation = ManipulationComponent()
  manipulation.audioConfiguration = .none
  sparky.components.set(manipulation)

  didHandOff = content.subscribe(to: ManipulationEvents.DidHandOff.self) { event in
    sparky.playAudio(handoffSound)
  }
}
```

### Builder based attachments — [16:19]

```swift
struct RealityViewAttachments: View {
  var body: some View {
    RealityView { content, attachments in
      let bolts = await loadAndSetupBolts()
      if let nameSign = attachments.entity(
        for: "name-sign"
      ) {
        content.add(nameSign)
        place(nameSign, above: bolts)
      }
      content.add(bolts)
    } attachments: {
      Attachment(id: "name-sign") {
        NameSign("Bolts")
      }
    }
    .realityViewLayoutBehavior(.centered)
  }
}
```

### Attachments created with ViewAttachmentComponent — [16:37]

```swift
struct AttachmentComponentAttachments: View {
  var body: some View {
    RealityView { content in
      let bolts = await loadAndSetupBolts()
      let attachment = ViewAttachmentComponent(
          rootView: NameSign("Bolts"))
      let nameSign = Entity(components: attachment)
      place(nameSign, above: bolts)
      content.add(bolts)
      content.add(nameSign)
    }
    .realityViewLayoutBehavior(.centered)
  }
}
```

### Targeted to entity gesture API — [17:04]

```swift
struct AttachmentComponentAttachments: View {
  @State private var bolts = Entity()
  @State private var nameSign = Entity()

  var body: some View {
    RealityView { ... }
    .realityViewLayoutBehavior(.centered)
    .gesture(
      TapGesture()
        .targetedToEntity(bolts)
        .onEnded { value in
          nameSign.isEnabled.toggle()
        }
    )
  }
}
```

### Gestures with GestureComponent — [17:10]

```swift
struct AttachmentComponentAttachments: View {
  var body: some View {
    RealityView { content in
      let bolts = await loadAndSetupBolts()
      let attachment = ViewAttachmentComponent(
          rootView: NameSign("Bolts"))
      let nameSign = Entity(components: attachment)
      place(nameSign, above: bolts)
      bolts.components.set(GestureComponent(
        TapGesture().onEnded {
          nameSign.isEnabled.toggle()
        }
      ))
      content.add(bolts)
      content.add(nameSign)
    }
    .realityViewLayoutBehavior(.centered)
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/274/4/af6a131e-f3ee-4d68-8371-4f52e9c4a3d6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/274/4/af6a131e-f3ee-4d68-8371-4f52e9c4a3d6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/274) — developer.apple.com. Indexed for agent consumption._