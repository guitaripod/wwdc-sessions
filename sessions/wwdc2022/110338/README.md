---
id: "wwdc2022-110338"
event: "wwdc2022"
year: 2022
title: "Explore media metadata publishing and playback interactions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110338"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore media metadata publishing and playback interactions

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110338](https://developer.apple.com/videos/play/wwdc2022/110338)

Learn how you can highlight your app's Now Playing information on every platform. We'll take you through an overview of media metadata, learn how it gets represented in areas like the Lock Screen and Control Center, and show you how to write and publish effective media metadata for your content. We'll also explore how your app can respond to commands from other devices such as HomePod.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,515 words)

## Documentation & Resources

- [Media Player](https://developer.apple.com/documentation/MediaPlayer) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MediaPlayer
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MediaPlayer.json

## Code Snippets

### Instantiation examples — [4:34]

```swift
// playing Magnificent

self.session = MPNowPlayingSession(players: [player])



// Playing different WWDC sessions, one full screen and one in PiP

self.session = MPNowPlayingSession(players: [player])
self.pipSession = MPNowPlayingSession(players: [pipPlayer])



// playing multi-view race

self.session = MPNowPlayingSession(players: [topLeft, topRight, bottomLeft, bottomRight])
```

### Promoting and demoting sessions as Now Playing — [4:58]

```swift
// Promoting and demoting sessions as Now Playing

self.session = MPNowPlayingSession(players: [player])
self.pipSession = MPNowPlayingSession(players: [pipPlayer])

// if the content in PiP is promoted to full screen, swap active

self.pipSession.becomeActiveIfPossible { becameActive in
    // if success, pipSession data populates lock screen, etc, and
    // controls from lock screen, etc are routed to pipSession
}
```

### Responding to play and pause commands — [5:32]

```swift
// Example of responding to play and pause commands

self.session = MPNowPlayingSession(players: [player])

// respond to play commands
self.session.remoteCommandCenter.playCommand.addTarget { event in
    player.play()
    return .success
}

// respond to pause commands
self.session.remoteCommandCenter.pauseCommand.addTarget { event in
    player.pause()
    return .success
}
```

### Responding to skip forward commands — [6:22]

```swift
// Example responding to skip forward commands

self.session.remoteCommandCenter.skipForwardCommand.preferredIntervals = [15.0]
self.session.remoteCommandCenter.skipForwardCommand.addTarget { event in
    let skipCommand = event as! MPSkipIntervalCommandEvent
    player.seek(to: CMTimeAdd(player.currentTime(), CMTimeMakeWithSeconds(skipCommand.interval, preferredTimescale: 1)))
    return .success
}

// commands can also be disabled. for example, during an ad:
self.session.remoteCommandCenter.skipForwardCommand.isEnabled = false

// add handlers for all commands that are applicable to the content // https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter
```

### Setting artwork metadata with automatic publishing — [7:48]

```swift
// Example of setting artwork metadata
let artwork = MPMediaItemArtwork(image: image)
let title = "Magnificent"

playerItem.nowPlayingInfo = [
    MPMediaItemPropertyTitle: title,
    MPMediaItemPropertyArtwork: artwork,
    // …
]

self.session = MPNowPlayingSession(players: [player])
self.session.automaticallyPublishNowPlayingInfo = true
```

### Setting ad time ranges for automatic publishing — [8:38]

```swift
// Example with ads that should not contribute to elapsed time and duration

let preroll = MPAdTimeRange(timeRange: CMTimeRange(start: CMTime.zero, duration: CMTimeMakeWithSeconds(30, preferredTimescale: 1)))


playerItem.nowPlayingInfo = [
    …
    MPNowPlayingInfoPropertyAdTimeRanges: [preroll]
    …
]

self.session = MPNowPlayingSession(players: [player])
self.session.automaticallyPublishNowPlayingInfo = true
```

### Setting artwork and title metadata for AVKit — [11:02]

```swift
// Example of setting artwork metadata

let path = Bundle.main.path(forResource: "poster", ofType: "jpg")
let posterData = FileManager.default.contents(atPath: path!)!

let artwork = AVMutableMetadataItem()
artwork.identifier = .commonIdentifierArtwork
artwork.value = posterData as NSData
artwork.dataType = kCMMetadataBaseDataType_JPEG as String
artwork.extendedLanguageTag = "und"

let title = AVMutableMetadataItem()
title.identifier = .commonIdentifierTitle
title.value = "Magnificent" as NSString
title.extendedLanguageTag = "und"

playerItem.externalMetadata = [artwork, title]
```

### Manually publishing Now Playing — [12:59]

```swift
// Example of setting Now Playing information

let artwork = MPMediaItemArtwork(image: image)

let nowPlayingInfo = [
    MPMediaItemPropertyTitle: title,
    MPMediaItemPropertyArtwork: artwork,
    MPMediaItemPropertyPlaybackDuration: playerItem.duration,
    MPNowPlayingInfoPropertyElapsedPlaybackTime: player.currentTime().seconds,
    MPNowPlayingInfoPropertyPlaybackRate: player.rate
]

MPNowPlayingInfoCenter.default().nowPlayingInfo = nowPlayingInfo
```

### Updating Now Playing metadata — [13:25]

```swift
// On any non-linear time change, playback rate change, or play/pause

var nowPlayingInfo = MPNowPlayingInfoCenter.default().nowPlayingInfo
nowPlayingInfo[MPNowPlayingInfoPropertyElapsedPlaybackTime] = player.currentTime().seconds
nowPlayingInfo[MPNowPlayingInfoPropertyPlaybackRate] = player.rate
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110338/3/BCB38F17-7908-4BD8-8A7A-767EC8C59367/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110338/3/BCB38F17-7908-4BD8-8A7A-767EC8C59367/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110338) — developer.apple.com. Indexed for agent consumption._