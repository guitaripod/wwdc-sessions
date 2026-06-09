---
id: "wwdc2023-10034"
event: "wwdc2023"
year: 2023
title: "Create accessible spatial experiences"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10034"
topics: ["Spatial Computing", "Accessibility & Inclusion"]
platforms: ["visionOS"]
hasTranscript: true
---

# Create accessible spatial experiences

**Event:** WWDC23 · **Topic:** Accessibility & Inclusion · **Platforms:** visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10034](https://developer.apple.com/videos/play/wwdc2023/10034)

Learn how you can make spatial computing apps that work well for everyone. Like all Apple platforms, visionOS is designed for accessibility: We’ll share how we’ve reimagined assistive technologies like VoiceOver and Pointer Control and designed features like Dwell Control to help people interact in the way that works best for them. Learn best practices for vision, motor, cognitive, and hearing accessibility and help everyone enjoy immersive experiences for visionOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,837 words)

## Documentation & Resources

- [Diorama](https://developer.apple.com/documentation/visionOS/diorama) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/diorama
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/diorama.json
- [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionOS/improving-accessibility-support-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/improving-accessibility-support-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/improving-accessibility-support-in-your-app.json
- [UIAccessibility](https://developer.apple.com/documentation/UIKit/UIAccessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIAccessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIAccessibility.json
- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json
- [Media Accessibility](https://developer.apple.com/documentation/MediaAccessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MediaAccessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MediaAccessibility.json

## Code Snippets

### Use AccessibilityComponent with RealityKit — [5:28]

```swift
var accessibilityComponent = AccessibilityComponent()
accessibilityComponent.isAccessibilityElement = true
accessibilityComponent.traits = [.button, .playsSound]
accessibilityComponent.label = "Cloud"
accessibilityComponent.value = "Grumpy"
cloud.components[AccessibilityComponent.self] = accessibilityComponent

// ...

var isHappy: Bool {
    didSet {
        cloudEntities[id].accessibilityValue = isHappy ? "Happy" : "Grumpy"
    }
}
```

### Add an activate action — [8:04]

```swift
var accessibilityComponent = AccessibilityComponent()
accessibilityComponent.isAccessibilityElement = true
accessibilityComponent.traits = [.button, .playsSound]
accessibilityComponent.label = "Cloud"
accessibilityComponent.value = "Grumpy"
accessibilityComponent.systemActions = [.activate]
cloud.components[AccessibilityComponent.self] = accessibilityComponent

// ...

content.subscribe(to: AccessibilityEvents.Activate.self, componentType: nil) { activation in
    handleCloudCollision(for: activation.entity, gameModel: gameModel)
}
```

### Announce meaningful events and changes in context — [9:23]

```swift
AccessibilityNotification.Announcement("8 clouds in front of you").post()
```

### Provide alternatives to head anchored content — [13:15]

```swift
// SwiftUI
@Environment(\.accessibilityPrefersHeadAnchorAlternative)
private var accessibilityPrefersHeadAnchorAlternative

// UIKit
AXPrefersHeadAnchorAlternative()
NSNotification.Name.AXPrefersHeadAnchorAlternativeDidChange
```

### Provide alternatives when Reduce Motion is enabled — [15:04]

```swift
// SwiftUI
@Environment(\.accessibilityReduceMotion)
private var accessibilityReduceMotion

// UIKit
UIAccessibility.isReduceMotionEnabled
UIAccessibility.reduceMotionStatusDidChangeNotification
```

### Check whether captions are enabled — [23:35]

```swift
UIAccessibility.isClosedCaptioningEnabled
UIAccessibility.closedCaptioningStatusDidChangeNotification
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10034/5/DF004F28-FE27-41BB-B1BB-4CF81F3F2695/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10034/5/DF004F28-FE27-41BB-B1BB-4CF81F3F2695/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10034) — developer.apple.com. Indexed for agent consumption._
