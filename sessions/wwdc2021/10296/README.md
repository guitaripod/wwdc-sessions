---
id: "wwdc2021-10296"
event: "wwdc2021"
year: 2021
title: "Diagnose unreliable code with test repetitions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10296"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Diagnose unreliable code with test repetitions

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10296](https://developer.apple.com/videos/play/wwdc2021/10296)

Test repetitions can help you debug even the most unreliable code. Discover how you can use the maximum repetitions, until failure, and retry on failure testing modes within test plans, Xcode, and xcodebuild to track down bugs and crashers and make your app more stable for everyone.

To get the most out of this session, we recommend being familiar with XCTest and managing tests through test plans. For more information, check out “Testing in Xcode” from WWDC19.

**Keywords:** `ci`, `failure`, `test repetition`, `xcode`, `xctest`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,084 words)

## Code Snippets

### testFlavors — [2:39]

```swift
func testFlavors() {
    var truck: IceCreamTruck?

    let flavorsExpectation = XCTestExpectation(description: "Get ice cream truck's flavors")
    truckDepot.iceCreamTruck { newTruck in
        truck = newTruck
        newTruck.prepareFlavors { error in
            XCTAssertNil(error)
        }
        flavorsExpectation.fulfill()
    }

    wait(for: [flavorsExpectation], timeout: 5)
    XCTAssertEqual(truck?.flavors, 33)
}
```

### testFlavors: add async throws to method header — [6:31]

```swift
func testFlavors() async throws {
    var truck: IceCreamTruck?

    let flavorsExpectation = XCTestExpectation(description: "Get ice cream truck's flavors")
    truckDepot.iceCreamTruck { newTruck in
        truck = newTruck
        newTruck.prepareFlavors { error in
            XCTAssertNil(error)
        }
        flavorsExpectation.fulfill()
    }

    wait(for: [flavorsExpectation], timeout: 5)
    XCTAssertEqual(truck?.flavors, 33)
}
```

### testFlavors: use the async version of the ice cream truck — [6:32]

```swift
func testFlavors() async throws {
    let truck = await truckDepot.iceCreamTruck()
        truck = newTruck
        newTruck.prepareFlavors { error in
            XCTAssertNil(error)
        }
        flavorsExpectation.fulfill()
    }

    wait(for: [flavorsExpectation], timeout: 5)
    XCTAssertEqual(truck?.flavors, 33)
}
```

### testFlavors: use the async version of prepareFlavors — [6:33]

```swift
func testFlavors() async throws {
    let truck = await truckDepot.iceCreamTruck()
    try await truck.prepareFlavors()
    XCTAssertEqual(truck?.flavors, 33)
}
```

### testFlavors: the truck is no longer optional — [6:50]

```swift
func testFlavors() async throws {
    let truck = await truckDepot.iceCreamTruck()
    try await truck.prepareFlavors()
    XCTAssertEqual(truck.flavors, 33)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10296/6/FE383085-9A76-432B-B78A-FF8149F81733/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10296/6/FE383085-9A76-432B-B78A-FF8149F81733/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10296) — developer.apple.com. Indexed for agent consumption._