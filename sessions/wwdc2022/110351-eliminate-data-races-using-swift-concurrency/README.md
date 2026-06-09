---
id: "wwdc2022-110351"
event: "wwdc2022"
year: 2022
title: "Eliminate data races using Swift Concurrency"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110351"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Eliminate data races using Swift Concurrency

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110351](https://developer.apple.com/videos/play/wwdc2022/110351)

Join us as we explore one of the core concepts in Swift concurrency: isolation of tasks and actors. We'll take you through Swift’s approach to eliminating data races and its effect on app architecture. We'll also discuss the importance of atomicity in your code, share the nuances of Sendable checking to maintain isolation, and revisit assumptions about ordering work in a concurrent system.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,380 words)

## Documentation & Resources

- [Concurrency](https://developer.apple.com/documentation/Swift/concurrency) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/concurrency.json
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Tasks — [1:18]

```swift
Task.detached {
  let fish = await catchFish()
  let dinner = await cook(fish)
  await eat(dinner)
}
```

### What is the pineapple? — [2:31]

```swift
enum Ripeness {
  case hard
  case perfect
  case mushy(daysPast: Int)
}

struct Pineapple {
  var weight: Double
  var ripeness: Ripeness

  mutating func ripen() async { … }
  mutating func slice() -> Int { … }
}
```

### Adding chickens — [3:15]

```swift
final class Chicken {
  let name: String
  var currentHunger: HungerLevel

  func feed() { … }
  func play() { … }
  func produce() -> Egg { … }
}
```

### Sendable protocol — [4:35]

```swift
protocol Sendable { }
```

### Use conformance to specify which types are Sendable — [4:44]

```swift
struct Pineapple: Sendable { … } //conforms to Sendable because its a value type
class Chicken: Sendable { } // cannot conform to Sendable because its an unsynchronized reference type.
```

### Check Sendable across task boundaries — [4:57]

```swift
// will get an error because Chicken is not Sendable
let petAdoption = Task {
  let chickens = await hatchNewFlock()
  return chickens.randomElement()!
}
let pet = await petAdoption.value
```

### The Sendable constraint is from the Task struct — [5:26]

```swift
struct Task<Success: Sendable, Failure: Error> {
  var value: Success {
    get async throws { … }
  }
}
```

### Sendable checking for enums and structs — [6:23]

```swift
enum Ripeness: Sendable {
  case hard
  case perfect
  case mushy(daysPast: Int)
}

struct Pineapple: Sendable {
  var weight: Double
  var ripeness: Ripeness
}
```

### Sendable checking for enums and structs with collections — [6:52]

```swift
//contains an array of Sendable types, therefore is Sendable
struct Crate: Sendable {
  var pineapples: [Pineapple]
}
```

### Sendable checking for enums and structs with non-Sendable collections — [7:17]

```swift
//stored property 'flock' of 'Sendable'-conforming struct 'Coop' has non-sendable type '[Chicken]'
struct Coop: Sendable {
  var flock: [Chicken]
}
```

### Sendable checking in classes — [7:36]

```swift
//Can be Sendable if a final class has immutable storage
final class Chicken: Sendable {
  let name: String
  var currentHunger: HungerLevel //'currentHunger' is mutable, therefore Chicken cannot be Sendable
}
```

### Reference types that do their own internal synchronization — [7:58]

```swift
//@unchecked can be used, but be careful!
class ConcurrentCache<Key: Hashable & Sendable, Value: Sendable>: @unchecked Sendable {
  var lock: NSLock
  var storage: [Key: Value]
}
```

### Sendable checking during task creation — [8:21]

```swift
let lily = Chicken(name: "Lily")
Task.detached {@Sendable in
	lily.feed()
}
```

### Sendable function types — [9:08]

```swift
struct Task<Success: Sendable, Failure: Error> {
  static func detached(
    priority: TaskPriority? = nil,
    operation: @Sendable @escaping () async throws -> Success
  ) -> Task<Success, Failure>
}
```

### Actors — [10:28]

```swift
actor Island {
  var flock: [Chicken]
  var food: [Pineapple]

  func advanceTime()
}
```

### Only one boat can visit an island at a time — [11:03]

```swift
func nextRound(islands: [Island]) async {
  for island in islands {
    await island.advanceTime()
  }
}
```

### Non-Sendable data cannot be shared between a task and actor — [11:34]

```swift
//Both examples cannot be shared
await myIsland.addToFlock(myChicken)
myChicken = await myIsland.adoptPet()
```

### What code is actor-isolated? — [12:43]

```swift
actor Island {
  var flock: [Chicken]
  var food: [Pineapple]

  func advanceTime() {
    let totalSlices = food.indices.reduce(0) { (total, nextIndex) in
      total + food[nextIndex].slice()
    }

    Task {
      flock.map(Chicken.produce)
    }

    Task.detached {
      let ripePineapples = await food.filter { $0.ripeness == .perfect }
      print("There are \(ripePineapples.count) ripe pineapples on the island")
    }
  }
}
```

### Nonisolated code — [14:03]

```swift
extension Island {
  nonisolated func meetTheFlock() async {
    let flockNames = await flock.map { $0.name }
    print("Meet our fabulous flock: \(flockNames)")
  }
}
```

### Non-isolated synchronous code — [14:48]

```swift
func greet(_ friend: Chicken) { }

extension Island {
  func greetOne() {
    if let friend = flock.randomElement() { 
      greet(friend)
    }
  }
}
```

### Non-isolated asynchronous code — [15:15]

```swift
func greet(_ friend: Chicken) { }

func greetAny(flock: [Chicken]) async {
  if let friend = flock.randomElement() { 
    greet(friend)
  }
}
```

### Isolating functions to the main actor — [17:01]

```swift
@MainActor func updateView() { … }

Task { @MainActor in
	// …
  view.selectedChicken = lily
}

nonisolated func computeAndUpdate() async {
  computeNewValues()
  await updateView()
}
```

### @MainActor types — [17:38]

```swift
@MainActor
class ChickenValley: Sendable {
  var flock: [Chicken]
  var food: [Pineapple]

  func advanceTime() {
    for chicken in flock {
      chicken.eat(from: &food)
    }
  }
}
```

### Non-transactional code — [19:58]

```swift
func deposit(pineapples: [Pineapple], onto island: Island) async {
   var food = await island.food
   food += pineapples
   await island.food = food
}
```

### Pirates! — [20:56]

```swift
await island.food.takeAll()
```

### Modify `deposit` function to be synchronous — [21:57]

```swift
extension Island {
   func deposit(pineapples: [Pineapple]) {
      var food = self.food
      food += pineapples
      self.food = food
   }
}
```

### AsyncStreams deliver elements in order — [23:56]

```swift
for await event in eventStream {
  await process(event)
}
```

### Minimal strict concurrency checking — [25:02]

```swift
import FarmAnimals
struct Coop: Sendable {
  var flock: [Chicken]
}
```

### Targeted strict concurrency checking — [25:21]

```swift
@preconcurrency import FarmAnimals

func visit(coop: Coop) async {
  guard let favorite = coop.flock.randomElement() else {
    return
  }

  Task {
    favorite.play()
  }
}
```

### Complete strict concurrency checking — [26:53]

```swift
import FarmAnimals

func doWork(_ body: @Sendable @escaping () -> Void) {
  DispatchQueue.global().async {
    body()
  }
}

func visit(friend: Chicken) {
  doWork {
    friend.play()
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110351/3/2B82DC62-6057-4460-93F4-B99CF7073221/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110351/3/2B82DC62-6057-4460-93F4-B99CF7073221/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110351) — developer.apple.com. Indexed for agent consumption._
