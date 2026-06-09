---
id: "wwdc2020-10011"
event: "wwdc2020"
year: 2020
title: "Author fragmented MPEG-4 content with AVAssetWriter"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10011"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Author fragmented MPEG-4 content with AVAssetWriter

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10011](https://developer.apple.com/videos/play/wwdc2020/10011)

Transform your audio and video content into fragmented MPEG-4 files for a faster and smoother HLS streaming experience. Learn how to work with the fragmented MPEG-4 format, generate fragmented content from a movie, and set up AVAssetWriter to create fragments for HLS output.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,589 words)

## Documentation & Resources

- [Writing fragmented MPEG-4 files for HTTP Live Streaming](https://developer.apple.com/documentation/AVFoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming.json

## Code Snippets

### Instantiate AVAssetWriter and input — [5:36]

```swift
// Instantiate asset writer
let assetWriter = AVAssetWriter(contentType: UTType(AVFileType.mp4.rawValue)!)

// Add inputs
let videoInput = AVAssetWriterInput(mediaType: .video, outputSettings: compressionSettings)

assetWriter.add(videoInput)
```

### Configure AVAssetWriter — [6:28]

```swift
assetWriter.outputFileTypeProfile = .mpeg4AppleHLS

assetWriter.preferredOutputSegmentInterval = CMTime(seconds: 6.0, preferredTimescale: 1)

assetWriter.initialSegmentStartTime = myInitialSegmentStartTime

assetWriter.delegate = myDelegateObject
```

### Delegate methods — [8:00]

```swift
optional func assetWriter(_ writer: AVAssetWriter, didOutputSegmentData segmentData: Data, segmentType: AVAssetSegmentType)


optional func assetWriter(_ writer: AVAssetWriter, didOutputSegmentData segmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)
```

### AVAssetSegmentType — [8:37]

```swift
public enum AVAssetSegmentType : Int {
    case initialization = 1 
    case separable = 2
}
```

### Custom segmentation — [13:45]

```swift
// Set properties
assetWriter.outputFileTypeProfile = .mpeg4AppleHLS

assetWriter.preferredOutputSegmentInterval = .indefinite

assetWriter.delegate = myDelegateObject

// Passthrough
let videoInput = AVAssetWriterInput(mediaType: .video, outputSettings: nil)
```

### Audio has dependencies — [15:17]

```swift
extension AVAssetTrack {
       /* indicates whether this audio track has dependencies (e.g. kAudioFormatMPEGD_USAC) */
    open var hasAudioSampleDependencies: Bool { get }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10011/2/090FF01F-98C7-410F-85B3-EB5551BFBD57/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10011) — developer.apple.com. Indexed for agent consumption._
