---
id: "wwdc2020-10221"
event: "wwdc2020"
year: 2020
title: "Get your test results faster"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10221"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Get your test results faster

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10221](https://developer.apple.com/videos/play/wwdc2020/10221)

Improve your testing suite to speed up your feedback loop and get fixes in faster. Learn more about the latest improvements to testing in Xcode, including how to leverage test plans, Xcodebuild updates, and APIs to eliminate never-ending and badly-behaved tests. We’ll explore Test Timeouts and Execution Time Allowances in XCTest, examine device parallelization, and detail recommended practices for balancing performance with clear fault localization.

To get the most out of this session, you should be familiar with authoring basic tests using XCTest and managing tests through test plans. For background, watch “Testing in Xcode” from WWDC19.

**Keywords:** `continuous integration`, `testing`, `test result`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,761 words)

## Code Snippets

### testUpdatingSmoothiesFromServer Sample — [6:12]

```swift
import XCTest
@testable import Fruta

class SmoothieNetworkingTests: XCTestCase {
    func testUpdatingSmoothiesFromServer() throws {
        let originalSmoothies = Smoothie.all
        try Smoothie.fetchSynchronouslyFromServer()
        XCTAssertNotEqual(originalSmoothies, Smoothie.all)
    }
}
```

### Interesting Spindump Content — [7:56]

```bash
11  __26-[XCTestCase performTest:]_block_invoke_2 + 43 (XCTest + 167518) [0x105a70e5e] 1-11
11  -[XCTestCase invokeTest] + 1069 (XCTest + 161187) [0x105a6f5a3] 1-11
  11  -[XCTestCase(XCTIssueHandling) _caughtUnhandledDeveloperExceptionPermittingControlFlowInterruptions:caughtInterruptionException:whileExecutingBlock:] + 183 (XCTest + 535831) [0x105acad17] 1-11
    11  __24-[XCTestCase invokeTest]_block_invoke.239 + 129 (XCTest + 162434) [0x105a6fa82] 1-11
      11  +[XCTSwiftErrorObservation observeErrorsInBlock:] + 69 (XCTest + 811868) [0x105b0e35c] 1-11
        11  __24-[XCTestCase invokeTest]_block_invoke_2 + 52 (XCTest + 162709) [0x105a6fb95] 1-11
          11  ??? [0x7fff20438bf6] 1-11
            11  ??? [0x7fff2043b73c] 1-11
              11  @objc SmoothieNetworkingTests.testUpdatingSmoothiesFromServer() + 74 (<compiler-generated> in Fruta Unit Tests + 23882) [0x105d35d4a] 1-11
                11  SmoothieNetworkingTests.testUpdatingSmoothiesFromServer() + 132 (Networking.swift:12,22 in Fruta Unit Tests + 22756) [0x105d358e4] 1-11
                  11  static Smoothie.fetchSynchronouslyFromServer() + 163 (Smoothie.swift:61,26 in Fruta + 374563) [0x10532f723] 1-11
                    11  static Smoothie.performGETRequest(to:) + 179 (Smoothie.swift:73,31 in Fruta + 375475) [0x10532fab3] 1-11
                      11  -[PKAppleAccountInformation appleID] + 6 (PassKitCore + 1577496) [0x7fff5bc14218] 1-11
                        11  -[PKNFCTagReaderSession delegate] + 8 (PassKitCore + 1348766) [0x7fff5bbdc49e] 1-11
                         *11  psynch_mtxcontinue + 0 (pthread + 9627) [0xffffff800365a59b] (blocked by turnstile waiting for this thread) 1-11
```

### Helper Methods — [8:23]

```swift
extension Smoothie {

    enum Errors: Error {
        case noData
    }

    static var serverIsAvailable: Bool { false }
    static var smoothieEndpoint: URL {
        URL(string: "https://smoothies.food.com")!
    }

    static func fetchSynchronouslyFromServer() throws {
        fetchSmoothieLock.lock()
        defer { fetchSmoothieLock.unlock() }

        guard let data = performGETRequest(to: smoothieEndpoint) else {
            throw Errors.noData
        }

        let smoothies = try JSONDecoder().decode([Smoothie].self, from: data)
        Smoothie.all += smoothies
    }

    static func performGETRequest(to url: URL) -> Data? {
        defer { fetchSmoothieLock.unlock() }

        if url == smoothieEndpoint {
            fetchSmoothieLock.lock()
        }

        return performNetworkRequest(method: .get, url: url)
    }
}
```

### Update performGETRequest function — [8:43]

```swift
extension Smoothie {

    // Omitted for brevity. See previous code snippet for content.

    static func performGETRequest(to url: URL) -> Data? {
        return performNetworkRequest(method: .get, url: url)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10221/2/6B07FDD7-B950-4B25-BA94-E07A733F537F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10221) — developer.apple.com. Indexed for agent consumption._