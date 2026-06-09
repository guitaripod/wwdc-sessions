---
id: "wwdc2021-10148"
event: "wwdc2021"
year: 2021
title: "Optimize high-end games for Apple GPUs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10148"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Optimize high-end games for Apple GPUs

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10148](https://developer.apple.com/videos/play/wwdc2021/10148)

Optimize your high-end games for Apple GPUs: We’ll show you how you can use our rendering and debugging tools to eliminate performance issues and make your games great on Apple platforms. Learn from our experiences working with developers at Larian Studios and 4A Games as we help them optimize their games for Apple GPUs.

We’ll explore various techniques for improving your game’s performance, including optimizing shaders, reducing memory bandwidth utilization, and increasing the overlap of your GPU workloads. We’ll also dive into the new GPU Timeline profiling tool in Xcode 13 to identify possible performance bottlenecks in “Divinity: Original Sin 2” when running on iPad.

For this session, you should be familiar with the tile-based deferred rendering architecture in Apple GPUs, and have a working knowledge of Xcode and the Metal API.

Check out “Discover Metal debugging, profiling, and asset creation tools” or the WWDC20 session “Optimize Metal apps and games with GPU counters” to learn more about using our tools to profile graphics workloads.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,383 words)

## Documentation & Resources

- [Debugging the shaders within a draw command or compute dispatch](https://developer.apple.com/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Debugging-the-shaders-within-a-draw-command-or-compute-dispatch.json
- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### Pseudocode to choose shared and private buffer count — [15:24]

```objectivec
// Number of frames application is processing
static const uint32_t MAX_FRAMES_IN_FLIGHT = 3;

uint32_t sharedBuffersCount  = 0; // Number of buffers with MTLStorageModeShared to create
uint32_t privateBuffersCount = 0; // Number of buffers with MTLStorageModePrivate to create
if (device.hasUnifiedMemory)
{     // Use extra buffer to reduce impact of completion handler
    sharedBuffersCount = MAX_FRAMES_IN_FLIGHT + 1;
    privateBuffersCount = 0;
}
else // GPUs with dedicated memory
{
    sharedBuffersCount = MAX_FRAMES_IN_FLIGHT;
    privateBuffersCount = 1;
}

// Create shared buffers MTLStorageModeShared
// If applicable, create private buffer
```

### Pseudocode to avoid redundant bindings — [21:40]

```objectivec
void Renderer::SetFragmentTexture(uint32_t index, id<MTLTexture> texture)
{
    if (m_FragmentTextures[index] != texture)
    {
        m_FragmentTextures[index] = texture;
        m_FragmentTexturesChanged = true;
    }
}

void Renderer::BindFragmentTextures()
{
    if (m_FragmentTexturesChanged)
    {
        [m_RenderCommandEncoder setFragmentTextures:m_FragmentTextures 
                          withRange:NSMakeRange(0, m_LastFragmentTexture + 1)];

        m_FragmentTexturesChanged = false;
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10148/8/2E6A96C2-2CC3-4852-A318-C5F493B55EC6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10148/8/2E6A96C2-2CC3-4852-A318-C5F493B55EC6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10148) — developer.apple.com. Indexed for agent consumption._