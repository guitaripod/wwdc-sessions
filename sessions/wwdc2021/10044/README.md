---
id: "wwdc2021-10044"
event: "wwdc2021"
year: 2021
title: "Explore ShazamKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10044"
topics: ["Spatial Computing", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore ShazamKit

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10044](https://developer.apple.com/videos/play/wwdc2021/10044)

Take advantage of Shazam’s exact audio matching capabilities within your app when you use ShazamKit. Learn how you can harness the immense Shazam catalog to create all sorts of experiences, including quickly recognizing the exact song playing in the background of a video captured by your app, offering dynamic visual effects based on the music playing in a room, or even syncing with external audio to provide companion app experiences. We’ll also show you how you can build custom catalogs within ShazamKit to match with any audio source — all on device.

For a deeper dive, check out “Create custom audio experiences with ShazamKit,” where you’ll code along with us and learn how to build an education app that synchronizes perfectly with streamed video content.

**Keywords:** `audio`, `music`, `musickit`, `shazam`, `shazamkit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,324 words)

## Documentation & Resources

- [ShazamKit](https://developer.apple.com/documentation/ShazamKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ShazamKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ShazamKit.json

## Code Snippets

### Matching signatures using SHSession — [9:11]

```swift
// Matching signatures using SHSession
let session = SHSession()
session.delegate = self

let signatureGenerator = SHSignatureGenerator()
try signatureGenerator.append(buffer, at: nil)

let signature = signatureGenerator.signature()
session.match(signature)
```

### Receive matches via session delegate — [10:45]

```swift
// Receiving matches via the session delegate
extension SongResultViewController: SHSessionDelegate {

    public func session(_ session: SHSession, didFind match: SHMatch) {

        guard let matchedMediaItem = match.mediaItems.first else {
            return
        }

        DispatchQueue.main.async {
            self.songView.titleLabel.text = matchedMediaItem.title
            self.songView.artistLabel.text = matchedMediaItem.artist
        }

    }
}
```

### Add to Shazam library — [12:24]

```swift
// Adding to a customer’s library
guard let matchedMediaItem = match.mediaItems.first else {
    return
}

SHMediaLibrary.default.add([matchedMediaItem]) { error in

    if error != nil {

        // handle the error
    }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10044/7/242BEFF9-E49D-4A96-972C-BEE65585211D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10044/7/242BEFF9-E49D-4A96-972C-BEE65585211D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10044) — developer.apple.com. Indexed for agent consumption._