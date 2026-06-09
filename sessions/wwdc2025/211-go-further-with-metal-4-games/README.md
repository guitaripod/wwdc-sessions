---
id: "wwdc2025-211"
event: "wwdc2025"
year: 2025
title: "Go further with Metal 4 games"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/211"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Go further with Metal 4 games

**Event:** WWDC25 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-211](https://developer.apple.com/videos/play/wwdc2025/211)

Dive deeper into the latest advancements in Metal 4. We’ll introduce the new ray tracing features that help bring your most complex and visually rich workloads to Apple silicon. Discover how MetalFX can help scale workloads by upscaling renderings, interpolating frames, and denoising scenes. To get the most out of this session, we recommend first checking out “Discover Metal 4” and “Explore Metal 4 games”.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,722 words)

## Code Snippets

### Reactive Mask — [6:46]

```objectivec
// Create reactive mask setup in shader
out.reactivity = m_material_id == eRain ? (m_material_id == eSpark ? 1.0f : 0.0f) : 0.8f;

// Set reactive mask before encoding upscaler on host
temporalUpscaler.reactiveMask = reactiveMaskTexture;
```

### MetalFX Frame Interpolator — [8:35]

```objectivec
// Create and configure the interpolator descriptor
MTLFXFrameInterpolatorDescriptor* desc = [MTLFXFrameInterpolatorDescriptor new];
desc.scaler = temporalScaler;
// ...

// Create the effect and configure your effect
id<MTLFXFrameInterpolator> interpolator = [desc newFrameInterpolatorWithDevice:device];
interpolator.motionVectorScaleX = mvecScaleX;
interpolator.motionVectorScaleY = mvecScaleY;
interpolator.depthReversed = YES;

// Set input textures
interpolator.colorTexture = colorTexture;
interpolator.prevColorTexture = prevColorTexture;
interpolator.depthTexture = depthTexture;
interpolator.motionTexture = motionTexture;
interpolator.outputTexture = outputTexture;
```

### Interpolator present helper class — [12:45]

