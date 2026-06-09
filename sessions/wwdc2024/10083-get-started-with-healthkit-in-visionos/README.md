---
id: "wwdc2024-10083"
event: "wwdc2024"
year: 2024
title: "Get started with HealthKit in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10083"
topics: ["Spatial Computing", "Health & Fitness"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Get started with HealthKit in visionOS

**Event:** WWDC24 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10083](https://developer.apple.com/videos/play/wwdc2024/10083)

Discover how to use HealthKit to create experiences that take full advantage of the spatial canvas. Learn the capabilities of HealthKit on the platform, find out how to bring an existing iPadOS app to visionOS, and explore the special considerations governing HealthKit during a Guest User session. You’ll also learn ways to use SwiftUI, Swift Charts, and Swift concurrency to craft innovative experiences with HealthKit.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,985 words)

## Documentation & Resources

- [Visualizing HealthKit State of Mind in visionOS](https://developer.apple.com/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/visualizing-healthkit-state-of-mind-in-visionos.json
- [Let others use your Apple Vision Pro](https://support.apple.com/guide/apple-vision-pro/let-others-use-your-apple-vision-pro-dev57f3c667e/visionos) _documentation_
- [Forum: Health & Fitness](https://developer.apple.com/forums/topics/health-and-fitness?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/health-and-fitness?cid=vf-a-0010
- [Bringing multiple windows to your SwiftUI app](https://developer.apple.com/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app.json
- [HealthKit](https://developer.apple.com/documentation/HealthKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit.json

## Code Snippets

### Check whether health data is available — [2:43]

```swift
import HealthKit

if HKHealthStore.isHealthDataAvailable() {
    // Configure HealthKit-powered experiences
} else {
    // Omit HealthKit experiences
}
```

### Request authorization to read or write data — [3:03]

```swift
import HealthKitUI
import SwiftUI

func healthDataAccessRequest(
    store: HKHealthStore,
    shareTypes: Set<HKSampleType>,
    readTypes: Set<HKObjectType>? = nil,
    trigger: some Equatable,
    completion: @escaping (Result<Bool, any Error>) -> Void
) -> some View
```

### Update number of chart points based on chart’s size — [5:59]

```swift
// Update number of chart points based on chart’s size

import SwiftUI
import HealthKit
import Charts

struct ChartView: View {
    @State var chartBinCount: Int

    var body: some View {
        Chart { ...
            // Chart body
        }
        .onGeometryChange(for: Int.self) { proxy in // Observe for changes to the chart’s size
            Int(proxy.size.width / 80) // 80 points per chart point
        } action: { newValue in
            // Update the number of chart points
            chartBinCount = newValue        
        }
    }
}
```

### Open chart as a new window — [6:33]

```swift
// Opens chart as a new window

struct NewChartViewerButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open In New Window", systemImage: "plus.rectangle.on.rectangle") {
            openWindow(id: "chart-viewer-window")
        }
    }
}
```

### HealthKit returns a new error if a write is attempted during a Guest User session — [9:00]

```swift
let sample = HKStateOfMind(date: date, kind: .momentaryEmotion, valence: valence,
                           labels: [label], associations: [association])
do {
    try await healthStore.save(sample)
} catch {
    switch error {
    case HKError.errorNotPermissibleForGuestUserMode:
        // Drop data generated in a Guest User session
    default:
        // Existing error handling
    }
}
```

### Request authorization to State of Mind datatype — [9:26]

```swift
// Request authorization to State of Mind datatype

@main
struct HKStateOfMindDataSampleApp: App {
    @State var toggleHealthDataAuthorization = false
    @State var healthDataAuthorized: Bool?

    var body: some Scene {
        WindowGroup {
            TabView { ... }
                .healthDataAccessRequest(store: healthStore,
                                         shareTypes: [.stateOfMindType()],
                                         readTypes: [.stateOfMindType()],
                                         trigger: toggleHealthDataAuthorization) { result in
                    switch result {
                    case .success: healthDataAuthorized = true
                    case .failure(let error as HKError):
                        switch (error.code) {
                        case .errorNotPermissibleForGuestUserMode:
                            // Defer requests for a later time
                        default:
                            // Existing error handling
                        }
                        ...
                    }
                }
        }
    }
}
```

### Save a State of Mind sample from an emoji type — [9:42]

```swift
// Saves a State of Mind sample from an emoji type 
public func saveSample(date: Date,
                       association: HKStateOfMind.Association,
                       healthStore: HKHealthStore,
                       didError: Binding<Bool>) async -> SaveDetails? {
    do {
        let sample = createSample(date: date, association: association)
        try await healthStore.save(sample)
    } catch {
        switch error {
        case HKError.errorNotPermissibleForGuestUserMode:
            // Drop data you generate in a Guest User session.
            didError.wrappedValue = true
            return SaveDetails(errorString: "Health data is not saved for Guest Users.")
        default:
            // Existing error handling.
            didError.wrappedValue = true
            return SaveDetails(errorString: "Health data could not be saved: \(error)")
        }
    }
...
```

### Present an alert with a message using the given details — [9:58]

```swift
// Present an alert with a message using the given details

struct EventView: View {
    @State private var showAlert: Bool = false
    @State private var saveDetails: EmojiType.SaveDetails? = nil

    var body: some View {
        EmojiPicker()
            .alert("Unable to Save Health Data",
                   isPresented: $showAlert,
                   presenting: saveDetails,
                   actions: { _ in }, // default OK button
                   message: { details in
                Text(details.errorString)
            })
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10083/4/3EDC61A5-EEBF-48EB-9CB9-9AC6F587005E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10083/4/3EDC61A5-EEBF-48EB-9CB9-9AC6F587005E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10083) — developer.apple.com. Indexed for agent consumption._
