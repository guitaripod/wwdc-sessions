---
id: "wwdc2025-253"
event: "wwdc2025"
year: 2025
title: "Enhancing your camera experience with capture controls"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/253"
topics: ["Photos & Camera"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Enhancing your camera experience with capture controls

**Event:** WWDC25 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-253](https://developer.apple.com/videos/play/wwdc2025/253)

Learn how to customize capture controls in your camera experiences. We’ll show you how to take photos with all physical capture controls, including new AirPods support, and how to adjust settings with Camera Control.

**Keywords:** `avfoundation`, `camera`, `capture`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,833 words)

## Documentation & Resources

- [Creating a camera experience for the Lock Screen](https://developer.apple.com/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen.json
- [Forum: Photos & Camera](https://developer.apple.com/forums/topics/media-technologies/photos-and-camera?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/media-technologies/photos-and-camera?cid=vf-a-0010
- [Supporting Continuity Camera in your tvOS app](https://developer.apple.com/documentation/AVKit/supporting-continuity-camera-in-your-tvos-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/supporting-continuity-camera-in-your-tvos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/supporting-continuity-camera-in-your-tvos-app.json
- [DockKit](https://developer.apple.com/documentation/DockKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DockKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DockKit.json
- [Creating a camera extension with Core Media I/O](https://developer.apple.com/documentation/coremediaio/creating_a_camera_extension_with_core_media_i_o) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/coremediaio/creating_a_camera_extension_with_core_media_i_o
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/coremediaio/creating_a_camera_extension_with_core_media_i_o.json
- [Accessing the camera while multitasking](https://developer.apple.com/documentation/avkit/accessing_the_camera_while_multitasking) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/avkit/accessing_the_camera_while_multitasking
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/avkit/accessing_the_camera_while_multitasking.json
- [Supporting Continuity Camera in your macOS app](https://developer.apple.com/documentation/AVFoundation/supporting-continuity-camera-in-your-macos-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-continuity-camera-in-your-macos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-continuity-camera-in-your-macos-app.json
- [Scanning data with the camera](https://developer.apple.com/documentation/VisionKit/scanning-data-with-the-camera) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VisionKit/scanning-data-with-the-camera
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VisionKit/scanning-data-with-the-camera.json
- [AVMultiCamPiP: Capturing from Multiple Cameras](https://developer.apple.com/documentation/AVFoundation/avmulticampip-capturing-from-multiple-cameras) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avmulticampip-capturing-from-multiple-cameras
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avmulticampip-capturing-from-multiple-cameras.json
- [Capturing photos with depth](https://developer.apple.com/documentation/AVFoundation/capturing-photos-with-depth) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-photos-with-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-photos-with-depth.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json
- [Capture setup](https://developer.apple.com/documentation/AVFoundation/capture-setup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capture-setup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capture-setup.json

## Code Snippets

### Initial PhotoCapture view setup — [5:35]

```swift
import SwiftUI

struct PhotoCapture: View {
    var body: some View {
        VStack {
            CameraView()
        }
    }
}
```

### Connecting a button to the camera model — [5:37]

```swift
import SwiftUI

struct PhotoCapture: View {
    let camera = CameraModel()
    var body: some View {
        VStack {
            CameraView()
            Button(action: camera.capturePhoto) {
                Text("Take a photo")
            }
        }
    }
}
```

### Importing AVKit — [6:10]

```swift
import AVKit
import SwiftUI

struct PhotoCapture: View {
    let camera = CameraModel()
    var body: some View {
        VStack {
            CameraView()
            Button(action: camera.capturePhoto) {
                Text("Take a photo")
            }
        }
    }
}
```

### Setting up onCameraCaptureEvent view modifier — [6:14]

```swift
import AVKit
import SwiftUI

struct PhotoCapture: View {
    let camera = CameraModel()
    var body: some View {
        VStack {
            CameraView()
            .onCameraCaptureEvent { event in
                if event.phase == .ended {
                   camera.capturePhoto()
                }
            }
            Button(action: camera.capturePhoto) {
                Text("Take a photo")
            }
        }
    }
}
```

### Default sound for onCameraCaptureEvent view modifier — [8:53]

```swift
.onCameraCaptureEvent { event
	if event.phase == .ended {
   	camera.capturePhoto() 
  }
}
```

### Play photo shutter sound on AirPod stem click — [9:13]

```swift
.onCameraCaptureEvent(defaultSoundDisabled: true) { event in
    if event.phase == .ended {a
        if event.shouldPlaySound {d
            event.play(.cameraShutter)
        }
    }
    camera.capturePhoto()
 }
```

### Add a build-in zoom slider to Camera Control — [14:46]

```swift
captureSession.beginConfiguration()

// configure device inputs and outputs

if captureSession.supportsControls {
    let zoomControl = AVCaptureSystemZoomSlider(device: device)

    if captureSession.canAddControl(zoomControl) {
        captureSession.addControl(zoomControl)
    }
}

captureSession.commitConfiguration()
```

### Modifying the built-in zoom slider to receive updates when zoom changes — [15:40]

```swift
let zoomControl = AVCaptureSystemZoomSlider(device: device) { [weak self] zoomFactor in
    self?.updateUI(zoomFactor: zoomFactor)
}
```

### Adding a custom reaction-effects picker alongside zoom slider — [16:46]

```swift
let reactions = device.availableReactionTypes.sorted { $0.rawValue < $1.rawValue }
let titles = reactions.map { localizedTitle(reaction: $0) }
let picker = AVCaptureIndexPicker(“Reactions", symbolName: “face.smiling.inverted”,
    localizedIndexTitles: titles)

picker.isEnabled = device.canPerformReactionEffects
picker.setActionQueue(sessionQueue) { index in
    device.performEffect(for: reactions[index])
}

let controls: [AVCaptureControl] = [zoomControl, picker]

for control in controls {
    if captureSession.canAddControl(control) {
        captureSession.addControl(control)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/253/4/61747dad-b349-43cc-83c6-782e690f2ae1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/253/4/61747dad-b349-43cc-83c6-782e690f2ae1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/253) — developer.apple.com. Indexed for agent consumption._
