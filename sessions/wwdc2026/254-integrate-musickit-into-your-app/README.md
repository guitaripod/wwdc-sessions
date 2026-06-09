---
id: "wwdc2026-254"
event: "wwdc2026"
year: 2026
title: "Integrate MusicKit into your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/254"
topics: ["Swift", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Integrate MusicKit into your app

**Event:** WWDC26 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-254](https://developer.apple.com/videos/play/wwdc2026/254)

Bring the power of Apple Music into your app using MusicKit. We’ll cover authorization, subscription-status checks, music selection, playback control, and cross-storefront song sharing. Learn how to use the new Music Picker to let people browse the Apple Music catalog and their personal libraries. We’ll also break down the differences between SystemMusicPlayer and ApplicationMusicPlayer, and show you how to observe playback state.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,562 words)

## Documentation & Resources

- [Integrating MusicKit into your app](https://developer.apple.com/documentation/MusicKit/integrating-musickit-into-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MusicKit/integrating-musickit-into-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MusicKit/integrating-musickit-into-your-app.json
- [Apple Services Performance Partner Program](https://performance-partners.apple.com/home) _documentation_
- [MusicKit](https://developer.apple.com/documentation/musickit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/musickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/musickit.json

## Code Snippets

### Presents the Apple Music subscription offer — [4:47]

```swift
@State var showSubscriptionOffer = false

let options = MusicSubscriptionOffer.Options(
    messageIdentifier: .playMusic
)

@ViewBuilder
var musicSubsriptionButton: some View {
    Button("Subscribe to Apple Music", systemImage: "music.note") {
        showSubscriptionOffer = true
    }
    .musicSubscriptionOffer(isPresented: $showSubscriptionOffer, options: options)
}
```

### Adds subscription button to main view — [5:59]

```swift
@State var subscription: MusicSubscription?

var body: some View {
  	VStack {
        // ...
        if let subscription, subscription.canBecomeSubscriber {
            musicSubscriptionButton
        }
    }
    .task(id: isAuthorized) {
	      self.subscription = try? await MusicSubscription.current
        for await subscription in MusicSubscription.subscriptionUpdates {
            self.subscription = subscription
        }
    }
}
```

### Add .musicPicker() modifier — [8:48]

```swift
@State var showMusicPicker = false
@State var selectedSong: Song? = nil

@ViewBuilder
var musicPickerButton: some View {
    Button("Pick some Music", systemImage: "music.note.list") {
        showMusicPicker = true
    }
    .musicPicker(isPresented: $showMusicPicker, selection: $selectedSong)
}

var body: some View {
    VStack {
        if let subscription, subscription.canBecomeSubscriber {
            musicSubscriptionButton
        }
        musicPickerButton
    }
}
```

### Artwork — [14:49]

```swift
@State var queue = ApplicationMusicPlayer.shared.queue

var body: some View {
    VStack {
        if let artwork = queue.currentEntry?.artwork {
            ArtworkImage(artwork, width: 200, height: 200)
        } else {
            // Placeholder artwork
            RoundedRectangle(cornerRadius: 16)
                .fill(.quaternary)
                .frame(width: 200, height: 200)
        }
    }
}
```

### Current entry info — [15:06]

```swift
@State var queue = ApplicationMusicPlayer.shared.queue

var body: some View {
    VStack {
        // ...
        if let currentSong = queue.currentEntry {
            Text(currentSong.title)
                .font(.title3.bold())

            if let subtitle = currentSong.subtitle {
                Text(subtitle)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }
        }
    }
}
```

### Playback controls (play, pause) — [15:14]

```swift
let player = ApplicationMusicPlayer.shared
@State var state = ApplicationMusicPlayer.shared.state

var isPlaying: Bool {
    state.playbackStatus == .playing
}

var playPause: some View {
    Button (
        isPlaying ? "Pause": "Play",
        systemImage: isplaying ? "pause.fill" : "play.fill"
    ) {
        if isPlaying {
            player.pause()
        } else {
            Task {
                try await player.play()
            }
        }
    }
}
```

### Playback controls (next, previous) — [15:38]

```swift
let player = ApplicationMusicPlayer.shared

var controls: some View {
    HStack {
        Button("Back", systemImage: "backward.fill") {
            Task {
                try await player.skipToPreviousEntry()
            }
        }
        // ...
        Button("Next", systemImage: "forward.fill") {
            Task {
                try await player.skipToNextEntry()
            }
        }
    }
}
```

### Music catalog resource request — [18:58]

```swift
func fetchSongs(songIDs: [MusicItemID]) async throws -> (featured: Song?, other: [Song]) {
    var request = MusicCatalogResourceRequest‹Song>(matching: \.id, memberOf: songIDs)
    request.options = [.findEquivalents]

    let response = try await request.response()

    let featuredSongID = songIDs[0]
    let featuredSong = response.item(for: featuredSongID)

    let others: [Song] = songIDs[1...].compactMap { songID in
        return response.item(for: songID)
    }

    return (featuredSong, others)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/254/5/d4b2c60a-8a2a-41d1-a55a-0fd60d927798/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/254/5/d4b2c60a-8a2a-41d1-a55a-0fd60d927798/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/254) — developer.apple.com. Indexed for agent consumption._
