---
id: "wwdc2023-10035"
event: "wwdc2023"
year: 2023
title: "Perform accessibility audits for your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10035"
topics: ["Developer Tools", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Perform accessibility audits for your app

**Event:** WWDC23 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10035](https://developer.apple.com/videos/play/wwdc2023/10035)

Discover how you can test your app for accessibility with every build. Learn how to perform automated audits for accessibility using XCTest and find out how to interpret the results. We’ll also share enhancements to the accessibility API that can help you improve UI test coverage.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,025 words)

## Documentation & Resources

- [XCUIApplication](https://developer.apple.com/documentation/XCUIAutomation/XCUIApplication) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/XCUIAutomation/XCUIApplication
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/XCUIAutomation/XCUIApplication.json

## Code Snippets

### Add an accessibility audit to a UI test — [2:52]

```swift
func testAccessibility() throws {
    let app = XCUIApplication()
    app.launch()

    try app.performAccessibilityAudit()
}
```

### Customize elements available to assistive technologies — [8:40]

```swift
view.accessibilityElements = [quoteTextView, newQuoteButton]
```

### Filter specific issues from accessibility audits — [9:57]

```swift
try app.performAccessibilityAudit(for: [.dynamicType, .contrast]) { issue in
    var shouldIgnore = false

    // ignore contrast issue on "My Label"
    if let element = issue.element, 
       element.label == "My Label",
       issue.auditType == .contrast {
           shouldIgnore = true
    }
    return shouldIgnore
}
```

### Customize automation elements available to UI tests — [14:07]

```swift
view.automationElements = [imageView, quoteTextView, newQuoteButton]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10035/5/AE94C37D-A130-4B28-987C-ADEA8AC1BEA8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10035/5/AE94C37D-A130-4B28-987C-ADEA8AC1BEA8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10035) — developer.apple.com. Indexed for agent consumption._
