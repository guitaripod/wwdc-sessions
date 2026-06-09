---
id: "wwdc2021-10287"
event: "wwdc2021"
year: 2021
title: "Measure health with motion"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10287"
topics: ["Health & Fitness"]
platforms: ["iOS", "iPadOS", "watchOS"]
hasTranscript: true
---

# Measure health with motion

**Event:** WWDC21 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10287](https://developer.apple.com/videos/play/wwdc2021/10287)

Discover how you can take your app’s health monitoring to the next level with motion data. Meet Walking Steadiness for iPhone and the six-minute-walk metric for Apple Watch: Walking Steadiness can help your app interpret someone’s quality of walking and risk of falling, while the six-minute-walk metric — along with the HealthKit estimate recalibration API — can track changes to walking endurance following acute events like surgery. We’ll show you how you can support these metrics and help provide actionable health data to people who use your app, helping improve patient care and clinical trials, especially as more services must be delivered remotely.

**Keywords:** `healthkit`, `therapy`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,522 words)

## Documentation & Resources

- [HKAppleWalkingSteadinessClassification](https://developer.apple.com/documentation/HealthKit/HKAppleWalkingSteadinessClassification) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/HKAppleWalkingSteadinessClassification
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/HKAppleWalkingSteadinessClassification.json
- [appleWalkingSteadinessEvent](https://developer.apple.com/documentation/HealthKit/HKCategoryTypeIdentifier/appleWalkingSteadinessEvent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/HKCategoryTypeIdentifier/appleWalkingSteadinessEvent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/HKCategoryTypeIdentifier/appleWalkingSteadinessEvent.json
- [appleWalkingSteadiness](https://developer.apple.com/documentation/HealthKit/HKQuantityTypeIdentifier/appleWalkingSteadiness) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/HKQuantityTypeIdentifier/appleWalkingSteadiness
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/HKQuantityTypeIdentifier/appleWalkingSteadiness.json
- [CMFallDetectionManager](https://developer.apple.com/documentation/CoreMotion/CMFallDetectionManager) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMotion/CMFallDetectionManager
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMotion/CMFallDetectionManager.json
- [Measuring Walking Quality Through iPhone Mobility Metrics](https://www.apple.com/healthcare/docs/site/Measuring_Walking_Quality_Through_iPhone_Mobility_Metrics.pdf) _guide_
- [Using Apple Watch to Estimate Six-Minute Walk Distance](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Six_Minute_Walk_Distance.pdf) _documentation_
- [Using Apple Watch to Estimate Cardio Fitness with VO2 max](https://www.apple.com/healthcare/docs/site/Using_Apple_Watch_to_Estimate_Cardio_Fitness_with_VO2_max.pdf) _guide_
- [Getting movement disorder symptom data](https://developer.apple.com/documentation/CoreMotion/getting-movement-disorder-symptom-data) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMotion/getting-movement-disorder-symptom-data
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMotion/getting-movement-disorder-symptom-data.json
- [Core Motion](https://developer.apple.com/documentation/CoreMotion) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMotion
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMotion.json

## Code Snippets

### Grab authorization to read and share sixMinuteWalkTestDistance type — [0:01]

```swift
// Grab authorization to read and share sixMinuteWalkTestDistance type

let healthStore = HKHealthStore()
let types: Set = [
    HKObjectType.quantityType(forIdentifier: .sixMinuteWalkTestDistance)!
]

healthStore.requestAuthorization(toShare: types, read: types) { _, _ in }
```

### Recalibrate Six-Minute Walk estimates — [0:02]

```swift
// Recalibrate estimate

let healthStore = HKHealthStore()
let sixMinuteWalkType = HKSampleType.quantityType(forIdentifier: .sixMinuteWalkTestDistance)!

if sixMinuteWalkType.allowsRecalibrationForEstimates {

    healthStore.recalibrateEstimates(sampleType: sixMinuteWalkType, date: surgeryDate) { 
        (success, error) in
        // Handle error
    }

}
```

### Get authorized for walkingSteadiness type — [0:03]

```swift
// Get authorized

let types: Set = [
    HKObjectType.quantityType(forIdentifier: .walkingSteadiness)!
]

healthKitStore.requestAuthorization(toShare: nil, read: types) { _, _ in }
```

### Construct a query for most recent walkingSteadiness score — [0:04]

```swift
// Construct a query for most recent walkingSteadiness score

let steadinessType = HKObjectType.quantityType(forIdentifier: .walkingSteadiness)
let sortByEndDate = NSSortDescriptor(key: HKSampleSortIdentifierEndDate, ascending: false)

let query = HKSampleQuery(sampleType: steadinessType,
                          predicate: nil,
                          limit: 1,
                          sortDescriptors: [sortByEndDate]) { (query, samples, error) in

    if let sample = samples?.first as? HKQuantitySample{

        let recentScore = sample.quantity.doubleValue(forUnit: .percentUnit)

        updateStatus(score: recentScore)
    }
}

self.healthStore.execute(query)
```

### Construct a query for most recent walkingSteadiness classification — [0:05]

```swift
// Construct a query for most recent walkingSteadiness classification

let steadinessType = HKObjectType.quantityType(forIdentifier: .walkingSteadiness)

let query = HKSampleQuery(sampleType: steadinessType,
                          predicate: nil,
                          limit: 1,
                          sortDescriptors: nil) { (query, samples, error) in

    if let sample = samples?.first as? HKQuantitySample{

        let recentScore = sample.quantity.doubleValue(forUnit: .percentUnit)

        // Use HealthKit API to classify a value as OK, Low, or Very Low
        let recentClassification = HKAppleWalkingSteadinessClassification(for: walkingSteadiness.quantity)

        updateStatus(classification: recentClassification, score: recentScore)
    }
}

self.healthStore.execute(query)
```

### Get authorized .walkingSteadinessEvent — [0:06]

```swift
// Get authorized

let types: Set = [
    HKObjectType.categoryType(forIdentifier: .walkingSteadinessEvent)!
]

healthKitStore.requestAuthorization(toShare: nil, read: types) { _, _ in }
```

### Watch for walkingSteadiness notifications — [0:07]

```swift
// Watch for walkingSteadiness notifications

let notificationType = HKCategoryType.categoryType(forIdentifier: .appleWalkingSteadinessEvent)!

let query = HKObserverQuery(sampleType: notificationType, predicate: nil) { 
    (query, completionHandler, errorOrNil) in

    if let error = errorOrNil {
        // Properly handle the error.
        return
    }

    promptCheckupForNotification()

    completionHandler()
}

self.healthStore.execute(query)
```

### Query walking steadiness in the past 6 weeks — [0:08]

```swift
// Query samples from HealthKit

// Look back 6 weeks
let end = Date()
let start = Calendar.current.date(byAdding: .week, value: -6, to: end)

let datePredicate = HKQuery.predicateForSamples(withStart: start, end: end, options: [])

// Query walking steadiness
let steadinessType = HKObjectType.quantityType(forIdentifier: .walkingSteadiness)
let sortByEndDate = NSSortDescriptor(key: HKSampleSortIdentifierEndDate, ascending: false)

let query = HKSampleQuery(sampleType: steadinessType,
                          predicate: sortByEndDate,
                          limit: nil,
                          sortDescriptors:[sortByEndDate]) { (_, samples, _) in

    detectTrends(samples)
}
self.healthStore.execute(query)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10287/5/C117695D-C24C-4B2E-B6A4-C87244FC08AC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10287/5/C117695D-C24C-4B2E-B6A4-C87244FC08AC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10287) — developer.apple.com. Indexed for agent consumption._
