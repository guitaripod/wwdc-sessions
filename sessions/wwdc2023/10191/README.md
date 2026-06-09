---
id: "wwdc2023-10191"
event: "wwdc2023"
year: 2023
title: "Meet Object Capture for iOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10191"
topics: ["Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Meet Object Capture for iOS

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10191](https://developer.apple.com/videos/play/wwdc2023/10191)

Discover how you can offer an end-to-end Object Capture experience directly in your iOS apps to help people turn their objects into ready-to-use 3D models. Learn how you can create a fully automated Object Capture scan flow with our sample app and how you can assist people in automatically capturing the best content for their model. We’ll also discuss LiDAR data and provide best practices for scanning objects.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,850 words)

## Code Snippets

### Instantiating ObjectCaptureSession — [10:03]

```swift
import RealityKit
import SwiftUI 

var session = ObjectCaptureSession()
```

### Starting the session — [10:25]

```swift
var configuration = ObjectCaptureSession.Configuration()
configuration.checkpointDirectory = getDocumentsDir().appendingPathComponent("Snapshots/")

session.start(imagesDirectory: getDocumentsDir().appendingPathComponent("Images/"),
              configuration: configuration)
```

### Creating ObjectCaptureView — [10:50]

```swift
import RealityKit
import SwiftUI

struct CapturePrimaryView: View {
    var body: some View {
        ZStack {
            ObjectCaptureView(session: session)
        }
    }
}
```

### Transition to detecting state — [11:20]

```swift
var body: some View {
    ZStack {
        ObjectCaptureView(session: session)
        if case .ready = session.state {
            CreateButton(label: "Continue") { 
                session.startDetecting() 
            }
        }
    }
}
```

### Showing ObjectCaptureView — [11:36]

```swift
var body: some View {
    ZStack {
        ObjectCaptureView(session: session)
    }
}
```

### Transition to capturing state — [12:04]

```swift
var body: some View {
    ZStack {
        ObjectCaptureView(session: session)
        if case .ready = session.state {
            CreateButton(label: "Continue") { 
                session.startDetecting()
            }
        } else if case .detecting = session.state {
            CreateButton(label: "Start Capture") { 
                session.startCapturing()
            }
        }
    }
}
```

### Showing ObjectCaptureView — [12:27]

```swift
var body: some View {
    ZStack {
        ObjectCaptureView(session: session)
    }
}
```

### Completed scan pass — [12:50]

```swift
var body: some View {
    if session.userCompletedScanPass {
        VStack {
        }
    } else {
        ZStack {
            ObjectCaptureView(session: session)
        }
    }
}
```

### Transition to finishing state — [14:03]

```swift
var body: some View {
    if session.userCompletedScanPass {
        VStack {
            CreateButton(label: "Finish") {
                session.finish() 
            }
        }
   } else {
        ZStack {
            ObjectCaptureView(session: session)
        }
    }
}
```

### Point cloud view — [15:00]

```swift
var body: some View {
    if session.userCompletedScanPass {
        VStack {
            ObjectCapturePointCloudView(session: session)
            CreateButton(label: "Finish") {
                session.finish() 
            }
        }
    } else {    
        ZStack {
            ObjectCaptureView(session: session)
        }
    }
}
```

### Reconstruction API — [15:50]

```swift
var body: some View {
ReconstructionProgressView()
    .task {
        var configuration = PhotogrammetrySession.Configuration()
        configuration.checkpointDirectory = getDocumentsDir()
            .appendingPathComponent("Snapshots/")
        let session = try PhotogrammetrySession(
            input: getDocumentsDir().appendingPathComponent("Images/"),
            configuration: configuration)
        try session.process(requests: [ 
            .modelFile(url: getDocumentsDir().appendingPathComponent("model.usdz")) 
        ])
        for try await output in session.outputs {
            switch output {
                case .processingComplete:
                    handleComplete()
                    // Handle other Output messages here.
            }}}}
```

### Capturing for Mac — [17:02]

```swift
// Capturing for Mac

var configuration = ObjectCaptureSession.Configuration()
configuration.isOverCaptureEnabled = true

session.start(imagesDirectory: getDocumentsDir().appendingPathComponent("Images/"),
              configuration: configuration)
```

### Pose output — [18:40]

```swift
// Pose output

try session.process(requests: [ 
    .poses 
    .modelFile(url: modelURL),
])
for try await output in session.outputs {
    switch output {
    case .poses(let poses):
        handlePoses(poses)
    case .processingComplete:
        handleComplete()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10191/4/4163D349-9555-463C-B8F1-0839D7BC6E49/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10191/4/4163D349-9555-463C-B8F1-0839D7BC6E49/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10191) — developer.apple.com. Indexed for agent consumption._