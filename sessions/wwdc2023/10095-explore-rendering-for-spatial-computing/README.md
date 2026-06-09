---
id: "wwdc2023-10095"
event: "wwdc2023"
year: 2023
title: "Explore rendering for spatial computing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10095"
topics: ["Spatial Computing"]
platforms: ["iOS", "visionOS"]
hasTranscript: true
---

# Explore rendering for spatial computing

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** iOS, visionOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10095](https://developer.apple.com/videos/play/wwdc2023/10095)

Find out how you can take control of RealityKit rendering to improve the look and feel of your apps and games on visionOS. Discover how you can customize lighting, add grounding shadows, and control tone mapping for your content. We’ll also go over best practices for two key treatments on the platform: rasterization rate maps and dynamic content scaling.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,332 words)

## Documentation & Resources

- [Rendering at different rasterization rates](https://developer.apple.com/documentation/Metal/rendering-at-different-rasterization-rates) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-at-different-rasterization-rates
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-at-different-rasterization-rates.json

## Code Snippets

### Image based lighting — [3:05]

```swift
RealityView { content in
    async let satellite = Entity(named: "Satellite", in: worldAssetsBundle)
    async let environment = EnvironmentResource(named: "Sunlight")

    if let satellite = try? await satellite, let environment = try? await environment {
        content.add(satellite)

        satellite.components.set(ImageBasedLightComponent(
           source: .single(environment)))

        satellite.components.set(ImageBasedLightReceiverComponent(
           imageBasedLight: satellite))
   }
}
```

### Grounding shadows — [4:28]

```swift
RealityView { content in
    if let vase = try? await Entity(named: "flower_tulip") {
        content.add(vase)

        vase.components.set(GroundingShadowComponent(castsShadow: true))
    }
}
```

### Disable tone mapping — [8:48]

```swift
RealityView { content in
    if let trafficLight = try? await Entity(named: "traffic_light") {
        content.add(trafficLight)

        if let lamp = trafficLight.findEntity(named: "red_light") {
            if var model = lamp.components[ModelComponent.self] {
                let material = UnlitMaterial(color: .init(color), 
                                             applyPostProcessToneMap: false)

                model.materials = [material]

                lamp.components[ModelComponent.self] = model
            }
        }
    }
}
```

### Dynamic content scaling — [15:34]

```swift
// Enable dynamic content scaling on CALayer with:

var wantsDynamicContentScaling: Bool { get set }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10095/4/CCE7B88E-E0C4-4BA3-87E7-9C1D644FA6CB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10095/4/CCE7B88E-E0C4-4BA3-87E7-9C1D644FA6CB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10095) — developer.apple.com. Indexed for agent consumption._
