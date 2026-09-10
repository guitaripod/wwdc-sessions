---
id: "tech-talks-111465"
event: "tech-talks"
year: 2026
title: "Build a great camera experience for iPhone Duo"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111465"
topics: ["SwiftUI & UI Frameworks", "Photos & Camera"]
platforms: ["iOS"]
hasTranscript: true
---

# Build a great camera experience for iPhone Duo

**Event:** Tech Talks · **Topic:** Photos & Camera · **Platforms:** iOS · **Published:** 2026-09-09 · **Session:** [tech-talks-111465](https://developer.apple.com/videos/play/tech-talks/111465)

Discover how to leverage the outer and inner cameras on iPhone Duo. Explore the Virtual Front Camera, and find out how to use the direction coordinator to switch between cameras and update your UI as people open and close iPhone Duo. Learn best practices for handling preview aspect ratios, positioning, and rotation to deliver a seamless capture experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,384 words)

## Code Snippets

### Understand AVCaptureDevicePosition — [3:00]

```swift
enum AVCaptureDevicePosition: Int {
    case unspecified
    case back
    case front
}

extension AVCaptureDevice {
    // ...
    var position: AVCaptureDevicePosition { get }
}
```

### Initialize a direction coordinator — [4:06]

```swift
directionCoordinator = AVCaptureDeviceDirectionCoordinator(
    view: view,
    deviceTypes: [
        .builtInOuterUltraWideCamera,
        .builtInInnerUltraWideCamera,
        .builtInDualWideCamera,
    ],
    changeHandler: { [weak self] map in
        self?.updateCameraSession(map)
    }
)
```

### Configure the video preview layer — [7:30]

```swift
class AVCaptureVideoPreviewLayer {
    // ...

    var videoGravity: AVLayerVideoGravity { get set }
}
```

### Select a dynamic aspect ratio — [7:51]

```swift
class AVCaptureDevice {
    // ...

    var dynamicAspectRatio: AVCaptureDevice.AspectRatio? { get }
}
```

### Disable sensor orientation compensation — [8:34]

```swift
// Disable for improved performance
class AVCapturePhotoOutput: AVCaptureOutput {
    // ...

    var isCameraSensorOrientationCompensationEnabled: Bool { get set }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111465/1/8972028b-c66c-469e-a410-df980b33271c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111465/1/8972028b-c66c-469e-a410-df980b33271c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111465) — developer.apple.com. Indexed for agent consumption._
