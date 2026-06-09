---
id: "wwdc2021-10087"
event: "wwdc2021"
year: 2021
title: "Diagnose Power and Performance regressions in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10087"
topics: ["App Store, Distribution & Marketing", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Diagnose Power and Performance regressions in your app

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10087](https://developer.apple.com/videos/play/wwdc2021/10087)

Quickly discover how to identify priorities when viewing power and performance regressions. Learn how to track metrics that have regressed with device-and percentile-specific information, so you can focus your efforts on optimization and save valuable development time. We’ll also show you how to track down common anti-patterns in your app that wear out device storage, help you customize your workflows, and add App Store Connect APIs to help you stay up to date on your app’s real-world performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,326 words)

## Documentation & Resources

- [Reducing terminations in your app](https://developer.apple.com/documentation/Xcode/reduce-terminations-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/reduce-terminations-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/reduce-terminations-in-your-app.json
- [Analyzing the performance of your shipping app](https://developer.apple.com/documentation/Xcode/analyzing-the-performance-of-your-shipping-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-the-performance-of-your-shipping-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-the-performance-of-your-shipping-app.json
- [Measuring App Performance](https://developer.apple.com/app-store/measuring-app-performance/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/app-store/measuring-app-performance/
- [MetricKit](https://developer.apple.com/documentation/MetricKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetricKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetricKit.json
- [App Store Connect API](https://developer.apple.com/documentation/AppStoreConnectAPI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppStoreConnectAPI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppStoreConnectAPI.json

## Code Snippets

### App Store Connect API Metrics — [13:00]

```bash
GET /v1/apps/{application-id}/perfPowerMetrics
GET /v1/builds/{id}/perfPowerMetrics
```

### App Store Connect API Diagnostics — [13:01]

```bash
GET /v1/builds/{id}/diagnosticSignatures
GET /v1/diagnosticSignatures/{id}/logs
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10087/6/35272A76-3FD8-4149-B4C9-B7C0AA197E61/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10087/6/35272A76-3FD8-4149-B4C9-B7C0AA197E61/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10087) — developer.apple.com. Indexed for agent consumption._
