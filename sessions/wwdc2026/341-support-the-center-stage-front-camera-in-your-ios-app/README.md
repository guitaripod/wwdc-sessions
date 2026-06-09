---
id: "wwdc2026-341"
event: "wwdc2026"
year: 2026
title: "Support the Center Stage front camera in your iOS app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/341"
topics: ["Photos & Camera"]
platforms: ["iOS"]
hasTranscript: true
---

# Support the Center Stage front camera in your iOS app

**Event:** WWDC26 · **Topic:** Photos & Camera · **Platforms:** iOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-341](https://developer.apple.com/videos/play/wwdc2026/341)

Supercharge your iOS camera app with Center Stage using AVCapture APIs with the front camera on iPhone 17, iPhone 17 Pro and iPhone Air. Explore how APIs enable zoom and rotate options, for more flexible ways to frame selfies and videos and to automatically get everyone in a group shot. Integrate Center Stage for video calls to automatically adjust the framing, so you’re front and center for virtual meetings and FaceTime calls. And learn how to stabilize your video for real-time video conferencing.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,938 words)

## Documentation & Resources

- [Supporting Center Stage front camera in your iOS app](https://developer.apple.com/documentation/AVFoundation/supporting-center-stage-front-camera-in-your-ios-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-center-stage-front-camera-in-your-ios-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-center-stage-front-camera-in-your-ios-app.json
- [AVCam: Building a camera app](https://developer.apple.com/documentation/AVFoundation/avcam-building-a-camera-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avcam-building-a-camera-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avcam-building-a-camera-app.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json
- [Capture setup](https://developer.apple.com/documentation/AVFoundation/capture-setup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capture-setup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capture-setup.json

## Code Snippets

### Support dynamic aspect ratio — [5:29]

```swift
// Select the Center Stage front camera

import AVFoundation

let deviceDiscoverySession = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInUltraWideCamera], mediaType: .video, position: .front)

guard let camera = deviceDiscoverySession.devices.first else {
    print("Failed to find the capture device")
    return
}

// Find a format that supports the 4x3 aspect ratio

for format in camera.formats {
    if format.supportedDynamicAspectRatios.contains(.ratio4x3) {
        try! camera.lockForConfiguration()
        camera.activeFormat = format
        camera.unlockForConfiguration()
        break
    }
}

// Set dynamic aspect ratio

try! camera.lockForConfiguration()

let timestamp = try! await camera.setDynamicAspectRatio(.ratio4x3)
print("Applied dynamic aspect ratio at timestamp: \(timestamp)")

camera.unlockForConfiguration()
```

### Support smart framing monitor — [7:39]

```swift
// Find a format that supports smart framing

import AVFoundation

for format in camera.formats {
    if format.isSmartFramingSupported {
        try! camera.lockForConfiguration()
        camera.activeFormat = format
        camera.unlockForConfiguration()
        break
    }
}

// Configure the smart framing monitor

let monitor = camera.smartFramingMonitor!

try! camera.lockForConfiguration()
monitor.enabledFramings = monitor.supportedFramings
camera.unlockForConfiguration()

// Monitor framing recommendations

observation = monitor.observe(\.recommendedFraming, options: [.new,]) { monitor, change in
    if let framing = monitor.recommendedFraming {

        Task {
            try! camera.lockForConfiguration()
            try! await camera.setDynamicAspectRatio(framing.aspectRatio)
            camera.videoZoomFactor = CGFloat(framing.zoomFactor)
            camera.unlockForConfiguration()
        }

    }
}

// Start the smart framing monitor

try! monitor.startMonitoring()

// Stop the smart framing monitor

observation?.invalidate()
observation = nil

monitor.stopMonitoring()
```

### Support Center Stage for video calls — [14:44]

```swift
// Find a format that supports Center Stage

import AVFoundation

for format in camera.formats {
    if format.isCenterStageSupported {
        try! camera.lockForConfiguration()
        camera.activeFormat = format
        camera.unlockForConfiguration()
        break
    }
}

// Turn on Center Stage

AVCaptureDevice.centerStageControlMode = .cooperative
AVCaptureDevice.isCenterStageEnabled = true
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/341/4/fa1380a3-e2ab-4442-9302-817be212e991/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/341/4/fa1380a3-e2ab-4442-9302-817be212e991/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/341) — developer.apple.com. Indexed for agent consumption._
