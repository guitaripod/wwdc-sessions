---
id: "wwdc2026-284"
event: "wwdc2026"
year: 2026
title: "Collaborate on structured 3D models in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/284"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Collaborate on structured 3D models in visionOS

**Event:** WWDC26 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-284](https://developer.apple.com/videos/play/wwdc2026/284)

Learn how to bring structured 3D models to life in visionOS. We’ll cover USDZ preparation, show you how to manipulate individual entities within hierarchical assemblies, and inspect the internal components within a model with a cross-sectional plane. Create stunning exploded-view animations for design review and collaboration experiences on Apple Vision Pro.

**Keywords:** `3d`, `3d content`, `3d model`, `design`, `hierarchical`, `hierarchy`, `review`, `shareplay`, `spatial computing`, `visionos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,040 words)

## Documentation & Resources

- [Manipulating models with RealityKit](https://developer.apple.com/documentation/RealityKit/manipulating-models-with-realitykit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/manipulating-models-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/manipulating-models-with-realitykit.json

## Code Snippets

### Opening an assembly — [7:10]

```swift
func openAssembly() {
    components[ManipulationComponent.self] = nil
    components[InputTargetComponent.self] = nil

    for child in assemblyChildren {
        child.components.set(InputTargetComponent())

        var manipulation = ManipulationComponent()
        manipulation.releaseBehavior = .stay
        child.manipulationComponent = manipulation
    }
}
```

### Closing an assembly — [7:11]

```swift
func closeAssembly() {
    for child in assemblyChildren {
        child.manipulationComponent = nil
        child.components[InputTargetComponent.self] = nil
    }

    components.set(InputTargetComponent())
    var manipulation = ManipulationComponent()
    manipulation.releaseBehavior = .stay
    manipulationComponent = manipulation
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/284/4/fa1d15b1-3f28-415a-907a-8ae1bb344494/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/284/4/fa1d15b1-3f28-415a-907a-8ae1bb344494/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/284) — developer.apple.com. Indexed for agent consumption._