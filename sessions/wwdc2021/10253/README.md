---
id: "wwdc2021-10253"
event: "wwdc2021"
year: 2021
title: "Write a DSL in Swift using result builders"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10253"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Write a DSL in Swift using result builders

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10253](https://developer.apple.com/videos/play/wwdc2021/10253)

Some problems are easier to solve by creating a customized programming language, or “domain-specific language.” While creating a DSL traditionally requires writing your own compiler, you can instead use result builders with Swift 5.4 to make your code both easier to read and maintain. We’ll take you through best practices for designing a custom language for Swift: Learn about result builders and trailing closure arguments, explore modifier-style methods and why they work well, and discover how you can extend Swift’s normal language rules to turn Swift into a DSL.

To get the most out of this session, it’s helpful (though not necessary) to have some experience writing SwiftUI views. You won’t need to know anything about parser or compiler implementation.

**Keywords:** `compiler`, `domain specific language`, `dsl`, `modifiers`, `property wrappers`, `result builders`, `trailing closure`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(7,726 words)

## Documentation & Resources

- [Result Builders - The Swift Programming Language](https://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID630) _guide_
- [Attributes - The Swift Programming Language](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html) _guide_
- [Fruta: Building a feature-rich app with SwiftUI](https://developer.apple.com/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui.json

## Code Snippets

### FavoriteSmoothies view — [3:15]

```swift
struct FavoriteSmoothies: View {
    @EnvironmentObject
    private var model: FrutaModel

    var body: some View {
        SmoothieList(smoothies: model.favoriteSmoothies)
            .overlay(
                Group {
                    if model.favoriteSmoothies.isEmpty {
                        Text("Add some smoothies!")
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity,
                                   maxHeight: .infinity) 
                    }
                }
            )
            .navigationTitle("Favorites")
    }
}
```

### FavoriteSmoothies view (hypothetical alternative) — [3:38]

```swift
// Hypothetical code--not actually supported by SwiftUI

struct FavoriteSmoothies: View {
    @EnvironmentObject
    private var model: FrutaModel

    var body: some View {
        var list = SmoothieList(smoothies: model.favoriteSmoothies)

        let overlay: View
        if model.favoriteSmoothies.isEmpty {
            var text = Text("Add some smoothies!")
            text.foregroundColor = .secondary

            var frame = Frame(subview: text)
            frame.maxWidth = .infinity
            frame.maxHeight = .infinity
            overlay = frame
        } else {
            overlay = EmptyView()
        }

        list.addOverlay(overlay)
        list.navigationTitle = "Favorites"

        return list
    }
}
```

### FavoriteSmoothies view — [3:59]

```swift
struct FavoriteSmoothies: View {
    @EnvironmentObject
    private var model: FrutaModel

    var body: some View {
        SmoothieList(smoothies: model.favoriteSmoothies)
            .overlay(
                Group {
                    if model.favoriteSmoothies.isEmpty {
                        Text("Add some smoothies!")
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity,
                                   maxHeight: .infinity) 
                    }
                }
            )
            .navigationTitle("Favorites")
    }
}
```

### FavoriteSmoothies view — [6:17]

```swift
struct FavoriteSmoothies: View {
    @EnvironmentObject
    private var model: FrutaModel

    var body: some View {
        SmoothieList(smoothies: model.favoriteSmoothies)
            .overlay(
                Group {
                    if model.favoriteSmoothies.isEmpty {
                        Text("Add some smoothies!")
                            .foregroundColor(.secondary)
                            .frame(maxWidth: .infinity,
                                   maxHeight: .infinity) 
                    }
                }
            )
            .navigationTitle("Favorites")
    }
}
```

### Simple result builder example — [9:26]

```swift
VStack {
    Text("Title").font(.title)
    Text("Contents")
}
```

### Simple result builder example + struct VStack — [9:36]

```swift
VStack {
    Text("Title").font(.title)
    Text("Contents")
}


struct VStack<Content: View>: View {
    …
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
}
```

### Simple result builder example + struct VStack + trailing closure applied — [9:40]

```swift
VStack /* .init(content: */ {
    Text("Title").font(.title)
    Text("Contents")
} /* ) */


struct VStack<Content: View>: View {
    …
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
}
```

### Simple result builder example + struct VStack + trailing closure applied + enum ViewBuilder — [9:50]

```swift
VStack /* .init(content: */ {
    Text("Title").font(.title)
    Text("Contents")
    /* return // TODO: build results using ‘ViewBuilder’ */
} /* ) */

struct VStack<Content: View>: View {
    …
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
}

@resultBuilder enum ViewBuilder {
    static func buildBlock(_: View...) -> some View { … }
}
```

### Simple result builder example + struct VStack + trailing closure applied + enum ViewBuilder + result builder applied — [10:15]

```swift
VStack /* .init(content: */ {
    /* let v0 = */ Text("Title").font(.title)
    /* let v1 = */ Text("Contents")
    /* return ViewBuilder.buildBlock(v0, v1) */
} /* ) */

struct VStack<Content: View>: View {
    …
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
}

@resultBuilder enum ViewBuilder {
    static func buildBlock(_: View...) -> some View { … }
}
```

### Fruta's smoothie lists, pre-DSL — [14:49]

```swift
// Fruta’s Smoothie lists

extension Smoothie {
    static let berryBlue = Smoothie(
        id: "berry-blue",
        title: "Berry Blue",
        description: "Filling and refreshing, this smoothie will fill you with joy!",
        measuredIngredients: [
            MeasuredIngredient(.orange, measurement: Measurement(value: 1.5, unit: .cups)),
            MeasuredIngredient(.blueberry, measurement: Measurement(value: 1, unit: .cups)),
            MeasuredIngredient(.avocado, measurement: Measurement(value: 0.2, unit: .cups))
        ],
        hasFreeRecipe: true
    )

    static let carrotChops = Smoothie(…)
    static let crazyColada = Smoothie(…)
    // Plus 12 more…
}

extension Smoothie {
    private static let allSmoothies: [Smoothie] = [
        .berryBlue,
        .carrotChops,
        .crazyColada,
        // Plus 12 more…
    ]

    static func all(includingPaid: Bool = true) -> [Smoothie] {
        if includingPaid {
            return allSmoothies
        }

        logger.log("Free smoothies only")
        return allSmoothies.filter { $0.hasFreeRecipe }
    }
}
```

### Fruta's smoothie lists, pre-DSL (hypothetical alternative) — [14:50]

```swift
// Fruta’s Smoothie lists (hypothetical alternative)

extension Smoothie {
    static let berryBlue = Smoothie(
        id: "berry-blue",
        title: "Berry Blue",
        description: "Filling and refreshing, this smoothie will fill you with joy!",
        measuredIngredients: [
            MeasuredIngredient(.orange, measurement: Measurement(value: 1.5, unit: .cups)),
            MeasuredIngredient(.blueberry, measurement: Measurement(value: 1, unit: .cups)),
            MeasuredIngredient(.avocado, measurement: Measurement(value: 0.2, unit: .cups))
        ],
        hasFreeRecipe: true
    )

    static let carrotChops = Smoothie(…)
    static let crazyColada = Smoothie(…)
    // Plus 12 more…
}

extension Smoothie {
   static func all(includingPaid: Bool = true) -> [Smoothie] {
       var allSmoothies: [Smoothie] = [
            .berryBlue,
            .carrotChops,
        ]

        if includingPaid {
            allSmoothies += [
                .crazyColada,
                // Plus more
            ]
        } else {
            logger.log("Free smoothies only")
        }

        return allSmoothies
    }
}
```

### Fruta's smoothie lists, pre-DSL — [14:51]

```swift
// Fruta’s Smoothie lists

extension Smoothie {
    static let berryBlue = Smoothie(
        id: "berry-blue",
        title: "Berry Blue",
        description: "Filling and refreshing, this smoothie will fill you with joy!",
        measuredIngredients: [
            MeasuredIngredient(.orange, measurement: Measurement(value: 1.5, unit: .cups)),
            MeasuredIngredient(.blueberry, measurement: Measurement(value: 1, unit: .cups)),
            MeasuredIngredient(.avocado, measurement: Measurement(value: 0.2, unit: .cups))
        ],
        hasFreeRecipe: true
    )

    static let carrotChops = Smoothie(…)
    static let crazyColada = Smoothie(…)
    // Plus 12 more…
}

extension Smoothie {
    private static let allSmoothies: [Smoothie] = [
        .berryBlue,
        .carrotChops,
        .crazyColada,
        // Plus 12 more…
    ]

    static func all(includingPaid: Bool = true) -> [Smoothie] {
        if includingPaid {
            return allSmoothies
        }

        logger.log("Free smoothies only")
        return allSmoothies.filter { $0.hasFreeRecipe }
    }
}
```

### Near-final DSL design — [18:05]

```swift
// DSL top-level design

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) -> [Smoothie] {
    Smoothie(
        // TODO: Change these parameters
        id: "berry-blue",
        title: "Berry Blue",
        description: "Filling and refreshing, this smoothie will fill you with joy!",
        measuredIngredients: [
            Ingredient.orange.measured(with: .cups).scaled(by: 1.5),
            Ingredient.blueberry.measured(with: .cups),
            Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
        ]
    )

    Smoothie(…)

    if includingPaid {
        Smoothie(…)

        Smoothie(…)
    } else {
        logger.log("Free smoothies only")
    }
}
```

### Possible DSL description/ingredient designs (start) — [19:57]

```swift
// Possible DSL description/ingredient designs

Smoothie(
    id: "berry-blue",
    title: "Berry Blue",
    description: "Filling and refreshing, this smoothie will fill you with joy!",
    measuredIngredients: [
        Ingredient.orange.measured(with: .cups).scaled(by: 1.5),
        Ingredient.blueberry.measured(with: .cups),
        Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
    ]
)
```

### Possible DSL description/ingredient designs (modifiers) — [20:11]

```swift
// Possible DSL description/ingredient designs

Smoothie(id: "berry-blue", title: "Berry Blue")
    .description("Filling and refreshing, this smoothie will fill you with joy!")
    .ingredient(Ingredient.orange.measured(with: .cups).scaled(by: 1.5))
    .ingredient(Ingredient.blueberry.measured(with: .cups))
    .ingredient(Ingredient.avocado.measured(with: .cups).scaled(by: 0.2))
```

### Possible DSL description/ingredient designs (all marker types) — [20:25]

```swift
// Possible DSL description/ingredient designs

Smoothie {
    ID("berry-blue")
    Title("Berry Blue")
    Description("Filling and refreshing, this smoothie will fill you with joy!")

    Recipe(
        Ingredient.orange.measured(with: .cups).scaled(by: 1.5),
        Ingredient.blueberry.measured(with: .cups),
        Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
    )
}
```

### Possible DSL description/ingredient designs (some marker types) — [20:36]

```swift
// Possible DSL description/ingredient designs

Smoothie(id: "berry-blue", title: "Berry Blue") {
    Description("Filling and refreshing, this smoothie will fill you with joy!")

    Recipe(
        Ingredient.orange.measured(with: .cups).scaled(by: 1.5),
        Ingredient.blueberry.measured(with: .cups),
        Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
    )
}
```

### Possible DSL description/ingredient designs (no marker types) — [21:13]

```swift
// Possible DSL description/ingredient designs

Smoothie(id: "berry-blue", title: "Berry Blue") {
    "Filling and refreshing, this smoothie will fill you with joy!"

    Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
    Ingredient.blueberry.measured(with: .cups)
    Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
}
```

### Final DSL design — [21:43]

```swift
// DSL top-level design

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) -> [Smoothie] {
    Smoothie(id: "berry-blue", title: "Berry Blue") {
        "Filling and refreshing, this smoothie will fill you with joy!"

        Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
        Ingredient.blueberry.measured(with: .cups)
        Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
    }

    Smoothie(…) { … }

    if includingPaid {
        Smoothie(…) { … }
    } else {
        logger.log("Free smoothies only")
    }
}
```

### Basic SmoothieArrayBuilder — [24:05]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildBlock(_ components: Smoothie...) -> [Smoothie] {
    return components
  }
}
```

### How ‘buildBlock(…)’ works — [24:39]

```swift
// How ‘buildBlock(…)’ works

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) {
    /* let v0 = */ Smoothie(id: "berry-blue", title: "Berry Blue") { … }

    /* let v1 = */ Smoothie(id: "carrot-chops", title: "Carrot Chops") { … }

    // …more smoothies…

    /* return SmoothieArrayBuilder.buildBlock(v0, v1, …) */
}
```

### Basic SmoothieArrayBuilder — [25:03]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildBlock(_ components: Smoothie...) -> [Smoothie] {
    return components
  }
}
```

