---
id: "wwdc2026-357"
event: "wwdc2026"
year: 2026
title: "Speedrun your game port with agentic coding"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/357"
topics: ["AI & Machine Learning", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Speedrun your game port with agentic coding

**Event:** WWDC26 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-357](https://developer.apple.com/videos/play/wwdc2026/357)

Kickstart your game’s journey to Apple platforms with new agentic skills in Game Porting Toolkit 4 that can dramatically accelerate the process of porting your game. Explore how to work alongside your AI coding assistant to adopt Metal 4, integrate MetalFX, and tune your game for Apple hardware. Find out how agents can autonomously troubleshoot GPU rendering issues using Metal debugging tools, empowering you to focus on what matters most.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,353 words)

## Documentation & Resources

- [Game Porting Toolkit on GitHub](https://github.com/apple/game-porting-toolkit/) _download_
- [Download the Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/games/game-porting-toolkit/

## Code Snippets

### Install Game Porting Toolkit skills — [3:31]

```bash
/plugin marketplace add apple/game-porting-toolkit
/plugin install game-porting-skills@game-porting-toolkit
```

### Register resources for residency — [10:24]

```cpp
// With skill
residencySet->addAllocation(texture);
residencySet->commit();
// ...
argumentTable->setAddress(texture->gpuAddress(), bindPoint);

// Without skill
argumentTable->setAddress(texture->gpuAddress(), bindPoint);
```

### Query argument buffer offsets — [11:25]

```cpp
// With skill
IRRootSignatureGetResourceLocations(m_MtlCurIRRootSig, locations);
size_t offset = locations[i].topLevelOffset;

// Without skill
size_t offset = paramIndex * descriptorSize;
```

### Map D3D12 states to Metal 4 stages — [12:34]

```cpp
// With skill
m_MtlPendingProducerStages |= MtlProducerStageFromD3D12(OldState);
m_MtlPendingConsumerStages |= MtlConsumerStageFromD3D12(NewState);
// ...
m_ComputeEncoder->barrierAfterStages(
    m_MtlPendingProducerStages,
    m_MtlPendingConsumerStages,
    MTL4::VisibilityOptionDevice);

// Without skill
m_ComputeEncoder->barrierAfterStages(
    MTL::StageDispatch,
    MTL::StageAll,
    MTL4::VisibilityOptionDevice);
```

### Query shader reflection parameter count — [14:24]

```cpp
// With skill
IRShaderReflection* refl = IRShaderReflectionCreate();
IRObjectGetReflection(compiledObj, IRShaderStageCompute, refl);
// ...
s_RootSignature.Reset(4, 2); // Reflection reveals: 4 params

// Without skill
s_RootSignature.Reset(5, 2);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/357/5/5cfd0ceb-598f-4535-9abc-12e22a778326/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/357/5/5cfd0ceb-598f-4535-9abc-12e22a778326/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/357) — developer.apple.com. Indexed for agent consumption._
