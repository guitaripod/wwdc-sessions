---
id: "wwdc2021-10146"
event: "wwdc2021"
year: 2021
title: "What’s new in AVFoundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10146"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What’s new in AVFoundation

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10146](https://developer.apple.com/videos/play/wwdc2021/10146)

Discover the latest updates to AVFoundation, Apple’s framework for inspecting, playing, and authoring audiovisual presentations. We’ll explore how you can use AVFoundation to query attributes of audiovisual assets, further customize your custom video compositions with timed metadata, and author caption files.

**Keywords:** `asset`, `authoring`, `avasset`, `avfoundation`, `composition`, `inspection`, `media`, `metadata`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,895 words)

## Documentation & Resources

- [Loading media data asynchronously](https://developer.apple.com/documentation/AVFoundation/loading-media-data-asynchronously) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/loading-media-data-asynchronously
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/loading-media-data-asynchronously.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### AVAsset property loading — [2:16]

```swift
func inspectAsset() async throws {
	let asset = AVAsset(url: movieURL)
	let duration = try await asset.load(.duration)
	myFunction(thatUses: duration)
}
```

### Load multiple properties — [4:02]

```swift
func inspectAsset() async throws {
	let asset = AVAsset(url: movieURL)
	let (duration, tracks) = try await asset.load(.duration, .tracks)
	myFunction(thatUses: duration, and: tracks)
}
```

### Check status — [4:52]

```swift
switch asset.status(of: .duration) {
case .notYetLoaded:
	// This is the initial state after creating an asset. 
case .loading:
	// This means the asset is actively doing work.
case .loaded(let duration):
	// Use the asset's property value.
case .failed(let error):
	// Handle the error.
}
```

### Async filtering methods — [6:32]

```swift
let asset: AVAsset
let trk1 = try await asset.loadTrack(withTrackID: 1)
let atrs = try await asset.loadTracks(withMediaType: .audio)
let ltrs = try await asset.loadTracks(withMediaCharacteristic: .legible)
let qtmd = try await asset.loadMetadata(for: .quickTimeMetadata)
let chcl = try await asset.loadChapterMetadataGroups(withTitleLocale: .current)
let chpl = try await asset.loadChapterMetadataGroups(bestMatchingPreferredLanguages: ["en-US"])
let amsg = try await asset.loadMediaSelectionGroup(for: .audible)

let track: AVAssetTrack
let seg0 = try await track.loadSegment(forTrackTime: .zero)
let spts = try await track.loadSamplePresentationTime(forTrackTime: .zero)
let ismd = try await track.loadMetadata(for: .isoUserData)
let fbtr = try await track.loadAssociatedTracks(ofType: .audioFallback)
```

### Async loading: Old API — [7:16]

```swift
asset.loadValuesAsynchronously(forKeys: ["duration", "tracks"]) {
	var error: NSError?
	guard asset.statusOfValue(forKey: "duration", error: &error) == .loaded else { ... }
	guard asset.statusOfValue(forKey: "tracks", error: &error) == .loaded else { ... }
	let duration = asset.duration
	let audioTracks = asset.tracks(withMediaType: .audio)
	// Use duration and audioTracks.
}
```

### This is the equivalent using the new API: — [8:09]

```swift
let duration = try await asset.load(.duration)
let audioTracks = try await asset.loadTracks(withMediaType: .audio)
// Use duration and audioTracks.
```

### load(_:) — [8:36]

```swift
let tracks = try await asset.load(.tracks)
```

### Async filtering method — [8:51]

```swift
let audioTracks = try await
    asset.loadTracks(withMediaType: .audio)
```

### status(of:) — [8:58]

```swift
switch status(of: .tracks) {
    case .loaded(let tracks):
    // Use tracks.
```

### load(_:) again (returns cached value) — [9:18]

```swift
let tracks = try await asset.load(.tracks)
```

### Assert status is .loaded() — [9:49]

```swift
guard case .loaded (let tracks)
    = asset.status(of: .tracks) else { ... }
```

### Custom video composition with metadata: Setup — [11:49]

```swift
/*
 Source movie:
 - Track 1: Audio
 - Track 2: Video
 - Track 3: Video
 - Track 4: Metadata
 - Track 5: Metadata
 - Track 6: Metadata
 */

// Tell AVMutableVideoComposition about all the metadata tracks.
videoComposition.sourceSampleDataTrackIDs = [4, 5]

// For each AVMutableVideoCompositionInstruction, specify the metadata track ID(s) to include.
instruction1.requiredSourceSampleDataTrackIDs = [4]
instruction2.requiredSourceSampleDataTrackIDs = [4, 5]
```

### Custom video composition with metadata: Compositing — [12:44]

```swift
// This is an implementation of a AVVideoCompositing method:
func startRequest(_ request: AVAsynchronousVideoCompositionRequest) {
	for trackID in request.sourceSampleDataTrackIDs {
		let metadata: AVTimedMetadataGroup? = request.sourceTimedMetadata(byTrackID: trackID)
		// To get CMSampleBuffers instead, use sourceSampleBuffer(byTrackID:).

	}

	// Compose input video frames, using metadata, here.

	request.finish(withComposedVideoFrame: composedFrame)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10146/5/DB6BBE8F-5AF9-4331-BF7B-F8DF5AC43A92/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10146/5/DB6BBE8F-5AF9-4331-BF7B-F8DF5AC43A92/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10146) — developer.apple.com. Indexed for agent consumption._
