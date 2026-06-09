---
id: "wwdc2023-10080"
event: "wwdc2023"
year: 2023
title: "Build spatial experiences with RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10080"
topics: ["Essentials", "Spatial Computing"]
platforms: ["iOS", "visionOS"]
hasTranscript: true
---

# Build spatial experiences with RealityKit

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** iOS, visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10080](https://developer.apple.com/videos/play/wwdc2023/10080)

Discover how RealityKit can bring your apps into a new dimension. Get started with RealityKit entities, components, and systems, and learn how you can add 3D models and effects to your app on visionOS. We’ll also take you through the RealityView API and demonstrate how to add 3D objects to windows, volumes, and spaces to make your apps more immersive. And we’ll explore combining RealityKit with spatial input, animation, and spatial audio.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,937 words)

## Documentation & Resources

- [Hello World](https://developer.apple.com/documentation/visionOS/World) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/World
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/World.json

## Code Snippets

### Model3D — [3:40]

```swift
import SwiftUI
import RealityKit

struct GlobeModule: View {
    var body: some View {
        Model3D(named: "Globe") { model in
            model
                .resizable()
                .scaledToFit()
        } placeholder: {
          	ProgressView()
        }
    }
}
```

### Volumetric window — [5:52]

```swift
import SwiftUI
import RealityKit

// Define a volumetric window.
struct WorldApp: App {
    var body: some SwiftUI.Scene {
        // ...

        WindowGroup(id: "planet-earth") {
            Model3D(named: "Globe")
        }
        .windowStyle(.volumetric)
        .defaultSize(width: 0.8, height: 0.8, depth: 0.8, in: .meters)
    }
}
```

### ImmersiveSpace — [7:31]

```swift
import SwiftUI
import RealityKit

// Define a immersive space.
struct WorldApp: App {
    var body: some SwiftUI.Scene {
        // ...

        ImmersiveSpace(id: "objects-in-orbit") {
            RealityView { content in
                // ...
            }
        }
    }
}
```

### RealityView — [12:40]

```swift
import SwiftUI
import RealityKit

struct Orbit: View {
    let earth: Entity

    var body: some View {
        RealityView { content in
            content.add(earth)
        }
    }
}
```

### RealityView asynchronous loading and entity positioning — [12:54]

```swift
import SwiftUI
import RealityKit

struct Orbit: View {
    var body: some View {
        RealityView { content in
            async let earth = ModelEntity(named: "Earth")
            async let moon = ModelEntity(named: "Moon")

            if let earth = try? await earth, let moon = try? await moon {
                content.add(earth)
                content.add(moon)
                moon.position = [0.5, 0, 0]
            }
        }
    }
}
```

### Earth rotation — [13:54]

```swift
import SwiftUI
import RealityKit

struct RotatedModel: View {
    var entity: Entity
    var rotation: Rotation3D

    var body: some View {
        RealityView { content in
            content.add(entity)
        } update: { content in
            entity.orientation = .init(rotation)
        }
   }
}
```

### Converting co-ordinate spaces — [14:27]

```swift
import SwiftUI
import RealityKit

struct ResizableModel: View {
    var body: some View {
        GeometryReader3D { geometry in
            RealityView { content in
                if let earth = try? await ModelEntity(named: "Earth") {
                    let bounds = content.convert(geometry.frame(in: .local),
                                                 from: .local, to: content)
                    let minExtent = bounds.extents.min()
                    earth.scale = [minExtent, minExtent, minExtent]
                }
            }
        }
    }
}
```

### Play an animation — [14:56]

```swift
import SwiftUI
import RealityKit

struct AnimatedModel: View {
    @State var subscription: EventSubscription? 

    var body: some View {
        RealityView { content in
            if let moon = try? await Entity(named: "Moon"),
               let animation = moon.availableAnimations.first {
                moon.playAnimation(animation)
                content.add(moon)
            }
            subscription = content.subscribe(to: AnimationEvents.PlaybackCompleted.self) {
                // ...
            }
       }
   }
}
```

### Adding a drag gesture — [18:31]

```swift
import SwiftUI
import RealityKit

struct DraggableModel: View {
    var earth: Entity

    var body: some View {
        RealityView { content in
            content.add(earth)
        }
        .gesture(DragGesture()
            .targetedToEntity(earth)
            .onChanged { value in
                earth.position = value.convert(value.location3D,
                                               from: .local, to: earth.parent!)
            })
    }
}
```

### Playing a transform animation — [20:20]

```swift
// Playing a transform animation
let orbit = OrbitAnimation(name: "Orbit",
                           duration: 30,
                           axis: [0, 1, 0],
                           startTransform: moon.transform,
                           bindTarget: .transform,
                           repeatMode: .repeat)

if let animation = try? AnimationResource.generate(with: orbit) {
    moon.playAnimation(animation)
}
```

### Adding audio — [22:12]

```swift
// Create an empty entity to act as an audio source.
let audioSource = Entity()

// Configure the audio source to project sound out in a tight beam.
audioSource.spatialAudio = SpatialAudioComponent(directivity: .beam(focus: 0.75))

// Change the orientation of the audio source (rotate 180º around the Y axis).
audioSource.orientation = .init(angle: .pi, axis: [0, 1, 0])

// Add the audio source to a parent entity, and play a looping sound on it.
if let audio = try? await AudioFileResource(named: "SatelliteLoop",
                                            configuration: .init(shouldLoop: true)) {
    satellite.addChild(audioSource)
    audioSource.playAudio(audio)
}
```

### Defining a custom component — [23:47]

```swift
import RealityKit

// Components are data attached to an Entity.
struct TraceComponent: Component {
    var mesh = TraceMesh()
}

// Entities contain components, identified by the component’s type.
func updateTrace(for entity: Entity) {
    var component = entity.components[TraceComponent.self] ?? TraceComponent()
    component.update()
    entity.components[TraceComponent.self] = component
}

// Codable components can be added to entities in Reality Composer Pro.
struct PointOfInterestComponent: Component, Codable {
    var name = ""
}
```

### Defining a system — [24:51]

```swift
import SwiftUI
import RealityKit

// Systems supply logic and behavior.
struct TraceSystem: System {
    static let query = EntityQuery(where: .has(TraceComponent.self))

    init(scene: Scene) {
        // ...
    }

    func update(context: SceneUpdateContext) {
         // Systems often act on all entities matching certain conditions.
        for entity in context.entities(Self.query, updatingSystemWhen: .rendering) {
            addCurrentPositionToTrace(entity)
        }
    }
}

// Systems run on all RealityKit content in your app once registered.
struct MyApp: App {
    init() {
        TraceSystem.registerSystem()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10080/4/285DEB34-9EE6-466F-8F33-BF04E334E215/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10080/4/285DEB34-9EE6-466F-8F33-BF04E334E215/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10080) — developer.apple.com. Indexed for agent consumption._