### Smoothie initializer (incomplete) — [25:56]

```swift
extension Smoothie {
  init(id: Smoothie.ID, title: String, /* FIXME */ _ makeIngredients: () -> (String, [MeasuredIngredient])) {
    let (description, ingredients) = makeIngredients()
    self.init(id: id, title: title, description: description, measuredIngredients: ingredients)
  }
}
```

### SmoothieArrayBuilder with simple ‘if’ statements (incorrect) — [27:47]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: Smoothie...) -> [Smoothie] {
    return components
  }
}
```

### How ‘if’ statements work with ‘buildOptional(_:)’ — [28:01]

```swift
// How ‘if’ statements work with ‘buildOptional(_:)’

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) {
    /* let v0 = */ Smoothie(id: "berry-blue", …) { … }
    /* let v1 = */ Smoothie(id: "carrot-chops", …) { … }

    /* let v2: [Smoothie] */
    if includingPaid {
        /* let v2_0 = */ Smoothie(id: "crazy-colada", …) { … }
        /* let v2_1 = */ Smoothie(id: "hulking-lemonade", …) { … }
        /* let v2_block = SmoothieArrayBuilder.buildBlock(v2_0, v2_1)
           v2 = SmoothieArrayBuilder.buildOptional(v2_block) */
    }
    /* else {
        v2 = SmoothieArrayBuilder.buildOptional(nil)
    } */

    /* return SmoothieArrayBuilder.buildBlock(v0, v1, v2) */
}
```

### SmoothieArrayBuilder with simple ‘if’ statements (incorrect) — [29:07]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: Smoothie...) -> [Smoothie] {
    return components
  }
}
```

