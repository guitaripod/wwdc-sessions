---
id: "wwdc2023-10087"
event: "wwdc2023"
year: 2023
title: "Build spatial SharePlay experiences"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10087"
topics: ["Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Build spatial SharePlay experiences

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10087](https://developer.apple.com/videos/play/wwdc2023/10087)

Discover how you can use the GroupActivities framework to build unique sharing and collaboration experiences for visionOS. We’ll introduce you to SharePlay on this platform, learn how to create experiences that make people feel present as if they were in the same space, and explore how immersive apps can respect shared context between participants.

**Keywords:** `group activities`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,094 words)

## Documentation & Resources

- [SystemCoordinator](https://developer.apple.com/documentation/GroupActivities/SystemCoordinator) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities/SystemCoordinator
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities/SystemCoordinator.json

## Code Snippets

### Observe the local participant state — [4:08]

```swift
for await session in ExploreActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    let isLocalParticipantSpatial = systemCoordinator.localParticipantState.isSpatial

    Task.detached {
        for await localParticipantState in systemCoordinator.localParticipantStates {
            if localParticipantState.isSpatial {
                // Start syncing scroll position
            } else {
                // Stop syncing scroll position
            }
        }
    }
}
```

### Configure the spatial template preferences — [6:10]

```swift
for await session in ExploreActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    var configuration = SystemCoordinator.Configuration()
    configuration.spatialTemplatePreference = .sideBySide
    systemCoordinator.configuration = configuration

    session.join()
}
```

### Configuring scene activation conditions — [9:10]

```swift
@main
struct ExploreTogetherApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .handlesExternalEvents(
                    preferring: ["com.example.explore-together.activity"],
                    allowing: ["com.example.explore-together.activity"]
                )
        }
    }
}
```

### Configuring scene activation conditions — [9:30]

```swift
class SceneDelegate: NSObject, UISceneDelegate {

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // ...

        scene.activationConditions.canActivateForTargetContentIdentifierPredicate =
                NSPredicate(format: "self == %@", "com.example.explore-together.activity")

        scene.activationConditions.prefersToActivateForTargetContentIdentifierPredicate =
                NSPredicate(format: "self == %@", "com.example.explore-together.activity")
    }
}
```

### Setting scene association behavior — [10:40]

```swift
struct ExploreActivity: GroupActivity {
    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        // ...
        metadata.sceneAssociationBehavior = .content("document-1")
        return metadata
    }
}
```

### Starting SharePlay — [13:44]

```swift
// Create the activity
let activity = ExploreActivity()

// Register the activity on the item provider
let itemProvider = NSItemProvider()
itemProvider.registerGroupActivity(activity)

// Create the activity items configuration
let configuration = UIActivityItemsConfiguration(itemProviders: [itemProvider])

// Provide the metadata for the group activity
configuration.metadataProvider = { key in
    guard key == .linkPresentationMetadata else { return nil }
    let metadata = LPLinkMetadata()
    metadata.title = "Explore Together"
    metadata.imageProvider = NSItemProvider(object: UIImage(named: "explore-activity")!)
    return metadata
}
self.activityItemsConfiguration = configuration
```

### Configure group ImmersiveSpace — [16:03]

```swift
for await session in ExploreActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    var configuration = SystemCoordinator.Configuration()
    configuration.supportsGroupImmersiveSpace = true
    systemCoordinator.configuration = configuration
}
```

### System Experience Displacement — [17:51]

```swift
// Use immersiveSpaceDisplacement to offset contents in group immersive space

var body: some Scene {
    ImmersiveSpace(id: "earth") {
        GeometryReader3D { proxy in
            let displacement = proxy.immersiveSpaceDisplacement(in: .global).inverse

            Control()
                .offset(displacement.position)
                .rotation3DEffect(displacement.rotation)
        }
    }
}
```

### Spatial Template Preferences — [20:46]

```swift
// Configure the spatial template preferences with content extent

for await session in ExploreSolarActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    var configuration = SystemCoordinator.Configuration()
    configuration.supportsGroupImmersiveSpace = true
    configuration.spatialTemplatePreference = .sideBySide.contentExtent(200)
    systemCoordinator.configuration = configuration
}
```

### Receive group immersion style to configure group immersive space — [22:32]

```swift
// Receive group immersion style to configure group immersive space

for await session in ExploreSolarActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    Task.detached {
        for await immersionStyle in systemCoordinator.groupImmersionStyle {
            if let immersionStyle {
                // Open an immersive space with the same immersion style
            } else {
                // Dismiss the immersive space
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10087/4/36E3D439-2B36-408C-9249-3929F2E75FBD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10087/4/36E3D439-2B36-408C-9249-3929F2E75FBD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10087) — developer.apple.com. Indexed for agent consumption._