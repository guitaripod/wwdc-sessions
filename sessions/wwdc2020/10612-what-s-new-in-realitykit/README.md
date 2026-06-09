---
id: "wwdc2020-10612"
event: "wwdc2020"
year: 2020
title: "What's new in RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10612"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in RealityKit

**Event:** WWDC20 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10612](https://developer.apple.com/videos/play/wwdc2020/10612)

RealityKit is Apple’s rendering, animation, physics, and audio engine built from the ground up for augmented reality: It reimagines the traditional 3D renderer to make it easy for developers to prototype and produce high-quality AR experiences. Learn how to effectively implement each of the latest improvements to RealityKit in your app. Discover features like video textures, scene understanding using the LiDAR scanner on iPad Pro, Location Anchors, face tracking, and improved debugging tools. To get the most out of this session, you should understand the building blocks of developing RealityKit-based apps and games. Watch “Introducing RealityKit and Reality Composer” for a primer. For more on how you can integrate Reality Composer into your augmented reality workflow, watch "The artist’s AR toolkit".

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,875 words)

## Documentation & Resources

- [Creating a game with scene understanding](https://developer.apple.com/documentation/RealityKit/creating-a-game-with-scene-understanding) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-a-game-with-scene-understanding
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-a-game-with-scene-understanding.json
- [RealityKit](https://developer.apple.com/documentation/RealityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit.json

## Code Snippets

### Loading a video material — [4:52]

```swift
// Use AVFoundation to load a video
let asset = AVURLAsset(url: Bundle.main.url(forResource: "glow", withExtension: "mp4")!)
let playerItem = AVPlayerItem(asset: asset)

// Create a Material and assign it to your model entity...
let player = AVPlayer()
bugEntity.materials = [VideoMaterial(player: player)]

// Tell the player to load and play
player.replaceCurrentItem(with: playerItem)
player.play()
```

### Implementing object avoidance with scene understanding — [13:58]

```swift
// Get the position and forward direction of the bug in world space
let bugOrigin = bug.position(relativeTo: nil)
let bugForward = bug.convert(direction: [0, 0, 1], relativeTo: nil)

// Perform a raycast 
let collisionResults = arView.scene.raycast(origin: bugOrigin, direction: bugForward)

// Get all hits against a Scene Understanding Entity
let filteredResults = collisionResults.filter { $0.entity as? HasSceneUnderstanding }

// Pick the closest one and get the collision point
guard let closestCollisionPoint = filteredResults.first?.position else {
	return
}

if length(bugOrigin - closestCollisionPoint) < safeDistance {
  // Avoid obstacle too close to object’s forward
}
```

### Using collision events with a scene understanding entity — [14:48]

```swift
// Subscribe to all collision events
arView.scene.subscribe(to: CollisionEvents.Began.self) { event in
    // Get any entity if it conforms to HasSceneUnderstanding
    guard let sceneUnderstandingEntity = (event.entityA as? HasSceneUnderstanding) 
                                      ?? (event.entityB as? HasSceneUnderstanding)   
    else { 
       // Did not collide with real world    
       return 
    } 
    // The bug entity is the one that is not the scene understanding entity
    let bugEntity = (sceneUnderstandingEntity == event.entityA)
                   ? event.entityB : event.entityA 

   // Disintegrate the bug entity
   …
}
```

### Real world collision filtering — [16:00]

```swift
// Only collide with real world
entity.collision?.filter.mask = [.sceneUnderstanding]

// Never collide with real world
entity.collision?.filter.mask = CollisionGroup.all.subtracting(.sceneUnderstanding)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10612/5/1B6C5C51-471E-4D93-9198-4D6B9AAE7D89/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10612) — developer.apple.com. Indexed for agent consumption._
