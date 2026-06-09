---
id: "wwdc2021-10140"
event: "wwdc2021"
year: 2021
title: "Explore dynamic pre-rolls and mid-rolls in HLS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10140"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Explore dynamic pre-rolls and mid-rolls in HLS

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10140](https://developer.apple.com/videos/play/wwdc2021/10140)

Learn how you can create seamless transitions between advertisements and your HLS streams. We’ll show you how to incorporate HLS tags and AVFoundation APIs to create media experiences that move easily between your primary content and mid-rolls, and provide best practices for playing these streams in your app.

**Keywords:** `ads`, `advertisements`, `interstitals`, `interstitial`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,668 words)

## Documentation & Resources

- [Getting Started with HLS Interstitials](https://developer.apple.com/streaming/GettingStartedWithHLSInterstitials.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/GettingStartedWithHLSInterstitials.pdf

## Code Snippets

### AVPlayerInterstitialEvent — [9:50]

```swift
class AVPlayerInterstitialEvent {
    var primaryItem: AVPlayerItem? { get }
    var identifier: String { get }
    var time: CMTime { get }
    var date: Date? { get }
    var templateItems: [AVPlayerItem] { get }
    var restrictions: AVPlayerInterstitialEvent.Restrictions { get }
    var resumptionOffset: CMTime { get }
    var playoutLimit: CMTime { get }
    var userDefinedAttributes: [AnyHashable : Any] { get }
}
```

### Observing server inserted events — [10:58]

```swift
// Client observes server-side interstitial playback
let player = AVPlayer(url: movieURL) // movieURL has EXT-X-DATERANGE ad tags
let observer = AVPlayerInterstitialEventMonitor(primaryPlayer: player)
NotificationCenter.default.addObserver(
  forName: AVPlayerInterstitialEventMonitor.currentEventDidChangeNotification,
  object: observer,
  queue: OperationQueue.main) {
      notification_ in
      self.updateUI(observer.currentEvent, observer.interstitialPlayer)
}
```

### AVPlayerInterstitialEventController — [11:40]

```swift
class AVPlayerInterstitialEventController : AVPlayerInterstitialEventMonitor {
    var events: [AVPlayerInterstitialEvent]!
    func cancelCurrentEvent(withResumptionOffset resumptionOffset: CMTime) 
}
```

### Client schedules ad pod — [12:01]

```swift
// Client inserted events

// Client schedules an ad pod at 10s into primary asset
let player  = AVPlayer(url: movieURL)  // no ads in primary asset
let controller = AVPlayerInterstitialEventController(primaryPlayer: player)
let adPodTemplates = [AVPlayerItem(url: ad1URL), AVPlayerItem(url: ad2URL)]
let event = AVPlayerInterstitialEvent( 
  primaryItem: player.currentItem,
  time: CMTime(seconds: 10, preferredTimescale: 1),
  templateItems: adPodTemplates,
  restrictions: [],
  resumptionOffset: .zero,
  playoutLimit: .invalid)

 controller.events = [event]
 player.currentItem.translatesPlayerInterstitialEvents = true
 let vc = AVPlayerViewController()
 vc.player = player
 player.play()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10140/15/4961CE04-6EAD-4B07-BD40-70010F74EF0D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10140/15/4961CE04-6EAD-4B07-BD40-70010F74EF0D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10140) — developer.apple.com. Indexed for agent consumption._