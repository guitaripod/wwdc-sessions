---
id: "wwdc2025-296"
event: "wwdc2025"
year: 2025
title: "Support immersive video playback in visionOS apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/296"
topics: ["Audio & Video", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Support immersive video playback in visionOS apps

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-296](https://developer.apple.com/videos/play/wwdc2025/296)

Discover how to play immersive videos in visionOS apps. We’ll cover various immersive rendering modes, review the frameworks that support them, and walk through how to render immersive video in your app. To get the most out of this video, we recommend first watching “Explore video experiences for visionOS” from WWDC25.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,111 words)

## Documentation & Resources

- [HTTP Live Streaming Examples](https://developer.apple.com/streaming/examples/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/examples/
- [Playing immersive media with RealityKit](https://developer.apple.com/documentation/visionOS/playing-immersive-media-with-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/playing-immersive-media-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/playing-immersive-media-with-realitykit.json
- [Playing immersive media with AVKit](https://developer.apple.com/documentation/AVKit/playing-immersive-media-with-avkit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/playing-immersive-media-with-avkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/playing-immersive-media-with-avkit.json
- [RealityKit](https://developer.apple.com/documentation/RealityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json
- [AVKit](https://developer.apple.com/documentation/AVKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit.json

## Code Snippets

### AVExperienceController - AutomaticTransitionToImmersive — [5:03]

```swift
struct ExpandedConfiguration {
    enum AutomaticTransitionToImmersive {
  		case `default`
  		case  none
    }
}
```

### Disable Automatic Transitions to immersive — [5:50]

```swift
import AVKit

let controller = AVPlayerViewController()

let experienceController = controller.experienceController
experienceController.allowedExperiences = .recommended(including: [.expanded, .immersive])

experienceController.configuration.expanded.automaticTransitionToImmersive = .none

await experienceController.transition(to: .expanded)
```

### AVExperienceController - Immersive — [6:26]

```swift
enum Experience {
    case immersive
}

struct Configuration {
		struct Placement {
			static var unspecified: Placement
			static func over(scene: UIScene) -> Placement
		}
}
```

### Transition to immersive — [6:53]

```swift
import AVKit

let controller = AVPlayerViewController()

let experienceController = controller.experienceController
experienceController.allowedExperiences = .recommended(including: [.immersive])

let myScene = getMyPreferredWindowUIScene()
experienceController.configuration.placement = .over(scene: myScene)

await experienceController.transition(to: .immersive)
```

### AVExperienceController.Delegate — [8:13]

```swift
func experienceController(_ controller: AVExperienceController, didChangeAvailableExperiences availableExperiences: AVExperienceController.Experiences)

func experienceController(_ controller: AVExperienceController, prepareForTransitionUsing context: AVExperienceController.TransitionContext) async

func experienceController(_ controller: AVExperienceController, didChangeTransitionContext context: AVExperienceController.TransitionContext)
```

### PortalVideoView — [12:52]

```swift
@main
struct ImmersiveVideoApp: App {
    var body: some Scene {
        WindowGroup {
            PortalVideoView()
        }
    }
}
```

### Portal Rendering — [13:03]

```swift
import AVFoundation
import RealityKit
import SwiftUI

struct PortalVideoView: View {
    var body: some View {
        RealityView { content in
            guard let url = URL(string: "https://cdn.example.com/My180.m3u8") else { return }
            let player = AVPlayer(playerItem: AVPlayerItem(url: url))
            let videoEntity = Entity()
            var videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
            videoPlayerComponent.desiredImmersiveViewingMode = .portal
            videoEntity.components.set(videoPlayerComponent)
            videoEntity.scale *= 0.4
            content.add(videoEntity)
        }
    }
}
```

### Progressive Immersion Rendering — [13:57]

```swift
import AVFoundation
import RealityKit
import SwiftUI

struct ProgressiveVideoView: View {
    var body: some View {
        RealityView { content in
            guard let url = URL(string: "https://cdn.example.com/My180.m3u8") else { return }
            let player = AVPlayer(playerItem: AVPlayerItem(url: url))
            let videoEntity = Entity()
            var videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
            videoPlayerComponent.desiredImmersiveViewingMode = .progressive
            videoEntity.components.set(videoPlayerComponent)
            content.add(videoEntity)
        }
    }
}
```

### ProgressiveVideoView — [14:20]

```swift
import AVFoundation
import RealityKit
import SwiftUI

@main
struct ImmersiveVideoApp: App {
    var body: some Scene {
        ImmersiveSpace {
            ProgressiveVideoView()
        }
				.immersionStyle(selection: .constant(.progressive(0.1...1, initialAmount: 1.0)), in: .progressive)    
    }
}
```

### SpatialVideoMode — [17:22]

```swift
if let vpc = components.get[VideoPlayerComponent.self] {
	vpc.desiredSpatialVideoMode = .spatial
}
```

### Spatial Video Portal Rendering — [18:32]

```swift
import AVFoundation
import RealityKit
import SwiftUI

struct PortalSpatialVideoView: View {
    var body: some View {
        RealityView { content in
            let url = Bundle.main.url(forResource: "MySpatialVideo", withExtension: "mov")!
            let player = AVPlayer(url: url)
            let videoEntity = Entity()
            var videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
            videoPlayerComponent.desiredViewingMode = .stereo
            videoPlayerComponent.desiredSpatialVideoMode = .spatial
            videoPlayerComponent.desiredImmersiveViewingMode = .portal
            videoEntity.components.set(videoPlayerComponent)
            videoEntity.scale *= 0.4
            content.add(videoEntity)
        }
    }
}
```

### Spatial Video Immersive Rendering — [19:02]

```swift
import AVFoundation
import RealityKit
import SwiftUI

struct PortalSpatialVideoView: View {
    var body: some View {
        RealityView { content in
            let url = Bundle.main.url(forResource: "MySpatialVideo", withExtension: "mov")!
            let player = AVPlayer(url: url)
            let videoEntity = Entity()
            var videoPlayerComponent = VideoPlayerComponent(avPlayer: player)
            videoPlayerComponent.desiredViewingMode = .stereo
            videoPlayerComponent.desiredSpatialVideoMode = .spatial
            videoPlayerComponent.desiredImmersiveViewingMode = .full
            videoEntity.position = [0, 1.5, -1]
            videoEntity.components.set(videoPlayerComponent)
            content.add(videoEntity)
        }
    }
}
```

### ImmersiveSpatialVideoView — [19:46]

```swift
import AVFoundation
import RealityKit
import SwiftUI

@main
struct SpatialVideoApp: App {
    var body: some Scene {
        ImmersiveSpace {
            ContentSimpleView()
        }
        .immersionStyle(selection: .constant(.mixed), in: .mixed)
        .immersiveEnvironmentBehavior(.coexist)
    }
}
```

### Comfort Mitigation Event — [21:40]

```swift
switch event.comfortMitigation {
case .reduceImmersion:
    // Default behavior
    break
case .play:
    // No action
    break
case .pause:
    // Show custom pause dialog
    break
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/296/4/5953ed86-1de9-408e-9d39-2efe18da426b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/296/4/5953ed86-1de9-408e-9d39-2efe18da426b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/296) — developer.apple.com. Indexed for agent consumption._