---
id: "wwdc2022-110361"
event: "wwdc2022"
year: 2022
title: "Author fast and reliable tests for Xcode Cloud"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110361"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Author fast and reliable tests for Xcode Cloud

**Event:** WWDC22 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110361](https://developer.apple.com/videos/play/wwdc2022/110361)

Discover how you can create effective testing plans for Xcode Cloud, Apple’s continuous integration and continuous delivery service. We'll show you how testing can be an essential tool to consistently verify your code works correctly. Learn how you can author fast, reliable, and efficient tests for Xcode Cloud, avoid irrelevant failures, and verify your code changes quickly.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,871 words)

## Code Snippets

### setUp() — [3:37]

```swift
override func setUp() async throws {

}
```

### setUp() example — [3:46]

```swift
var truck: Truck!

override func setUp() async throws {
    let directoryURL = FileManager.default.temporaryDirectory
    let fileName = UUID().uuidString
    let fileURL = directoryURL.appendingPathComponent(fileName, isDirectory: false)
    let data = await mockDonutMenuData()
    try data.write(to: fileURL)
    truck = Truck(menuURL: fileURL)
}
```

### Environment variable example — [5:55]

```swift
var truck: Truck!

func testOrderDonut() throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]

    let expectation = XCTestExpectation(description: "Order donut")
    truck.order(with: .sprinkles, host: host) { error, donut in
        XCTAssertTrue(donut.hasSprinkles)
        expectation.fulfill()
    }       
    wait(for: [expectation], timeout: 5)
}
```

### XCTSkip example — [6:00]

```swift
var truck: Truck!

func testOrderDonut() throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let expectation = XCTestExpectation(description: "Order donut")
    truck.order(with: .sprinkles, host: host) { error, donut in
        XCTAssertTrue(donut.hasSprinkles)
        expectation.fulfill()
    }       
    wait(for: [expectation], timeout: 5)
}
```

### XCTSkip example — [8:18]

```swift
var truck: Truck!

func testOrderDonut() throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let expectation = XCTestExpectation(description: "Order donut")
    truck.order(with: .sprinkles, host: host) { error, donut in
        XCTAssertTrue(donut.hasSprinkles)
        expectation.fulfill()
    }       
    wait(for: [expectation], timeout: 5)
}
```

### XCTestExpectation example — [8:48]

```swift
var truck: Truck!

func testOrderDonut() throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let expectation = XCTestExpectation(description: "Order donut")
    truck.order(with: .sprinkles, host: host) { error, donut in
        XCTAssertTrue(donut.hasSprinkles)
        expectation.fulfill()
    }       
    wait(for: [expectation], timeout: 5)
}
```

### Increase XCTestExpectation example — [8:59]

```swift
var truck: Truck!

func testOrderDonut() throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let expectation = XCTestExpectation(description: "Order donut")
    truck.order(with: .sprinkles, host: host) { error, donut in
        XCTAssertTrue(donut.hasSprinkles)
        expectation.fulfill()
    }       
    wait(for: [expectation], timeout: 10)
}
```

### Async/await example — [9:16]

```swift
var truck: Truck!

func testOrderDonut() async throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let donut = try await truck.orderDonut(with: .sprinkles, host: host)
    XCTAssertTrue(donut.hasSprinkles)
}
```

### XCTExpectFailure example — [10:02]

```swift
var truck: Truck!

func testOrderDonut() async throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    let donut = try await truck.orderDonut(with: .sprinkles, host: host)
    XCTAssertTrue(donut.hasSprinkles)
}
```

### XCTExpectFailure example — [10:06]

```swift
var truck: Truck!

func testOrderDonut() async throws {
    let host = ProcessInfo.processInfo.environment["BASE_URL"]
    try XCTSkipIf(host == "prod.example.com")

    XCTExpectFailure("<https://dev.myco.com/bug/98> Donut ordering service is down")
    let donut = try await truck.orderDonut(with: .sprinkles, host: host)
    XCTAssertTrue(donut.hasSprinkles)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110361/3/7FB8FB7D-976B-432E-A47D-05ADDFE1BD45/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110361/3/7FB8FB7D-976B-432E-A47D-05ADDFE1BD45/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110361) — developer.apple.com. Indexed for agent consumption._
