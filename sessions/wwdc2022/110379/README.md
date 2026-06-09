---
id: "wwdc2022-110379"
event: "wwdc2022"
year: 2022
title: "Create a more responsive media app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110379"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Create a more responsive media app

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110379](https://developer.apple.com/videos/play/wwdc2022/110379)

Discover how you can use AVFoundation to keep people focused on your media app’s content — not your loading spinner. We’ll show you how to support a responsive and fluid interface in your app, all while you create rich audiovisual compositions, load audiovisual assets, and prepare media thumbnails. Find out how you can perform these tasks on your app’s main thread while I/O processes in parallel, learn how to get top-notch playback performance when loading data from custom storage, and more. 

To get the most out of this session, we recommend first watching "What's new in AVFoundation” from WWDC21.

**Keywords:** `async load`, `avasset`, `avassetresourceloader`, `avasynchronouskeyvalueloading`, `avcomposition`, `latency`, `thumbnail`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,649 words)

## Documentation & Resources

- [Creating images from a video asset](https://developer.apple.com/documentation/AVFoundation/creating-images-from-a-video-asset) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/creating-images-from-a-video-asset
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/creating-images-from-a-video-asset.json
- [Loading media data asynchronously](https://developer.apple.com/documentation/AVFoundation/loading-media-data-asynchronously) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/loading-media-data-asynchronously
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/loading-media-data-asynchronously.json

## Code Snippets

### Generate a thumbnail — [1:41]

```swift
func thumbnail() async throws -> UIImage {
    let generator = AVAssetImageGenerator(asset: asset)
    generator.requestedTimeToleranceBefore = .zero
    generator.requestedTimeToleranceAfter = CMTime(seconds: 3, preferredTimescale: 600)
    let thumbnail = try await generator.image(at: time).image
    return UIImage(cgImage: thumbnail)
}
```

### Generate a series of thumbnails — [2:56]

```swift
func timelineThumbnails(for times: [CMTime]) async {
    for await result in generator.images(for: times) {
        switch result {
        case .success(requestedTime: let requestedTime, image: let image, actualTime: _):
            updateThumbnail(for: requestedTime, with: image)
        case .failed(requestedTime: let requestedTime, error: _):
            updateThumbnail(for: requestedTime, with: placeholder)
        }
    }
}
```

### Generate a series of thumbnails — [3:49]

```swift
func timelineThumbnails(for times: [CMTime]) async {
    for await result in generator.images(for: times) {
        updateThumbnail(for: result.requestedTime, with: (try? result.image) ?? placeholder)
    }
}
```

### AVMutableComposition — [4:40]

```swift
let composition = AVMutableComposition()
try await composition.insertTimeRange(timeRange, of: asset, at: startTime)
```

### AVVideoComposition — [4:57]

```swift
let videoComposition = try await AVVideoComposition .videoComposition(withPropertiesOf: asset)

try await videoComposition.isValid(for: asset, timeRange: range, validationDelegate: delegate)
```

### Asset inspection — [5:33]

```swift
asset.loadValuesAsynchronously(forKeys: ["duration", "tracks"]) {
    guard asset.statusOfValue(forKey: "duration", error: &error) == .loaded else { ... }
    guard asset.statusOfValue(forKey: "tracks", error: &error) == .loaded else { ... }
    myFunction(thatUses: asset.duration, and: asset.tracks)
}

let (duration, tracks) = try await asset.load(.duration, .tracks)
myFunction(thatUses: duration, and: tracks)
```

### Synchronously insert track segments into a composition — [7:06]

```swift
// videoTrack1: AVAssetTrack, videoTrack2: AVAssetTrack

// Create a composition and add an empty track
let composition = AVMutableComposition()
guard let compositionTrack = composition
    .addMutableTrack(withMediaType: .video,
                     preferredTrackID: 1) else { return }

// Append the first 5 seconds of track 1
try compositionTrack
    .insertTimeRange(firstFiveSeconds,
                     of: videoTrack1, at: .zero)

// Append the first 5 seconds of track 2
try compositionTrack
    .insertTimeRange(firstFiveSeconds,
                     of: videoTrack2, at: fiveSeconds)
myFunction(thatUses: composition.duration,
           and: composition.tracks)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110379/3/072CE81E-54AA-400F-82CC-3667BB3549E1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110379/3/072CE81E-54AA-400F-82CC-3667BB3549E1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110379) — developer.apple.com. Indexed for agent consumption._