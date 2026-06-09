---
id: "wwdc2020-10010"
event: "wwdc2020"
year: 2020
title: "Export HDR media in your app with AVFoundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10010"
topics: ["Developer Tools", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Export HDR media in your app with AVFoundation

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10010](https://developer.apple.com/videos/play/wwdc2020/10010)

Discover how to author and export high dynamic range (HDR) content in your app using AVFoundation. Learn about high dynamic range and how you can take advantage of it in your app. We’ll show you how to implement feature sets that allow people to export HDR content, go over supported HDR formats, review current restrictions, and explore the Apple platforms that support HDR export.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,557 words)

## Documentation & Resources

- [Core Media](https://developer.apple.com/documentation/CoreMedia) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMedia
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMedia.json
- [Learn more about AVFoundation](https://developer.apple.com/av-foundation/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/av-foundation/

## Code Snippets

### AVAssetExportSession Intro — [9:02]

```swift
// AVAssetExportSession code snippet

guard let exportSession = AVAssetExportSession(asset: sourceAsset,
                      presetName: AVAssetExportPresetHEVCHighestQuality) else {
	// Handle error
}

exportSession.outputURL = outputURL 
exportSession.outputFileType = AVFileTypeQuickTimeMovie 

exportSession.exportAsynchronouslyWithCompletionHandler {
	// Handle completion 
}
```

### AVAssetWriter with sourceFormatHint — [13:24]

```swift
// AVAssetWriter with sourceFormatHint

let assetWriter = try AVAssetWriter(url: outputURL, fileType: AVFileTypeQuickTimeMovie)

let outputSettings: [String: AnyObject] = [
			AVVideoCodecKey: AVVideoCodecTypeHEVC
		]

let assetWriterInput = AVAssetWriterInput(mediaType: AVMediaTypeVideo,
                                     outputSettings: outputSettings
                                   sourceFormatHint: videoFormatDescription)

assetWriter.add(assetWriterInput)

guard assetWriter.startWriting() else {
	throw assetWriter.error!
}
```

### AVAssetWriter with AVOutputSettingsAssistant — [14:13]

```swift
// AVAssetWriter with AVOutputSettingsAssistant

let assetWriter = try AVAssetWriter(url: outputURL, fileType: AVFileTypeQuickTimeMovie)

let settingsAssistant = AVOutputSettingsAssistant(
                                     preset: AVOutputSettingsPreset.hevc1920x1080)

settingsAssistant.sourceVideoFormat = videoFormatDescription

let newVideoSettings = settingsAssistant.videoSettings

// Modify a few fields in newVideoSettings here

let assetWriterInput = AVAssetWriterInput(mediaType: AVMediaTypeVideo,
                                     outputSettings: newVideoSettings)

assetWriter.add(assetWriterInput)
guard assetWriter.startWriting() else {
	throw assetWriter.error!
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10010/4/BA038DF7-160D-47A0-B92D-DA6F71360CCA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10010) — developer.apple.com. Indexed for agent consumption._
