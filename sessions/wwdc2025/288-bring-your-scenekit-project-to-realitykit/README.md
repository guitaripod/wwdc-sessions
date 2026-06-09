---
id: "wwdc2025-288"
event: "wwdc2025"
year: 2025
title: "Bring your SceneKit project to RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/288"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Bring your SceneKit project to RealityKit

**Event:** WWDC25 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-288](https://developer.apple.com/videos/play/wwdc2025/288)

Understand SceneKit deprecation and explore how to transition your 3D projects to RealityKit, Apple’s recommended high-level 3D engine. We’ll clarify what SceneKit deprecation means for your projects, compare key concepts between the two engines, and show you how to port a sample SceneKit game to RealityKit. We’ll also explore the potential of RealityKit across all supported platforms to help you create amazing 3D experiences with your apps and games.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,162 words)

## Documentation & Resources

- [Bringing your SceneKit projects to RealityKit](https://developer.apple.com/documentation/RealityKit/bringing-your-scenekit-projects-to-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/bringing-your-scenekit-projects-to-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/bringing-your-scenekit-projects-to-realitykit.json

## Code Snippets

### Animations in RealityKit — [16:33]

```swift
// RealityKit
guard let max = scene.findEntity(named: "Max") else { return }

guard let library = max.components[AnimationLibraryComponent.self],
      let spinAnimation = library.animations["spin"]
else { return }

max.playAnimation(spinAnimation)
```

### Directional Light Component in RealityKit — [18:18]

```swift
// RealityKit

let lightEntity = Entity(components:
    DirectionalLightComponent(),
    DirectionalLightComponent.Shadow()
)
```

### Create Bloom effect using RealityKit Post processing API — [24:37]

```swift
final class BloomPostProcess: PostProcessEffect {

    let bloomThreshold: Float = 0.5
    let bloomBlurRadius: Float = 15.0

    func postProcess(context: borrowing PostProcessEffectContext<any MTLCommandBuffer>) {

        // Create metal texture of the same format as 'context.sourceColorTexture'.
        var bloomTexture = ...

        // Write brightest parts of 'context.sourceColorTexture' to 'bloomTexture'
        // using 'MPSImageThresholdToZero'.

        // Blur 'bloomTexture' in-place using 'MPSImageGaussianBlur'.

        // Combine original 'context.sourceColorTexture' and 'bloomTexture'
        // using 'MPSImageAdd', and write to 'context.targetColorTexture'.
    }
}

// RealityKit

content.renderingEffects.customPostProcessing = .effect(
    BloomPostProcess()
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/288/5/810e7d3c-54d7-43e5-82ba-d0f45b804193/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/288/5/810e7d3c-54d7-43e5-82ba-d0f45b804193/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/288) — developer.apple.com. Indexed for agent consumption._
