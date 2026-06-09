---
id: "wwdc2023-10125"
event: "wwdc2023"
year: 2023
title: "Bring your game to Mac, Part 3: Render with Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10125"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Bring your game to Mac, Part 3: Render with Metal

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10125](https://developer.apple.com/videos/play/wwdc2023/10125)

Discover how you can support Metal in your rendering code as we close out our three-part series on bringing your game to Mac. Once you’ve evaluated your existing Windows binary with the game porting toolkit and brought your HLSL shaders over to Metal, learn how you can optimally implement the features that high-end, modern games require. We’ll show you how to manage GPU resource bindings, residency, and synchronization. Find out how to optimize GPU commands submission, render rich visuals with MetalFX Upscaling, and more. To get the most out of this session, we recommend first watching “Bring your game to Mac, Part 1: Make a game plan” and “Bring your game to Mac, Part 2: Compile your shaders" from WWDC23.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,270 words)

## Documentation & Resources

- [Applying temporal antialiasing and upscaling using MetalFX](https://developer.apple.com/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalFX/applying-temporal-antialiasing-and-upscaling-using-metalfx.json
- [MetalFX](https://developer.apple.com/documentation/MetalFX) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalFX
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalFX.json
- [Modern rendering with Metal](https://developer.apple.com/documentation/Metal/modern-rendering-with-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/modern-rendering-with-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/modern-rendering-with-metal.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Encode the texture tables. — [3:55]

```objectivec
// Encode the texture tables outside of the rendering loop.


id<MTLBuffer> textureTable  = [device newBufferWithLength:sizeof(MTLResourceID) * texturesCount
                                                  options:MTLResourceStorageModeShared];


MTLResourceID* textureTableCPUPtr = (MTLResourceID*)textureTable.contents;
for (uint32_t i = 0; i < texturesCount; ++i)
{
    // create the textures.
    id<MTLTexture> texture = [device newTextureWithDescriptor:textureDesc[i]];

    // encode texture in argument buffer
    textureTableCPUPtr[i] = texture.gpuResourceID;
}
```

### Encode the sampler tables. — [4:33]

```objectivec
// Encode the sampler tables outside of the rendering loop.


id<MTLBuffer> samplerTable  = [device newBufferWithLength:sizeof(MTLResourceID) * samplersCount
                                                  options:MTLResourceStorageModeShared];

MTLResourceID* samplerTableCPUPtr = (MTLResourceID*)samplerTable.contents;
for (uint32_t i = 0; i < samplersCount; ++i)
{
    // create sampler descriptor
    MTLSamplerDescriptor* desc  = [MTLSamplerDescriptor new];
    desc.supportArgumentBuffers = YES;
    . . .

    // create a sampler
    id<MTLSamplerState> sampler = [device newSamplerStateWithDescriptor:desc];

    // encode the sampler in argument buffer
    samplerTableCPUPtr[i] = sampler.gpuResourceID;
}
```

### Encode the top level argument buffer. — [5:05]

```objectivec
// Encode the top level argument buffer.


struct TopLevelAB
{
    MTLResourceID* textureTable;
    float*         myBuffer;
    uint32_t       myConstant;
    MTLResourceID* samplerTable;
};

id<MTLBuffer> topAB = [device newBufferWithLength:sizeof(TopLevelAB)
                                          options:MTLResourceStorageModeShared];


TopLevelAB* topABCPUPtr     = (TopLevelAB*)topAB.contents;
topABCPUPtr->textureTable   = (MTLResourceID*)textureTable.gpuAddress;
topABCPUPtr->myBuffer       = (float*)myBuffer.gpuAddress;
topABCPUPtr->myConstant     = 128;
topABCPUPtr->samplerTable   = (MTLResourceID*)samplerTable.gpuAddress;
```

### Allocate the read-only resources. — [6:49]

```objectivec
// Allocate the read-only resources from a heap.

MTLHeapDescriptor* heapDesc = [MTLHeapDescriptor new];
heapDesc.size               = requiredSize;
heapDesc.type               = MTLHeapTypeAutomatic;

id<MTLHeap> heap = [device newHeapWithDescriptor:heapDesc];



// Allocate the textures and the buffers from the heap.

id<MTLTexture> texture = [heap newTextureWithDescriptor:desc];
id<MTLBuffer>  buffer = [heap newBufferWithLength:length options:options];
. . .


// Make the heap resident once for each encoder that uses it.

[encoder useHeap:heap];
```

### Allocate the writable resources. — [7:34]

```objectivec
// Allocate the writable resources individually.

id<MTLTexture> textureRW = [device newTextureWithDescriptor:desc];
id<MTLBuffer>  bufferRW  = [device newBufferWithLength:length options:options];



// Mark these resources resident when they're needed in the current encoder.
// Specify the resource usage in the encoder using MTLResourceUsage.

[encoder useResource:textureRW usage:MTLResourceUsageWrite stages:stage];
[encoder useResource:bufferRW  usage:MTLResourceUsageRead  stages:stage];
```

### Encode the execute indirect — [19:31]

```objectivec
// Encode the execute indirect command as a series of indirect draw calls.

for (uint32_t i = 0; i < maxDrawCount; ++i)
{
    // Encode the current indirect draw call.
    [renderEncoder drawIndexedPrimitives:MTLPrimitiveTypeTriangle
                       				 indexType:MTLIndexTypeUInt16
                             indexBuffer:indexBuffer
                       indexBufferOffset:indexBufferOffset
                          indirectBuffer:drawArgumentsBuffer
                    indirectBufferOffset:drawArgumentsBufferOffset];

    // Advance the draw arguments buffer offset to the next indirect arguments.
    drawArgumentsBufferOffset += sizeof(MTLDrawIndexedPrimitivesIndirectArguments);
}
```

### Translate the indirect draw arguments to ICB. — [21:48]

```cpp
// Kernel written in Metal Shading Language to translate the indirect draw arguments to an ICB. 


kernel void translateToICB(device const Command* indirectCommands [[ buffer(0) ]],
                           device const ICBContainerAB* icb [[ buffer(1) ]],
                           . . .)
{
    . . .

    device const Command* indirectCommand = &indirectCommands[commandIndex];
    device const MTLDrawIndexedPrimitivesIndirectArguments* args =
    &command->mdiBuffer[mdiIndex];

    render_command drawCall(icb->buffer, indirectCommand->mdiCmdStart + mdiIndex);

    if(args->indexCount > 0 && args->instanceCount > 0) {
        encodeCommand(indirectCommand, args, drawCall);
    }
    else {
        cmd.reset();
    }
}

// Encode a render command on the GPU.
void encodeCommand(device const Command* indirectCommand,
                   device const MTLDrawIndexedPrimitivesIndirectArguments* args,
                   thread render_command& drawCall)
{
    drawCall.set_render_pipeline_state(indirectCommand->pso);

    for(ushort i = 0; i < indirectCommand->vertexBuffersCount; ++i) {
        drawCall.set_vertex_buffer(indirectCommand->vertexBuffer[i].buffer,
                              indirectCommand->vertexBuffer[i].slot);
    }

    for(ushort i = 0; i < indirectCommand->fragmentBuffersCount; ++i) {
        drawCall.set_fragment_buffer(indirectCommand->fragmentBuffer[i].buffer,
                                indirectCommand->fragmentBuffer[i].slot);
    }

    drawCall.draw_indexed_primitives(primitive_type::triangle,
                                args->indexCount,
                                indirectCommand->indexBuffer + args->indexStart,
                                args->instanceCount,
                                args->baseVertex,
                                args->baseInstance);
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10125/4/1283FC25-C4D6-40B5-AAEC-221E3E4C6D16/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10125/4/1283FC25-C4D6-40B5-AAEC-221E3E4C6D16/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10125) — developer.apple.com. Indexed for agent consumption._
