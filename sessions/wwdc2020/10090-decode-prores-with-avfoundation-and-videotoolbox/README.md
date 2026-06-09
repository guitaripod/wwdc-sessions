---
id: "wwdc2020-10090"
event: "wwdc2020"
year: 2020
title: "Decode ProRes with AVFoundation and VideoToolbox"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10090"
topics: ["Developer Tools", "Graphics & Games", "Audio & Video"]
platforms: ["macOS"]
hasTranscript: true
---

# Decode ProRes with AVFoundation and VideoToolbox

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10090](https://developer.apple.com/videos/play/wwdc2020/10090)

Make decoding and displaying ProRes content easier in your Mac app: Learn how to implement an optimal graphics pipeline by leveraging AVFoundation and VideoToolbox’s decoding capabilities. We’ll share best practices and performance considerations for your app, show you how to integrate Afterburner cards into your pipeline, and walk through how you can display decoded frames using Metal.

**Keywords:** `av foundation`, `metal`, `performance`, `prores`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,318 words)

## Documentation & Resources

- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Creating an AVAssetReader is pretty easy — [7:41]

```objectivec
// Constructing an AVAssetReader

// Create an AVAsset with an URL pointing at a local asset
AVAsset *sourceMovieAsset = [AVAsset assetWithURL:sourceMovieURL];

// Create an AVAssetReader for the asset
AVAssetReader *assetReader = [AVAssetReader assetReaderWithAsset:sourceMovieAsset 
                                                           error:&error];
```

### // Configuring AVAssetReaderTrackOutput — [7:58]

```objectivec
// Configuring AVAssetReaderTrackOutput

// Copy the array of video tracks from the source movie
NSArray<AVAssetTrack*>  *tracks = [sourceMovieAsset tracksWithMediaType:AVMediaTypeVideo];

// Get the first video track
AVAssetTrack *track = [sourceMovieVideoTracks objectAtIndex:0];

// Create the asset reader track output for this video track, requesting ‘y416’ output
NSDictionary *outputSettings = @{ (id)kCVPixelBufferPixelFormatTypeKey :
                                  @(kCVPixelFormatType_4444AYpCbCr16) };

AVAssetReaderTrackOutput* assetReaderTrackOutput
= [AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:track
                                             outputSettings:outputSettings];

// Set the property to instruct the track output to return the samples 
// without copying them
assetReaderTrackOutput.alwaysCopiesSampleData = NO;

// Connect the the AVAssetReaderTrackOutput to the AVAssetReader
[assetReader addOutput:assetReaderTrackOutput];
```

### Running AVAssetReader — [8:57]

```objectivec
// Running AVAssetReader

BOOL success = [assetReader startReading];

if (success) {
   CMSampleBufferRef sampleBuffer = NULL;

   // output is a AVAssetReaderOutput
   while ((sampleBuffer = [output copyNextSampleBuffer]))
   {
       CVImageBufferRef imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);

       if (imageBuffer)
       {
          // Use the image buffer here
          // if imageBuffer is NULL, this is likely a marker sampleBuffer
       }
    }
}
```

### Prepareing CMSampleBuffers for optimized RPC transfer — [11:40]

```objectivec
AVAssetReaderTrackOutput* assetReaderTrackOutput
= [AVAssetReaderTrackOutput assetReaderTrackOutputWithTrack:track
                                             outputSettings:nil];
```

### How an AVSampleBufferGenerator is created — [12:24]

```objectivec
AVSampleCursor* cursor = [assetTrack makeSampleCursorAtFirstSampleInDecodeOrder];

AVSampleBufferRequest* request = [[AVSampleBufferRequest alloc] initWithStartCursor:cursor];

request.direction = AVSampleBufferRequestDirectionForward;
request.preferredMinSampleCount = 1;
request.maxSampleCount = 1;

AVSampleBufferGenerator* generator
= [[AVSampleBufferGenerator alloc] initWithAsset:srcAsset timebase:nil];

BOOL notDone = YES;

while(notDone)
{
   CMSampleBufferRef sampleBuffer = [generator createSampleBufferForRequest:request];

   // do your thing with the sampleBuffer

   [cursor stepInDecodeOrderByCount:1];
}
```

### Pack your sample data into a CMBlockBuffer — [13:40]