### Why didn’t our ‘buildOptional(_:)’ work? — [29:28]

```swift
// Why didn’t our ‘buildOptional(_:)’ work?

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) {
    /* let v0 = */ Smoothie(id: "berry-blue", …) { … }
    /* let v1 = */ Smoothie(id: "carrot-chops", …) { … }

    /* let v2: [Smoothie] */
    if includingPaid {
        /* let v2_0 = */ Smoothie(id: "crazy-colada", …) { … }
        /* let v2_1 = */ Smoothie(id: "hulking-lemonade", …) { … }
        /* let v2_block = SmoothieArrayBuilder.buildBlock(v2_0, v2_1)
           v2 = SmoothieArrayBuilder.buildOptional(v2_block) */
    }
    /* else {
        v2 = SmoothieArrayBuilder.buildOptional(nil)
    } */

    /* return SmoothieArrayBuilder.buildBlock(v0, v1, v2) */
}
```

### SmoothieArrayBuilder with simple ‘if’ statements (still incorrect) — [29:40]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: [Smoothie]...) -> [Smoothie] {
    return components.flatMap { $0 }
  }
}
```

### Why didn’t our ‘buildOptional(_:)’ work? — [30:14]

```swift
// Why didn’t our ‘buildOptional(_:)’ work?

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) {
    /* let v0 = */ Smoothie(id: "berry-blue", …) { … }
    /* let v1 = */ Smoothie(id: "carrot-chops", …) { … }

    /* let v2: [Smoothie] */
    if includingPaid {
        /* let v2_0 = */ Smoothie(id: "crazy-colada", …) { … }
        /* let v2_1 = */ Smoothie(id: "hulking-lemonade", …) { … }
        /* let v2_block = SmoothieArrayBuilder.buildBlock(v2_0, v2_1)
           v2 = SmoothieArrayBuilder.buildOptional(v2_block) */
    }
    /* else {
        v2 = SmoothieArrayBuilder.buildOptional(nil)
    } */

    /* return SmoothieArrayBuilder.buildBlock(v0, v1, v2) */
}
```

### The ‘buildExpression(_:)’ method — [31:23]

```swift
// The ‘buildExpression(_:)’ method

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) {
    /* let v0 = SmoothieArrayBuilder.buildExpression( */ Smoothie(id: "berry-blue", …) { … } /* ) */
    /* let v1 = SmoothieArrayBuilder.buildExpression( */ Smoothie(id: "carrot-chops", …) { … } /* ) */

    /* let v2: [Smoothie] */
    if includingPaid {
        /* let v2_0 = SmoothieArrayBuilder.buildExpression( */ Smoothie(id: "crazy-colada", …) { … } /* ) */
        /* let v2_1 = SmoothieArrayBuilder.buildExpression( */ Smoothie(id: "hulking-lemonade", …) { … } /* ) */
        /* let v2_block = SmoothieArrayBuilder.buildBlock(v2_0, v2_1)
           v2 = SmoothieArrayBuilder.buildOptional(v2_block) */
    }
    /* else {
        v2 = SmoothieArrayBuilder.buildOptional(nil)
    } */

    /* return SmoothieArrayBuilder.buildBlock(v0, v1, v2) */
}
```

### SmoothieArrayBuilder with simple ‘if’ statements (correct) — [31:44]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: [Smoothie]...) -> [Smoothie] {
    return components.flatMap { $0 }
  }

  static func buildExpression(_ expression: Smoothie) -> [Smoothie] {
    return [expression]
  }
}
```

