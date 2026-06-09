---
id: "wwdc2025-291"
event: "wwdc2025"
year: 2025
title: "SwiftData: Dive into inheritance and schema migration"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/291"
topics: ["App Services", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# SwiftData: Dive into inheritance and schema migration

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-291](https://developer.apple.com/videos/play/wwdc2025/291)

Discover how to use class inheritance to model your data. Learn how to optimize queries and seamlessly migrate your app’s data to use inheritance. Explore subclassing for building model graphs, crafting efficient fetches and queries, and implementing robust schema migrations. Understand how to use Observable and persistent history for efficient change tracking.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,091 words)

## Documentation & Resources

- [Building rich SwiftUI text experiences](https://developer.apple.com/documentation/SwiftUI/building-rich-swiftui-text-experiences) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/building-rich-swiftui-text-experiences
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/building-rich-swiftui-text-experiences.json
- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Import SwiftData and add @Model — [1:07]

```swift
// Trip Models decorated with @Model
import Foundation
import SwiftData

@Model
class Trip {
  var name: String
  var destination: String
  var startDate: Date
  var endDate: Date

  var bucketList: [BucketListItem] = [BucketListItem]()
  var livingAccommodation: LivingAccommodation?
}

@Model
class BucketListItem { ... }

@Model
class LivingAccommodation { ... }
```

### Add modelContainer modifier — [1:18]

```swift
// SampleTrip App using modelContainer Scene modifier

import SwiftUI
import SwiftData

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

### Adopt @Query — [1:30]

```swift
// Trip App using @Query
import SwiftUI
import SwiftData

struct ContentView: View {
  @Query
  var trips: [Trip]

  var body: some View {
    NavigationSplitView {
      List(selection: $selection) {
        ForEach(trips) { trip in
          TripListItem(trip: trip)
        }
      }
    }
  }
}
```

### Add subclasses to Trip — [3:28]

```swift
// Trip Model extended with two new subclasses

@Model
class Trip { 
  var name: String
  var destination: String
  var startDate: Date
  var endDate: Date

  var bucketList: [BucketListItem] = [BucketListItem]()
  var livingAccommodation: LivingAccommodation?
}

@available(iOS 26, *)
@Model
class BusinessTrip: Trip {
  var perdiem: Double = 0.0
}

@available(iOS 26, *)
@Model
class PersonalTrip: Trip {
  enum Reason: String, CaseIterable, Codable {
    case family
    case reunion
    case wellness
  }

  var reason: Reason
}
```

### Update modelContainer modifier — [4:03]

```swift
// SampleTrip App using modelContainer Scene modifier

import SwiftUI
import SwiftData

@main
struct TripsApp: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .modelContainer(for: [Trip.self, BusinessTrip.self, PersonalTrip.self])
  }
}
```

### Add segmented control to drive a predicate to filter by Type — [7:06]

```swift
// Trip App add segmented control
import SwiftUI
import SwiftData

struct ContentView: View {
  @Query
  var trips: [Trip]

  enum Segment: String, CaseIterable {
    case all = "All"
    case personal = "Personal"
    case business = "Business"
  }

  init() {
    let classPredicate: Predicate<Trip>? = {
      switch segment.wrappedValue {
      case .personal:
        return #Predicate { $0 is PersonalTrip }
      case .business:
        return #Predicate { $0 is BusinessTrip }
      default:
        return nil
      }
    }
    _trips = Query(filter: classPredicate, sort: \.startDate, order: .forward)
  }

  var body: some View { ... }
}
```

### SampleTrips Versioned Schema 2.0 — [8:26]

```swift
enum SampleTripsSchemaV2: VersionedSchema {
  static var versionIdentifier: Schema.Version { Schema.Version(2, 0, 0) }
  static var models: [any PersistentModel.Type] {
    [SampleTripsSchemaV2.Trip.self, BucketListItem.self, LivingAccommodation.self]
  }

  @Model
  class Trip {
    @Attribute(.unique) var name: String
    var destination: String

    @Attribute(originalName: "start_date") var startDate: Date
    @Attribute(originalName: "end_date") var endDate: Date

    var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?

