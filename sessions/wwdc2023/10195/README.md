---
id: "wwdc2023-10195"
event: "wwdc2023"
year: 2023
title: "Model your schema with SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10195"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Model your schema with SwiftData

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10195](https://developer.apple.com/videos/play/wwdc2023/10195)

Learn how to use schema macros and migration plans with SwiftData to build more complex features for your app. We’ll show you how to fine-tune your persistence with @Attribute and @Relationship options. Learn how to exclude properties from your data model with @Transient and migrate from one version of your schema to the next with ease.

To get the most out of this session, we recommend first watching "Meet SwiftData" and "Build an app with SwiftData" from WWDC23.

**Keywords:** `@attribute`, `coredata`, `core data`, `data`, `fetchdescriptor`, `macro`, `macros`, `model`, `@model`, `models`, `persistence`, `predicate`, `#predicate`, `@relationship`, `sortdescriptor`, `swift`, `swiftdata`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,392 words)

## Documentation & Resources

- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/adopting-swiftdata-for-a-core-data-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/adopting-swiftdata-for-a-core-data-app.json

## Code Snippets

### Original Trip model — [0:56]

```swift
import SwiftUI
import SwiftData

@Model
final class Trip {
    var name: String
    var destination: String
    var start_date: Date
    var end_date: Date

    var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?
}
```

### Adding a unique attribute — [1:50]

```swift
@Model 
final class Trip {
    @Attribute(.unique) var name: String
    var destination: String
    var start_date: Date
    var end_date: Date

    var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?
}
```

### Specifying original property names — [2:48]

```swift
@Model 
final class Trip {
    @Attribute(.unique) var name: String
    var destination: String
    @Attribute(originalName: "start_date") var startDate: Date
    @Attribute(originalName: "end_date") var endDate: Date

    var bucketList: [BucketListItem]? = []
    var livingAccommodation: LivingAccommodation?
}
```

### Cascading delete rule — [4:00]

```swift
@Model 
final class Trip {
    @Attribute(.unique) var name: String
    var destination: String
    @Attribute(originalName: "start_date") var startDate: Date
    @Attribute(originalName: "end_date") var endDate: Date

    @Relationship(.cascade)
    var bucketList: [BucketListItem]? = []

    @Relationship(.cascade)
    var livingAccommodation: LivingAccommodation?
}
```

### Transient properties — [4:54]

```swift
@Model 
final class Trip {
    @Attribute(.unique) var name: String
    var destination: String
    @Attribute(originalName: "start_date") var startDate: Date
    @Attribute(originalName: "end_date") var endDate: Date

    @Relationship(.cascade)
    var bucketList: [BucketListItem]? = []

    @Relationship(.cascade)
    var livingAccommodation: LivingAccommodation?

    @Transient
    var tripViews: Int = 0
}
```

### Defining versioned schemas — [7:12]

```swift
enum SampleTripsSchemaV1: VersionedSchema {
    static var models: [any PersistentModel.Type] {
        [Trip.self, BucketListItem.self, LivingAccommodation.self]
    }

    @Model
    final class Trip {
        var name: String
        var destination: String
        var start_date: Date
        var end_date: Date

        var bucketList: [BucketListItem]? = []
        var livingAccommodation: LivingAccommodation?
    }

    // Define the other models in this version...
}

enum SampleTripsSchemaV2: VersionedSchema {
    static var models: [any PersistentModel.Type] {
        [Trip.self, BucketListItem.self, LivingAccommodation.self]
    }

    @Model
    final class Trip {
        @Attribute(.unique) var name: String
        var destination: String
        var start_date: Date
        var end_date: Date

        var bucketList: [BucketListItem]? = []
        var livingAccommodation: LivingAccommodation?
    }

    // Define the other models in this version...
}

enum SampleTripsSchemaV3: VersionedSchema {
    static var models: [any PersistentModel.Type] {
        [Trip.self, BucketListItem.self, LivingAccommodation.self]
    }

    @Model
    final class Trip {
        @Attribute(.unique) var name: String
        var destination: String
        @Attribute(originalName: "start_date") var startDate: Date
        @Attribute(originalName: "end_date") var endDate: Date

        var bucketList: [BucketListItem]? = []
        var livingAccommodation: LivingAccommodation?
    }

    // Define the other models in this version...
}
```

### Implementing a SchemaMigrationPlan — [7:49]

```swift
enum SampleTripsMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] {
        [SampleTripsSchemaV1.self, SampleTripsSchemaV2.self, SampleTripsSchemaV3.self]
    }

    static var stages: [MigrationStage] {
        [migrateV1toV2, migrateV2toV3]
    }

    static let migrateV1toV2 = MigrationStage.custom(
        fromVersion: SampleTripsSchemaV1.self,
        toVersion: SampleTripsSchemaV2.self,
        willMigrate: { context in
            let trips = try? context.fetch(FetchDescriptor<SampleTripsSchemaV1.Trip>())

            // De-duplicate Trip instances here...

            try? context.save() 
        }, didMigrate: nil
    )

    static let migrateV2toV3 = MigrationStage.lightweight(
        fromVersion: SampleTripsSchemaV2.self,
        toVersion: SampleTripsSchemaV3.self
    )
}
```

### Configuring the migration plan — [8:40]

```swift
struct TripsApp: App {
    let container = ModelContainer(
        for: Trip.self, 
        migrationPlan: SampleTripsMigrationPlan.self
    )

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(container)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10195/4/1FEA69A1-120E-4305-8976-D2E1D1530A13/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10195/4/1FEA69A1-120E-4305-8976-D2E1D1530A13/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10195) — developer.apple.com. Indexed for agent consumption._