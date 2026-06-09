---
id: "wwdc2022-110380"
event: "wwdc2022"
year: 2022
title: "Display ads and interstitials in SharePlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110380"
topics: ["App Services", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Display ads and interstitials in SharePlay

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110380](https://developer.apple.com/videos/play/wwdc2022/110380)

Find out how you can deliver a coordinated playback experience in SharePlay when your app delivers different ad schedules to each participant. We'll explore how to build playback experiences with stitched-in ads and scheduled HLS interstitials, and share tips and best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,875 words)

## Code Snippets

### Specific sample accurate time ranges that represent ads or interstitials — [5:13]

```swift
class MyAVPlayerCoordinatorDelegate : NSObject, AVPlayerPlaybackCoordinatorDelegate
{   
    func playbackCoordinator(_ coordinator: AVPlayerPlaybackCoordinator,     interstitialTimeRangesFor playerItem: AVPlayerItem) -> [NSValue]
 {
        return interstitialTimeRanges
     }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110380/4/F37ED64E-304D-423D-B8FA-17687B8EC980/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110380/4/F37ED64E-304D-423D-B8FA-17687B8EC980/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110380) — developer.apple.com. Indexed for agent consumption._