```cpp
#include <thread>
#include <mutex>
#include <sys/event.h>
#include <mach/mach_time.h>


class PresentThread
{
    int m_timerQueue;
    std::thread m_encodingThread, m_pacingThread;
    std::mutex m_mutex;
    std::condition_variable m_scheduleCV, m_threadCV, m_pacingCV;
    float m_minDuration;

    uint32_t m_width, m_height;
    MTLPixelFormat m_pixelFormat;

    const static uint32_t kNumBuffers = 3;
    uint32_t m_bufferIndex, m_inputIndex;
    bool m_renderingUI, m_presentsPending;

    CAMetalLayer *m_metalLayer;
    id<MTLCommandQueue> m_presentQueue;

    id<MTLEvent> m_event;
    id<MTLSharedEvent> m_paceEvent, m_paceEvent2;
    uint64_t m_eventValue;
    uint32_t m_paceCount;

    int32_t m_numQueued, m_framesInFlight;

    id<MTLTexture> m_backBuffers[kNumBuffers];
    id<MTLTexture> m_interpolationOutputs[kNumBuffers];
    id<MTLTexture> m_interpolationInputs[2];
    id<MTLRenderPipelineState> m_copyPipeline;

    std::function<void(id<MTLRenderCommandEncoder>)> m_uiCallback = nullptr;

    void PresentThreadFunction();
    void PacingThreadFunction();

    void CopyTexture(id<MTLCommandBuffer> commandBuffer, id<MTLTexture> dest, id<MTLTexture> src, NSString *label);

public:

    PresentThread(float minDuration, CAMetalLayer *metalLayer);
    ~PresentThread()
    {
        std::unique_lock<std::mutex> lock(m_mutex);
        m_numQueued = -1;
        m_threadCV.notify_one();
        m_encodingThread.join();
    }
    void StartFrame(id<MTLCommandBuffer> commandBuffer)
    {
        [commandBuffer encodeWaitForEvent:m_event value:m_eventValue++];
    }

    void StartUI(id<MTLCommandBuffer> commandBuffer)
    {
        assert(m_uiCallback == nullptr);
        if(!m_renderingUI)
        {
            CopyTexture(commandBuffer, m_interpolationInputs[m_inputIndex], m_backBuffers[m_bufferIndex], @"Copy HUDLESS");
            m_renderingUI = true;
        }
    }

    void Present(id<MTLFXFrameInterpolator> frameInterpolator, id<MTLCommandQueue> queue);

    id<MTLTexture> GetBackBuffer()
    {
        return m_backBuffers[m_bufferIndex];
    }

    void Resize(uint32_t width, uint32_t height, MTLPixelFormat pixelFormat);

    void DrainPendingPresents()
    {
        std::unique_lock<std::mutex> lock(m_mutex);
        while(m_presentsPending)
            m_scheduleCV.wait(lock);
    }

    bool UICallbackEnabled() const
    {
        return m_uiCallback != nullptr;
    }

    void SetUICallback(std::function<void(id<MTLRenderCommandEncoder>)> callback)
    {
        m_uiCallback = callback;
    }

};

PresentThread::PresentThread(float minDuration, CAMetalLayer *metalLayer)
    : m_encodingThread(&PresentThread::PresentThreadFunction, this)
    , m_pacingThread(&PresentThread::PacingThreadFunction, this)
    , m_minDuration(minDuration)
    , m_numQueued(0)
    , m_metalLayer(metalLayer)
    , m_inputIndex(0u)
    , m_bufferIndex(0u)
    , m_renderingUI(false)
    , m_presentsPending(false)
    , m_framesInFlight(0)
    , m_paceCount(0)
    , m_eventValue(0)
{
    id<MTLDevice> device = metalLayer.device;
    m_presentQueue = [device newCommandQueue];
    m_presentQueue.label = @"presentQ";
    m_timerQueue = kqueue();

    metalLayer.maximumDrawableCount = 3;

    Resize(metalLayer.drawableSize.width, metalLayer.drawableSize.height, metalLayer.pixelFormat);

    m_event = [device newEvent];
    m_paceEvent = [device newSharedEvent];
	m_paceEvent2 = [device newSharedEvent];
}


void PresentThread::Present(id<MTLFXFrameInterpolator> frameInterpolator, id<MTLCommandQueue> queue)
{
    id<MTLCommandBuffer> commandBuffer = [queue commandBuffer];

    if(m_renderingUI)
    {
        frameInterpolator.colorTexture = m_interpolationInputs[m_inputIndex];
        frameInterpolator.prevColorTexture = m_interpolationInputs[m_inputIndex^1];
        frameInterpolator.uiTexture = m_backBuffers[m_bufferIndex];
    }
    else
    {
        frameInterpolator.colorTexture = m_backBuffers[m_bufferIndex];
        frameInterpolator.prevColorTexture = m_backBuffers[(m_bufferIndex + kNumBuffers - 1) % kNumBuffers];
        frameInterpolator.uiTexture = nullptr;
    }

    frameInterpolator.outputTexture = m_interpolationOutputs[m_bufferIndex];

    [frameInterpolator encodeToCommandBuffer:commandBuffer];
    [commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> _Nonnull) {
        std::unique_lock<std::mutex> lock(m_mutex);
        m_framesInFlight--;
        m_scheduleCV.notify_one();
        m_paceCount++;
        m_pacingCV.notify_one();
    }];
    [commandBuffer encodeSignalEvent:m_event value:m_eventValue++];
    [commandBuffer commit];

    std::unique_lock<std::mutex> lock(m_mutex);
    m_framesInFlight++;
    m_numQueued++;
    m_presentsPending = true;
    m_threadCV.notify_one();
    while((m_framesInFlight >= 2) || (m_numQueued >= 2))
        m_scheduleCV.wait(lock);

    m_bufferIndex = (m_bufferIndex + 1) % kNumBuffers;
    m_inputIndex = m_inputIndex^1u;
    m_renderingUI = false;
}

void PresentThread::CopyTexture(id<MTLCommandBuffer> commandBuffer, id<MTLTexture> dest, id<MTLTexture> src, NSString *label)
{
    MTLRenderPassDescriptor *desc = [MTLRenderPassDescriptor new];
    desc.colorAttachments[0].texture = dest;
    desc.colorAttachments[0].loadAction = MTLLoadActionDontCare;
    desc.colorAttachments[0].storeAction = MTLStoreActionStore;
    id<MTLRenderCommandEncoder> renderEncoder = [commandBuffer renderCommandEncoderWithDescriptor:desc];
    [renderEncoder setFragmentTexture:src atIndex:0];
    [renderEncoder setRenderPipelineState:m_copyPipeline];
    [renderEncoder drawPrimitives:MTLPrimitiveTypeTriangle vertexStart:0 vertexCount:3];
    if(m_uiCallback)
        m_uiCallback(renderEncoder);
    renderEncoder.label = label;
    [renderEncoder endEncoding];
}


void PresentThread::PacingThreadFunction()
{
    NSThread *thread = [NSThread currentThread];
    [thread setName:@"PacingThread"];
    [thread setQualityOfService:NSQualityOfServiceUserInteractive];
    [thread setThreadPriority:1.f];

    mach_timebase_info_data_t info;
    mach_timebase_info(&info);

    // maximum delta (0.1ms) in machtime units
    const uint64_t maxDeltaInNanoSecs = 100000000;
    const uint64_t maxDelta = maxDeltaInNanoSecs * info.denom / info.numer;

    uint64_t time = mach_absolute_time();

    uint64_t paceEventValue = 0;

    for(;;)
    {
        std::unique_lock<std::mutex> lock(m_mutex);
        while(m_paceCount == 0)
            m_pacingCV.wait(lock);
        m_paceCount--;
        lock.unlock();

        // we get signal...
        const uint64_t prevTime = time;
        time = mach_absolute_time();
		m_paceEvent.signaledValue = ++paceEventValue;

        const uint64_t delta = std::min(time - prevTime, maxDelta);
        const uint64_t timeStamp = time + ((delta*31)>>6);

        struct kevent64_s timerEvent, eventOut;
        struct timespec timeout;
        timeout.tv_nsec = maxDeltaInNanoSecs;
        timeout.tv_sec = 0;
        EV_SET64(&timerEvent,
                 0,
                 EVFILT_TIMER,
                 EV_ADD | EV_ONESHOT | EV_ENABLE,
                 NOTE_CRITICAL | NOTE_LEEWAY | NOTE_MACHTIME | NOTE_ABSOLUTE,
                 timeStamp,
                 0,
                 0,
                 0);

        kevent64(m_timerQueue, &timerEvent, 1, &eventOut, 1, 0, &timeout);

        // main screen turn on...
        m_paceEvent2.signaledValue = ++paceEventValue;
    }
}


void PresentThread::PresentThreadFunction()
{
    NSThread *thread = [NSThread currentThread];
    [thread setName:@"PresentThread"];
    [thread setQualityOfService:NSQualityOfServiceUserInteractive];
    [thread setThreadPriority:1.f];


    uint64_t eventValue = 0;
    uint32_t bufferIndex = 0;

    uint64_t paceEventValue = 0;

    for(;;)
    {
        std::unique_lock<std::mutex> lock(m_mutex);

        if(m_numQueued == 0)
        {
            m_presentsPending = false;
            m_scheduleCV.notify_one();
        }

        while(m_numQueued == 0)
            m_threadCV.wait(lock);

        if(m_numQueued < 0)
            break;
        lock.unlock();

        @autoreleasepool
        {
            id<CAMetalDrawable> drawable = [m_metalLayer nextDrawable];

			lock.lock();
			m_numQueued--;
			m_scheduleCV.notify_one();
			lock.unlock();

            id<MTLCommandBuffer> commandBuffer = [m_presentQueue commandBuffer];
            [commandBuffer encodeWaitForEvent:m_event value:++eventValue];
            CopyTexture(commandBuffer, drawable.texture, m_interpolationOutputs[bufferIndex], @"Copy Interpolated");
            [commandBuffer encodeSignalEvent:m_event value:++eventValue];
			[commandBuffer encodeWaitForEvent:m_paceEvent value:++paceEventValue];

            if(m_minDuration > 0.f)
                [commandBuffer presentDrawable:drawable afterMinimumDuration:m_minDuration];
            else
                [commandBuffer presentDrawable:drawable];
            [commandBuffer commit];
        }

        @autoreleasepool
        {
            id<MTLCommandBuffer> commandBuffer = [m_presentQueue commandBuffer];
            id<CAMetalDrawable> drawable = [m_metalLayer nextDrawable];
            CopyTexture(commandBuffer, drawable.texture, m_backBuffers[bufferIndex], @"Copy Rendered");
			[commandBuffer encodeWaitForEvent:m_paceEvent2 value:++paceEventValue];
            if(m_minDuration > 0.f)
                [commandBuffer presentDrawable:drawable afterMinimumDuration:m_minDuration];
            else
                [commandBuffer presentDrawable:drawable];
            [commandBuffer commit];
        }

        bufferIndex = (bufferIndex + 1) % kNumBuffers;
    }
}

void PresentThread::Resize(uint32_t width, uint32_t height, MTLPixelFormat pixelFormat)
{
    if((m_width != width) || (m_height != height) || (m_pixelFormat != pixelFormat))
    {
        id<MTLDevice> device = m_metalLayer.device;

        if(m_pixelFormat != pixelFormat)
        {
            id<MTLLibrary> lib = [device newDefaultLibrary];
            MTLRenderPipelineDescriptor *pipelineDesc = [MTLRenderPipelineDescriptor new];
            pipelineDesc.vertexFunction = [lib newFunctionWithName:@"FSQ_VS_V4T2"];
            pipelineDesc.fragmentFunction = [lib newFunctionWithName:@"FSQ_simpleCopy"];
            pipelineDesc.colorAttachments[0].pixelFormat = pixelFormat;
            m_copyPipeline = [device newRenderPipelineStateWithDescriptor:pipelineDesc error:nil];
            m_pixelFormat = pixelFormat;
        }

        DrainPendingPresents();

        m_width = width;
		m_height = height;

        MTLTextureDescriptor *texDesc = [MTLTextureDescriptor texture2DDescriptorWithPixelFormat:pixelFormat width:width height:height mipmapped:NO];
		texDesc.storageMode = MTLStorageModePrivate;
        for(uint32_t i = 0; i < kNumBuffers; i++)
        {
            texDesc.usage = MTLTextureUsageShaderRead|MTLTextureUsageShaderWrite|MTLTextureUsageRenderTarget;
            m_backBuffers[i] = [device newTextureWithDescriptor:texDesc];
            texDesc.usage = MTLTextureUsageShaderRead|MTLTextureUsageRenderTarget;
            m_interpolationOutputs[i] = [device newTextureWithDescriptor:texDesc];
        }
        texDesc.usage = MTLTextureUsageShaderRead|MTLTextureUsageRenderTarget;
        m_interpolationInputs[0] = [device newTextureWithDescriptor:texDesc];
        m_interpolationInputs[1] = [device newTextureWithDescriptor:texDesc];

    }
}
```

