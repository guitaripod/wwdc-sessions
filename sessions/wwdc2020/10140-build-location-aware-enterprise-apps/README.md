---
id: "wwdc2020-10140"
event: "wwdc2020"
year: 2020
title: "Build location-aware enterprise apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10140"
topics: ["Accessibility & Inclusion", "Maps & Location", "Business & Education"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build location-aware enterprise apps

**Event:** WWDC20 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10140](https://developer.apple.com/videos/play/wwdc2020/10140)

Develop location-aware enterprise apps for your business and personalize your employee’s everyday experience. Learn how Apple built the Caffe Macs app for its on-campus cafeterias using iBeacons and Location Services and how you can apply these tools and frameworks to your own apps, while preserving employee privacy. From there, discover how you can use localization to deliver a great experience for your international employees.

**Keywords:** `core location`, `enterprise`, `ibeacon`, `internationalization`, `localization`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,283 words)

## Code Snippets

### Preferences: User-defined Preferred Location — [3:28]

```swift
// Storing the user’s preference using UserDefaults

UserDefaults.standard.set(defaultLocation.id, forKey: "defaultLocationId")

let defaultLocationId = UserDefaults.standard.integer(forKey: "defaultLocationId")
```

### Location Services: Requesting Authorization — [6:14]

```swift
// Add NSLocationWhenInUseUsageDescription to your Info.plist 
// e.g. “Location is required for placing orders while using the app."

locationManager.requestWhenInUseAuthorization()

func locationManager(
    _ manager: CLLocationManager,
    didChangeAuthorization status: CLAuthorizationStatus) {

    switch status {
    case .restricted, .denied: 
        disableLocationFeatures()

    case .authorizedWhenInUse, .authorizedAlways: 
        enableLocationFeatures()

    case .notDetermined: // The user hasn’t chosen an authorization status
    }
}
```

### Location Services: Determining Device Support — [7:02]

```swift
if CLLocationManager.isMonitoringAvailable(for: CLBeaconRegion.self) {
    // Supports region monitoring to detect beacon regions
}

if CLLocationManager.isRangingAvailable() {
    // Supports obtaining the relative distance to a nearby iBeacon device
}
```

### Stage 1: Region Monitoring — [8:54]

```swift
// Stage 1: Region Monitoring

func monitorBeacons() {
    if CLLocationManager.isMonitoringAvailable(for: CLBeaconRegion.self) {

        let constraint = CLBeaconIdentityConstraint(uuid: proximityUUID)

        let beaconRegion = CLBeaconRegion(
            beaconIdentityConstraint: constraint,
            identifier: beaconID
        )

        self.locationManager.startMonitoring(for: beaconRegion)
    }
}
```

### Stage 2: Beacon Ranging — [9:30]

```swift
// Stage 2: Beacon Ranging

func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
    guard let region = region as? CLBeaconRegion,
        CLLocationManager.isRangingAvailable()
        else { return }

    let constraint = CLBeaconIdentityConstraint(uuid: region.uuid)
    manager.startRangingBeacons(satisfying: constraint)
    beaconsToRange.append(region)
}

func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {

}
```

### Stage 2: Beacon Ranging — [10:09]

```swift
// Stage 2: Beacon Ranging

func locationManager(
    _ manager: CLLocationManager,
    didRangeBeacons beacons: [CLBeacon],
    in region: CLBeaconRegion) {

    guard let nearestBeacon = beacons.first else { return }
    let major = CLBeaconMajorValue(truncating: nearestBeacon.major)
    let minor = CLBeaconMinorValue(truncating: nearestBeacon.major)

    switch nearestBeacon.proximity {
    case .near, .immediate:
        displayInformation(for: major, and: minor)

    default:
        handleUnknownOrFarBeacon(for: major, and: minor)
    }
}
```

### Formatting Dates — [11:32]

```swift
// Formatting Dates
let dateFormatter = DateFormatter()
dateFormatter.dateStyle = .medium
dateFormatter.timeStyle = .short
dateFormatter.string(from: Date())
// "Jun 25, 2020 at 9:41 AM"
```

### Configuring the Format of Currency — [12:41]

```swift
// Configuring the Format of Currency
let formatter = NumberFormatter()
formatter.currencyCode = "CAD"
formatter.numberStyle = .currency
formatter.string(from: amount)
// "CA$1.00"
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10140/5/C86424DC-C2CF-464A-BDCE-35C9B4476E4B/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10140) — developer.apple.com. Indexed for agent consumption._
