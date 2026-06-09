---
id: "wwdc2020-10081"
event: "wwdc2020"
year: 2020
title: "What's new in MetricKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10081"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in MetricKit

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10081](https://developer.apple.com/videos/play/wwdc2020/10081)

Quickly detect power and performance regressions and troubleshoot app issues when you adopt MetricKit. Discover the latest trackable metrics for your app, including CPU instructions, animation hitches, and exit reasons. And learn about diagnostics in MetricKit that can help you troubleshoot hangs, crashes, and disk writes.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,205 words)

## Code Snippets

### Using MetricKit — [2:11]

```swift
import MetricKit

class MySubscriber: NSObject, MXMetricManagerSubscriber {

    var metricManager: MXMetricManager?

    override init() {
        super.init()
        metricManager = MXMetricManager.shared
        metricManager?.add(self)
    }

    override deinit() {
        metricManager?.remove(self)
    }

    func didReceive(_ payload: [MXMetricPayload]) {
        for metricPayload in payload {
            // Do something with metricPayload.
        }
    }

}
```

### Adopting MetricKit Diagnostics — [8:14]

```swift
func didReceive(_ payload: [MXDiagnosticPayload]) {
    for diagnosticPayload in payload {
        // Consume diagnosticPayload.
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10081/3/7AC69CDE-C614-4237-9C10-93A3B67C923E/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10081) — developer.apple.com. Indexed for agent consumption._