---
id: "wwdc2021-10158"
event: "wwdc2021"
year: 2021
title: "Explore low-latency video encoding with VideoToolbox"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10158"
topics: ["Photos & Camera", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore low-latency video encoding with VideoToolbox

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10158](https://developer.apple.com/videos/play/wwdc2021/10158)

Supporting low latency encoders has become an important aspect of video application development process. Discover how VideoToolbox supports low-delay H.264 hardware encoding to minimize end-to-end latency and achieve new levels of performance for optimal real-time communication and high-quality video playback.

**Keywords:** `acceleration`, `avfoundation`, `coremedia`, `hardware`, `performance`, `video`, `videotoolbox`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,559 words)

## Documentation & Resources

- [Video Toolbox](https://developer.apple.com/documentation/VideoToolbox) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VideoToolbox
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VideoToolbox.json

## Code Snippets

### VTCompressionSession creation — [5:03]

```objectivec
CFMutableDictionaryRef encoderSpecification =
            CFDictionaryCreateMutable(kCFAllocatorDefault, 0, NULL, NULL);

CFDictionarySetValue(encoderSpecification,
                     kVTVideoEncoderSpecification_EnableLowLatencyRateControl,
                     kCFBooleanTrue)

VTCompressionSessionRef compressionSession;

OSStatus err = VTCompressionSessionCreate(kCFAllocatorDefault, 
                                          width, 
                                          height,
                                          kCMVideoCodecType_H264, 
                                          encoderSpecification,
                                          NULL, 
                                          NULL, 
                                          outputHandler, 
                                          NULL,
                                          &compressionSession);
```

### New profiles — [7:35]

```objectivec
// Request CBP

VTSessionSetProperty(compressionSession, 
                     kVTCompressionPropertyKey_ProfileLevel, 
                     kVTProfileLevel_H264_ConstrainedBaseline_AutoLevel);

// Request CHP

VTSessionSetProperty(compressionSession, 
                     kVTCompressionPropertyKey_ProfileLevel, 
                     kVTProfileLevel_H264_ConstrainedHigh_AutoLevel);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10158/4/1A6010D5-5911-425C-96D0-DAA26DBE60C0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10158/4/1A6010D5-5911-425C-96D0-DAA26DBE60C0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10158) — developer.apple.com. Indexed for agent consumption._
