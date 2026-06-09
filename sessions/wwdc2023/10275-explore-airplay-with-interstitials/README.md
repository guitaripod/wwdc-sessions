---
id: "wwdc2023-10275"
event: "wwdc2023"
year: 2023
title: "Explore AirPlay with interstitials"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10275"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Explore AirPlay with interstitials

**Event:** WWDC23 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10275](https://developer.apple.com/videos/play/wwdc2023/10275)

Learn how you can use HLS Interstitials with AirPlay to create seamless transitions for your video content between advertisements. We’ll share best practices and tips for creating a great experience when sharing content from Apple devices to popular smart TVs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,734 words)

## Documentation & Resources

- [AirPlay-Enabled TVs and Video Accessories](https://www.apple.com/home-app/accessories/#section-tvs) _documentation_
- [Media playback](https://developer.apple.com/documentation/AVFoundation/media-playback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/media-playback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/media-playback.json
- [Supporting AirPlay in your app](https://developer.apple.com/documentation/AVFoundation/supporting-airplay-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-airplay-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-airplay-in-your-app.json
- [Getting Started with HLS Interstitials](https://developer.apple.com/streaming/GettingStartedWithHLSInterstitials.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/GettingStartedWithHLSInterstitials.pdf

## Code Snippets

### Example: Navigation restriction client driven — [9:19]

```swift
let player = AVPlayer(url: movieURL) //no ads in primary
let controller = AVPlayerInterstitialEventController( primaryPlayer: player )

let ad1Item = [AVPlayerItem(url: ad1Url)]
let ad1event = AVPlayerInterstitialEvent( primaryItem: player.currentItem,
										  time: CMTime(seconds: 5, preferredTimescale: 1) )
ad1event.identifier = "ad1"
ad1event.templateItems = ad1Item

//set SKIP restriction on ad1 
ad1event.restrictions = [.requiresPlaybackAtPreferredRateForAdvancement]

controller.events = [ad1event]

 code snippet.
```

### Plan C: Sample code to override the restrictions — [15:44]

```swift
let player = AVPlayer( url: movieURL )
let controller = AVPlayerInterstitialEventController( primaryPlayer: player )

let ad1Event = controller.events[0]
let ad2Event = controller.events[1]

let newEvent  = ad2Event.copy() as! AVPlayerInterstitialEvent
//clear the restrictions on ad2 event
newEvent.restrictions = []

//set the original ad1 Event and modified ad2 Event on controller
controller.events = [ad1Event, newEvent]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10275/5/9AAAFD03-718B-497E-8A61-C0B00CC14513/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10275/5/9AAAFD03-718B-497E-8A61-C0B00CC14513/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10275) — developer.apple.com. Indexed for agent consumption._
