---
id: "wwdc2020-10687"
event: "wwdc2020"
year: 2020
title: "Triage test failures with XCTIssue"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10687"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Triage test failures with XCTIssue

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10687](https://developer.apple.com/videos/play/wwdc2020/10687)

Put your test failures to work: Learn how to triage and diagnose uncaught issues in your app using the latest testing APIs in Xcode. We’ll show you how to help ease your testing workflow and put failures into context to help you deliver the best quality product. For more information on designing your tests to improve triaging, see “Write tests to fail.” And check out the latest improvements to Xcode’s testing workflow by watching “Get your test results faster”, “Handle interruptions and alerts in UI tests”, and “XCTSkip your tests.”

**Keywords:** `test`, `test failure`, `testing`, `xcode`, `xctest`, `xctissue`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,019 words)

## Code Snippets

### Implement a custom test assertion using XCTIssue — [9:52]

```swift
func assertSomething(about data: Data,
                         file: StaticString = #filePath,
                         line: UInt = #line) {

        // Call out to custom validation function.
        if !isValid(data) {

            // Create issue, declare with var for mutability.
            var issue = XCTIssue(type: .assertionFailure, compactDescription: "Invalid data")

            // Attach the invalid data.
            issue.add(XCTAttachment(data: data))

            // Capture the call site location as the point of failure.
            let location = XCTSourceCodeLocation(filePath: file, lineNumber: line)
            issue.sourceCodeContext = XCTSourceCodeContext(location: location)

            // Record the issue.
            self.record(issue)
        }
    }
```

### Override record(_ issue:) for observation — [11:12]

```swift
override func record(_ issue: XCTIssue) {

    // Observe, introspect, log, etc.:
    if shouldLog(issue) {
        print("I just observed an issue!")
    }

    // Don't forget to call super!
    super.record(issue)
}
```

### Override record(_ issue:) to suppress failures — [11:30]

```swift
override func record(_ issue: XCTIssue) {

    // If you don't want to record it, just return.
    if shouldSuppress(issue) {
        return
    }

    // Otherwise pass it to super.
    super.record(issue)
}
```

### Override record(_ issue:) to add an attachment — [11:39]

```swift
override func record(_ issue: XCTIssue) {

    // Redeclare using var to enable mutation.
    var issue = issue

    // Add a simple attachment.
    issue.add(XCTAttachment(string: "hello"))

    // Pass it to super.
    super.record(issue)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10687/4/9416FDA9-FC21-48ED-BBCC-ABF5C5A9B0DA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10687) — developer.apple.com. Indexed for agent consumption._
