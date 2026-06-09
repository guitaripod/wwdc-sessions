---
id: "wwdc2025-403"
event: "wwdc2025"
year: 2025
title: "Learn about Apple Immersive Video technologies"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/403"
topics: ["Audio & Video", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Learn about Apple Immersive Video technologies

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-403](https://developer.apple.com/videos/play/wwdc2025/403)

Explore the capabilities of Apple Immersive Video and Apple Spatial Audio Format technologies to create truly immersive experiences. Meet the new ImmersiveMediaSupport framework, which offers functionality to read and write the necessary metadata for enabling Apple Immersive Video. Learn guidelines for encoding and publishing Apple Immersive Video content in standalone files for playback or streaming via HLS. To get the most out of this session, we recommend first watching “Explore video experiences for visionOS.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,044 words)

## Documentation & Resources

- [Immersive Media Support](https://developer.apple.com/documentation/ImmersiveMediaSupport) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ImmersiveMediaSupport
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ImmersiveMediaSupport.json
- [Authoring Apple Immersive Video](https://developer.apple.com/documentation/ImmersiveMediaSupport/authoring-apple-immersive-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ImmersiveMediaSupport/authoring-apple-immersive-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ImmersiveMediaSupport/authoring-apple-immersive-video.json
- [What's new in HTTP Live Streaming](https://developer.apple.com/streaming/Whats-new-HLS.pdf) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/Whats-new-HLS.pdf
- [AVPlayerItemMetadataOutput](https://developer.apple.com/documentation/AVFoundation/AVPlayerItemMetadataOutput) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/AVPlayerItemMetadataOutput
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/AVPlayerItemMetadataOutput.json
- [Core Media](https://developer.apple.com/documentation/CoreMedia) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMedia
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMedia.json
- [HTTP Live Streaming (HLS) authoring specification for Apple devices](https://developer.apple.com/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HTTP-Live-Streaming/hls-authoring-specification-for-apple-devices.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Read VenueDescriptor from AIVU file — [6:23]

```swift
func readAIMEData(from aivuFile: URL) async throws -> VenueDescriptor? {
    let avAsset = AVURLAsset(url: aivuFile)
    let metadata = try await avAsset.load(.metadata)
    let aimeData = metadata.filter({ $0.identifier == .quickTimeMetadataAIMEData }).first
    if let dataValue = try await aimeData.load(.value) as? NSData {
        return try await VenueDescriptor(aimeData: dataValue as Data)
    }
    return nil
}
```

### Read PresentationDescriptor from AIVU playback — [6:50]

```swift
func presentation(timedMetadata: [AVTimedMetadataGroup]) async throws ->   
[PresentationDescriptor] {
    var presentations: [PresentationDescriptor] = [] 
    for group in timedMetadata {
        for metadata in group.items {
            if metadata.identifier == .quickTimeMetadataPresentationImmersiveMedia {
                let data = try await metadata.load(.dataValue) {
                    presentations.append(
                        try JSONDecoder().decode(PresentationDescriptor.self, from: data)
                    )
                }
            }
        }
    }
    return presentations
}
```

### Create AVMetadataItem from VenueDescriptor — [7:52]

```swift
func getMetadataItem(from metadata: VenueDescriptor) async throws -> AVMetadataItem {
    let aimeData = try await metadata.aimeData
    let aimeMetadataItem = AVMutableMetadataItem()
    aimeMetadataItem.identifier = .quickTimeMetadataAIMEData
    aimeMetadataItem.dataType = String(kCMMetadataBaseDataType_RawData)
    aimeMetadataItem.value = aimeData as NSData

    return aimeMetadataItem
}
```

### Create timed AVMetadataItem from PresentationDescriptorReader — [8:02]

```swift
func getMetadataItem(reader: PresentationDescriptorReader, 
                     time: CMTime, frameDuration: CMTime) -> AVMetadataItem? {
    let commands = reader.outputPresentationCommands(for: time) ?? []
    if commands.isEmpty { return nil }

    let descriptor = PresentationDescriptor(commands: commands)
    let encodedData = try JSONEncoder().encode(descriptor)
    let presentationMetadata = AVMutableMetadataItem()
    presentationMetadata.identifier = .quickTimeMetadataPresentationImmersiveMedia
    presentationMetadata.dataType = String(kCMMetadataBaseDataType_RawData)
    presentationMetadata.value = encodedData as NSData
    presentationMetadata.time = time
    presentationMetadata.duration = frameDuration

    return presentationMetadata
}
```

### Validate AIVU file — [8:20]

```swift
func validAIVU(file aivuFile: URL) async throws -> Bool { 
    return try await AIVUValidator.validate(url: aivuFile)
}
```

### Save AIME file — [9:31]

```swift
let aimeFile = FileManager.default.temporaryDirectory.appendingPathComponent("primary.aime")
try? await venueDescriptor.save(to: aimeFile)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/403/4/ef519281-1213-4ddf-892a-ca33ae288ef1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/403/4/ef519281-1213-4ddf-892a-ca33ae288ef1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/403) — developer.apple.com. Indexed for agent consumption._
