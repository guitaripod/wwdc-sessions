---
id: "wwdc2024-10109"
event: "wwdc2024"
year: 2024
title: "Explore wellbeing APIs in HealthKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10109"
topics: ["App Services", "Health & Fitness"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Explore wellbeing APIs in HealthKit

**Event:** WWDC24 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10109](https://developer.apple.com/videos/play/wwdc2024/10109)

Learn how to incorporate mental health and wellbeing into your app using HealthKit. There are new APIs for State of Mind, as well as for Depression Risk and Anxiety Risk. We’ll dive into principles of emotion science to cover how reflecting on feelings can be beneficial, and how State of Mind can be used to represent different types of mood and emotion.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,473 words)

## Documentation & Resources

- [Visualizing HealthKit State of Mind in visionOS](https://developer.apple.com/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos.json
- [Forum: Health & Fitness](https://developer.apple.com/forums/topics/health-and-fitness?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/health-and-fitness?cid=vf-a-0010
- [HealthKit](https://developer.apple.com/documentation/HealthKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit.json

## Code Snippets

### Request authorization to read and write State of Mind HealthKit samples — [5:37]

```swift
// Request authorization to read and write State of Mind HealthKit samples

import HealthKitUI

func healthDataAccessRequest(
    store: HKHealthStore, 
    shareTypes: Set<HKSampleType>,
    readTypes: Set<HKObjectType>? = nil,
    trigger: some Equatable,
    completion: @escaping (Result<Bool, any Error>) -> Void
) -> some View
```

### EmojiType — [6:26]

```swift
// EmojiType

enum EmojiType: CaseIterable {
    case angry
    case sad
    case indifferent
    case satisfied
    case happy

    var emoji: String {
        switch self {
        case .angry: return "😡"
        case .sad: return "😢"
        case .indifferent: return "😐"
        case .satisfied: return "😌"
        case .happy: return "😊"
        }
    }

}
```

### Create State of Mind sample for an event and emoji selection — [6:32]

```swift
/// Create State of Mind sample for an event and emoji selection

func createSample(for event: EventModel, emojiType: EmojiType) ->
HKStateOfMind {
    let kind: HKStateOfMind.Kind = .momentaryEmotion
    let valence: Double = emojiType.valence
    let label = emojiType.label
    let association = event.association
    return HKStateOfMind(date: event.endDate,
                         kind: kind,
                         valence: valence,
                         labels: [label],
                         associations: [association])
｝
```

### Save State of Mind sample from emoji choice — [7:21]

```swift
// Save State of Mind sample from emoji choice

func save(sample: HKSample, healthStore: HKHealthStore) async {
    do {
        try await healthStore.save(sample)
    ｝
    catch {
        // Handle error here.
    }
｝
```

### Query State of Mind samples — [10:34]

```swift
// Query State of Mind samples

let datePredicate: NSPredicate = { ... }
let associationsPredicate = NSCompoundPredicate (
    orPredicateWithSubpredicates: associations.map {
        HKQuery.predicateForStatesOfMind(with: $0)
    }
)  
let compoundPredicate = NSCompoundPredicate(
    andPredicateWithSubpredicates: [datePredicate, associationsPredicate]
)
let state0fMindPredicate = HKSamplePredicate.stateOfMind(compoundPredicate)
```

### Query State of Mind samples — [10:49]

```swift
// Query State of Mind samples

let datePredicate: NSPredicate = { ... }
let associationsPredicate = NSCompoundPredicate (
    orPredicateWithSubpredicates: associations.map {
        HKQuery.predicateForStatesOfMind(with: $0)
    }
)  
let compoundPredicate = NSCompoundPredicate(
    andPredicateWithSubpredicates: [datePredicate, associationsPredicate]
)
let stateOfMindPredicate = HKSamplePredicate.stateOfMind(compoundPredicate)

let descriptor = HKSampleQueryDescriptor(predicates: [stateOfMindPredicate],
                                         sortDescriptors: [])
var results: [HKStateOfMind] = []
do {
    // Launch the query and wait for the results.
    results = try await descriptor.result(for: healthStore)
} catch {
    // Handle error here.
｝
```

### Query State of Mind samples (continued) — [10:54]

```swift
// Adjust each valence value to be from a range of 0.0 to 2.0.
let adjustedValenceResults = results.map { $0.valence + 1.0 }
// Calculate average valence.
let totalAdjustedValence = adjustedValenceResults.reduce (0.0, +)
let averageAdjustedValence = totalAdjustedValence / Double(results.count)
// Convert valence to percentage.
let adjustedValenceAsPercent = Int(100.0 * (averageAdjustedValence / 2.0))
```

### Query for relevant State of Mind samples with a specific label — [11:33]

```swift
// Query for relevant State of Mind samples with a specific label
let label: HKStateOfMind.Label = .happy

// Configure the query
let datePredicate = HKQuery.predicateForSamples(withStart: dateInterval.start,
                                                end: dateInterval.end)
let associationPredicate = HKQuery.predicateForStatesOfMind(with: association)
let labelPredicate = HKQuery.predicateForStates0fMind(with: label)
let compoundPredicate = NSCompoundPredicate(
    andPredicateWithSubpredicates: [datePredicate, associationPredicate, labelPredicate]
)
let stateOfMindPredicate = HKSamplePredicate.stateOfMind(compoundPredicate)
let descriptor = HKAnchoredObjectQueryDescriptor(predicates: [state0fMindPredicate],
                                                 anchor: nil)

// Fetch the results
let results = descriptor.results(for: healthStore)
let samples: [HKStateOfMind] = try await results.reduce([]) { $1.addedSamples }
```

### Process State of Mind sample data — [11:45]

```swift
// Process State of Mind sample data

let happiestSample = samples.max { $0.valence < $1. valence }
let happiestEvent: EventModel? = findClosestEvent(startDate: happiestSample?.startDate,
                                                  endDate: happiestSample?.endDate)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10109/4/C6E12E83-F007-47F9-A74C-6DDC86BEE5AB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10109/4/C6E12E83-F007-47F9-A74C-6DDC86BEE5AB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10109) — developer.apple.com. Indexed for agent consumption._
