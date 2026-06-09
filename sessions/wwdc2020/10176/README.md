---
id: "wwdc2020-10176"
event: "wwdc2020"
year: 2020
title: "Master Picture in Picture on tvOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10176"
topics: ["SwiftUI & UI Frameworks", "Audio & Video"]
platforms: ["tvOS"]
hasTranscript: true
---

# Master Picture in Picture on tvOS

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** tvOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10176](https://developer.apple.com/videos/play/wwdc2020/10176)

Picture in Picture is coming to Apple TV: With simultaneous video playback and the ability to swap between full screen content and Picture in Picture, you’ve never had more multitasking flexibility within your tvOS app. Discover how you can add AVPictureInPictureController to your project, leverage familiar APIs to create custom playback interfaces, and implement the best playback experience possible for people using your app. We'll also show you how to migrate away from the "swipe up" gesture to activate customOverlayViewController, as AVPlayerViewController now uses that gesture in tvOS 14.

To get the most out of this session, you should have a basic understanding of AVKit. For more information, watch "Delivering Intuitive Media Playback with AVKit."

We can't wait to see how you take advantage of tvOS’s unique Picture in Picture features with AVPlayerViewController.

**Keywords:** `appletv`, `apple tv`, `apple tv 4k`, `apple tv developer`, `avpictureinpicturecontroller`, `picture in picture`, `picture-in-picture`, `pip`, `tv`, `tv app`, `tv app dev`, `tv app developer`, `tv dev`, `tv developer`, `tvos`, `tvos dev`, `tvos developer`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,899 words)

## Documentation & Resources

- [Human Interface Guidelines: Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/playing-video
- [Adopting Picture in Picture Playback in tvOS](https://developer.apple.com/documentation/AVKit/adopting-picture-in-picture-playback-in-tvos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/adopting-picture-in-picture-playback-in-tvos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/adopting-picture-in-picture-playback-in-tvos.json
- [Adopting Picture in Picture in a Standard Player](https://developer.apple.com/documentation/AVKit/adopting-picture-in-picture-in-a-standard-player) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/adopting-picture-in-picture-in-a-standard-player
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/adopting-picture-in-picture-in-a-standard-player.json
- [Adopting Picture in Picture in a Custom Player](https://developer.apple.com/documentation/AVKit/adopting-picture-in-picture-in-a-custom-player) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/adopting-picture-in-picture-in-a-custom-player
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/adopting-picture-in-picture-in-a-custom-player.json

## Code Snippets

### Setting up your app's audio session — [2:13]

```swift
let audioSession = AVAudioSession.sharedInstance()
do {
    try audioSession.setCategory(.playback)
} catch {
    print("Setting category to AVAudioSessionCategoryPlayback failed.")
}
```

### Observering canStopPictureInPicture — [5:57]

```swift
_ = pipController.observe(\.canStopPictureInPicture) { controller, change in
    // Update your UI
    if controller.canStopPictureInPicture {
        pipActions = [.swap, .stop]
    } else {
        pipActions = [.start]
    }
}
```

### Tying AVPlayer with MPNowPlayingSession — [7:06]

```swift
final class CustomPlayerViewController: UIViewController {

    init(player: AVPlayer) {       
        let playerLayer = AVPlayerLayer(player: player)       
        pictureInPictureController = AVPictureInPictureController(playerLayer: playerLayer)

        nowPlayingSession = MPNowPlayingSession(players: [player])
    }

    private func publishNowPlayingMetadata() {
        nowPlayingSession.nowPlayingInfoCenter.nowPlayingInfo = // Your Now Playing info
        nowPlayingSession.becomeActiveIfPossible()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10176/2/4E16A761-E513-4658-9F3F-4BC73B38271A/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10176) — developer.apple.com. Indexed for agent consumption._