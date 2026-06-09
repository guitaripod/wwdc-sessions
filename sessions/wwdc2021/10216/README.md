---
id: "wwdc2021-10216"
event: "wwdc2021"
year: 2021
title: "ARC in Swift: Basics and beyond"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10216"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# ARC in Swift: Basics and beyond

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10216](https://developer.apple.com/videos/play/wwdc2021/10216)

Learn about the basics of object lifetimes and ARC in Swift. Dive deep into what language features make object lifetimes observable, consequences of relying on observed object lifetimes and some safe techniques to fix them.

**Keywords:** `arc`, `memory`, `object life cycle`, `retain`, `unknown`, `weak`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,579 words)

## Documentation & Resources

- [ARC - The Swift Programming Language](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html) _guide_

## Code Snippets

### ARC Example — [1:49]

```swift
class Traveler {
    var name: String
    var destination: String?
}

func test() {
    let traveler1 = Traveler(name: "Lily")
    let traveler2 = traveler1
    traveler2.destination = "Big Sur"
    print("Done traveling")
}
```

### Reference Cycle Example — [6:37]

```swift
class Traveler {
    var name: String
    var account: Account?
    func printSummary() {
        if let account = account {
            print("\(name) has \(account.points) points")
        }
    }
}

class Account {
    var traveler: Traveler
    var points: Int
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    traveler.printSummary()
}
```

### Weak Reference Example — [9:05]

```swift
class Traveler {
    var name: String
    var account: Account?
    func printSummary() {
        if let account = account {
            print("\(name) has \(account.points) points")
        }
    }
}

class Account {
    weak var traveler: Traveler?
    var points: Int
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    traveler.printSummary()
}
```

### Accessing an object via weak reference — [10:05]

```swift
class Traveler {
    var name: String
    var account: Account?
}

class Account {
    weak var traveler: Traveler?
    var points: Int
    func printSummary() {
        print("\(traveler!.name) has \(points) points")
    }
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    account.printSummary()
}
```

### Accessing an object via optional binding of weak reference — [11:14]

```swift
class Traveler {
    var name: String
    var account: Account?
}

class Account {
    weak var traveler: Traveler?
    var points: Int
    func printSummary() {
         if let traveler = traveler {
            print("\(traveler.name) has \(points) points") 
         }
    }
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    account.printSummary()
}
```

### Safe techniques for handling weak references - withExtendedLifetime() — [11:45]

```swift
func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    withExtendedLifetime(traveler) {
        account.printSummary()
    }
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    account.printSummary()
    withExtendedLifetime(traveler) {}
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    defer {withExtendedLifetime(traveler) {}}
    traveler.account = account
    account.printSummary()
}
```

### Safe techniques for handling weak references - Redesign to access via strong reference — [12:55]

```swift
class Traveler {
    var name: String
    var account: Account?
    func printSummary() {
        if let account = account {
            print("\(name) has \(account.points) points")
        }
    }
}

class Account {
    private weak var traveler: Traveler?
    var points: Int
}

func test() {
    let traveler = Traveler(name: "Lily")
    let account = Account(traveler: traveler, points: 1000)
    traveler.account = account
    traveler.printSummary()
}
```

### Safe techniques for handling weak references - Redesign to avoid weak/unowned reference — [14:20]

```swift
class PersonalInfo {
    var name: String
}

class Traveler {
    var info: PersonalInfo
    var account: Account?
}

class Account {
    var info: PersonalInfo
    var points: Int
}
```

### Deinitializer Example — [15:23]

```swift
class Traveler {
  var name: String
  var destination: String?
  deinit {
    print("\(name) is deinitializing")
  }
}

func test() {
    let traveler1 = Traveler(name: "Lily")
    let traveler2 = traveler1
    traveler2.destination = "Big Sur"
    print("Done traveling")
}
```

### Sequencing deinitializer side-effects with external program effects — [16:10]

```swift
class Traveler {
    var name: String
    var id: UInt
    var destination: String?
    var travelMetrics: TravelMetrics
    // Update destination and record travelMetrics
    func updateDestination(_ destination: String) {
        self.destination = destination
        travelMetrics.destinations.append(self.destination)
    }
    // Publish computed metrics
    deinit {
        travelMetrics.publish()
    }
}

class TravelMetrics {
    let id: UInt
    var destinations = [String]()
    var category: String?
    // Finds the most interested travel category based on recorded destinations
    func computeTravelInterest()
    // Publishes id, destinations.count and travel interest category
    func publish()
}

func test() {
    let traveler = Traveler(name: "Lily", id: 1)
    let metrics = traveler.travelMetrics
    ...
    traveler.updateDestination("Big Sur")
    ...
    traveler.updateDestination("Catalina")
    metrics.computeTravelInterest()
}

verifyGlobalTravelMetrics()
```

### Safe techniques for handing deinitalizer side effects - withExtendedLifetime() — [17:56]

```swift
func test() {
    let traveler = Traveler(name: "Lily", id: 1)
    let metrics = traveler.travelMetrics
    ...
    traveler.updateDestination("Big Sur")
    ...
    traveler.updateDestination("Catalina")
    withExtendedLifetime(traveler) {
        metrics.computeTravelInterest()
    }
}
```

### Safe techniques for handing deinitalizer side effects - Redesign to limit visibility of internal class details — [18:31]

```swift
class Traveler {
    ...
    private var travelMetrics: TravelMetrics
    deinit {
        travelMetrics.computeTravelInterest()
        travelMetrics.publish()
    }
}

func test() {
    let traveler = Traveler(name: "Lily", id: 1)
    ...
    traveler.updateDestination("Big Sur")
    ...
    traveler.updateDestination("Catalina")
}
```

### Safe techniques for handling deinitalizer side effects - Redesign to avoid deinitializer side-effects — [19:08]

```swift
class Traveler {
    ...
    private var travelMetrics: TravelMetrics

    func publishAllMetrics() {
        travelMetrics.computeTravelInterest()
        travelMetrics.publish()
    }

    deinit {
				assert(travelMetrics.published)
    }
}

class TravelMetrics {
    ...
    var published: Bool
    ...
}

func test() {
    let traveler = Traveler(name: "Lily", id: 1)
    defer { traveler.publishAllMetrics() }
    ...
    traveler.updateDestination("Big Sur")
    ...
    traveler.updateDestination("Catalina")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10216) — developer.apple.com. Indexed for agent consumption._