### SmoothieArrayBuilder with ‘if’-‘else’ statements — [32:48]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildEither(first component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildEither(second component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: [Smoothie]...) -> [Smoothie] {
    return components.flatMap { $0 }
  }

  static func buildExpression(_ expression: Smoothie) -> [Smoothie] {
    return [expression]
  }
}
```

### How ‘if’-‘else’ statements work with ‘buildEither(…)’ — [32:53]

```swift
// How ‘if’-‘else’ statements work with ‘buildEither(…)’

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) -> [Smoothie] {
    /* let v0: [Smoothie] */
    if includingPaid {
        /* let v0_0 = SmoothieArrayBuilder.buildExpression( */ Smoothie(…) { … } /* ) */
        /* let v0_block = SmoothieArrayBuilder.buildBlock(v0_0)
           v0 = SmoothieArrayBuilder.buildEither(first: v0_block) */
    }
    else {
        /* let v0_0 = SmoothieArrayBuilder.buildExpression( */ logger.log("Only got free smoothies!") /* ) */
        /* let v0_block = SmoothieArrayBuilder.buildBlock(v0_0)
           v0 = SmoothieArrayBuilder.buildEither(second: v0_block) */
    }

    /* return SmoothieArrayBuilder.buildBlock(v0) */
}
```

### How more complicated statements work with ‘buildEither(…)’ — [33:37]

```swift
// How more complicated statements work with ‘buildEither(…)’

