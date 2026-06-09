---
id: "wwdc2020-10611"
event: "wwdc2020"
year: 2020
title: "Explore ARKit 4"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10611"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Explore ARKit 4

**Event:** WWDC20 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10611](https://developer.apple.com/videos/play/wwdc2020/10611)

ARKit 4 enables you to build the next generation of augmented reality apps to transform how people connect with the world around them. We’ll walk you through the latest improvements to Apple’s augmented reality platform, including how to use Location Anchors to connect virtual objects with a real-world longitude, latitude, and altitude. Discover how to harness the LiDAR Scanner on iPad Pro and obtain a depth map of your environment. And learn how to track faces in AR on more devices, including the iPad Air (3rd generation), iPad mini (5th generation), and all devices with the A12 Bionic chip or later that have a front-facing camera. To get the most out of this session, you should be familiar with how your apps can take advantage of LiDAR Scanner on iPad Pro. Watch “Advanced Scene Understanding in AR” for more information. Once you’ve learned how to leverage ARKit 4 in your iOS and iPadOS apps, explore realistic rendering improvements in “What’s New in RealityKit” and other ARKit features like People Occlusion and Motion Capture with “Introducing ARKit 3”.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,425 words)

## Documentation & Resources

- [Displaying a point cloud using scene depth](https://developer.apple.com/documentation/ARKit/displaying-a-point-cloud-using-scene-depth) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/displaying-a-point-cloud-using-scene-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/displaying-a-point-cloud-using-scene-depth.json
- [Tracking geographic locations in AR](https://developer.apple.com/documentation/ARKit/tracking-geographic-locations-in-ar) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/tracking-geographic-locations-in-ar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/tracking-geographic-locations-in-ar.json
- [Creating a fog effect using scene depth](https://developer.apple.com/documentation/ARKit/creating-a-fog-effect-using-scene-depth) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/creating-a-fog-effect-using-scene-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/creating-a-fog-effect-using-scene-depth.json
- [ARKit](https://developer.apple.com/documentation/ARKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit.json

## Code Snippets

### Availability — [6:58]

```swift
// Check device support for geo-tracking
guard ARGeoTrackingConfiguration.isSupported else {
    // Geo-tracking not supported on this device
    return
}

// Check current location is supported for geo-tracking
ARGeoTrackingConfiguration.checkAvailability { (available, error) in
    guard available else {
        // Geo-tracking not supported at current location
        return
    }
    // Run ARSession
    let arView = ARView()
    arView.session.run(ARGeoTrackingConfiguration())
}
```

### Adding Location Anchors — [8:38]

```swift
// Create coordinates
let coordinate = CLLocationCoordinate2D(latitude: 37.795313, longitude: -122.393792)

// Create Location Anchor
let geoAnchor = ARGeoAnchor(name: "Ferry Building", coordinate: coordinate)

// Add Location Anchor to session
arView.session.add(anchor: geoAnchor)

// Create a RealityKit anchor entity 
let geoAnchorEntity = AnchorEntity(anchor: geoAnchor)

// Anchor content under the RealityKit anchor
geoAnchorEntity.addChild(generateSignEntity())

// Add the RealityKit anchor to the scene
arView.scene.addAnchor(geoAnchorEntity)
```

### Positioning Content — [10:32]

```swift
// Create a new entity for our virtual content
let signEntity = generateSignEntity();

// Add the virtual content entity to the Geo Anchor entity
geoAnchorEntity.addChild(signEntity)

// Rotate text to face the city
let orientation = simd_quatf.init(angle: -Float.pi / 3.5, axis: SIMD3<Float>(0, 1, 0))
signEntity.setOrientation(orientation, relativeTo: geoAnchorEntity)

// Elevate text to 35 meters above ground level
let position = SIMD3<Float>(0, 35, 0)
signEntity.setPosition(position, relativeTo: geoAnchorEntity)
```

### User Interactive Location Anchors — [14:08]

```swift
let session = ARSession()
let worldPosition = raycastLocationFromUserTap()
session.getGeoLocation(forPoint: worldPosition) { (location, altitude, error) in
    if let error = error {
        ...
    }
    let geoAnchor = ARGeoAnchor(coordinate: location, altitude: altitude)
}
```

### Enabling the Depth API — [20:32]

```swift
// Enabling the depth API

let session = ARSession()
let configuration = ARWorldTrackingConfiguration()

// Check if configuration and device supports .sceneDepth
if type(of: configuration).supportsFrameSemantics(.sceneDepth) {
    // Activate sceneDepth
    configuration.frameSemantics = .sceneDepth
}
session.run(configuration)

...

// Accessing depth data
func session(_ session: ARSession, didUpdate frame: ARFrame) {
    guard let depthData = frame.sceneDepth else { return }
    // Use depth data
}
```

### Depth API alongside person occlusion — [21:12]

```swift
// Using the depth API alongside person occlusion

let session = ARSession()
let configuration = ARWorldTrackingConfiguration()

// Set required frame semantics
let semantics: ARConfiguration.FrameSemantics = .personSegmentationWithDepth

// Check if configuration and device supports the required semantics
if type(of: configuration).supportsFrameSemantics(semantics) {
    // Activate .personSegmentationWithDepth
    configuration.frameSemantics = semantics
}
session.run(configuration)
```

### Raycasting — [25:41]

```swift
let session = ARSession()
hitTest(point, types: [.existingPlaneUsingGeometry,
                       .estimatedVerticalPlane,
                       .estimatedHorizontalPlane])

let query = arView.makeRaycastQuery(from: point,
                                    allowing: .estimatedPlane,
                                    alignment: .any)

let raycast = session.trackedRaycast(query) { results in
   // result updates
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10611/8/203AC69C-0F17-4709-B622-08C2740C7539/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10611) — developer.apple.com. Indexed for agent consumption._
