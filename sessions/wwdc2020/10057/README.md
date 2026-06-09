---
id: "wwdc2020-10057"
event: "wwdc2020"
year: 2020
title: "Identify trends with the Power and Performance API"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10057"
topics: ["Developer Tools", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Identify trends with the Power and Performance API

**Event:** WWDC20 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10057](https://developer.apple.com/videos/play/wwdc2020/10057)

Track your app’s performance metrics in custom team dashboards, bug reporting systems, and other custom workflows with the Power and Performance Metrics and Diagnostics API. Explore how you can access the same data that drives the Power and Performance analysis tools in Xcode to quickly identify trends and regressions. Learn how to leverage diagnostic signatures and logs — including call stack trees — to prioritize and debug issues. And discover how you can integrate this API with your development team’s existing tools to troubleshoot issues quickly, offering better overall performance for people who use your app.

**Keywords:** `analytics`, `app store connect`, `automation`, `diagnostics`, `insights`, `json`, `metrics`, `web api`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,004 words)

## Code Snippets

### Get metrics and insights for most recent app versions — [4:48]

```swift
GET /v1/apps/{id}/perfPowerMetrics
```

### Get top diagnostic signatures for released app versions — [8:19]

```swift
GET /v1/builds/{id}/diagnosticSignatures
```

### Get logs for a diagnostic signature — [9:42]

```swift
GET /v1/diagnosticSignatures/{id}/logs
```

### Access perfPowerMetrics for an app — [11:19]

```bash
curl -X GET -H "Authorization: Bearer ${JWT}" -H "Accept: application/vnd.apple.xcode-metrics+json,application/json" https://api.appstoreconnect.apple.com/v1/apps/${id}/perfPowerMetrics
```

### Access diagnosticSignatures for an app build — [12:23]

```bash
curl -X GET -H "Authorization: Bearer ${JWT}" -H "Accept: application/vnd.apple.xcode-metrics+json,application/json" https://api.appstoreconnect.apple.com/v1/builds/${id}/diagnosticSignatures
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10057/3/138E68BD-E9B2-4980-8CF7-738D58F9959D/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10057) — developer.apple.com. Indexed for agent consumption._