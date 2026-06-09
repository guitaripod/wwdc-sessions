---
id: "wwdc2026-312"
event: "wwdc2026"
year: 2026
title: "Meet the Now Playing framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/312"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Meet the Now Playing framework

**Event:** WWDC26 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-312](https://developer.apple.com/videos/play/wwdc2026/312)

Get a first look at Now Playing — a Swift framework that connects your app’s media playback to system surfaces like the Lock Screen, Control Center, Dynamic Island, and CarPlay. Discover how to publish playback state and respond to commands using its observable API. Explore remote playback sessions, a new capability that lets your app represent media playing on external devices and bring full playback controls to those same system surfaces.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,735 words)

## Documentation & Resources

- [Routing media to third-party devices](https://developer.apple.com/documentation/AVSystemRouting/routing-media-to-third-party-devices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVSystemRouting/routing-media-to-third-party-devices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVSystemRouting/routing-media-to-third-party-devices.json
- [Publishing remote media sessions](https://developer.apple.com/documentation/NowPlaying/publishing-remote-media-sessions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NowPlaying/publishing-remote-media-sessions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NowPlaying/publishing-remote-media-sessions.json
- [Publishing media sessions](https://developer.apple.com/documentation/NowPlaying/publishing-media-sessions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NowPlaying/publishing-media-sessions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NowPlaying/publishing-media-sessions.json
- [Setting up a remote notification server](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/setting-up-a-remote-notification-server
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/setting-up-a-remote-notification-server.json

## Code Snippets

### Existing PlayerModel implementation — [1:57]

```swift
import Observation

@Observable
final class PlayerModel {
    let player: SoundPlayer
    var sound: Sound { player.currentSound }

    init(player: SoundPlayer) {
        self.player = player
    }
}
```

### Adopt MediaSessionRepresentable — [2:06]

```swift
import NowPlaying

extension PlayerModel: MediaSessionRepresentable {
    var id: String { "ambient-sound-session" }

    var content: (any MediaContentRepresentable)? {
        return GenericContent(
            id: sound.id,
            title: sound.name,
            subtitle: sound.description,
            type: .audio,
            duration: .live,
            artwork: Artwork(id: sound.id) { size in
                let data = try await self.artworkData(size: size)
                return try ArtworkRepresentation(data: data)
            }
        )
    }

    var playbackSnapshot: MediaPlaybackSnapshot? {
        MediaPlaybackSnapshot(
            state: player.isPlaying ? .playing() : .paused
        )
    }

    var commands: [MediaCommand] {[
        .play { self.player.play() },
        .pause { self.player.pause() },
        .previous { self.player.previous() },
        .next { self.player.next() }
    ]}
}
```

### MediaSession initialization — [4:31]

```swift
import NowPlaying

struct PlayerController {
    let player: SoundPlayer
    let model: PlayerModel
    let session: MediaSession<PlayerModel>

    init() {
        self.player = SoundPlayer()
        self.model = PlayerModel(player: player)
        self.session = MediaSession(model)
    }
}
```

### App extension entry point — [6:42]

```swift
import ExtensionFoundation
import NowPlaying

@main
final class SampleAppExtension: @MainActor RemoteMediaSessionExtension {
    var configuration: some AppExtensionConfiguration {
        RemoteMediaSessionExtensionConfiguration(extension: self)
    }

    var extensionPoint: AppExtensionPoint {
        AppExtensionPoint.Identifier(host: "com.apple.nowplaying", name: "remote-media")
    }

    func session(_ state: RemotePlayerState) async throws -> RemotePlayerModel {
        RemotePlayerModel(state: state)
    }
}
```

### Existing RemotePlayerModel implementation — [7:23]

```swift
import Observation

@Observable
@MainActor
final class RemotePlayerModel {
    let client: ServerClient
    var state: RemotePlayerState

    init(state: RemotePlayerState) {
        self.client = ServerClient(sessionID: state.sessionID)
        self.state = state
    }
}
```

### Adopt RemoteMediaSessionRepresentable in app extension — [7:40]

```swift
import NowPlaying

extension RemotePlayerModel: @MainActor RemoteMediaSessionRepresentable {
    var id: String { state.sessionID }

    var content: (any MediaContentRepresentable)? {
        GenericContent(
            id: state.sound.id,
            title: state.sound.name,
            subtitle: state.sound.description,
            type: .audio,
            duration: .live,
            artwork: Artwork(id: state.sound.id) { size in
                let data = try await self.artworkData(size: size)
                return try ArtworkRepresentation(data: data)
            }
        )
    }

    var playbackSnapshot: MediaPlaybackSnapshot? {
        MediaPlaybackSnapshot(
            state: state.isPlaying ? .playing() : .paused
        )
    }

    var commands: [MediaCommand] {[
        .play { try await self.client.send(.play) },
        .pause { try await self.client.send(.pause) },
        .previous { try await self.client.send(.previous) },
        .next { try await self.client.send(.next) }
    ]}

    var devices: [MediaDevice] {
        state.devices.map { device in
            MediaDevice(
                id: device.id,
                name: device.name,
                type: .speaker,
                capabilities: [
                    .absoluteVolume(device.volume) { volume in
                        // send volume change to server
                    }
                ]
            )
        }
    }

    func update(_ state: RemotePlayerState) {
        self.state = state
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/312/5/3f128d25-f1c6-49d3-a9c0-0bdc22af5f95/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/312/5/3f128d25-f1c6-49d3-a9c0-0bdc22af5f95/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/312) — developer.apple.com. Indexed for agent consumption._