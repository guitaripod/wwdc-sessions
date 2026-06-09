---
id: "wwdc2025-290"
event: "wwdc2025"
year: 2025
title: "Set the scene with SwiftUI in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/290"
topics: ["Design", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Set the scene with SwiftUI in visionOS

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-290](https://developer.apple.com/videos/play/wwdc2025/290)

Discover exciting new APIs to enhance windows, volumes, and immersive spaces in your visionOS app. Fine tune the behavior of your scenes when relaunched or locked in place. Make volumes adapt to their surroundings with clipping margins and snapping. Stream immersive content from Mac to Vision Pro. Elevate your existing UIKit-based apps with volumes and immersive spaces.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,349 words)

## Documentation & Resources

- [Adopting best practices for persistent UI](https://developer.apple.com/documentation/visionOS/adopting-best-practices-for-scene-restoration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/adopting-best-practices-for-scene-restoration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/adopting-best-practices-for-scene-restoration.json
- [Tracking accessories in volumetric windows](https://developer.apple.com/documentation/ARKit/tracking-accessories-in-volumetric-windows) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/tracking-accessories-in-volumetric-windows
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/tracking-accessories-in-volumetric-windows.json
- [Petite Asteroids: Building a volumetric visionOS game](https://developer.apple.com/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/petite-asteroids-building-a-volumetric-visionos-game.json
- [Canyon Crosser: Building a volumetric hike-planning app](https://developer.apple.com/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app.json

## Code Snippets

### Disabling restoration — [4:10]

```swift
// Disabling restoration

WindowGroup("Tools", id: "tools") {
    ToolsView()
}
.restorationBehavior(.disabled)
```

### Disabling restoration in UIKit — [4:36]

```swift
// Disabling restoration

windowScene.destructionConditions = [
    .systemDisconnection
]
```

### Specifying launch window — [5:02]

```swift
// Specifying launch window

@AppStorage("isFirstLaunch") private var isFirstLaunch = true

var body: some Scene {
    WindowGroup("Stage Selection", id: "selection") {
        SelectionView()
    }

    WindowGroup("Welcome", id: "welcome") {
        WelcomeView()
            .onAppear {
                isFirstLaunch = false
            }
    }
    .defaultLaunchBehavior(isFirstLaunch ? .presented : .automatic)

    // ...
}
```

### "suppressed" behavior — [6:39]

```swift
// "suppressed" behavior

WindowGroup("Tools", id: "tools") {
    ToolsView()
}
.restorationBehavior(.disabled)
.defaultLaunchBehavior(.suppressed)
```

### Unique window — [7:44]

```swift
// Unique window

@AppStorage("isFirstLaunch") private var isFirstLaunch = true

var body: some Scene {
    // ...

    Window("Welcome", id: "welcome") {
        WelcomeView()
            .onAppear {
                isFirstLaunch = false
            }
    }
    .defaultLaunchBehavior(isFirstLaunch ? .presented : .automatic)

    WindowGroup("Main Stage", id: "main") {
        StageView()
    }

    // ...
}
```

### Surface snapping — [10:24]

```swift
// Surface snapping

@Environment(\.surfaceSnappingInfo) private var snappingInfo
@State private var hidePlatform = false

var body: some View { 
    RealityView { /* ... */ }
    .onChange(of: snappingInfo) {
        if snappingInfo.isSnapped &&
            SurfaceSnappingInfo.authorizationStatus == .authorized
        {
            switch snappingInfo.classification {
                case .table:
                    hidePlatform = true
                default:
                    hidePlatform = false
            }
        }
    }
}
```

### Clipping margins — [14:41]

```swift
// Clipping margins

@Environment(\.windowClippingMargins) private var windowMargins
@PhysicalMetric(from: .meters) private var pointsPerMeter = 1

var body: some View {
    RealityView { content in
        // ...
        waterfall = createWaterfallEntity()
        content.add(waterfall)
    } update: { content in
        waterfall.scale.y = Float(min(
            windowMargins.bottom / pointsPerMeter,
            maxWaterfallHeight))
        // ...
    }
    .preferredWindowClippingMargins(.bottom, maxWaterfallHeight * pointsPerMeter)
}
```

### World recenter — [16:44]

```swift
// World recenter

var body: some View {
    RealityView { content in
        // ...
    }
    .onWorldRecenter {
        recomputePositions()
    }
}
```

### Progressive immersion style — [17:58]

```swift
// Progressive immersion style

@State private var selectedStyle: ImmersionStyle = .progressive

var body: some Scene {
    ImmersiveSpace(id: "space") {
        ImmersiveView()
    }
    .immersionStyle(
        selection: $selectedStyle,
        in: .progressive(aspectRatio: .portrait))
}
```

### Mixed immersion style — [18:37]

```swift
// Mixed immersion style

@State private var selectedStyle: ImmersionStyle = .progressive

var body: some Scene {
    ImmersiveSpace(id: "space") {
        ImmersiveView()
    }
    .immersionStyle(selection: $selectedStyle, in: .mixed)
    .immersiveEnvironmentBehavior(.coexist)
}
```

### Remote immersive space — [20:14]

```swift
// Remote immersive space

// Presented on visionOS
RemoteImmersiveSpace(id: "preview-space") {
    CompositorLayer(configuration: config) { /* ... */ }
}

// Presented on macOS
WindowGroup("Main Stage", id: "main") {
    StageView()
}
```

### 'CompositorLayer' is a 'CompositorContent' — [20:48]

```swift
// 'CompositorLayer' is a 'CompositorContent'

struct ImmersiveContent: CompositorContent {
    @Environment(\.scenePhase) private var scenePhase

    var body: some CompositorContent {
        CompositorLayer { renderer in
            // ...
        }
        .onImmersionChange { oldImmersion, newImmersion in
            // ...
        }
    }
}
```

### Scene bridging — [23:00]

```swift
// Scene bridging

import UIKit
import SwiftUI

// Declare the scenes
class MyHostingSceneDelegate: NSObject, UIHostingSceneDelegate {
    static var rootScene: some Scene {
        WindowGroup(id: "my-volume") {
            ContentView()
        }
        .windowStyle(.volumetric)
    }
}

// Create a request for the scene
let requestWithId = UISceneSessionActivationRequest(
    hostingDelegateClass: MyHostingSceneDelegate.self, id: "my-volume")!

// Send a request
UIApplication.shared.activateSceneSession(for: requestWithId)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/290/4/fb07fe18-8745-4cfd-8448-1879b8f207dc/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/290/4/fb07fe18-8745-4cfd-8448-1879b8f207dc/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/290) — developer.apple.com. Indexed for agent consumption._
