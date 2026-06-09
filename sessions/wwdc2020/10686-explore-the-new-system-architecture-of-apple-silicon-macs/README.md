---
id: "wwdc2020-10686"
event: "wwdc2020"
year: 2020
title: "Explore the new system architecture of Apple silicon Macs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10686"
topics: ["Developer Tools", "System Services"]
platforms: ["macOS"]
hasTranscript: true
---

# Explore the new system architecture of Apple silicon Macs

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10686](https://developer.apple.com/videos/play/wwdc2020/10686)

Discover how Macs with Apple silicon will deliver modern advantages using Apple's System-on-Chip (SoC) architecture. Leveraging a unified memory architecture for CPU and GPU tasks, Mac apps will see amazing performance benefits from Apple silicon tuned frameworks such as Metal and Accelerate. Learn about new features and changes coming to boot and security, and how these may affect your applications.

**Keywords:** `amp`, `apple silicon`, `apple silicon mac`, `asymmetric multiprocessing`, `driverkit`, `macos recovery`, `mac sharing mode`, `reduced security`, `rosetta`, `secure boot`, `soc`, `system recovery`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,103 words)

## Code Snippets

### Set up DMA transfer in a PCIe driver — [9:42]

```swift
// Get the IOMapper for the device
IOMapper *mapper = IOMapper::copyMapperForDevice(device);

// Use an IODMACommand; pass the mapper when initializing
IODMACommand *dmaCommand = IODMACommand::withSpecification(
   outSegFunc, numAddressBits, maxSegmentSize, mappingOptions,
   maxTransferSize, alignment, mapper, refCon);

// Keep the IODMACommand prepared for the duration of the i/o
```

### Check if running in Rosetta — [14:31]

```objectivec
// Use "sysctl.proc_translated" to check if running in Rosetta

// Returns 1 if running in Rosetta
int processIsTranslated() {
   int ret = 0;
   size_t size = sizeof(ret);

   // Call the sysctl and if successful return the result
   if (sysctlbyname("sysctl.proc_translated", &ret, &size, NULL, 0) != -1) 
      return ret;

   // If "sysctl.proc_translated" is not present then must be native
   if (errno == ENOENT)
      return 0;

   return -1;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10686/4/63FE46AD-053B-4294-B04F-A4BE576BD265/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10686) — developer.apple.com. Indexed for agent consumption._
