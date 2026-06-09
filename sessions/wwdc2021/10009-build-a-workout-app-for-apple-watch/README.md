---
id: "wwdc2021-10009"
event: "wwdc2021"
year: 2021
title: "Build a workout app for Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10009"
topics: ["SwiftUI & UI Frameworks", "Health & Fitness"]
platforms: ["watchOS"]
hasTranscript: true
---

# Build a workout app for Apple Watch

**Event:** WWDC21 · **Topic:** Health & Fitness · **Platforms:** watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10009](https://developer.apple.com/videos/play/wwdc2021/10009)

Build a workout app from scratch using SwiftUI and HealthKit during this code along. Learn how to support the Always On state using timelines to update workout metrics. Follow best design practices for workout apps.

**Keywords:** `⌚️`, `always-on`, `codealong`, `code-along`, `healthkit`, `hkworkoutsession`, `isluminancereduced`, `metrics`, `workout`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,944 words)

## Documentation & Resources

- [Build a workout app for Apple Watch](https://developer.apple.com/documentation/HealthKit/build-a-workout-app-for-apple-watch) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/build-a-workout-app-for-apple-watch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/build-a-workout-app-for-apple-watch.json

## Code Snippets

### StartView - import HealthKit — [3:17]

```swift
import HealthKit
```

### StartView - workoutTypes — [3:25]

```swift
var workoutTypes: [HKWorkoutActivityType] = [.cycling, .running, .walking]
```

### StartView - HKWorkoutActivityType identifiable and name — [3:26]

```swift
extension HKWorkoutActivityType: Identifiable {
    public var id: UInt {
        rawValue
    }

    var name: String {
        switch self {
        case .running:
            return "Run"
        case .cycling:
            return "Bike"
        case .walking:
            return "Walk"
        default:
            return ""
        }
    }
}
```

### StartView - body — [4:22]

```swift
List(workoutTypes) { workoutType in
    NavigationLink(
        workoutType.name,
        destination: Text(workoutType.name)
    ).padding(
        EdgeInsets(top: 15, leading: 5, bottom: 15, trailing: 5)
    )
}
.listStyle(.carousel)
.navigationBarTitle("Workouts")
```

### SessionPagingView - Tab enum and selection — [6:55]

```swift
@State private var selection: Tab = .metrics

enum Tab {
    case controls, metrics, nowPlaying
}
```

### SessionPagingView - TabView — [7:20]

```swift
TabView(selection: $selection) {
    Text("Controls").tag(Tab.controls)
    Text("Metrics").tag(Tab.metrics)
    Text("Now Playing").tag(Tab.nowPlaying)
}
```

### MetricsView - VStack and TextViews — [9:02]

```swift
VStack(alignment: .leading) {
    Text("03:15.23")
        .foregroundColor(Color.yellow)
        .fontWeight(.semibold)
    Text(
        Measurement(
            value: 47,
            unit: UnitEnergy.kilocalories
        ).formatted(
            .measurement(
                width: .abbreviated,
                usage: .workout,
                numberFormat: .numeric(precision: .fractionLength(0))
            )
        )
    )
    Text(
        153.formatted(
            .number.precision(.fractionLength(0))
        )
        + " bpm"
    )
    Text(
        Measurement(
            value: 515,
            unit: UnitLength.meters
        ).formatted(
            .measurement(
                width: .abbreviated,
                usage: .road
            )
        )
    )
}
.font(.system(.title, design: .rounded)
        .monospacedDigit()
        .lowercaseSmallCaps()
)
.frame(maxWidth: .infinity, alignment: .leading)
.ignoresSafeArea(edges: .bottom)
.scenePadding()
```

### ElapsedTimeView - ElapsedTimeView and ElapsedTimeFormatter — [11:42]

```swift
struct ElapsedTimeView: View {
    var elapsedTime: TimeInterval = 0
    var showSubseconds: Bool = true
    @State private var timeFormatter = ElapsedTimeFormatter()

    var body: some View {
        Text(NSNumber(value: elapsedTime), formatter: timeFormatter)
            .fontWeight(.semibold)
            .onChange(of: showSubseconds) {
                timeFormatter.showSubseconds = $0
            }
    }
}

class ElapsedTimeFormatter: Formatter {
    let componentsFormatter: DateComponentsFormatter = {
        let formatter = DateComponentsFormatter()
        formatter.allowedUnits = [.minute, .second]
        formatter.zeroFormattingBehavior = .pad
        return formatter
    }()
    var showSubseconds = true

    override func string(for value: Any?) -> String? {
        guard let time = value as? TimeInterval else {
            return nil
        }

        guard let formattedString = componentsFormatter.string(from: time) else {
            return nil
        }

        if showSubseconds {
            let hundredths = Int((time.truncatingRemainder(dividingBy: 1)) * 100)
            let decimalSeparator = Locale.current.decimalSeparator ?? "."
            return String(format: "%@%@%0.2d", formattedString, decimalSeparator, hundredths)
        }

        return formattedString
    }
}
```

### MetricsView - replace TextView with ElapsedTimeView — [13:56]

```swift
ElapsedTimeView(
    elapsedTime: 3 * 60 + 15.24,
    showSubseconds: true
).foregroundColor(Color.yellow)
```

### ControlsView - Stacks, Buttons and TextViews — [14:47]

```swift
HStack {
    VStack {
        Button {
        } label: {
            Image(systemName: "xmark")
        }
        .tint(Color.red)
        .font(.title2)
        Text("End")
    }
    VStack {
        Button {
        } label: {
            Image(systemName: "pause")
        }
        .tint(Color.yellow)
        .font(.title2)
        Text("Pause")
    }
}
```

### SessionPagingView - import WatchKit — [16:05]

```swift
import WatchKit
```

### SessionPagingView - TabView using actual views — [16:09]

```swift
ControlsView().tag(Tab.controls)
MetricsView().tag(Tab.metrics)
NowPlayingView().tag(Tab.nowPlaying)
```

### StartView - NavigationLink to use SessionPagingView — [17:08]

```swift
destination: SessionPagingView()
```

### SummaryView - SummaryMetricView — [17:50]

```swift
struct SummaryMetricView: View {
    var title: String
    var value: String

    var body: some View {
        Text(title)
        Text(value)
            .font(.system(.title2, design: .rounded)
                    .lowercaseSmallCaps()
            )
            .foregroundColor(.accentColor)
        Divider()
    }
}
```

### SummaryView - durationFormatter — [18:27]

```swift
@State private var durationFormatter: DateComponentsFormatter = {
    let formatter = DateComponentsFormatter()
    formatter.allowedUnits = [.hour, .minute, .second]
    formatter.zeroFormattingBehavior = .pad
    return formatter
}()
```

### SummaryView - body — [18:45]

```swift
ScrollView(.vertical) {
    VStack(alignment: .leading) {
        SummaryMetricView(
            title: "Total Time",
            value: durationFormatter.string(from: 30 * 60 + 15) ?? ""
        ).accentColor(Color.yellow)
        SummaryMetricView(
            title: "Total Distance",
            value: Measurement(
                value: 1625,
                unit: UnitLength.meters
            ).formatted(
                .measurement(
                    width: .abbreviated,
                    usage: .road
                )
            )
        ).accentColor(Color.green)
        SummaryMetricView(
            title: "Total Energy",
            value: Measurement(
                value: 96,
                unit: UnitEnergy.kilocalories
            ).formatted(
                .measurement(
                    width: .abbreviated,
                    usage: .workout,
                    numberFormat: .numeric(precision: .fractionLength(0))
                )
            )
        ).accentColor(Color.pink)
        SummaryMetricView(
            title: "Avg. Heart Rate",
            value: 143
                .formatted(
                    .number.precision(.fractionLength(0))
                )
            + " bpm"
        ).accentColor(Color.red)
        Button("Done") {
        }
    }
    .scenePadding()
}
.navigationTitle("Summary")
.navigationBarTitleDisplayMode(.inline)
```

### ActivityRingsView — [21:00]

```swift
import HealthKit
import SwiftUI

struct ActivityRingsView: WKInterfaceObjectRepresentable {
    let healthStore: HKHealthStore

    func makeWKInterfaceObject(context: Context) -> some WKInterfaceObject {
        let activityRingsObject = WKInterfaceActivityRing()

        let calendar = Calendar.current
        var components = calendar.dateComponents([.era, .year, .month, .day], from: Date())
        components.calendar = calendar

        let predicate = HKQuery.predicateForActivitySummary(with: components)

        let query = HKActivitySummaryQuery(predicate: predicate) { query, summaries, error in
            DispatchQueue.main.async {
                activityRingsObject.setActivitySummary(summaries?.first, animated: true)
            }
        }

        healthStore.execute(query)

        return activityRingsObject
    }

    func updateWKInterfaceObject(_ wkInterfaceObject: WKInterfaceObjectType, context: Context) {

    }
}
```

### SummaryView - add ActivityRingsView — [22:15]

```swift
Text("Activity Rings")
ActivityRingsView(
    healthStore: HKHealthStore()
).frame(width: 50, height: 50)
```

### SummaryView - import HealthKit — [22:28]

```swift
import HealthKit
```

### WorkoutManager — [25:22]

```swift
import HealthKit

class WorkoutManager: NSObject, ObservableObject {

}
```

### MyWorkoutsApp - add workoutManager @StateObject — [25:53]

```swift
@StateObject var workoutManager = WorkoutManager()
```

### MyWorkoutsApp - .environmentObject to NavigationView — [26:00]

```swift
.environmentObject(workoutManager)
```

### WorkoutManager - selectedWorkout — [26:25]

```swift
var selectedWorkout: HKWorkoutActivityType?
```

### StartView - add workoutManager — [26:49]

```swift
@EnvironmentObject var workoutManager: WorkoutManager
```

### StartView - Add tag and selection to NavigationLink — [26:56]

```swift
,
tag: workoutType,
selection: $workoutManager.selectedWorkout
```

### WorkoutManager - Add healthStore, session, builder — [27:32]

```swift
let healthStore = HKHealthStore()
var session: HKWorkoutSession?
var builder: HKLiveWorkoutBuilder?
```

### WorkoutManager - startWorkout(workoutType:) — [27:42]

```swift
func startWorkout(workoutType: HKWorkoutActivityType) {
    let configuration = HKWorkoutConfiguration()
    configuration.activityType = workoutType
    configuration.locationType = .outdoor

    do {
        session = try HKWorkoutSession(healthStore: healthStore, configuration: configuration)
        builder = session?.associatedWorkoutBuilder()
    } catch {
        // Handle any exceptions.
        return
    }

    builder?.dataSource = HKLiveWorkoutDataSource(
        healthStore: healthStore,
        workoutConfiguration: configuration
    )

    // Start the workout session and begin data collection.
    let startDate = Date()
    session?.startActivity(with: startDate)
    builder?.beginCollection(withStart: startDate) { (success, error) in
        // The workout has started.
    }
}
```

### WorkoutManager - selectedWorkout didSet — [29:06]

```swift
{
    didSet {
        guard let selectedWorkout = selectedWorkout else { return }
        startWorkout(workoutType: selectedWorkout)
    }
}
```

### WorkoutManager - requestAuthorization from HealthKit — [29:35]

```swift
// Request authorization to access HealthKit.
func requestAuthorization() {
    // The quantity type to write to the health store.
    let typesToShare: Set = [
        HKQuantityType.workoutType()
    ]

    // The quantity types to read from the health store.
    let typesToRead: Set = [
        HKQuantityType.quantityType(forIdentifier: .heartRate)!,
        HKQuantityType.quantityType(forIdentifier: .activeEnergyBurned)!,
        HKQuantityType.quantityType(forIdentifier: .distanceWalkingRunning)!,
        HKQuantityType.quantityType(forIdentifier: .distanceCycling)!,
        HKObjectType.activitySummaryType()
    ]

    // Request authorization for those quantity types.
    healthStore.requestAuthorization(toShare: typesToShare, read: typesToRead) { (success, error) in
        // Handle error.
    }
}
```

### StartView - requestAuthorization onAppear — [30:20]

```swift
.onAppear {
    workoutManager.requestAuthorization()
}
```

### Privacy - Health Share Usage Description - Key — [31:30]

```swift
NSHealthShareUsageDescription
```

### Privacy - Health Share Usage Description - Value — [31:38]

```swift
Your workout related data will be used to display your saved workouts in MyWorkouts.
```

### Privacy - Health Update Usage Description - Key — [31:47]

```swift
NSHealthUpdateUsageDescription
```

### Privacy - Health Update Usage Description - Value — [31:54]

```swift
Workouts tracked by MyWorkouts on Apple Watch will be saved to HealthKit.
```

### WorkoutManager - session state control — [33:29]

```swift
// MARK: - State Control

// The workout session state.
@Published var running = false

func pause() {
    session?.pause()
}

func resume() {
    session?.resume()
}

func togglePause() {
    if running == true {
        pause()
    } else {
        resume()
    }
}

func endWorkout() {
    session?.end()
}
```

### WorkoutManager - HKWorkoutSessionDelegate — [34:11]

```swift
// MARK: - HKWorkoutSessionDelegate
extension WorkoutManager: HKWorkoutSessionDelegate {
    func workoutSession(_ workoutSession: HKWorkoutSession,
                        didChangeTo toState: HKWorkoutSessionState,
                        from fromState: HKWorkoutSessionState,
                        date: Date) {
        DispatchQueue.main.async {
            self.running = toState == .running
        }

        // Wait for the session to transition states before ending the builder.
        if toState == .ended {
            builder?.endCollection(withEnd: date) { (success, error) in
                self.builder?.finishWorkout { (workout, error) in
                }
            }
        }
    }

    func workoutSession(_ workoutSession: HKWorkoutSession, didFailWithError error: Error) {

    }
}
```

### WorkoutManager - assign HKWorkoutSessionDelegate in startWorkout() — [34:58]

```swift
session?.delegate = self
```

### ControlsView - workoutManager environmentObject — [35:22]

```swift
@EnvironmentObject var workoutManager: WorkoutManager
```

### ControlsView - End Button action — [35:33]

```swift
workoutManager.endWorkout()
```

### ControlsView - Pause / Resume Button and Text — [35:43]

```swift
Button {
    workoutManager.togglePause()
} label: {
    Image(systemName: workoutManager.running ? "pause" : "play")
}
.tint(Color.yellow)
.font(.title2)
Text(workoutManager.running ? "Pause" : "Resume")
```

### SessionPagingView - add workoutManager environment variable — [36:30]

```swift
@EnvironmentObject var workoutManager: WorkoutManager
```

### SessionPagingView - navigationBar — [36:42]

```swift
.navigationTitle(workoutManager.selectedWorkout?.name ?? "")
.navigationBarBackButtonHidden(true)
.navigationBarHidden(selection == .nowPlaying)
```

### SessionPagingView - onChange of workoutManager.running — [37:10]

```swift
.onChange(of: workoutManager.running) { _ in
        displayMetricsView()
    }
}

private func displayMetricsView() {
    withAnimation {
        selection = .metrics
    }
}
```

### WorkoutManager - showingSummaryView — [37:45]

```swift
@Published var showingSummaryView: Bool = false {
    didSet {
        // Sheet dismissed
        if showingSummaryView == false {
            selectedWorkout = nil
        }
    }
}
```

### WorkoutManager - showingSummaryView true in endWorkout — [37:59]

```swift
showingSummaryView = true
```

### MyWorkoutApp - add summaryView sheet to NavigationView — [38:22]

```swift
.sheet(isPresented: $workoutManager.showingSummaryView) {
    SummaryView()
}
```

### SummaryView - add dismiss environment variable — [38:49]

```swift
@Environment(\.dismiss) var dismiss
```

### SummaryView - add dismiss() to done button — [38:58]

```swift
dismiss()
```

### WorkoutManager - Metric publishers — [40:25]

```swift
// MARK: - Workout Metrics
@Published var averageHeartRate: Double = 0
@Published var heartRate: Double = 0
@Published var activeEnergy: Double = 0
@Published var distance: Double = 0
```

### WorkoutManager - assigned as HKLiveWorkoutBuilderDelegate in startWorkout() — [40:48]

```swift
builder?.delegate = self
```

### WorkoutManager - add HKLiveWorkoutBuilderDelegate extension — [41:05]

```swift
// MARK: - HKLiveWorkoutBuilderDelegate
extension WorkoutManager: HKLiveWorkoutBuilderDelegate {
    func workoutBuilderDidCollectEvent(_ workoutBuilder: HKLiveWorkoutBuilder) {
    }

    func workoutBuilder(_ workoutBuilder: HKLiveWorkoutBuilder, didCollectDataOf collectedTypes: Set<HKSampleType>) {
        for type in collectedTypes {
            guard let quantityType = type as? HKQuantityType else { return }

            let statistics = workoutBuilder.statistics(for: quantityType)

            // Update the published values.
            updateForStatistics(statistics)
        }
    }
}
```

### WorkoutManager - add updateForStatistics() — [42:01]

```swift
func updateForStatistics(_ statistics: HKStatistics?) {
    guard let statistics = statistics else { return }

    DispatchQueue.main.async {
        switch statistics.quantityType {
        case HKQuantityType.quantityType(forIdentifier: .heartRate):
            let heartRateUnit = HKUnit.count().unitDivided(by: HKUnit.minute())
            self.heartRate = statistics.mostRecentQuantity()?.doubleValue(for: heartRateUnit) ?? 0
            self.averageHeartRate = statistics.averageQuantity()?.doubleValue(for: heartRateUnit) ?? 0
        case HKQuantityType.quantityType(forIdentifier: .activeEnergyBurned):
            let energyUnit = HKUnit.kilocalorie()
            self.activeEnergy = statistics.sumQuantity()?.doubleValue(for: energyUnit) ?? 0
        case HKQuantityType.quantityType(forIdentifier: .distanceWalkingRunning), HKQuantityType.quantityType(forIdentifier: .distanceCycling):
            let meterUnit = HKUnit.meter()
            self.distance = statistics.sumQuantity()?.doubleValue(for: meterUnit) ?? 0
        default:
            return
        }
    }
}
```

### MetricsView - add workoutManager as environment variable to MetricsView — [43:25]

```swift
@EnvironmentObject var workoutManager: WorkoutManager
```

### MetricsView - VStack with Text bound to workoutManager variables — [43:35]

```swift
VStack(alignment: .leading) {
    ElapsedTimeView(
        elapsedTime: workoutManager.builder?.elapsedTime ?? 0,
        showSubseconds: true
    ).foregroundColor(Color.yellow)
    Text(
        Measurement(
            value: workoutManager.activeEnergy,
            unit: UnitEnergy.kilocalories
        ).formatted(
            .measurement(
                width: .abbreviated,
                usage: .workout,
                numberFormat: .numeric(precision: .fractionLength(0))
            )
        )
    )
    Text(
        workoutManager.heartRate
            .formatted(
                .number.precision(.fractionLength(0))
            )
        + " bpm"
    )
    Text(
        Measurement(
            value: workoutManager.distance,
            unit: UnitLength.meters
        ).formatted(
            .measurement(
                width: .abbreviated,
                usage: .road
            )
        )
    )
}
```

### MetricsView - MetricsTimelineSchedule — [45:51]

```swift
private struct MetricsTimelineSchedule: TimelineSchedule {
    var startDate: Date

    init(from startDate: Date) {
        self.startDate = startDate
    }

    func entries(from startDate: Date, mode: TimelineScheduleMode) -> PeriodicTimelineSchedule.Entries {
        PeriodicTimelineSchedule(
            from: self.startDate,
            by: (mode == .lowFrequency ? 1.0 : 1.0 / 30.0)
        ).entries(
            from: startDate,
            mode: mode
        )
    }
}
```

### MetricsView - TimelineView wrapping VStack — [46:38]

```swift
TimelineView(
    MetricsTimelineSchedule(
        from: workoutManager.builder?.startDate ?? Date()
    )
) { context in
    VStack(alignment: .leading) {
        ElapsedTimeView(
            elapsedTime: workoutManager.builder?.elapsedTime ?? 0,
            showSubseconds: context.cadence == .live
        ).foregroundColor(Color.yellow)
        Text(
            Measurement(
                value: workoutManager.activeEnergy,
                unit: UnitEnergy.kilocalories
            ).formatted(
                .measurement(
                    width: .abbreviated,
                    usage: .workout,
                    numberFormat: .numeric(precision: .fractionLength(0))
                )
            )
        )
        Text(
            workoutManager.heartRate
                .formatted(
                    .number.precision(.fractionLength(0))
                )
            + " bpm"
        )
        Text(
            Measurement(
                value: workoutManager.distance,
                unit: UnitLength.meters
            ).formatted(
                .measurement(
                    width: .abbreviated,
                    usage: .road
                )
            )
        )
    }
    .font(.system(.title, design: .rounded)
            .monospacedDigit()
            .lowercaseSmallCaps()
    )
    .frame(maxWidth: .infinity, alignment: .leading)
    .ignoresSafeArea(edges: .bottom)
    .scenePadding()
}
```

### WorkoutManager - workout: HKWorkout added — [48:23]

```swift
@Published var workout: HKWorkout?
```

### WorkoutManager - assign HKWorkout in finishWorkout — [48:38]

```swift
DispatchQueue.main.async {
    self.workout = workout
}
```

### WorkoutManager - resetWorkout() — [48:57]

```swift
func resetWorkout() {
    selectedWorkout = nil
    builder = nil
    session = nil
    workout = nil
    activeEnergy = 0
    averageHeartRate = 0
    heartRate = 0
    distance = 0
}
```

### WorkoutManager - add resetWorkout to showingSummaryView didSet — [49:21]

```swift
resetWorkout()
```

### SummaryView - add workoutManager — [49:48]

```swift
@EnvironmentObject var workoutManager: WorkoutManager
```

### SummaryView - add ProgressView — [50:06]

```swift
if workoutManager.workout == nil {
    ProgressView("Saving workout")
        .navigationBarHidden(true)
} else {
    ScrollView(.vertical) {
        VStack(alignment: .leading) {
            SummaryMetricView(
                title: "Total Time",
                value: durationFormatter.string(from: 30 * 60 + 15) ?? ""
            ).accentColor(Color.yellow)
            SummaryMetricView(
                title: "Total Distance",
                value: Measurement(
                    value: 1625,
                    unit: UnitLength.meters
                ).formatted(
                    .measurement(
                        width: .abbreviated,
                        usage: .road
                    )
                )
            ).accentColor(Color.green)
            SummaryMetricView(
                title: "Total Calories",
                value: Measurement(
                    value: 96,
                    unit: UnitEnergy.kilocalories
                ).formatted(
                    .measurement(
                        width: .abbreviated,
                        usage: .workout,
                        numberFormat: .numeric(precision: .fractionLength(0))
                    )
                )
            ).accentColor(Color.pink)
            SummaryMetricView(
                title: "Avg. Heart Rate",
                value: 143.formatted(
                    .number.precision(.fractionLength(0))
                )
                + " bpm"
            )
            Text("Activity Rings")
            ActivityRingsView(healthStore: workoutManager.healthStore)
                .frame(width: 50, height: 50)
            Button("Done") {
                dismiss()
            }
        }
        .scenePadding()
    }
    .navigationTitle("Summary")
    .navigationBarTitleDisplayMode(.inline)
}
```

### SummaryView - SummaryMetricViews using HKWorkout values — [50:43]

```swift
SummaryMetricView(
    title: "Total Time",
    value: durationFormatter
        .string(from: workoutManager.workout?.duration ?? 0.0) ?? ""
).accentColor(Color.yellow)
SummaryMetricView(
    title: "Total Distance",
    value: Measurement(
        value: workoutManager.workout?.totalDistance?
            .doubleValue(for: .meter()) ?? 0,
        unit: UnitLength.meters
    ).formatted(
        .measurement(
            width: .abbreviated,
            usage: .road
        )
    )
).accentColor(Color.green)
SummaryMetricView(
    title: "Total Energy",
    value: Measurement(
        value: workoutManager.workout?.totalEnergyBurned?
                        .doubleValue(for: .kilocalorie()) ?? 0,
        unit: UnitEnergy.kilocalories
    ).formatted(
        .measurement(
            width: .abbreviated,
            usage: .workout,
            numberFormat: .numeric(precision: .fractionLength(0))
        )
    )
).accentColor(Color.pink)
SummaryMetricView(
    title: "Avg. Heart Rate",
    value: workoutManager.averageHeartRate
        .formatted(
            .number.precision(.fractionLength(0))
        )
    + " bpm"
).accentColor(Color.red)
```

### SessionPagingView - add isLuminanceReduced — [51:45]

```swift
@Environment(\.isLuminanceReduced) var isLuminanceReduced
```

### SessionPagingView - add tabViewStyle and onChangeOf based on isLuminanceReduced — [51:57]

```swift
.tabViewStyle(
    PageTabViewStyle(indexDisplayMode: isLuminanceReduced ? .never : .automatic)
)
.onChange(of: isLuminanceReduced) { _ in
    displayMetricsView()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10009/4/C77618B9-A832-406C-89F0-933F2139F0AD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10009/4/C77618B9-A832-406C-89F0-933F2139F0AD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10009) — developer.apple.com. Indexed for agent consumption._
