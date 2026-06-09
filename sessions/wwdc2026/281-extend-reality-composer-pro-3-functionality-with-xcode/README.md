---
id: "wwdc2026-281"
event: "wwdc2026"
year: 2026
title: "Extend Reality Composer Pro 3 functionality with Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/281"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Extend Reality Composer Pro 3 functionality with Xcode

**Event:** WWDC26 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-281](https://developer.apple.com/videos/play/wwdc2026/281)

Discover how Reality Composer Pro 3 empowers you to build bigger, more ambitious spatial projects. Learn about creating project-specific plugins that let you edit custom components, run custom systems, and build your own ScriptGraph nodes—giving you complete control over your spatial authoring workflow.

**Keywords:** `3d`, `game`, `plugin`, `reality composer pro`, `realitykit`, `scene`, `scripting`, `spatial computing`, `swift`, `visionos`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,056 words)

## Code Snippets

### Cauldron component — [6:08]

```swift
// Add a component to represent the water level

import RealityKit

public struct Cauldron: Component, Codable {
    public var waterLevel: Float

    enum CodingKeys: CodingKey {
        case waterLevel
    }
}
```

### CauldronSystem — [6:42]

```swift
// Add a system to control the water level

import RealityKit

public struct CauldronSystem: System {
    let query = EntityComponentQuery(Cauldron.self)
    public init(scene: Scene) {}

    public func update(context: SceneUpdateContext) {
        for (entity, cauldron) in context.entities(matching: query) {
            guard let water = entity.findEntity(named: "Cauldron_Water_mesh")
                else { continue }
            water.setPosition(SIMD3<Float>(0, 1, 0) * cauldron.waterLevel, relativeTo: entity)
        }
    }
}
```

### RCPCustomComponentsPlugin — [7:00]

```swift
// Make sure that Reality Composer Pro 3 knows about the Cauldron and CauldronSystem

import RealityComposerPro

final class RCPCustomComponentsPlugin: RealityComposerProPlugin {
    public func setup(context: any RealityComposerProContext) {
        context.registerComponent(Cauldron.self)
        context.registerSystem(CauldronSystem.self)
    }
}

@_cdecl("createRealityComposerProPlugin")
public func createRealityComposerProPlugin() -> UnsafeMutableRawPointer {
    return RCPCustomComponentsPlugin().passRetained()
}
```

### Cauldron component with vortex properties — [10:49]

```swift
// Properties to control water surface

import RealityKit

public struct Cauldron: Component, Codable {
    public var waterLevel: Float
    public var rotationSpeed: Float
    public var minWaterLevel: Float
    public var maxWaterLevel: Float
    public var vortexCoeff: Float
}
```

### CauldronSystem update with ShaderGraph — [11:05]

```swift
public func update(context: SceneUpdateContext) {
    for (entity, cauldron) in context.entities(matching: query) {
        guard let water = entity.findEntity(named: "Cauldron_Water_mesh") else { continue }
        water.setPosition(SIMD3<Float>(0, 1, 0) * cauldron.waterLevel, relativeTo: entity)

        guard var model = water.components[ModelComponent.self] else { continue }
        guard var mat = model.materials.first as? ShaderGraphMaterial else { continue }
        let surface = computeSurface(cauldron: cauldron)
        try? mat.setParameter(name: "Level Radius", value: .float(surface.levelRadius))
        try? mat.setParameter(name: "Lowest Point",
            value: .float(cauldron.waterLevel - surface.lowestPoint))
        try? mat.setParameter(name: "Height Change", value: .float(surface.heightChange))
        try? mat.setParameter(name: "Level Coeff", value: .float(surface.levelCoeff))
        try? mat.setParameter(name: "Is Level", value: .bool(surface.isLevel))
        model.materials[0] = mat
        water.components.set(model)
    }
}
```

### SetWaterLevelAction — [13:25]

```swift
// Custom action for setting the water level of the Cauldron

import RealityKit

public struct SetWaterLevelAction: EntityAction, Codable {
    // Parameters for the action
    public let startWaterLevel: Float
    public let endWaterLevel: Float

    // Required by EntityAction protocol
    public var animatedValueType: (any AnimatableData.Type)? { Transform.self }
}
```

### SetWaterLevelAction subscribe — [14:05]

```swift
extension SetWaterLevelAction {
    static func subscribe() {
        Task { @MainActor in
            SetWaterLevelAction.subscribe(to: .updated) { event in
                let normalizedTime = (event.playbackController.time - event.startTime) /
                    event.duration
                let action = event.action
                let currentLevel = action.startWaterLevel +
                    Float(normalizedTime) * (action.endWaterLevel - action.startWaterLevel)
                guard let entity = event.targetEntity else { return }
                guard var cauldron = entity.components[Cauldron.self] else { return }
                cauldron.waterLevel = currentLevel
                entity.components.set(cauldron)
            }
        }
    }
}
```

### RCPCustomComponentsPlugin with action — [14:56]

```swift
// Make sure that Reality Composer Pro 3 knows about the SetWaterLevelAction

import RealityComposerPro

final class RCPCustomComponentsPlugin: RealityComposerProPlugin {
    public func setup(context: any RealityComposerProContext) {
        context.registerComponent(Cauldron.self)
        context.registerSystem(CauldronSystem.self)

        context.registerAction(SetWaterLevelAction.self)
        SetWaterLevelAction.subscribe()
    }
}

@_cdecl("createRealityComposerProPlugin")
public func createRealityComposerProPlugin() -> UnsafeMutableRawPointer {
    return RCPCustomComponentsPlugin().passRetained()
}
```

### Cauldron with @Scriptable macro — [17:32]

```swift
// Expose Cauldron to Script Graphs

import RealityKit
import RealityKitScripting
import RealityKitScriptingMacros

@Scriptable
public struct Cauldron: Component, Codable {
    public var waterLevel: Float
    public var rotationSpeed: Float
    public var minWaterLevel: Float
    public var maxWaterLevel: Float
    public var vortexCoeff: Float
}
```

### Register scripting module — [18:08]

```swift
// Register scripting module

public func setup(context: any RealityComposerProContext) {
    context.registerComponent(Cauldron.self)
    context.registerSystem(CauldronSystem.self)

    context.registerAction(SetWaterLevelAction.self)
    SetWaterLevelAction.subscribe()

    Task { @MainActor in
        let config = RKS.Configuration(id: "ChaparralVillage")
            .onInitialize { _ in
            [
                Module("ChaparralVillage") {
                    Cauldron.SchemaProvider.schema
                }
            ]
        }
        try! RKS.addConfiguration(config)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/281/6/1aef704f-ccc6-4c1d-b7b7-94da42d29609/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/281/6/1aef704f-ccc6-4c1d-b7b7-94da42d29609/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/281) — developer.apple.com. Indexed for agent consumption._
