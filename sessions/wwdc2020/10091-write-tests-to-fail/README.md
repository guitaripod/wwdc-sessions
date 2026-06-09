---
id: "wwdc2020-10091"
event: "wwdc2020"
year: 2020
title: "Write tests to fail"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10091"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Write tests to fail

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10091](https://developer.apple.com/videos/play/wwdc2020/10091)

Plan for failure: Design great tests to help you find and diagnose even the toughest bugs. Learn how to improve your automated tests with XCTest to find hidden issues in even the best code. We’ll explain how to prepare your tests for failure to make triaging issues easier, letting you solve interface issues and deliver fixes quickly. To get the most out of this session, you should already be familiar with writing UI tests within the XCTest framework. For more on testing tools, head over to “The suite life of testing”.

**Keywords:** `testing`, `xcode`, `xctest`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,782 words)

## Code Snippets

### Use setUpWithError() — [1:58]

```swift
class RecipesTests: XCTestCase {
    let app = FrutaApp()

    override func setUpWithError() throws {
        continueAfterFailure = false
        app.launchArguments.append("-recipes-tests")
        app.launch()
    }
}
```

### Use launch arguments — [3:09]

```swift
class RecipesTests: XCTestCase {
    let app = FrutaApp()

    override func setUpWithError() throws {
        continueAfterFailure = false
        app.launchArguments.append("-recipes-tests")
        app.launch()
    }
}

@State private var selection: Tab = 
       CommandLine.arguments.contains("-recipes-tests") 
       ? .recipes : .menu
```

### Design tests for a specific goal — [4:12]

```swift
func testIngredientsListAccuracy() throws {
    // Select Berry Blue recipe
    let recipe = try   
        app.smoothieList().selectRecipe
                           (smoothie: .berryBlue)

    // Verify ingredients list
    try recipe.verify(ingredients: 
        SmoothieType.berryBlue.ingredients)
}
```

### Use enums for string values — [4:56]

```swift
public enum SmoothieType : String {
    case berryBlue = "Berry Blue"
    case carrotChops = "Carrot Chops"
    case berryBananas = "That's Berry Bananas!"

    var ingredients : [String] {
        switch self {
        case .berryBlue:
            return ["Orange", "Blueberry", "Avocado"]
        case .carrotChops:
            return ["Orange", "Carrot", "Mango"]
        case .berryBananas:
            return ["Almond Milk", "Banana", "Strawberry"]
        }
    }
}
```

### Factor common code — [5:25]

```swift
let recipe = try app.smoothieList().selectRecipe(smoothie: .berryBlue)

public class FrutaApp : XCUIApplication {
   public func smoothieList() throws -> SmoothieList {
        let element = tables["Smoothie List"]
        if !element.waitForExistence(timeout: 5) {
            throw FrutaError.elementDoesNotExist("Smoothie List table")
        }
        return SmoothieList(app: self, element: element)
    }
}  

public class SmoothieList : FrutaUIElement {
    public func selectRecipe(smoothie: SmoothieType) throws -> Recipe {
       element.buttons[smoothie.rawValue].tap()
       return try app.recipe()
   }
}
```

### Model UI hierarchy in testing code — [5:49]

```swift
public class FrutaApp : XCUIApplication {
   public func smoothieList() throws -> SmoothieList { ￼ }
} 

public class SmoothieList : FrutaUIElement {
    public func selectRecipe(smoothie: SmoothieType) throws -> Recipe { ￼ }
}

open class FrutaUIElement {
    let app: FrutaApp
    let element: XCUIElement
    init(app: FrutaApp, element: XCUIElement) {
        self.app = app
        self.element = element
    }
}
```

### Use assertion messages — [8:17]

```swift
XCTAssertEqual(count, expectedCount, "\(SmoothieType.berryBlue.rawValue) smoothie is expected to have \(expectedCount) ingredients: \(expectedIngredients), however, there were 
\(count) found.")
```

### Asynchronous events — [9:21]

```swift
public func selectRecipe(smoothie: SmoothieType) throws -> Recipe {
    element.buttons[smoothie.rawValue].tap()
    return try app.recipe()
}

public func recipe() throws -> Recipe {
    let element = scrollViews["Ingredients View"]
    if !element.waitForExistence(timeout: 5) {
        throw FrutaError.elementDoesNotExist(
                        "Ingredients View scroll view")
    }
    return Recipe(app: self, element: element)
}
```

### Unwrapping optionals — [10:19]

```swift
func countFavorites(favorites: [String]?) -> Int{
     let favs = favorites!
     return favs.count
}
```

### Unwrapping optionals continued — [10:56]

```swift
if let favs = favorites { ￼ }
guard let favs = favorites else { /* throw an error */ }
let favs = favorites ?? []
let favs = try XCTUnwrap(favorites, "favorites is nil, so there is nothing to count”)
```

### Throw errors from shared code — [12:19]

```swift
public func verify(ingredients: [String]) throws {
    try XCTContext.runActivity(named: "Verifying \(ingredients) exists in the Recipe screen.")
    { verifyingRecipe in
        for ingredient in ingredients {
            if !element.switches[ingredient].waitForExistence(timeout: 5) {
                throw RecipeError.ingredientDoesNotExist(ingredient)
            }
        }
    }
}

public enum RecipeError : Error, CustomStringConvertible {
    case ingredientDoesNotExist(String)

    public var description : String {
        switch self {
        case .ingredientDoesNotExist(let ingredient):
            return "\(ingredient) does not exist in the Ingredients View.)"
        }
    }
}
```

### Use XCTContext.runActivity() — [13:41]

```swift
public func verify(ingredients: [String]) throws {
    try XCTContext.runActivity(named: "Verifying \(ingredients) exists in the Recipe screen.")
    { verifyingRecipe in
        for ingredient in ingredients {
            if !element.switches[ingredient].waitForExistence(timeout: 5) {
                throw RecipeError.ingredientDoesNotExist(ingredient)
            }
        }
    }
```

### Add attachments to the result bundle — [14:02]

```swift
public func verify(ingredients: [String]) throws {
    try XCTContext.runActivity(named: "Verifying \(ingredients) exists in the Recipe screen.")
    { verifyingRecipe in
        for ingredient in ingredients {
            if !element.switches[ingredient].waitForExistence(timeout: 5) {
                let attachment = XCTAttachment(string: element.debugDescription)
                verifyingRecipe.add(attachment)
                 throw RecipeError.ingredientDoesNotExist(ingredient)
            }
        }
    }
```

### Use XCTSkip — [14:50]

```swift
let debuggingTests = false

func testSelectSmoothie() throws {
    try XCTSkipUnless(debuggingTests == true, "This test is not yet implemented.")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10091/2/B1C6A6C1-C50B-41C3-826B-AE16864B2245/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10091) — developer.apple.com. Indexed for agent consumption._
