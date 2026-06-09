---
id: "wwdc2025-280"
event: "wwdc2025"
year: 2025
title: "Code-along: Cook up a rich text experience in SwiftUI with AttributedString"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/280"
topics: ["Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Code-along: Cook up a rich text experience in SwiftUI with AttributedString

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-280](https://developer.apple.com/videos/play/wwdc2025/280)

Learn how to build a rich text experience with SwiftUI’s TextEditor API and AttributedString. Discover how you can enable rich text editing, build custom controls that manipulate the contents of your editor, and customize the formatting options available. Explore advanced capabilities of AttributedString that help you craft the best text editing experiences.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,720 words)

## Documentation & Resources

- [Character](https://developer.apple.com/documentation/Swift/Character) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/Character
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/Character.json
- [AttributedTextSelection](https://developer.apple.com/documentation/SwiftUI/AttributedTextSelection) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/AttributedTextSelection
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/AttributedTextSelection.json
- [AttributedTextFormatting](https://developer.apple.com/documentation/SwiftUI/AttributedTextFormatting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/AttributedTextFormatting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/AttributedTextFormatting.json
- [Building rich SwiftUI text experiences](https://developer.apple.com/documentation/SwiftUI/building-rich-swiftui-text-experiences) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/building-rich-swiftui-text-experiences
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/building-rich-swiftui-text-experiences.json

## Code Snippets

### TextEditor and String — [1:15]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: String

    var body: some View {
        TextEditor(text: $text)
    }
}
```

### TextEditor and AttributedString — [1:45]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: AttributedString

    var body: some View {
        TextEditor(text: $text)
    }
}
```

### AttributedString Basics — [4:43]

```swift
var text = AttributedString(
  "Hello 👋🏻! Who's ready to get "
)

var cooking = AttributedString("cooking")
cooking.foregroundColor = .orange
text += cooking

text += AttributedString("?")

text.font = .largeTitle
```

### Build custom controls: Basics (initial attempt) — [5:36]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: AttributedString
    @State private var selection = AttributedTextSelection()

    var body: some View {
        TextEditor(text: $text, selection: $selection)
            .preference(key: NewIngredientPreferenceKey.self, value: newIngredientSuggestion)
    }

    private var newIngredientSuggestion: IngredientSuggestion {
        let name = text[selection.indices(in: text)] // build error

        return IngredientSuggestion(
            suggestedName: AttributedString())
    }
}
```

### Slicing AttributedString with a Range — [8:53]

```swift
var text = AttributedString(
  "Hello 👋🏻! Who's ready to get cooking?"
)

guard let cookingRange = text.range(of: "cooking") else {
  fatalError("Unable to find range of cooking")
}

text[cookingRange].foregroundColor = .orange
```

### Slicing AttributedString with a RangeSet — [10:50]

```swift
var text = AttributedString(
  "Hello 👋🏻! Who's ready to get cooking?"
)

let uppercaseRanges = text.characters
  .indices(where: \.isUppercase)

text[uppercaseRanges].foregroundColor = .blue
```

### Build custom controls: Basics (fixed) — [11:40]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: AttributedString
    @State private var selection = AttributedTextSelection()

    var body: some View {
        TextEditor(text: $text, selection: $selection)
            .preference(key: NewIngredientPreferenceKey.self, value: newIngredientSuggestion)
    }

    private var newIngredientSuggestion: IngredientSuggestion {
        let name = text[selection]

        return IngredientSuggestion(
            suggestedName: AttributedString(name))
    }
}
```

### Build custom controls: Recipe attribute — [12:32]

```swift
import SwiftUI

struct IngredientAttribute: CodableAttributedStringKey {
    typealias Value = Ingredient.ID

    static let name = "SampleRecipeEditor.IngredientAttribute"
}

extension AttributeScopes {
    /// An attribute scope for custom attributes defined by this app.
    struct CustomAttributes: AttributeScope {
        /// An attribute for marking text as a reference to an recipe's ingredient.
        let ingredient: IngredientAttribute
    }
}

extension AttributeDynamicLookup {
    /// The subscript for pulling custom attributes into the dynamic attribute lookup.
    ///
    /// This makes them available throughout the code using the name they have in the
    /// `AttributeScopes.CustomAttributes` scope.
    subscript<T: AttributedStringKey>(
        dynamicMember keyPath: KeyPath<AttributeScopes.CustomAttributes, T>
    ) -> T {
        self[T.self]
    }
}
```

### Build custom controls: Modifying text (initial attempt) — [12:56]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: AttributedString
    @State private var selection = AttributedTextSelection()

    var body: some View {
        TextEditor(text: $text, selection: $selection)
            .preference(key: NewIngredientPreferenceKey.self, value: newIngredientSuggestion)
    }

    private var newIngredientSuggestion: IngredientSuggestion {
        let name = text[selection]

        return IngredientSuggestion(
            suggestedName: AttributedString(name),
            onApply: { ingredientId in
                let ranges = text.characters.ranges(of: name.characters)

                for range in ranges {
                    // modifying `text` without updating `selection` is invalid and resets the cursor 
                    text[range].ingredient = ingredientId
                }
            })
    }
}
```

### AttributedString Character View — [17:40]

```swift
text.characters[index] // "👋🏻"
```

### AttributedString Unicode Scalar View — [17:44]

```swift
text.unicodeScalars[index] // "👋"
```

### AttributedString Runs View — [17:49]

```swift
text.runs[index] // "Hello 👋🏻! ..."
```

### AttributedString UTF-8 View — [18:13]

```swift
text.utf8[index] // "240"
```

### AttributedString UTF-16 View — [18:17]

```swift
text.utf16[index] // "55357"
```

### Updating Indices during AttributedString Mutations — [18:59]

```swift
var text = AttributedString(
  "Hello 👋🏻! Who's ready to get cooking?"
)

guard var cookingRange = text.range(of: "cooking") else {
  fatalError("Unable to find range of cooking")
}

let originalRange = cookingRange
text.transform(updating: &cookingRange) { text in
  text[originalRange].foregroundColor = .orange

  let insertionPoint = text
    .index(text.startIndex, offsetByCharacters: 6)

  text.characters
    .insert(contentsOf: "chef ", at: insertionPoint)
}

print(text[cookingRange])
```

### Build custom controls: Modifying text (fixed) — [20:22]

```swift
import SwiftUI

struct RecipeEditor: View {
    @Binding var text: AttributedString
    @State private var selection = AttributedTextSelection()

    var body: some View {
        TextEditor(text: $text, selection: $selection)
            .preference(key: NewIngredientPreferenceKey.self, value: newIngredientSuggestion)
    }

    private var newIngredientSuggestion: IngredientSuggestion {
        let name = text[selection]

        return IngredientSuggestion(
            suggestedName: AttributedString(name),
            onApply: { ingredientId in
                let ranges = RangeSet(text.characters.ranges(of: name.characters))

                text.transform(updating: &selection) { text in
                    text[ranges].ingredient = ingredientId
                }
            })
    }
}
```

### Define your text format: RecipeFormattingDefinition Scope — [22:03]

```swift
struct RecipeFormattingDefinition: AttributedTextFormattingDefinition {
    struct Scope: AttributeScope {
        let foregroundColor: AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute
        let adaptiveImageGlyph: AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute
        let ingredient: IngredientAttribute
    }

    var body: some AttributedTextFormattingDefinition<Scope> {

    }
}

// pass the custom formatting definition to the TextEditor in the updated `RecipeEditor.body`:

        TextEditor(text: $text, selection: $selection)
            .preference(key: NewIngredientPreferenceKey.self, value: newIngredientSuggestion)
            .attributedTextFormattingDefinition(RecipeFormattingDefinition())
```

### Define your text format: AttributedTextValueConstraints — [23:50]

```swift
struct IngredientsAreGreen: AttributedTextValueConstraint {
    typealias Scope = RecipeFormattingDefinition.Scope
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute

    func constrain(_ container: inout Attributes) {
        if container.ingredient != nil {
            container.foregroundColor = .green
        } else {
            container.foregroundColor = nil
        }
    }
}

// list the value constraint in the recipe formatting definition's body:
    var body: some AttributedTextFormattingDefinition<Scope> {
        IngredientsAreGreen()
    }
```

### AttributedStringKey Constraint: Inherited by Added Text — [29:28]

```swift
static let inheritedByAddedText = false
```

### AttributedStringKey Constraint: Invalidation Conditions — [30:12]

```swift
static let invalidationConditions:
  Set<AttributedString.AttributeInvalidationCondition>? =
  [.textChanged]
```

### AttributedStringKey Constraint: Run Boundaries — [31:25]

```swift
static let runBoundaries:
  AttributedString.AttributeRunBoundaries? =
  .paragraph
```

### Define your text format: AttributedStringKey Constraints — [32:46]

```swift
struct IngredientAttribute: CodableAttributedStringKey {
    typealias Value = Ingredient.ID

    static let name = "SampleRecipeEditor.IngredientAttribute"

    static let inheritedByAddedText: Bool = false

    static let invalidationConditions: Set<AttributedString.AttributeInvalidationCondition>? = [.textChanged]
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/280/5/3596f3d4-e661-4414-a6ba-79128adcc8e6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/280/5/3596f3d4-e661-4414-a6ba-79128adcc8e6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/280) — developer.apple.com. Indexed for agent consumption._
