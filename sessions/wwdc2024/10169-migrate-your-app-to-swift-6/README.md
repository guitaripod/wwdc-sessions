---
id: "wwdc2024-10169"
event: "wwdc2024"
year: 2024
title: "Migrate your app to Swift 6"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10169"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Migrate your app to Swift 6

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10169](https://developer.apple.com/videos/play/wwdc2024/10169)

Experience Swift 6 migration in action as we update an existing sample app. Learn how to migrate incrementally, module by module, and how the compiler helps you identify code that’s at risk of data races. Discover different techniques for ensuring clear isolation boundaries and eliminating concurrent access to shared mutable state.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,091 words)

## Documentation & Resources

- [Swift Migration Guide](https://www.swift.org/migration/documentation/migrationguide/) _documentation_
- [Updating an app to use strict concurrency](https://developer.apple.com/documentation/Swift/updating-an-app-to-use-strict-concurrency) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/updating-an-app-to-use-strict-concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/updating-an-app-to-use-strict-concurrency.json
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010

## Code Snippets

### Recaffeinater and CaffeineThresholdDelegate — [9:08]

```swift
//Define Recaffeinator class
class Recaffeinater: ObservableObject {
    @Published var recaffeinate: Bool = false
    var minimumCaffeine: Double = 0.0
}

//Add protocol to notify if caffeine level is dangerously low
extension Recaffeinater: CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### Add @MainActor to isolate the Recaffeinator — [9:26]

```swift
//Isolate the Recaffeinater class to the main actor
@MainActor
class Recaffeinater: ObservableObject {
    @Published var recaffeinate: Bool = false
    var minimumCaffeine: Double = 0.0
}
```

### Warning in the protocol implementation — [9:38]

```swift
//warning: Main actor-isolated instance method 'caffeineLevel(at:)' cannot be used to satisfy nonisolated protocol requirement
public func caffeineLevel(at level: Double) {
      if level < minimumCaffeine {
          // TODO: alert user to drink more coffee!
      }
}
```

### Understanding why the warning is there — [9:59]

```swift
//This class is guaranteed on the main actor...
@MainActor
class Recaffeinater: ObservableObject {
    @Published var recaffeinate: Bool = false
    var minimumCaffeine: Double = 0.0
}

//...but this protocol is not
extension Recaffeinater: CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### A warning on the logger variable — [12:59]

```swift
//var 'logger' is not concurrency-safe because it is non-isolated global shared mutable state; this is an error in the Swift 6 language mode
var logger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.ContentView",
    category: "Root View")
```

### Option 1: Convert 'logger' to a 'let' constant — [13:38]

```swift
//Option 1: Convert 'logger' to a 'let' constant to make 'Sendable' shared state immutable
let logger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.ContentView",
    category: "Root View")
```

### Option 2: Isolate 'logger' it to the main actor — [14:20]

```swift
//Option 2: Annotate 'logger' with '@MainActor' if property should only be accessed from the main actor
@MainActor var logger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.ContentView",
    category: "Root View")
```

### Option 3: Mark it nonisolated(unsafe) — [14:58]

```swift
//Option 3: Disable concurrency-safety checks if accesses are protected by an external synchronization mechanism
nonisolated(unsafe) var logger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.ContentView",
    category: "Root View")
```

### The right answer — [15:43]

```swift
//Option 1: Convert 'logger' to a 'let' constant to make 'Sendable' shared state immutable
let logger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.ContentView",
    category: "Root View")
```

### scheduleBackgroundRefreshTasks() has two warnings — [17:03]

```swift
func scheduleBackgroundRefreshTasks() {

    scheduleLogger.debug("Scheduling a background task.")

    // Get the shared extension object.
    let watchExtension = WKApplication.shared() //warning: Call to main actor-isolated class method 'shared()' in a synchronous nonisolated context

    // If there is a complication on the watch face, the app should get at least four
    // updates an hour. So calculate a target date 15 minutes in the future.
    let targetDate = Date().addingTimeInterval(15.0 * 60.0)

    // Schedule the background refresh task.
    watchExtension.scheduleBackgroundRefresh(withPreferredDate: targetDate, userInfo: nil) { //warning: Call to main actor-isolated instance method 'scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)' in a synchronous nonisolated context
        error in

        // Check for errors.
        if let error {
            scheduleLogger.error(
                "An error occurred while scheduling a background refresh task: \(error.localizedDescription)"
            )
            return
        }

        scheduleLogger.debug("Task scheduled!")
    }
}
```

### Annotate function with @MainActor — [17:57]

```swift
@MainActor func scheduleBackgroundRefreshTasks() {

    scheduleLogger.debug("Scheduling a background task.")

    // Get the shared extension object.
    let watchExtension = WKApplication.shared()

    // If there is a complication on the watch face, the app should get at least four
    // updates an hour. So calculate a target date 15 minutes in the future.
    let targetDate = Date().addingTimeInterval(15.0 * 60.0)

    // Schedule the background refresh task.
    watchExtension.scheduleBackgroundRefresh(withPreferredDate: targetDate, userInfo: nil) {
        error in

        // Check for errors.
        if let error {
            scheduleLogger.error(
                "An error occurred while scheduling a background refresh task: \(error.localizedDescription)"
            )
            return
        }

        scheduleLogger.debug("Task scheduled!")
    }
}
```

### Revisiting the Recaffeinater — [22:15]

```swift
//This class is guaranteed on the main actor...
@MainActor
class Recaffeinater: ObservableObject {
    @Published var recaffeinate: Bool = false
    var minimumCaffeine: Double = 0.0
}

//...but this protocol is not
//warning: Main actor-isolated instance method 'caffeineLevel(at:)' cannot be used to satisfy nonisolated protocol requirement
extension Recaffeinater: CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### Option 1: Mark function as nonisolated — [22:26]

```swift
//error: Main actor-isolated property 'minimumCaffeine' can not be referenced from a non-isolated context
nonisolated public func caffeineLevel(at level: Double) {
    if level < minimumCaffeine {
        // TODO: alert user to drink more coffee!
    }
}
```

### Option 1b: Wrap functionality in a Task — [23:07]

```swift
nonisolated public func caffeineLevel(at level: Double) {
    Task { @MainActor in
      if level < minimumCaffeine {
        // TODO: alert user to drink more coffee!
    	}
    }
}
```

### Option 1c: Explore options to update the protocol — [23:34]

```swift
public protocol CaffeineThresholdDelegate: AnyObject {
    func caffeineLevel(at level: Double)
}
```

### Option 1d: Instead of wrapping it in a Task, use `MainActor.assumeisolated` — [24:15]

```swift
nonisolated public func caffeineLevel(at level: Double) {
    MainActor.assumeIsolated {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### `@preconcurrency` as a shorthand for assumeIsolated — [25:21]

```swift
extension Recaffeinater: @preconcurrency CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### Add `@MainActor` to the delegate protocol in CoffeeKit — [26:42]

```swift
@MainActor
public protocol CaffeineThresholdDelegate: AnyObject {
    func caffeineLevel(at level: Double)
}
```

### A new warning — [26:50]

```swift
//warning: @preconcurrency attribute on conformance to 'CaffeineThresholdDelegate' has no effect
extension Recaffeinater: @preconcurrency CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### Remove @preconcurrency — [27:09]

```swift
extension Recaffeinater: CaffeineThresholdDelegate {
    public func caffeineLevel(at level: Double) {
        if level < minimumCaffeine {
            // TODO: alert user to drink more coffee!
        }
    }
}
```

### Global variables in CoffeeKit are marked as `var` — [29:56]

```swift
//warning: Var 'hkLogger' is not concurrency-safe because it is non-isolated global shared mutable state
private var hkLogger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.HealthKitController",
    category: "HealthKit")

// The key used to save and load anchor objects from user defaults.
//warning: Var 'anchorKey' is not concurrency-safe because it is non-isolated global shared mutable state
private var anchorKey = "anchorKey"

// The HealthKit store.
// warning: Var 'store' is not concurrency-safe because it is non-isolated global shared mutable state
private var store = HKHealthStore()
// warning: Var 'isAvailable' is not concurrency-safe because it is non-isolated global shared mutable state
private var isAvailable = HKHealthStore.isHealthDataAvailable()

// Caffeine types, used to read and write caffeine samples.
// warning: Var 'caffeineType' is not concurrency-safe because it is non-isolated global shared mutable state
private var caffeineType = HKObjectType.quantityType(forIdentifier: .dietaryCaffeine)!
// warning: Var 'types' is not concurrency-safe because it is non-isolated global shared mutable state
private var types: Set<HKSampleType> = [caffeineType]

// Milligram units.
// warning: Var 'miligrams' is not concurrency-safe because it is non-isolated global shared mutable state
internal var miligrams = HKUnit.gramUnit(with: .milli)
```

### Change all global variables to `let` — [30:19]

```swift
private let hkLogger = Logger(
    subsystem:
        "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.HealthKitController",
    category: "HealthKit")

// The key used to save and load anchor objects from user defaults.
private let anchorKey = "anchorKey"

// The HealthKit store.
private let store = HKHealthStore()
private let isAvailable = HKHealthStore.isHealthDataAvailable()

// Caffeine types, used to read and write caffeine samples.
private let caffeineType = HKObjectType.quantityType(forIdentifier: .dietaryCaffeine)!
private let types: Set<HKSampleType> = [caffeineType]

// Milligram units.
internal let miligrams = HKUnit.gramUnit(with: .milli)
```

### Warning 1: Sending arrays in `drinksUpdated()` — [30:38]

```swift
// warning: Sending 'self.currentDrinks' risks causing data races
// Sending main actor-isolated 'self.currentDrinks' to actor-isolated instance method 'save' risks causing data races between actor-isolated and main actor-isolated uses
await store.save(currentDrinks)
```

### Looking at Drink struct — [32:04]

```swift
// The record of a single drink.
public struct Drink: Hashable, Codable {

    // The amount of caffeine in the drink.
    public let mgCaffeine: Double

    // The date when the drink was consumed.
    public let date: Date

    // A globally unique identifier for the drink.
    public let uuid: UUID

    public let type: DrinkType?

    public var latitude, longitude: Double?

    // The drink initializer.
    public init(type: DrinkType, onDate date: Date, uuid: UUID = UUID()) {
        self.mgCaffeine = type.mgCaffeinePerServing
        self.date = date
        self.uuid = uuid
        self.type = type
    }

    internal init(from sample: HKQuantitySample) {
        self.mgCaffeine = sample.quantity.doubleValue(for: miligrams)
        self.date = sample.startDate
        self.uuid = sample.uuid
        self.type = nil
    }

    // Calculate the amount of caffeine remaining at the provided time,
    // based on a 5-hour half life.
    public func caffeineRemaining(at targetDate: Date) -> Double {
        // Calculate the number of half-life time periods (5-hour increments)
        let intervals = targetDate.timeIntervalSince(date) / (60.0 * 60.0 * 5.0)
        return mgCaffeine * pow(0.5, intervals)
    }
}
```

### Mark `Drink` struct as Sendable — [33:29]

```swift
// The record of a single drink.
public struct Drink: Hashable, Codable, Sendable {
  //...
}
```

### Another type that isn't Sendable — [33:35]

```swift
// warning: Stored property 'type' of 'Sendable'-conforming struct 'Drink' has non-sendable type 'DrinkType?'
public let type: DrinkType?
```

### Using nonisolated(unsafe) — [34:28]

```swift
nonisolated(unsafe)
public let type: DrinkType?
```

### Undo that change — [34:45]

```swift
public let type: DrinkType?
```

### Change DrinkType to be Sendable — [35:04]

```swift
// Define the types of drinks supported by Coffee Tracker.
public enum DrinkType: Int, CaseIterable, Identifiable, Codable, Sendable {
  //...
}
```

### CoreLocation using AsyncSequence — [36:35]

```swift
//Create a new drink to add to the array.
var drink = Drink(type: type, onDate: date)

do {
  //error: 'CLLocationUpdate' is only available in watchOS 10.0 or newer
  for try await update in CLLocationUpdate.liveUpdates() {
    guard let coord = update.location else {
      logger.info( "Update received but no location, \(update.location)")
      break
    }
    drink.latitude = coord.coordinate.latitude
    drink.longitude = coord.coordinate.longitude
  } catch {

  }
```

### Create a CoffeeLocationDelegate — [38:10]

```swift
class CoffeeLocationDelegate: NSObject, CLLocationManagerDelegate {
  var location: CLLocation?
  var manager: CLLocationManager!

  var latitude: CLLocationDegrees? { location?.coordinate.latitude } 
  var longitude: CLLocationDegrees? { location?.coordinate.longitude }

  override init () {
    super.init()
    manager = CLLocationManager()
    manager.delegate = self
    manager.startUpdatingLocation()
  }

  func locationManager (
    _ manager: CLLocationManager, 
    didUpdateLocations locations: [CLLocation]
  ) {
      self.location = locations. last
  }
}
```

### Put the CoffeeLocationDelegate on the main actor — [39:32]

```swift
@MainActor
class CoffeeLocationDelegate: NSObject, CLLocationManagerDelegate {
  var location: CLLocation?
  var manager: CLLocationManager!

  var latitude: CLLocationDegrees? { location?.coordinate.latitude } 
  var longitude: CLLocationDegrees? { location?.coordinate.longitude }

  override init () {
    super.init()
    // This CLLocationManager will be initialized on the main thread
    manager = CLLocationManager()
    manager.delegate = self
    manager.startUpdatingLocation()
  }

  // error: Main actor-isolated instance method 'locationManager_:didUpdateLocations:)' cannot be used to satisfy nonisolated protocol requirement
  func locationManager (
    _ manager: CLLocationManager, 
    didUpdateLocations locations: [CLLocation]
  ) {
      self.location = locations. last
  }
}
```

### Update the locationManager function — [40:06]

```swift
nonisolated func locationManager (
  _ manager: CLLocationManager, 
  didUpdateLocations locations: [CLLocation]
) {
    MainActor.assumeIsolated { self.location = locations. last }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10169/6/4E4B2CB2-ABE3-49B7-AA2B-D97C6BF13B49/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10169/6/4E4B2CB2-ABE3-49B7-AA2B-D97C6BF13B49/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10169) — developer.apple.com. Indexed for agent consumption._
