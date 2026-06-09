---
id: "wwdc2022-10002"
event: "wwdc2022"
year: 2022
title: "Create macOS or Linux virtual machines"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10002"
topics: ["Business & Education", "System Services"]
platforms: ["macOS"]
hasTranscript: true
---

# Create macOS or Linux virtual machines

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10002](https://developer.apple.com/videos/play/wwdc2022/10002)

Learn how you can use the Virtualization framework to quickly create virtual machines on your Mac. We'll show you how to create a virtual Mac and quickly test changes to your app in an isolated environment. We'll also explore how you can install and run full Linux distributions on Apple silicon, and share how you can take advantage of Rosetta 2 to run x86-64 Linux binaries.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,599 words)

## Documentation & Resources

- [Hypervisor](https://developer.apple.com/documentation/Hypervisor) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Hypervisor
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Hypervisor.json
- [Running GUI Linux in a virtual machine on a Mac](https://developer.apple.com/documentation/Virtualization/running-gui-linux-in-a-virtual-machine-on-a-mac) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Virtualization/running-gui-linux-in-a-virtual-machine-on-a-mac
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Virtualization/running-gui-linux-in-a-virtual-machine-on-a-mac.json
- [Virtualization](https://developer.apple.com/documentation/Virtualization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Virtualization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Virtualization.json

## Code Snippets

### Running the virtual machine — [4:11]

```swift
let virtualMachine = VZVirtualMachine(configuration: configuration)
try await virtualMachine.start()
```

### Showing the virtual machine’s display — [4:33]

```swift
let virtualMachineView = VZVirtualMachineView()
virtualMachineView.virtualMachine = virtualMachine
```

### Start from the base — [7:43]

```swift
var configuration = VZVirtualMachineConfiguration()
configuration.cpuCount = 4
configuration.memorySize = (4 * 1024 * 1024 * 1024) as UInt64
configuration.storageDevices = [newBlockDevice()]
configuration.pointingDevices = [newPointingDevice()]
```

### Set up the platform — [7:47]

```swift
let platform = VZMacPlatformConfiguration()

let hardwareModel = VZMacHardwareModel(dataRepresentation: savedHardwareModel)
platform.hardwareModel = hardwareModel!

let auxiliaryStorage = VZMacAuxiliaryStorage(contentsOf: auxiliaryStorageURL)
platform.auxiliaryStorage = auxiliaryStorage

let machineIdentifier = VZMacMachineIdentifier(dataRepresentation: savedIdentifier)
platform.machineIdentifier = machineIdentifier!

configuration.platform = platform
```

### Boot loader — [8:31]

```swift
configuration.bootLoader = VZMacOSBootLoader()
```

### 1. Getting an image — [9:16]

```swift
let restoreImage = try await VZMacOSRestoreImage.latestSupported

try await download(restoreImage.url)
```

### 2. Create a compatible configuration — [9:29]

```swift
let requirements = restoreImage.mostFeaturefulSupportedConfiguration

guard let requirements = requirements else {
    // No compatible configuration.
    return
}

platform.hardwareModel = requirements.hardwareModel

configuration.cpuCount = requirements.minimumSupportedCPUCount
configuration.memorySize = requirements.minimumSupportedMemorySize
```

### 3. Install macOS — [10:10]

```swift
let virtualMachine = VZVirtualMachine(configuration: configuration)

let installer = VZMacOSInstaller(virtualMachine: virtualMachine,
                                 restoringFromImageAt: imageURL)
try await installer.install()
```

### Setting up GPU acceleration — [10:58]

```swift
let graphicsConfiguration = VZMacGraphicsDeviceConfiguration()
graphicsConfiguration.displays = [
    VZMacGraphicsDisplayConfiguration(widthInPixels: 1920,
                                      heightInPixels: 1200,
                                      pixelsPerInch: 80)
]

configuration.graphicsDevices = [graphicsConfiguration]
```

### Setting up the Mac trackpad — [11:48]

```swift
let trackpad = VZMacTrackpadConfiguration()
configuration.pointingDevices = [trackpad]
```

### Share a folder — [12:33]

```swift
let sharedDirectory = VZSharedDirectory(url: directoryURL, readOnly: false)
let share = VZSingleDirectoryShare(directory: sharedDirectory)

let tag = VZVirtioFileSystemDeviceConfiguration.macOSGuestAutomountTag
let sharingDevice = VZVirtioFileSystemDeviceConfiguration(tag: tag)
sharingDevice.share = share

configuration.directorySharingDevices = [sharingDevice]
```

### Setting up USB Mass Storage device configuration — [16:10]

```swift
let diskImageURL = URL(fileURLWithPath: "linux.iso")
let attachment = try! VZDiskImageStorageDeviceAttachment(url: diskImageURL, readOnly: true)
let usbDeviceConfiguration = VZUSBMassStorageDeviceConfiguration(attachment: attachment)

configuration.storageDevices = [usbDeviceConfiguration, createBlockDevice()]
```

### Booting Linux — [17:27]

```swift
let efi = VZEFIBootLoader()
efi.variableStore = VZEFIVariableStore(creatingVariableStoreAt: storeURL,
                                       options: [])
configuration.bootLoader = efi
```

### Setting up Virtio graphics — [18:24]

```swift
let virtioGPU = VZVirtioGraphicsDeviceConfiguration()
virtioGPU.scanouts = [
    VZVirtioGraphicsScanoutConfiguration(widthInPixels: 1280, heightInPixels: 720)
]

configuration.graphicsDevices = [virtioGPU]
```

### Setting up Rosetta — [21:02]

```swift
let rosettaDirectoryShare = try! VZLinuxRosettaDirectoryShare()
let directorySharingDevice = VZVirtioFileSystemDeviceConfiguration(tag: "RosettaShare")
directorySharingDevice.share = rosettaDirectoryShare

configuration.directorySharingDevices = [directorySharingDevice]
```

### Setting up Linux — [21:37]

```bash
mount -t virtiofs RosettaShare /mnt/Rosetta

sudo /usr/sbin/update-binfmts --install rosetta /mnt/Rosetta/rosetta \
  --magic "\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3e\x00" \
  --mask "\xff\xff\xff\xff\xff\xfe\xfe\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff" \
  --credentials yes --preserve no --fix-binary yes
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10002/5/F229C2EC-A6BC-4671-91A0-65FBC9D71DDF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10002/5/F229C2EC-A6BC-4671-91A0-65FBC9D71DDF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10002) — developer.apple.com. Indexed for agent consumption._
