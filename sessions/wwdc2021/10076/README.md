---
id: "wwdc2021-10076"
event: "wwdc2021"
year: 2021
title: "Create 3D models with Object Capture"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10076"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Create 3D models with Object Capture

**Event:** WWDC21 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10076](https://developer.apple.com/videos/play/wwdc2021/10076)

Object Capture provides a quick and easy way to create lifelike 3D models of real-world objects using just a few images. Learn how you can get started and bring your assets to life with Photogrammetry for macOS. And discover best practices with object selection and image capture to help you achieve the highest-quality results.

**Keywords:** `3d content creation`, `3d graphics`, `ar`, `arkit`, `augmented reality`, `photogrammetry`, `realitykit`, `usdz`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,385 words)

## Documentation & Resources

- [Creating a photogrammetry command-line app](https://developer.apple.com/documentation/RealityKit/creating-a-photogrammetry-command-line-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-a-photogrammetry-command-line-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-a-photogrammetry-command-line-app.json
- [Capturing photographs for RealityKit Object Capture](https://developer.apple.com/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture.json
- [Creating 3D objects from photographs](https://developer.apple.com/documentation/RealityKit/creating-3d-objects-from-photographs) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-3d-objects-from-photographs
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-3d-objects-from-photographs.json
- [Capturing photographs for RealityKit Object Capture](https://developer.apple.com/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture.json
- [PhotogrammetrySample](https://developer.apple.com/documentation/RealityKit/PhotogrammetrySample) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/PhotogrammetrySample
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/PhotogrammetrySample.json
- [PhotogrammetrySession](https://developer.apple.com/documentation/RealityKit/PhotogrammetrySession) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/PhotogrammetrySession
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/PhotogrammetrySession.json
- [Explore the RealityKit Developer Forums](https://developer.apple.com/forums/tags/realitykit) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/realitykit

## Code Snippets

### Creating a PhotogrammetrySession with a folder of images — [6:56]

```swift
import RealityKit

let inputFolderUrl = URL(fileURLWithPath: "/tmp/Sneakers/", isDirectory: true)
let session = try! PhotogrammetrySession(input: inputFolderUrl,
                                         configuration: PhotogrammetrySession.Configuration())
```

### Creating the async message stream dispatcher — [9:26]

```swift
// Create an async message stream dispatcher task

Task {
    do {
        for try await output in session.outputs {
            switch output {
            case .requestProgress(let request, let fraction):
                print("Request progress: \(fraction)")
            case .requestComplete(let request, let result):
                if case .modelFile(let url) = result {
                    print("Request result output at \(url).")
                }
            case .requestError(let request, let error):
                print("Error: \(request) error=\(error)")
            case .processingComplete:
                print("Completed!")
                handleComplete()
            default:  // Or handle other messages...
                break
            }
        }
    } catch {
       print("Fatal session error! \(error)")
    }
}
```

### Calling process on two models simultaneously — [13:44]

```swift
try! session.process(requests: [
    .modelFile("/tmp/Outputs/model-reduced.usdz", detail: .reduced),
    .modelFile("/tmp/Outputs/model-medium.usdz", detail: .medium)
])
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10076/9/616F3DCB-8F4E-4C91-924E-6DB20B3D2A27/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10076/9/616F3DCB-8F4E-4C91-924E-6DB20B3D2A27/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10076) — developer.apple.com. Indexed for agent consumption._