---
id: "wwdc2024-10212"
event: "wwdc2024"
year: 2024
title: "What’s new in location authorization"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10212"
topics: ["Privacy & Security", "Maps & Location"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in location authorization

**Event:** WWDC24 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10212](https://developer.apple.com/videos/play/wwdc2024/10212)

Location authorization is turning 2.0. Learn about new recommendations and techniques to get the authorization you need, and a new system of diagnostics that can let you know when an authorization goal can’t be met.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,049 words)

## Documentation & Resources

- [Configuring your app to use location services](https://developer.apple.com/documentation/CoreLocation/configuring-your-app-to-use-location-services) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreLocation/configuring-your-app-to-use-location-services
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreLocation/configuring-your-app-to-use-location-services.json
- [Adopting live updates in Core Location](https://developer.apple.com/documentation/CoreLocation/adopting-live-updates-in-core-location) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreLocation/adopting-live-updates-in-core-location
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreLocation/adopting-live-updates-in-core-location.json
- [Forum: Maps & Location](https://developer.apple.com/forums/topics/maps-and-location?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/maps-and-location?cid=vf-a-0010

## Code Snippets

### CLLocationUpdate and CLMonitor — [0:31]

```swift
// Iterating liveUpdates to reflect current location
Task {
    let updates = CLLocationUpdate.liveUpdates()
    for try await update in updates {
        if let loc = update.location {
            updateLocationUI(location: loc)
        }
    }
}

// Iterating monitor events to report condition state changes
Task {
    let monitor = await CLMonitor(monitorName)
    await monitor.add(CLMonitor.CircularGeographicCondition(center: applePark, radius: 50),
                      identifier: "ApplePark")

    for try await event in await monitor.events {
        updateConditionsUI(for: event.identifier, state: event.state)
    }
}
```

### Handle updates with CLLocationManagerDelegate — [0:52]

```swift
// Adapting location authorization to Swift with a MainActor singleton
@MainActor class LocationReflector: NSObject, CLLocationManagerDelegate, ObservableObject {
    static let shared = LocationReflector()
    private let manager = CLLocationManager()

    override init() {
        super.init()
        manager.delegate = self
    }

    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager){
        if (manager.authorizationStatus == .notDetermined) {
            manager.requestWhenInUseAuthorization()
        }
    }

    func locationManager(_ manager: CLLocationManager,
                         didUpdateLocations locations:[CLLocation]) {
        // Process locations[0]
    }
    // ...
}
```

### CLServiceSession simplifies — [1:07]

```swift
// CLServiceSession in action

Task {
    let session = CLServiceSession(authorization: .whenInUse)

    for try await update in CLLocationUpdate.liveUpdates {
        // Process update.location or update.authorizationDenied
    }
}
```

### Implicit service sessions — [7:15]

```swift
// CLServiceSession in action

Task {
    let session = CLServiceSession(authorization: .whenInUse)

    for try await update in CLLocationUpdate.liveUpdates {
        // Process update.location or update.authorizationDenied
    }
}
```

### Implicit service sessions — [7:34]

```swift
Task {
    for try await update in CLLocationUpdate.liveUpdates {
        // Process update.location or update.authorizationDenied
    }
}
```

### Diagnostics – Following the progress of location authorization — [13:37]

```swift
// Following the progress of location authorization with CLServiceSession
let mySession = CLServiceSession(authorization:.whenInUse)

for try await diagnostic in mySession.diagnostics {
    if (diagnostic.authorizationDenied) {
        // Ok, let’s let them pick a location instead?
    }
}
```

### Diagnostics – Following the progress of location authorization — [15:00]

```swift
// Following the progress of location authorization with CLServiceSession
let mySession = CLServiceSession(authorization:.whenInUse)

for try await diagnostic in mySession.diagnostics {
    if (!diagnostic.authorizationRequestInProgress) {
        // They’ve decided (maybe already).  We can move on!
        break
    }
}
```

### Diagnostics – Following the progress of location authorization — [15:25]

```swift
// Following the progress of location authorization with CLServiceSession
let mySession = CLServiceSession(authorization:.whenInUse)

for try await diagnostic in mySession.diagnostics {
    if (!diagnostic.authorizationRequestInProgress) {
       reactToChanges(authorized:!diagnostic.authorizationDenied)
    }
}
```

### Diagnostics – Following the progress of location authorization — [15:46]

```swift
// Following the progress of location authorization with CLServiceSession
Task {
    let mySession = CLServiceSession(authorization:.whenInUse)

    for try await diagnostic in mySession.diagnostics {
        if (!diagnostic.authorizationRequestInProgress) {
            reactToChanges(authorized:!diagnostic.authorizationDenied)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10212/4/4E06515C-912A-4159-8C07-9468D1209F8F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10212/4/4E06515C-912A-4159-8C07-9468D1209F8F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10212) — developer.apple.com. Indexed for agent consumption._