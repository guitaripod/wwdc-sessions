---
id: "wwdc2021-10220"
event: "wwdc2021"
year: 2021
title: "Localize your SwiftUI app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10220"
topics: ["Accessibility & Inclusion", "Developer Tools", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Localize your SwiftUI app

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10220](https://developer.apple.com/videos/play/wwdc2021/10220)

Learn how to localize your SwiftUI app and make it available to a global audience. Explore how you can localize strings in SwiftUI, including those with styles and formatting. We'll demonstrate how you can save time by having SwiftUI automatically handle tasks such as layout and keyboard shortcuts, and take you through the localization workflow in Xcode 13. To get the most out of this session and learn more about the Markdown language and AttributedString, check out "What's new in Foundation" from WWDC21.

**Keywords:** `🌍`, `🌎`, `🌏`, `i18n`, `keyboard shortcuts`, `localizedstringkey`, `markdown`, `stringsdict`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,560 words)

## Documentation & Resources

- [Localization](https://developer.apple.com/documentation/Xcode/localization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localization.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/
- [Fruta: Building a feature-rich app with SwiftUI](https://developer.apple.com/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui.json

## Code Snippets

### Text() with a string literal — [1:34]

```swift
Button(action: done) {
   Text("Done", comment: "Button title to dismiss rewards sheet")
}
```

### Text() with a string literal and interpolation — [1:58]

```swift
// RewardsCard.swift

Text("You are \(10 - totalStamps) points away from a free smoothie!")
```

### Text() with tableName — [2:06]

```swift
// RecipeView.swift
Text("Ingredients.recipe", tableName: "Ingredients", comment: "Ingredients in a recipe. For languages that have different words for \"Ingredient\" based on semantic context.")
Text("Ingredients.menu", tableName: "Ingredients", comment: "Ingredients in a smoothie. For languages that have different words for \"Ingredient\" based on semantic context.")
```

### Declare localizable attributes in a custom view — [2:52]

```swift
struct Card: View {
    var title: LocalizedStringKey
    var subtitle: LocalizedStringKey

    var body: some View {
        Circle()
            .fill(BackgroundStyle())
            .overlay(
                VStack(spacing: 16) {
                    Text(title)
                    Text(subtitle)
                }
            )
    }
}

Card(
    title: "Thank you for your order!",
    subtitle: "We will notify you when your order is ready."
 )
```

### Text() with multiline string literal — [3:47]

```swift
Text("""
        A delicious blend of tropical fruits and blueberries will
        have you sambaing around like you never knew you could!
        """,
        comment: "Tropical Blue smoothie description")
```

### Customize attributes — [4:39]

```swift
VStack(alignment: .leading) {
    Text(smoothie.title)
        .font(.headline)
    Text(ingredients)
}
```

### Using Markdown — [5:13]

```swift
// Smoothie.swift

Text("A refreshing blend that's a *real kick*!", comment: "Lemonberry smoothie description")
```

### Create a measurement formatter (prior to iOS 15) — [6:04]

```swift
let calories = Measurement<UnitEnergy>(
    value: nutritionFact.kilocalories, unit: .kilocalories)

static let measurementFormatter: MeasurementFormatter = {
    let formatter = MeasurementFormatter()
    formatter.unitStyle = .long
    formatter.unitOptions = .providedUnit
    return formatter
}()

Text(Self.measurementFormatter.string(from: calories))

Text("Energy: \(calories, formatter: Self.measurementFormatter)")
```

### Specify the format in a declarative manner (iOS 15) — [6:22]

```swift
let calories = Measurement<UnitEnergy>(
    value: nutritionFact.kilocalories, unit: .kilocalories)

Text(calories.formatted(.measurement(width: .wide, usage: .food)))

Text("Energy: \(calories, format: .measurement(width: .wide, usage: .food))")
```

### Specify a keyboard shortcut — [6:53]

```swift
struct SmoothieCommands: Commands {

    var body: some Commands {
        CommandMenu(Text("Smoothie", comment: "Menu title for smoothie-related actions")) {
            SmoothieFavoriteButton(smoothie)
                .keyboardShortcut("+")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10220/6/3866585A-3920-44B4-AB3F-03A446FCDE3A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10220/6/3866585A-3920-44B4-AB3F-03A446FCDE3A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10220) — developer.apple.com. Indexed for agent consumption._
