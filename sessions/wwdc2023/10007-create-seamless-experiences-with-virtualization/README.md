---
id: "wwdc2023-10007"
event: "wwdc2023"
year: 2023
title: "Create seamless experiences with Virtualization"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10007"
topics: ["System Services"]
platforms: ["macOS"]
hasTranscript: true
---

# Create seamless experiences with Virtualization

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** macOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10007](https://developer.apple.com/videos/play/wwdc2023/10007)

Discover the latest updates to the Virtualization framework. We’ll show you how to configure a virtual machine (VM) to automatically resize its display, take you through saving and restoring a running VM, and explore storage and performance options for Virtualization apps running on the desktop or in the data center. To learn more about the Virtualization framework, check out “Create macOS or Linux virtual machines” from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,977 words)

## Documentation & Resources

- [Running macOS in a virtual machine on Apple silicon](https://developer.apple.com/documentation/Virtualization/running-macos-in-a-virtual-machine-on-apple-silicon) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Virtualization/running-macos-in-a-virtual-machine-on-apple-silicon
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Virtualization/running-macos-in-a-virtual-machine-on-apple-silicon.json
- [Virtualization](https://developer.apple.com/documentation/Virtualization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Virtualization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Virtualization.json

## Code Snippets

### Set display as resizable — [1:58]

```swift
// virtualMachine is a VZVirtualMachine.
let virtualMachineView = VZVirtualMachineView()
virtualMachineView.virtualMachine = virtualMachine

virtualMachineView.automaticallyReconfiguresDisplay = true
```

### Save a virtual machine — [4:20]

```swift
// virtualMachine is a running VZVirtualMachine.
try await virtualMachine.pause()

let saveFileURL = URL(filePath: "SaveFile.vzvmsave", directoryHint: .notDirectory)
try await virtualMachine.saveMachineStateTo(url: saveFileURL)
```

### Restore a virtual machine — [4:58]

```swift
let configuration = VZVirtualMachineConfiguration()
// Customize configuration.

let virtualMachine = VZVirtualMachine(configuration: configuration)

let saveFileURL = URL(filePath: "SaveFile.vzvmsave", directoryHint: .notDirectory)
try await virtualMachine.restoreMachineStateFrom(url: saveFileURL)

try await virtualMachine.resume()
```

### Configure a Virtio block device with the NBD attachment — [9:28]

```swift
let url = URL(string: "nbd://localhost:10809/myDisk")!
let attachment = try VZNetworkBlockDeviceStorageDeviceAttachment(url: url)

let blockDevice = VZVirtioBlockDeviceConfiguration(attachment: attachment)
```

### Respond to events with a delegate with the NBD attachment — [10:02]

```swift
let url = URL(string: "nbd://localhost:10809/myDisk")!
let attachment = try VZNetworkBlockDeviceStorageDeviceAttachment(url: url)

// NetworkBlockDeviceAttachmentDelegate implements the delegate protocol.
let delegate = NetworkBlockDeviceAttachmentDelegate()
attachment.delegate = delegate

let blockDevice = VZVirtioBlockDeviceConfiguration(attachment: attachment)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10007/4/ADC7900A-352D-4B06-8285-22AFB8A66356/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10007/4/ADC7900A-352D-4B06-8285-22AFB8A66356/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10007) — developer.apple.com. Indexed for agent consumption._