```objectivec
CMBlockBufferCreateWithMemoryBlock(kCFAllocatorDefault, sampleData, sizeof(sampleData), 
                                   kCFAllocatorMalloc, NULL, 0, sizeof(sampleData), 0, 
                                   &blockBuffer);

CMVideoFormatDescriptionCreate(kCFAllocatorDefault, kCMVideoCodecType_AppleProRes4444, 1920, 
                               1080, extensionsDictionary, &formatDescription);

CMSampleTimingInfo timingInfo;

timingInfo.duration = CMTimeMake(10, 600);
timingInfo.presentationTimeStamp = CMTimeMake(frameNumber * 10, 600);

CMSampleBufferCreateReady(kCFAllocatorDefault, blockBuffer, formatDescription, 1, 1, 
                          &timingInfo, 1, &sampleSize, &sampleBuffer);
```

### VTDecompressionSession Creation — [17:47]

```objectivec
// VTDecompressionSession Creation

CMFormatDescriptionRef formatDesc = CMSampleBufferGetFormatDescription(sampleBuffer);

CFDictionaryRef pixelBufferAttributes = (__bridge CFDictionaryRef)@{
    (id)kCVPixelBufferPixelFormatTypeKey :
    @(kCVPixelFormatType_4444AYpCbCr16) };

VTDecompressionSessionRef decompressionSession;

OSStatus err = VTDecompressionSessionCreate(kCFAllocatorDefault, 
                                            formatDesc, 
                                            NULL,
                                            pixelBufferAttributes, 
                                            NULL, 
                                            &decompressionSession);
```

### Running a VTDecompressionSession — [18:30]

```objectivec
// Running a VTDecompressionSession

uint32_t inFlags = kVTDecodeFrame_EnableAsynchronousDecompression;

VTDecompressionOutputHandler  outputHandler
 = ^(OSStatus status,
     VTDecodeInfoFlags infoFlags,
     CVImageBufferRef imageBuffer,
     CMTime presentationTimeStamp,
     CMTime presentationDurationVTDecodeInfoFlags)
 {
     // Handle decoder output in this block
     // Status reports any decoder errors
     // imageBuffer contains the decoded frame if there were no errors
 };

VTDecodeInfoFlags outFlags;

OSStatus err = VTDecompressionSessionDecodeFrameWithOutputHandler(decompressionSession,
                                                   sampleBuffer, inFlags, 
                                                   &outFlags, outputHandler);
```

### CVPixelBuffer to Metal texture: IOSurface — [20:54]

```objectivec
// CVPixelBuffer to Metal texture: IOSurface

IOSurfaceRef surface = CVPixelBufferGetIOSurface(imageBuffer);

id <MTLTexture> metalTexture = [metalDevice newTextureWithDescriptor:descriptor
                                                           iosurface:surface 
                                                               plane:0];

// Mark the IOSurface as in-use so that it won’t be recycled by the CVPixelBufferPool
IOSurfaceIncrementUseCount(surface);

// Set up command buffer completion handler to decrement IOSurface use count again
[cmdBuffer addCompletedHandler:^(id<MTLCommandBuffer> buffer) {
     IOSurfaceDecrementUseCount(surface);
 }];
```

### Create a CVMetalTextureCacheRef — [21:42]

```objectivec
// Create a CVMetalTextureCacheRef

CVMetalTextureCacheRef metalTextureCache = NULL;

id <MTLDevice> metalDevice = MTLCreateSystemDefaultDevice();

CVMetalTextureCacheCreate(kCFAllocatorDefault, NULL, metalDevice, NULL, &metalTextureCache);

// Create a CVMetalTextureRef using metalTextureCache and our pixelBuffer
CVMetalTextureCacheCreateTextureFromImage(kCFAllocatorDefault,
                                          metalTextureCache,
                                          pixelBuffer,
                                          NULL,
                                          pixelFormat,
                                          CVPixelBufferGetWidth(pixelBuffer),
                                          CVPixelBufferGetHeight(pixelBuffer),
                                          0,
                                          &cvTexture);

id <MTLTexture>  texture = CVMetalTextureGetTexture(cvTexture);
// Be sure to release the cvTexture object when the Metal command buffer completes!
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10090/6/EA16694F-BEEC-44FF-A129-12336E5390B9/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10090) — developer.apple.com. Indexed for agent consumption._
