---
id: "wwdc2026-297"
event: "wwdc2026"
year: 2026
title: "Best practices for integrating visual intelligence in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/297"
topics: ["App Services", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Best practices for integrating visual intelligence in your app

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-297](https://developer.apple.com/videos/play/wwdc2026/297)

Gain insight on how visual intelligence can transform content discovery in your app. Explore how to define entities, process images, and handle multiple result types effectively. Learn best practices for optimizing speed and relevance, and discover how intents enable direct actions like opening or playing content with a single tap.

**Keywords:** `ai`, `intelligence`, `machine learning`, `visual`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,316 words)

## Documentation & Resources

- [Integrating your app with visual intelligence](https://developer.apple.com/documentation/VisualIntelligence/integrating-your-app-with-visual-intelligence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VisualIntelligence/integrating-your-app-with-visual-intelligence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VisualIntelligence/integrating-your-app-with-visual-intelligence.json
- [Visual Intelligence](https://developer.apple.com/documentation/VisualIntelligence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VisualIntelligence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VisualIntelligence.json

## Code Snippets

### Define the content you want to return as an App Entity — [3:21]

```swift
// Define the content you want to return as an App Entity
import AppIntents

struct AlbumEntity: AppEntity {
    var id: String
    @Property var name: String
    @Property var artistName: String
    var coverArtData: Data

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation( 
            title: "\(name)",
            subtitle: "\(artistName)",
            image: .init(data: coverArtData)
        )   
    }   

    static let defaultQuery = AlbumEntityQuery()

    static var typeDisplayRepresentation: TypeDisplayRepresentation { "Album" }
}   

struct AlbumEntityQuery: EntityQuery {
    @Dependency var catalog: AlbumCatalog
    func entities(for identifiers: [String]) async throws -> [AlbumEntity] {
        catalog.albums(for: identifiers)
    }
}
```

### Adopt IntentValueQuery to return results — [5:39]

```swift
// Adopt IntentValueQuery to return visual search results
import AppIntents
import VisualIntelligence

struct SearchHandler: IntentValueQuery {
    @Dependency var catalog: AlbumCatalog
    @Dependency var concertFinder: ConcertFinder

    func values(for input: SemanticContentDescriptor) async throws -> [VisualSearchResult] {
        guard let pixelBuffer = input.pixelBuffer else {
            return []
        }   

        let albums = try await catalog.search(matching: pixelBuffer)

        return albums.map { VisualSearchResult.album($0) }
    }
}
```

### Build a catalog of albums with precomputed feature prints — [6:24]

```swift
// Build a catalog of albums with precomputed feature prints
import Vision

@Observable
class AlbumCatalog {
    static let shared = AlbumCatalog()

    struct CatalogEntry: Sendable {
        let album: AlbumEntity
        let featurePrint: FeaturePrintObservation
    }   

    private(set) var entries: [CatalogEntry] = []

    private func generateFeaturePrint(
        for image: CGImage
    ) async throws -> FeaturePrintObservation {
        let request = GenerateImageFeaturePrintRequest()
        let result = try await request.perform(on: image)
        return result
    }
}
```

### Search the catalog for albums matching the captured image — [6:45]

```swift
// Search the catalog for albums matching the captured image
func search(matching pixelBuffer: CVReadOnlyPixelBuffer, limit: Int = 10, maxDistance: Double = 1.0) async throws ->
[AlbumEntity] {
    var cgImage: CGImage?
    _ = pixelBuffer.withUnsafeBuffer { VTCreateCGImageFromCVPixelBuffer($0, options: nil, imageOut: &cgImage) }
    guard let cgImage else { return [] }

    let queryPrint = try await generateFeaturePrint(for: cgImage)

    return try entries.compactMap { entry -> (album: AlbumEntity, distance: Double)? in
        let distance = try queryPrint.distance(to: entry.featurePrint)
        guard distance <= maxDistance else { return nil }
        return (entry.album, distance)
    }   
    .sorted { $0.distance < $1.distance }
    .prefix(limit)
    .map { $0.album }
}
```

### Create an open intent to land users on the right screen — [8:27]

```swift
// Create an open intent to land users on the right screen
import AppIntents

struct OpenAlbumIntent: OpenIntent {
    static let title: LocalizedStringResource = "Open Album"

    @Parameter(title: "Album")
    var target: AlbumEntity

    @Dependency var appState: AppState

    func perform() async throws -> some IntentResult {
        await appState.openAlbum(id: target.id)
        return .result()
    }
}
```

### Use UnionValue to return multiple visual search result types — [12:05]

```swift
// Use UnionValue to return multiple visual search result types
@UnionValue
enum VisualSearchResult {
    case album(AlbumEntity)
    case concert(ConcertEntity)
}   

struct OpenConcertIntent: OpenIntent {
    static let title: LocalizedStringResource = "Open Concert"

    @Parameter(title: "Concert")
    var target: ConcertEntity

    @Dependency var appState: AppState

    func perform() async throws -> some IntentResult {
        await appState.openConcert(id: target.id)
        return .result()
    }
}
```

### Expand the IntentValueQuery to return the UnionValue — [12:18]

```swift
// Expand the IntentValueQuery to return the UnionValue
struct SearchHandler: IntentValueQuery {
    @Dependency var catalog: AlbumCatalog
    @Dependency var concertFinder: ConcertFinder

    func values(for input: SemanticContentDescriptor) async throws -> [VisualSearchResult] {
        guard let pixelBuffer = input.pixelBuffer else {
            return []
        }   

        let albums = try await catalog.search(matching: pixelBuffer)

        let artists = albums.map { $0.artistName }

        let concerts = await concertFinder.findNearby(byArtists: artists)

        return albums.map { VisualSearchResult.album($0) }
            + concerts.map { VisualSearchResult.concert($0) }
    }
}
```

### Provide a link to in-app search — [13:13]

```swift
// Provide a link to in-app search
@AppIntent(schema: .visualIntelligence.semanticContentSearch)
struct SemanticContentSearchIntent: AppIntent {
    static let title: LocalizedStringResource = "Search in app"
    static let openAppWhenRun: Bool = true

    var semanticContent: SemanticContentDescriptor
    @Dependency var catalog: AlbumCatalog
    @Dependency var concertFinder: ConcertFinder
    @Dependency var appState: AppState

    func perform() async throws -> some IntentResult {
        guard let pixelBuffer = semanticContent.pixelBuffer else { return .result() }
        let albums = try await catalog.search(matching: pixelBuffer)
        let artists = albums.map { $0.artistName }
        let concerts = await concertFinder.findNearby(byArtists: artists)
        await appState.openSearch(albums: albums, concerts: concerts)
        return .result()
    }   
}
```

### Request calendar access and fetch upcoming concerts — [15:24]

```swift
// Request calendar access and fetch upcoming concerts
import EventKit

@Observable
class UpcomingConcertManager {
    private let eventStore = EKEventStore()
    var upcomingConcerts: [EKEvent] = []
    var authorizationStatus: EKAuthorizationStatus = .notDetermined

    func requestAccessAndFetch() async throws {
        let granted = try await eventStore.requestFullAccessToEvents()
        guard granted else {
            authorizationStatus = .denied
            return
        }   
        authorizationStatus = .fullAccess
        await fetchUpcomingConcerts()

        // ...
    }
}
```

### Filter for upcoming events that match known artists in our catalog — [15:42]

```swift
// Filter for upcoming events that match known artists in our catalog
class UpcomingConcertManager {
    func fetchUpcomingConcerts() async {
        let predicate = eventStore.predicateForEvents(
            withStart: .now,
            end: .now.addingTimeInterval(90 * 24 * 60 * 60),
            calendars: nil
        )   

        let events = eventStore.events(matching: predicate)

        upcomingConcerts = events.filter { event in
            AlbumCatalog.shared.entries.contains { entry in
                event.title?.localizedCaseInsensitiveContains(entry.album.artistName) == true
            }
        }
    }
}
```

### Observe newly created events — [15:44]

```swift
// Observe newly created events
@Observable
class UpcomingConcertManager {
    // ...

    func requestAccessAndFetch() async throws {
        // ...

        for await _ in NotificationCenter.default
            .notifications(
                named: .EKEventStoreChanged
            ) {
            await fetchUpcomingConcerts()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/297/5/25343020-b502-4808-967a-6f6460789dc2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/297/5/25343020-b502-4808-967a-6f6460789dc2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/297) — developer.apple.com. Indexed for agent consumption._