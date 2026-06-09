---
id: "wwdc2025-318"
event: "wwdc2025"
year: 2025
title: "Share visionOS experiences with nearby people"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/318"
topics: ["Audio & Video", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Share visionOS experiences with nearby people

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-318](https://developer.apple.com/videos/play/wwdc2025/318)

Learn how to create shared experiences for people wearing Vision Pro in the same room. We’ll show you how to integrate SharePlay and leverage ARKit in your app, introduce the updated window sharing flows for nearby and FaceTime participants, and cover new API designed for seamless collaboration. Discover best practices to make your collaborative features stand out, easily discoverable, and engaging for people together in the same space.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,463 words)

## Documentation & Resources

- [worldAnchorSharingAvailability](https://developer.apple.com/documentation/ARKit/WorldTrackingProvider/worldAnchorSharingAvailability-swift.property) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/WorldTrackingProvider/worldAnchorSharingAvailability-swift.property
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/WorldTrackingProvider/worldAnchorSharingAvailability-swift.property.json
- [groupActivityAssociation(_:)](https://developer.apple.com/documentation/SwiftUI/View/groupActivityAssociation(_:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View/groupActivityAssociation(_:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View/groupActivityAssociation(_:).json
- [init(originFromAnchorTransform:sharedWithNearbyParticipants:)](https://developer.apple.com/documentation/ARKit/WorldAnchor/init(originFromAnchorTransform:sharedWithNearbyParticipants:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/WorldAnchor/init(originFromAnchorTransform:sharedWithNearbyParticipants:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/WorldAnchor/init(originFromAnchorTransform:sharedWithNearbyParticipants:).json
- [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/GroupActivities/configure-your-app-for-sharing-with-people-nearby) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities/configure-your-app-for-sharing-with-people-nearby
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities/configure-your-app-for-sharing-with-people-nearby.json
- [AVPlaybackCoordinator](https://developer.apple.com/documentation/AVFoundation/AVPlaybackCoordinator) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/AVPlaybackCoordinator
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/AVPlaybackCoordinator.json
- [Building a guessing game for visionOS](https://developer.apple.com/documentation/GroupActivities/building-a-guessing-game-for-visionos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities/building-a-guessing-game-for-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities/building-a-guessing-game-for-visionos.json

## Code Snippets

### Expose an activity with GroupActivities and SwiftUI — [6:21]

```swift
// Expose an activity with GroupActivities and SwiftUI

import SwiftUI
import GroupActivities

struct BoardGameActivity: GroupActivity, Transferable {
    var metadata: GroupActivityMetadata = {
        var metadata = GroupActivityMetadata()
        metadata.title = "Play Together"
        return metadata
    }()
}

struct BoardGameApp: App {
    var body: some Scene {
        WindowGroup {
            BoardGameView()
            ShareLink(item: BoardGameActivity(), preview: SharePreview("Play Together"))
                .hidden()
        }
        .windowStyle(.volumetric)
    }
}

struct BoardGameView: View {
    var body: some View {
        // Board game content
    }
}
```

### Join a GroupSession with GroupActivities — [7:14]

```swift
// Join a GroupSession with GroupActivities

func observeSessions() async {

    // Sessions are created automatically when the activity is activated
    for await session in BoardGameActivity.sessions() {

        // Additional configuration and setup

        // Join SharePlay
        session.join()
    }
}
```

### Join and configure a GroupSession with GroupActivities — [8:57]

```swift
// Join a GroupSession with GroupActivities

func observeSessions() async {

    // Sessions are created automatically when the activity is activated
    for await session in BoardGameActivity.sessions() {

        // Additional configuration and setup

        guard let systemCoordinator = await session.systemCoordinator else { continue }
        systemCoordinator.configuration.supportsGroupImmersiveSpace = true

        // Join SharePlay
        session.join()
    }
}
```

### Check for nearby participants with GroupActivities — [9:59]

```swift
// Check for nearby participants with GroupActivities

func observeParticipants(session: GroupSession<BoardGameActivity>) async {
    for await activeParticipants in session.$activeParticipants.values {
        let nearbyParticipants = activeParticipants.filter {
            $0.isNearbyWithLocalParticipant && $0 != session.localParticipant
        }
    }
}
```

### Observe local participant pose with GroupActivities — [11:42]

```swift
// Observe local participant pose with GroupActivities

func observeLocalParticipantState(session: GroupSession<BoardGameActivity>) async {
    guard let systemCoordinator = await session.systemCoordinator else { return }

    for await localParticipantState in systemCoordinator.localParticipantStates {
        let localParticipantPose = localParticipantState.pose
        // Place presented content relative to the local participant pose
    }
}
```

### Associate a specific window with GroupActivities and SwiftUI — [15:54]

```swift
// Associate a specific window with GroupActivities and SwiftUI

import SwiftUI
import GroupActivities

struct BoardGameApp: App {
    var body: some Scene {
        WindowGroup {
            BoardGameView()
            ShareLink(item: BoardGameActivity(), preview: SharePreview("Play Together"))
                .hidden()
        }
        .windowStyle(.volumetric)

        WindowGroup(id: "InstructionalVideo") {
            InstructionalVideoView()
                .groupActivityAssociation(.primary("InstructionalVideo"))
        }
    }
}

struct BoardGameView: View {
    var body: some View {
        // Board game content
    }
}

struct InstructionalVideoView: View {
    var body: some View {
        // Video content
    }
}
```

### Create a world anchor with ARKit — [18:27]

```swift
// Create a world anchor with ARKit

import ARKit

class AnchorController {

    func setUp(session: ARKitSession, provider: WorldTrackingProvider) async throws {
        try await session.run([provider])
    }

    func createAnchor(at transform: simd_float4x4, provider: WorldTrackingProvider) async throws {
        let anchor = WorldAnchor(originFromAnchorTransform: transform)
        try await provider.addAnchor(anchor)
    }

    func observeWorldTracking(provider: WorldTrackingProvider) async {
       for await update in provider.anchorUpdates {
            switch update.event {
            case .added, .updated, .removed:
                // Add, update, or remove furniture
                break
            }
        }
    }
}
```

### Observe sharing availability with ARKit — [20:02]

```swift
// Observe sharing availability with ARKit

func observeSharingAvailability(provider: WorldTrackingProvider) async {
    for await sharingAvailability in provider.worldAnchorSharingAvailability {
         if sharingAvailability == .available {
             // Store availability to check when creating a new shared world anchor
         }
     }
}
```

### Create a shared world anchor with ARKit — [20:24]

```swift
// Create a shared world anchor with ARKit

import ARKit

class SharedAnchorController {

    func setUp(session: ARKitSession, provider: WorldTrackingProvider) async throws {
        try await session.run([provider])
    }

    func createAnchor(at transform: simd_float4x4, provider: WorldTrackingProvider) async throws {
        let anchor = WorldAnchor(originFromAnchorTransform: transform,
                                 sharedWithNearbyParticipants: true)
        try await provider.addAnchor(anchor)
    }

    func observeWorldTracking(provider: WorldTrackingProvider) async {
       for await update in provider.anchorUpdates {
            switch update.event {
            case .added, .updated, .removed:
                // Add, update, or remove furniture. Updates with shared anchors from others!
                let anchorIdentifier = update.anchor.id
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/318/5/b5e843e6-41fc-4ddd-8aa6-91e3ede41898/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/318/5/b5e843e6-41fc-4ddd-8aa6-91e3ede41898/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/318) — developer.apple.com. Indexed for agent consumption._
