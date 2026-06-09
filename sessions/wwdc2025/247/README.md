---
id: "wwdc2025-247"
event: "wwdc2025"
year: 2025
title: "What’s new in Xcode 26"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/247"
topics: ["Design", "Swift", "SwiftUI & UI Frameworks", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Xcode 26

**Event:** WWDC25 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-247](https://developer.apple.com/videos/play/wwdc2025/247)

Discover the latest productivity and performance advancements in Xcode 26. Learn how to leverage large language models in your development workflow. Explore editing and debugging enhancements, improved performance and testing tools, and Swift Build - the open-source build system engine used by Xcode.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,683 words)

## Documentation & Resources

- [Analyzing CPU usage with the Processor Trace instrument](https://developer.apple.com/documentation/Xcode/analyzing-cpu-usage-with-processor-trace) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-cpu-usage-with-processor-trace
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-cpu-usage-with-processor-trace.json
- [Measuring your app’s power use with Power Profiler](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler.json
- [Enabling enhanced security for your app](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/enabling-enhanced-security-for-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/enabling-enhanced-security-for-your-app.json
- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/Xcode/understanding-and-improving-swiftui-performance) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/understanding-and-improving-swiftui-performance
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/understanding-and-improving-swiftui-performance.json
- [Xcode updates](https://developer.apple.com/documentation/Updates/Xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Xcode.json

## Code Snippets

### Using Playgrounds — [5:25]

```swift
import Playgrounds
```

### Using Playgrounds — [5:30]

```swift
#Playground {

}
```

### Using Playgrounds — [5:37]

```swift
let landmark = Landmark.exampleData.first
```

### Using Playgrounds — [6:10]

```swift
let region = landmark?.coordinateRegion
```

### Regex to scan for floating point numbers — [6:33]

```swift
func scanForFloatingPointNumbers() -> [Regex<Substring>.Match] {
    return self.matches(of: /[0-9]*[.][0-9]+/)
}
```

### Adding another playground — [6:42]

```swift
#Playground {

}
```

### Adding another playground — [6:49]

```swift
let string = "lon: -113.16096, lat: 36.21904"
let longitude = string.scanForFloatingPointNumbers().first
let latitude = string.scanForFloatingPointNumbers().last
```

### Updated regular expression — [7:33]

```swift
func scanForFloatingPointNumbers() -> [Regex<Substring>.Match] {
    return self.matches(of: /[+-]?[0-9]*[.][0-9]+/)
}
```

### Checking for camera authorization — [18:49]

```swift
// Checking for camera authorization

var isCameraAuthorized: Bool {
    get async {
        let status = AVCaptureDevice.authorizationStatus(for: .video)

        // Determine if the user previously authorized camera access.
        var isAuthorized = status == .authorized

        // If the system hasn't determined the user's authorization status,
        // explicitly prompt them for approval.
        if status == .notDetermined {
            isAuthorized = await AVCaptureDevice.requestAccess(for: .video)
        }

        return isAuthorized
    }
}
```

### Test scrolling animation performance with XCTHitchMetric — [34:40]

```swift
// XCTHitchMetric

func testScrollingAnimationPerformance() throws {
    // Custom performance test measure options.
    let measureOptions = XCTMeasureOptions()
    measureOptions.invocationOptions = .manuallyStop

    // App being tested.
    let app = XCUIApplication()

    // Launch app and get reference to scroll view.
    app.launch()
    let scrollView = app.scrollViews.firstMatch

    measure(metrics: [XCTHitchMetric(application: app)], options: measureOptions) {
        scrollView.swipeUp(velocity: .fast)
        stopMeasuring()
        scrollView.swipeDown(velocity: .fast)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/247/5/5455d9cc-d071-4119-84e7-db8eadeaaeb0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/247/5/5455d9cc-d071-4119-84e7-db8eadeaaeb0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/247) — developer.apple.com. Indexed for agent consumption._