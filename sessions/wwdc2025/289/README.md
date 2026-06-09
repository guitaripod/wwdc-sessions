---
id: "wwdc2025-289"
event: "wwdc2025"
year: 2025
title: "Explore spatial accessory input on visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/289"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore spatial accessory input on visionOS

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-289](https://developer.apple.com/videos/play/wwdc2025/289)

Learn how you can integrate spatial accessories into your app. Display virtual content, interact with your app, track them in space, and get information on interactions for enhanced virtual experiences on visionOS.

**Keywords:** `3d`, `6dof`, `accessory`, `controller`, `input`, `pencilkit`, `spatial computing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,177 words)

## Documentation & Resources

- [Tracking a handheld accessory as a virtual sculpting tool](https://developer.apple.com/documentation/RealityKit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.json

## Code Snippets

### Get in-app transforms — [0:09]

```swift
// Get in-app transforms

let session = SpatialTrackingSession()

let configuration = SpatialTrackingSession.Configuration(tracking: [.accessory])

await session.run(configuration)
```

### Check for accessory support — [4:57]

```swift
// Check spatial accessory support

NotificationCenter.default.addObserver(forName: NSNotification.Name.GCControllerDidConnect, object: nil, queue: nil) {
  notification in
    if let controller = notification.object as? GCController,
       controller.productCategory == GCProductCategorySpatialController {

    }
}
```

### Anchor virtual content to an accessory — [7:20]

```swift
// Anchor virtual content to an accessory

func setupSpatialAccessory(device: GCDevice) async throws {

    let source = try await AnchoringComponent.AccessoryAnchoringSource(device: device)

    guard let location = source.locationName(named: "aim") else {
        return
    }

    let sculptingEntity = AnchorEntity(.accessory(from: source, location: location),
                                       trackingMode: .predicted)

}
```

### Add haptics to an accessory — [9:45]

```swift
// Add haptics to an accessory

let stylus: GCStylus = ...

guard let haptics = stylus.haptics else {
    return
}

guard let hapticsEngine: CHHapticEngine = haptics.createEngine(withLocality: .default) else {
    return
}

try? hapticsEngine.start()
```

### Access ARKit anchors from AnchorEntity — [11:25]

```swift
// Access ARKit anchors from AnchorEntity

func getAccessoryAnchor(entity: AnchorEntity) -> AccessoryAnchor? {
    if let component = entity.components[ARKitAnchorComponent.self],
       let accessoryAnchor = component.anchor as? AccessoryAnchor {
        return accessoryAnchor
    }
    return nil
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/289/4/7934a0e5-f8a8-4530-b614-5ed367076da5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/289/4/7934a0e5-f8a8-4530-b614-5ed367076da5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/289) — developer.apple.com. Indexed for agent consumption._