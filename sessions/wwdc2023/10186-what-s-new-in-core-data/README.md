---
id: "wwdc2023-10186"
event: "wwdc2023"
year: 2023
title: "What’s new in Core Data"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10186"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What’s new in Core Data

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10186](https://developer.apple.com/videos/play/wwdc2023/10186)

Elevate your app’s data persistence with improvements in Core Data. Learn how you can use composite attributes to create more intuitive data models. We’ll also show you how to migrate your schema through disruptive changes, when to defer intense migrations, and how to avoid overhead on a person’s device. To get the most out of this session, you should be familiar with handling different data types in Core Data as well as the basics of lightweight migration.

**Keywords:** `coredata`, `core data`, `custom`, `custom migration`, `data`, `data model`, `defer`, `deferred`, `deferred migration`, `lightweight`, `lightweight migration`, `migration`, `model`, `persistence`, `swift`, `swift data`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,513 words)

## Documentation & Resources

- [Migrating your data model automatically](https://developer.apple.com/documentation/CoreData/migrating-your-data-model-automatically) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/migrating-your-data-model-automatically
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/migrating-your-data-model-automatically.json
- [Core Data](https://developer.apple.com/documentation/CoreData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData.json

## Code Snippets

### Adding a composite attribute — [5:39]

```swift
enum PaintColor: String, CaseIterable, Identifiable {
    case none, white, blue, orange, red, gray, green, gold, yellow, black
    var id: Self { self }
}

extension Aircraft {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<Aircraft> {
        return NSFetchRequest<Aircraft>(entityName: "Aircraft")
    }

    @NSManaged public var aircraftCategory: String?
    @NSManaged public var aircraftClass: String?
    @NSManaged public var aircraftType: String?
    @NSManaged public var colorScheme: [String: Any]?
    @NSManaged public var photo: Data?
    @NSManaged public var tailNumber: String?
    @NSManaged public var logEntries: NSSet?

}
```

### Setting a composite attribute — [5:53]

```swift
private func addAircraft() {
    viewContext.performAndWait {
        let newAircraft = Aircraft(context: viewContext)

        newAircraft.tailNumber = tailNumber
        newAircraft.aircraftType = aircraftType
        newAircraft.aircraftClass = aircraftClass
        newAircraft.aircraftCategory = aircraftCategory

        newAircraft.colorScheme = [
            "primary": primaryColor.rawValue,
            "secondary": secondaryColor.rawValue,
            "tertiary": tertiaryColor.rawValue
        ]

        do {
            try viewContext.save()
        } catch {
            // ...
        }
    }
}
```

### Fetching a composite attribute — [6:11]

```swift
private func findAircraft(with color: String) {
    viewContext.performAndWait {
        let fetchRequest = Aircraft.fetchRequest()
        fetchRequest.predicate = NSPredicate(format: "colorScheme.primary == %@", color)

        do {
            var fetchedResults: [Aircraft]
            fetchedResults = try viewContext.fetch(fetchRequest)

            // ...
        } catch {
            // Handle any errors that may occur
        }
    }
}
```

### Creating managed object model references for staged migration — [16:00]

```swift
let v1ModelChecksum = "kk8XL4OkE7gYLFHTrH6W+EhTw8w14uq1klkVRPiuiAk="
let v1ModelReference = NSManagedObjectModelReference(
    modelName: "modelV1"
    in: NSBundle.mainBundle
    versionChecksum: v1ModelChecksum
)

let v2ModelChecksum = "PA0Gbxs46liWKg7/aZMCBtu9vVIF6MlskbhhjrCd7ms="
let v2ModelReference = NSManagedObjectModelReference(
    modelName: "modelV2"                          
    in: NSBundle.mainBundle                                                 
    versionChecksum: v2ModelChecksum
)

let v3ModelChecksum = "iWKg7bxs46g7liWkk8XL4OkE7gYL/FHTrH6WF23Jhhs="
let v3ModelReference = NSManagedObjectModelReference(
    modelName: "modelV3"
    in: NSBundle.mainBundle
    versionChecksum: v3ModelChecksum
)
```

### Creating migration stages for staged migration — [16:19]

```swift
let lightweightStage = NSLightweightMigrationStage([v1ModelChecksum])
lightweightStage.label = "V1 to V2: Add flightData attribute"

let customStage = NSCustomMigrationStage(
    migratingFrom: v2ModelReference,
    to: v3ModelReference
)

customStage.label = "V2 to V3: Denormalize model with FlightData entity"
```

### willMigrationHandler and didMigrationHandler of NSCustomMigrationStage — [16:54]

```swift
customStage.willMigrateHandler = { migrationManager, currentStage in
    guard let container = migrationManager.container else {
        return
    }

    let context = container.newBackgroundContext()
    try context.performAndWait {
        let fetchRequest = NSFetchRequest<NSFetchRequestResult>(entityName: "Aircraft")
        fetchRequest.predicate = NSPredicate(format: "flightData != nil")

        do {
           var fetchedResults: [NSManagedObject]
           fetchedResults = try viewContext.fetch(fetchRequest)

           for airplane in fetchedResults {
                let fdEntity = NSEntityDescription.insertNewObject(
                    forEntityName: "FlightData,
                    into: context
                )

                let flightData = airplane.value(forKey: "flightData")
                fdEntity.setValue(flightData, forKey: “data”)
                fdEntity.setValue(airplane, forKey: "aircraft")
                airplane.setValue(nil, forKey: "flightData")
            }
            try context.save()
        } catch {
            // Handle any errors that may occur
        }
    }
}
```

### Loading the persistent stores with an NSStagedMigrationManager — [17:41]

```swift
let migrationStages = [lightweightStage, customStage]
let migrationManager = NSStagedMigrationManager(migrationStages)

let persistentContainer = NSPersistentContainer(
    path: "/path/to/store.sqlite",
    managedObjectModel: myModel
)

var storeDescription = persistentContainer?.persistentStoreDescriptions.first

storeDescription?.setOption(
    migrationManager,
    forKey: NSPersistentStoreStagedMigrationManagerOptionKey
)

persistentContainer?.loadPersistentStores { storeDescription, error in
    if let error = error {
        // Handle any errors that may occur
    }
}
```

### Adding a persistent store with NSPersistentStoreDeferredLightweightMigrationOptionKey option — [21:01]

```swift
let options = [
    NSPersistentStoreDeferredLightweightMigrationOptionKey: true,
    NSMigratePersistentStoresAutomaticallyOption: true,
    NSInferMappingModelAutomaticallyOption: true
]

let store = try coordinator.addPersistentStore(
    ofType: NSSQLiteStoreType,
    configurationName: nil,
    at: storeURL,
    options: options
)
```

### Executing deferred migrations — [21:17]

```swift
// After using BGProcessingTask to run migration work   
let metadata = coordinator.metadata(for: store)
if (metadata[NSPersistentStoreDeferredLightweightMigrationOptionKey] == true) {
    coordinator.finishDeferredLightweightMigration()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10186/4/169A3CA9-FA4A-40D0-A3A5-3635916BBCCE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10186/4/169A3CA9-FA4A-40D0-A3A5-3635916BBCCE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10186) — developer.apple.com. Indexed for agent consumption._
