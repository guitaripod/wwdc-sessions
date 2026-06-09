---
id: "wwdc2021-10194"
event: "wwdc2021"
year: 2021
title: "Swift concurrency: Update a sample app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10194"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Swift concurrency: Update a sample app

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10194](https://developer.apple.com/videos/play/wwdc2021/10194)

Discover Swift concurrency in action: Follow along as we update an existing sample app. Get real-world experience with async/await, actors, and continuations. We’ll also explore techniques for migrating existing code to Swift concurrency over time. To get the most out of this code-along, we recommend first watching “Meet async/await in Swift” and “Protect mutable state with Swift actors” from WWDC21. Note: To create an async task in Xcode 13 beta 3 and later, use the Task initializer instead.

**Keywords:** `caffeine`, `codealong`, `coffeetracker`, `completionhandler`, `complication`, `condition`, `dispatchqueue`, `drinklist`, `handler`, `healthkit`, `immutable`, `mainactor`, `mutable`, `nonisolated`, `observableobject`, `published`, `queues`, `race`, `thread`, `uimodel`, `watch`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(7,005 words)

## Documentation & Resources

- [Updating an App to Use Swift Concurrency](https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swift/updating_an_app_to_use_swift_concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swift/updating_an_app_to_use_swift_concurrency.json
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Call the async version of the HKHealthKitStore save(_:) method — [7:34]

```swift
do {
    try await store.save(caffeineSample)
    self.logger.debug("\(mgCaffeine) mg Drink saved to HealthKit")
} catch {
    self.logger.error("Unable to save \(caffeineSample) to the HealthKit store: \(error.localizedDescription)")
}
```

### Change save(drink:) to be an async function — [9:38]

```swift
public func save(drink: Drink) async {
```

### Create a new asynchronous task — [10:15]

```swift
Task { await self.healthKitController.save(drink: drink) }
```

### Add an async alternative for requestAuthorization(completionHandler:) — [12:13]

```swift
@available(*, deprecated, message: "Prefer async alternative instead")
public func requestAuthorization(completionHandler: @escaping (Bool) -> Void ) {
    Task {
        let result = await requestAuthorization()
        completionHandler(result)
    }
}
```

### Update the async version of requestAuthorization() — [14:55]

```swift
public func requestAuthorization() async -> Bool {
    guard isAvailable else { return false }

    do {
        try await store.requestAuthorization(toShare: types, read: types)
        self.isAuthorized = true
        return true
    } catch let error {
        self.logger.error("An error occurred while requesting HealthKit Authorization: \(error.localizedDescription)")
        return false
    }
}
```

### Add an async alternative for loadNewDataFromHealthKit(completionHandler:) — [15:43]

```swift
@available(*, deprecated, message: "Prefer async alternative instead")
public func loadNewDataFromHealthKit(completionHandler: @escaping (Bool) -> Void = { _ in }) {
    Task { completionHandler(await self.loadNewDataFromHealthKit()) }
}
```

### Create a queryHealthKit() helper function that uses a continuation — [17:43]

```swift
private func queryHealthKit() async throws -> ([HKSample]?, [HKDeletedObject]?, HKQueryAnchor?) {
    return try await withCheckedThrowingContinuation { continuation in
        // Create a predicate that only returns samples created within the last 24 hours.
        let endDate = Date()
        let startDate = endDate.addingTimeInterval(-24.0 * 60.0 * 60.0)
        let datePredicate = HKQuery.predicateForSamples(withStart: startDate, end: endDate, options: [.strictStartDate, .strictEndDate])

        // Create the query.
        let query = HKAnchoredObjectQuery(
            type: caffeineType,
            predicate: datePredicate,
            anchor: anchor,
            limit: HKObjectQueryNoLimit) { (_, samples, deletedSamples, newAnchor, error) in

            // When the query ends, check for errors.
            if let error = error {
                continuation.resume(throwing: error)
            } else {
                continuation.resume(returning: (samples, deletedSamples, newAnchor))
            }
        }
        store.execute(query)
    }
}
```

### Update the async version of loadNewDataFromHealthKit() — [20:17]

```swift
@discardableResult
public func loadNewDataFromHealthKit() async -> Bool {

    guard isAvailable else {
        logger.debug("HealthKit is not available on this device.")
        return false
    }

    logger.debug("Loading data from HealthKit")

    do {
        let (samples, deletedSamples, newAnchor) = try await queryHealthKit()

        // Update the anchor.
        self.anchor = newAnchor

        // Convert new caffeine samples into Drink instances.
        let newDrinks: [Drink]
        if let samples = samples {
            newDrinks = self.drinksToAdd(from: samples)
        } else {
            newDrinks = []
        }

        // Create a set of UUIDs for any samples deleted from HealthKit.
        let deletedDrinks = self.drinksToDelete(from: deletedSamples ?? [])

        // Update the data on the main queue.
        await MainActor.run {
            // Update the model.
            self.updateModel(newDrinks: newDrinks, deletedDrinks: deletedDrinks)
        }
        return true
    } catch {
        self.logger.error("An error occurred while querying for samples: \(error.localizedDescription)")
        return false
    }
}
```

### Annotate updateModel(newDrinks:deletedDrinks:) with @MainActor — [25:09]

```swift
@MainActor
private func updateModel(newDrinks: [Drink], deletedDrinks: Set<UUID>) {
```

### Remove MainActor.run from the call site of updateModel(newDrinks:deletedDrinks:) — [26:43]

```swift
await self.updateModel(newDrinks: newDrinks, deletedDrinks: deletedDrinks)
```

### Change HealthKitController to be an actor — [29:24]

```swift
actor HealthKitController {
```

### Move updateModel(newDrinks:deletedDrinks:) to CoffeeData — [32:31]

```swift
@MainActor
public func updateModel(newDrinks: [Drink], deletedDrinks: Set<UUID>) {

    guard !newDrinks.isEmpty && !deletedDrinks.isEmpty else {
        logger.debug("No drinks to add or delete from HealthKit.")
        return
    }

    // Remove the deleted drinks.
    var drinks = currentDrinks.filter { deletedDrinks.contains($0.uuid) }

    // Add the new drinks.
    drinks += newDrinks

    // Sort the array by date.
    drinks.sort { $0.date < $1.date }

    currentDrinks = drinks
}
```

### Update the call site of updateModel(newDrinks:deletedDrinks:) — [33:18]

```swift
await model?.updateModel(newDrinks: newDrinks, deletedDrinks: deletedDrinks)
```

### Mark the deprecated completion handler methods as nonisolated — [34:01]

```swift
@available(*, deprecated, message: "Prefer async alternative instead")
nonisolated public func requestAuthorization(completionHandler: @escaping (Bool) -> Void ) {
    // ...
}

@available(*, deprecated, message: "Prefer async alternative instead")
nonisolated public func loadNewDataFromHealthKit(completionHandler: @escaping (Bool) -> Void = { _ in }) {
    // ...
}
```

### Create a private CoffeeDataStore actor for loading and saving — [36:20]

```swift
private actor CoffeeDataStore {

}
```

### Add a dedicated logger for CoffeeDataStore — [36:43]

```swift
let logger = Logger(subsystem: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeDataStore", category: "ModelIO")
```

### Add an instance of the actor to CoffeeData — [37:05]

```swift
private let store = CoffeeDataStore()
```

### Move the savedValue property from CoffeeData to CoffeeDataStore — [38:37]

```swift
private var savedValue: [Drink] = []
```

### Move the dataURL property from CoffeeData to CoffeeDataStore — [39:00]

```swift
private var dataURL: URL {
    get throws {
        try FileManager
            .default
            .url(for: .documentDirectory,
                 in: .userDomainMask,
                 appropriateFor: nil,
                 create: false)
            // Append the file name to the directory.
            .appendingPathComponent("CoffeeTracker.plist")
    }
}
```

### Move the didSet for currentDrinks to a new async function — [42:42]

```swift
@Published public private(set) var currentDrinks: [Drink] = []

private func drinksUpdated() async {
    logger.debug("A value has been assigned to the current drinks property.")

    // Update any complications on active watch faces.
    let server = CLKComplicationServer.sharedInstance()
    for complication in server.activeComplications ?? [] {
        server.reloadTimeline(for: complication)
    }

    // Begin saving the data.
    await store.save(currentDrinks)
}
```

### Update addDrink(mgCaffeine:onData:) to call drinksUpdated() — [44:00]

```swift
// Save drink information to HealthKit.
Task {
    await self.healthKitController.save(drink: drink)
    await self.drinksUpdated()
}
```

### Update updateModel(newDrinks:deletedDrinks:) to call drinksUpdated() — [44:09]

```swift
await drinksUpdated()
```

### Mark the updateModel(newDrinks:deletedDrinks:) method as async — [44:17]

```swift
@MainActor
public func updateModel(newDrinks: [Drink], deletedDrinks: Set<UUID>) async {
```

### Complete the move of the save() method into CoffeeDataStore — [45:26]

```swift
// Begin saving the drink data to disk.
func save(_ currentDrinks: [Drink]) {

    // Don't save the data if there haven't been any changes.
    if currentDrinks == savedValue {
        logger.debug("The drink list hasn't changed. No need to save.")
        return
    }

    // Save as a binary plist file.
    let encoder = PropertyListEncoder()
    encoder.outputFormat = .binary

    let data: Data

    do {
        // Encode the currentDrinks array.
        data = try encoder.encode(currentDrinks)
    } catch {
        logger.error("An error occurred while encoding the data: \(error.localizedDescription)")
        return
    }

    // Save the data to disk as a binary plist file.
    do {
        // Write the data to disk.
        try data.write(to: self.dataURL, options: [.atomic])

        // Update the saved value.
        self.savedValue = currentDrinks

        self.logger.debug("Saved!")
    } catch {
        self.logger.error("An error occurred while saving the data: \(error.localizedDescription)")
    }
}
```

### Move the top part of the load() method into CoffeeDataStore — [46:20]

```swift
func load() -> [Drink] {
    logger.debug("Loading the model.")

    var drinks: [Drink]

    do {
        // Load the drink data from a binary plist file.
        let data = try Data(contentsOf: self.dataURL)

        // Decode the data.
        let decoder = PropertyListDecoder()
        drinks = try decoder.decode([Drink].self, from: data)
        logger.debug("Data loaded from disk")
    } catch CocoaError.fileReadNoSuchFile {
        logger.debug("No file found--creating an empty drink list.")
        drinks = []
    } catch {
        fatalError("*** An unexpected error occurred while loading the drink list: \(error.localizedDescription) ***")
    }

    // Update the saved value.
    savedValue = drinks
    return drinks
}
```

### Update the load() method in CoffeeData to use the actor — [48:01]

```swift
func load() async {
    var drinks = await store.load()

    // Drop old drinks
    drinks.removeOutdatedDrinks()

    // Assign loaded drinks to model
    currentDrinks = drinks

    // Load new data from HealthKit.
    let success = await self.healthKitController.requestAuthorization()
    guard success else {
        logger.debug("Unable to authorize HealthKit.")
        return
    }

    await self.healthKitController.loadNewDataFromHealthKit()
}
```

### Update the CoffeeData initializer to use an async task — [49:08]

```swift
Task { await load() }
```

### Annotate CoffeeData with @MainActor — [50:03]

```swift
@MainActor
class CoffeeData: ObservableObject {
```

### Replace the completion handler usage in the handle(_:) method of ExtensionDelegate — [52:18]

```swift
// Check for updates from HealthKit.
let model = CoffeeData.shared

Task {
    let success = await model.healthKitController.loadNewDataFromHealthKit()

    if success {
        // Schedule the next background update.
        scheduleBackgroundRefreshTasks()
        self.logger.debug("Background Task Completed Successfully!")
    }

    // Mark the task as ended, and request an updated snapshot, if necessary.
    backgroundTask.setTaskCompletedWithSnapshot(success)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10194/12/ED815E9C-D0B9-4B94-ABA6-1EFDCFB2D5D4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10194/12/ED815E9C-D0B9-4B94-ABA6-1EFDCFB2D5D4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10194) — developer.apple.com. Indexed for agent consumption._
