---
id: "wwdc2026-338"
event: "wwdc2026"
year: 2026
title: "Build live production tools for Apple Immersive Video"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/338"
topics: ["Spatial Computing", "Audio & Video"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Build live production tools for Apple Immersive Video

**Event:** WWDC26 · **Topic:** Audio & Video · **Platforms:** macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-338](https://developer.apple.com/videos/play/wwdc2026/338)

Go behind the scenes of live Apple Immersive Video production. Discover how to package immersive video, spatial audio, and scene metadata for transport over IP networks using the SMPTE 2110 standard. Harness Apple’s Immersive Media Support, Video Toolbox, and AVFoundation frameworks to power real-time Apple Immersive Video workflows. To get the most out of this session, watch “Learn about Apple Immersive Video technologies” from WWDC25.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,314 words)

## Documentation & Resources

- [kVTCompressionPropertyKey_ProjectionKind](https://developer.apple.com/documentation/VideoToolbox/kVTCompressionPropertyKey_ProjectionKind) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VideoToolbox/kVTCompressionPropertyKey_ProjectionKind
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VideoToolbox/kVTCompressionPropertyKey_ProjectionKind.json
- [CMVideoCodecType](https://developer.apple.com/documentation/CoreMedia/CMVideoCodecType) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreMedia/CMVideoCodecType
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreMedia/CMVideoCodecType.json
- [Apple ProRes RAW White Paper](https://www.apple.com/final-cut-pro/docs/Apple_ProRes_RAW.pdf) _documentation_
- [Apple ProRes White Paper](https://www.apple.com/final-cut-pro/docs/Apple_ProRes.pdf) _documentation_
- [Immersive Media Support](https://developer.apple.com/documentation/ImmersiveMediaSupport) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ImmersiveMediaSupport
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ImmersiveMediaSupport.json

## Code Snippets

### Set compression properties for vexu metadata — [13:17]

```swift
import VideoToolbox

let compressionProperties: [String: Any] = [
    // ...
    kVTCompressionPropertyKey_ProjectionKind as String: kVTProjectionKind_AppleImmersiveVideo
    // ...
]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/338/5/4549be24-44c7-4214-ab9b-f21f9ed04691/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/338/5/4549be24-44c7-4214-ab9b-f21f9ed04691/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/338) — developer.apple.com. Indexed for agent consumption._