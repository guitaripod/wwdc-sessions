---
id: "wwdc2022-110373"
event: "wwdc2022"
year: 2022
title: "Bring your driver to iPad with DriverKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110373"
topics: ["Audio & Video", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring your driver to iPad with DriverKit

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110373](https://developer.apple.com/videos/play/wwdc2022/110373)

Discover how you can easily connect Thunderbolt and USB accessories to iPad with DriverKit. We’ll show you how to convert your existing Mac drivers without any code changes, learn how to add real-time audio support with AudioDriverKit, and provide best practices and tips for developing drivers for iPad.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,366 words)

## Documentation & Resources

- [Communicating between a DriverKit extension and a client app](https://developer.apple.com/documentation/DriverKit/communicating-between-a-driverkit-extension-and-a-client-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DriverKit/communicating-between-a-driverkit-extension-and-a-client-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DriverKit/communicating-between-a-driverkit-extension-and-a-client-app.json
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/kernel/implementing_drivers_system_extensions_and_kexts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/kernel/implementing_drivers_system_extensions_and_kexts.json
- [System Extensions and DriverKit](https://developer.apple.com/system-extensions/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/system-extensions/

## Code Snippets

### Register real-time callback in AudioDriverKit — [2:25]

```cpp
// Declare a IOOperationHandler block to set on the IOUserAudioDevice.
// The block will be called from a real time context when a i/o operation
// occurs on the IOUserAudioStream buffers for the device.
io_operation = ^kern_return_t(IOUserAudioObjectID in_device,
                              IOUserAudioIOOperation in_io_operation,
                              uint32_t in_io_buffer_frame_size,
                              uint64_t in_sample_time,
                              uint64_t in_host_time)
{
    // Add custom code to make modifications to the buffers as necessary
    if (in_io_operation == IOUserAudioIOOperationWriteEnd) {
        ...
    } else if (in_io_operation == IOUserAudioIOOperationBeginRead) {
        ...
    }
    return kIOReturnSuccess;
};
this->SetIOOperationHandler(io_operation);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110373/5/9E0B243C-9E0C-4E4E-91FF-AACD903146B2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110373/5/9E0B243C-9E0C-4E4E-91FF-AACD903146B2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110373) — developer.apple.com. Indexed for agent consumption._