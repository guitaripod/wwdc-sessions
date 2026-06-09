---
id: "wwdc2021-10203"
event: "wwdc2021"
year: 2021
title: "Triage TestFlight crashes in Xcode Organizer"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10203"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Triage TestFlight crashes in Xcode Organizer

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10203](https://developer.apple.com/videos/play/wwdc2021/10203)

Learn how Xcode Organizer makes it easier and faster to triage and fix crashes. We'll explore how you can get access to crash information and feedback from your TestFlight testers just moments after they occur. And we'll show you how to analyze crashes, view metrics, and even share crash information among your team. For a primer on crash logs, we recommend watching “Understanding Crashes and Crash Logs” from WWDC18.

**Keywords:** `app store`, `debugging`, `metrickit`, `testing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,715 words)

## Documentation & Resources

- [Diagnosing issues using crash reports and device logs](https://developer.apple.com/documentation/Xcode/diagnosing-issues-using-crash-reports-and-device-logs) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/diagnosing-issues-using-crash-reports-and-device-logs
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/diagnosing-issues-using-crash-reports-and-device-logs.json

## Code Snippets

### Using MetricKit — [14:02]

```swift
//  Capture crash logs in your code

import MetricKit

class Subscriber: NSObject {
    override init() {
        super.init()
        MXMetricManager.shared.add(self)
    }

    deinit {
        MXMetricManager.shared.remove(self)
    }
}

extension Subscriber: MXMetricManagerSubscriber {
    func didReceive(_ payloads: [MXDiagnosticPayload]) {
        payloads.forEach {
            if let crashDiagnostics = $0.crashDiagnostics {
                // Begin analyzing crash diagnostic payload.      
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10203/7/1A8E1E96-00E5-4E9C-B392-6A2AE2AED9ED/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10203/7/1A8E1E96-00E5-4E9C-B392-6A2AE2AED9ED/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10203) — developer.apple.com. Indexed for agent consumption._