### Set intersection function table offset — [13:00]

```swift
// Set intersection function table offset on host-side geometry descriptors
NSMutableArray<MTLAccelerationStructureGeometryDescriptor *> *geomDescs ...;
for (auto g = 0; g < geomList.size(); ++g)
{
    MTLAccelerationStructureGeometryDescriptor *descriptor = ...;
    descriptor.intersectionFunctionTableOffset = g;
    ...
    [geomDescs addObject:descriptor];
}
```

### Set up the intersector — [13:01]

```objectivec
// Set up the intersector
metal::raytracing::intersector<intersection_function_buffer, instancing, triangle> trace;
trace.set_geometry_multiplier(2); // Number of ray types, defaults to 1
trace.set_base_id(1);             // Set ray type index, defaults to 0
```

### Ray trace intersection function buffers — [13:02]

```objectivec
// Ray trace intersection function buffers

// Set up intersection function buffer arguments
intersection_function_buffer_arguments ifb_arguments;
ifb_arguments.intersection_function_buffer = raytracingResources.ifbBuffer;
ifb_arguments.intersection_function_buffer_size = raytracingResources.ifbBufferSize;
ifb_arguments.intersection_function_stride = raytracingResources.ifbBufferStride;

// Set up the ray and finish intersecting
metal::raytracing::ray r = { origin, direction };
auto result = trace.intersect(r, ads, ifb_arguments);
```

