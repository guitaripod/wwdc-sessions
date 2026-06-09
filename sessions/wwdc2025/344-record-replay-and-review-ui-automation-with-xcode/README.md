---
id: "wwdc2025-344"
event: "wwdc2025"
year: 2025
title: "Record, replay, and review: UI automation with Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/344"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Record, replay, and review: UI automation with Xcode

**Event:** WWDC25 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-344](https://developer.apple.com/videos/play/wwdc2025/344)

Learn to record, run, and maintain XCUIAutomation tests in Xcode. Replay your XCTest UI tests in dozens of locales, device types, and system conditions using test plan configurations. Review your test results using the Xcode test report, and download screenshots and videos of your runs. We’ll also cover best practices for preparing your app for automation with Accessibility and writing stable, high-quality automation code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,916 words)

## Documentation & Resources

- [Performing accessibility testing for your app](https://developer.apple.com/documentation/Accessibility/performing-accessibility-testing-for-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/performing-accessibility-testing-for-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/performing-accessibility-testing-for-your-app.json
- [Improving code assessment by organizing tests into test plans](https://developer.apple.com/documentation/Xcode/organizing-tests-to-improve-feedback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/organizing-tests-to-improve-feedback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/organizing-tests-to-improve-feedback.json
- [Delivering an exceptional accessibility experience](https://developer.apple.com/documentation/Accessibility/delivering_an_exceptional_accessibility_experience) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/delivering_an_exceptional_accessibility_experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/delivering_an_exceptional_accessibility_experience.json

## Code Snippets

### Adding accessibility identifiers in SwiftUI — [7:52]

```swift
// Adding accessibility identifiers in SwiftUI
import SwiftUI

struct LandmarkDetailView: View {
  let landmark: Landmark
  var body: some View {
    VStack {
      Image(landmark.backgroundImageName)
        .accessibilityIdentifier("LandmarkImage-\(landmark.id)")

      Text(landmark.description)
        .accessibilityIdentifier("LandmarkDescription-\(landmark.id)")
    }
  }
}
```

### Adding accessibility identifiers in UIKit — [8:19]

```swift
// Adding accessibility identifiers in UIKit
import UIKit

struct LandmarksListViewController: UIViewController {
  let landmarks: [Landmark] = [landmarkGreatBarrier, landmarkCairo]

  override func viewDidLoad() {
    super.viewDidLoad()

    for landmark in landmarks {
      let button = UIButton(type: .custom)
      setupButtonView()

      button.accessibilityIdentifier = "LandmarkButton-\(landmark.id)"

      view.addSubview(button)
    }
  }
}
```

### Best practice: Prefer accessibility identifiers over localized strings — [13:54]

```swift
// Example SwiftUI view
struct CollectionDetailDisplayView: View {
  var body: some View {
    ScrollView {
      Text(collection.name)
        .font(.caption)
        .accessibilityIdentifier("Collection-\(collection.id)")
    }
  }
}

// Example of a worse XCUIElementQuery
XCUIApplication().staticTexts["Max's Australian Adventure"]

// Example of a better XCUIElementQuery
XCUIApplication().staticTexts["Collection-1"]
```

### Best practice: Keep queries as concise as possible — [14:09]

```swift
// Example SwiftUI view
struct CollectionDetailDisplayView: View {
  var body: some View {
    ScrollView {
      Text(collection.name)
        .font(.caption)
        .accessibilityIdentifier("Collection-\(collection.id)")
    }
  }
}

// Example of a worse XCUIElementQuery
XCUIApplication().scrollViews.staticTexts["Collection-1"]

// Example of a better XCUIElementQuery
XCUIApplication().staticTexts["Collection-1"]
```

### Best practice: Prefer generic queries for dynamic content — [14:21]

```swift
// Example SwiftUI view
struct CollectionDetailDisplayView: View {
  var body: some View {
    ScrollView {
      Text(collection.name)
        .font(.caption)
        .accessibilityIdentifier("Collection-\(collection.id)")
    }
  }
}

// Example of a worse XCUIElementQuery
XCUIApplication().staticTexts["Max's Australian Adventure"]

// Example of a better XCUIElementQuery
XCUIApplication().staticTexts.firstMatch
```

### Add validations to a test case — [15:49]

```swift
// Add validations to the test case
import XCTest

class LandmarksUITests: XCTestCase {

  func testGreatBarrierAddedToFavorites() {
    let app = XCUIApplication()
    app.launch()
    app.cells["Landmark-186"].tap()
    XCTAssertTrue(
      app.staticTexts["Landmark-186"].waitForExistence(timeout: 10.0)),
      "Great Barrier exists"
    )

    let favoriteButton = app.buttons["Favorite"]
    favoriteButton.tap()
    XCTAssertTrue(
      favoriteButton.wait(for: \.value, toEqual: true, timeout: 10.0),
      "Great Barrier is a favorite"
    )
  }
}
```

### Set up your device for test execution — [16:36]

```swift
// Set up your device for test execution
import XCTest
import CoreLocation

class LandmarksUITests: XCTestCase {

  override func setUp() {
    continueAfterFailure = false

    XCUIDevice.shared.orientation = .portrait
    XCUIDevice.shared.appearance = .light

    let simulatedLocation = CLLocation(latitude: 28.3114, longitude: -81.5535)
    XCUIDevice.shared.location = XCUILocation(location: simulatedLocation)
  }

}
```

### Launch your app with environment variables and arguments — [16:54]

```swift
// Launch your app with environment variables and arguments
import XCTest

class LandmarksUITests: XCTestCase {

  func testLaunchWithDefaultCollection() {
    let app = XCUIApplication()
    app.launchArguments = ["ClearFavoritesOnLaunch"]
    app.launchEnvironment = ["DefaultCollectionName": "Australia 🐨 🐠"]
    app.launch()

    app.tabBars.buttons["Collections"].tap()
    XCTAssertTrue(app.buttons["Australia 🐨 🐠"].waitForExistence(timeout: 10.0))
  }
}
```

### Launch your app using custom URL schemes — [17:04]

```swift
// Launch your app using custom URL schemes
import XCTest

class LandmarksUITests: XCTestCase {

  func testOpenGreatBarrier() {
    let app = XCUIApplication()
    let customURL = URL(string: "landmarks://great-barrier")!
    app.open(customURL)

    XCTAssertTrue(app.wait(for: .runningForeground, timeout: 10.0))
    XCTAssertTrue(app.staticTexts["Great Barrier Reef"].waitForExistence(timeout: 10.0))
  }
}
```

### Launch your app using custom URL schemes and the system default app — [17:12]

```swift
// Launch your app using custom URL schemes
import XCTest

class LandmarksUITests: XCTestCase {

  func testOpenGreatBarrier() {
    let app = XCUIApplication()
    let customURL = URL(string: "landmarks://great-barrier")!
    XCUIDevice.shared.system.open(customURL)

    XCTAssertTrue(app.wait(for: .runningForeground, timeout: 10.0))
    XCTAssertTrue(app.staticTexts["Great Barrier Reef"].waitForExistence(timeout: 10.0))
  }
}
```

### Perform an accessibility audit during an automation — [17:13]

```swift
// Perform an accessibility audit during an automation
import XCTest

class LandmarksUITests: XCTestCase {

  func testPerformAccessibilityAudit() {
    let app = XCUIApplication()
    try app.performAccessibilityAudit()
  }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/344/6/d83ce906-0fb6-484b-a0f2-4f678161d5b8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/344/6/d83ce906-0fb6-484b-a0f2-4f678161d5b8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/344) — developer.apple.com. Indexed for agent consumption._
