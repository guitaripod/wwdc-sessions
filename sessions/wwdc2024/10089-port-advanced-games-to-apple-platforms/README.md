---
id: "wwdc2024-10089"
event: "wwdc2024"
year: 2024
title: "Port advanced games to Apple platforms"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10089"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Port advanced games to Apple platforms

**Event:** WWDC24 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10089](https://developer.apple.com/videos/play/wwdc2024/10089)

Discover how simple it can be to reach players on Apple platforms worldwide. We’ll show you how to evaluate your Windows executable on Apple silicon, start your game port with code samples, convert your shader code to Metal, and bring your game to Mac, iPhone, and iPad. Explore enhanced Metal tools that understand HLSL shaders to validate, debug, and profile your ported shaders on Metal.

**Keywords:** `game porting toolkit`, `game porting toolkit 2`, `gptk2`, `ios games`, `ipad games`, `mac games`, `metal`, `metal-cpp`, `metalfx`, `metal shader converter`, `metal shading language`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,638 words)

## Documentation & Resources

- [Simplifying GPU resource management with residency sets](https://developer.apple.com/documentation/Metal/simplifying-gpu-resource-management-with-residency-sets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/simplifying-gpu-resource-management-with-residency-sets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/simplifying-gpu-resource-management-with-residency-sets.json
- [Validating your app’s Metal API usage](https://developer.apple.com/documentation/Xcode/Validating-your-apps-Metal-API-usage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Validating-your-apps-Metal-API-usage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Validating-your-apps-Metal-API-usage.json
- [Validating your app’s Metal shader usage](https://developer.apple.com/documentation/Xcode/Validating-your-apps-Metal-shader-usage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Validating-your-apps-Metal-shader-usage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Validating-your-apps-Metal-shader-usage.json
- [Download the Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/games/game-porting-toolkit/
- [Forum: Graphics & Games](https://developer.apple.com/forums/topics/graphics-and-games?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/graphics-and-games?cid=vf-a-0010
- [Get started with Metal shader converter](https://developer.apple.com/metal/shader-converter/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/shader-converter/
- [Metal Developer Resources](https://developer.apple.com/metal/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/
- [Getting started with Metal-cpp](https://developer.apple.com/metal/cpp/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/cpp/
- [Rendering reflections in real time using ray tracing](https://developer.apple.com/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-reflections-in-real-time-using-ray-tracing.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Build a residency set — [12:51]

```cpp
// Build a residency set.

// Create a new residency set.
MTL::ResidencySet* residencySet;
residencySet = device->newResidencySet(residencySetDescriptor, &error);

// Add to main command queue.
commandQueue->addResidencySet(residencySet);

// Add allocations and commit changes.
residencySet->addAllocation(texture);
residencySet->addAllocation(buffer);
residencySet->addAllocation(heap);
residencySet->commit();

  // Use residency sets.

// Allocate and encode a command buffer.
MTL::CommandBuffer* commandBuffer = commandQueue->commandBuffer();

// ...

// The command queue marks residency for the set for this command buffer.
commandBuffer->commit();
```

### Upscale image with MetalFX — [14:46]

```cpp
// Upscale image with MetalFX.

mfxTemporalScaler->setColorTexture(currentFrameColor);
mfxTemporalScaler->setDepthTexture(currentFrameDepth);
mfxTemporalScaler->setMotionTexture(currentFrameMotion);
mfxTemporalScaler->setOutputTexture(currentFrameUpscaledColor);

mfxTemporalScaler->setJitterOffsetX(currentFrameJitter.x);
mfxTemporalScaler->setJitterOffsetY(currentFrameJitter.y);

mfxTemporalScaler->setReactiveMaskTexture(currentFrameReactiveMask);

mfxTemporalScaler->encodeToCommandBuffer(commandBuffer);
```

### Use the cloud save manager — [19:53]

```objectivec
// Use the cloud save manager.

CloudSaveManager* cloudSaveManager =
    [[CloudSaveManager alloc] initWithCloudIdentifier:@"iCloud.com.mycompany.mygame"
                              saveDirectoryURL:[NSURL fileURLWithPath:@"/path/to/saves"]];

[cloudSaveManager syncWithCompletionHandler:^(BOOL conflictDetected, NSError *error) {
    // Handle conflicts or errors, for example, by presenting a choice.
}];

// Access and write saves
[cloudSaveManager uploadWithCompletionHandler:^(BOOL conflictDetected, NSError *error) {
    // Handle errors and conflicts or delay until the next sync.
}];
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10089/5/DFD23E3B-AB98-42B1-9219-9C8B1FCD44EA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10089/5/DFD23E3B-AB98-42B1-9219-9C8B1FCD44EA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10089) — developer.apple.com. Indexed for agent consumption._