var v0: [Smoothie]
switch userRegion {
case .americas:
    // ...smoothies omitted...
    /* let v0_block = SmoothieArrayBuilder.buildBlock(...parameters omitted...)
       v0 = SmoothieArrayBuilder.buildEither(first:
                SmoothieArrayBuilder.buildEither(first: v0_block)) */

case .asiaPacific:
    // ...smoothies omitted...
    /* let v0_block = SmoothieArrayBuilder.buildBlock(…)
       v0 = SmoothieArrayBuilder.buildEither(first:
                SmoothieArrayBuilder.buildEither(second: v0_block)) */

case .eastAtlantic:
    // ...smoothies omitted...
    /* let v0_block = SmoothieArrayBuilder.buildBlock(…)
       v0 = SmoothieArrayBuilder.buildEither(second: v0_block) */
}
```

### SmoothieArrayBuilder with ‘if’-‘else’ statements — [34:12]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildEither(first component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildEither(second component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: [Smoothie]...) -> [Smoothie] {
    return components.flatMap { $0 }
  }

  static func buildExpression(_ expression: Smoothie) -> [Smoothie] {
    return [expression]
  }
}
```

### How ‘if’-‘else’ statements work with ‘buildEither(…)’ — [34:54]

```swift
// How ‘if’-‘else’ statements work with ‘buildEither(…)’

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) -> [Smoothie] {
    /* let v0: [Smoothie] */
    if includingPaid {
        /* let v0_0 = SmoothieArrayBuilder.buildExpression( */ Smoothie(…) { … } /* ) */
        /* let v0_block = SmoothieArrayBuilder.buildBlock(v0_0)
           v0 = SmoothieArrayBuilder.buildEither(first: v0_block) */
    }
    else {
        /* let v0_0 = SmoothieArrayBuilder.buildExpression( */ logger.log("Only got free smoothies!") /* ) */
        /* let v0_block = SmoothieArrayBuilder.buildBlock(v0_0)
           v0 = SmoothieArrayBuilder.buildEither(second: v0_block) */
    }

    /* return SmoothieArrayBuilder.buildBlock(v0) */
}
```

