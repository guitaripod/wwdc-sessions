---
id: "wwdc2021-10181"
event: "wwdc2021"
year: 2021
title: "Ultimate application performance survival guide"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10181"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Ultimate application performance survival guide

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10181](https://developer.apple.com/videos/play/wwdc2021/10181)

Performance optimization can seem like a daunting task — with many metrics to track and tools to use. Fear not: Our survival guide to app performance is here to help you understand tooling, metrics, and paradigms that can help smooth your development process and contribute to a great experience for people using your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,823 words)

## Documentation & Resources

- [Analyzing the performance of your shipping app](https://developer.apple.com/documentation/Xcode/analyzing-the-performance-of-your-shipping-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-the-performance-of-your-shipping-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-the-performance-of-your-shipping-app.json
- [Improving app responsiveness](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/improving-app-responsiveness
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/improving-app-responsiveness.json
- [MetricKit](https://developer.apple.com/documentation/MetricKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit.json
- [App Store Connect API](https://developer.apple.com/documentation/AppStoreConnectAPI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppStoreConnectAPI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppStoreConnectAPI.json
- [XCTest](https://developer.apple.com/documentation/XCTest) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/XCTest
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/XCTest.json

## Code Snippets

### Using MetricKit — [5:46]

```swift
class AppMetrics: MXMetricManagerSubscriber {
	init() {
		let shared = MXMetricManager.shared
		shared.add(self)
	}

	deinit {
		let shared = MXMetricManager.shared
		shared.remove(self)
	}

	// Receive daily metrics
	func didReceive(_ payloads: [MXMetricPayload]) {
		// Process metrics
	}

	// Receive diagnostics
	func didReceive(_ payloads: [MXDiagnosticPayload]) {
		// Process metrics
	}
}
```

### Testing Scroll performance — [10:29]

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

### Using mxSignpostAnimationIntervalBegin — [11:53]

```swift
func startAnimating() {
	// Mark the beginning of animations
	mxSignpostAnimationIntervalBegin(
		log: MXMetricManager.makeLogHandle(category: "animation_telemetry"), 
		name: "custom_animation”)
	}

	func animationDidComplete() {
	// Mark the end of the animation to receive the collected hitch rate telemetry
	mxSignpost(OSSignpostType.end, 
		log: MXMetricManager.makeLogHandle(category: "animation_telemetry"), 
		name: "custom_animation")
}
```

### Using XCTest to Measure Disk Usage — [13:51]

```swift
// Example performance XCTest

func testSaveMeal() {
	let app = XCUIApplication()
	let options = XCTMeasureOptions()
	options.invocationOptions = [.manuallyStart]

	measure(metrics: [XCTStorageMetric(application: app)], options: options) {
		app.launch()
		startMeasuring()

		let firstCell = app.cells.firstMatch
		firstCell.buttons["Save meal"].firstMatch.tap()

		let savedButton = firstCell.buttons["Saved"].firstMatch
		XCTAssertTrue(savedButton.waitForExistence(timeout: 2))
	}
}
```

### Collect memory telemetry — [21:19]

```swift
// Collect memory telemetry

func saveAppAssets() {
	mxSignpost(OSSignpostType.begin, 
		log: MXMetricManager.makeLogHandle(category: "memory_telemetry"), 
		name: "custom_memory")

	// save app metadata

	mxSignpost(OSSignpostType.end, 
		log: MXMetricManager.makeLogHandle(category: "memory_telemetry"), 
		name: "custom_memory")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10181/11/A69D2FCC-21C3-4392-B857-552EF73E7714/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10181/11/A69D2FCC-21C3-4392-B857-552EF73E7714/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10181) — developer.apple.com. Indexed for agent consumption._
