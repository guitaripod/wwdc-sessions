---
id: "wwdc2023-10170"
event: "wwdc2023"
year: 2023
title: "Beyond the basics of structured concurrency"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10170"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Beyond the basics of structured concurrency

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10170](https://developer.apple.com/videos/play/wwdc2023/10170)

It’s all about the task tree: Find out how structured concurrency can help your apps manage automatic task cancellation, task priority propagation, and useful task-local value patterns. Learn how to manage resources in your app with useful patterns and the latest task group APIs. We’ll show you how you can leverage the power of the task tree and task-local values to gain insight into distributed systems.

Before watching, review the basics of Swift Concurrency and structured concurrency by checking out “Swift concurrency: Behind the scenes” and “Explore structured concurrency in Swift” from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,694 words)

## Documentation & Resources

- [Swift Distributed Tracing - Repository](https://github.com/apple/swift-distributed-tracing) _guide_

## Code Snippets

### Unstructured concurrency — [2:27]

```swift
func makeSoup(order: Order) async throws -> Soup {
    let boilingPot = Task { try await stove.boilBroth() }
    let choppedIngredients = Task { try await chopIngredients(order.ingredients) }
    let meat = Task { await marinate(meat: .chicken) }
    let soup = await Soup(meat: meat.value, ingredients: choppedIngredients.value)
    return await stove.cook(pot: boilingPot.value, soup: soup, duration: .minutes(10))
}
```

### Structured concurrency — [2:42]

```swift
func makeSoup(order: Order) async throws -> Soup {
    async let pot = stove.boilBroth()
    async let choppedIngredients = chopIngredients(order.ingredients)
    async let meat = marinate(meat: .chicken)
    let soup = try await Soup(meat: meat, ingredients: choppedIngredients)
    return try await stove.cook(pot: pot, soup: soup, duration: .minutes(10))
}
```

### Structured concurrency — [3:00]

```swift
func chopIngredients(_ ingredients: [any Ingredient]) async -> [any ChoppedIngredient] {
    return await withTaskGroup(of: (ChoppedIngredient?).self,
                               returning: [any ChoppedIngredient].self) { group in
         // Concurrently chop ingredients
         for ingredient in ingredients {
             group.addTask { await chop(ingredient) }
         }
         // Collect chopped vegetables
         var choppedIngredients: [any ChoppedIngredient] = []
         for await choppedIngredient in group {
             if choppedIngredient != nil {
                choppedIngredients.append(choppedIngredient!)
             }
         }
         return choppedIngredients
    }
}
```

### Task cancellation — [4:32]

```swift
func makeSoup(order: Order) async throws -> Soup {
    async let pot = stove.boilBroth()

    guard !Task.isCancelled else {
        throw SoupCancellationError()
    }

    async let choppedIngredients = chopIngredients(order.ingredients)
    async let meat = marinate(meat: .chicken)
    let soup = try await Soup(meat: meat, ingredients: choppedIngredients)
    return try await stove.cook(pot: pot, soup: soup, duration: .minutes(10))
}
```

### Task cancellation — [4:58]

```swift
func chopIngredients(_ ingredients: [any Ingredient]) async throws -> [any ChoppedIngredient] {
    return try await withThrowingTaskGroup(of: (ChoppedIngredient?).self,
                                   returning: [any ChoppedIngredient].self) { group in
        try Task.checkCancellation()

        // Concurrently chop ingredients
        for ingredient in ingredients {
            group.addTask { await chop(ingredient) }
        }

        // Collect chopped vegetables
        var choppedIngredients: [any ChoppedIngredient] = []
        for try await choppedIngredient in group {
            if let choppedIngredient {
                choppedIngredients.append(choppedIngredient)
            }
        }
        return choppedIngredients
    }
}
```

### Cancellation and async sequences — [5:47]

```swift
actor Cook {
    func handleShift<Orders>(orders: Orders) async throws
       where Orders: AsyncSequence,
             Orders.Element == Order {

        for try await order in orders {
            let soup = try await makeSoup(order)
            // ...
        }
    }
}
```

### Cancellation and async sequences — [6:41]

```swift
public func next() async -> Order? {
    return await withTaskCancellationHandler {
        let result = await kitchen.generateOrder()
        guard state.isRunning else {
            return nil
        }
        return result
    } onCancel: {
        state.cancel()
    }
}
```

### AsyncSequence state machine — [7:40]

```swift
private final class OrderState: Sendable {
    let protectedIsRunning = ManagedAtomic<Bool>(true)
    var isRunning: Bool {
        get { protectedIsRunning.load(ordering: .acquiring) }
        set { protectedIsRunning.store(newValue, ordering: .relaxed) }
    }
    func cancel() { isRunning = false }
}
```

### Limiting concurrency with TaskGroups — [10:55]

```swift
func chopIngredients(_ ingredients: [any Ingredient]) async -> [any ChoppedIngredient] {
    return await withTaskGroup(of: (ChoppedIngredient?).self,
                               returning: [any ChoppedIngredient].self) { group in
        // Concurrently chop ingredients
        for ingredient in ingredients {
            group.addTask { await chop(ingredient) }
        }

        // Collect chopped vegetables
        var choppedIngredients: [any ChoppedIngredient] = []
        for await choppedIngredient in group {
            if let choppedIngredient {
                choppedIngredients.append(choppedIngredient)
            }
        }
        return choppedIngredients
    }
}
```

### Limiting concurrency with TaskGroups — [11:01]

```swift
func chopIngredients(_ ingredients: [any Ingredient]) async -> [any ChoppedIngredient] {
    return await withTaskGroup(of: (ChoppedIngredient?).self,
                               returning: [any ChoppedIngredient].self) { group in
        // Concurrently chop ingredients
        let maxChopTasks = min(3, ingredients.count)
        for ingredientIndex in 0..<maxChopTasks {
            group.addTask { await chop(ingredients[ingredientIndex]) }
        }

        // Collect chopped vegetables
        var choppedIngredients: [any ChoppedIngredient] = []
        for await choppedIngredient in group {
            if let choppedIngredient {
                choppedIngredients.append(choppedIngredient)
            }
        }
        return choppedIngredients
    }
}
```

### Limiting concurrency with TaskGroups — [11:17]

```swift
func chopIngredients(_ ingredients: [any Ingredient]) async -> [any ChoppedIngredient] {
    return await withTaskGroup(of: (ChoppedIngredient?).self,
                               returning: [any ChoppedIngredient].self) { group in
        // Concurrently chop ingredients
        let maxChopTasks = min(3, ingredients.count)
        for ingredientIndex in 0..<maxChopTasks {
            group.addTask { await chop(ingredients[ingredientIndex]) }
        }

        // Collect chopped vegetables
        var choppedIngredients: [any ChoppedIngredient] = []
        var nextIngredientIndex = maxChopTasks
        for await choppedIngredient in group {
            if nextIngredientIndex < ingredients.count {
                group.addTask { await chop(ingredients[nextIngredientIndex]) }
                nextIngredientIndex += 1
            }
            if let choppedIngredient {
                choppedIngredients.append(choppedIngredient)
            }
        }
        return choppedIngredients
    }
}
```

### Limiting concurrency with TaskGroups — [11:26]

```swift
withTaskGroup(of: Something.self) { group in
    for _ in 0..<maxConcurrentTasks {
        group.addTask { }
    }
    while let <partial result> = await group.next() {
        if !shouldStop { 
            group.addTask { }
        }
    }
}
```

### Kitchen Service — [11:56]

```swift
func run() async throws {
    try await withThrowingTaskGroup(of: Void.self) { group in
        for cook in staff.keys {
            group.addTask { try await cook.handleShift() }
        }

        group.addTask {
            // keep the restaurant going until closing time
            try await Task.sleep(for: shiftDuration)
        }

        try await group.next()
        // cancel all ongoing shifts
        group.cancelAll()
    }
}
```

### Introducing DiscardingTaskGroups — [12:41]

```swift
func run() async throws {
    try await withThrowingDiscardingTaskGroup { group in
        for cook in staff.keys {
            group.addTask { try await cook.handleShift() }
        }

        group.addTask { // keep the restaurant going until closing time
            try await Task.sleep(for: shiftDuration)
            throw TimeToCloseError()
        }
    }
}
```

### TaskLocal values — [14:10]

```swift
actor Kitchen {
    @TaskLocal static var orderID: Int?
    @TaskLocal static var cook: String?
    func logStatus() {
        print("Current cook: \(Kitchen.cook ?? "none")")
    }
}

let kitchen = Kitchen()
await kitchen.logStatus()
await Kitchen.$cook.withValue("Sakura") {
    await kitchen.logStatus()
}
await kitchen.logStatus()
```

### Logging — [16:17]

```swift
func makeSoup(order: Order) async throws -> Soup {
     log.debug("Preparing dinner", [
       "cook": "\(self.name)",
       "order-id": "\(order.id)",
       "vegetable": "\(vegetable)",
     ])
     // ... 
}

 func chopVegetables(order: Order) async throws -> [Vegetable] {
     log.debug("Chopping ingredients", [
       "cook": "\(self.name)",
       "order-id": "\(order.id)",
       "vegetable": "\(vegetable)",
     ])

     async let choppedCarrot = try chop(.carrot)
     async let choppedPotato = try chop(.potato)
     return try await [choppedCarrot, choppedPotato]
}

func chop(_ vegetable: Vegetable, order: Order) async throws -> Vegetable {
    log.debug("Chopping vegetable", [
      "cook": "\(self.name)",
      "order-id": "\(order)",
      "vegetable": "\(vegetable)",
    ])
    // ...
}
```

### MetadataProvider in action — [17:33]

```swift
let orderMetadataProvider = Logger.MetadataProvider {
    var metadata: Logger.Metadata = [:]
    if let orderID = Kitchen.orderID {
        metadata["orderID"] = "\(orderID)"
    }
    return metadata
}
```

### MetadataProvider in action — [17:50]

```swift
let orderMetadataProvider = Logger.MetadataProvider {
    var metadata: Logger.Metadata = [:]
    if let orderID = Kitchen.orderID {
        metadata["orderID"] = "\(orderID)"
    }
    return metadata
}

let chefMetadataProvider = Logger.MetadataProvider {
    var metadata: Logger.Metadata = [:]
    if let chef = Kitchen.chef {
        metadata["chef"] = "\(chef)"
    }
    return metadata
}

let metadataProvider = Logger.MetadataProvider.multiplex([orderMetadataProvider,
                                                          chefMetadataProvider])

LoggingSystem.bootstrap(StreamLogHandler.standardOutput, metadataProvider: metadataProvider)

let logger = Logger(label: "KitchenService")
```

### Logging with metadata providers — [18:13]

```swift
func makeSoup(order: Order) async throws -> Soup {
    logger.info("Preparing soup order")
    async let pot = stove.boilBroth()
    async let choppedIngredients = chopIngredients(order.ingredients)
    async let meat = marinate(meat: .chicken)
    let soup = try await Soup(meat: meat, ingredients: choppedIngredients)
    return try await stove.cook(pot: pot, soup: soup, duration: .minutes(10))
}
```

### Profile server-side execution — [20:30]

```swift
func makeSoup(order: Order) async throws -> Soup {
    try await withSpan("makeSoup(\(order.id)") { span in
        async let pot = stove.boilWater()
        async let choppedIngredients = chopIngredients(order.ingredients)
        async let meat = marinate(meat: .chicken)
        let soup = try await Soup(meat: meat, ingredients: choppedIngredients)
        return try await stove.cook(pot: pot, soup: soup, duration: .minutes(10))
    }
}
```

### Profiling server-side execution — [21:36]

```swift
func makeSoup(order: Order) async throws -> Soup {
    try await withSpan(#function) { span in
        span.attributes["kitchen.order.id"] = order.id
        async let pot = stove.boilWater()
        async let choppedIngredients = chopIngredients(order.ingredients)
        async let meat = marinate(meat: .chicken)
        let soup = try await Soup(meat: meat, ingredients: choppedIngredients)
        return try await stove.cook(pot: pot, soup: soup, duration: .minutes(10))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10170/5/4608ED1F-4D83-4444-83A0-DF3EACCE4369/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10170/5/4608ED1F-4D83-4444-83A0-DF3EACCE4369/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10170) — developer.apple.com. Indexed for agent consumption._