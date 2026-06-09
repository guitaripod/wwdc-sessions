---
id: "wwdc2026-267"
event: "wwdc2026"
year: 2026
title: "Migrate to Swift Testing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/267"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Migrate to Swift Testing

**Event:** WWDC26 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-267](https://developer.apple.com/videos/play/wwdc2026/267)

Learn how to fearlessly adopt Swift Testing alongside your XCTests using test framework interoperability. Discover best practices and patterns for incrementally introducing advanced testing features that accelerate development and increase coverage.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,891 words)

## Code Snippets

### Name a test using a raw identifier — [1:12]

```swift
import Testing

@testable import DemoApp

@Test func `Default climate: tropical`() async throws {
    let fruit = Fruit(name: "Coconut")
    #expect(fruit.climate == .tropical)
}
```

### Wrap XCTFail in a test helper function — [5:03]

```swift
func testUniqueFruitNames() async throws {
    assertUnique(Market.fruits + [Fruit.lychee])
}

// TestHelpers.swift

func assertUnique(_ fruits: [Fruit], file: StaticString = #filePath, line: UInt = #line) {
    var uniqueNames = Set<String>()
    for name in fruits.map(\.name) {
        if !uniqueNames.insert(name).inserted {
            XCTFail("Duplicate name: \(name)", file: file, line: line)
        }
    }
}
```

### Replace XCTFail with Issue.record in the test helper — [10:12]

```swift
import Testing

func assertUnique(_ fruits: [Fruit], sourceLocation: SourceLocation = ...) {
    var uniqueNames = Set<String>()
    for name in fruits.map(\.name) {
        if !uniqueNames.insert(name).inserted {
            Issue.record("Duplicate name: \(name)", sourceLocation: sourceLocation)
        }
    }
}
```

### Run Swift Package tests with the strict interoperability mode from Terminal — [12:15]

```bash
> SWIFT_TESTING_XCTEST_INTEROP_MODE=strict swift test
```

### Common migration: skipping tests — [13:10]

```swift
let isFall = false

// XCTest
func testSwallowFallMigration() async throws {
    try XCTSkipIf(!isFall, "Wrong season for migration")
    // ...
}

// Test.cancel interoperability from Swift Testing
func testSwallowFallMigration() async throws {
    if !isFall {
        try Test.cancel("Wrong season for migration")
    }
    // ...
}

// ✅ Prefer test trait in Swift Testing
@Test(.enabled(if: isFall, "Wrong season for migration"))
func `Swallow fall migration`() async throws {
   // ...
}
```

### Common migration: halting after test failures — [13:41]

```swift
func testExample() async throws {
    #expect(Fruit.banana.climate == .temperate)

    try #require(Fruit.banana == Fruit.plantain)
    XCTFail("This is never reached")
}
```

### Example of nested loops which can be converted into a parameterized @Test function — [15:57]

```swift
struct BirdTests {

    @Test func `Birds flap wings successfully`() async throws {
        for bird in Aviary.birds {
            for count in (40...100) {
                try await bird.flapWings(count: count)
            }
        }
    }

}
```

### Refactor nested loops into a parameterized @Test function — [16:47]

```swift
struct BirdTests {

    @Test(arguments: Aviary.birds, 40...100)
    func `Birds flap wings successfully`(bird: Bird, count: Int) async throws {
        try await bird.flapWings(count: count)
    }

}
```

### Precondition check on empty input name in an initializer — [18:21]

```swift
// In `Bird.init(...)`
if name.isEmpty {
    preconditionFailure("Bird name cannot be empty")
}
```

### Add coverage for precondition failure with exit test — [19:27]

```swift
extension BirdTests {

    @Test func `Bird with empty name crashes`() async throws {
        await #expect(processExitsWith: .failure) {
            _ = Bird(name: "")
        }
    }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/267/4/d54e4861-10d9-4d4d-9952-3fe311cd2dc4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/267/4/d54e4861-10d9-4d4d-9952-3fe311cd2dc4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/267) — developer.apple.com. Indexed for agent consumption._