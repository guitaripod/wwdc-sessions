---
id: "wwdc2025-228"
event: "wwdc2025"
year: 2025
title: "Supercharge device connectivity with Wi-Fi Aware"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/228"
topics: ["Privacy & Security", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Supercharge device connectivity with Wi-Fi Aware

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-228](https://developer.apple.com/videos/play/wwdc2025/228)

Learn how to create peer-to-peer network connections with Wi-Fi Aware. We’ll also cover how to share videos in real time, transfer large files, and control accessories with improved bandwidth and lower latency. And you’ll learn how to use DeviceDiscoveryUI, AccessorySetupKit, and the Network framework to use Wi-Fi Aware in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,838 words)

## Documentation & Resources

- [Wi-Fi Aware](https://developer.apple.com/documentation/WiFiAware) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WiFiAware
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WiFiAware.json
- [Accessory Design Guidelines](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/accessories/Accessory-Design-Guidelines.pdf

## Code Snippets

### Access capabilities and services — [6:57]

```swift
import WiFiAware

// Check if Wi-Fi Aware is supported on your device
guard WACapabilities.supportedFeatures.contains(.wifiAware) else { return }

// Publishable service declared in Info.plist
extension WAPublishableService {
    public static var fileService: WAPublishableService {
        allServices["_file-service._tcp"]!
    }
}

// Subscribable services declared in Info.plist
extension WASubscribableService {
    public static var fileService: WASubscribableService {
        allServices["_file-service._tcp"]!
    }
    public static var droneService: WASubscribableService {
        allServices["_drone-service._udp"]!
    }
}
```

### Pair with DeviceDiscoveryUI — [10:33]

```swift
import DeviceDiscoveryUI
import WiFiAware
import SwiftUI

// Listener (Publisher) Device
// Invoke Listener UI
DevicePairingView(.wifiAware(.connecting(to: .fileService, from: .selected([])))) {
    // Provide a view to display to user before launching System UI
} fallback: {
    // Provide a view in case of error
}

// Browser (Subscriber) Device
// Invoke Browser UI
DevicePicker(.wifiAware(.connecting(to: .selected([]), from: .fileService))) { endpoint in
    // Process the paired network endpoint
} label: {
    // Provide a view to display to user before launching System UI
} fallback: {
    // Provide a view in case of error
}
```

### Pair with AccessorySetupKit — [12:29]

```swift
import AccessorySetupKit

// Configure ASDiscoveryDescriptor (Subscriber)
let descriptor = ASDiscoveryDescriptor()
descriptor.wifiAwareServiceName = "_drone-service._udp"
descriptor.wifiAwareModelNameMatch = .init(string: "Example Model")
descriptor.wifiAwareVendorNameMatch = .init(string: "Example Inc", compareOptions: .literal)
let item = ASPickerDisplayItem(name: "My Drone",
                               productImage: UIImage(named: "DroneProductImage")!,
                               descriptor: descriptor)

// Create and activate session
let session = ASAccessorySession()
session.activate(on: sessionQueue) { event in
    // Closure will execute when device is added with event: .accessoryAdded
    // ASAccessoryWiFiAwarePairedDeviceID can be used to lookup a WAPairedDevice
}
// Present Picker UI
session.showPicker(for: [item]) { error in
    // Handle error
}
```

### Access paired devices — [13:51]

```swift
import Foundation
import WiFiAware

// WAPairedDevice
var device: WAPairedDevice // Get using WAPairedDevice.allDevices

// Access WAPairedDevice properties
let pairingName = device.pairingInfo?.pairingName
let vendorName = device.pairingInfo?.vendorName
let modelName = device.pairingInfo?.modelName

// Create a filter to select devices of interest
let filter = #Predicate<WAPairedDevice> {
    $0.pairingInfo?.vendorName.starts(with: "Example Inc") ?? false
}

// Get all paired devices, matching the filter, at the current moment
// A new snapshot of all paired devices each time a device is added, changed, or removed
for try await devices in WAPairedDevice.allDevices(matching: filter) {
    // Process new snapshot of all paired devices
}
```

### Filter paired devices — [16:23]

```swift
import Foundation
import WiFiAware

// Listener (Publisher) Device
// Specify the paired devices of interest for the use case
let deviceFilter = #Predicate<WAPairedDevice> {
    $0.name?.starts(with: "My Device") ?? false
}

// Browser (Subscriber) Device
// Specify the paired devices of interest for the use case
let deviceFilter = #Predicate<WAPairedDevice> {
    $0.pairingInfo?.vendorName.starts(with: "Example Inc") ?? false
}
```

### Create listener and browser — [16:54]

```swift
import WiFiAware
import Network

// Listener (Publisher) Device: Construct a NetworkListener
let listener = try NetworkListener(for:
        .wifiAware(.connecting(to: .fileService, from: .matching(deviceFilter))),
    using: .parameters {
        TLS()
    })
    .onStateUpdate { listener, state in
        // Process state update
    }

// Browser (Subscriber) Device: Construct a NetworkBrowser
let browser = NetworkBrowser(for:
        .wifiAware(.connecting(to: .matching(deviceFilter), from: .fileService))
    )
    .onStateUpdate { browser, state in
        // Process state update
    }
```

### Establish a connection — [17:44]

```swift
// Listener (Publisher) Device: Start NetworkListener
try await listener.run { connection in  // Radio resources in use
    // Closure executes for each incoming connection
    connection.onStateUpdate { connection, state in
        // Process state update
    }
}

// Browser (Subscriber) Device: Start NetworkBrowser
let endpoint = try await browser.run { waEndpoints in // Radio resources in use
        // Review endpoints, decide whether to return or skip
        if let endpoint = self.endpoint(in: waEndpoints) { return .finish(endpoint) }
        else { return .continue }
    }
// Create the connection
let connection = NetworkConnection(to: endpoint, using: .parameters {
        TLS()
    })
    .onStateUpdate { connection, state in
        // Process state update
    }
```

### Tune performance — [21:11]

```swift
// Listener (Publisher) Device
// Configure .realtime + .interactiveVideo on NetworkListener
let listener = try NetworkListener(for:
        .wifiAware(.connecting(to: .fileService, from: .matching(deviceFilter))),
    using: .parameters {
        TLS()
    }
    .wifiAware { $0.performanceMode = .realtime }
    .serviceClass(.interactiveVideo))

// Browser (Subscriber) Device
// Configure .realtime + .interactiveVideo on NetworkConnection
let connection = NetworkConnection(to: endpoint, using: .parameters {
        TLS()
    }
    .wifiAware { $0.performanceMode = .realtime }
    .serviceClass(.interactiveVideo))

// Listener (Publisher) Device & Browser (Subscriber) Device
// Read performance report
let performanceReport = try await connection.currentPath?.wifiAware?.performance
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/228/4/b7b10ed3-bcfe-4935-919a-1b7faef02d2b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/228/4/b7b10ed3-bcfe-4935-919a-1b7faef02d2b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/228) — developer.apple.com. Indexed for agent consumption._
