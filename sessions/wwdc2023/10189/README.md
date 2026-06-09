---
id: "wwdc2023-10189"
event: "wwdc2023"
year: 2023
title: "Migrate to SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10189"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Migrate to SwiftData

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10189](https://developer.apple.com/videos/play/wwdc2023/10189)

Discover how you can start using SwiftData in your apps. We’ll show you how to use Xcode to generate model classes from your existing Core Data object models, use SwiftData alongside your previous implementation, or even completely replace your existing solution.

Before watching this session, make sure you check out "Meet SwiftData."

**Keywords:** `@attribute`, `coredata`, `core data`, `data`, `data model`, `macros`, `migration`, `model`, `@model`, `presistence`, `refactor`, `@relationship`, `swift`, `swiftdata`, `upgrade`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,782 words)

## Documentation & Resources

- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Creating a ModelContainer in SwiftUI — [4:37]

```swift
@main
struct TripsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(
            for: [Trip.self, BucketListItem.self, LivingAccommodation.self]
        )
    }
}
```

### Object creation in Core Data — [4:57]

```swift
@Environment(\.managedObjectContext) private var viewContext

let newTrip = Trip(context: viewContext)
newTrip.name = name
newTrip.destination = destination
newTrip.startDate = startDate
newTrip.endDate = endDate
```

### Object creation in SwiftData — [5:30]

```swift
@Environment(\.modelContext) private var modelContext

let trip = Trip(
    name: name, 
    destination: destination, 
    startDate: startDate, 
    endDate: endDate
)

modelContext.insert(object: trip)
```

### Fetch with Query in SwiftData — [6:16]

```swift
@Query(sort: \.startDate, order: .forward)

var trips: [Trip]
```

### Setting store path and enabling persistent history tracking in Core Data — [7:30]

```swift
let url = URL(fileURLWithPath: "/path/to/Trips.store")

if let description = container.persistentStoreDescriptions.first {
    description.url = url
    description.setOption(true as NSNumber, forKey: NSPersistentHistoryTrackingKey)
}
```

### Ensuring Core Data and SwiftData class names are unique — [9:11]

```swift
class CDTrip: NSManagedObject {
    // ...
}


@Model final class Trip {
    // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10189/4/87485DA7-96D9-41FA-979E-1D0224B540C2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10189/4/87485DA7-96D9-41FA-979E-1D0224B540C2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10189) — developer.apple.com. Indexed for agent consumption._