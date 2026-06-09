---
id: "wwdc2022-10135"
event: "wwdc2022"
year: 2022
title: "Get timely alerts from Bluetooth devices on watchOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10135"
topics: ["Health & Fitness", "System Services"]
platforms: ["iOS", "iPadOS", "watchOS"]
hasTranscript: true
---

# Get timely alerts from Bluetooth devices on watchOS

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10135](https://developer.apple.com/videos/play/wwdc2022/10135)

Find out how Bluetooth devices can send timely and relevant alerts to Apple Watch. We'll show you how to take advantage of periodic data in complications, explore background peripheral discovery, and help you learn how to use characteristic monitoring in watchOS. We'll also share best practices and design guidance for creating a great Bluetooth accessory.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,886 words)

## Documentation & Resources

- [Accessory Design Guidelines](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/accessories/Accessory-Design-Guidelines.pdf
- [Core Bluetooth](https://developer.apple.com/documentation/CoreBluetooth) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreBluetooth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreBluetooth.json

## Code Snippets

### Listen for alerts — [3:41]

```swift
func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
    peripheral.setNotifyValue(true, for: characteristic)
}

func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error: Error?) {
    if let newData = characteristic.value {
        // Post a local notification.
    }
}
```

### Discover peripherals — [9:15]

```swift
func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
    central.scanForPeripherals(withServices: [myCustomUUID])
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10135/4/B6405ED7-98EE-473C-8174-144D5E72CA02/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10135/4/B6405ED7-98EE-473C-8174-144D5E72CA02/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10135) — developer.apple.com. Indexed for agent consumption._