---
id: "wwdc2024-10166"
event: "wwdc2024"
year: 2024
title: "Build compelling spatial photo and video experiences"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10166"
topics: ["Photos & Camera", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Build compelling spatial photo and video experiences

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10166](https://developer.apple.com/videos/play/wwdc2024/10166)

Learn how to adopt spatial photos and videos in your apps. Explore the different types of stereoscopic media and find out how to capture spatial videos in your iOS app on iPhone 15 Pro. Discover the various ways to detect and present spatial media, including the new QuickLook Preview Application API in visionOS. And take a deep dive into the metadata and stereo concepts that make a photo or video spatial.

**Keywords:** `audio &amp; video`, `camera`, `machine learning`, `photokit`, `spatial photos and videos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,726 words)

## Documentation & Resources

- [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.json
- [Writing spatial photos](https://developer.apple.com/documentation/ImageIO/writing-spatial-photos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ImageIO/writing-spatial-photos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ImageIO/writing-spatial-photos.json
- [Converting side-by-side 3D video to multiview HEVC and spatial video](https://developer.apple.com/documentation/AVFoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010
- [AVCam: Building a camera app](https://developer.apple.com/documentation/AVFoundation/avcam-building-a-camera-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avcam-building-a-camera-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avcam-building-a-camera-app.json

## Code Snippets

### Spatial video capture on iPhone 15 Pro — [6:19]

```swift
class CaptureManager {
    var session: AVCaptureSession!
    var input: AVCaptureDeviceInput!
    var output: AVCaptureMovieFileOutput!

    func setupSession() throws -> Bool {
        session = AVCaptureSession()
        session.beginConfiguration()

        guard let videoDevice = AVCaptureDevice.default(
            .builtInDualWideCamera, for: .video, position: .back
        ) else { return false }

        var foundSpatialFormat = false
        for format in videoDevice.formats {
            if format.isSpatialVideoCaptureSupported {
                try videoDevice.lockForConfiguration()
                videoDevice.activeFormat = format
                videoDevice.unlockForConfiguration()
                foundSpatialFormat = true
                break
            }
        }
        guard foundSpatialFormat else { return false }

        let videoDeviceInput = try AVCaptureDeviceInput(device: videoDevice)
        guard session.canAddInput(videoDeviceInput) else { return false }
        session.addInput(videoDeviceInput)
        input = videoDeviceInput

        let movieFileOutput = AVCaptureMovieFileOutput()
        guard session.canAddOutput(movieFileOutput) else { return false }
        session.addOutput(movieFileOutput)
        output = movieFileOutput

        guard let connection = output.connection(with: .video) else { return false }
        guard connection.isVideoStabilizationSupported else { return false }
        connection.preferredVideoStabilizationMode = .cinematicExtendedEnhanced

        guard movieFileOutput.isSpatialVideoCaptureSupported else { return false }
        movieFileOutput.isSpatialVideoCaptureEnabled = true

        session.commitConfiguration()
        session.startRunning()
        return true
    }

}
```

### Observing spatial capture discomfort reasons — [9:13]

```swift
let observation = videoDevice.observe(\.spatialCaptureDiscomfortReasons) { (device, change) in
    guard let newValue = change.newValue else { return }
    if newValue.contains(.subjectTooClose) {
        // Guide user to move back
    }
    if newValue.contains(.notEnoughLight) {
        // Guide user to find a brighter environment
    }
}
```

### PhotosPicker — [9:58]

```swift
import SwiftUI
import PhotosUI

struct PickerView: View {
    @State var selectedItem: PhotosPickerItem?
    var body: some View {
        PhotosPicker(selection: $selectedItem, matching: .spatialMedia) {
            Text("Choose a spatial photo or video")
        }
    }
}
```

### PhotoKit - all spatial assets — [10:14]

```swift
import Photos

func fetchSpatialAssets() {
    let fetchOptions = PHFetchOptions()
    fetchOptions.predicate = NSPredicate(
        format: "(mediaSubtypes & %d) != 0",
        argumentArray: [PHAssetMediaSubtype.spatialMedia.rawValue]
    )
    fetchResult = PHAsset.fetchAssets(with: fetchOptions)
}
```

### AVAssetPlaybackAssistant — [10:36]

```swift
import AVFoundation

extension AVURLAsset {
    func isSpatialVideo() async -> Bool {
        let assistant = AVAssetPlaybackAssistant(asset: self)
        let options = await assistant.playbackConfigurationOptions
        return options.contains(.spatialVideo)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10166/5/6FC98319-6431-448D-9962-370826A7F6FC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10166/5/6FC98319-6431-448D-9962-370826A7F6FC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10166) — developer.apple.com. Indexed for agent consumption._
