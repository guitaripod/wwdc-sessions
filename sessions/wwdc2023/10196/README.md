---
id: "wwdc2023-10196"
event: "wwdc2023"
year: 2023
title: "Dive deeper into SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10196"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Dive deeper into SwiftData

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10196](https://developer.apple.com/videos/play/wwdc2023/10196)

Learn how you can harness the power of SwiftData in your app. Find out how ModelContext and ModelContainer work together to persist your app’s data. We’ll show you how to track and make your changes manually and use SwiftData at scale with FetchDescriptor, SortDescriptor, and enumerate.

To get the most out of this session, we recommend first watching "Meet SwiftData" and "Model your schema with SwiftData" from WWDC23.

**Keywords:** `@attribute`, `coredata`, `core data`, `data`, `data model`, `enumerate`, `enumeration`, `fetchdescriptor`, `macros`, `model`, `@model`, `modelcontainer`, `modelcontext`, `persistence`, `predicate`, `#predicate`, `@relationship`, `sortdescriptor`, `swift`, `swiftdata`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,196 words)

## Documentation & Resources

- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Trip model with cascading relationships — [1:45]

```swift
@Model
final class Trip {
    var destination: String?
    var end_date: Date?
    var name: String?
    var start_date: Date?

    @Relationship(.cascade)
    var bucketListItem: [BucketListItem] = [BucketListItem]()

    @Relationship(.cascade)
    var livingAccommodation: LivingAccommodation?
}
```

### Initializing a ModelContainer — [4:21]

```swift
// ModelContainer initialized with just Trip
let container = try ModelContainer(for: Trip.self)

// SwiftData infers related model classes as well
let container = try ModelContainer(
    for: [
        Trip.self, 
        BucketListItem.self, 
        LivingAccommodation.self
    ]
)
```

### Using ModelConfiguration to customize ModelContainer — [5:41]

```swift
let fullSchema = Schema([
    Trip.self,
    BucketListItem.self,
    LivingAccommodations.self,
    Person.self,
    Address.self
])

let trips = ModelConfiguration(
    schema: Schema([
        Trip.self,
        BucketListItem.self,
        LivingAccommodations.self
    ]),
    url: URL(filePath: "/path/to/trip.store"),
    cloudKitContainerIdentifier: "com.example.trips"
)

let people = ModelConfiguration(
    schema: Schema([Person.self, Address.self]),
    url: URL(filePath: "/path/to/people.store"),
    cloudKitContainerIdentifier: "com.example.people"
) 

let container = try ModelContainer(for: fullSchema, trips, people)
```

### Creating ModelContainer in SwiftUI — [6:49]

```swift
@main
struct TripsApp: App {
    let fullSchema = Schema([
        Trip.self, 
        BucketListItem.self,
        LivingAccommodations.self,
        Person.self, 
        Address.self
    ])

    let trips = ModelConfiguration(
        schema: Schema([
            Trip.self,
            BucketListItem.self,
            LivingAccommodations.self
        ]),
        url: URL(filePath: "/path/to/trip.store"),
        cloudKitContainerIdentifier: "com.example.trips"
    )

    let people = ModelConfiguration(
        schema: Schema([
            Person.self, 
            Address.self
        ]),
        url: URL(filePath: "/path/to/people.store"),
        cloudKitContainerIdentifier: "com.example.people"
    )

    let container = try ModelContainer(for: fullSchema, trips, people)
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(container)
    }
}
```

### Using the modelContainer modifier — [7:40]

```swift
@main
struct TripsApp: App {
   var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Trip.self)
    }
}
```

### Referencing a ModelContext in SwiftUI views — [7:50]

```swift
struct ContentView: View {
    @Query var trips: [Trip]
    @Environment(\.modelContext) var modelContext

    var body: some View {
        NavigationStack (path: $path) {
            List(selection: $selection) {
                ForEach(trips) { trip in
                    TripListItem(trip: trip)
                        .swipeActions(edge: .trailing) {
                            Button(role: .destructive) {
                                modelContext.delete(trip)
                            } label: {
                                Label("Delete", systemImage: "trash")
                            }
                        }
                }
                .onDelete(perform: deleteTrips(at:))
            }
        }
    }
}
```

### Enabling undo on a ModelContainer — [9:57]

```swift
@main
struct TripsApp: App {
   @Environment(\.undoManager) var undoManager
   var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Trip.self, isUndoEnabled: true)
    }
}
```

### Enabling autosave on a ModelContainer — [11:05]

```swift
@main
struct TripsApp: App {
   var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Trip.self, isAutosaveEnabled: false)
    }
}
```

### Fetching objects with FetchDescriptor — [11:54]

```swift
let context = self.newSwiftContext(from: Trip.self)
var trips = try context.fetch(FetchDescriptor<Trip>())
```

### Fetching objects with #Predicate and FetchDescriptor — [12:14]

```swift
let context = self.newSwiftContext(from: Trip.self)
let hotelNames = ["First", "Second", "Third"]

var predicate = #Predicate<Trip> { trip in
    trip.livingAccommodations.filter {
        hotelNames.contains($0.placeName)
    }.count > 0
}

var descriptor = FetchDescriptor(predicate: predicate)
var trips = try context.fetch(descriptor)
```

### Fetching objects with #Predicate and FetchDescriptor — [12:27]

```swift
let context = self.newSwiftContext(from: Trip.self)

predicate = #Predicate<Trip> { trip in
    trip.livingAccommodations.filter {
        $0.hasReservation == false
    }.count > 0
}

descriptor = FetchDescriptor(predicate: predicate)
var trips = try context.fetch(descriptor)
```

### Enumerating objects with FetchDescriptor — [13:18]

```swift
context.enumerate(FetchDescriptor<Trip>()) { trip in
    // Operate on trip
}
```

### Enumerating with FetchDescriptor and SortDescriptor — [13:36]

```swift
let predicate = #Predicate<Trip> { trip in
    trip.bucketListItem.filter {
        $0.hasReservation == false
    }.count > 0
}

let descriptor = FetchDescriptor(predicate: predicate)
descriptor.sortBy = [SortDescriptor(\.start_date)]

context.enumerate(descriptor) { trip in
    // Remind me to make reservations for trip
}
```

### Fine tuning enumerate with batchSize — [14:01]

```swift
let predicate = #Predicate<Trip> { trip in
    trip.bucketListItem.filter {
        $0.hasReservation == false
    }.count > 0
}

let descriptor = FetchDescriptor(predicate: predicate)
descriptor.sortBy = [SortDescriptor(\.start_date)]

context.enumerate(
    descriptor,
    batchSize: 10000
) { trip in
    // Remind me to make reservations for trip
}
```

### Fine tuning enumerate with batchSize and allowEscapingMutations — [14:28]

```swift
let predicate = #Predicate<Trip> { trip in
    trip.bucketListItem.filter {
        $0.hasReservation == false
    }.count > 0
}

let descriptor = FetchDescriptor(predicate: predicate)
descriptor.sortBy = [SortDescriptor(\.start_date)]

context.enumerate(
    descriptor,
    batchSize: 500,
    allowEscapingMutations: true
) { trip in
    // Remind me to make reservations for trip
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10196/5/44001952-2ED6-45B5-9BF4-CFCE817D1CA7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10196/5/44001952-2ED6-45B5-9BF4-CFCE817D1CA7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10196) — developer.apple.com. Indexed for agent consumption._