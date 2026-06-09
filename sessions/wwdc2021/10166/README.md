---
id: "wwdc2021-10166"
event: "wwdc2021"
year: 2021
title: "Meet DocC documentation in Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10166"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet DocC documentation in Xcode

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10166](https://developer.apple.com/videos/play/wwdc2021/10166)

Discover how you can use DocC to build and share documentation for Swift packages and frameworks. We’ll show you how to begin generating documentation from your own code — or from third-party code you depend upon — and write and format it using Markdown. And we’ll also take you through the export process, helping you generate DocC archives to share with the public.

**Keywords:** `docc`, `doccarchive`, `documentation`, `documentation catalog`, `documentation compiler`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,421 words)

## Documentation & Resources

- [Formatting your documentation](https://developer.apple.com/documentation/docc) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [Writing symbol documentation in your source files](https://developer.apple.com/documentation/Xcode/writing-symbol-documentation-in-your-source-files) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/writing-symbol-documentation-in-your-source-files
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/writing-symbol-documentation-in-your-source-files.json
- [SlothCreator: Building DocC documentation in Xcode](https://developer.apple.com/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode.json
- [Documenting a Swift Framework or Package](https://www.swift.org/documentation/docc/documenting-a-swift-framework-or-package) _documentation_

## Code Snippets

### Existing comments in code — [9:34]

```swift
// A model representing a sloth.
public struct Sloth {
    // ...
}
```

### Writing documentation comments — [10:05]

```swift
/// A model representing a sloth.
public struct Sloth {
    // ...
}
```

### Writing block-style documentation comments — [10:22]

```swift
/** 
 A model representing a sloth.
 */
public struct Sloth {
    // ...
}
```

### Documenting the Food struct — [11:34]

```swift
/// Food that a sloth can consume.
///
/// Sloths love to eat the leaves and twigs they find in the rainforest canopy as they
/// slowly move around. To feed them these items, you can use the `twig`,
/// `regularLeaf` and `largeLeaf` default foods.
///
/// ```swift
/// superSloth.eat(.twig)
/// ```
public struct Food {
		// ...
}
```

### Documenting the Sloth.sleep(in:for:) method — [13:58]

```swift
/// A model representing a sloth.
public struct Sloth {
    /// Sleep in the specified habitat for a number of hours.
    ///
    /// - Parameters:
    ///     - habitat: The location for the sloth to sleep.
    ///     - numberOfHours: The number of hours for the sloth to sleep.
    /// - Returns: The sloth’s energy level after sleeping.
    mutating public func sleep(in habitat: Habitat, for numberOfHours: Int = 12) -> Int {
        energyLevel += habitat.comfortLevel * numberOfHours
        return energyLevel
    }
}
```

### Documenting the Sloth.eat(_:quantity:) method — [15:39]

```swift
/// A model representing a sloth.
public struct Sloth {
    /// Eat the provided specialty sloth food.
    ///
    /// Sloths love to eat while they move very slowly through their rainforest habitats. They
    /// are especially happy to consume leaves and twigs, which they digest over long periods
    /// of time, mostly while they sleep.
    ///
    /// ```swift
    /// let flower = Sloth.Food(name: "Flower Bud", energy: 10)
    /// superSloth.eat(flower)
    /// ```
    ///
    /// - Parameters:
    ///   - food: The food for the sloth to eat.
    ///   - quantity: The quantity of the food for the sloth to eat.
    /// - Returns: The sloth's energy level after eating.
    mutating public func eat(_ food: Food, quantity: Int = 1) -> Int {
        energyLevel += food.energy * quantity
        return energyLevel
    }
}
```

### Adding symbol links to the documentation for Sloth.sleep(in:for:) — [17:46]

```swift
/// A model representing a sloth.
public struct Sloth {
    /// The energy level of the sloth.
    public var energyLevel: EnergyLevel

    /// Sleep in the specified habitat for a number of hours.
    ///
    /// Each time the sloth sleeps, their ``energyLevel`` increases every hour by the
    /// habitat's ``Habitat/comfortLevel``.  
    ///
    /// - Parameters:
    ///     - habitat: The location for the sloth to sleep.
    ///     - numberOfHours: The number of hours for the sloth to sleep.
    /// - Returns: The sloth’s energy level after sleeping.
    mutating public func sleep(in habitat: Habitat, for numberOfHours: Int = 12) -> Int {
        energyLevel += habitat.comfortLevel * numberOfHours
        return energyLevel
    }
}
```

### Adding symbol links to the documentation for Sloth.eat(_:quantity:) — [18:44]

```swift
/// A model representing a sloth.
public struct Sloth {
    /// Eat the provided specialty sloth food.
    ///
    /// Sloths love to eat while they move very slowly through their rainforest habitats. They
    /// are especially happy to consume leaves and twigs, which they digest over long periods
    /// of time, mostly while they sleep.
    ///
    /// ```swift
    /// let flower = Sloth.Food(name: "Flower Bud", energy: 10)
    /// superSloth.eat(flower)
    /// ```
    ///
    /// When they eat food, a sloth's ``energyLevel`` increases by the food's
    /// ``Food/energy``. 
    ///
    /// - Parameters:
    ///   - food: The food for the sloth to eat.
    ///   - quantity: The quantity of the food for the sloth to eat.
    /// - Returns: The sloth's energy level after eating.
    mutating public func eat(_ food: Food, quantity: Int = 1) -> Int {
        energyLevel += food.energy * quantity
        return energyLevel
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10166/7/097C7329-25A1-4933-A07D-78C7F1F1CA46/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10166/7/097C7329-25A1-4933-A07D-78C7F1F1CA46/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10166) — developer.apple.com. Indexed for agent consumption._