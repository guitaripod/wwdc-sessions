# Refine accessibility for custom controls

**Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-220](https://developer.apple.com/videos/play/wwdc2026/220)

Unlock the full potential of your app’s interactive elements by making them accessible to everyone. We’ll break down how people understand and use controls with VoiceOver and other assistive technologies, exploring a variety of input methods like actions, the passthrough gesture, and direct touch. Join us for an in-depth exploration of several example controls as we refine and elevate the accessibility experience in each one.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Accessible controls](https://developer.apple.com/documentation/SwiftUI/Accessible-controls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Accessible-controls
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Accessible-controls.json
- [Accessible descriptions](https://developer.apple.com/documentation/SwiftUI/Accessible-descriptions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Accessible-descriptions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Accessible-descriptions.json
- [Accessibility fundamentals](https://developer.apple.com/documentation/SwiftUI/Accessibility-fundamentals) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Accessibility-fundamentals
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Accessibility-fundamentals.json
- [Creating accessible views](https://developer.apple.com/documentation/SwiftUI/creating-accessible-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/creating-accessible-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/creating-accessible-views.json

## Code Snippets

### Improve accessibility for coffee dispenser — [5:01]

```swift
// Improve accessibility for coffee dispenser

import SwiftUI

struct CoffeeDispenserView: View {
    @State var coffee: Double = 0.0
    var body: some View {
        CoffeeSlider(value: coffee)
            .accessibilityElement()
            .accessibilityLabel("Coffee Dispenser")
            .accessibilityValue("\(Int(coffee)) ounces")
            .accessibilityAddTraits(.adjustable)
            .accessibilityAdjustableAction { direction in
                switch direction {
                case .increment:
                    increaseCoffeeAmount()
                case .decrement:
                    decreaseCoffeeAmount()
                }
            }
    }
}
```

### Set the accessibility activation point — [7:05]

```swift
// Set the accessibility activation point
import SwiftUI

struct CoffeeDispenserView: View {
    @State var coffee: Double = 0.0

    var body: some View {
        CoffeeSlider(value: coffee)
            .accessibilityActivationPoint(
                UnitPoint(x: 0.5, y: 1 - coffee)
            )
    }
}
```

### Post accessibility announcements — [7:27]

```swift
// Post accessibility announcements 

import SwiftUI

struct CoffeeDispenserView: View {
    @State var coffee: Double = 0.0

    var body: some View {
        CoffeeSlider(value: coffee)
            // ...
            .onChange(of: coffee) { _, newValue in
                if sufficientTimeSinceLastAnnouncement() && valueHasChanged() {
                    cacheLastSpokenValue(newValue)
                    AccessibilityNotification
                        .Announcement(newValue)
                        .post()
                }
            }
    }
}
```

### Add custom actions — [10:13]

```swift
// Add custom actions

import SwiftUI

struct EqualizerView: View {
    var body: some View {
        EqualizerPad()
            .accessibilityActions("Move Up") {
                increaseY(by: 10)
            }
            .accessibilityActions("Move Right") {
                increaseX(by: 10)
            }
            .accessibilityActions("Move Down") {
                decreaseY(by: 10)
            }
            .accessibilityActions("Move Left") {
                decreaseX(by: 10)
            }
     }
 }
```

### Customize accessibility for the interactive cat surface — [12:47]

```swift
// Customize accessibility for the interactive cat surface

import SwiftUI

struct VirtualCat: View {
    var cat: CatModel
    var body: some View {
        InteractiveCatSurface()
            .accessibilityLabel("Virtual Cat")
            .accessibilityValue(cat.currentReaction.description)
            .accessibilityDirectTouch([.requiresActivation])
     }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/220/4/945f8d34-8427-4476-ae75-34edc4a9c3f9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/220/4/945f8d34-8427-4476-ae75-34edc4a9c3f9/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._