### Change of temporal scaler setup to denoised temporal scaler setup — [13:02]

```objectivec
// Change of temporal scaler setup to denoised temporal scaler setup

MTLFXTemporalScalerDescriptor* desc = [MTLFXTemporalScalerDescriptor new];
desc.colorTextureFormat = MTLPixelFormatBGRA8Unorm_sRGB;
desc.outputTextureFormat = MTLPixelFormatBGRA8Unorm_sRGB;
desc.depthTextureFormat = DepthStencilFormat;
desc.motionTextureFormat = MotionVectorFormat;

desc.diffuseAlbedoTextureFormat = DiffuseAlbedoFormat;
desc.specularAlbedoTextureFormat = SpecularAlbedoFormat;
desc.normalTextureFormat = NormalVectorFormat;
desc.roughnessTextureFormat = RoughnessFormat;

desc.inputWidth = _mainViewWidth;
desc.inputHeight = _mainViewHeight;
desc.outputWidth = _screenWidth;
desc.outputHeight = _screenHeight;
temporalScaler = [desc newTemporalDenoisedScalerWithDevice:_device];
```

### Change temporal scaler encode to denoiser temporal scaler encode — [13:04]

```objectivec
// Change temporal scaler encode to denoiser temporal scaler encode

temporalScaler.colorTexture = _mainView;
temporalScaler.motionTexture = _motionTexture;

temporalScaler.diffuseAlbedoTexture = _diffuseAlbedoTexture;
temporalScaler.specularAlbedoTexture = _specularAlbedoTexture;
temporalScaler.normalTexture = _normalTexture;
temporalScaler.roughnessTexture = _roughnessTexture;

temporalScaler.depthTexture = _depthTexture;
temporalScaler.jitterOffsetX = _pixelJitter.x;
temporalScaler.jitterOffsetY = -_pixelJitter.y;
temporalScaler.outputTexture = _upscaledColorTarget;
temporalScaler.motionVectorScaleX = (float)_motionTexture.width;
temporalScaler.motionVectorScaleY = (float)_motionTexture.height;
[temporalScaler encodeToCommandBuffer:commandBuffer];
```

### Creating instance descriptors for instance acceleration structure — [16:04]

```objectivec
// Creating instance descriptors for instance acceleration structure
MTLAccelerationStructureInstanceDescriptor *grassInstanceDesc, *treeInstanceDesc = . . .;
grassInstanceDesc.intersectionFunctionTableOffset = 0;
treeInstanceDesc.intersectionFunctionTableOffset  = 1;

// Create buffer for instance descriptors of as many trees/grass instances the scene holds
id <MTLBuffer> instanceDescs = . . .;
for (auto i = 0; i < scene.instances.size(); ++i)
. . .
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/211/4/03920d98-a8a0-4cc8-bc99-3fcf874e0232/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/211/4/03920d98-a8a0-4cc8-bc99-3fcf874e0232/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/211) — developer.apple.com. Indexed for agent consumption._
