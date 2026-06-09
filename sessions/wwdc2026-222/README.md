# Meet the new MetricKit

**Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-222](https://developer.apple.com/videos/play/wwdc2026/222)

Find and fix performance problems faster than ever. Join us to explore how MetricKit equips you with vital performance metrics and actionable diagnostics to help you understand exactly where your app has opportunities for improvements. We’ll also cover how to intersect your app’s metrics and diagnostics by app state by using the StateReporting framework, providing you with the full picture to investigate optimizations in your app’s experience.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Getting started with StateReporting](https://developer.apple.com/documentation/StateReporting/getting-started-with-statereporting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StateReporting/getting-started-with-statereporting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StateReporting/getting-started-with-statereporting.json
- [Analyzing app performance with MetricKit](https://developer.apple.com/documentation/MetricKit/analyzing-app-performance-with-metrickit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit/analyzing-app-performance-with-metrickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit/analyzing-app-performance-with-metrickit.json
- [Monitoring app performance with MetricKit](https://developer.apple.com/documentation/MetricKit/monitoring-app-performance-with-metrickit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit/monitoring-app-performance-with-metrickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit/monitoring-app-performance-with-metrickit.json
- [Track performance by app state using MetricKit](https://developer.apple.com/documentation/MetricKit/track-performance-by-app-state-using-metrickit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit/track-performance-by-app-state-using-metrickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit/track-performance-by-app-state-using-metrickit.json
- [MetricKit](https://developer.apple.com/documentation/MetricKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit.json

## Code Snippets

### Receive metrics from MetricKit — [4:59]

```swift
// Receive metrics from MetricKit

import MetricKit

let manager = MetricManager()

for await report in manager.metricReports {
    processReport(report)
}
```

### Send your metrics to the server — [5:25]

```swift
// Send your metrics to the server

import MetricKit

for await report in manager.metricReports {
    let jsonData = try JSONEncoder().encode(report)
    sendToServer(jsonData)
}
```

### Access your performance metrics — [5:44]

```swift
// Access your performance metrics

import MetricKit

for await report in manager.metricReports {
    let intervalEntries = report.intervalEntries
    let fullDayEntry = intervalEntries.fullDayEntry

    for entry in intervalEntries {
        let memoryMetrics = entry.values.filter { $0.metricGroup == .memory }

        for metric in memoryMetrics {
            switch metric {
            case .peakMemory(let peak):
                processPeakMemory(peak)
            default: break
            }
        }
    }
}
```

### Receive diagnostics — [8:59]

```swift
// Receive diagnostics

import MetricKit

let manager = MetricManager()

for await report in manager.diagnosticReports {
    processReport(report)
}
```

### Send your diagnostic data to the server — [9:14]

```swift
// Send your diagnostic data to the server

import MetricKit

for await report in manager.diagnosticReports {
    let jsonData = try JSONEncoder().encode(report)
    sendToServer(jsonData)
}
```

### Access your diagnostic data — [9:39]

```swift
// Access your diagnostic data

import MetricKit

for await report in manager.diagnosticReports {
    switch report.result {
    case .crash(let crash):
        let backtrace = crash.callStackTree
        let reason = crash.terminationReason
        let category = crash.terminationCategory
        processCrash(backtrace: backtrace, reason: reason, category: category)
    case .hang(let hang):
        processHangDiagnostic(hang)
    default: break
    }
}
```

### Receive MetricKit data with states — [13:57]

```swift
// Receive MetricKit data with states

import MetricKit
import StateReporting

let domain = StateReportingDomain("com.metrickitsample.tabs")
let manager = MetricManager(enabledStateReportingDomains: [domain])


// Report transitions throughout the app

let reporter = StateReporter.reporter(for: domain.rawValue)
reporter.reportTransition(to: "Reports")
```

### Define custom structured types — [14:21]

```swift
// Define custom structured types

import StateReporting

@ReportableMetadata
struct ViewConfiguration {
    let listSize: String
    let isSorted: Bool
}

let reporter = StateReporter.reporter(
    for: domain.rawValue,
    stableMetadata: ViewConfiguration.self
)

reporter.reportTransition(
    to: "Reports",
    stableMetadata: ViewConfiguration(listSize: "large", isSorted: false)
)
```

### Send encoded metric reports to the server — [15:29]

```swift
// Send encoded metric reports to the server

import MetricKit

for await report in manager.metricReports {
    let encoder = JSONEncoder()

    let formatKey = MetricReport.encodingFormatKey
    encoder.userInfo[formatKey] = MetricReport.EncodingFormat.byStateReportingDomain

    let jsonData = try encoder.encode(report)
    sendToServer(jsonData)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/222/4/86b76599-f095-4bd8-8004-f1dbd1bacb84/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._