### SmoothieArrayBuilder with support for ‘Void’ results — [35:07]

```swift
@resultBuilder
enum SmoothieArrayBuilder {
  static func buildEither(first component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildEither(second component: [Smoothie]) -> [Smoothie] {
    return component
  }

  static func buildOptional(_ component: [Smoothie]?) -> [Smoothie] {
    return component ?? []
  }

  static func buildBlock(_ components: [Smoothie]...) -> [Smoothie] {
    return components.flatMap { $0 }
  }

  static func buildExpression(_ expression: Smoothie) -> [Smoothie] {
    return [expression]
  }

  static func buildExpression(_ expression: Void) -> [Smoothie] {
    return []
  }
}
```

### Modifier-style methods on Ingredient and MeasuredIngredient — [36:41]

```swift
extension Ingredient {
  func measured(with unit: UnitVolume) -> MeasuredIngredient {
    MeasuredIngredient(self, measurement: Measurement(value: 1, unit: unit))
  }
}

extension MeasuredIngredient {
  func scaled(by scale: Double) -> MeasuredIngredient {
    return MeasuredIngredient(ingredient, measurement: measurement * scale)
  }
}
```

### Closures and result builders — [37:32]

```swift
// Closures and result builders

@SmoothieArrayBuilder
static func all(includingPaid: Bool = true) -> [Smoothie] {
    /* let v0 = SmoothieArrayBuilder.buildExpression( */ Smoothie(…) {
        "Filling and refreshing, this smoothie will fill you with joy!"

        Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
        Ingredient.blueberry.measured(with: .cups)
        Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)
    } /* ) */

    /* let v1 = SmoothieArrayBuilder.buildExpression( */ Smoothie(…) {
        "Packed with vitamin A and C, Carrot Chops is a great way to start your day!"

        Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
        Ingredient.carrot.measured(with: .cups).scaled(by: 0.5)
        Ingredient.mango.measured(with: .cups).scaled(by: 0.5)
    } /* ) */

    /* return SmoothieArrayBuilder.buildBlock(v0, v1) */
}
```

### Smoothie initializer (final) and SmoothieBuilder (initial) — [39:22]

```swift
extension Smoothie {
  init(id: Smoothie.ID, title: String, @SmoothieBuilder _ makeIngredients: () -> (String, [MeasuredIngredient])) {
    let (description, ingredients) = makeIngredients()
    self.init(id: id, title: title, description: description, measuredIngredients: ingredients)
  }
}

@resultBuilder
enum SmoothieBuilder {
  static func buildBlock(_ description: String, components: MeasuredIngredient...) -> (String, [MeasuredIngredient]) {
    return (description, components)
  }
}
```

