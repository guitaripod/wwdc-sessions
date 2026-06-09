---
id: "wwdc2026-369"
event: "wwdc2026"
year: 2026
title: "Find your accessory with Bluetooth Channel Sounding"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/369"
topics: ["System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Find your accessory with Bluetooth Channel Sounding

**Event:** WWDC26 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-369](https://developer.apple.com/videos/play/wwdc2026/369)

Get started with Channel Sounding to bring distance and direction awareness to your Bluetooth accessories. Dive into the new Nearby Interaction and Core Bluetooth APIs, and walk through the accessory-side changes you’ll need. Optimize power consumption while ensuring a smooth, responsive experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(947 words)

## Documentation & Resources

- [AccessorySetupKit](https://developer.apple.com/documentation/AccessorySetupKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AccessorySetupKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AccessorySetupKit.json
- [Nearby Interaction](https://developer.apple.com/documentation/NearbyInteraction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NearbyInteraction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NearbyInteraction.json
- [Core Bluetooth](https://developer.apple.com/documentation/CoreBluetooth) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreBluetooth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreBluetooth.json

## Code Snippets

### Start a Core Bluetooth Channel Sounding session — [3:43]

```swift
import CoreBluetooth

func isChannelSoundingSupported() -> BOOL {
    guard centralManager.state == .poweredOn else { return }
    if #available(iOS 27.0, *) {
        // Check current device supports Bluetooth Channel Sounding
        return CBCentralManager.supportsFeatures(.channelSounding)
    }
}

func startChannelSounding(_ peripheral: CBPeripheral) {
    guard peripheral.isConnected else { return }
    if #available(iOS 27.0, *) {  
        // Step 1: Create a CBChannelSoundingSessionConfiguration
        let config = CBChannelSoundingSessionConfiguration(role: .initiator)

        // Step 2: Start the channel sounding session
        peripheral.startChannelSoundingSession(config)
    }
}
```

### Receive distance results and cancel a session — [4:09]

```swift
import CoreBluetooth

// Receive distance results
func peripheral(_ peripheral: CBPeripheral,
                didReceive results: CBChannelSoundingProcedureResults?,
                error: Error?) {
    guard let results = results else { return }

    let distance = results.distance

    // Do something with distance
}

// Cancel a Channel Sounding session
func cancelChannelSounding(_ peripheral: CBPeripheral) {
    guard peripheral.isConnected else { return }
    if #available(iOS 27.0, *) {
        // Cancel the channel sounding session
        peripheral.cancelChannelSoundingSession(config)
    }
}

func peripheral(_ peripheral: CBPeripheral,
                didCompleteChannelSoundingSession error: Error?) {   
    // Session is complete
}
```

### Start a Nearby Interaction Channel Sounding session — [4:41]

```swift
import CoreBluetooth
import NearbyInteraction

// Configure a Nearby Interaction Channel Sounding session
func startChannelSoundingThroughNearbyInteraction(_ peripheral: CBPeripheral) {
    if #available(iOS 27.0, *) {        
        // Step 1: Check current device supports Bluetooth Channel Sounding
        guard NISession.deviceCapabilities.supportsBluetoothChannelSounding else { return }

        // Step 2: Create an NINearbyAccessoryConfiguration
        let config = NINearbyAccessoryConfiguration(
            bluetoothChannelSoundingIdentifier: peripheral.identifier, 
            previousChannelSoundingIdentifier: nil)

        // Step 3: Enable camera assistance for direction support
        if NISession.deviceCapabilities.supportsCameraAssistance { 
            config.isCameraAssistanceEnabled = true
        }
    }
}
```

### Run a Nearby Interaction Channel Sounding session — [5:19]

```swift
import CoreBluetooth
import NearbyInteraction

// Run a Nearby Interaction Channel Sounding session
func runChannelSoundingThroughNearbyInteraction(_ config: NINearbyAccessoryConfiguration) {
    // Create an NISession
    let session = NISession()
    session.delegate = self
    // Run the NISession with the accessory configuration
    session.run(config)
}

// Improve Nearby Interaction direction outputs
func updateAccessoryMotionState(_ isMoving: Bool) {
    NIMotionActivityState motionState = isMoving ? .moving : .stationary

    // Tell NISession about.the accessory's motion state
    session.updateMotionState(motionState, forObjectWithToken: object.discoveryToken)
}

// Receive NISession updates
func session(_ session: NISession, didUpdate nearbyObjects: [NINearbyObjects]) {   
    guard let object = nearbyObjects.first else { return }

    if let distance = object.distance {
        // Do something with distance
    }

    if let direction = object.horizontalAngle {
        // Do something with horizontal angle
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/369/4/fea90204-fd38-4da4-b9e7-5dce37bc87d8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/369/4/fea90204-fd38-4da4-b9e7-5dce37bc87d8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/369) — developer.apple.com. Indexed for agent consumption._