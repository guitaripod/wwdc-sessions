---
id: "wwdc2023-10124"
event: "wwdc2023"
year: 2023
title: "Bring your game to Mac, Part 2: Compile your shaders"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10124"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Bring your game to Mac, Part 2: Compile your shaders

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10124](https://developer.apple.com/videos/play/wwdc2023/10124)

Discover how the Metal shader converter streamlines the process of bringing your HLSL shaders to Metal as we continue our three-part series on bringing your game to Mac. Find out how to build a fast, end-to-end shader pipeline from DXIL that supports all shader stages and allows you to leverage the advanced features of Apple GPUs. We’ll also show you how to reduce app launch time and stutters by generating GPU binaries with the offline compiler.

To get the most out of this session, we recommend first watching “Bring your game to Mac, Part 1: Make a game plan." And once you’re ready to level up, check out “Bring your game to Mac, Part 3: Render with Metal" from WWDC23.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,891 words)

## Documentation & Resources

- [Get started with Metal shader converter](https://developer.apple.com/metal/shader-converter/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/shader-converter/
- [Download the Metal shader converter (Mac and Windows)](https://developer.apple.com/download/all/?q=shader%20converter) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/all/?q=shader%20converter
- [Download the game porting toolkit](https://developer.apple.com/download/all/?q=game%20porting%20toolkit) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/all/?q=game%20porting%20toolkit
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Json Metal Script — [14:28]

```json
{“libraries": {
    "paths": [
   {"path": “ba.metallib”, "label": "myMetalLib"}

    ]
  },
  "pipelines": {
    "render_pipelines": [{
      "vertex_function": "alias:myMetalLib#v",
      "fragment_function": "alias:myMetalLib#f",
      "raster_sample_count": 2,
      "color_attachments": [{
          "pixel_format": "BGRA8Unorm"
      }],
      "depth_attachment_pixel_format":      
        "Depth32Float"
    }]
  }
}
```

### Testing Binary Archive hit — [16:30]

```objectivec
// Create Pipeline Descriptor
MTLComputePipelineDescriptor *computeDesc = [MTLComputePipelineDescriptor new];
computeDesc.binaryArchives = @[existingBinaryArchive];
computeDesc.computeFunction = computeFn;
id<MTLComputePipelineState> computePS = 
                     [device newComputePipelineStateWithDescriptor:computeDesc
                                     options:MTLPipelineOptionFailonBinaryArchiveMiss
                                     error:&err];                                                                                        

if(computePS == nil)
{
    // Binary archive is missing compiled shader.
}
```

### Loading appropriate Binary Archive — [17:03]

```objectivec
// Load OS-specific binary archives


MTLComputePipelineDescriptor *computeDesc = [MTLComputePipelineDescriptor new];

if (@available(macOS 14, *)) {
    computeDesc.binaryArchives = @[binaryArchive_macOS14];
} else {
    computeDesc.binaryArchives = @[binaryArchive_macOS13_3];
}  
computeDesc.computeFunction = computeFn;
id<MTLComputePipelineState> computePS = 
                     [device newComputePipelineStateWithDescriptor:computeDesc
                                     options:nil
                                     error:&err];
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10124/4/8043B2FD-2363-4733-85E6-CCDF0BEE783F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10124/4/8043B2FD-2363-4733-85E6-CCDF0BEE783F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10124) — developer.apple.com. Indexed for agent consumption._