---
id: "wwdc2022-10147"
event: "wwdc2022"
year: 2022
title: "Create a great video playback experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10147"
topics: ["Health & Fitness", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Create a great video playback experience

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10147](https://developer.apple.com/videos/play/wwdc2022/10147)

Find out how you can use the latest iOS and iPadOS system media players to build amazing media apps. We’ll share how we designed the updated player and give you best practices and tips to help you design media experiences of your own. We’ll also explore Live Text for video and show you how to integrate interstitials and playback speed controls into your apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,566 words)

## Documentation & Resources

- [Human Interface Guidelines: Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/playing-video

## Code Snippets

### Setting content external metadata — [4:08]

```swift
// Setting content external metadata

let titleItem = AVMutableMetadataItem()
titleItem.identifier = .commonIdentifierTitle
titleItem.value = // Title string

let subtitleItem = AVMutableMetadataItem()
subtitleItem.identifier = .iTunesMetadataTrackSubTitle
subtitleItem.value = // Subtitle string

let infoItem = AVMutableMetadataItem()
infoItem.identifier = .commonIdentifierDescription
infoItem.value = // Descriptive info paragraph

playerItem.externalMetadata = [titleItem, subtitleItem, infoItem]
```

### Creating a skip button for a preroll ad — [19:03]

```swift
// Creating a skip button for a preroll ad

let eventController = AVPlayerInterstitialEventController(primaryPlayer: mediaPlayer)

let event = AVPlayerInterstitialEvent(primaryItem: interstitialItem, time: .zero)
event.restrictions = [
	.requiresPlaybackAtPreferredRateForAdvancement,
	.constrainsSeekingForwardInPrimaryContent
]

eventController.events.append(event)


func playerViewController(playerViewController: AVPlayerViewController, willPresent interstitial: AVInterstitialTimeRange) {
	showSkipButton(afterTime: 5.0, onPress: {
		eventController.cancelCurrentEvent(withResumptionOffset: CMTime.zero)
	})
}
```

### Setting custom playback speeds — [21:14]

```swift
// Setting custom playback speeds


let player = AVPlayerViewController()
player.player = // Some AVPlayer

present(player, animated: true)


let newSpeed = AVPlaybackSpeed(rate: 2.5, localizedName: "Two and a half times speed”)

player.speeds.append(newSpeed)
```

### Hiding the playback speed menu — [23:02]

```swift
// Hiding the playback speed menu


let player = AVPlayerViewController()
player.player = // Some AVPlayer

present(player, animated: true)


player.speeds = []
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10147/5/B7675782-6F3F-4D44-B56D-06CCE29D9E22/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10147/5/B7675782-6F3F-4D44-B56D-06CCE29D9E22/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10147) — developer.apple.com. Indexed for agent consumption._