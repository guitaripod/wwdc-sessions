---
id: "wwdc2023-10158"
event: "wwdc2023"
year: 2023
title: "Animate with springs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10158"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Animate with springs

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10158](https://developer.apple.com/videos/play/wwdc2023/10158)

Discover how you can bring life to your app with animation! We’ll show you how to create amazing animations when you take advantage of springs and help you learn how to use them in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,626 words)

## Code Snippets

### Spring Preset — [18:00]

```swift
withAnimation(.snappy) {
  // Changes
}
```

### Spring Preset with Custom Duration — [18:15]

```swift
withAnimation(.snappy(duration: 0.4)) {
  // Changes
}
```

### Spring Preset with Custom Bounce — [18:21]

```swift
withAnimation(.snappy(extraBounce: 0.1)) {
  // Changes
}
```

### Custom Spring — [18:37]

```swift
withAnimation(.spring(duration: 0.6, bounce: 0.2)) {
  // Changes
}

// UIKit
UIView.animate(duration: 0.6, bounce: 0.2) {
  // Changes
}

// Core Animation
let animation = CASpringAnimation(perceptualDuration: 0.6, bounce: 0.2)
```

### Spring Model — [18:57]

```swift
let mySpring = Spring(duration: 0.5, bounce: 0.2)
let (mass, stiffness, damping) = (mySpring.mass, mySpring.stiffness, mySpring.damping)
```

### Spring Model Animation — [19:16]

```swift
let otherSpring = Spring(mass: 1, stiffness: 100, damping: 10)
withAnimation(.spring(otherSpring)) {
    // Changes
}
```

### Spring Parameter Conversion — [19:26]

```markdown
mass = 1

stiffness = (2π ÷ duration)^2

damping = 1 - 4π × bounce ÷ duration, bounce ≥ 0
          4π ÷ (duration + 4π × bounce), bounce < 0
```

### Evaluating Spring Model — [19:35]

```swift
let mySpring = Spring(duration: 0.4, bounce: 0.2)
let value = mySpring.value(target: 1, time: time)
let velocity = mySpring.velocity(target: 1, time: time)
```

### Custom Spring Animation — [20:15]

```swift
func animate<V: VectorArithmetic>(
    value: V, time: Double, context: inout AnimationContext<V>
) -> V? {
    spring.value(
        target: value, initialVelocity: context.initialVelocity,
        time: effectiveTime(time: time, context: context))
}
```

### Spring with No Bounce — [20:34]

```swift
withAnimation(.spring(duration: 0.5)) {
    isActive.toggle()
}
```

### Spring with Small Bounce — [21:07]

```swift
withAnimation(.spring(duration: 0.5, bounce: 0.15)) {
    isActive.toggle()
}
```

### Spring with Large Bounce — [21:14]

```swift
withAnimation(.spring(duration: 0.5, bounce: 0.3)) {
    isActive.toggle()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10158/4/0BAD22E7-61F5-4C4C-BA74-61BF66E8A9B1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10158/4/0BAD22E7-61F5-4C4C-BA74-61BF66E8A9B1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10158) — developer.apple.com. Indexed for agent consumption._
