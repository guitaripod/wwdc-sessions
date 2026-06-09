---
id: "wwdc2026-295"
event: "wwdc2026"
year: 2026
title: "Validate your App Intents adoption with AppIntentsTesting"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/295"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Validate your App Intents adoption with AppIntentsTesting

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-295](https://developer.apple.com/videos/play/wwdc2026/295)

Meet AppIntentsTesting, a new framework for validating your App Intents through the same infrastructure used by Siri, Shortcuts, and Spotlight. Discover how to execute intents, inspect results, and test entities and queries — all without requiring UI automation. Find out how to verify integrations like View annotations and Spotlight indexing, helping you catch bugs early in your development workflow.

**Keywords:** `ai`, `app intents`, `machine learning`, `testing`, `xcode`, `xctest`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,137 words)

## Documentation & Resources

- [Testing your App Intents code](https://developer.apple.com/documentation/AppIntentsTesting/testing-your-app-intents-code) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntentsTesting/testing-your-app-intents-code
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntentsTesting/testing-your-app-intents-code.json
- [App Intents Testing](https://developer.apple.com/documentation/AppIntentsTesting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntentsTesting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntentsTesting.json

## Code Snippets

### Your first test: execute an intent — [6:48]

```swift
import AppIntentsTesting

func testCreateCalendar() async throws {
    let definitions = IntentDefinitions(bundleIdentifier: "com.example.apple-samplecode.CometCal")
    let createCalendar = definitions.intents["CreateCalendarIntent"]
    let result = try await createCalendar.makeIntent(
        name: "Occupy Saturn",
        color: "red"
    ).run()
    XCTAssertEqual(try result.value.title, "Occupy Saturn")
}
```

### Test an entity string query — [12:25]

```swift
// Testing Entity string queries
func testEventStringQuery() async throws {
    let results = try await eventEntityDefinition
        .entities(matching: "Cosmic Ray")

    XCTAssertEqual(results.count, 1)
    XCTAssertEqual(try results[0].title, "Cosmic Ray Calibration")
}
```

### Implement the EntityStringQuery under test — [13:00]

```swift
// Updated query implementation
struct EventEntityQuery: EntityStringQuery {
    func entities(for identifiers: [EventEntity.ID]) async throws -> [EventEntity] {

    }

    func suggestedEntities() async throws -> [EventEntity] {

    }

    func entities(matching string: String) async throws -> [EventEntity] {
        try calendarManager.fetchEvents()
            .filter { $0.title.localizedCaseInsensitiveContains(string) }
            .map(\.entity)
    }
}
```

### Chain multiple intents in one test — [15:42]

```swift
// Test event creation followed by update
func testCreateAndUpdateEvent() async throws {
    let createResult = try await createEventDefinition.makeIntent(
        title: "Asteroid Dodgeball Practice",
        startDate: Date(),
        isAllDay: false,
        calendar: "Deep Space"
    ).run()

    XCTAssertEqual(try createResult.value.title, "Asteroid Dodgeball Practice")

    let updateResult = try await updateEventDefinition.makeIntent(
        title: "Asteroid Dodgeball Rules Overview",
        event: createResult.value
    ).run()

    XCTAssertEqual(try updateResult.value.title, "Asteroid Dodgeball Rules Overview")
}
```

### Make an intent test-only — [17:45]

```swift
// Test-only intent: SeedSampleEventsIntent
#if DEBUG
struct SeedSampleEventsIntent: AppIntent {
    static let isDiscoverable = false

    func perform() async throws -> some IntentResult {
        // Create known list of events
        return .result()
    }
}
#endif
```

### Test Spotlight indexing — [20:27]

```swift
// Testing Spotlight indexing
func testNewEventIndexedInSpotlight() async throws {

    let before = try await eventEntityDefinition.spotlightQuery("Supernova Viewing Party")
    XCTAssertTrue(before.isEmpty, "Event should not exist in Spotlight yet")

    // ... Create "Supernova Viewing Party" Event

    let after = try await eventEntityDefinition.spotlightQuery("Supernova Viewing Party")
    XCTAssertEqual(after.count, 1)
    XCTAssertEqual(try after[0].title, "Supernova Viewing Party")
}
```

### Test view annotations — [22:33]

```swift
/ Testing view annotations
func testEventViewAnnotation() async throws {
    try await openEventDefinition.makeIntent(target: "Morning Launch Briefing").run()

    // Confirm correct event page
    let app = XCUIApplication()
    let title = app.staticTexts["Morning Launch Briefing"]
    XCTAssertTrue(title.waitForExistence(timeout: 5))

    let annotations = try await eventEntityDefinition.viewAnnotations()

    XCTAssertEqual(annotations.count, 1, "Expected exactly one view annotation")
    XCTAssertEqual(try annotations[0].entity.title, "Morning Launch Briefing")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/295/4/cdcee6d3-e3e9-4201-b1ef-cd33e2d10e6f/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/295/4/cdcee6d3-e3e9-4201-b1ef-cd33e2d10e6f/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/295) — developer.apple.com. Indexed for agent consumption._
