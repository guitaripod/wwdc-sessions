# Deliver workout insights with HealthKit workout zones

**Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-207](https://developer.apple.com/videos/play/wwdc2026/207)

HealthKit makes it easier to provide workout insights — like heart rate and cycling power zones — in your app. Learn to leverage the built-in, personalized zones or create custom ones. Discover how to use the current zone and time spent in each zone to provide meaningful guidance during and after workouts.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Tracking heart rate zones for workouts](https://developer.apple.com/documentation/HealthKit/tracking-heart-rate-zones-for-workouts) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/tracking-heart-rate-zones-for-workouts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/tracking-heart-rate-zones-for-workouts.json
- [Accessing workout zone data](https://developer.apple.com/documentation/HealthKit/accessing-workout-zone-data) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/accessing-workout-zone-data
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/accessing-workout-zone-data.json

## Code Snippets

### Reading Heart Rate Zones from a completed workout — [3:54]

```swift
// Read heart rate zones from the completed workout​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​

if let heartRateZoneGroup = workout.zoneGroupsByType?[HKQuantityType(.heartRate)] {​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
let zones = ZoneDisplayData(​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    zoneCount: heartRateZoneGroup.configuration.zones.count,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    currentZoneIndex: nil,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    durations: heartRateZoneGroup.zoneDurations.map(\.duration)​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
)
```

### Handling Live Zone Updates — [7:57]

```swift
func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
                    didUpdateWorkoutZone zoneUpdate: HKLiveWorkoutZoneUpdate) {​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    guard let zoneGroup = zoneUpdate.zoneGroup else {​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
        return​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    }​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    if let currentIndex = zoneUpdate.currentZoneDuration?.zone.index {​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
        let data = ZoneDisplayData(​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
            zoneCount: zoneGroup.configuration.zones.count,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
            currentZoneIndex: currentIndex,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
            durations: zoneGroup.zoneDurations.map(\.duration)​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
        )​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
        Task { @MainActor in​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
            self.heartRateZones = data​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
        }​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    }​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
}
```

### Check if Preferred Zone has been set — [9:19]

```swift
if try await builder.zoneConfiguration(for: HKQuantityType(.heartRate)) == nil {
```

### Create Zone Boundaries — [9:24]

```swift
let defaultHeartRateZoneThresholds = [91.0, 114.0, 136.0, 158.0]​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
let bpmUnit = HKUnit.count().unitDivided(by: HKUnit.minute())​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
let boundaries = defaultHeartRateZoneThresholds.map(​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
    {HKQuantity(unit: bpmUnit, doubleValue:$0)}
)
```

### Create Default Workout Zone Configuration — [9:33]

```swift
let heartRate = HKQuantityType(.heartRate)​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
let defaultConfiguration = try HKWorkoutZoneConfiguration(quantityType: heartRate,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
                                                          zoneBoundaries: boundaries)
```

### Set Custom Zone Configuration — [9:58]

```swift
try await builder.setCustomZoneConfiguration(defaultConfiguration,​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
                                                 for: heartRate)​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
}
```

### Begin Data Collection — [10:03]

```swift
// Begin data collection
let startDate = Date()​​​​​​​​​​​​​​
try await builder.beginCollection(at: startDate)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/207/5/8627c1d4-7a34-46f2-8491-f0d1c138edd1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/207/5/8627c1d4-7a34-46f2-8491-f0d1c138edd1/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._