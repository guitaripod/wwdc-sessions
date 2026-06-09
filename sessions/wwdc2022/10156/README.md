---
id: "wwdc2022-10156"
event: "wwdc2022"
year: 2022
title: "Meet ScreenCaptureKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10156"
topics: ["Audio & Video", "Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# Meet ScreenCaptureKit

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10156](https://developer.apple.com/videos/play/wwdc2022/10156)

Learn how ScreenCaptureKit can deliver high-performance screen capture for your macOS screen sharing applications, video conferencing apps, game streaming services, and more. We'll explore the building blocks of this API, learn how to configure streams to capture on-screen video and audio content, and share tips for integrating it into your existing apps.

**Keywords:** `audio capture`, `screen capture`, `screencapturekit`, `streaming`, `video capture`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,874 words)

## Documentation & Resources

- [ScreenCaptureKit](https://developer.apple.com/documentation/ScreenCaptureKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ScreenCaptureKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ScreenCaptureKit.json
- [Capturing screen content in macOS](https://developer.apple.com/documentation/ScreenCaptureKit/capturing-screen-content-in-macos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ScreenCaptureKit/capturing-screen-content-in-macos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ScreenCaptureKit/capturing-screen-content-in-macos.json

## Code Snippets

### Creating a SCShareableContent object — [6:53]

```swift
// Creating a SCShareableContent object

// Get the content that's available to capture.
let content = try await SCShareableContent.excludingDesktopWindows(
    false,
    onScreenWindowsOnly: true
)
```

### Creating a SCContentFilter object — [8:32]

```swift
// Creating a SCContentFilter object

// Get the content that's available to capture.
let content = try await SCShareableContent.excludingDesktopWindows(
    false,
    onScreenWindowsOnly: true
)

// Exclude the sample app by matching the bundle identifier.
let excludedApps = content.applications.filter { app in
    Bundle.main.bundleIdentifier == app.bundleIdentifier
}

// Create a content filter that excludes the sample app.
filter = SCContentFilter(display: display,
                         excludingApplications: excludedApps,
                         exceptingWindows: [])
```

### Creating a SCStreamConfiguration object — [10:23]

```swift
// Creating a SCStreamConfiguration object
let streamConfig = SCStreamConfiguration()

// Set output resolution to 1080p
streamConfig.width = 1920
streamConfig.height = 1080

// Set the capture interval at 60 fps
streamConfig.minimumFrameInterval = CMTime(value: 1, timescale: CMTimeScale(60))

// Hides cursor
streamConfig.showsCursor = false

// Enable audio capture
streamConfig.capturesAudio = true

// Set sample rate to 48000 kHz stereo
streamConfig.sampleRate = 48000
streamConfig.channelCount = 2
```

### Creating and starting a SCStream object — [11:46]

```swift
// Creating and starting a SCStream object

// Create a capture stream with the filter and stream configuration
stream = SCStream(filter: filter, configuration: streamConfig, delegate: self)

// Start the capture session
try await stream?.startCapture()      


// ...
// Error handling delegate 
func stream(_ stream: SCStream, didStopWithError error: Error) {
    DispatchQueue.main.async {
        self.logger.error("Stream stopped with error: \(error.localizedDescription)")
        self.error = error
        self.isRecording = false
   }
}
```

### Getting media samples — [13:07]

```swift
// SCStreamOutput protocol implementation
func stream(_ stream: SCStream, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, of type: SCStreamOutputType) {
    switch type {
    case .screen:
        handleLatestScreenSample(sampleBuffer)
    case .audio:         handleLatestAudioSample(sampleBuffer)
    }
}

// ...
// Create a capture stream with the filter and stream configuration
stream = SCStream(filter: filter, configuration: streamConfig, delegate: self)

// Add a stream output to capture screen and audio content
try stream?.addStreamOutput(self, type: .screen, sampleHandlerQueue: screenFrameOutputQueue)
try stream?.addStreamOutput(self, type: .audio, sampleHandlerQueue: audioFrameOutputQueue)

// Start the capture session
try await stream?.startCapture()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10156/3/740DABB6-6584-492E-AA71-A628E023B346/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10156/3/740DABB6-6584-492E-AA71-A628E023B346/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10156) — developer.apple.com. Indexed for agent consumption._