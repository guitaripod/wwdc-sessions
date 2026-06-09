---
id: "wwdc2020-10020"
event: "wwdc2020"
year: 2020
title: "Make your app visually accessible"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10020"
topics: ["Design", "SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Make your app visually accessible

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10020](https://developer.apple.com/videos/play/wwdc2020/10020)

When you design with accessibility in mind, you empower everyone to use your app. Discover how to create an adaptive interface for your app that takes a thoughtful approach to color, provides readable text, and accommodates other visual settings to maintain a great experience throughout. We’ve designed this session like our user interfaces — to be accessible to all. If you’d like to learn even more about accessibility and design, you may also enjoy “Visual Design and Accessibility,” “Accessibility Inspector,” “Building Apps with Dynamic Type,” and “Introducing SF Symbols.”

**Keywords:** `accessibility`, `color`, `color blind`, `design`, `labels`, `reduce motion`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,561 words)

## Documentation & Resources

- [Accessibility for UIKit](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/accessibility-for-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/accessibility-for-uikit.json

## Code Snippets

### Button Shapes — [3:14]

```swift
func observeButtonShapesNotification() {
    // Make buttons more visible by using shapes.
    // If your default design does not include button shapes, observe this notification to make visual changes.
    NotificationCenter.default.addObserver(self, selector: #selector(updateButtonShapes), name: UIAccessibility.buttonShapesEnabledStatusDidChangeNotification, object: nil)
}

@objc func updateButtonShapes() {
    if UIAccessibility.buttonShapesEnabled {
        // Use extra visualizations for buttons.
    } else {
        // Use default design for buttons.
    }
}
```

### Differentiate Without Color — [3:31]

```swift
func observeDifferentiateWithoutColorNotification() {
    // Use symbols or shapes to convey meaning instead of relying on color alone.
    // If your default design does not differentiate without color, observe this notification to make visual changes.
    NotificationCenter.default.addObserver(self, selector: #selector(updateColorAndSymbols), name: NSNotification.Name(UIAccessibility.differentiateWithoutColorDidChangeNotification), object: nil)
}

@objc func updateColorAndSymbols() {
    if UIAccessibility.shouldDifferentiateWithoutColor {
        // Use symbols or shapes to convey meaning.
    } else {
        // Use default design.
    }
}
```

### Smart Invert Colors — [7:47]

```swift
extension UIView {
    @available(iOS 11.0, tvOS 11.0)
    var accessibilityIgnoresInvertColors: Bool { get set }
}
```

### Large Text — [9:57]

```swift
// ZodiacConstellationCell.swift


override func traitCollectionDidChange (_ previousTraitCollection: UITraitCollection?) {

     if (traitCollection.preferredContentSizeCategory       
         < .accessibilityMedium) { // Default font sizes

         stackView.axis = .horizontal
         stackView.alignment = .center

     } else { // Accessibility font sizes

         stackView.axis = .vertical
         stackView.alignment = .leading

     }
}
```

### Bold Text — [11:33]

```swift
func observeBoldTextNotification() {
    // Update labels to use bold or heavy font styles.
    // If you aren't using system font styles, observe this notification to make visual changes.
    NotificationCenter.default.addObserver(self, selector: #selector(updateLabelWeight), name: UIAccessibility.boldTextStatusDidChangeNotification, object: nil)
}

@objc func updateLabelWeight() {
    if UIAccessibility.isBoldTextEnabled {
        // Use bold or heavy font weight
    } else {
        // Use font weight that is default to your design.
    }
}
```

### Reduce Motion — [13:08]

```swift
func observeReduceMotionNotification() {
    // Observe this notification to reduce or remove the frequency and intensity of motion effects.
    NotificationCenter.default.addObserver(self, selector: #selector(updateMotionEffects), name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
}

@objc func updateMotionEffects() {
    if UIAccessibility.isReduceMotionEnabled {
        // Reduce or remove extraneous motion effects.
    } else {
        // Use default motion effects.
    }
}
```

### Prefers Cross-fade Transitions — [13:51]

```swift
func observeCrossFadeTransitionsNotification() {
    // Reduce or remove sliding animations for transitioning views.
    // If you aren't using system-provided navigation, observe this notification to make visual changes.
    NotificationCenter.default.addObserver(self, selector: #selector(updateTransitionEffects), name: UIAccessibility.prefersCrossFadeTransitionsStatusDidChange, object: nil)
}

@objc func updateTransitionEffects() {
    if UIAccessibility.prefersCrossFadeTransitions {
        // Replace sliding transitions with cross-fade animations.
    } else {
        // Use default sliding transitions.
    }
}
```

### Reduce Transparency — [15:07]

```swift
func observeReduceTransparencyNotification() {
    // Reduce or remove transparency by adjusting these effects to be completely opaque.
    // If you aren't using system-provided visual effects for blurs or vibrancy, observe this notification to make visual changes.
    NotificationCenter.default.addObserver(self, selector: #selector(updateTransparencyEffects), name: UIAccessibility.reduceTransparencyStatusDidChangeNotification, object: nil)
}

@objc func updateTransparencyEffects() {
    if UIAccessibility.isReduceTransparencyEnabled {
        // Make transparency effects opaque.
    } else {
        // Use default transparency.
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10020/6/E082026F-7D80-4814-9A23-5A52E4CBF628/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10020) — developer.apple.com. Indexed for agent consumption._
