---
id: "wwdc2021-10143"
event: "wwdc2021"
year: 2021
title: "Explore HLS variants in AVFoundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10143"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore HLS variants in AVFoundation

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10143](https://developer.apple.com/videos/play/wwdc2021/10143)

Discover how you can use AVFoundation APIs to highlight different variants of your content within your app. We’ll show you how you can inspect HLS content using these APIs for different video characteristics, including attributes like SDR/HDR, FPS, and the like. And we’ll explore the AVAssetVariant, which represents streaming and offline content.

**Keywords:** `4k`, `hd`, `hls`, `sd`, `variants`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,282 words)

## Documentation & Resources

- [HTTP Live Streaming - Overview](https://developer.apple.com/streaming/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/streaming/

## Code Snippets

### HLS Master Playlist — [0:40]

```swift
#EXTM3U
#EXT-X-VERSION:7
#EXT-X-INDEPENDENT-SEGMENTS

#EXT-X-MEDIA:TYPE=AUDIO,NAME="English",GROUP-ID="stereo",LANGUAGE="en",DEFAULT=YES, AUTOSELECT=YES,CHANNELS="2",URI="en_stereo.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,NAME="French",GROUP-ID="stereo",LANGUAGE="fr",DEFAULT=NO, AUTOSELECT=YES,CHANNELS="2",URI="fr_stereo.m3u8"

#EXT-X-MEDIA:TYPE=AUDIO,NAME="English",GROUP-ID="atmos",LANGUAGE="en",DEFAULT=YES, AUTOSELECT=YES,CHANNELS="16/JOC",URI="en_atmos.m3u8"
#EXT-X-MEDIA:TYPE=AUDIO,NAME="French",GROUP-ID="atmos",LANGUAGE="fr",DEFAULT=NO, AUTOSELECT=YES,CHANNELS="16/JOC",URI="fr_atmos.m3u8"

#EXT-X-STREAM-INF:BANDWIDTH=14516883,VIDEO-RANGE=SDR,CODECS="avc1.64001f,mp4a.40.5", AUDIO="stereo",FRAME-RATE=23.976,RESOLUTION=1920x1080
sdr_variant.m3u8

#EXT-X-STREAM-INF:BANDWIDTH=34516883,VIDEO-RANGE=PQ,CODECS="dvh1.05.06,ec-3", AUDIO="atmos",FRAME-RATE=23.976,RESOLUTION=3840x1920
dovi_variant.m3u8
```

### Peak bitrate cap predicate — [3:38]

```swift
let peakBitRateCap = NSPredicate(format: "peakBitRate < 5000000")

let peakBitRateCapQualifier = AVAssetVariantQualifier(predicate: peakBitRateCap)
```

### HDR predicate — [3:55]

```swift
let hdrOnlyPredicate = NSPredicate(format: "videoAttributes.videoRange == %@", argumentArray: [AVVideoRange.pq])

let hdrOnlyQualifier = AVAssetVariantQualifier(predicate: hdrOnlyPredicate)
```

### Content configuration — [4:46]

```swift
let variantPref = AVAssetVariantQualifier(predicate: NSPredicate(format: "videoAttributes.videoRange == %@ && peakBitRate < 5000000", argumentArray: [AVVideoRange.pq]))

let myMediaSelections : [AVMediaSelection] = [enAudioMS, frAudioMS, enLegibleMS] //English, French audio and English subtitle renditions 

let contentConfig = AVAssetDownloadContentConfiguration()

contentConfig.variantQualifiers = [variantPref]

contentConfig.mediaSelections = myMediaSelections
```

### Download configuration — [6:29]

```swift
let asset = AVURLAsset(url: URL(string: "http://example.com/master.m3u8")!)
let dwConfig = AVAssetDownloadConfiguration(asset: asset, title: "my-title")

/* Primary content config */
let varPref = NSPredicate(format: "videoAttributes.videoRange == %@ && peakBitRate < 5000000", argumentArray: [AVVideoRange.pq])
let varQf = AVAssetVariantQualifier(predicate: varPref)

dwConfig.primaryContentConfiguration.variantQualifiers = [varQf]
dwConfig.primaryContentConfiguration.mediaSelections = [enAudioMS, frAudioMS, enLegibleMS] //English, French audio and English subtitle renditions 

/* Aux content config */
let auxVarPref = NSPredicate(format: "%d IN audioAttributes.formatIDs", argumentArray: [kAudioFormatAppleLossless])
let auxVarQf = AVAssetVariantQualifier(predicate: auxVarPref)

let auxContentConfig = AVAssetDownloadContentConfiguration()
auxContentConfig.variantQualifiers = [auxVarQf]
auxContentConfig.mediaSelections = [enAudioMS] //english audio
dwConfig.auxiliaryContentConfigurations = [auxContentConfig]

dwConfig.optimizesAuxiliaryContentConfigurations = true
```

### Download task — [7:42]

```swift
let myAssetDownloadDelegate = MyDownloadDelegate()
let avurlsession = AVAssetDownloadURLSession(configuration: URLSessionConfiguration.background(withIdentifier: "my-background-session"), assetDownloadDelegate: myAssetDownloadDelegate, delegateQueue: OperationQueue.main)

let asset = AVURLAsset(url: URL(string: "http://example.com/master.m3u8")!)
let dwConfig = AVAssetDownloadConfiguration(asset: asset, title: “my-title”)

...

let downloadTask = avurlsession.makeAssetDownloadTask(downloadConfiguration: dwConfig)

downloadTask.resume()

let progress = downloadTask.progress
```

### Direct variant selection — [8:10]

```swift
/* Example for direct variant selection */

let asset = AVURLAsset(url: URL(string: "http://example.com/master.m3u8")!)
let dwConfig = AVAssetDownloadConfiguration(asset: asset, title: "my-title")

/* Primary content config */
let myVariant : AVAssetVariant = ...
let myMediaSelections : [AVMediaSelection] = ...

let variantQf = AVAssetVariantQualifier(variant: myVariant)

dwConfig.primaryContentConfiguration.variantQualifiers = [variantQf]
dwConfig.primaryContentConfiguration.mediaSelections = myMediaSelections

/* Aux content config */
let myAuxVariant : AVAssetVariant = ...
let myAuxMediaSelections : [AVMediaSelection] = ...

let auxVariantQf = AVAssetVariantQualifier(variant: myAuxVariant)

let auxContentConfig = AVAssetDownloadContentConfiguration()
auxContentConfig.variantQualifiers = [auxVariantQf]
auxContentConfig.mediaSelections = myAuxMediaSelections
dwConfig.auxiliaryContentConfigurations = [auxContentConfig]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10143/8/02A20AB5-0C7F-4E9F-B252-75A25D1261ED/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10143/8/02A20AB5-0C7F-4E9F-B252-75A25D1261ED/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10143) — developer.apple.com. Indexed for agent consumption._
