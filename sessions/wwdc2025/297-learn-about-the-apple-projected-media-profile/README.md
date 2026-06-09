---
id: "wwdc2025-297"
event: "wwdc2025"
year: 2025
title: "Learn about the Apple Projected Media Profile"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/297"
topics: ["Audio & Video", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Learn about the Apple Projected Media Profile

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-297](https://developer.apple.com/videos/play/wwdc2025/297)

Dive into the Apple Projected Media Profile (APMP) and see how APMP enables 180º/360º and Wide FoV projections in QuickTime and MP4 files using Video Extended Usage signaling. We’ll provide guidance on using OS-provided frameworks and tools to convert, read/write, edit, and encode media containing APMP. And we’ll review Apple Positional Audio Codec’s (APAC) capabilities for creating and delivering spatial audio content for the most immersive experiences.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,453 words)

## Documentation & Resources

- [QuickTime and ISO Base Media File Formats and Spatial and Immersive Media](https://developer.apple.com/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/av-foundation/Stereo-Video-ISOBMFF-Extensions.pdf
- [Converting projected video to Apple Projected Media Profile](https://developer.apple.com/documentation/AVFoundation/converting-projected-video-to-apple-projected-media-profile) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/converting-projected-video-to-apple-projected-media-profile
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/converting-projected-video-to-apple-projected-media-profile.json
- [Apple HEVC Stereo Video Interoperability Profile](https://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/av-foundation/HEVC-Stereo-Video-Profile.pdf
- [Using Apple’s HTTP Live Streaming (HLS) Tools](https://developer.apple.com/documentation/HTTP-Live-Streaming/using-apple-s-http-live-streaming-hls-tools) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HTTP-Live-Streaming/using-apple-s-http-live-streaming-hls-tools
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HTTP-Live-Streaming/using-apple-s-http-live-streaming-hls-tools.json
- [Core Media](https://developer.apple.com/documentation/CoreMedia) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMedia
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMedia.json
- [HTTP Live Streaming](https://developer.apple.com/documentation/HTTP-Live-Streaming) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HTTP-Live-Streaming
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HTTP-Live-Streaming.json
- [HTTP Live Streaming (HLS) authoring specification for Apple devices](https://developer.apple.com/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Recognize spherical v1/v2 equirectangular content — [8:58]

```swift
// Convert spherical v1/v2 RFC 180/360 equirectangular content

import AVFoundation

func wasConvertedFromSpherical(url: URL) -> Bool {
	let assetOptions = [AVURLAssetShouldParseExternalSphericalTagsKey: true]
	let urlAsset = AVURLAsset(url: url, options: assetOptions)

	// simplified for sample, assume first video track
	let track = try await urlAsset.loadTracks(withMediaType: .video).first!

	// Retrieve formatDescription from video track, simplified for sample assume first format description
	let formatDescription = try await videoTrack.load(.formatDescriptions).first

	// Detect if formatDescription includes extensions synthesized from spherical
	let wasConvertedFromSpherical = formatDescription.extensions[.convertedFromExternalSphericalTags]

	return wasConvertedFromSpherical
}
```

### Convert wide FOV content from supported cameras — [9:54]

```swift
// Convert wide-FOV content from recognized camera models
import ImmersiveMediaSupport

func upliftIntoParametricImmersiveIfPossible(url: URL) -> AVMutableMovie {
	let movie = AVMutableMovie(url: url)

	let assetInfo = try await ParametricImmersiveAssetInfo(asset: movie)
	if (assetInfo.isConvertible) {
		guard let newDescription = assetInfo.requiredFormatDescription else {
			fatalError("no format description for convertible asset")
		}
		let videoTracks = try await movie.loadTracks(withMediaType: .video)
		guard let videoTrack = videoTracks.first,
			  let currentDescription = try await videoTrack.load(.formatDescriptions).first
		else {
      fatalError("missing format description for video track")
		}
		// presumes that format already compatible for intended use case (delivery or production)
    // for delivery then if not already HEVC should transcode for example
		videoTrack.replaceFormatDescription(currentDescription, with: newDescription)
	}
  return movie
}
```

### Recognize Projected & Immersive Video — [10:58]

```swift
// Determine if an asset contains any tracks with nonRectilinearVideo and if so, whether any are AIV
import AVFoundation

func classifyProjectedMedia( movieURL: URL ) async -> (containsNonRectilinearVideo: Bool, containsAppleImmersiveVideo: Bool) {

	let asset = AVMovie(url: movieURL)
	let assistant = AVAssetPlaybackAssistant(asset: asset)
	let options = await assistant.playbackConfigurationOptions
	// Note contains(.nonRectilinearProjection) is true for both APMP & AIV, while contains(.appleImmersiveVideo) is true only for AIV
	return (options.contains(.nonRectilinearProjection), options.contains(.appleImmersiveVideo))
}
```

### Perform projection or viewPacking processing — [11:22]

```swift
import AVFoundation
import CoreMedia

// Perform projection or viewPacking specific processing
func handleProjectionAndViewPackingKind(_ movieURL: URL) async throws {

	let movie = AVMovie(url: movieURL)
	let track = try await movie.loadTracks(withMediaType: .video).first!
	let mediaCharacteristics = try await track.load(.mediaCharacteristics)

	// Check for presence of non-rectilinear projection
	if mediaCharacteristics.contains(.indicatesNonRectilinearProjection) {
		let formatDescriptions = try await track.load(.formatDescriptions)
		for formatDesc in formatDescriptions {
			if let projectionKind = formatDesc.extensions[.projectionKind] {
				if projectionKind == .projectionKind(.equirectangular) {
					// handle equirectangular (360) video
				} else if projectionKind == .projectionKind(.halfEquirectangular) {
					// handle 180 video
				} else if projectionKind == .projectionKind(.parametricImmersive) {
					// handle parametric wfov video
				} else if projectionKind == .projectionKind(.appleImmersiveVideo) {
					// handle AIV
				}
			}
			if let viewPackingKind = formatDesc.extensions[.viewPackingKind] {
				if viewPackingKind == .viewPackingKind(.sideBySide) {
					// handle side by side
				} else if viewPackingKind == .viewPackingKind(.overUnder) {
					// handle over under
				}
			}
		}
	}
}
```

### Specify outputBufferDescription for a stereoscopic pair — [12:51]

```swift
var config = try await AVVideoComposition.Configuration(for: asset)

	config.outputBufferDescription = [[.stereoView(.leftEye)], [.stereoView(.rightEye)]]

	let videoComposition = AVVideoComposition(configuration: config)
```

### Finish an asyncVideoCompositionRequest with tagged buffers — [13:01]

```swift
func startRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest) {
	var taggedBuffers: [CMTaggedDynamicBuffer] = []
	let MVHEVCLayerIDs = [0, 1]
	let eyes: [CMStereoViewComponents] = [.leftEye, .rightEye]

	for (layerID, eye) in zip(MVHEVCLayerIDs, eyes) {
		// take a monoscopic image and convert it to a z=0 stereo image with identical content for each eye
		let pixelBuffer = asyncVideoCompositionRequest.sourceReadOnlyPixelBuffer(byTrackID: 0)

		let tags: [CMTag] = [.videoLayerID(Int64(layerID)), .stereoView(eye)]
		let buffer = CMTaggedDynamicBuffer(tags: tags, content: .pixelBuffer(pixelBuffer!))
		taggedBuffers.append(buffer)
	}
	asyncVideoCompositionRequest.finish(withComposedTaggedBuffers: taggedBuffers)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/297/5/331d65eb-4973-4be1-a3b2-c1ae3ec8703a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/297/5/331d65eb-4973-4be1-a3b2-c1ae3ec8703a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/297) — developer.apple.com. Indexed for agent consumption._
