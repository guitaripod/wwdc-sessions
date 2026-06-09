---
id: "wwdc2024-10101"
event: "wwdc2024"
year: 2024
title: "Explore object tracking for visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10101"
topics: ["AI & Machine Learning", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore object tracking for visionOS

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10101](https://developer.apple.com/videos/play/wwdc2024/10101)

Find out how you can use object tracking to turn real-world objects into virtual anchors in your visionOS app. Learn how you can build spatial experiences with object tracking from start to finish. Find out how to create a reference object using machine learning in Create ML and attach content relative to your target object in Reality Composer Pro, RealityKit or ARKit APIs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,873 words)

## Documentation & Resources

- [Implementing object tracking in your app](https://developer.apple.com/documentation/visionOS/implementing-object-tracking-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/implementing-object-tracking-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/implementing-object-tracking-in-your-app.json
- [Exploring object tracking with ARKit](https://developer.apple.com/documentation/visionOS/exploring_object_tracking_with_arkit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/exploring_object_tracking_with_arkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/exploring_object_tracking_with_arkit.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Coaching UI - display object USDZ preview — [13:55]

```swift
// Display object USDZ
struct ImmersiveView: View {
   @State var globeAnchor: Entity? = nil
    var body: some View {
        RealityView { content in
            // Load the reference object with ARKit API
            let refObjURL = 
            Bundle.main.url(forResource: "globe", withExtension: ".referenceobject")
            let refObject = try? await ReferenceObject(from: refObjURL!)

            // Load the model entity with USDZ path extracted from reference object
            let globePreviewEntity = 
            try? await Entity.init(contentsOf: (refObject?.usdzFile)!)

            // Set opacity to 0.5 and add to scene
            globePreviewEntity!.components.set(OpacityComponent(opacity: 0.5))
            content.add(globePreviewEntity!)
        }
    }
}
```

### Coaching UI - check anchor state — [14:13]

```swift
// Check anchor state
struct ImmersiveView: View {
   @State var globeAnchor: Entity? = nil
    var body: some View {
        RealityView { content in
            if let scene = try? await Entity(named: "Immersive", in: realityKitContentBundle) {
                globeAnchor = scene.findEntity(named: "GlobeAnchor")
                content.add(scene)
            }
            let updateSub = content.subscribe(to: SceneEvents.AnchoredStateChanged.self) { event in
                if let anchor = globeAnchor, event.anchor == anchor {
                    if event.isAnchored {
                        // Object anchor found, trigger transition animation
                    } else {
                        // Object anchor not found, display coaching UI
                    }
                }
            }
        }
    }
}
```

### Coaching UI - Transform space with SpatialSession — [14:31]

```swift
// Transform space
struct ImmersiveView: View {
   @State var globeAnchor: Entity? = nil
    var body: some View {
        RealityView { content in
            // Setup anchor transform space for object and world anchor
            let trackingSession = SpatialTrackingSession()
            let config = SpatialTrackingSession.Configuration(tracking: [.object, .world])
            if let result = await trackingSession.run(config) {
                if result.anchor.contains(.object) {
                    // Tracking not authorized, adjust experience accordingly
                }
            }
           // Get tracked object's world transform, identity if tracking not authorized
            let objectTransform = globeAnchor?.transformMatrix(relativeTo: nil)
            // Implement animation
            ...
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10101/4/6F54068C-B055-45B1-97A0-89AA6CFBDDD5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10101/4/6F54068C-B055-45B1-97A0-89AA6CFBDDD5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10101) — developer.apple.com. Indexed for agent consumption._