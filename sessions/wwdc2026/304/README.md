---
id: "wwdc2026-304"
event: "wwdc2026"
year: 2026
title: "Implement high resolution photo capture"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/304"
topics: ["Photos & Camera"]
platforms: ["iOS"]
hasTranscript: true
---

# Implement high resolution photo capture

**Event:** WWDC26 · **Topic:** Photos & Camera · **Platforms:** iOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-304](https://developer.apple.com/videos/play/wwdc2026/304)

Capture super high resolution photos in your app using AVFoundation. Learn when to use the three different options to capture images — RAW, exposure-bracketed, and fully processed. Walk through configuring photo capture for 24MP and 48MP images across the Main, Tele, and Ultra Wide cameras. And discover how deferred photo processing keeps your app responsive as more photos are taken.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,117 words)

## Documentation & Resources

- [Capturing photos in RAW and Apple ProRAW formats](https://developer.apple.com/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats.json
- [AVCam: Building a camera app](https://developer.apple.com/documentation/AVFoundation/avcam-building-a-camera-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avcam-building-a-camera-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avcam-building-a-camera-app.json

## Code Snippets

### Configure the AVCaptureSession — [5:26]

```swift
import AVFoundation

private let session = AVCaptureSession()
private func configureSession() {
    session.beginConfiguration()
    session.sessionPreset = .photo
}
```

### Configure AVCapturePhotoOutput — [6:11]

```swift
import AVFoundation

private let photoOutput = AVCapturePhotoOutput()
private let configurePhotoOutput: () -> Void = {
    photoOutput.maxPhotoQualityPrioritization = .quality // or .balanced
}
```

### Add maxPhotoDimensions to AVCapturePhotoOutput — [6:38]

```swift
import AVFoundation

let supportedMaxPhotoDimensions = device?.activeFormat.supportedMaxPhotoDimensions ?? []
if let largestDimension = supportedMaxPhotoDimensions.max(by: { lhs, rhs in
    Int(lhs.width) * Int(lhs.height) < Int(rhs.width) * Int(rhs.height)
} ) {
    photoOutput?.maxPhotoDimensions = largestDimension
}

session?.commitConfiguration()
session?.startRunning()
```

### Update AVCapturePhotoSettings — [7:21]

```swift
import AVFoundation

let settings = AVCapturePhotoSettings()
settings.maxPhotoDimensions = dimension.cmVideoDimensionsValue
settings.photoQualityPrioritization = .quality

var delegate: AVCapturePhotoCaptureDelegate?

// Configure photo request delegate

if let delegate {
 photoOutput?.capturePhoto(with: settings, delegate: delegate)
}
```

### Prepare resources for the capture — [8:59]

```swift
import AVFoundation

let prepareSettings = AVCapturePhotoSettings()
prepareSettings.maxPhotoDimensions = photoOutput.maxPhotoDimensions
prepareSettings.photoQualityPrioritization = .quality

photoOutput.setPreparedPhotoSettingsArray([prepareSettings]) { prepared, error in
  if let error = error {
    print("Failed to prepare: \(error)")
      return
  }
  print("Pipeline prepared: \(prepared)")
}

// Later, when ready to capture — create NEW settings
let captureSettings = AVCapturePhotoSettings()
captureSettings.maxPhotoDimensions = photoOutput.maxPhotoDimensions
captureSettings.photoQualityPrioritization = quality
photoOutput.capturePhoto(with: captureSettings, delegate: self)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/304/4/7a18d6ee-a63d-4402-bfb6-85a21dfac7dd/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/304/4/7a18d6ee-a63d-4402-bfb6-85a21dfac7dd/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/304) — developer.apple.com. Indexed for agent consumption._