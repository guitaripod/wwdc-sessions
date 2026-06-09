---
id: "wwdc2022-10102"
event: "wwdc2022"
year: 2022
title: "Target and optimize GPU binaries with Metal 3"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10102"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Target and optimize GPU binaries with Metal 3

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10102](https://developer.apple.com/videos/play/wwdc2022/10102)

Discover how you can reduce in-app stutters, first launch times, and new level load times when you generate your GPU binaries entirely at project build time with offline compilation. We'll also show you how to improve total compile time and binary size for larger GPU programs using the "Optimize for size" compiler option.

**Keywords:** `compilation`, `compiler`, `metal`, `metal shading language`, `metal tools`, `performance`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,159 words)

## Documentation & Resources

- [MTLLibraryOptimizationLevel](https://developer.apple.com/documentation/Metal/MTLLibraryOptimizationLevel) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/MTLLibraryOptimizationLevel
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/MTLLibraryOptimizationLevel.json
- [Minimizing the binary size of a shader library](https://developer.apple.com/documentation/Metal/minimizing-the-binary-size-of-a-shader-library) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/minimizing-the-binary-size-of-a-shader-library
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/minimizing-the-binary-size-of-a-shader-library.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Using a JSON editor: render pipeline descriptor — [4:47]

```objectivec
// An existing Obj-C render pipeline descriptor
NSError *error = nil;
id<MTLDevice> device = MTLCreateSystemDefaultDevice();

id<MTLLibrary> library = [device newLibraryWithFile:@"default.metallib" error:&error];

MTLRenderPipelineDescriptor *desc = [MTLRenderPipelineDescriptor new];
desc.vertexFunction = [library newFunctionWithName:@"vert_main"];
desc.fragmentFunction = [library newFunctionWithName:@"frag_main"];
desc.rasterSampleCount = 2;
desc.colorAttachments[0].pixelFormat = MTLPixelFormatBGRA8Unorm;
desc.depthAttachmentPixelFormat = MTLPixelFormatDepth32Float;
```

### Using a JSON editor: pipelines script — [4:47]

```json
{
  "//comment": "Its equivalent new JSON script",
  "libraries": {
    "paths": [
      {
        "path": "default.metallib"
      }
    ]
  },
  "pipelines": {
    "render_pipelines": [
      {
        "vertex_function": "vert_main",
        "fragment_function": "frag_main",
        "raster_sample_count": 2,
        "color_attachments": [
          {
            "pixel_format": "BGRA8Unorm"
          },
        ],
        "depth_attachment_pixel_format": "Depth32Float"
      }
    ]
  }
}
```

### Harvesting sample — [5:33]

```objectivec
// Create pipeline descriptor
MTLRenderPipelineDescriptor *pipeline_desc = [MTLRenderPipelineDescriptor new];
pipeline_desc.vertexFunction = [library newFunctionWithName:@"vert_main"];
pipeline_desc.fragmentFunction = [library newFunctionWithName:@"frag_main"];
pipeline_desc.rasterSampleCount = 2;
pipeline_desc.colorAttachments[0].pixelFormat = MTLPixelFormatBGRA8Unorm;
pipeline_desc.depthAttachmentPixelFormat = MTLPixelFormatDepth32Float;

// Add pipeline descriptor to new archive
MTLBinaryArchiveDescriptor* archive_desc = [MTLBinaryArchiveDescriptor new];
id<MTLBinaryArchive> archive = [device newBinaryArchiveWithDescriptor:archive_desc error:&error];
bool success = [archive addRenderPipelineFunctionsWithDescriptor:pipeline_desc error:&error];

// Serialize archive to file system
NSURL *url = [NSURL fileURLWithPath:@"harvested-binaryArchive.metallib"];
success = [archive serializeToURL:url error:&error];
```

### Extracting a JSON script — [6:01]

```bash
metal-source -flatbuffers=json harvested-binaryArchive.metallib -o /tmp/descriptors.mtlp-json
```

### Generate a GPU binary from source — [6:24]

```bash
metal shaders.metal -N descriptors.mtlp-json -o archive.metallib
```

### Generate a GPU binary from Metal library — [6:48]

```bash
metal-tt shaders.metallib descriptors.mtlp-json -o archive.metallib
```

### Load GPU binaries via the runtime API — [7:07]

```objectivec
MTLBinaryArchiveDescriptor *desc = [MTLBinaryArchiveDescriptor new];
desc.url = [NSURL fileURLWithPath:@"archive.metallib"];
NSError *error = nil;
id<MTLDevice> device = MTLCreateSystemDefaultDevice();
id<MTLBinaryArchive> binaryArchive = [device newBinaryArchiveWithDescriptor:desc error:&error];
```

### Enable optimize for size in command lines — [12:11]

```bash
xcrun metal -Os large_shader.metal

# or

xcrun metal -c -Os large_shader.metal
xcrun metal -c     more_shaders.metal
xcrun metal large_shader.air more_shaders.air
```

### Enable optimize for size with Metal framework — [12:44]

```objectivec
MTLCompileOptions* options = [MTLCompileOptions new];
options.optimizationLevel = MTLLibraryOptimizationLevelSize;

NSString* source = @"...";
NSError* error = nil;
id<MTLLibrary> lib = [device newLibraryWithSource:source
                                          options:options
                                            error:&error];
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10102/4/E03398C4-8CAE-4CA1-905A-22205249E038/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10102/4/E03398C4-8CAE-4CA1-905A-22205249E038/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10102) — developer.apple.com. Indexed for agent consumption._