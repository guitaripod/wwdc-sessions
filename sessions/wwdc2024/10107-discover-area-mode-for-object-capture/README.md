---
id: "wwdc2024-10107"
event: "wwdc2024"
year: 2024
title: "Discover area mode for Object Capture"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10107"
topics: ["Developer Tools", "Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "macOS"]
hasTranscript: true
---

# Discover area mode for Object Capture

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** iOS, macOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10107](https://developer.apple.com/videos/play/wwdc2024/10107)

Discover how area mode for Object Capture enables new 3D capture possibilities on iOS by extending the functionality of Object Capture to support capture and reconstruction of an area. Learn how to optimize the quality of iOS captures using the new macOS sample app for reconstruction, and find out how to view the final results with Quick Look on Apple Vision Pro, iPhone, iPad or Mac. Learn about improvements to 3D reconstruction, including a new API that allows you to create your own custom image processing pipelines.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,997 words)

## Documentation & Resources

- [Building an object reconstruction app](https://developer.apple.com/documentation/RealityKit/building-an-object-reconstruction-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/building-an-object-reconstruction-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/building-an-object-reconstruction-app.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Data Loading API - load Sample and Mask — [8:19]

```swift
func loadSampleAndMask(file: URL) -> PhotogrammetrySample? {
    do {
        var sample = try PhotogrammetrySample(contentsOf: file)
        sample.objectMask = try loadObjectMask(for: file)
        return sample
    } catch {
        return nil
    }
}
```

### Data Loading API - create custom photogrammetry Session — [9:15]

```swift
func createCustomPhotogrammetrySession(for images: [URL]) -> PhotogrammetrySession {
    let inputSequence = images.lazy.compactMap { file in
        return loadSampleAndMask(file: file)
    }
    return PhotogrammetrySession(input: inputSequence)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10107/4/94F3C53B-10C1-4E39-8B9F-33A5BA561420/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10107/4/94F3C53B-10C1-4E39-8B9F-33A5BA561420/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10107) — developer.apple.com. Indexed for agent consumption._
