---
id: "wwdc2021-10180"
event: "wwdc2021"
year: 2021
title: "Detect and diagnose memory issues"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10180"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Detect and diagnose memory issues

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10180](https://developer.apple.com/videos/play/wwdc2021/10180)

Discover how you can understand and diagnose memory performance problems with Xcode. We’ll take you through the latest updates to Xcode’s tools, explore Metrics, check out the memgraph collection feature in XCTest, and learn how to catch regressions using a Performance XCTest.


**Keywords:** `memory`, `performance`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,506 words)

## Documentation & Resources

- [Analyzing the performance of your shipping app](https://developer.apple.com/documentation/Xcode/analyzing-the-performance-of-your-shipping-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-the-performance-of-your-shipping-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-the-performance-of-your-shipping-app.json
- [Manual Memory Management](https://developer.apple.com/documentation/Swift/manual-memory-management) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/manual-memory-management
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/manual-memory-management.json
- [MetricKit](https://developer.apple.com/documentation/MetricKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit.json
- [XCTest](https://developer.apple.com/documentation/XCTest) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/XCTest
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/XCTest.json

## Code Snippets

### Monitor memory performance with XCTests — [4:52]

```swift
// Monitor memory performance with XCTests

func testSaveMeal() {
    let app = XCUIApplication()

    let options = XCTMeasureOptions()
    options.invocationOptions = [.manuallyStart]

    measure(metrics: [XCTMemoryMetric(application: app)],
            options: options) {

        app.launch()

        startMeasuring()

        app.cells.firstMatch.buttons["Save meal"].firstMatch.tap()

             let savedButton = app.cells.firstMatch.buttons["Saved"].firstMatch
        XCTAssertTrue(savedButton.waitForExistence(timeout: 30))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10180/5/0CD6241A-4A02-4CD3-9885-93ABE0FD4981/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10180/5/0CD6241A-4A02-4CD3-9885-93ABE0FD4981/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10180) — developer.apple.com. Indexed for agent consumption._