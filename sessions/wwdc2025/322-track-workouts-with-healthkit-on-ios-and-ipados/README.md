---
id: "wwdc2025-322"
event: "wwdc2025"
year: 2025
title: "Track workouts with HealthKit on iOS and iPadOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/322"
topics: ["App Services", "Health & Fitness"]
platforms: ["iOS"]
hasTranscript: true
---

# Track workouts with HealthKit on iOS and iPadOS

**Event:** WWDC25 · **Topic:** Health & Fitness · **Platforms:** iOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-322](https://developer.apple.com/videos/play/wwdc2025/322)

Learn best practices for building a great workout experience for iOS. Review the life cycle of a workout session, explore the differences between workouts on Apple Watch and iPhone, and find out how to use Live Activities and Siri to pump up your app’s Lock Screen experience.

**Keywords:** `bluetooth`, `heart rate`, `samples`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,949 words)

## Documentation & Resources

- [Handling Workout Requests with SiriKit](https://developer.apple.com/documentation/SiriKit/handling-workout-requests-with-sirikit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/handling-workout-requests-with-sirikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/handling-workout-requests-with-sirikit.json
- [Running workout sessions](https://developer.apple.com/documentation/HealthKit/running-workout-sessions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/running-workout-sessions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/running-workout-sessions.json
- [Building a workout app for iPhone and iPad](https://developer.apple.com/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad.json
- [Building a multidevice workout app](https://developer.apple.com/documentation/HealthKit/building-a-multidevice-workout-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/building-a-multidevice-workout-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/building-a-multidevice-workout-app.json
- [HKWorkoutSession](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/HKWorkoutSession
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/HKWorkoutSession.json

## Code Snippets

### Set up workout session — [1:30]

```swift
// Set up workout session

// Create workout configuration
let configuration = HKWorkoutConfiguration()
configuration.activityType = .running
configuration.locationType = .outdoor

// Create workout session
let session = try HKWorkoutSession(healthStore: healthStore, configuration: configuration)
session.delegate = self

// Get associated workout builder and add data source
let builder = session.associatedWorkoutBuilder()
builder.delegate = self
builder.dataSource = HKLiveWorkoutDataSource(healthStore: healthStore,
                                             workoutConfiguration: configuration)
```

### Starting the session — [1:54]

```swift
// Prepare and start session

session.prepare()

// Start and display count down

// Start session and builder collection once count down finishes
session.startActivity(with: startDate)
try await builder.beginCollection(at: startDate)
```

### Handling Metrics — [2:14]

```swift
// Handling collected metrics

func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, 
                    didCollectDataOf collectedTypes: Set<HKSampleType>) {
    for type in collectedTypes {
        guard let quantityType = type as? HKQuantityType else { return }

        let statistics = workoutBuilder.statistics(for: quantityType)

        // Update the published values
        updateForStatistics(statistics)
    }
}
```

### Ending workout — [2:28]

```swift
// Stopping the workout session

session.stopActivity(with: .now)

// Session transitions to stopped then call end
func workoutSession(_ workoutSession: HKWorkoutSession,
                    didChangeTo toState: HKWorkoutSessionState,
                    from fromState: HKWorkoutSessionState,
                    date: Date) {
    guard change.newState == .stopped, let builder else { return }

    try await builder.endCollection(at: change.date)
    let finishedWorkout = try await builder.finishWorkout()
    session.end()
}
```

### Set up Siri Intent — [7:17]

```swift
// Create an INExtension within your main app

// Define an intent handler
public class IntentHandler: INExtension {

}

// Define the intents to support
extension IntentHandler: INStartWorkoutIntentHandling

extension IntentHandler: INPauseWorkoutIntentHandling

extension IntentHandler: INResumeWorkoutIntentHandling

extension IntentHandler: INEndWorkoutIntentHandling
```

### Handle the Siri intent — [7:32]

```swift
// Handle the intent

public func handle(intent: INStartWorkoutIntent) async -> INStartWorkoutIntentResponse {
    let state = await WorkoutManager.shared.state

    switch state {
    case .running, .paused, .prepared, .stopped:
        return INStartWorkoutIntentResponse(code: .failureOngoingWorkout, 
                                            userActivity: nil)
    default:
        break;
    }
    Task {
        await MainActor.run {
            // Handle the intents activity type and location
            WorkoutManager.shared.setWorkoutConfiguration(activityType: .running,   
                                                          location: .outdoor)
        }
    }
    return INStartWorkoutIntentResponse(code: .success, userActivity: nil)
 }
```

### App Delegate — [7:52]

```swift
// Implement an app delegate

// Create app delegate
class WorkoutsOniOSSampleAppDelegate: NSObject, UIApplicationDelegate {
    let handler = IntentHandler()

    func application(_ application: UIApplication, handlerFor intent: INIntent) -> Any? {
        return handler
    }
}

// Add app delegate to app
struct WorkoutsOniOSSampleApp: App {
    @UIApplicationDelegateAdaptor(WorkoutsOniOSSampleAppDelegate.self) var appDelegate

}
```

### Set up crash recovery — [9:09]

```swift
// App Delegate

func application(_ application: UIApplication,
                 configurationForConnecting connectingSceneSession: UISceneSession,
                 options: UIScene.ConnectionOptions) -> UISceneConfiguration {
    if options.shouldHandleActiveWorkoutRecovery {
        let store = HKHealthStore()
        store.recoverActiveWorkoutSession(completion: { (workoutSession, error) in
            // Handle error
            Task {
                await WorkoutManager.shared.recoverWorkout(recoveredSession: workoutSession)
            }
        })
    }
    let configuration = UISceneConfiguration(name: "Default Configuration", 
                                             sessionRole: connectingSceneSession.role)
    configuration.delegateClass = WorkoutsOniOSSampleAppSceneDelegate.self
    return configuration
}
```

### Recover the workout session — [9:25]

```swift
// Recover the workout for the session


func recoverWorkout(recoveredSession: HKWorkoutSession) {
    session = recoveredSession
    builder = recoveredSession.associatedWorkoutBuilder()
    session?.delegate = self
    builder?.delegate = self
    workoutConfiguration = recoveredSession.workoutConfiguration

    let dataSource = HKLiveWorkoutDataSource(healthStore: healthStore,                                                                  
                                             workoutConfiguration: workoutConfiguration)
    builder?.dataSource = dataSource
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/322/4/f9d00075-ebbe-458c-a1e6-597ff5d78a1b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/322/4/f9d00075-ebbe-458c-a1e6-597ff5d78a1b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/322) — developer.apple.com. Indexed for agent consumption._
