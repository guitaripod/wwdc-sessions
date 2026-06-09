---
id: "wwdc2021-10290"
event: "wwdc2021"
year: 2021
title: "What's new in AVKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10290"
topics: ["Essentials", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in AVKit

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10290](https://developer.apple.com/videos/play/wwdc2021/10290)

Learn about enhancements to Picture in Picture and full screen improvements on macOS. Explore the new content source API, and learn how AVPictureInPictureController supports AVSampleBufferDisplayLayer, as well as recommended steps for an app to provide a seamless full screen experience on macOS or in a Mac Catalyst app.

**Keywords:** `avkit`, `picture in picture`, `pip`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,294 words)

## Documentation & Resources

- [AVKit](https://developer.apple.com/documentation/AVKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit.json

## Code Snippets

### New canStartPictureInPictureAutomaticallyFromInline property — [1:16]

```swift
// New property on AVPlayerViewController / AVPictureInPictureController.
var canStartPictureInPictureAutomaticallyFromInline: Bool { get set }
```

### Setting up AVPictureInPictureController with an AVPlayerLayer — [1:40]

```swift
func setupPictureInPicture() {
    // Ensure PiP is supported by current device.
    if AVPictureInPictureController.isPictureInPictureSupported() {
        // Create a new controller, passing the reference to the AVPlayerLayer.
        pictureInPictureController = AVPictureInPictureController(playerLayer: playerLayer)
        pictureInPictureController.delegate = self

        // Observe AVPictureInPictureController.isPictureInPicturePossible to update the PiP
        // button’s enabled state.
    } else {
        // PiP isn't supported by the current device. Disable the PiP button.
        pictureInPictureButton.isEnabled = false
    }
}
```

### Starting and stopping picture in picture — [2:11]

```swift
@IBAction func togglePictureInPictureMode(_ sender: UIButton) {
    if pictureInPictureController.isPictureInPictureActive {
        pictureInPictureController.stopPictureInPicture()
    } else {
        pictureInPictureController.startPictureInPicture()
    }
}
```

### AVPictureInPictureSampleBufferPlaybackDelegate — [2:56]

```swift
public protocol AVPictureInPictureSampleBufferPlaybackDelegate: NSObjectProtocol{

    // Delegate is responsible for:
    //
    // - Supplying playback state information for PiP UI.
    // - Responding to user input from PiP UI.

}
```

### Toggle playback of the video and seek back / ahead 15 seconds — [3:17]

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, setPlaying playing: Bool)

func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime, completion completionHandler: @escaping () -› Void)
```

### Provide elapsed time information — [3:31]

```swift
func pictureInPictureControllerTimeRangeForPlayback(_ pictureInPictureController: AVPictureInPictureController) -> CMTimeRange
```

### Choose appropriate media variant for render size — [3:51]

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, didTransitionToRenderSize newRenderSize: CMVideoDimensions)
```

### Update playback state — [4:06]

```swift
func pictureInPictureControllerIsPlaybackPaused(pictureInPictureController: AVPictureInPictureController) -> Bool
```

### iOS / MacCatalyst - Persist full screen playback — [6:05]

```swift
func playerViewController(_ playerViewController: AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator coordinator: UIViewControllerTransitionCoordinator) {
    coordinator.animate(alongsideTransition: nil) { context in
        // Keep a strong reference to the playerViewController while in full screen.
        self.detachedPlayerViewController = playerViewController
    }
}
```

### iOS / MacCatalyst - Release the playerViewController — [6:38]

```swift
func playerViewController(_ playerViewController: AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator coordinator: UIViewControllerTransitionCoordinator){
    coordinator.animate(alongsideTransition: nil) { context in
        // Stop keeping the playerViewController alive when transition completes,
        self.detachedPlayerViewController = nil
    }
}
```

### Persist full screen playback on macOS — [6:46]

```swift
func playerViewWillEnterFullScreen(_ playerView: AVPlayerView) {
    // Start keeping the player view alive while it is not in the view hierarchy.
    self.detachedPlayerView = playerView
}

func playerViewWillExitFullScreen(_ playerView: AVPlayerView) {
    // Stop keeping the player view alive.
    self.detachedPlayerView = nil
}
```

### Restoring UI when exiting full screen — [6:55]

```swift
// Restoring UI when exiting full screen

// iOS / MacCatalyst
func playerViewControllerRestoreUserInterfaceForFullScreenExit(_ playerViewController: AVPlayerViewController) async -> Bool {
	// Custom UI restoration logic
	return true
}

// macOS
func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool {
	// custom UI restore logic here		
	return true
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10290/7/3B2EE1D3-46DD-48DC-8B8A-FDF061067D68/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10290/7/3B2EE1D3-46DD-48DC-8B8A-FDF061067D68/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10290) — developer.apple.com. Indexed for agent consumption._