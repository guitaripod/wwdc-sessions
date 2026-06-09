---
id: "wwdc2021-10142"
event: "wwdc2021"
year: 2021
title: "Transition media gaplessly with HLS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10142"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Transition media gaplessly with HLS

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10142](https://developer.apple.com/videos/play/wwdc2021/10142)

Discover how you can create streaming media content that seamlessly transitions between episodes, songs, scenes, and individual resources. With gapless HLS playback, you can stitch together multiple pieces of content on the fly to create customized workouts, design interactive content, tell compelling stories, and more. We’ll show you how you can provide faithful continuity for streaming music, event recordings, and pre-recorded video and provide a captivating viewing experience within your app.

**Keywords:** `gapless`, `hls`, `http live streaming`, `media`, `transition`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,326 words)

## Documentation & Resources

- [HTTP Live Streaming - Overview](https://developer.apple.com/streaming/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/

## Code Snippets

### create two items, enqueue in order and play gaplessly — [6:12]

```swift
// create two items, enqueue in order, 
// and play gaplessly

let item1 = AVPlayerItem(url: url1)
let item2 = AVPlayerItem(url: url2)

let player = AVQueuePlayer()

player.insert(item1, after: nil)
player.insert(item2, after: item1)

player.play()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10142/14/423D5648-E58A-4CD1-A06F-1290EFA18BC4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10142/14/423D5648-E58A-4CD1-A06F-1290EFA18BC4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10142) — developer.apple.com. Indexed for agent consumption._
