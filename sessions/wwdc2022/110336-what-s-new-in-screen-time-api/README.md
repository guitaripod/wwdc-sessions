---
id: "wwdc2022-110336"
event: "wwdc2022"
year: 2022
title: "What's new in Screen Time API"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110336"
topics: ["App Services", "Business & Education", "Essentials", "System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in Screen Time API

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110336](https://developer.apple.com/videos/play/wwdc2022/110336)

Find out how you can build apps that help people manage their relationship with their device — all while putting privacy first. We’ll take you through the Screen Time API and share how you can use features like core restrictions and device activity reports to create great experiences while providing measurable control for the device’s owner, parents, and guardians.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,580 words)

## Documentation & Resources

- [Managed Settings](https://developer.apple.com/documentation/ManagedSettings) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ManagedSettings
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ManagedSettings.json
- [Family Controls](https://developer.apple.com/documentation/FamilyControls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FamilyControls
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FamilyControls.json
- [Device Activity](https://developer.apple.com/documentation/DeviceActivity) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceActivity
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceActivity.json

## Code Snippets

### Request aAhuthorization — [3:12]

```swift
// APP: Request Authorization

import SwiftUI
import FamilyControls

@main
struct Worklog: App {
    let center = AuthorizationCenter.shared
    var body: some Scene {
        WindowGroup {
            VStack {…}
                .onAppear {
                    Task {
                        do {
                            try await center.requestAuthorization(for: .individual)
                        } catch {
                            print("Failed to enroll Aniyah with error: \(error)")
                        }
                    }
                }
        }
    }
```

### Managed settings store — [5:13]

```swift
// MONITOR EXTENSION: Handle Social category at start/end of interval

import DeviceActivity
import ManagedSettings

class WorklogMonitor: DeviceActivityMonitor {
    let database = BarkDatabase()
    override func intervalDidStart(for activity: DeviceActivityName) {
        super.intervalDidStart(for: activity)
        let socialStore = ManagedSettingsStore(named: .social)
        socialStore.clearAllSettings()
    }

    override func intervalDidEnd(for activity: DeviceActivityName) {
        super.intervalDidEnd(for: activity)
        let socialStore = ManagedSettingsStore(named: .social)
        let socialCategory = database.socialCategoryToken
        socialStore.shield.applicationCategories = .specific([socialCategory])
        socialStore.shield.webDomainCategories = .specific([socialCategory])
    }
}
```

### Device activity report and filter — [7:02]

```swift
// APP: Top-level view

import SwiftUI
import DeviceActivity

extension DeviceActivityReport.Context {
    static let pieChart = Self(“Pie Chart")
}

@main
struct Worklog: App {
    private let thisWeek = DateInterval(...)
    @State private var context: DeviceActivityReport.Context = .pieChart
    @State private var filter = DeviceActivityFilter(segment: .daily(during: thisWeek))

    var body: some Scene {
        WindowGroup {
            GeometryReader { geometry in
                VStack(alignment: .leading) {
                   DeviceActivityReport(context: context, filter: filter)
                        .frame(height: geometry.size.height * 0.75)


    }
}
```

### Device activity report — [7:24]

```swift
// REPORT EXTENSION: Configure Custom Device Activity Report

import SwiftUI
import DeviceActivity

struct PieChartReport: DeviceActivityReportScene {
    let context: DeviceActivityReport.Context = .pieChart
    let content: (PieChartView.Configuration) -> PieChartView

    func makeConfiguration(representing data: [DeviceActivityData]) 
        -> PieChartView.Configuration {
        var totalUsageByCategory: [ActivityCategory:TimeInterval]
        totalUsageByCategory = data.map(…)

        return PieChartView.Configuration(totalUsageByCategory: totalUsageByCategory)
    }
}
```

### Configure Custom Device Activity Report — [7:55]

```swift
// REPORT EXTENSION: Configure Custom Device Activity Report

import SwiftUI
import DeviceActivity

struct PieChartView: View {
    struct Configuration {
        let totalUsageByCategory: [ActivityCategory:TimeInterval]
    }

    let configuration: Configuration

    var body: some View {
        // A complex view that renders a bar graph based on Aniyah’s usage per category.
        PieChart(usage: configuration.totalUsageByCategory)
    }
}
```

### Present custom report — [8:05]

```swift
// REPORT EXTENSION: Draw Custom Device Activity Report

import SwiftUI
import DeviceActivity

@main
struct WorklogReportExtension: DeviceActivityReportExtension {
    var body: some DeviceActivityReportScene {
        PieChartReport { configuration in
            PieChartView(configuration: configuration)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110336/4/DB808128-449E-420A-9FA1-E5CF7403B7FD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110336/4/DB808128-449E-420A-9FA1-E5CF7403B7FD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110336) — developer.apple.com. Indexed for agent consumption._
