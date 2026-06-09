---
id: "wwdc2023-10238"
event: "wwdc2023"
year: 2023
title: "Tune up your AirPlay audio experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10238"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Tune up your AirPlay audio experience

**Event:** WWDC23 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10238](https://developer.apple.com/videos/play/wwdc2023/10238)

Learn how you can upgrade your app’s AirPlay audio experience to be more robust and responsive. We’ll show you how to adopt enhanced audio buffering with AVQueuePlayer, explore alternatives when building a custom player in your app, and share best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,493 words)

## Documentation & Resources

- [Playing custom audio with your own player](https://developer.apple.com/documentation/AVFAudio/playing-custom-audio-with-your-own-player) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFAudio/playing-custom-audio-with-your-own-player
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFAudio/playing-custom-audio-with-your-own-player.json
- [AVQueuePlayer](https://developer.apple.com/documentation/AVFoundation/AVQueuePlayer) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/AVQueuePlayer
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/AVQueuePlayer.json

## Code Snippets

### Set the audio type — [4:00]

```swift
let audioSession = AVAudioSession.sharedInstance()
try audioSession.setCategory(. playback ,xmode: . default , policy:.longFormAudio )
```

### AVQueuePlayer — [7:23]

```swift
let player = AVQueuePlayer()

let url = URL(string: "http://www.examplecontenturl.com")
let asset = AVAsset(url: url)
let item = AVPlayItem(asset: asset)

player.insert(item, after: nil)
player.play()
```

### Add the audio renderer to the render synchronizer — [8:28]

```swift
let serializationQueue = DispatchQueue(label: "sample.buffer.player.serialization.queue")
let audioRenderer = AVSampleBufferAudioRenderer()
let renderSynchronizer = AVSampleBufferRenderSynchronizer()

renderSynchronizer.addRenderer(audioRenderer)
```

### Enqueue audio data — [8:50]

```swift
serializationQueue.async { [weak self] in
    guard let self = self else { return }
    // Start processing audio data and stop when there's no more data.
    self.audioRenderer.requestMediaDataWhenReady(on: serializationQueue) { [weak self] in
        guard let self = self else { return }
        while self.audioRenderer.isReadyForMoreMediaData {
            let sampleBuffer = self.nextSampleBuffer() // Returns nil at end of data.
            if let sampleBuffer = sampleBuffer {
                self.audioRenderer.enqueue(sampleBuffer)
            } else {
                // Tell the renderer to stop requesting audio data.
                audioRenderer.stopRequestingMediaData()
            }
        }
    }

    // Start playback at the natural rate of the media.
    self.renderSynchronizer.rate = 1.0
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10238/4/5BA02CFE-52D4-497B-BD99-75E591F41885/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10238/4/5BA02CFE-52D4-497B-BD99-75E591F41885/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10238) — developer.apple.com. Indexed for agent consumption._