    ...
  }
}
```

### SampleTrips Custom Migration Stage from Version 1.0 to 2.0 — [8:41]

```swift
static let migrateV1toV2 = MigrationStage.custom(
   fromVersion: SampleTripsSchemaV1.self,
   toVersion: SampleTripsSchemaV2.self,
   willMigrate: { context in
      let fetchDesc =  FetchDescriptor<SampleTripsSchemaV1.Trip>()
      let trips = try? context.fetch(fetchDesc)

      // De-duplicate Trip instances here...

      try? context.save()
    }, 
    didMigrate: nil
)
```

### SampleTrips Versioned Schema 3.0 — [9:09]

```swift
enum SampleTripsSchemaV3: VersionedSchema {
  static var versionIdentifier: Schema.Version { Schema.Version(3, 0, 0) }
  static var models: [any PersistentModel.Type] {
    [SampleTripsSchemaV3.Trip.self, BucketListItem.self, LivingAccommodation.self]
  }

  @Model
  class Trip {
    #Unique<Trip>([\.name, \.startDate, \.endDate])
    #Index<Trip>([\.name], [\.startDate], [\.endDate], [\.name, \.startDate, \.endDate])

    @Attribute(.preserveValueOnDeletion)
    var name: String

    @Attribute(hashModifier:@"v3")
    var destination: String

    @Attribute(.preserveValueOnDeletion, originalName: "start_date")
    var startDate: Date

    @Attribute(.preserveValueOnDeletion, originalName: "end_date")
    var endDate: Date
  }
}
```

### SampleTrips Custom Migration Stage from Version 2.0 to 3.0 — [9:33]

```swift
static let migrateV2toV3 = MigrationStage.custom(
  fromVersion: SampleTripsSchemaV2.self,
  toVersion: SampleTripsSchemaV3.self,
  willMigrate: { context in
    let trips = try? context.fetch(FetchDescriptor<SampleTripsSchemaV2.Trip>())

    // De-duplicate Trip instances here...

    try? context.save()
  }, 
  didMigrate: nil
)
```

### SampleTrips Versioned Schema 4.0 — [9:50]

```swift
@available(iOS 26, *)
enum SampleTripsSchemaV4: VersionedSchema {
  static var versionIdentifier: Schema.Version { Schema.Version(4, 0, 0) }

  static var models: [any PersistentModel.Type] {
    [Trip.self, 
     BusinessTrip.self, 
     PersonalTrip.self, 
     BucketListItem.self,
     LivingAccommodation.self]
  }
}
```

### SampleTrips Lightweight Migration Stage from Version 3.0 to 4.0 — [10:03]

```swift
@available(iOS 26, *)
static let migrateV3toV4 = MigrationStage.lightweight(
  fromVersion: SampleTripsSchemaV3.self,
  toVersion: SampleTripsSchemaV4.self
)
```

### SampleTrips Schema Migration Plan — [10:24]

```swift
enum SampleTripsMigrationPlan: SchemaMigrationPlan {
  static var schemas: [any VersionedSchema.Type] {
    var currentSchemas: [any VersionedSchema.Type] =
      [SampleTripsSchemaV1.self, SampleTripsSchemaV2.self, SampleTripsSchemaV3.self]
    if #available(iOS 26, *) {
      currentSchemas.append(SampleTripsSchemaV4.self)
    }
    return currentSchemas
  }

  static var stages: [MigrationStage] {
    var currentStages = [migrateV1toV2, migrateV2toV3]
    if #available(iOS 26, *) {
      currentStages.append(migrateV3toV4)
    }
    return currentStages
  }
}
```

### Use Schema Migration Plan with ModelContainer — [10:51]

```swift
// SampleTrip App update modelContainer Scene modifier for migrated container

@main
struct TripsApp: App {

  let container: ModelContainer = {
    do {
      let schema = Schema(versionedSchema: SampleTripsSchemaV4.self)
      container = try ModelContainer(
        for: schema, migrationPlan: SampleTripsMigrationPlan.self)
    } catch { ... }
    return container
  }()
  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .modelContainer(container)
  }
}
```

### Add search predicate to Query — [11:48]

```swift
// Trip App add search text to predicate
struct ContentView: View {
  @Query
  var trips: [Trip]

