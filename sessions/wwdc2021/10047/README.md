---
id: "wwdc2021-10047"
event: "wwdc2021"
year: 2021
title: "What’s new in camera capture"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10047"
topics: ["Photos & Camera"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in camera capture

**Event:** WWDC21 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10047](https://developer.apple.com/videos/play/wwdc2021/10047)

Learn how you can interact with Video Effects in Control Center including Center Stage, Portrait mode, and Mic modes. We’ll show you how to detect when these features have been enabled for your app and explore ways to adopt custom interfaces to make them controllable from within your app. Discover how to enable 10-bit HDR video capture and take advantage of minimum-focus-distance reporting for improved camera capture experiences. Explore support for IOSurface compression and delivering optimal performance in camera capture.

To learn more about camera capture, we also recommend watching "Capture high-quality photos using video formats" from WWDC21.

**Keywords:** `avcapture`, `camera`, `microphone`, `photo`, `photography`, `video`, `video effects`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,693 words)

## Documentation & Resources

- [Capture setup](https://developer.apple.com/documentation/AVFoundation/capture-setup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capture-setup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capture-setup.json

## Code Snippets

### Optimize QR code scanning — [0:01]

```swift
// Optimize the user experience for scanning QR codes down to sizes of 20mm x 20mm.

let deviceFieldOfView = self.videoDeviceInput.device.activeFormat.videoFieldOfView

let minSubjectDistance = minSubjectDistanceForCode(
  fieldOfView: deviceFieldOfView,
  minimumCodeSize: 20,
  previewFillPercentage: Float(rectOfInterestWidth))
```

### minSubjectDistance — [0:02]

```swift
private func minSubjectDistance(
  fieldOfView: Float,
  minimumCodeSize: Float,
  previewFillPercentage: Float) -> Float {
    let radians = degreesToRadians(fieldOfView / 2)
    let filledCodeSize = minimumCodeSize / previewFillPercentage
    return filledCodeSize / tan(radians)
}
```

### Lock device for configuration — [0:03]

```swift
let deviceMinimumFocusDistance = Float(self.videoDeviceInput.device.minimumFocusDistance)
if minimumSubjectDistanceForCode < deviceMinimumFocusDistance {
  let zoomFactor = deviceMinimumFocusDistance / minimumSubjectDistanceForCode
  do {
    try videoDeviceInput.device.lockForConfiguration()
    videoDeviceInput.device.videoZoomFactor = CGFloat(zoomFactor)
    videoDeviceInput.device.unlockForConfiguration()
  } catch {
    print("Could not lock for configuration: \(error)")
  }
}
```

### firstTenBitFormatOfDevice — [0:04]

```swift
func firstTenBitFormatOfDevice(device: AVCaptureDevice) -> AVCaptureDevice.Format? {
  for format in device.formats {
    let pixelFormat = CMFormatDescriptionGetMediaSubType(format.formatDescription)

    if pixelFormat == kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange /* 'x420' */ {
      return format
    }
  }
  return nil
}
```

### captureOutput — [0:05]

```swift
func captureOutput(
  _ output: AVCaptureOutput,
  didDrop sampleBuffer: CMSampleBuffer,
  from connection: AVCaptureConnection) {
    guard let attachment = sampleBuffer.attachments[.droppedFrameReason],
          let reason = attachment.value as? String else { return }
    switch reason as CFString {
    case kCMSampleBufferDroppedFrameReason_FrameWasLate:
      // Handle the late frame case.
      break
    case kCMSampleBufferDroppedFrameReason_OutOfBuffer:
      // Handle the out of buffers case.
      break
    case kCMSampleBufferDroppedFrameReason_Discontinuity:
      // Handle the discontinuity case.
      break
    default:
      fatalError("A frame dropped for an undefined reason.")
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10047/3/642D1BFE-7823-4CA8-8572-B2478B9C4B44/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10047/3/642D1BFE-7823-4CA8-8572-B2478B9C4B44/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10047) — developer.apple.com. Indexed for agent consumption._