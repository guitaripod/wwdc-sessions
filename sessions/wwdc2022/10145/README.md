---
id: "wwdc2022-10145"
event: "wwdc2022"
year: 2022
title: "What’s new in HLS Interstitials"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10145"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in HLS Interstitials

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10145](https://developer.apple.com/videos/play/wwdc2022/10145)

HLS Interstitials can help you create seamless transitions in video content between advertisements, other interstitials, and your HLS streams. Learn how you can optimize your ad inventory, fine-tune interstitial presentation with SNAP-IN/OUT when using HLS, and more.

**Keywords:** `ad cueing`, `ads`, `avfoundation`, `cue`, `interstitials`, `mid rolls`, `pre rolls`, `snap`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,559 words)

## Code Snippets

### Client schedules an ad pod at 10s into primary asset — [7:58]

```swift
// Client schedules an ad pod at 10s into primary asset
let player  = AVPlayer( url: movieURL )  // no ads in primary asset
let controller = AVPlayerInterstitialEventController( primaryPlayer: player )
let adPodTemplates = [AVPlayerItem( url: ad1URL ), AVPlayerItem( url: ad2URL )]
let event = AVPlayerInterstitialEvent( primaryItem: player.currentItem,
                             time: CMTime( seconds: 10, preferredTimescale: 1 ),
                                     )
event.templateItems = adPodTemplates
event.identifier = "Ad1"
event.restrictions = []
event.resumptionOffset = .zero
event.playoutLimit = .invalid
event.cue = .none

controller.events = [event]
player.currentItem.translatesPlayerInterstitialEvents = true
let vc = AVPlayerViewController()
vc.player = player
player.play()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10145/4/1BA9D9C4-C8EC-4D33-A67A-2DFEBD032041/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10145/4/1BA9D9C4-C8EC-4D33-A67A-2DFEBD032041/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10145) — developer.apple.com. Indexed for agent consumption._