  init( ... ) {
    let classPredicate: Predicate<Trip>? = {
      switch segment.wrappedValue {
      case .personal:
        return #Predicate { $0 is PersonalTrip }
      case .business:
        return #Predicate { $0 is BusinessTrip }
      default:
        return nil
      }
    }

    let searchPredicate = #Predicate<Trip> {
      searchText.isEmpty ? true : 
        $0.name.localizedStandardContains(searchText) ||              
        $0.destination.localizedStandardContains(searchText)
    }

    let fullPredicate: Predicate<Trip>
    if let classPredicate {
      fullPredicate = #Predicate { classPredicate.evaluate($0) &&
                                   searchPredicate.evaluate($0)}
    } else { 
      fullPredicate = searchPredicate
    }
    _trips = Query(filter: fullPredicate, sort: \.startDate, order: .forward)
  }
  var body: some View { ... }
}
```

### Tailor SwiftData Fetch in Custom Migration Stage — [12:31]

```swift
static let migrateV1toV2 = MigrationStage.custom(
   fromVersion: SampleTripsSchemaV1.self,
   toVersion: SampleTripsSchemaV2.self,
   willMigrate: { context in
      var fetchDesc =  FetchDescriptor<SampleTripsSchemaV1.Trip>()
      fetchDesc.propertiesToFetch = [\.name]

      let trips = try? context.fetch(fetchDesc)

      // De-duplicate Trip instances here...

      try? context.save()
    }, 
    didMigrate: nil
)
```

### Add relationshipsToPrefetch in Custom Migration Stage — [13:11]

```swift
static let migrateV1toV2 = MigrationStage.custom(
   fromVersion: SampleTripsSchemaV1.self,
   toVersion: SampleTripsSchemaV2.self,
   willMigrate: { context in
      var fetchDesc =  FetchDescriptor<SampleTripsSchemaV1.Trip>()
      fetchDesc.propertiesToFetch = [\.name]
      fetchDesc.relationshipKeyPathsForPrefetching = [\.livingAccommodation]

      let trips = try? context.fetch(fetchDesc)

      // De-duplicate Trip instances here...

      try? context.save()
    }, 
    didMigrate: nil
)
```

### Update Widget to harness fetchLimit — [13:28]

```swift
// Widget code to get new Timeline Entry

func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> Void) {
  let currentDate = Date.now
  var fetchDesc = FetchDescriptor(sortBy: [SortDescriptor(\Trip.startDate, order: .forward)])
  fetchDesc.predicate = #Predicate { $0.endDate >= currentDate }

  fetchDesc.fetchLimit = 1

  let modelContext = ModelContext(DataModel.shared.modelContainer)
  if let upcomingTrips = try? modelContext.fetch(fetchDesc) {
    if let trip = upcomingTrips.first { ... }

  }
}
```

### Fetch the last transaction efficiently — [16:24]

```swift
// Fetch history with sortBy and fetchlimit to get the last token

var historyDesc = HistoryDescriptor<DefaultHistoryTransaction>()
historyDesc.sortBy = [.init(\.transactionIdentifier, order: .reverse)]
historyDesc.fetchLimit = 1

let transactions = try context.fetchHistory(historyDesc)
if let transaction = transactions.last {
  historyToken = transaction.token
}
```

### Fetch History after the given token and only for the entities of concern — [17:29]

```swift
// Changes AFTER the last known token
let tokenPredicate = #Predicate<DefaultHistoryTransaction> { $0.token > historyToken }

// Changes for ONLY entities of concern
let entityNames = [LivingAccommodation.self, Trip.self]
let changesPredicate = #Predicate<DefaultHistoryTransaction> {
                         $0.changes.contains { change in
                           entityNames.contains(change.changedPersistentIdentifier.entityName)
                         }
                       }


let fullPredicate = #Predicate<DefaultHistoryTransaction> {
                      tokenPredicate.evaluate($0)
                      &&
                      changesPredicate.evaluate($0)
                    }

let historyDesc = HistoryDescriptor<DefaultHistoryTransaction>(predicate: fullPredicate)
let transactions = try context.fetchHistory(historyDesc)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/291/4/446be11b-b8d3-42dd-b981-a22010ddbbe9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/291/4/446be11b-b8d3-42dd-b981-a22010ddbbe9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/291) — developer.apple.com. Indexed for agent consumption._
