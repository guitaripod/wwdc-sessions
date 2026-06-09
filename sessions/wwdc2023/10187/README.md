---
id: "wwdc2023-10187"
event: "wwdc2023"
year: 2023
title: "Meet SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10187"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet SwiftData

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10187](https://developer.apple.com/videos/play/wwdc2023/10187)

SwiftData is a powerful and expressive persistence framework built for Swift. We’ll show you how you can model your data directly from Swift code, use SwiftData to work with your models, and integrate with SwiftUI.

**Keywords:** `@attribute`, `coredata`, `core data`, `data`, `fetchdescriptor`, `macro`, `macros`, `model`, `@model`, `models`, `observation`, `persistence`, `predicate`, `#predicate`, `@relationship`, `sortdescriptor`, `swift`, `swiftdata`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,307 words)

## Documentation & Resources

- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Adding @Model to Trip — [1:27]

```swift
import SwiftData

@Model
class Trip {
    var name: String
    var destination: String
    var endDate: Date
    var startDate: Date

    var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?
}
```

### Providing options for @Attribute and @Relationship — [2:46]

```swift
@Model
class Trip {
    @Attribute(.unique) var name: String
    var destination: String
    var endDate: Date
    var startDate: Date

    @Relationship(.cascade) var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?
}
```

### Initialize a ModelContainer — [3:43]

```swift
// Initialize with only a schema
let container = try ModelContainer([Trip.self, LivingAccommodation.self])

// Initialize with configurations
let container = try ModelContainer(
    for: [Trip.self, LivingAccommodation.self],
    configurations: ModelConfiguration(url: URL("path"))
)
```

### Creating a model container in SwiftUI — [3:58]

```swift
import SwiftUI

@main
struct TripsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(
            for: [Trip.self, LivingAccommodation.self]
        )
    }
}
```

### Accessing the environment's ModelContext — [4:20]

```swift
import SwiftUI

struct ContextView : View {
    @Environment(\.modelContext) private var context
}
```

### Building a predicate — [5:13]

```swift
let today = Date()
let tripPredicate = #Predicate<Trip> { 
    $0.destination == "New York" &&
    $0.name.contains("birthday") &&
    $0.startDate > today
}
```

### Fetching with a FetchDescriptor — [5:32]

```swift
let descriptor = FetchDescriptor<Trip>(predicate: tripPredicate)

let trips = try context.fetch(descriptor)
```

### Fetching with fetch and sort descriptors — [5:46]

```swift
let descriptor = FetchDescriptor<Trip>(
    sortBy: SortDescriptor(\Trip.name),
    predicate: tripPredicate
)

let trips = try context.fetch(descriptor)
```

### Working with a ModelContext — [6:15]

```swift
var myTrip = Trip(name: "Birthday Trip", destination: "New York")

// Insert a new trip
context.insert(myTrip)

// Delete an existing trip
context.delete(myTrip)

// Manually save changes to the context
try context.save()
```

### Using @Query in SwiftUI — [7:38]

```swift
import SwiftUI

struct ContentView: View  {
    @Query(sort: \.startDate, order: .reverse) var trips: [Trip]
    @Environment(\.modelContext) var modelContext

    var body: some View {
       NavigationStack() {
          List {
             ForEach(trips) { trip in 
                 // ...
             }
          }
       }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10187/5/1D820D6D-4F01-48EB-8F22-901F4A4B69FE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10187/5/1D820D6D-4F01-48EB-8F22-901F4A4B69FE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10187) — developer.apple.com. Indexed for agent consumption._