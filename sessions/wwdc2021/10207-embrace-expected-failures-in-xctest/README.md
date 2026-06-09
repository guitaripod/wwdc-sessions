---
id: "wwdc2021-10207"
event: "wwdc2021"
year: 2021
title: "Embrace Expected Failures in XCTest"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10207"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Embrace Expected Failures in XCTest

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10207](https://developer.apple.com/videos/play/wwdc2021/10207)

Testing is a crucial part of building a great app: Great tests can help you track down important issues before release, improve your workflow, and provide a quality experience upon release. For issues that can’t be immediately resolved, however, XCTest can help provide better context around those problems with XCTExpectFailure. Learn how this API works, its strict behavior, and how to improve the signal-to-noise ratio in your tests to identify new issues more efficiently.

**Keywords:** `expected failure`, `test failure`, `xctest`, `xctexpectfailure`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,742 words)

## Documentation & Resources

- [Expected Failures](https://developer.apple.com/documentation/XCTest/expected-failures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/XCTest/expected-failures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/XCTest/expected-failures.json

## Code Snippets

### XCTSkip unless device is iPad — [3:31]

```swift
try XCTSkipUnless(UIDevice.current.userInterfaceIdiom == .pad, "Only supported on iPad")
```

### XCTExpectFailure — [4:31]

```swift
XCTExpectFailure("<https://dev.myco.com/bugs/4923> myValidationFunction is returning false")
```

### Scoped XCTExpectFailure — [7:14]

```swift
XCTExpectFailure("<https://dev.myco.com/bugs/4923> fix myValidationFunction") {
    XCTAssert(myValidationFunction())
}
```

### XCTExpectFailure with issue matcher — [8:34]

```swift
let options = XCTExpectedFailure.Options()
options.issueMatcher = { issue in
    return issue.type == .assertionFailure
}

XCTExpectFailure("<https://dev.myco.com/bugs/4923> fix myValidationFunction", options: options)
```

### Disable XCTExpectFailure for some platforms — [9:03]

```swift
let options = XCTExpectedFailure.Options()
#if os(macOS)
options.isEnabled = false
#endif

XCTExpectFailure("<https://dev.myco.com/bugs/4923> fix myValidationFunction", options: options) {
    XCTAssert(myValidationFunction())
}
```

### Disable strict XCTExpectFailure behavior via options — [10:39]

```swift
let options = XCTExpectedFailure.Options()
options.isStrict = false

XCTExpectFailure("<https://dev.myco.com/bugs/4923> fix myValidationFunction", options: options) {
    XCTAssert(myValidationFunction())
}
```

### Disable strict XCTExpectFailure behavior via parameter — [10:53]

```swift
XCTExpectFailure("<https://dev.myco.com/bugs/4923> fix myValidationFunction", strict: false) {
    XCTAssert(myValidationFunction())
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10207/5/1AF9A073-9D29-4091-9876-AE8868480EDA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10207/5/1AF9A073-9D29-4091-9876-AE8868480EDA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10207) — developer.apple.com. Indexed for agent consumption._
