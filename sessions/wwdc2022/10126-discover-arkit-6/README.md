---
id: "wwdc2022-10126"
event: "wwdc2022"
year: 2022
title: "Discover ARKit 6"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10126"
topics: ["Essentials", "Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Discover ARKit 6

**Event:** WWDC22 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10126](https://developer.apple.com/videos/play/wwdc2022/10126)

Discover how you can build more refined and powerful augmented reality apps with ARKit 6. We'll explore how you can create AR experiences rendered in 4K HDR and take you through camera settings customizations for your app. We'll also share how you can export high-resolution still images from an ARKit session, take advantage of Plane Estimation and Motion Capture, and add AR Location Anchors in new regions.

**Keywords:** `ar`, `arkit`, `augmented reality`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,654 words)

## Documentation & Resources

- [Human Interface Guidelines: Augmented reality](https://developer.apple.com/design/human-interface-guidelines/augmented-reality) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/augmented-reality
- [Explore the ARKit Developer Forums](https://developer.apple.com/forums/tags/arkit) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/arkit
- [Tracking geographic locations in AR](https://developer.apple.com/documentation/ARKit/tracking-geographic-locations-in-ar) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/tracking-geographic-locations-in-ar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/tracking-geographic-locations-in-ar.json
- [ARKit](https://developer.apple.com/documentation/ARKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit.json

## Code Snippets

### HighRes Capturing — [5:00]

```swift
if let hiResCaptureVideoFormat = ARWorldTrackingConfiguration.recommendedVideoFormatForHighResolutionFrameCapturing {
    // Assign the video format that supports hi-res capturing.
config.videoFormat = hiResCaptureVideoFormat
}
// Run the session.
session.run(config)
```

### highRes background photos — [10:55]

```swift
session.captureHighResolutionFrame { (frame, error) in
   if let frame = frame {
      saveHiResImage(frame.capturedImage)
   }
}
```

### HDR support — [12:00]

```swift
if (config.videoFormat.isVideoHDRSupported) {
    config.videoHDRAllowed = true
}
session.run(config)
```

### AVCapture Session — [12:35]

```swift
if let device = ARWorldTrackingConfiguration.configurableCaptureDeviceForPrimaryCamera {
   do {
      try device.lockForConfiguration()
      // configure AVCaptureDevice settings
      …
      device.unlockForConfiguration()
   } catch {
      // error handling
      …
   }
}
```

### plane anchors — [16:00]

```swift
// Create a model entity sized to the plane's extent.
let planeEntity = ModelEntity(
    mesh: .generatePlane (
        width: planeExtent.width, 
        depth: planeExtent.height),
    materials: [material])

// Orient the entity.
planeEntity.transform = Transform(
    pitch: 0, 
    yaw: planeExtent.rotationOnYAxis, 
    roll: 0)

// Center the entity on the plane.
planeEntity.transform.translation = planeAnchor.center
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10126/4/042EC236-E96E-4969-A68A-1D379C84D647/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10126/4/042EC236-E96E-4969-A68A-1D379C84D647/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10126) — developer.apple.com. Indexed for agent consumption._
