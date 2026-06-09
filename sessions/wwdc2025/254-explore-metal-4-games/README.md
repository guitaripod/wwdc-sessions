---
id: "wwdc2025-254"
event: "wwdc2025"
year: 2025
title: "Explore Metal 4 games"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/254"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Explore Metal 4 games

**Event:** WWDC25 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-254](https://developer.apple.com/videos/play/wwdc2025/254)

Learn to optimize your game engine with the latest advancements in Metal 4. We’ll cover how to unify your command encoding to minimize CPU overhead, scale up your graphics resource management to support massive scenes and maximize your memory budget, and load large libraries of pipeline states quickly. To get the most out of this session, first watch “Discover Metal 4.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,785 words)

## Documentation & Resources

- [Metal binary archives](https://developer.apple.com/documentation/Metal/metal-binary-archives) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/metal-binary-archives
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/metal-binary-archives.json
- [Reading and writing to sparse textures](https://developer.apple.com/documentation/Metal/reading-and-writing-to-sparse-textures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/reading-and-writing-to-sparse-textures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/reading-and-writing-to-sparse-textures.json
- [Synchronizing passes with producer barriers](https://developer.apple.com/documentation/Metal/synchronizing-passes-with-producer-barriers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/synchronizing-passes-with-producer-barriers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/synchronizing-passes-with-producer-barriers.json
- [Synchronizing passes with consumer barriers](https://developer.apple.com/documentation/Metal/synchronizing-passes-with-consumer-barriers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/synchronizing-passes-with-consumer-barriers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/synchronizing-passes-with-consumer-barriers.json
- [Synchronizing passes with a fence](https://developer.apple.com/documentation/Metal/synchronizing-passes-with-a-fence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/synchronizing-passes-with-a-fence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/synchronizing-passes-with-a-fence.json
- [Synchronizing stages within a pass](https://developer.apple.com/documentation/Metal/synchronizing-stages-within-a-pass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/synchronizing-stages-within-a-pass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/synchronizing-stages-within-a-pass.json
- [Resource synchronization](https://developer.apple.com/documentation/Metal/resource-synchronization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/resource-synchronization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/resource-synchronization.json
- [Drawing a triangle with Metal 4](https://developer.apple.com/documentation/Metal/drawing-a-triangle-with-metal-4) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/drawing-a-triangle-with-metal-4
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/drawing-a-triangle-with-metal-4.json
- [Using the Metal 4 compilation API](https://developer.apple.com/documentation/Metal/using-the-metal-4-compilation-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/using-the-metal-4-compilation-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/using-the-metal-4-compilation-api.json
- [Understanding the Metal 4 core API](https://developer.apple.com/documentation/Metal/understanding-the-metal-4-core-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/understanding-the-metal-4-core-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/understanding-the-metal-4-core-api.json
- [Human Interface Guidelines: Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-games

## Code Snippets

### Synchronize access to a buffer within an encoder — [0:01]

```objectivec
// Synchronize access to a buffer within an encoder

id<MTL4ComputeCommandEncoder> encoder = [commandBuffer computeCommandEncoder];

[encoder copyFromBuffer:src sourceOffset:0 toBuffer:buffer1 destinationOffset:0 size:64];

[encoder barrierAfterEncoderStages:MTLStageBlit 
               beforeEncoderStages:MTLStageDispatch
                 visibilityOptions:MTL4VisibilityOptionDevice];

[encoder setComputePipelineState:pso];

[argTable setAddress:buffer1.gpuAddress atIndex:0];
[encoder setArgumentTable:argTable];
[encoder dispatchThreads:threadsPerGrid threadsPerThreadgroup:threadsPerThreadgroup];

[encoder endEncoding];code snippet.
```

### Configure superset of color attachments — [4:29]

```objectivec
// Configure superset of color attachments

MTL4RenderPassDescriptor *desc = [MTLRenderPassDescriptor renderPassDescriptor];

desc.supportColorAttachmentMapping = YES;

desc.colorAttachments[0].texture = colortex0;
desc.colorAttachments[1].texture = colortex1;
desc.colorAttachments[2].texture = colortex2;
desc.colorAttachments[3].texture = colortex3;
desc.colorAttachments[4].texture = colortex4;
```

### Set color attachment map entries — [4:38]

```objectivec
// Set color attachment map entries

MTLLogicalToPhysicalColorAttachmentMap* myAttachmentRemap = [MTLLogicalToPhysicalColorAttachmentMap new];

[myAttachmentRemap setPhysicalIndex:0 forLogicalIndex:0];
[myAttachmentRemap setPhysicalIndex:3 forLogicalIndex:1];
[myAttachmentRemap setPhysicalIndex:4 forLogicalIndex:2];
```

### Set a color attachment map per pipeline — [4:57]

```objectivec
// Set a color attachment map per pipeline

[renderEncoder setRenderPipelineState:myPipeline];
[renderEncoder setColorAttachmentMap:myAttachmentRemap];
// Draw with myPipeline

[renderEncoder setRenderPipelineState:myPipeline2];
[renderEncoder setColorAttachmentMap:myAttachmentRemap2];
// Draw with myPipeline2
```

### Encode a single render pass with 3 render encoders — [8:03]

```objectivec
// Encode a single render pass with 3 render encoders with suspend/resume options


id<MTL4RenderCommandEncoder> enc0 = [cmdbuf0 renderCommandEncoderWithDescriptor:desc options:MTL4RenderEncoderOptionSuspending];

id<MTL4RenderCommandEncoder> enc1 = [cmdbuf1 renderCommandEncoderWithDescriptor:desc options:MTL4RenderEncoderOptionResuming | MTL4RenderEncoderOptionSuspending];

id<MTL4RenderCommandEncoder> enc2 = [cmdbuf2 renderCommandEncoderWithDescriptor:desc options:MTL4RenderEncoderOptionResuming];


id<MTL4CommandBuffer> cmdbufs[] = { cmdbuf0, cmdbuf1, cmdbuf2 };
[commandQueue commit:cmdbufs count:3]
```

### Synchronize drawable contents — [11:48]

```objectivec
// Synchronize drawable contents

id<MTLDrawable> drawable = [metalLayer nextDrawable];
[queue waitForDrawable:drawable];

// ... encode render commands to commandBuffer ...
[queue commit:&commandBuffer count:1];

[queue signalDrawable:drawable];

[drawable present];
```

### Encode a queue barrier to synchronize data — [13:25]

```objectivec
// Encode a queue barrier to synchronize data

id<MTL4ComputeCommandEncoder> compute = [commandBuffer computeCommandEncoder];

[compute dispatchThreadgroups:threadGrid threadsPerThreadgroup:threadsPerThreadgroup];

[compute endEncoding];


id<MTL4RenderCommandEncoder> render = [commandBuffer renderCommandEncoderWithDescriptor:des];

[render barrierAfterQueueStages:MTLStageDispatch
                   beforeStages:MTLStageFragment
              visibilityOptions:MTL4VisibilityOptionDevice];

[renderCommandEncoder drawPrimitives:MTLPrimitiveTypeTriangle
                         vertexStart:vertexStart
                         vertexCount:vertexCount];

[render endEncoding];
```

### Create a texture view pool — [14:57]

```objectivec
// Create a texture view pool

MTLResourceViewPoolDescriptor *desc = [[MTLResourceViewPoolDescriptor alloc] init]; 
desc.resourceCount = 500;

id <MTLTextureViewPool> myTextureViewPool =  
    [myDevice newTextureViewPoolWithDescriptor:myTextureViewPoolDescriptor 
                                         error:nullptr];
```

### Set a texture view — [15:07]

```objectivec
// Set a texture view

MTLResourceID myTextureView = [myTextureViewPool setTextureView:myTexture  
                                                     descriptor:myTextureViewDescriptor  
                                                        atIndex:5];

[myArgumentTable setTexture:myTextureView 
                    atIndex:0];
```

### Choose appropriate sparse page size — [16:01]

```objectivec
MTLHeapDescriptor *desc = [MTLHeapDescriptor new];    
desc.type = MTLHeapTypePlacement;
desc.storageMode = MTLStorageModePrivate;
desc.maxCompatiblePlacementSparsePageSize = MTLSparsePageSize64;
desc.size = alignedHeapSize;

id<MTLHeap> heap = [device newHeapWithDescriptor:desc];
```

### Update buffer mappings — [17:05]

```objectivec
// Update buffer mappings

MTL4UpdateSparseBufferMappingOperation bufferOperation;

bufferOperation.mode = MTLSparseTextureMappingModeMap;  
bufferOperation.bufferRange.location = bufferOffsetInTiles;
bufferOperation.bufferRange.length = length;
bufferOperation.heapOffset = heapOffsetInTiles;

[cmdQueue updateBufferMappings:myBuf heap:myHeap operations:&bufferOperation count:1];
```

### Set unspecialized configuration — [20:41]

```objectivec
// In MTL4RenderPipelineColorAttachmentDescriptor
// Set unspecialized configuration

pipelineDescriptor.colorAttachments[i].pixelFormat   = MTLPixelFormatUnspecialized;
pipelineDescriptor.colorAttachments[i].writeMask     = MTLColorWriteMaskUnspecialized;
pipelineDescriptor.colorAttachments[i].blendingState = MTL4BlendStateUnspecialized;
```

### Create a specialized transparent pipeline — [21:40]

```objectivec
// Create a specialized transparent pipeline

// Set the previously unspecialized properties
pipelineDescriptor.colorAttachments[0].pixelFormat = MTLPixelFormatBGRA8Unorm;
pipelineDescriptor.colorAttachments[0].writeMask =
    MTLColorWriteMaskRed | MTLColorWriteMaskGreen | MTLColorWriteMaskBlue;
pipelineDescriptor.colorAttachments[0].blendingState = MTL4BlendStateEnabled;

pipelineDescriptor.colorAttachments[0].sourceRGBBlendFactor = MTLBlendFactorOne;
pipelineDescriptor.colorAttachments[0].destinationRGBBlendFactor = 
    MTLBlendFactorOneMinusSourceAlpha;
pipelineDescriptor.colorAttachments[0].rgbBlendOperation = MTLBlendOperationAdd;

id<MTLRenderPipelineState> transparentPipeline = 
    [compiler newRenderPipelineStateBySpecializationWithDescriptor:pipelineDescriptor
                                                          pipeline:unspecializedPipeline
                                                             error:&error];

// Similarly, create the specialized opaque and hologram pipelines
```

### Determine thread count — [26:22]

```objectivec
// Determine thread count
NSInteger numThreads = 2;
if (@available(macOS 13.3, iOS 19, visionOS 3, tvOS 19, *))
{
    numThreads = [device maximumConcurrentCompilationTaskCount];
}
```

### Set a proper QoS class for your compilation threads — [26:30]

```objectivec
// Create thread pool
for (NSInteger i = 0; i < numThreads; ++i)
{
    // Creating a thread with a QoS class DEFAULT
    pthread_attr_set_qos_class_np(&attr, QOS_CLASS_DEFAULT, 0) ;
    pthread_create(&threadIds[i], &attr, entryPoint, NULL);
    pthread_attr_destroy(&attr);
}
```

### Harvest pipeline configuration scripts — [28:24]

```objectivec
// Harvest pipeline configuration scripts with the pipeline data set serializer

// Create a pipeline data set serializer that only captures descriptors
MTL4PipelineDataSetSerializerDescriptor *desc = [MTL4PipelineDataSetSerializerDescriptor new];
desc.configuration = MTL4PipelineDataSetSerializerConfigurationCaptureDescriptors;
id<MTL4PipelineDataSetSerializer> serializer =
    [device newPipelineDataSetSerializerWithDescriptor:desc];

// Set the pipeline data set serializer when creating the compiler
MTL4CompilerDescriptor *compilerDesc = [MTL4CompilerDescriptor new];
[compilerDesc setPipelineDataSetSerializer:serializer];
id<MTL4Compiler> compiler = [device newCompilerWithDescriptor:compilerDesc error:nil];

// Create pipelines using the compiler as usual

// Serialize the descriptors as a pipeline script
NSData *data = [serializer serializeAsPipelinesScriptWithError:&err];

// Write the pipeline script data to disk
NSString *path = [NSString pathWithComponents:@[folder, @"pipelines.mtl4-json"]];
BOOL success = [data writeToFile:path options:NSDataWritingAtomic error:&err];
```

### Query pipeline state from MTLArchive — [30:28]

```objectivec
// Query pipeline state from MTLArchive

id<MTL4Archive> archive = [device newArchiveWithURL:archiveURL error:&error];

id<MTLRenderPipelineState> pipeline = 
    [archive newRenderPipelineStateWithDescriptor:descriptor error:&error];

if (pipeline == nil)
{
    // handle lookup miss
		pipeline = [compiler newRenderPipelineStateWithDescriptor:descriptor 
                                          compilerTaskOptions:nil 
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/254/6/a73ce35f-7f81-4203-9df3-46c48308ca6f/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/254/6/a73ce35f-7f81-4203-9df3-46c48308ca6f/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/254) — developer.apple.com. Indexed for agent consumption._