### Accepting different types — [40:38]

```swift
// Accepting different types

Smoothie(…) /* @SmoothieBuilder */ {
    /* let v0 = */ "Filling and refreshing, this smoothie will fill you with joy!"
    /* let v1 = */ Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
    /* let v2 = */ Ingredient.blueberry.measured(with: .cups)
    /* let v3 = */ Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)

    /* return SmoothieBuilder.buildBlock(v0, v1, v2, v3) */
}
```

### Smoothie initializer (final) and SmoothieBuilder (initial) — [41:01]

```swift
extension Smoothie {
  init(id: Smoothie.ID, title: String, @SmoothieBuilder _ makeIngredients: () -> (String, [MeasuredIngredient])) {
    let (description, ingredients) = makeIngredients()
    self.init(id: id, title: title, description: description, measuredIngredients: ingredients)
  }
}

@resultBuilder
enum SmoothieBuilder {
  static func buildBlock(_ description: String, components: MeasuredIngredient...) -> (String, [MeasuredIngredient]) {
    return (description, components)
  }
}
```

### SmoothieBuilder without the string — [42:43]

```swift
// SmoothieBuilder without the string

Smoothie(…) /* @SmoothieBuilder */ {
    // "Filling and refreshing, this smoothie will fill you with joy!"
    /* let v0 = */ Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
    /* let v1 = */ Ingredient.blueberry.measured(with: .cups)
    /* let v2 = */ Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)

    /* return SmoothieBuilder.buildBlock(v0, v1, v2) */
}

extension SmoothieBuilder {
    static func buildBlock(_ description: String, _ ingredients: ManagedIngredients...) -> (String, [ManagedIngredients]) { … }
}
```

### How Swift improves diagnostics — [43:38]

```swift
// How Swift improves diagnostics

func fn0() throws {}
func fn1() rethrows {}
func fn2() {}

func fn3() deinit {}

func fn4() try {}
```

### SmoothieBuilder without the string — [44:30]

```swift
// SmoothieBuilder without the string

Smoothie(…) /* @SmoothieBuilder */ {
    // "Filling and refreshing, this smoothie will fill you with joy!"
    /* let v0 = */ Ingredient.orange.measured(with: .cups).scaled(by: 1.5)
    /* let v1 = */ Ingredient.blueberry.measured(with: .cups)
    /* let v2 = */ Ingredient.avocado.measured(with: .cups).scaled(by: 0.2)

    /* return SmoothieBuilder.buildBlock(v0, v1, v2) */
}

extension SmoothieBuilder {
    static func buildBlock(_ description: String, _ ingredients: ManagedIngredients...)
        -> (String, [ManagedIngredients]) { … }

    @available(*, unavailable, message: "missing ‘description’ field")
    static func buildBlock(_ ingredients: ManagedIngredients...)
        -> (String, [ManagedIngredients]) { fatalError() }
}
```

### Smoothie initializer (final) and SmoothieBuilder (with error handling) — [44:55]

```swift
extension Smoothie {
  init(id: Smoothie.ID, title: String, @SmoothieBuilder _ makeIngredients: () -> (String, [MeasuredIngredient])) {
    let (description, ingredients) = makeIngredients()
    self.init(id: id, title: title, description: description, measuredIngredients: ingredients)
  }
}

@resultBuilder
enum SmoothieBuilder {
  static func buildBlock(_ description: String, components: MeasuredIngredient...) -> (String, [MeasuredIngredient]) {
    return (description, components)
  }

  @available(*, unavailable, message: "first statement of SmoothieBuilder must be its description String")
  static func buildBlock(_ components: MeasuredIngredient...) -> (String, [MeasuredIngredient]) {
    fatalError()
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10253/4/F323F580-06C3-4F19-9548-AB7560E40CD4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10253/4/F323F580-06C3-4F19-9548-AB7560E40CD4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10253) — developer.apple.com. Indexed for agent consumption._