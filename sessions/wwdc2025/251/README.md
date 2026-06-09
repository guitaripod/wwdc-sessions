---
id: "wwdc2025-251"
event: "wwdc2025"
year: 2025
title: "Enhance your app’s audio recording capabilities"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/251"
topics: ["Audio & Video", "Spatial Computing", "Photos & Camera"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance your app’s audio recording capabilities

**Event:** WWDC25 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-251](https://developer.apple.com/videos/play/wwdc2025/251)

Learn how to improve your app’s audio recording functionality. Explore the flexibility of audio device selection using the input picker interaction on iOS and iPadOS 26. Discover APIs available for high-quality voice recording using AirPods. We’ll also introduce spatial audio recording and editing capabilities that allow you to isolate speech and ambient background sounds — all using the the AudioToolbox, AVFoundation, and Cinematic frameworks.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,444 words)

## Documentation & Resources

- [TN3177: Understanding alternate audio track groups in movie files](https://developer.apple.com/documentation/Technotes/tn3177-understanding-alternate-audio-track-groups-in-movie-files) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3177-understanding-alternate-audio-track-groups-in-movie-files
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3177-understanding-alternate-audio-track-groups-in-movie-files.json
- [Capturing Spatial Audio in your iOS app](https://developer.apple.com/documentation/AVFoundation/capturing-spatial-audio-in-your-ios-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-spatial-audio-in-your-ios-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-spatial-audio-in-your-ios-app.json
- [Editing Spatial Audio with an audio mix](https://developer.apple.com/documentation/Cinematic/editing-spatial-audio-with-an-audio-mix) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Cinematic/editing-spatial-audio-with-an-audio-mix
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Cinematic/editing-spatial-audio-with-an-audio-mix.json
- [Cinematic](https://developer.apple.com/documentation/Cinematic) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Cinematic
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Cinematic.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Input route selection — [2:10]

```swift
import AVKit

class AppViewController {

    // Configure AudioSession

    // AVInputPickerInteraction is a NSObject subclass that presents an input picker
    let inputPickerInteraction = AVInputPickerInteraction()   
    inputPickerInteraction.delegate = self

    // connect the PickerInteraction to a UI element for displaying the picker
    @IBOutlet weak var selectMicButton: UIButton!
    self.selectMicButton.addInteraction(self.inputPickerInteraction)

    // button press callback: present input picker UI
    @IBAction func handleSelectMicButton(_ sender: UIButton) {
	    inputPickerInteraction.present()
    }
}
```

### AirPods high quality recording — [3:57]

```swift
// AVAudioSession clients opt-in - session category option
AVAudioSessionCategoryOptions.bluetoothHighQualityRecording

// AVCaptureSession clients opt-in - captureSession property
session.configuresApplicationAudioSessionForBluetoothHighQualityRecording = true
```

### Audio Mix with AVPlayer — [13:26]

```swift
import Cinematic

// Audio Mix parameters (consider using UI elements to change these values)
var intensity: Float32 = 0.5 // values between 0.0 and 1.0
var style = CNSpatialAudioRenderingStyle.cinematic

// Initializes an instance of CNAssetAudioInfo for an AVAsset asynchronously
let audioInfo = try await CNAssetSpatialAudioInfo(asset: myAVAsset)

// Returns an AVAudioMix with effect intensity and rendering style.
let newAudioMix: AVAudioMix = audioInfo.audioMix(effectIntensity: intensity,
                                                 renderingStyle: style)

// Set the new AVAudioMix on your AVPlayerItem
myAVPlayerItem.audioMix = newAudioMix
```

### Get remix metadata from input file — [16:45]

```swift
// Get Spatial Audio remix metadata from input AVAsset

let audioInfo = try await CNAssetSpatialAudioInfo(asset: myAVAsset)

// extract the remix metadata. Set on AUAudioMix with AudioUnitSetProperty()
let remixMetadata = audioInfo.spatialAudioMixMetadata as CFData
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/251/4/d14e1f6d-5996-4c7a-8576-c7cb4e6eaf02/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/251/4/d14e1f6d-5996-4c7a-8576-c7cb4e6eaf02/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/251) — developer.apple.com. Indexed for agent consumption._