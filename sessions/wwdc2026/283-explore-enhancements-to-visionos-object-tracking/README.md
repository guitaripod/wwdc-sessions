---
id: "wwdc2026-283"
event: "wwdc2026"
year: 2026
title: "Explore enhancements to visionOS object tracking"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/283"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Explore enhancements to visionOS object tracking

**Event:** WWDC26 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-283](https://developer.apple.com/videos/play/wwdc2026/283)

Find out how visionOS is advancing object tracking and spatial accessory input. Discover new ways to track moving and handheld objects, allowing you to bridge the physical and digital worlds. Learn about new supported classes of spatial accessories and what is needed to build your own custom accessories to enable unique interaction models in your apps.

**Keywords:** `3d`, `3d content`, `anchor entity`, `object`, `object tracking`, `spatial accessories`, `spatial computing`, `visionos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,406 words)

## Documentation & Resources

- [Implementing object tracking in your app](https://developer.apple.com/documentation/visionOS/implementing-object-tracking-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/implementing-object-tracking-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/implementing-object-tracking-in-your-app.json
- [Working with generic spatial accessories](https://developer.apple.com/documentation/visionOS/working-with-generic-spatial-accessories) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/working-with-generic-spatial-accessories
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/working-with-generic-spatial-accessories.json
- [Preparing spatial accessories for tracking in your visionOS app](https://developer.apple.com/documentation/ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app.json
- [Spatial accessory design guidelines for Apple devices (check section 20)](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf#page=135) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/accessories/Accessory-Design-Guidelines.pdf#page=135
- [Exploring object tracking with ARKit](https://developer.apple.com/documentation/visionOS/exploring_object_tracking_with_arkit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/exploring_object_tracking_with_arkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/exploring_object_tracking_with_arkit.json

## Code Snippets

### Enable high frame rate tracking — [3:50]

```swift
// Enable high frame rate tracking

// Create reference object configuration
var configuration = ReferenceObject.Configuration()
configuration.highFrameRateTrackingEnabled = true

// Load the reference object with ARKit API
let refObjURL = Bundle.main.url(forResource: "flashlight", withExtension: ".referenceobject")
let refObject = try? await ReferenceObject(from: refObjURL!, configuration: configuration)
```

### Extended training mode via command-line — [4:50]

```bash
// Extended training mode on Mac using command-line interface

% xrun createml objecttracker --source flashlight.usdz --output flashlight.referenceobject --training-mode extended --all-angles
```

### Object pose coordinate spaces — [5:25]

```swift
// Different object pose spaces

// Obtain anchor transform with display corrections

let renderingPose = myObjectAnchor.coordinateSpace(correction: .rendered)

// Obtain anchor transform in metric space

let metricPose = myObjectAnchor.coordinateSpace(correction: .none)
```

### Implement object tracking in iOS — [6:22]

```swift
// Implement object tracking in iOS

import ARKit
import RealityKit

class ObjectTrackingARSessionDelegate: NSObject, ARSessionDelegate {
        let arView = ARView(frame: .zero)
        var entities: [UUID: AnchorEntity] = [:]

        func start() throws {
                let stationaryObject = try ARReferenceObject(archiveURL:
                        Bundle.main.url(forResource: "stationary", withExtension: "referenceobject")!)
                let movingObject = try ARReferenceObject(archiveURL:
                        Bundle.main.url(forResource: "moving", withExtension: "referenceobject")!)

                let configuration = ARWorldTrackingConfiguration()
                configuration.detectionObjects = [stationaryObject]   // Low frame rate
                configuration.trackingObjects = [movingObject]        // High frame rate

                arView.session.delegate = self
                arView.session.run(configuration)
        }

				func session(_ session: ARSession, didAdd anchors: [ARAnchor]) {
                for case let anchor as ARObjectAnchor in anchors {
                        let entity = AnchorEntity(anchor: anchor)
                        entities[anchor.identifier] = entity
                        arView.scene.addAnchor(entity)
                }
        }

        func session(_ session: ARSession, didUpdate anchors: [ARAnchor]) {
                for case let anchor as ARObjectAnchor in anchors {
                        entities[anchor.identifier]?.isEnabled = anchor.isTracked
                }
        }

        func session(_ session: ARSession, didRemove anchors: [ARAnchor]) {
                for case let anchor as ARObjectAnchor in anchors {
                        if let entity = entities.removeValue(forKey: anchor.identifier) {
                                arView.scene.removeAnchor(entity)
                        }
                }
        }
}
```

### Discover and connect a spatial accessory — [12:26]

```swift
import ARKit
import GameController

// Generic accessory discovery

if let device = GCSpatialAccessory.spatialAccessories.first {

        // Resolves the .referenceaccessory bundle automatically

        let accessory = try await Accessory(device: device)
        let provider = AccessoryTrackingProvider(accessories: [accessory])
        try await arkitSession.run([provider])
}

// Update tracked accessories without restarting the session                             

try await provider.updateAccessories([newAccessory])
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/283/4/22b92960-c65b-450f-b42c-6d6bff64a9b4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/283/4/22b92960-c65b-450f-b42c-6d6bff64a9b4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/283) — developer.apple.com. Indexed for agent consumption._
