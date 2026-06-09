---
id: "wwdc2024-10100"
event: "wwdc2024"
year: 2024
title: "Create enhanced spatial computing experiences with ARKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10100"
topics: ["Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Create enhanced spatial computing experiences with ARKit

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10100](https://developer.apple.com/videos/play/wwdc2024/10100)

Learn how to create captivating immersive experiences with ARKit’s latest features. Explore ways to use room tracking and object tracking to further engage with your surroundings. We’ll also share how your app can react to changes in your environment’s lighting on this platform. Discover improvements in hand tracking and plane detection which can make your spatial experiences more intuitive.

**Keywords:** `arkit`, `immersive apps`, `spatial computing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,234 words)

## Documentation & Resources

- [Building local experiences with room tracking](https://developer.apple.com/documentation/arkit/building_local_experiences_with_room_tracking) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/arkit/building_local_experiences_with_room_tracking
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/arkit/building_local_experiences_with_room_tracking.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### RoomTrackingProvider — [3:35]

```swift
// RoomTrackingProvider

@available(visionOS, introduced: 2.0)
public final class RoomTrackingProvider: DataProvider, Sendable {

    /// The room which a person is currently in, if any.
    public var currentRoomAnchor: RoomAnchor? { get }

    /// An async sequence of all anchor updates.
    public var anchorUpdates: AnchorUpdateSequence<RoomAnchor> { get }

    ...
}
```

### RoomAnchor — [4:20]

```swift
@available(visionOS, introduced: 2.0)
public struct RoomAnchor: Anchor, Sendable, Equatable {
    /// True if this is the room which a person is currently in.
    public var isCurrentRoom: Bool { get }

    /// Get the geometry of the mesh in the anchor's coordinate system.
    public var geometry: MeshAnchor.Geometry { get }
    /// Get disjoint mesh geometries of a given classification.
    public func geometries(of classification: MeshAnchor.MeshClassification) -> 
        [MeshAnchor.Geometry]

    /// True if this room contains the given point.
    public func contains(_ point: SIMD3<Float>) -> Bool

    /// Get the IDs of the plane anchors associated with this room.
    public var planeAnchorIDs: [UUID] { get }
    /// Get the IDs of the mesh anchors associated with this room.
    public var meshAnchorIDs: [UUID] { get }
}
```

### Load Object Tracking referenceobject — [8:06]

```swift
// Object tracking

Task {
    do {
        let url = URL(fileURLWithPath: "/path/to/globe.referenceobject")
        let referenceObject = try await ReferenceObject(from: url)
        let objectTracking = ObjectTrackingProvider(referenceObjects: [referenceObject])
    } catch {
        // Handle reference object loading error.
    }
    ...
}
```

### Run ARKitSession with ObjectTracking provider — [8:27]

```swift
let session = ARKitSession()

Task {
    do {
        try await session.run([objectTracking])
    } catch {
        // Handle session run error.
    }

    for await event in session.events {
        switch event {
        case .dataProviderStateChanged(_, newState: let newState, _):
            if newState == .running {
                // Ready to start processing anchor updates.
            }
        ...
        }
    }
}
```

### ObjectAnchor — [8:43]

```swift
// ObjectAnchor

@available(visionOS, introduced: 2.0)
public struct ObjectAnchor: TrackableAnchor, Sendable, Equatable {

    /// An axis-aligned bounding box.
    public struct AxisAlignedBoundingBox: Sendable, Equatable {
        ...
    }

    /// The bounding box of this anchor.
    public var boundingBox: AxisAlignedBoundingBox { get }

    /// The reference object which this anchor corresponds to.
    public var referenceObject: ReferenceObject { get }
}
```

### World Tracking - reacting to changes in lighting conditions — [11:03]

```swift
struct WellPreparedView: View {
    @Environment(\.worldTrackingLimitations) var worldTrackingLimitations

    var body: some View {
        ...

        .onChange(of: worldTrackingLimitations) {
            if worldTrackingLimitations.contains(.translation) {
                // Rearrange content when anchored positions are unavailable.
            }
        }
    }
}
```

### Hands prediction — [12:51]

```swift
// Hands prediction

func submitFrame(_ frame: LayerRenderer.Frame) {
    ...

    guard let drawable = frame.queryDrawable() else { return }

    // Get the trackable anchor time to target.
    let trackableAnchorTime = drawable.frameTiming.trackableAnchorTime

    // Convert the timestamp into units of seconds.
let anchorPredictionTime = LayerRenderer.Clock.Instant.epoch.duration(to:     trackableAnchorTime).timeInterval  

    // Predict hand anchors for the time that provides best content registration.
    let (leftHand, rightHand) = handTracking.handAnchors(at: anchorPredictionTime)

    ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10100/4/3F3285E6-7223-427A-A3AE-169CFB35EB37/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10100/4/3F3285E6-7223-427A-A3AE-169CFB35EB37/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10100) — developer.apple.com. Indexed for agent consumption._