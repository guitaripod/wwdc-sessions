# Explore advances in RealityKit

**Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-279](https://developer.apple.com/videos/play/wwdc2026/279)

Discover the latest advancements in RealityKit designed to make your apps and games more immersive and realistic than ever. Explore powerful new capabilities including interactive cloth simulations, NavMesh pathfinding, mixed reality lighting, and customizable reverb meshes for enhanced spatial audio. Elevate your visual fidelity with improved shadows, character rendering enhancements, and support for Gaussian splatting.

**Keywords:** `3d content`, `games`, `gaussian splatting`, `reality composer pro`, `realitykit`, `realitykit audio`, `spatial computing`, `visionos`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Gaussian splats on visionOS](https://developer.apple.com/documentation/visionOS/gaussian-splats-on-visionos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/gaussian-splats-on-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/gaussian-splats-on-visionos.json

## Code Snippets

### Soft shadows — [4:02]

```swift
// Enable soft shadows for the hearth spotlight

guard var shadow = hearthSpotlight.components[SpotLightComponent.Shadow.self] else {
    // handle error
}
shadow.lightSize = 0.7 // meters

shadow.quality = .medium // or .high
// shadow.quality = .low // will result in hard shadows

hearthSpotlight.components.set(shadow)
```

### Projective textures — [6:13]

```swift
// Create one of the planetarium spotlights

let spotLightEntity = Entity()
spotLightEntity.components.set(SpotLightComponent(
    color: .white,
    intensity: intensity,
    innerAngleInDegrees: innerAngle,
    outerAngleInDegrees: outerAngle,
    attenuationRadius: attenuationRadius,
))

let projectiveTexture: TextureResource = generateStarsAndNebulaeTexture()
spotLightEntity.components.set(SpotLightComponent.ProjectiveTexture(
    texture: projectiveTexture
))
```

### Physical space lighting — [7:13]

```swift
// Enable physical space lighting

spotLightEntity.components.set(SpotLightComponent.SurroundingsLight())
```

### Querying the navigation mesh — [9:46]

```swift
// Querying the navigation mesh in Chaparral Village

extension Entity {
    public func navigate(/* ... */) async {
        let navigator = try! NavigationController(entity: self)
        guard let result = await navigator.computePath(from: fromPosition, to: toPosition) 
        else {
            return
        }
        if result.isEmpty {
            return
        }
        for node in result {
            switch node.category {
                case .meshPoint:
                    finalPath.append(node.position)
                case .offMeshConnection:
                    // handle ladders
            }
        }
    }
}
```

### Pinning cloth to anchor points — [12:51]

```swift
// Pin the curtains to the Alchemist's lab

for (pin, pinComponent) in pins {
        let position = pin.position(relativeTo: event.entity)
        let selectionSphere = ClothSphereShape(radius: pinComponent.radius)

        let vertices = clothMesh.vertices(in: .sphere(selectionSphere),
                                    center: position)
        clothBody.motionTypes.set(vertexIndices: vertices, value: .kinematic)
}
```

### LOD by camera distance — [14:42]

```swift
// Create entity with LODs

let lod0 = [ModelEntity(mesh: lodMesh0)]
let lod1 = [ModelEntity(mesh: lodMesh1)]
let lod2 = [ModelEntity(mesh: lodMesh2)]

let entity = Entity()

LevelOfDetailComponent.addByCameraDistance(to: entity, levels: [
    (entities: lod0, maxDistance: 1.0 /* meters */), // highest detail
    (entities: lod1, maxDistance: 5.0),              // medium detail
    (entities: lod2, maxDistance: .infinity),        // lowest detail
])
```

### LOD by screen area — [15:58]

```swift
// Create entity with LODs

let lod0 = [ModelEntity(mesh: lodMesh0)]
let lod1 = [ModelEntity(mesh: lodMesh1)]
let lod2 = [ModelEntity(mesh: lodMesh2)]

let entity = Entity()

LevelOfDetailComponent.addByScreenArea(to: entity, levels: [
    (entities: lod0, minArea: 0.2 /* fraction of screen area */),  // highest detail
    (entities: lod1, minArea: 0.1),                                // medium detail
    (entities: lod2, minArea: 0.01),                               // lowest detail
])
```

### Responding to thermal state changes — [16:26]

```swift
// Respond to changes in device thermal state

NotificationCenter.default.addObserver(of: ProcessInfo.self,
                                       for: .thermalStateDidChange) {_ in
    switch ProcessInfo.processInfo.thermalState {
        case .nominal, .fair:
            // Stay the course
        case .serious, .critical:
            // Improve performance by:
            // More aggressive LOD switching
            // Lower shadow quality
    }
}
```

### Creating a Gaussian splat — [18:44]

```swift
// Create Gaussian splat resource and component

let resource = try GaussianSplatResource.BufferResource(count: splatCount,
                                                        position: positionBuffer,
                                                        scale: scaleBuffer,
                                                        rotation: rotationBuffer,
                                                        opacity: opacityBuffer,
                                                        sphericalHarmonics:
                                                                                                                    (sphericalHarmonicsBuffer, degree))

let splatResource = GaussianSplatResource(resource)

let splatComponent = GaussianSplatComponent(splatResource)

splatEntity.components.set(splatComponent)
```

### Creating a custom reverb mesh — [20:49]

```swift
// Create and use custom reverb mesh

let mesh: ReverbMeshResource = .shoebox(size: [5, 4, 6])

let reverb: Reverb = .simulated(mesh: mesh, materials: [.dryWall])

entity.components.set(ReverbComponent(reverb: reverb))
```

### Creating custom reverb materials — [21:33]

```swift
// Create custom materials for custom reverb mesh

let thickCarpet: Audio.Material = .carpet.scalingAbsorption {freq in 0.1 }

let bookshelf: Audio.Material

// Absorption coefficients by center frequency:
// 31.5Hz, 63Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz, 8kHz, 16kHz
let bookshelfAbsorption = Audio.Absorption(
    [0.10, 0.15, 0.28, 0.20, 0.15, 0.10, 0.10, 0.07, 0.07, 0.05])

// Scattering coefficients for: 500Hz, 1000Hz, 4000Hz
let bookshelfScattering = Audio.Scattering([500: 0.5, 1000: 0.6, 4000: 0.7])

bookshelf = .init(absorption: bookshelfAbsorption,
              scattering: bookshelfScattering)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/279/4/ab575725-be7d-4348-a3ae-6595ef4070c4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/279/4/ab575725-be7d-4348-a3ae-6595ef4070c4/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._