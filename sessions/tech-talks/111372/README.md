---
id: "tech-talks-111372"
event: "tech-talks"
year: 2017
title: "Bring your high-end game to iPhone 15 Pro"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111372"
topics: ["Graphics & Games"]
platforms: ["iOS"]
hasTranscript: true
---

# Bring your high-end game to iPhone 15 Pro

**Event:** Tech Talks · **Topic:** Graphics & Games · **Platforms:** iOS · **Published:** 2023-11-09 · **Session:** [tech-talks-111372](https://developer.apple.com/videos/play/tech-talks/111372)

Discover how the power of A17 Pro can help you maximize your game on iPhone 15 Pro and iPhone 15 Pro Max. We’ll share best practices and technical resources, and explore ways to optimize game performance, input, and asset management.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,522 words)

## Documentation & Resources

- [Download the game porting toolkit](https://developer.apple.com/download/all/?q=game%20porting%20toolkit) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/all/?q=game%20porting%20toolkit

## Code Snippets

### Slide 24: Scale by GPU family capabilities — [0:01]

```objectivec
MTLDevice *device = MTLCreateSystemDefaultDevice();

if ([device supportsFamily:MTLGPUFamilyApple9]) {

   // features available in Apple GPU Family 9:

   //  hardware accelerated mesh shaders

   //  hardware accelerated ray-tracing

} else {

   // fall back on alternative techniques

}
```

### Slide 54: Scale textures size & quality — [0:02]

```objectivec
MTLDevice *device = MTLCreateSystemDefaultDevice();

if (device.supportsBCTextureCompression) {

   // BCn textures are available

} else {

   // fall back to ASTC texture assets for maximum compatibility

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111372/3/0849CEA3-A0B7-455C-AA2D-50F6C441BAED/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111372/3/0849CEA3-A0B7-455C-AA2D-50F6C441BAED/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111372) — developer.apple.com. Indexed for agent consumption._