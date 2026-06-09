---
id: "wwdc2021-10265"
event: "wwdc2021"
year: 2021
title: "Immerse your app in Spatial Audio"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10265"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Immerse your app in Spatial Audio

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10265](https://developer.apple.com/videos/play/wwdc2021/10265)

Discover how spatial audio can help you provide a theater-like experience for media in your apps and on the web. We’ll show you how you can easily bring immersive audio to those listening with compatible hardware, and how to automatically deliver different listening experiences depending on someone’s bandwidth or connection — all with little to no change to your code. And gain recommendations on how you can tailor the experience in your app and use spatial audio to tell stories in new, exciting ways.

**Keywords:** `atmos`, `audio`, `dolby`, `multichannel`, `multi channel`, `spatial`, `spatial audio`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,433 words)

## Documentation & Resources

- [Core Audio](https://developer.apple.com/documentation/CoreAudio) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAudio
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAudio.json

## Code Snippets

### Spatialization Formats — [6:55]

```swift
public struct AVAudioSpatializationFormats : OptionSet {

    public init(rawValue: UInt)


    public static var monoAndStereo: AVAudioSpatializationFormats { get }

    public static var multichannel: AVAudioSpatializationFormats { get }

    public static var monoStereoAndMultichannel: AVAudioSpatializationFormats { get }
}
```

### AVPlayerItem and AVSampleBufferAudioRenderer — [7:21]

```swift
@available(macOS 11.0, *)
var allowedAudioSpatializationFormats: Int32
```

### Spatial audio availability — [8:21]

```swift
@available(iOS 6.0, *)
class AVAudioSessionPortDescription : NSObject {

  @available(iOS 15.0, *)
  var isSpatialAudioEnabled: Bool { get }

 }
```

### Spatial audio availability — [8:35]

```swift
extension AVAudioSession {
  @available(iOS 15.0, *)
  class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name
}

@available(iOS 15.0, *)
let AVAudioSessionSpatialAudioEnabledKey: String
```

### Control center integration — [9:01]

```swift
extension AVAudioSession {
  @available(iOS 15.0, *)
  func setSupportsMultichannelContent(_ inValue: Bool) throws
  @available(iOS 15.0, *)
  var supportsMultichannelContent: Bool { get }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10265/4/9BD45E56-F096-4BDD-AAFA-CF90B0501E1B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10265/4/9BD45E56-F096-4BDD-AAFA-CF90B0501E1B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10265) — developer.apple.com. Indexed for agent consumption._
