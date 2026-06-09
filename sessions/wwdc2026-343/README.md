# Explore advanced App Intents features for Siri and Apple Intelligence

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-343](https://developer.apple.com/videos/play/wwdc2026/343)

Polish how your app works with Siri using advanced App Intents APIs. Learn techniques that let people accomplish more with just their voice, help Apple Intelligence find your content, and provide context for on-screen awareness so Siri understands what’s happening in your app. 

**Keywords:** `ai`, `app intents`, `machine learning`, `siri`, `xcode`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [App Intents Testing](https://developer.apple.com/documentation/AppIntentsTesting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntentsTesting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntentsTesting.json
- [Donating your app’s data and actions to the system](https://developer.apple.com/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system.json
- [Donations and discovery](https://developer.apple.com/documentation/AppIntents/donations-and-discovery) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/donations-and-discovery
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/donations-and-discovery.json
- [Making app entities available in Spotlight](https://developer.apple.com/documentation/AppIntents/making-app-entities-available-in-spotlight) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/making-app-entities-available-in-spotlight
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/making-app-entities-available-in-spotlight.json
- [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence.json
- [Providing contextual cues to Apple Intelligence and Siri](https://developer.apple.com/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri.json
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/AppIntents/apple-intelligence-and-siri-ai) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/apple-intelligence-and-siri-ai
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/apple-intelligence-and-siri-ai.json

## Code Snippets

### Custom dialog response — [2:42]

```swift
@AppIntent(schema: .audio.addToPlaylist)
struct AddToPlaylistIntent {

    func perform() async throws -> some IntentResult & ProvidesDialog {
        // Adds song to playlist and responds
        return .result(
            dialog: IntentDialog(
                full: """
                      Added \(song.title) to the \
                      \(playlist.title) mix tape.
                      """,
                supporting: "Added"
            )
        )
    }
}
```

### Ask a clarifying question within an inten — [3:42]

```swift
@AppIntent(schema: .clock.createTimer)
struct CreateTimerIntent {
    // MARK: Schema Parameters
    var duration: Duration
    var label: String?
    var isSleepTimer: Bool

    func perform() async throws -> some ReturnsValue<TimerEntity> {
        // Checks active timers and requests label parameter
        label = try await $label.requestValue(
            """
            You already have a timer running. \
            What should we call this one?
            """
        )
        return .result(value: timerEntity)
    }
}
```

### Enhanced DisplayRepresentation — [4:26]

```swift
// Enhanced DisplayRepresentation
@AppEntity(schema: .audio.song)
struct SongEntity {

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(title)",
            subtitle: "\(artistName)",
            image: artworkImage
        )
    }
}
```

### Return a custom snippet view — [5:05]

```swift
@AppIntent(schema: .audio.addToPlaylist)
struct AddToPlaylistIntent {

    var audioEntity: AudioEntity
    var playlist: PlaylistEntity

    func perform() async throws -> some IntentResult & ProvidesDialog & ShowsSnippetView {
        // Adds to playlist and shows dialog and snippet
        let view = PlaylistSnippetView(
            playlist: updatedEntity,
            tracks: updated.tracks
        )
        return .result(dialog: dialog, view: view)
    }
}
```

### Donate a UI interaction — [7:44]

```swift
@ModelActor
actor ModelManager {
    func sendMessage(_ /* ... */, donateIntent: Bool = false) async throws -> [Message.ID] {

        // Donate intent with parameters and result so Siri can learn user preferences
        if donateIntent {
            let intent = SendMessageIntent()
            intent.destination = .recipients(conversation.recipients.map(\.entity))

            let result = messages.map(\.entity)
            Task {
                try await IntentDonationManager.shared.donate(
                    intent: intent,
                    result: .result(value: result)
                )
            }
        }
    }
}
```

### Declare entity ownership for confirmations — [10:03]

```swift
// Informs system if entity is public or shared with others
@AppEntity(schema: .calendar.event)
struct EventEntity: OwnershipProvidingEntity {

    var ownership: EntityOwnership {
        // isShared used to compute ownership state: .shared, .public, or .unknown
        attendees.isEmpty ? .unknown : .shared
    }
}
```

### Index entities with IndexedEntity — [11:30]

```swift
// Indexing IndexedEntity with CSSearchableIndex
struct EntityIndexingHelper {
    // Indexes playlist entities
    func indexPlaylist(_ playlist: Playlist) async throws {
        let entity = PlaylistEntity(playlist: playlist)
        try await CSSearchableIndex(name: indexName)
            .indexAppEntities([entity])
    }
}
```

### Structured search with IntentValueQuer — [13:38]

```swift
// Structured search of songs and playlists
struct AudioIntentValueQuery: IntentValueQuery {

    // AudioSearch, IntentPerson, and other system types may be supported as input
    func values(for input: AudioSearch) async throws -> [AudioEntity] {
        switch input.criteria {
        case .searchQuery(let query):
            return try await searchResults(for: query)
        case .unspecified:
            return try await likedSongResults()
        // ... also a .url case
        }
    }
}
```

### Re-run Siri search in your app — [14:49]

```swift
// Intent that re-runs the Siri search in app
@AppIntent(schema: .system.searchInApp)
struct SearchAudioLibraryIntent {

    var criteria: StringSearchCriteria

    func perform() async throws -> some IntentResult {
        // Perform in-app search with Siri search string
        navigation.searchText = criteria.term
        navigation.selectedTab = .library
        return .result()
    }
}
```

### Onscreen awareness annotations — [16:27]

```swift
// (a) Single primary entity on screen — NSUserActivity
struct NowPlayingView: View {
    @Environment(PlaybackController.self) private var playback

    var body: some View {
        VStack {
            // Player UI
        }
        .userActivity("cosmotunes.nowPlaying", isActive: playback.currentTrack) { activity in
            activity.title = playback.currentTrack?.title
            activity.appEntityIdentifier = EntityIdentifier(
                for: SongEntity.self,
                identifier: playback.currentTrack.id
            )
        }
    }
}

// (b) One entity among many — View Entity annotation
struct AlbumView: View {
    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            // ...
        }
        .appEntityIdentifier(
            EntityIdentifier(for: AlbumEntity.self, identifier: session.id.uuidString)
        )
    }
}

// (c) Lists and collections — Collection annotation
struct PlaylistDetailView: View {
    var body: some View {
        List {
            ForEach(playlist.tracks) { track in
                PlaylistTrackRow(track: track)
            }
        }
        .appEntityIdentifier(forSelectionType: GeneratedTrack.ID.self) { trackID in
            EntityIdentifier(for: SongEntity.self, identifier: trackID)
        }
    }
}
```

### Component-based display representation query — [17:23]

```swift
// Component-based display representation queries
extension PlaylistQuery {
    func displayRepresentations(
        for identifiers: [PlaylistEntity.ID],
        requestedComponents: DisplayRepresentation.Components = .text
    ) async throws -> [PlaylistEntity.ID: DisplayRepresentation] {
        let entities = try await model.playlistEntities(for: identifiers)

        // Fetch display representations for fetched entities
        var result: [PlaylistEntity.ID: DisplayRepresentation] = [:]
        for entity in entities {
            result[entity.id] = await entity.displayRepresentation(with: requestedComponents)
        }
        return result
    }
}
```

### Entity annotations on system integrations — [21:07]

```swift
// (a) User notifications
import AppIntents
import UserNotifications

func scheduleNotification(message: Message, author: Contact, conversation: Conversation) {
    let content = UNMutableNotificationContent()
    content.title = author.name
    content.body = message.body

    // Annotate with entity identifier
    content.appEntityIdentifiers = [
        EntityIdentifier(for: MessageEntity.self, identifier: message.id)
    ]
    // Schedule the notification
}

// (b) Now Playing — most specific to least specific
import NowPlaying

final class CosmoTunesMediaSession: MediaSessionRepresentable {
    var content: (any MediaContentRepresentable)? {
        var content = MusicContent(id: track.id.uuidString, songTitle: track.title /* ... */)
        content.appEntityIdentifiers = [
            EntityIdentifier(for: SongEntity.self, identifier: track.id),
            EntityIdentifier(for: ArtistEntity.self, identifier: track.session.artistName),
            EntityIdentifier(for: PlaylistEntity.self, identifier: currentPlaylist.id),
        ]
        return content
    }
}

// (c) AlarmKit
import AlarmKit

func scheduleAlarm(_ alarm: Alarm) async throws {
    let configuration = AlarmManager.AlarmConfiguration<CosmoTunesAlarmMetadata>.alarm(
        schedule: schedule,
        attributes: attributes,
        appEntityIdentifier: EntityIdentifier(for: AlarmEntity.self, identifier: alarm.id),
        stopIntent: DismissAlarmIntent(),
        secondaryIntent: SnoozeAlarmIntent(),
        sound: sound
    )
    // Schedule alarm
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/343/4/00190d1d-55b6-4eb2-9ee3-e09f3d8d1c7d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/343/4/00190d1d-55b6-4eb2-9ee3-e09f3d8d1c7d/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._