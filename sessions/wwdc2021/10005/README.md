---
id: "wwdc2021-10005"
event: "wwdc2021"
year: 2021
title: "Connect Bluetooth devices to Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10005"
topics: ["Health & Fitness", "System Services"]
platforms: ["watchOS"]
hasTranscript: true
---

# Connect Bluetooth devices to Apple Watch

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10005](https://developer.apple.com/videos/play/wwdc2021/10005)

Discover how you can integrate data from Bluetooth accessories into Apple Watch apps and complications. Bluetooth devices can provide medical data, sports stats, and more to Apple Watch, and help people get more out of your software in the process. We’ll show you how to connect to these devices during Background App Refresh to display the most up-to-date information in your Apple Watch complications, provide an overview of Core Bluetooth on watchOS, and explore best practices for Bluetooth accessory design.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,451 words)

## Documentation & Resources

- [Background execution](https://developer.apple.com/documentation/WatchKit/background-execution) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WatchKit/background-execution
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WatchKit/background-execution.json
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/WatchKit/interacting-with-bluetooth-peripherals-during-background-app-refresh) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WatchKit/interacting-with-bluetooth-peripherals-during-background-app-refresh
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WatchKit/interacting-with-bluetooth-peripherals-during-background-app-refresh.json
- [Core Bluetooth](https://developer.apple.com/documentation/CoreBluetooth) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreBluetooth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreBluetooth.json

## Code Snippets

### didDiscoverPeripheral — [7:35]

```swift
func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String: Any], rssi RSSI: NSNumber ) {

    // Add to an array of discovered peripherals,
    // then connect to the peripheral.

    central.connect(peripheral, options: nil)

}
```

### handleBackgroundTasks — [7:55]

```swift
func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
    for task in backgroundTasks {
        if let refreshTask = task as? WKApplicationRefreshBackgroundTask {
            // Insert your code to start background work here.
            central.connect(peripheral, options: nil)
            refreshTask.expirationHandler = {
                // Insert your code to cancel existing work here.
                if let peripheral = self.bluetoothReceiver.connectedPeripheral {
                    self.central.cancelPeripheralConnection(peripheral)
                }
                refreshTask.setTaskCompletedWithSnapshot(false)
            }
        }
    }
}
```

### didDisconnectPeripheral — [8:51]

```swift
// If the app gets woken up to handle a background refresh task, this method will be called
// if a peripheral was disconnected when the app had previously transitioned to the
// background.
func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error: Error?) {
    connectedPeripheral = nil
    delegate?.didCompleteDisconnection(from: peripheral)
}
```

### didCompleteDisconnection — [9:08]

```swift
// In your WatchKit Extension delegate:

func didCompleteDisconnection(from peripheral: CBPeripheral) {
    if let refreshTask = currentRefreshTask {
        task.setTaskCompletedWithSnapshot(false)
        currentRefreshTask = nil
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10005/6/F54416C7-9591-4AE8-AE9D-365C4BAC2D7E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10005/6/F54416C7-9591-4AE8-AE9D-365C4BAC2D7E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10005) — developer.apple.com. Indexed for agent consumption._