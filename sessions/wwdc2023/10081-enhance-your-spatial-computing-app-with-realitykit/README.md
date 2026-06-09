---
id: "wwdc2023-10081"
event: "wwdc2023"
year: 2023
title: "Enhance your spatial computing app with RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10081"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "visionOS"]
hasTranscript: true
---

# Enhance your spatial computing app with RealityKit

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** iOS, visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10081](https://developer.apple.com/videos/play/wwdc2023/10081)

Go beyond the window and learn how you can bring engaging and immersive 3D content to your apps with RealityKit. Discover how SwiftUI scenes work in tandem with RealityView and how you can embed your content into an entity hierarchy. We’ll also explore how you can blend virtual content and the real world using anchors, bring particle effects into your apps, add video content, and create more immersive experiences with portals.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,863 words)

## Documentation & Resources

- [Diorama](https://developer.apple.com/documentation/visionOS/diorama) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/diorama
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/diorama.json

## Code Snippets

### Attachments — [2:30]

```swift
import SwiftUI
import RealityKit

struct MoonOrbit: View {
    var body: some View {
        RealityView { content, attachments in
            guard let earth = try? await Entity(named: "Earth") else {
                return
            }
            content.add(earth)

            if let earthAttachment = attachments.entity(for: "earth_label") {
                earthAttachment.position = [0, -0.15, 0]
                earth.addChild(earthAttachment)
            }
        } attachments: {
            Attachment(id: "earth_label") {
                Text("Earth")
            }
        }
    }
}
```

### VideoPlayerComponent — [8:03]

```swift
public func makeVideoEntity() -> Entity {
    let entity = Entity()

    let asset = AVURLAsset(url: Bundle.main.url(forResource: "tides_video",
                                                withExtension: "mp4")!)
    let playerItem = AVPlayerItem(asset: asset)

    let player = AVPlayer()
    entity.components[VideoPlayerComponent.self] = .init(avPlayer: player)

    entity.scale *= 0.4

    player.replaceCurrentItem(with: playerItem)
    player.play()

    return entity
}
```

### Passthrough tinting — [10:05]

```swift
var videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
    videoPlayerComponent.isPassthroughTintingEnabled = true

    entity.components[VideoPlayerComponent.self] = videoPlayerComponent
```

### VideoPlayerEvents — [10:40]

```swift
content.subscribe(to: VideoPlayerEvents.VideoSizeDidChange.self,
                      on: entity) { event in
        // ...
    }
```

### Portal — [13:12]

```swift
struct PortalView : View {
    var body: some View {
        RealityView { content in
            let world = makeWorld()
            let portal = makePortal(world: world)

            content.add(world)
            content.add(portal)
        }
    }
}

public func makeWorld() -> Entity {
    let world = Entity()
    world.components[WorldComponent.self] = .init()

    let environment = try! EnvironmentResource.load(named: "SolarSystem")
    world.components[ImageBasedLightComponent.self] = .init(source: .single(environment),
                                                            intensityExponent: 6)
    world.components[ImageBasedLightReceiverComponent.self] = .init(imageBasedLight: world)

    let earth = try! Entity.load(named: "Earth")
    let moon = try! Entity.load(named: "Moon")
    let sky = try! Entity.load(named: "OuterSpace")
    world.addChild(earth)
    world.addChild(moon)
    world.addChild(sky)

    return world
}

public func makePortal(world: Entity) -> Entity {
    let portal = Entity()

    portal.components[ModelComponent.self] = .init(mesh: .generatePlane(width: 1,
                                                                        height: 1,
                                                                        cornerRadius: 0.5),
                                                   materials: [PortalMaterial()])
    portal.components[PortalComponent.self] = .init(target: world)

    return portal
}
```

### Adding particles around the portal — [15:50]

```swift
public class ParticleTransitionSystem: System {
    private static let query = EntityQuery(where: .has(ParticleEmitterComponent.self))

    public func update(context: SceneUpdateContext) {
        let entities = context.scene.performQuery(Self.query)
        for entity in entities {
            updateParticles(entity: entity)
        }
    }
}

public func updateParticles(entity: Entity) {
    guard var particle = entity.components[ParticleEmitterComponent.self] else {
        return
    }

    let scale = max(entity.scale(relativeTo: nil).x, 0.3)

    let vortexStrength: Float = 2.0
    let lifeSpan: Float = 1.0
    particle.mainEmitter.vortexStrength = scale * vortexStrength
    particle.mainEmitter.lifeSpan = Double(scale * lifeSpan)

    entity.components[ParticleEmitterComponent.self] = particle
}
```

### Anchoring the portal — [18:19]

```swift
import SwiftUI
import RealityKit

struct PortalApp: App {

    @State private var immersionStyle: ImmersionStyle = .mixed

    var body: some SwiftUI.Scene {
        ImmersiveSpace {
            RealityView { content in
                let anchor = AnchorEntity(.plane(.vertical, classification: .wall,
                                                 minimumBounds: [1, 1]))
                content.add(anchor)

                anchor.addChild(makePortal())
            }
        }
        .immersionStyle(selection: $immersionStyle, in: .mixed)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10081/4/218C691E-8111-4A1A-925F-F43AB9832C41/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10081/4/218C691E-8111-4A1A-925F-F43AB9832C41/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10081) — developer.apple.com. Indexed for agent consumption._
