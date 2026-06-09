---
id: "tech-talks-111433"
event: "tech-talks"
year: 2026
title: "Prepare your app for Accessibility Nutrition Labels"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111433"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Prepare your app for Accessibility Nutrition Labels

**Event:** Tech Talks · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-04-22 · **Session:** [tech-talks-111433](https://developer.apple.com/videos/play/tech-talks/111433)

Learn how to prepare your app for Accessibility Nutrition Labels by supporting essential accessibility features. Discover how you can enhance interaction methods like VoiceOver and Voice Control by properly configuring accessibility labels, traits, and values for custom controls and gestures. Find out how you can support larger text sizes using Dynamic Type, and prevent content truncation with flexible layouts. And learn how to make your app design more inclusive by adopting Dark Mode, responding to preferences like Differentiate Without Color, and ensuring sufficient contrast.

**Keywords:** `accessibility`, `inclusion`, `nutrition label`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,216 words)

## Documentation & Resources

- [Overview of Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels
- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json
- [Learn more about designing for accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility/overview/introduction/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility/overview/introduction/

## Code Snippets

### Add descriptive accessibility labels — [6:39]

```swift
// Add descriptive accessibility labels

// SwiftUI
Image(landmark.backgroundImageName)
  .accessibilityLabel("Vibrant cherry blossoms frame a snow-capped mountain rising in the background.")


// UIKit
let imageView = UIImageView(image: UIImage(named: landmark.backgroundImageName))
imageView.isAccessibilityElement = true
imageView.accessibilityLabel = "Vibrant cherry blossoms frame a snow-capped mountain rising in the background."
```

### Add alternate labels for Voice Control — [7:43]

```swift
// Add alternate labels for Voice Control

Button {
  addFavorite()
} label: {
  Image(systemName: "heart")
}
.accessibilityLabel("Favorite")
.accessibilityInputLabels(["Favorite", "Heart", "Like", "Love"])
```

### Set accessibility traits to match an element’s role — [8:23]

```swift
// Set accessibility traits to match an element’s role

// SwiftUI
Text("Accessibility Nutrition Labels")
  .font(.title)
  .accessibilityAddTraits(.isHeader)


// UIKit
let label = UILabel()
/*...*/
label.accessibilityTraits = .header
```

### Implement custom adjustable behavior — [9:29]

```swift
// Implement custom adjustable behavior

// SwiftUI
MySliderView()
  .accessibilityAdjustableAction { direction in
    switch direction {
    case .increment:
      // Increase value
    case .decrement:
      // Decrease value
    }
  }


// UIKit
class MySliderView: UIView {
  override var accessibilityTraits: UIAccessibilityTraits { get { .adjustable } set {} }
  override func accessibilityIncrement() { /* Increase value */ }
  override func accessibilityDecrement() { /* Decrease value */ }
}
```

### Set an accessibility value — [9:54]

```swift
// Set an accessibility value

// SwiftUI
MyView()
  .accessibilityValue("Value")


// UIKit
myView.accessibilityValue = "Value"
```

### Hide decorative images from VoiceOver — [12:26]

```swift
// Hide decorative images from VoiceOver

// SwiftUI
Image(decorative: landmark.thumbnailImageName)
/* or */
Image(landmark.thumbnailImageName)
  .accessibilityHidden(true)


// UIKit
imageView.isAccessibilityElement = false
```

### Combine elements to improve VoiceOver navigation — [12:59]

```swift
// Combine elements to improve VoiceOver navigation

HStack {
  HStack {
    Text("SFO")
    Image(systemName: "airplane.departure")
      .accessibilityLabel("to")
    Text("HND")
  }
  .font(.title3.bold())
  Spacer()
  VStack {
    Text("Arriving in")
    Text("15").font(.title.bold())
    Text("minutes")
  }
}
.accessibilityElement(children: .combine)
```

### Make a custom component accessible — [15:03]

```swift
// Make a custom component accessible

HStack {
  ForEach(1...5, id: \.self) { index in
    Image(systemName: index <= Int(badgeProgress.rating) ? "star.fill" : "star") 
  }
}
.accessibilityElement()
.accessibilityLabel("Rating")
.accessibilityValue("\(Int(badgeProgress.rating))")
.accessibilityAdjustableAction { direction in
  switch direction {
  case .increment:
    badgeProgress.rating = min(5, badgeProgress.rating + 1)
  case .decrement:
    badgeProgress.rating = max(0, badgeProgress.rating - 1)
  }
}
```

### Make a custom component accessible — [15:37]

```swift
// Make a custom component accessible

HStack {
  ForEach(1...5, id: \.self) { index in
    Image(systemName: index <= Int(badgeProgress.rating) ? "star.fill" : "star")
  }
}
.accessibilityRepresentation {
  Slider(value: $badgeProgress.rating, in: 0...5, step: 1.0) {
    Text("Rating")
  }
}
```

### Add accessibility traits for tap gestures — [16:30]

```swift
// Add accessibility traits for tap gestures

HStack {
  Text("Learn more")
  Image(systemName: "chevron.forward")
}
.foregroundColor(.blue)
.onTapGesture {
  /*...*/
}
.accessibilityAddTraits(.isButton)
```

### Add accessibility actions for custom gestures — [17:13]

```swift
// Add accessibility actions for custom gestures

Image(landmark.backgroundImageName)
  .accessibilityLabel(landmark.imageDescription ?? landmark.name)
  .onTapGesture(count: 2) {
    modelData.addFavorite(landmark)
  }
  .accessibilityAction(named: "Favorite") {
    modelData.addFavorite(landmark)
  }
```

### Adopt system text styles for automatic scaling — [20:07]

```swift
// Adopt system text styles for automatic scaling

// SwiftUI
Text("Hello World")
  .font(.body)


// UIKit
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true
```

### Make custom fonts scale proportionally with system font styles — [20:33]

```swift
// Make custom fonts scale proportionally with system font styles

// SwiftUI
Text("Hello World")
  .font(.custom("MyFont", size: 17, relativeTo: .body))


// UIKit
guard let customFont = UIFont(name: "MyFont", size: 17) else { return }
label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: customFont)
label.adjustsFontForContentSizeCategory = true
```

### Embed content in ScrollView to avoid truncation — [22:57]

```swift
// Embed content in ScrollView to avoid truncation

ScrollView {
  VStack(spacing: 24) {
    EarnedBadgeView(badge: badge)
    Text("Congratulations!")
    Text("...")
  }
}
.scrollBounceBehavior(.basedOnSize)
.safeAreaBar(edge: .bottom) {
    VStack {
        Button("Share badge") { }
        Button("Close") { }
    }
}
```

### Set number of lines to 0 to avoid truncation — [25:17]

```swift
// Set number of lines to 0 to avoid truncation

// SwiftUI

Text("Some longer text that takes up multiple lines.")
  .lineLimit(nil)


// UIKit

label.numberOfLines = 0
```

### Check the differentiate without color setting — [26:53]

```swift
// Check the differentiate without color setting

// SwiftUI

@Environment(\.accessibilityDifferentiateWithoutColor) var differentiateWithoutColor


// UIKit

let differentiateWithoutColor = UIAccessibility.shouldDifferentiateWithoutColor
NotificationCenter.default.addObserver(self, selector: #selector(diffWithoutColorDidChange), name: UIAccessibility.differentiateWithoutColorDidChangeNotification, object: nil)
```

### Differentiate without color alone in Swift Charts — [27:42]

```swift
// Differentiate without color alone in Swift Charts

Chart(visitorData) { data in
  LineMark(
    x: .value("Month", data.month),
    y: .value("Visitors", data.numVisitors)
  )
  .foregroundStyle(by: .value("Landmark", data.landmark))

  PointMark(
    x: .value("Month", data.month),
    y: .value("Visitors", data.numVisitors)
  )
  .foregroundStyle(by: .value("Landmark", data.landmark))
  .symbol(by: .value("Landmark", data.landmark))
}
```

### Check the preference for Reduce Transparency — [30:36]

```swift
// Check the preference for Reduce Transparency

// SwiftUI

@Environment(\.accessibilityReduceTransparency) var reduceTransparencyEnabled


// UIKit

let reduceTransparencyEnabled = UIAccessibility.isReduceTransparencyEnabled
NotificationCenter.default.addObserver(self, selector: #selector(reduceTransparencyDidChange), name: UIAccessibility.reduceTransparencyStatusDidChangeNotification, object: nil)
```

### Check the preference for Increase Contrast — [31:22]

```swift
// Check the preference for Increase Contrast

// SwiftUI

@Environment(\.colorSchemeContrast) var colorSchemeContrast


// UIKit

let increaseContrastEnabled = view.traitCollection.accessibilityContrast == .high
registerForTraitChanges([UITraitAccessibilityContrast.self], action: #selector(accessibilityContrastDidChange))
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111433/5/688d4ff2-043e-49bb-9d2d-c63b385b1b6e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111433/5/688d4ff2-043e-49bb-9d2d-c63b385b1b6e/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111433) — developer.apple.com. Indexed for agent consumption._
