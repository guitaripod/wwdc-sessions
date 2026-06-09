---
id: "wwdc2021-10161"
event: "wwdc2021"
year: 2021
title: "Explore HDR rendering with EDR"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10161"
topics: ["Audio & Video", "Photos & Camera", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore HDR rendering with EDR

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10161](https://developer.apple.com/videos/play/wwdc2021/10161)

EDR is Apple’s High Dynamic Range representation and rendering pipeline. Explore how you can render HDR content using EDR in your app and unleash the dynamic range capabilities of your HDR display including Apple’s internal displays and Pro Display XDR. We’ll show you how game and pro app developers can take advantage of the native EDR APIs on macOS for even more control, and provide best practices for deciding when HDR is appropriate, applying tone-mapping, and delivering HDR content.

**Keywords:** `display`, `display p3`, `edr`, `hdr`, `metal`, `metal shading language`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,512 words)

## Documentation & Resources

- [Processing HDR images with Metal](https://developer.apple.com/documentation/Metal/processing-hdr-images-with-metal) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/processing-hdr-images-with-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/processing-hdr-images-with-metal.json
- [Edit and play back HDR video with AVFoundation](https://apple.co/3orEzXX) _documentation_
- [Export HDR media in your app using AVFoundation](https://apple.co/2NA4pft) _documentation_
- [Editing and playing HDR video](https://developer.apple.com/documentation/AVFoundation/editing-and-playing-hdr-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/editing-and-playing-hdr-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/editing-and-playing-hdr-video.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json
- [Metal Shading Language Specification](https://developer.apple.com/metal/metal-shading-language-specification.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/metal-shading-language-specification.pdf

## Code Snippets

### AVPlayer automatically uses EDR with HDR content — [16:00]

```objectivec
// Instantiate AVPlayer with HDR Video Content

VPLayer*      player      = [AVPLayer playerWithURL:HDRVideoURL];
AVPlayerLayer* playerLayer = [AVPlayerLayer playerLayerWithPlayer:player];

// Play HDR Video via EDR

AVPlayerViewController* controller = [[AVPlayerViewController alloc] init];

controller.player = player;

[player play];
```

### EDR with CAMetalLayer 1 — [17:52]

```objectivec
// Opt-in to EDR

metalLayer.wantsExtendedDynamicRangeContent = YES;

// Set extended-range colorspace

metalLayer.colorspace =
              CGColorSpaceCreateWithName(kCGColorSpaceExtendedLinearDisplayP3);

// Select FP16 pixel buffer format

metalLayer.pixelFormat = MTLPixelFormatRGBA16Float;
```

### EDR with CAMetalLayer 2 — [18:53]

```objectivec
// Create CGImage from HDR Image

CGImageSourceRef isr = CGImageSourceCreateWithURL((CFURLRef)HDRimageURL, NULL);
CGImageRef       img = CGImageSourceCreateImageAtIndex(isr, 0, NULL);

// Draw into floating point bitmap context

size_t width  = CGImageGetWidth(img);
size_t height = CGImageGetHeight(img);

CGBitmapInfo info = kCGBitmapByteOrder16Host | kCGImageAlphaPremultipliedLast |
                    kCGBitmapFloatComponents;

CGContextRef ctx = CGBitmapContextCreate(NULL, width, height, 16, 0,
                                         metalLayer.colorspace, info);

CGContextDrawImage(ctx, CGRectMake(0, 0, width, height), img);

// Create floating point texture

MTLTextureDescriptor* desc = [[MTLTextureDescriptor alloc] init];

desc.pixelFormat = MTLPixelFormatRGBA16Float;
desc.textureType = MTLTextureType2D;

id<MTLTexture> tex = [metalLayer.device newTextureWithDescriptor:desc];

// Load EDR bitmap into texture

const void* data = CGBitmapContextGetData(ctx);

[tex replaceRegion:MTLRegionMake2D(0, 0, width, height)
       mipmapLevel:0
         withBytes:data
       bytesPerRow:CGBitmapContextGetBytesPerRow(ctx)];

// Draw with the texture in your EDR enabled metal pipeline
```

### EDR with NSOpenGLView — [20:30]

```objectivec
// Opt-in to EDR

  - (void) viewWillMoveToWindow:(nullable NSWindow *)newWindow {
     self.wantsExtendedDynamicRangeOpenGLSurface = YES;
  }

// Select OpenGL float pixel buffer format

  NSOpenGLPixelFormatAttribute attribs[] = {
    NSOpenGLPFADoubleBuffer,
    NSOpenGLPFAMultiSample,
    NSOpenGLPFAColorFloat,
    NSOpenGLPFAColorSize, 64, 
    NSOpenGLPFAOpenGLProfile, NSOpenGLProfileVersion4_1Core,
    0};

  NSOpenGLPixelFormat* pf = [[NSOpenGLPixelFormat alloc] initWithAttributes:attribs];

// Draw EDR content into NSOpenGLView
```

### EDR with NSOpenGLView — [21:46]

```objectivec
// Get existing colorspace from the window 

CGColorSpaceRef color_space = [view.window.colorSpace CGColorSpace];

// Promote the colorspace to extended-range

CGColorSpaceRef color_space_extended = CGColorSpaceCreateExtended(color_space);

// Apply the extended-range colorspace to your app

NSColorSpace* extended_ns_color_space
                   = [[NSColorSpace alloc] initWithCGColorSpace:color_space_extended];

view.window.colorSpace = extended_ns_color_space;

CGColorSpaceRelease(color_space_extended);
```

### EDR display change notifications via NSScreen — [29:00]

```objectivec
// Read static values

NSScreen* screen = window.screen;

double maxPotentialEDR = screen.maximumPotentialExtendedDynamicRangeColorComponentValue;
double maxReferenceEDR = screen.maximumReferenceExtendedDynamicRangeColorComponentValue;

// Register for dynamic EDR notifications

NSNotificationCenter* notification = [NSNotificationCenter defaultCenter];  

[notification addObserver:self
                 selector:@selector(screenChangedEvent:)
                     name:NSApplicationDidChangeScreenParametersNotification
                   object:nil];

// Query for latest values

- (void)screenChangedEvent:(NSNotification *)notification {  
    double maxEDR = screen.maximumExtendedDynamicRangeColorComponentValue;
}
```

### CAEDRMetadata tone-mapper — [30:28]

```objectivec
// HLG

CAEDRMetadata* edrMetaData = [CAEDRMetadata HLGMetadata];

// HDR10

CAEDRMetadata* edrMetaData
   = [CAEDRMetadata HDR10MetadataWithMinLuminance:minLuminance
                                     maxLuminance:maxContentMasteringDisplayBrightness 
                               opticalOutputScale:outputScale]; 

// Set on CAMetalLayer

metalLayer.EDRMetadata = edrMetaData;
```

### Computing your app’s brightest pixel — [31:35]

```objectivec
// Create the linear pixel we want to render

double EDRmaxComponents[4] = {EDRmax, EDRmax, EDRmax, 1.0};

CGColorSpaceRef linearColorSpace =
                   CGColorSpaceCreateWithName(kCGColorSpaceExtendedLinearDisplayP3);

CGColorRef EDRmaxColorLinear = CGColorCreate(linearColorSpace, EDRmaxComponents);

// Convert from linear to application’s colorspace

CGColorSpaceRef winColorSpace = [self.window.colorSpace CGColorSpace];

CGColorRef EDRmaxColor = CGColorCreateCopyByMatchingToColorSpace(winColorSpace,
                                                                 kCGRenderingIntentDefault,
                                                                 EDRmaxColorLinear,
                                                                 NULL);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10161/5/A571AEFA-117F-4E9C-B4A0-C4543637CBFA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10161/5/A571AEFA-117F-4E9C-B4A0-C4543637CBFA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10161) — developer.apple.com. Indexed for agent consumption._
