---
id: "wwdc2023-10180"
event: "wwdc2023"
year: 2023
title: "Discover streamlined location updates"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10180"
topics: ["App Services", "Maps & Location"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Discover streamlined location updates

**Event:** WWDC23 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10180](https://developer.apple.com/videos/play/wwdc2023/10180)

Move into the future with Core Location! Meet the CLLocationUpdate class, designed for modern Swift concurrency, and learn how it simplifies getting location updates. We’ll show you how this class works with your apps when they run in the foreground or background and share some best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,025 words)

## Documentation & Resources

- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/CoreLocation/monitoring-location-changes-with-core-location) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreLocation/monitoring-location-changes-with-core-location
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreLocation/monitoring-location-changes-with-core-location.json
- [Adopting live updates in Core Location](https://developer.apple.com/documentation/corelocation/adopting_live_updates_in_core_location) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/corelocation/adopting_live_updates_in_core_location
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/corelocation/adopting_live_updates_in_core_location.json
- [Core Location](https://developer.apple.com/documentation/CoreLocation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreLocation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreLocation.json

## Code Snippets

### Getting location updates is easy! — [0:26]

```swift
for try await update in CLLocationUpdate.liveUpdates() {
    print("My current location : \(update.location)")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10180/3/BF2CDA20-2D8F-46B8-B850-E1799030451B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10180/3/BF2CDA20-2D8F-46B8-B850-E1799030451B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10180) — developer.apple.com. Indexed for agent consumption._
