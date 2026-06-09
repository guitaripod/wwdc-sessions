---
id: "wwdc2026-303"
event: "wwdc2026"
year: 2026
title: "Build a responsive camera app that launches quickly"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/303"
topics: ["Audio & Video", "Photos & Camera"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build a responsive camera app that launches quickly

**Event:** WWDC26 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-303](https://developer.apple.com/videos/play/wwdc2026/303)

Discover how to build a camera app that launches instantly so people never miss the perfect shot. Explore how to optimize the entire camera launch sequence — from app startup to first preview frame. Ensure your app has a polished camera experience by learning about new API’s that deliver faster launches, and best practices for smooth preview rendering and maintaining sustainable performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,965 words)

## Documentation & Resources

- [Performance and metrics](https://developer.apple.com/documentation/Xcode/performance-and-metrics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/performance-and-metrics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/performance-and-metrics.json
- [AVCam: Building a camera app](https://developer.apple.com/documentation/AVFoundation/avcam-building-a-camera-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avcam-building-a-camera-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avcam-building-a-camera-app.json

## Code Snippets

### Automatic deferred start delegate — [9:14]

```swift
import AVFoundation

class DeferredStartDelegate: NSObject, AVCaptureSessionDeferredStartDelegate {
    func sessionWillRunDeferredStart(_ session: AVCaptureSession)
    {
        // This is called before deferred start begins for the deferred outputs
    }

    func sessionDidRunDeferredStart(_ session: AVCaptureSession)
    {
        // This is called after deferred start completes for all outputs
    }
}
```

### Adopt automatic deferred start — [9:46]

```swift
import AVFoundation

let captureSession = AVCaptureSession()
captureSession.beginConfiguration()
captureSession.automaticallyRunsDeferredStart = true

let videoPreviewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
videoPreviewLayer.isDeferredStartEnabled = false

let photoOutput = AVCapturePhotoOutput()
photoOutput.isDeferredStartEnabled = true
captureSession.addOutput(photoOutput)

captureSession.setDeferredStartDelegate(deferredStartDelegate, deferredStartDelegateCallbackQueue: sessionQueue)

captureSession.commitConfiguration()
captureSession.startRunning()
```

### Adopt manual deferred start — [11:30]

```swift
import AVFoundation

let captureSession = AVCaptureSession()
captureSession.beginConfiguration()
captureSession.automaticallyRunsDeferredStart = false

let videoOutput = AVCaptureVideoDataOutput()
captureSession.addOutput(videoOutput)
videoOutput.isDeferredStartEnabled = false

let photoOutput = AVCapturePhotoOutput()
photoOutput.isDeferredStartEnabled = true
captureSession.addOutput(photoOutput)

captureSession.setDeferredStartDelegate(deferredStartDelegate, deferredStartDelegateCallbackQueue: sessionQueue)

captureSession.commitConfiguration()
captureSession.startRunning()
```

### Manage runDeferredStartWhenNeeded — [11:53]

```swift
import AVFoundation
import QuartzCore

private var firstFramePresented = false
guard let drawable = layer.nextDrawable()
if (!firstFramePresented) {
    drawable.addPresentedHandler({ drawable in
        // Set up postponed UI elements
        captureSession.runDeferredStartWhenNeeded()
    })
    firstFramePresented = true
}
```

### Enable responsive capture — [14:07]

```swift
import AVFoundation

func configurePhotoOutput(for session: AVCaptureSession, device: AVCaptureDevice) {
    let photoOutput = AVCapturePhotoOutput()

    guard session.canAddOutput(photoOutput) else { return }
    session.addOutput(photoOutput)

    photoOutput.maxPhotoQualityPrioritization = .quality
    // Responsive capture lets the photo output capture immediately
    photoOutput.isResponsiveCaptureEnabled = photoOutput.isResponsiveCaptureSupported
}
```

### Monitor for system pressure — [20:16]

```swift
import AVFoundation

let captureSession = AVCaptureSession()
let device = activeVideoInput?.device
captureSession.beginConfiguration()
// ...
captureSession.commitConfiguration()

guard captureSession.hardwareCost <= 1.0 else {
    print("hardwareCost \(captureSession.hardwareCost) — cannot start session. Reconfiguring.")
    setupLowCostConfiguration()
}

captureSession.startRunning()
let systemPressureObserver = device?.observe(\.systemPressureState,
                                               options: [.initial, .new],
                                               changeHandler: { /* Handle state change */ })
```

### Manage pro video storage — [22:17]

```swift
import AVFoundation

func configureProVideoStorage() {
    guard AVProVideoStorage.isSupported else { return }
    let storage = AVProVideoStorage.shared
    guard storage.remainingCapacity != 0 else {
        storage.openSettings()
        return
    }
}
```

### Adopt AVProVideoStorage for deterministic file write speeds — [22:43]

```swift
import AVFoundation

guard AVProVideoStorage.isSupported else { return }
guard let pvs = AVProVideoStorage.shared else { return }

// Configure and set up AVCaptureSession, AVCaptureConnections and format
// ...
let movieOutput = AVCaptureMovieFileOutput()

guard movieOutput.isProVideoStorageSupported else { return }
guard !pvs.isBusy else { return }

let movieFileURL = FileManager.default.temporaryDirectory
            .appendingPathComponent(UUID().uuidString)
            .appendingPathExtension("mov")

movieOutput.usesProVideoStorage = true // Also available with AVAssetWriter
movieOutput.startRecording(to: movieFileURL, recordingDelegate: delegate)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/303/5/fb6dc55a-c026-4ce1-9902-7a744fef4c99/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/303/5/fb6dc55a-c026-4ce1-9902-7a744fef4c99/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/303) — developer.apple.com. Indexed for agent consumption._
