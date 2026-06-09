---
id: "wwdc2020-10077"
event: "wwdc2020"
year: 2020
title: "Eliminate animation hitches with XCTest"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10077"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Eliminate animation hitches with XCTest

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10077](https://developer.apple.com/videos/play/wwdc2020/10077)

Animations can dramatically enhance the user experience of your app, provide a sense of direct manipulation, and help people to better understand the results of their actions. Animation hitches can break that experience. Discover how to use XCTest to detect interruptions to smooth scrolling and animations, and learn how to catch regressions before they affect the people relying on your app.

**Keywords:** `animate`, `battery`, `energy`, `metrics`, `performance`, `scroll`, `xcode`, `xctest`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,089 words)

## Code Snippets

### Create an animation os_signpost interval — [6:35]

```swift
os_signpost(.animationBegin, log: logHandle, name: "performAnimationInterval")
os_signpost(.end, log: logHandle, name: "performAnimationInterval")
```

### Use a UIKit instrumented animation os_signpost interval — [6:55]

```swift
extension XCTOSSignpostMetric {
     open class var navigationTransitionMetric: XCTMetric { get }
     open class var customNavigationTransitionMetric: XCTMetric { get }
     open class var scrollDecelerationMetric: XCTMetric { get }
     open class var scrollDraggingMetric: XCTMetric { get }
}
```

### Measure scrolling animation performance using a Performance XCTest — [7:12]

```swift
// Measure scrolling animation performance using a Performance XCTest
func testScrollingAnimationPerformance() throws {
    app.launch()
    app.staticTexts["Meal Planner"].tap()
    let foodCollection = app.collectionViews.firstMatch

    measure(metrics: [XCTOSSignpostMetric.scrollDecelerationMetric]) {
        foodCollection.swipeUp(velocity: .fast)
    }
}
```

### Reset the application state between runs — [8:02]

```swift
func testScrollingAnimationPerformance() throws { 
    app.launch()
    app.staticTexts["Meal Planner"].tap()
    let foodCollection = app.collectionViews.firstMatch

    let measureOptions = XCTMeasureOptions()
    measureOptions.invocationOptions = [.manuallyStop]

    measure(metrics: [XCTOSSignpostMetric.scrollDecelerationMetric],
            options: measureOptions) {
        foodCollection.swipeUp(velocity: .fast)
        stopMeasuring()
        foodCollection.swipeDown(velocity: .fast)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10077/2/B3286370-EF32-46C5-AF96-8EF51A8EB971/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10077) — developer.apple.com. Indexed for agent consumption._
