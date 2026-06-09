---
id: "wwdc2024-10195"
event: "wwdc2024"
year: 2024
title: "Go further with Swift Testing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10195"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Go further with Swift Testing

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10195](https://developer.apple.com/videos/play/wwdc2024/10195)

Learn how to write a sweet set of (test) suites using Swift Testing’s baked-in features. Discover how to take the building blocks further and use them to help expand tests to cover more scenarios, organize your tests across different suites, and optimize your tests to run in parallel.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,568 words)

## Documentation & Resources

- [Swift Testing vision document](https://github.com/apple/swift-testing/blob/main/Documentation/Vision.md) _guide_
- [Swift Testing GitHub repository](https://github.com/apple/swift-testing) _guide_
- [Running tests and interpreting results](https://developer.apple.com/documentation/Xcode/running-tests-and-interpreting-results) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/running-tests-and-interpreting-results
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/running-tests-and-interpreting-results.json
- [Adding tests to your Xcode project](https://developer.apple.com/documentation/Xcode/adding-tests-to-your-xcode-project) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/adding-tests-to-your-xcode-project
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/adding-tests-to-your-xcode-project.json
- [Swift Testing](https://developer.apple.com/documentation/Testing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Testing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Testing.json
- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010
- [Improving code assessment by organizing tests into test plans](https://developer.apple.com/documentation/Xcode/organizing-tests-to-improve-feedback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/organizing-tests-to-improve-feedback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/organizing-tests-to-improve-feedback.json

## Code Snippets

### Successful throwing function — [0:01]

```swift
// Expecting errors

import Testing

@Test func brewTeaSuccessfully() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    let cupOfTea = try teaLeaves.brew(forMinutes: 3)
}
```

### Validating a successful throwing function — [0:02]

```swift
import Testing

@Test func brewTeaSuccessfully() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    let cupOfTea = try teaLeaves.brew(forMinutes: 3)
    #expect(cupOfTea.quality == .perfect)
}
```

### Validating an error is thrown with do-catch (not recommended) — [0:03]

```swift
import Testing

@Test func brewTeaError() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 3)

    do {
        try teaLeaves.brew(forMinutes: 100)
    } catch is BrewingError {
        // This is the code path we are expecting
    } catch {
        Issue.record("Unexpected Error")
    }
}
```

### Validating a general error is thrown — [0:04]

```swift
import Testing

@Test func brewTeaError() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    #expect(throws: (any Error).self) {
        try teaLeaves.brew(forMinutes: 200) // We don't want this to fail the test!
    }
}
```

### Validating a type of error — [0:05]

```swift
import Testing

@Test func brewTeaError() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    #expect(throws: BrewingError.self) {
        try teaLeaves.brew(forMinutes: 200) // We don't want this to fail the test!
    }
}
```

### Validating a specific error — [0:06]

```swift
import Testing

@Test func brewTeaError() throws {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    #expect(throws: BrewingError.oversteeped) {
        try teaLeaves.brew(forMinutes: 200) // We don't want this to fail the test!
    }
}
```

### Complicated validations — [0:07]

```swift
import Testing

@Test func brewTea() {
    let teaLeaves = TeaLeaves(name: "EarlGrey", optimalBrewTime: 4)
    #expect {
        try teaLeaves.brew(forMinutes: 3)
    } throws: { error in
        guard let error = error as? BrewingError,
              case let .needsMoreTime(optimalBrewTime) = error else {
            return false
        }
        return optimalBrewTime == 4
    }
}
```

### Throwing expectation — [0:08]

```swift
import Testing

@Test func brewAllGreenTeas() {
  #expect(throws: BrewingError.self) {
    brewMultipleTeas(teaLeaves: ["Sencha", "EarlGrey", "Jasmine"], time: 2)
  }
}
```

### Required expectations — [0:09]

```swift
import Testing

@Test func brewAllGreenTeas() throws {
  try #require(throws: BrewingError.self) {
    brewMultipleTeas(teaLeaves: ["Sencha", "EarlGrey", "Jasmine"], time: 2)
  }
}
```

### Control flow of validating an optional value (not recommended) — [0:10]

```swift
import Testing

struct TeaLeaves {symbols
    let name: String
    let optimalBrewTime: Int

    func brew(forMinutes minutes: Int) throws -> Tea { ... }
}

@Test func brewTea() throws {
    let teaLeaves = TeaLeaves(name: "Sencha", optimalBrewTime: 2)
    let brewedTea = try teaLeaves.brew(forMinutes: 100)
    guard let color = brewedTea.color else {
        Issue.record("Tea color was not available!")
    }
    #expect(color == .green)
}
```

### Failing test with a throwing function — [0:11]

```swift
import Testing

@Test func softServeIceCreamInCone() throws {
    try softServeMachine.makeSoftServe(in: .cone)
}
```

### Disabling a test with a throwing function (not recommended) — [0:12]

```swift
import Testing

@Test(.disabled) func softServeIceCreamInCone() throws {
    try softServeMachine.makeSoftServe(in: .cone)
}
```

### Wrapping a failing test in withKnownIssue — [0:13]

```swift
import Testing

@Test func softServeIceCreamInCone() throws {
    withKnownIssue {
        try softServeMachine.makeSoftServe(in: .cone)
    }
}
```

### Wrap just the failing section in withKnownIssue — [0:14]

```swift
import Testing

@Test func softServeIceCreamInCone() throws {
    let iceCreamBatter = IceCreamBatter(flavor: .chocolate)
    try #require(iceCreamBatter != nil)
    #expect(iceCreamBatter.flavor == .chocolate)

    withKnownIssue {
        try softServeMachine.makeSoftServe(in: .cone)
    }
}
```

### Simple enumerations — [0:15]

```swift
import Testing

enum SoftServe {
    case vanilla, chocolate, pineapple
}
```

### Complex types — [0:16]

```swift
import Testing

struct SoftServe {
    let flavor: Flavor
    let container: Container
    let toppings: [Topping]
}

@Test(arguments: [
    SoftServe(flavor: .vanilla, container: .cone, toppings: [.sprinkles]),
    SoftServe(flavor: .chocolate, container: .cone, toppings: [.sprinkles]),
    SoftServe(flavor: .pineapple, container: .cup, toppings: [.whippedCream])
])
func softServeFlavors(_ softServe: SoftServe) { /*...*/ }
```

### Conforming to CustomTestStringConvertible — [0:17]

```swift
import Testing

struct SoftServe: CustomTestStringConvertible {
    let flavor: Flavor
    let container: Container
    let toppings: [Topping]

    var testDescription: String {
        "\(flavor) in a \(container)"
    }
}

@Test(arguments: [
    SoftServe(flavor: .vanilla, container: .cone, toppings: [.sprinkles]),
    SoftServe(flavor: .chocolate, container: .cone, toppings: [.sprinkles]),
    SoftServe(flavor: .pineapple, container: .cup, toppings: [.whippedCream])
])
func softServeFlavors(_ softServe: SoftServe) { /*...*/ }
```

### An enumeration with a computed property — [0:18]

```swift
extension IceCream {
    enum Flavor {
        case vanilla, chocolate, strawberry, mintChip, rockyRoad, pistachio

        var containsNuts: Bool {
            switch self {
            case .rockyRoad, .pistachio:
                return true
            default:
                return false
            }
        }
    }
}
```

### A test function for a specific case of an enumeration — [0:19]

```swift
import Testing

@Test func doesVanillaContainNuts() throws {
    try #require(!IceCream.Flavor.vanilla.containsNuts)
}
```

### Separate test functions for all cases of an enumeration — [0:20]

```swift
import Testing

@Test func doesVanillaContainNuts() throws {
    try #require(!IceCream.Flavor.vanilla.containsNuts)
}

@Test func doesChocolateContainNuts() throws {
    try #require(!IceCream.Flavor.chocolate.containsNuts)
}

@Test func doesStrawberryContainNuts() throws {
    try #require(!IceCream.Flavor.strawberry.containsNuts)
}

@Test func doesMintChipContainNuts() throws {
    try #require(!IceCream.Flavor.mintChip.containsNuts)
}

@Test func doesRockyRoadContainNuts() throws {
    try #require(!IceCream.Flavor.rockyRoad.containsNuts)
}
```

### Parameterizing a test with a for loop (not recommended) — [0:21]

```swift
import Testing

extension IceCream {
    enum Flavor {
        case vanilla, chocolate, strawberry, mintChip, rockyRoad, pistachio
    }
}

@Test
func doesNotContainNuts() throws {
    for flavor in [IceCream.Flavor.vanilla, .chocolate, .strawberry, .mintChip] {
        try #require(!flavor.containsNuts)
    }
}
```

### Swift testing parameterized tests — [0:22]

```swift
import Testing

extension IceCream {
    enum Flavor {
        case vanilla, chocolate, strawberry, mintChip, rockyRoad, pistachio
    }
}

@Test(arguments: [IceCream.Flavor.vanilla, .chocolate, .strawberry, .mintChip])
func doesNotContainNuts(flavor: IceCream.Flavor) throws {
    try #require(!flavor.containsNuts)
}
```

### 100% test coverage — [0:23]

```swift
import Testing

extension IceCream {
    enum Flavor {
        case vanilla, chocolate, strawberry, mintChip, rockyRoad, pistachio
    }
}

@Test(arguments: [IceCream.Flavor.vanilla, .chocolate, .strawberry, .mintChip])
func doesNotContainNuts(flavor: IceCream.Flavor) throws {
    try #require(!flavor.containsNuts)
}

@Test(arguments: [IceCream.Flavor.rockyRoad, .pistachio])
func containNuts(flavor: IceCream.Flavor) {
   #expect(flavor.containsNuts)
}
```

### A parameterized test with one argument — [0:24]

```swift
import Testing

enum Ingredient: CaseIterable {
    case rice, potato, lettuce, egg
}

@Test(arguments: Ingredient.allCases)
func cook(_ ingredient: Ingredient) async throws {
    #expect(ingredient.isFresh)
    let result = try cook(ingredient)
    try #require(result.isDelicious)
}
```

### Adding a second argument to a parameterized test — [0:26]

```swift
import Testing

enum Ingredient: CaseIterable {
    case rice, potato, lettuce, egg
}

enum Dish: CaseIterable {
    case onigiri, fries, salad, omelette
}

@Test(arguments: Ingredient.allCases, Dish.allCases)
func cook(_ ingredient: Ingredient, into dish: Dish) async throws {
    #expect(ingredient.isFresh)
    let result = try cook(ingredient)
    try #require(result.isDelicious)
    try #require(result == dish)
}
```

### Using zip() on arguments — [0:28]

```swift
import Testing

enum Ingredient: CaseIterable {
    case rice, potato, lettuce, egg
}

enum Dish: CaseIterable {
    case onigiri, fries, salad, omelette
}

@Test(arguments: zip(Ingredient.allCases, Dish.allCases))
func cook(_ ingredient: Ingredient, into dish: Dish) async throws {
    #expect(ingredient.isFresh)
    let result = try cook(ingredient)
    try #require(result.isDelicious)
    try #require(result == dish)
}
```

### Suites — [0:29]

```swift
@Suite("Various desserts") 
struct DessertTests {
    @Test func applePieCrustLayers() { /* ... */ }
    @Test func lavaCakeBakingTime() { /* ... */ }
    @Test func eggWaffleFlavors() { /* ... */ }
    @Test func cheesecakeBakingStrategy() { /* ... */ }
    @Test func mangoSagoToppings() { /* ... */ }
    @Test func bananaSplitMinimumScoop() { /* ... */ }
}
```

### Nested suites — [0:30]

```swift
import Testing

@Suite("Various desserts")
struct DessertTests {
    @Suite struct WarmDesserts {
        @Test func applePieCrustLayers() { /* ... */ }
        @Test func lavaCakeBakingTime() { /* ... */ }
        @Test func eggWaffleFlavors() { /* ... */ }
    }

    @Suite struct ColdDesserts {
        @Test func cheesecakeBakingStrategy() { /* ... */ }
        @Test func mangoSagoToppings() { /* ... */ }
        @Test func bananaSplitMinimumScoop() { /* ... */ }
    }
}
```

### Separate suites — [0:31]

```swift
@Suite struct DrinkTests {
    @Test func espressoExtractionTime() { /* ... */ }
    @Test func greenTeaBrewTime() { /* ... */ }
    @Test func mochaIngredientProportion() { /* ... */ }
}

@Suite struct DessertTests {
    @Test func espressoBrownieTexture() { /* ... */ }
    @Test func bungeoppangFilling() { /* ... */ }
    @Test func fruitMochiFlavors() { /* ... */ }
}
```

### Separate suites — [0:32]

```swift
@Suite struct DrinkTests {
    @Test func espressoExtractionTime() { /* ... */ }
    @Test func greenTeaBrewTime() { /* ... */ }
    @Test func mochaIngredientProportion() { /* ... */ }
}

@Suite struct DessertTests {
    @Test func espressoBrownieTexture() { /* ... */ }
    @Test func bungeoppangFilling() { /* ... */ }
    @Test func fruitMochiFlavors() { /* ... */ }
}
```

### Using a tag — [0:35]

```swift
import Testing 

extension Tag {
    @Tag static var caffeinated: Self
}

@Suite(.tags(.caffeinated)) struct DrinkTests {
    @Test func espressoExtractionTime() { /* ... */ }
    @Test func greenTeaBrewTime() { /* ... */ }
    @Test func mochaIngredientProportion() { /* ... */ }
}

@Suite struct DessertTests {
    @Test(.tags(.caffeinated)) func espressoBrownieTexture() { /* ... */ }
    @Test func bungeoppangFilling() { /* ... */ }
    @Test func fruitMochiFlavors() { /* ... */ }
}
```

### Declare and use a second tag — [0:36]

```swift
import Testing 

extension Tag {
    @Tag static var caffeinated: Self
    @Tag static var chocolatey: Self
}

@Suite(.tags(.caffeinated)) struct DrinkTests {
    @Test func espressoExtractionTime() { /* ... */ }
    @Test func greenTeaBrewTime() { /* ... */ }
    @Test(.tags(.chocolatey)) func mochaIngredientProportion() { /* ... */ }
}

@Suite struct DessertTests {
    @Test(.tags(.caffeinated, .chocolatey)) func espressoBrownieTexture() { /* ... */ }
    @Test func bungeoppangFilling() { /* ... */ }
    @Test func fruitMochiFlavors() { /* ... */ }
}
```

### Two tests with an unintended data dependency (not recommended) — [0:37]

```swift
import Testing

// ❌ This code is not concurrency-safe.

var cupcake: Cupcake? = nil

@Test func bakeCupcake() async {
    cupcake = await Cupcake.bake(toppedWith: .frosting)
    // ...
}

@Test func eatCupcake() async {
    await eat(cupcake!)
    // ...
}
```

### Serialized trait — [0:38]

```swift
import Testing

@Suite("Cupcake tests", .serialized)
struct CupcakeTests {
    var cupcake: Cupcake?

    @Test func mixingIngredients() { /* ... */ }
    @Test func baking() { /* ... */ }
    @Test func decorating() { /* ... */ }
    @Test func eating() { /* ... */ }
}
```

### Serialized trait with nested suites — [0:39]

```swift
import Testing

@Suite("Cupcake tests", .serialized)
struct CupcakeTests {
    var cupcake: Cupcake?

    @Suite("Mini birthday cupcake tests")
    struct MiniBirthdayCupcakeTests {
        // ...
    }

    @Test(arguments: [...]) func mixing(ingredient: Food) { /* ... */ }
    @Test func baking() { /* ... */ }
    @Test func decorating() { /* ... */ }
    @Test func eating() { /* ... */ }
}
```

### Using async/await in a test — [0:40]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    try await eat(cookies, with: .milk)
}
```

### Using a function with a completion handler in a test (not recommended) — [0:41]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    // ❌ This code will run after the test function returns.
    eat(cookies, with: .milk) { result, error in
        #expect(result != nil)
    }
}
```

### Replacing a completion handler with an asynchronous function call — [0:42]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    try await eat(cookies, with: .milk)
}
```

### Using withCheckedThrowingContinuation — [0:43]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    try await withCheckedThrowingContinuation { continuation in
        eat(cookies, with: .milk) { result, error in
            if let result {
                continuation.resume(returning: result)
            } else {
                continuation.resume(throwing: error)
            }
        }
    }
}
```

### Callback that invokes more than once (not recommended) — [0:44]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    // ❌ This code is not concurrency-safe.
    var cookiesEaten = 0
    try await eat(cookies, with: .milk) { cookie, crumbs in
        #expect(!crumbs.in(.milk))
        cookiesEaten += 1
    }
    #expect(cookiesEaten == 10)
}
```

### Confirmations on callbacks that invoke more than once — [0:45]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    try await confirmation("Ate cookies", expectedCount: 10) { ateCookie in
        try await eat(cookies, with: .milk) { cookie, crumbs in
            #expect(!crumbs.in(.milk))
            ateCookie()
        }
    }
}
```

### Confirmation that occurs 0 times — [0:46]

```swift
import Testing

@Test func bakeCookies() async throws {
    let cookies = await Cookie.bake(count: 10)
    try await confirmation("Ate cookies", expectedCount: 0) { ateCookie in
        try await eat(cookies, with: .milk) { cookie, crumbs in
            #expect(!crumbs.in(.milk))
            ateCookie()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10195/4/7FBA1EC9-FB05-46DA-852F-C090FB5A53E6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10195/4/7FBA1EC9-FB05-46DA-852F-C090FB5A53E6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10195) — developer.apple.com. Indexed for agent consumption._