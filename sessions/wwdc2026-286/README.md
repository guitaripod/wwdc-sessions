# Use foveated streaming to bring immersive content to visionOS

**Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-286](https://developer.apple.com/videos/play/wwdc2026/286)

Find out how foveated streaming delivers remotely rendered scenes to Apple Vision Pro in full fidelity. Explore how this framework combines native visionOS capabilities with third-party streaming technologies completely wirelessly, demonstrated using an OpenXR scene and NVIDIA CloudXR. Learn about the FoveatedStreaming framework, integration with the NVIDIA CloudXR SDK, and how dynamically foveated streaming provides benefits while still preserving privacy.

**Keywords:** `3d content`, `enterprise`, `spatial`, `spatial accessories`, `spatial computing`, `visionos`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Analyzing the performance of a foveated streaming session](https://developer.apple.com/documentation/FoveatedStreaming/analyzing-the-performance-of-a-foveated-streaming-session) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoveatedStreaming/analyzing-the-performance-of-a-foveated-streaming-session
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoveatedStreaming/analyzing-the-performance-of-a-foveated-streaming-session.json
- [Establishing foveated streaming sessions with Apple Vision Pro](https://developer.apple.com/documentation/FoveatedStreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoveatedStreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoveatedStreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro.json
- [Streaming a CloudXR application to Apple Vision Pro with foveation](https://developer.apple.com/documentation/FoveatedStreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoveatedStreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoveatedStreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation.json
- [Creating a foveated streaming client on visionOS](https://developer.apple.com/documentation/FoveatedStreaming/creating-a-foveated-streaming-client-on-visionos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoveatedStreaming/creating-a-foveated-streaming-client-on-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoveatedStreaming/creating-a-foveated-streaming-client-on-visionos.json
- [Foveated Streaming](https://developer.apple.com/documentation/FoveatedStreaming) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoveatedStreaming
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoveatedStreaming.json
- [StreamingSession: Streaming immersive content from a CloudXR™ application to visionOS and iOS](https://github.com/apple/StreamingSession) _documentation_

## Code Snippets

### Connect to a streaming endpoint — [6:03]

```swift
// Connect to a streaming endpoint

import SwiftUI
import FoveatedStreaming

struct ConnectView: View {
    let session: FoveatedStreamingSession

    var body: some View {
        Button("Connect") {
            Task {
                try await session.connect()
            }
        }
    }
}
```

### Display a Foveated Streaming session in your immersive space — [6:44]

```swift
// Display a Foveated Streaming session in your immersive space

import SwiftUI
import FoveatedStreaming

@main struct FoveatedStreamingSampleApp: App {
    private let session = FoveatedStreamingSession()

    var body: some SwiftUI.Scene {
        ImmersiveSpace(foveatedStreaming: session)
    }
}
```

### Compose SwiftUI content with Foveated Streaming — [6:55]

```swift
// Compose SwiftUI content with Foveated Streaming

import SwiftUI
import FoveatedStreaming

@main struct FoveatedStreamingSampleApp: App {
    private let session = FoveatedStreamingSession()
    private let appModel = AppModel()

    var body: some SwiftUI.Scene {
        Window("Main", id: appModel.mainWindowId) {
            ContentView(session: session)
                .environment(appModel)
                .environment(session)
                // ...
        }

        ImmersiveSpace(foveatedStreaming: session) {
            SpatialContainer {
                ReopenMainWindowView().environment(appModel)
                TransformStreamWidgetView().environment(session)
            }
        }

    }
}
```

### Compose RealityKit content with Foveated Streaming — [13:42]

```swift
// Compose RealityKit content with Foveated Streaming

import SwiftUI
import RealityKit
import FoveatedStreaming

@main struct FoveatedStreamingSampleApp: App {
    private let session = FoveatedStreamingSession()
    private let appModel = AppModel()

    var body: some SwiftUI.Scene {
        ImmersiveSpace(foveatedStreaming: session) {
            RealityView { content in
                // ...
            }
        }

    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/286/4/fa302edd-f95a-49f4-b51c-3899d49c6dec/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/286/4/fa302edd-f95a-49f4-b51c-3899d49c6dec/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._