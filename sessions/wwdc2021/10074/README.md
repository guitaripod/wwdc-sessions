---
id: "wwdc2021-10074"
event: "wwdc2021"
year: 2021
title: "Dive into RealityKit 2"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10074"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Dive into RealityKit 2

**Event:** WWDC21 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10074](https://developer.apple.com/videos/play/wwdc2021/10074)

Creating engaging AR experiences has never been easier with RealityKit 2. Explore the latest enhancements to the RealityKit framework and take a deep dive into this underwater sample project. We’ll take you through the improved Entity Component System, streamlined animation pipeline, and the plug-and-play character controller with enhancements to face mesh and audio.

**Keywords:** `3d graphics`, `ar`, `arkit`, `augmented reality`, `lidar`, `physics`, `realitykit`, `scenekit`, `usdz`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,086 words)

## Documentation & Resources

- [Creating an App for Face-Painting in AR](https://developer.apple.com/documentation/RealityKit/creating-an-app-for-face-painting-in-ar) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-an-app-for-face-painting-in-ar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-an-app-for-face-painting-in-ar.json
- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/RealityKit/building-an-immersive-experience-with-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/building-an-immersive-experience-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/building-an-immersive-experience-with-realitykit.json
- [Applying realistic material and lighting effects to entities](https://developer.apple.com/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/applying-realistic-material-and-lighting-effects-to-entities.json
- [PhysicallyBasedMaterial](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/PhysicallyBasedMaterial
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/PhysicallyBasedMaterial.json
- [Explore the RealityKit Developer Forums](https://developer.apple.com/forums/tags/realitykit) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/realitykit
- [Creating a fog effect using scene depth](https://developer.apple.com/documentation/ARKit/creating-a-fog-effect-using-scene-depth) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/creating-a-fog-effect-using-scene-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/creating-a-fog-effect-using-scene-depth.json
- [RealityKit](https://developer.apple.com/documentation/RealityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit.json

## Code Snippets

### FlockingSystem — [7:10]

```swift
class FlockingSystem: RealityKit.System {

required init(scene: RealityKit.Scene) { }

static var dependencies: [SystemDependency] { [.before(MotionSystem.self)] }

private static let query = EntityQuery(where: .has(FlockingComponent.self)
                                            && .has(MotionComponent.self)
                                            && .has(SettingsComponent.self))
```

### FlockingSystem.update — [8:34]

```swift
func update(context: SceneUpdateContext) {

    context.scene.performQuery(Self.query).forEach { entity in

        guard var motion: MotionComponent = entity.components[MotionComponent.self]
            else { continue }

        // ... Using a Boids simulation, add forces to the MotionComponent
        motion.forces.append(/* separation, cohesion, alignment forces */)

        entity.components[MotionComponent.self] = motion
    }
}
```

### Store Subscription While Entity Active — [11:58]

```swift
arView.scene.subscribe(to: CollisionEvents.Began.self, on: fish) { [weak self] event in
    // ... handle collisions with this particular fish
}.storeWhileEntityActive(fish)
```

### SwiftUI + RealityKit Settings Instance — [12:36]

```swift
class Settings: ObservableObject {
    @Published var separationWeight: Float = 1.6
    // ...
}

struct ContentView : View {
    @StateObject var settings = Settings()
    var body: some View { 
        ZStack {
            ARViewContainer(settings: settings) 
            MovementSettingsView()
              .environmentObject(settings)
        }
    }
} 





struct SettingsComponent: RealityKit.Component {
    var settings: Settings
}

class UnderwaterView: ARView {
    let settings: Settings
    private func addEntity(_ entity: Entity) {
        entity.components[SettingsComponent.self] = 
          SettingsComponent(settings: self.settings)
    }
}
```

### FaceMesh — [21:26]

```swift
static let sceneUnderstandingQuery = 
    EntityQuery(where: .has(SceneUnderstandingComponent.self) && .has(ModelComponent.self))

func findFaceEntity(scene: RealityKit.Scene) -> HasModel? {
    let faceEntity = scene.performQuery(sceneUnderstandingQuery).first {
        $0.components[SceneUnderstandingComponent.self]?.entityType == .face
    }
    return faceEntity as? HasModel
}
```

### FaceMesh - Painting material — [22:03]

```swift
func updateFaceEntityTextureUsing(cgImage: CGImage) {
  guard let faceEntity = self.faceEntity else { return }
  guard let faceTexture =
  try? TextureResource.generate(from: cgImage,
                                options: .init(semantic: .color))
  else { return }

  var faceMaterial = PhysicallyBasedMaterial()        
  faceMaterial.roughness = 0.1
  faceMaterial.metallic = 1.0
  faceMaterial.blending = .transparent(opacity: .init(scale: 1.0))

  let sparklyNormalMap = try! TextureResource.load(named: "sparkly")
  faceMaterial.normal.texture = PhysicallyBasedMaterial.Texture.init(sparklyNormalMap)

  faceMaterial.baseColor.texture = PhysicallyBasedMaterial.Texture.init(faceTexture)

  faceEntity.model!.materials = [faceMaterial]
}
```

### AudioBufferResource — [23:09]

```swift
let synthesizer = AVSpeechSynthesizer()

func speakText(_ text: String, forEntity entity: Entity) {

    let utterance = AVSpeechUtterance(string: text)
    utterance.voice = AVSpeechSynthesisVoice(language: "en-IE")

    synthesizer.write(utterance) { audioBuffer in

        guard
            let audioResource = try? AudioBufferResource(buffer: audioBuffer,
                                                         inputMode: .spatial,
                                                         shouldLoop: true)
        else { return }

        entity.playAudio(audioResource)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10074/4/67629E8A-3351-47A6-941D-B3C60B778BAF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10074/4/67629E8A-3351-47A6-941D-B3C60B778BAF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10074) — developer.apple.com. Indexed for agent consumption._