---
id: "wwdc2026-274"
event: "wwdc2026"
year: 2026
title: "What’s new in SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/274"
topics: ["Swift", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in SwiftData

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-274](https://developer.apple.com/videos/play/wwdc2026/274)

Discover the latest enhancements to SwiftData. We’ll show you how to persist custom and third-party types using Codable, and group fetched data into sections in your SwiftUI app. We’ll also explore how to observe data store changes anywhere else using ResultsObserver and HistoryObserver, giving you the flexibility to drive powerful state objects and react precisely to model updates.

**Keywords:** `screenshots`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,933 words)

## Documentation & Resources

- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Sectioned fetching — [0:01]

```swift
// Sectioned fetching

struct TripListView: View {   
    @Query(sort: \Trip.startDate,
           sectionBy: \.destination)
    var trips: [Trip]

    var body: some View: {
        List(selection: $selection) {
            ForEach(_trips.sections) {section in
                Section(section.id) {
                    ForEach(trips) {trip in
                        TripListItem(trip: trip)
                    }
               }
            }
        }
    }
}
```

### Using Codable — [4:59]

```swift
// Using Codable

import SwiftData

@Model class Trip {

    struct Location: Codable {
        var latitude: Double
        var longitude: Double
    }

    var name: String
    var destination: String

    var startDate: Date
    var endDate: Date

    var location: Location?
    @Attribute(.codable) var mapItemIdentifier: MKMapItem.Identifier?
}
```

### // Use observation to update map bounds — [8:20]

```swift
// Use observation to update map bounds

@Observable @MainActor final class MapCameraController {
    private let resultsObserver: ResultsObserver<Trip, Never>
    var bounds: MapCameraBounds?
    private var token: ObservationTracking.Token?

    init(modelContext: ModelContext) throws {
        resultsObserver = try ResultsObserver<Trip, Never>(modelContext: modelContext)

        token = withContinuousObservation(options: [.didSet]) {[weak self], event in
            self?.bounds = self?.calculateBounds(trips: resultsObserver.results)
       }
    }

    private func calculateBounds(trips: [Trip]) -> MapCameraBounds? { / * */ }
}
```

### // Using HistoryObserver to sync with a server — [8:21]

```swift
// Using HistoryObserver to sync with a server

@SyncActor final class ServerSync {
    private let observer: HistoryObserver
    private var token: ObservationTracking.Token?

    func start() throws {
        self.observer = try HistoryObserver(authors: ["App"], modelContainer: modelContainer)
        token = withContinuousObservation(options: .didSet) {[weak self] _ in
            _ = self?.observer.eventCounter
            self?.processChanges()
        }
    }

    private func processChanges() {
        // Fetch and process history transactions
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/274/4/87fb1efb-9956-414e-8c99-f2579fe86da2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/274/4/87fb1efb-9956-414e-8c99-f2579fe86da2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/274) — developer.apple.com. Indexed for agent consumption._
