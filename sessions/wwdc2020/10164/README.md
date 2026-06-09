---
id: "wwdc2020-10164"
event: "wwdc2020"
year: 2020
title: "XCTSkip your tests"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10164"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# XCTSkip your tests

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10164](https://developer.apple.com/videos/play/wwdc2020/10164)

Get the test results that matter — and skip the ones that don’t. Discover how you can implement XCTSkip to conditionally avoid tests at runtime. We'll take you through how to return this new test result and better document tests beyond pass and fail within your test bundle.

To get the most out of this session, you should be familiar with XCTest and unit/UI testing. Watch “Testing in Xcode” for a primer.

Once you’ve learned about XCTSkip, learn more about improvements in testing: Watch "Triage test failures with XCTIssue", "Handle interruptions and alerts in UI tests", "Get your test results faster", and "Eliminate animation hitches with XCTest".

To learn how to improve your testing suites, check out "Write tests to fail".

**Keywords:** `continuous integration`, `testing`, `test result`, `xcode`, `xct`, `xctest`, `xctskip`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(999 words)

## Code Snippets

### Use XCTSkipUnless to bypass a test on devices other than iPad — [5:45]

```swift
func testExample() throws {

    /// Example usage: skip test if device is not an iPad
    try XCTSkipUnless(UIDevice.current.userInterfaceIdiom == .pad, 
              "Pointer interaction tests are for iPad only")

    // test...
}
```

### Use guard+XCTSkip to bypass a test on an older OS version — [5:58]

```swift
func testExample() throws {

    /// Example usage: skip test if OS version is older than iOS 13.4
    guard #available(iOS 13.4, *) else {
        throw XCTSkip("Pointer interaction tests can only run on iOS 13.4+")

    // test...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10164/4/3A9C343F-42ED-48B9-B8CA-D9645E719CFB/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10164) — developer.apple.com. Indexed for agent consumption._