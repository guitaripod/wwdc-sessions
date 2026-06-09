---
id: "wwdc2021-10298"
event: "wwdc2021"
year: 2021
title: "Add support for Matter in your smart home app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10298"
topics: ["System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Add support for Matter in your smart home app

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10298](https://developer.apple.com/videos/play/wwdc2021/10298)

The enhanced and new APIs in HomeKit enable smart home developers to integrate with the new Matter protocol in the most convenient way. Tour the Matter protocol, and discover how to set up and manage Matter accessories on our platforms and within your smart home apps.

**Keywords:** `chip`, `home automation`, `homekit`, `matter`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,628 words)

## Code Snippets

### Add a Matter accessory to your HomeKit app — [4:58]

```swift
home.addAndSetupAccessories() { error in
    if let error = error {
         print("Error occurred in accessory setup \(error)”)
    } else {
         print("Successfully added accessory to HomeKit")
    }
}
```

### Invocation example — [9:12]

```swift
let homes = proprietaryHomeStorage.homes.map { home in
    HMCHIPServiceHome(uuid: home.uuid, name: home.name)
}

let topology = HMCHIPServiceTopology(homes: homes)
let setupManager = HMAccessorySetupManager()

do {
    try await setupManager.addAndSetUpAccessories(for: topology)
    print("Successfully added accessory to my app”)
} catch {
    print("Error occurred in accessory setup \(error)")
}
```

### Extension communication — [10:15]

```swift
class RequestHandler: HMCHIPServiceRequestHandler, CHIPDevicePairingDelegate {

   // . . .

   override func pairAccessory(in: HMCHIPServiceHome, onboardingPayload: String) async throws -> Void {
        // iOS is instructing the extension to pair the accessory via CHIP.framework
  }     // . . .
}
```

### Extension communication — [10:39]

```swift
class RequestHandler: HMCHIPServiceRequestHandler, CHIPDevicePairingDelegate {

   // . . .

   override func rooms(in: HMCHIPServiceHome) async throws -> [HMCHIPServiceRoom] {
        // iOS is querying for a room list that corresponds to the given home
    }     // . . .
}
```

### Extension communication — [11:03]

```swift
class RequestHandler: HMCHIPServiceRequestHandler, CHIPDevicePairingDelegate {

   // . . .

   override func configureAccessory(named accessoryName: String, room accessoryRoom: HMCHIPServiceRoom) async throws -> Void {
        // iOS is instructing the extension to apply configuration via CHIP.framework.
    }     // . . .
}
```

### Extension communication — [11:27]

```swift
class RequestHandler: HMCHIPServiceRequestHandler, CHIPDevicePairingDelegate {

    override func rooms(in: HMCHIPServiceHome) async throws -> [HMCHIPServiceRoom] {
        // iOS is querying for rooms that match the given home.  These rooms will be shown in system UI and the selection will be vended back to your extension's `configureAccessory` function
   }

    override func pairAccessory(in: HMCHIPServiceHome, onboardingPayload: String) async throws -> Void {
        // iOS is instructing the extension to pair the accessory via CHIP.framework
   }

    override func configureAccessory(named accessoryName: String, room accessoryRoom: HMCHIPServiceRoom) async throws -> Void {
       // iOS is instructing the extension to apply configuration via CHIP.framework.
    }
}
```

### Status and Control — [14:27]

```swift
let controller = CHIPDeviceController.shared()
do {
    let device = try controller.getPairedDevice(accessoryDeviceID)
    let onOffCluster = CHIPOnOff(device: device,
                               endpoint: lightEndpoint,
                                  queue: DispatchQueue.main)
    onOffCluster?.toggle({ (error, values) in
        // Error handling code here
    })
    onOffCluster?.readAttributeOnOff(responseHandler: { error, response in
        if let state = response?[VALUE_KEY] as? NSInteger {
           updateLightState(state: state)
        }
    })
} catch {
    print("Error occurred in accessory control \(error)")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10298/8/B4998783-FC66-455C-9469-213C69446C72/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10298/8/B4998783-FC66-455C-9469-213C69446C72/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10298) — developer.apple.com. Indexed for agent consumption._
