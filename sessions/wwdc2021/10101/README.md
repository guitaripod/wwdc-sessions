---
id: "wwdc2021-10101"
event: "wwdc2021"
year: 2021
title: "Discover rolling clips with ReplayKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10101"
topics: ["Graphics & Games", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Discover rolling clips with ReplayKit

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10101](https://developer.apple.com/videos/play/wwdc2021/10101)

Never again miss anyone's great moment in your game or app. Learn about ReplayKit's latest update — clips screen recording — which provides your app with a rolling buffer of past video and audio samples. When memorable moments happen, discover how you can record and save it for people, and find out how you can surface those clips when they’re most relevant. Lastly, we’ll take you through integrating ReplayKit into your iOS and macOS apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,339 words)

## Documentation & Resources

- [Recording and Streaming Your macOS App](https://developer.apple.com/documentation/ReplayKit/recording-and-streaming-your-macos-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ReplayKit/recording-and-streaming-your-macos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ReplayKit/recording-and-streaming-your-macos-app.json
- [ReplayKit](https://developer.apple.com/documentation/ReplayKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ReplayKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ReplayKit.json

## Code Snippets

### Start clip buffering — [5:19]

```swift
// Start clip buffering API call

func startClipBuffering() {
    RPScreenRecorder.shared().startClipBuffering { error in
        if error != nil {
            print("Error attempting to start Clip Buffering")
            // Update the app recording state and UI.
            self.setClipState(active: false)
        } else {
            // No error encountered attempting to start a clip session.
            // Update the app recording state and UI.
            self.setClipState(active: true)

            // Set up camera View.
            self.setupCameraView()
        }
    }
}
```

### Stop clip buffering — [5:46]

```swift
// Stop clip buffering

func stopClipBuffering() {
    RPScreenRecorder.shared().stopClipBuffering { error in
        if error != nil {
            print("Error attempting to stop clip buffering")
        }
        // Update the app recording state and UI.
        self.setClipState(active: false)

        // Tear down camera view.
        self.tearDownCameraView()
    }
}
```

### Export clip button — [6:13]

```swift
// Export clip button

@IBAction func exportClipButtonTapped(_ sender: Any) {
    // If clip buffering is active, export clip
    if self.isActive && self.getClipButton.isEnabled {
        exportClip()
    }
}
```

### Export clip — [6:41]

```swift
// Export clip

func exportClip() {
    let clipURL = getAppTempDirectory()
    let interval = TimeInterval(5)

    print("Generating clip at URL: \(clipURL)")
    RPScreenRecorder.shared().exportClip(to: clipURL, duration: interval) { error in
        if error != nil {
            print("Error attempting to export clip")
        } else {
            // No error, so save clip at URL to photos
            self.saveToPhotos(tempURL: clipURL)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10101/7/50A5D34B-6D32-429A-B737-D3C0C9EB58B8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10101/7/50A5D34B-6D32-429A-B737-D3C0C9EB58B8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10101) — developer.apple.com. Indexed for agent consumption._