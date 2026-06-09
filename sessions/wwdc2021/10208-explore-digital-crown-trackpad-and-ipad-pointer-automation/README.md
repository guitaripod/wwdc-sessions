---
id: "wwdc2021-10208"
event: "wwdc2021"
year: 2021
title: "Explore Digital Crown, Trackpad, and iPad pointer automation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10208"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore Digital Crown, Trackpad, and iPad pointer automation

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10208](https://developer.apple.com/videos/play/wwdc2021/10208)

Learn how you can interact with devices in UI Tests in Xcode 13. Discover newly-automatable input methods including iPadOS pointer, watchOS Digital Crown, and enhanced macOS trackpad scrolling APIs.

**Keywords:** `digital crown`, `interaction`, `interaction tests`, `pointer`, `pointer events`, `scroll`, `testing`, `trackpad`, `ui testing`, `xcuitest`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,154 words)

## Code Snippets

### New supportsPointerInteraction property on XCUIDevice — [1:28]

```swift
extension XCUIDevice {

  public var supportsPointerInteraction: Bool

}
```

### New methods on XCUIElement and XCUICoordinate for pointer interactions on iOS — [1:37]

```swift
extension XCUIElement {
  open func hover()

  open func click()

  open func rightClick()

  open func doubleClick()

  open func scroll(byDeltaX: CGFloat, deltaY: CGFloat)

  open func click(forDuration: TimeInterval, thenDragToElement: XCUIElement)

  open func click(forDuration: TimeInterval, thenDragToElement: XCUIElement,
                  withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)

  open class func perform(withKeyModifiers flags: XCUIElement.KeyModifiers,
                          block: () -> Void)
}
```

### Empty UI test class — [2:31]

```swift
import XCTest

class Pointer_UI_Tests: XCTestCase {



}
```

### UI test for opening the sidebar with a two-finger horizontal trackpad swipe — [2:43]

```swift
import XCTest

class Pointer_UI_Tests: XCTestCase {

  @available(iOS 15.0, *)
  func testHorizontalScrollRevealsSidebar() throws {
    let app = XCUIApplication()
    app.launch()

    let sidebar = app.tables["Sidebar"]

    // Make sure sidebar menu is not present initially.
    XCTAssertFalse(sidebar.exists, "Sidebar should not be present initially")

    // Swipe horizontally to reveal sidebar.
    app.staticTexts["Select a smoothie"].scroll(byDeltaX: -200, deltaY: 0)

    // Verify sidebar is now present.
    XCTAssertTrue(sidebar.waitForExistence(timeout: 5),
                  "Sidebar did not appear within 5 second timeout")
  }

}
```

### Use the new supportsPointerInteraction property to skip the test on devices that don't support pointer interaction — [4:36]

```swift
import XCTest

class Pointer_UI_Tests: XCTestCase {

  @available(iOS 15.0, *)
  func testHorizontalScrollRevealsSidebar() throws {
    try XCTSkipUnless(XCUIDevice.shared.supportsPointerInteraction,
                      "Device does not support pointer interaction")

    let app = XCUIApplication()
    app.launch()

    let sidebar = app.tables["Sidebar"]

    // Make sure sidebar menu is not present initially.
    XCTAssertFalse(sidebar.exists, "Sidebar should not be present initially")

    // Swipe horizontally to reveal sidebar.
    app.staticTexts["Select a smoothie"].scroll(byDeltaX: -200, deltaY: 0)

    // Verify sidebar is now present.
    XCTAssertTrue(sidebar.waitForExistence(timeout: 5),
                  "Sidebar did not appear within 5 second timeout")
  }

}
```

### New method on XCUIDevice for Digital Crown rotation on watchOS — [5:27]

```swift
// New rotateDigitalCrown API

extension XCUIDevice {

  open func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity = .default)

}
```

### UI test to verify the app's Digital Crown rotation functionality behaves as expected — [6:22]

```swift
// Example use of watchOS Digital Crown API

func testForecastScrolling() {
  let app = XCUIApplication()
  app.launch()

  let forecastTime = app.staticTexts["forecast-time"]

  XCTAssertEqual(forecastTime.label, "Current Temperature")

  // Scroll 1 full rotation forward.
  XCUIDevice.shared.rotateDigitalCrown(delta: 1.0)
  XCTAssertEqual(forecastTime.label, "One hour from now")

  // Scroll 2 full rotations backward.
  XCUIDevice.shared.rotateDigitalCrown(delta: -2.0)
  XCTAssertEqual(forecastTime.label, "One hour ago")
}
```

### Existing API for performing discrete (mouse wheel-like) scrolling on macOS — [7:46]

```swift
extension XCUIElement {

  // Use the existing API for discrete (mouse wheel-like) scrolling.
  open func scroll(byDeltaX: CGFloat, deltaY: CGFloat)

}
```

### New API for performing continuous (trackpad-like) scrolling on macOS — [8:05]

```swift
extension XCUIElement {

  // Use the new API for continuous (trackpad-like) scrolling.
  open func swipeUp(velocity: XCUIGestureVelocity = .default)
  open func swipeDown(velocity: XCUIGestureVelocity = .default)
  open func swipeLeft(velocity: XCUIGestureVelocity = .default)
  open func swipeRight(velocity: XCUIGestureVelocity = .default)

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10208/7/D03FEAA6-4A84-48E0-BC4B-0B194701D23A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10208/7/D03FEAA6-4A84-48E0-BC4B-0B194701D23A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10208) — developer.apple.com. Indexed for agent consumption._
