---
id: "wwdc2020-10615"
event: "wwdc2020"
year: 2020
title: "Build GPU binaries with Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10615"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Build GPU binaries with Metal

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10615](https://developer.apple.com/videos/play/wwdc2020/10615)

Power up your shader pipeline with enhancements to the Metal shader compilation model — all leading to a dramatic reduction in Pipeline State Object (PSO) loading time, especially upon first launch. Learn about explicit PSO caching and sharing of GPU binaries using Metal binary archives and dynamic libraries. And we’ll detail the toolchain to create libraries and improve your shader compilation workflow.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,180 words)

## Documentation & Resources

- [Creating a Metal dynamic library](https://developer.apple.com/documentation/Metal/creating-a-metal-dynamic-library) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/creating-a-metal-dynamic-library
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/creating-a-metal-dynamic-library.json
- [Metal Developer Tools on Windows](https://developer.apple.com/download/more/?=Metal%20Developer%20Tools%20for%20Windows) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/more/?=Metal%20Developer%20Tools%20for%20Windows
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Creating an empty archive — [6:19]

```swift
let descriptor = MTLBinaryArchiveDescriptor()
descriptor.url = nil
let binaryArchive = try device.makeBinaryArchive(descriptor:descriptor)
```

### Populating an archive — [6:47]

```swift
// Render pipelines
try binaryArchive.addRenderPipelineFunctions(with: renderPipelineDescriptor)

// Compute pipelines
try binaryArchive.addComputePipelineFunctions(with: computePipelineDescriptor)

// Tile render pipelines
try binaryArchive.addTileRenderPipelineFunctions(with: tileRenderPipelineDescriptor)
```

### Reusing compiled functions — [6:56]

```swift
// Reusing compiled functions to build a pipeline state object from a file

let renderPipelineDescriptor = MTLRenderPipelineDescriptor()
// ...
renderPipelineDescriptor.binaryArchives = [ binaryArchive ]

let renderPipeline = try device.makeRenderPipelineState(descriptor:  
                                                          renderPipelineDescriptor)
```

### Serialization — [7:15]

```swift
let documentsURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
let archiveURL = documentsURL.appendingPathComponent("binaryArchive.metallib")

try binaryArchive.serialize(to: NSURL.fileURL(withPath: archiveURL))
```

### Deserialization — [7:26]

```swift
let documentsURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
let serializeURL = documentsURL.appendingPathComponent("binaryArchive.metallib")

let descriptor = MTLBinaryArchiveDescriptor()
descriptor.url = NSURL.fileURL(withPath: serializeURL)
let binaryArchive = try device.makeBinaryArchive(descriptor: descriptor)
```

### Runtime compiled dynamic library — [17:18]

```swift
let options = MTLCompileOptions();
options.libraryType = .dynamic;
options.installName = "@executable_path/myDynamicLibrary.metallib"
let utilityLib = try device.makeLibrary(source: dylibSrc, options: options)
let utilityDylib = try device.makeDynamicLibrary(library: utilityLib)
```

### Compiling with a dynamic library — [17:59]

```swift
let options = MTLCompileOptions()
options.libraries = [ utilityDylib ]
let library = try device.makeLibrary(source: kernelStr, options: options)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10615/4/E619263D-7298-4BD0-B998-1954AF02BEB2/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10615) — developer.apple.com. Indexed for agent consumption._