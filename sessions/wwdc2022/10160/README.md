---
id: "wwdc2022-10160"
event: "wwdc2022"
year: 2022
title: "Program Metal in C++ with metal-cpp"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10160"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Program Metal in C++ with metal-cpp

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10160](https://developer.apple.com/videos/play/wwdc2022/10160)

Your C++ games and apps can now tap into the power of Metal. We'll show you how metal-cpp helps you bridge your C++ code to Metal, explore how each manages object lifecycles, and demonstrate utilities that can help these language cooperate in your app. We'll also share best practices for designing app architecture to elegantly integrate Objective-C and C++ together.

**Keywords:** `c++`, `game dev`, `game developer`, `metal 3`, `metal-cpp`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,538 words)

## Documentation & Resources

- [Getting started with Metal-cpp](https://developer.apple.com/metal/cpp/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/cpp/
- [Download the LearnMetalCPP project](https://developer.apple.com/metal/LearnMetalCPP.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/LearnMetalCPP.zip
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Draw a single triangle in C++ — [3:10]

```cpp
MTL::CommandBuffer* pCmd = _pCommandQueue->commandBuffer();
MTL::RenderCommandEncoder* pEnc = pCmd->renderCommandEncoder( pRpd );
pEnc->setRenderPipelineState( _pPSO );
pEnc->drawPrimitives( MTL::PrimitiveTypeTriangle, 
                      NS::UInteger(0), 
                      NS::UInteger(3));
pEnc->endEncoding();
pCmd->presentDrawable( pView->currentDrawable() );
pCmd->commit();
```

### Draw a single triangle in Objective-C — [3:27]

```objectivec
id<MTLCommandBuffer> cmd = [_commandQueue commandBuffer];
id<MTLRenderCommandEncoder> enc = [cmd renderCommandEncoderWithDescriptor:pRpd];
[enc setRenderPipelineState:_pPSO];
[enc drawPrimitives:MTLPrimitiveTypeTriangle 
        vertexStart:0 
        vertexCount:3];
[enc endEncoding];
[cmd presentDrawable:view.currentDrawable];
[cmd commit];
```

### Generate the implementation — [6:10]

```cpp
#define NS_PRIVATE_IMPLEMENTATION
#define CA_PRIVATE_IMPLEMENTATION
#define MTL_PRIVATE_IMPLEMENTATION

#include <Foundation/Foundation.hpp>
#include <Metal/Metal.hpp>
#include <QuartzCore/QuartzCore.hpp>
```

### How to use autoreleased objects and AutoreleasePool — [11:46]

```cpp
NS::AutoreleasePool* pPool = NS::AutoreleasePool::alloc()->init();
MTL::CommandBuffer* pCmd = _pCommandQueue->commandBuffer();
MTL::RenderPassDescriptor* pRpd = pView->currentRenderPassDescriptor();
MTL::RenderCommandEncoder* pEnc = pCmd->renderCommandEncoder( pRpd );
pEnc->endEncoding();
pCmd->presentDrawable( pView->currentDrawable() );
pCmd->commit();
pPool->release();
```

### How NS::TransferPtr works — [11:47]

```cpp
{
   auto ptr = NS::TransferPtr( pMRR );
   // Do something with ptr 
   . . . 
}
```

### How NS::RetainPtr works — [17:19]

```cpp
{
   auto ptr = NS::RetainPtr( pMRR );
   // Do something with ptr 
   . . . 
}
```

### Create an adapter class calling C++ from Objective-C files — [20:43]

```objectivec
@interface AAPLRendererAdapter () 
{
    AAPLRenderer* _pRenderer;
}
@end

@implementation AAPLRendererAdapter
- (void)drawInMTKView:(MTKView *)pMtkView
{
    _pRenderer->draw((__bridge MTK::View*)pMtkView);
}

@end
```

### Create an adapter class calling Objective-C from C++ files — [21:49]

```cpp
CA::MetalDrawable* AAPLViewAdapter::currentDrawable() const
{
    return (__bridge CA::MetalDrawable*)[(__bridge MTKView *)m_pMTKView currentDrawable];
}

MTL::Texture* AAPLViewAdapter::depthStencilTexture() const
{
    return (__bridge MTL::Texture*)[(__bridge MTKView *)m_pMTKView depthStencilTexture];
}
```

### Cast between Objective-C and C++ objects and transfer ownership — [24:59]

```cpp
MTL::Texture* newTextureFromCatalog( MTL::Device* pDevice, const char* name,   
                                     MTL::StorageMode storageMode, MTL::TextureUsage usage )
{
    NSDictionary<MTKTextureLoaderOption, id>* options = @{
            MTKTextureLoaderOptionTextureStorageMode : @( (MTLStorageMode)storageMode ),
            MTKTextureLoaderOptionTextureUsage : @( (MTLTextureUsage)usage )
    };

    MTKTextureLoader* textureLoader = [[MTKTextureLoader alloc] 
                                        initWithDevice:(__bridge id<MTLDevice>)pDevice];

    NSError* __autoreleasing err = nil;
    id< MTLTexture > texture = [textureLoader 
                        newTextureWithName:[NSString stringWithUTF8String:name] 
                               scaleFactor:1 
                                            bundle:nil 
                                           options:options 
                                             error:&err];

    return (__bridge_retained MTL::Texture*)texture;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10160/5/F0ACC08B-EFC0-459E-AE6D-DEA492619F49/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10160/5/F0ACC08B-EFC0-459E-AE6D-DEA492619F49/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10160) — developer.apple.com. Indexed for agent consumption._