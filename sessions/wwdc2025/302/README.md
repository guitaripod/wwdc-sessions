---
id: "wwdc2025-302"
event: "wwdc2025"
year: 2025
title: "Create a seamless multiview playback experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/302"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Create a seamless multiview playback experience

**Event:** WWDC25 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-302](https://developer.apple.com/videos/play/wwdc2025/302)

Learn how to build advanced multiview playback experiences in your app. We’ll cover how you can synchronize playback between multiple players, enhance multiview playback with seamless AirPlay integration, and optimize playback quality to deliver engaging multiview playback experiences.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,545 words)

## Documentation & Resources

- [AVRouting](https://developer.apple.com/documentation/AVRouting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVRouting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVRouting.json
- [Creating a seamless multiview playback experience](https://developer.apple.com/documentation/AVFoundation/creating-a-seamless-multiview-playback-experience) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/creating-a-seamless-multiview-playback-experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/creating-a-seamless-multiview-playback-experience.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Coordinate playback — [7:55]

```swift
import AVFoundation

var closeUpVideo = AVPlayer()
var birdsEyeVideo = AVPlayer()

let coordinationMedium = AVPlaybackCoordinationMedium()

do {
  try closeUpVideo.playbackCoordinator.coordinate(using: coordinationMedium)
}catch let error {
  // Handle error
}

do {
  try birdsEyeVideo.playbackCoordinator.coordinate(using: coordinationMedium)
}catch let error {
  // Handle error
}
```

### Set preferred participant — [13:17]

```swift
import AVFoundation
import AVRouting

var closeUpVideo = AVPlayer()
var birdsEyeVideo = AVPlayer()

let routingPlaybackArbiter = AVRoutingPlaybackArbiter.shared()

routingPlaybackArbiter.preferredParticipantForExternalPlayback = birdsEyeVideo

routingPlaybackArbiter.preferredParticipantForNonMixableAudioRoutes = birdsEyeVideo
```

### Set network resource priority — [16:15]

```swift
birdsEyeVideo.networkResourcePriority = .high
closeUpVideo.networkResourcePriority = .low
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/302/5/87e78c55-cb0a-4d6f-9567-bc3f91ecb747/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/302/5/87e78c55-cb0a-4d6f-9567-bc3f91ecb747/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/302) — developer.apple.com. Indexed for agent consumption._