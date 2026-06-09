---
id: "wwdc2026-224"
event: "wwdc2026"
year: 2026
title: "Expand the capabilities of your Virtualization app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/224"
topics: ["System Services"]
platforms: ["macOS"]
hasTranscript: true
---

# Expand the capabilities of your Virtualization app

**Event:** WWDC26 · **Topic:** System Services · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-224](https://developer.apple.com/videos/play/wwdc2026/224)

Bring powerful new capabilities in macOS 27 to your Virtualization app. Discover how to automate the setup of macOS guests through user account setup on first boot. We’ll explore advanced workflows that involve passthrough of USB accessories to virtual machines, as well as custom network topologies and port forwarding. You’ll also learn about recent improvements that can enrich the experience of running your app’s virtual machines.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,051 words)

## Documentation & Resources

- [DiskImageKit](https://developer.apple.com/documentation/DiskImageKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DiskImageKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DiskImageKit.json
- [Accessory Access](https://developer.apple.com/documentation/AccessoryAccess) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AccessoryAccess
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AccessoryAccess.json
- [vmnet](https://developer.apple.com/documentation/vmnet) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/vmnet
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/vmnet.json
- [Virtual I/O Device (VIRTIO) Version 1.4](https://docs.oasis-open.org/virtio/virtio/v1.4/virtio-v1.4.html) _documentation_
- [Virtualization](https://developer.apple.com/documentation/Virtualization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Virtualization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Virtualization.json

## Code Snippets

### Provision a macOS guest — [1:57]

```swift
import Virtualization

let provisioningOptions = VZMacGuestProvisioningOptions()
provisioningOptions.fullName = fullName
provisioningOptions.username = username
provisioningOptions.password = password
provisioningOptions.logsInAutomatically = true
provisioningOptions.enablesRemoteLogin = true

let startOptions = VZMacOSVirtualMachineStartOptions()
try startOptions.setGuestProvisioning(provisioningOptions)

try await virtualMachine.start(options: startOptions)
```

### Register an Accessory Access listener — [7:12]

```swift
import AccessoryAccess

let criteria: [AAUSBAccessoryMatchingCriteria] = []
let accessories = try await AAUSBAccessoryManager.shared.registerListener(self, matchingCriteria: criteria)

for accessory in accessories {
    // Handle previously attached accessories.
}
```

### Respond to USB accessory connection — [7:39]

```swift
import AccessoryAccess
import Virtualization

class AccessoryListener: NSObject, AAUSBAccessoryListener {
    func usbAccessoryDidConnect(_ usbAccessory: AAUSBAccessory) {
        virtualMachine.queue.async {
            do {
                let configuration = VZUSBPassthroughDeviceConfiguration(device: usbAccessory)
                let device = try VZUSBPassthroughDevice(configuration: configuration)
                self.virtualMachine.usbControllers.first?.attach(device: device) { error in
                    // Handle error if necessary...
                }
            } catch {
                // Handle error...
            }
        }
    }
}
```

### Create a custom vmnet network — [10:04]

```swift
import Virtualization
import vmnet

var status: vmnet_return_t = .VMNET_FAILURE
guard let networkConfiguration =
    vmnet_network_configuration_create(.VMNET_SHARED_MODE, &status) else { ... }

guard let network =
    vmnet_network_create(networkConfiguration, &status) else { ... }

let attachment = VZVmnetNetworkDeviceAttachment(network: network)

let networkDeviceConfiguration = VZVirtioNetworkDeviceConfiguration()
networkDeviceConfiguration.attachment = attachment

virtualMachineConfiguration.networkDevices = [networkDeviceConfiguration]

let virtualMachine = VZVirtualMachine(configuration: virtualMachineConfiguration)
```

### Use DiskImageKit with Virtualization — [14:54]

```swift
import DiskImageKit
import Virtualization

let baseImage = try DiskImage(opening: .open(url: baseLayerURL, mode: .readOnly))
let cacheImage = try baseImage.appending(.asifLayer(url: cacheLayerURL, type: .cache))
let overlayImage = try DiskImage(opening: .open(url: overlayLayerURL))
let stackedImage = try cacheImage.appending(overlayImage)

let storageDeviceAttachment = try VZDiskImageStorageDeviceAttachment(diskImage: stackedImage)

let storageDeviceConfiguration =
    VZVirtioBlockDeviceConfiguration(attachment: storageDeviceAttachment)

virtualMachineConfiguration.storageDevices = [storageDeviceConfiguration]

let virtualMachine = VZVirtualMachine(configuration: virtualMachineConfiguration)
```

### Configure a custom Virtio device — [17:41]

```swift
import Virtualization

let deviceConfiguration = VZCustomVirtioDeviceConfiguration()

// Virtio entropy device.
deviceConfiguration.deviceID = 4
// PCI class for crypto devices.
deviceConfiguration.pciClassID = 0x10
// PCI subclass for network and computing encryption controllers.
deviceConfiguration.pciSubclassID = 0x00
// An entropy device uses a single Virtio queue.
deviceConfiguration.virtioQueueCount = 1

deviceConfiguration.provider =
    VZCustomVirtioDeviceDelegateProvider(deviceQueue: deviceQueue, delegate: provider)

virtualMachineConfiguration.customVirtioDevices = [deviceConfiguration]

let virtualMachine = VZVirtualMachine(configuration: virtualMachineConfiguration)
```

### Attach a delegate to a VZCustomVirtioDevice — [18:20]

```swift
import Virtualization

class DeviceConfigurationDelegate: NSObject, VZCustomVirtioDeviceConfigurationDelegate {
    func customVirtioConfiguration(_ deviceConfiguration: VZCustomVirtioDeviceConfiguration,
                                   didCreateDevice device: VZCustomVirtioDevice) {
        device.delegate = deviceDelegate
        self.device = device
    }
}
```

### Process Virtio queue elements — [18:42]

```swift
import Virtualization

class DeviceDelegate: NSObject, VZCustomVirtioDeviceDelegate {
    func customVirtioDevice(_ device: VZCustomVirtioDevice,
                            didReceiveNotificationFor queue: VZVirtioQueue) {
        while let element = queue.nextElement() {
            // Process element...
            element.returnToQueue()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/224/5/33a91529-8caf-409e-9c54-1b8952744651/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/224/5/33a91529-8caf-409e-9c54-1b8952744651/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/224) — developer.apple.com. Indexed for agent consumption._
