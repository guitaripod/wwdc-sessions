---
id: "wwdc2026-282"
event: "wwdc2026"
year: 2026
title: "Discover the Spatial Preview framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/282"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Discover the Spatial Preview framework

**Event:** WWDC26 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-282](https://developer.apple.com/videos/play/wwdc2026/282)

Check out how the new Spatial Preview framework brings content from your Mac directly into visionOS. Discover how to build dynamic workflows with live-syncing and bidirectional editing across both platforms. Learn about the SpatialPreview API, device discovery, 2D and 3D session integration, and new Quick Look capabilities to elevate your Mac apps spatially.

**Keywords:** `3d`, `3d content`, `document preview`, `mac virtual display`, `quick look`, `shareplay`, `spatial computing`, `spatial preview`, `usd`, `usdkit`, `usdz`, `visionos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,409 words)

## Documentation & Resources

- [Reducing the rendering cost of RealityKit content on visionOS](https://developer.apple.com/documentation/visionOS/reducing-the-rendering-cost-of-RealityKit-content-on-visionOS) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/reducing-the-rendering-cost-of-RealityKit-content-on-visionOS
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/reducing-the-rendering-cost-of-RealityKit-content-on-visionOS.json
- [Spatial Preview](https://developer.apple.com/documentation/SpatialPreview) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SpatialPreview
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SpatialPreview.json

## Code Snippets

### Document Preview Session with Device Picker — [3:58]

```swift
// Send and update documents using the Spatial Preview framework

import SwiftUI
import SpatialPreview
let deviceObserver = ConnectedSpatialEndpointObserver()

let previewSession = DocumentPreviewSession(name: "Immersive.aivu", contentType: .aivu)

func startPreview(contentURL: URL, endpoint: SpatialPreviewEndpoint) async throws {
    let endpoint = try await deviceObserver.endpoint
    try await previewSession.start(endpoint: endpoint)
    try await previewSession.updateContents(url: contentURL)
}

@State var showDevicePicker: Bool = false

var body: some View {
    ...
    .sheet(isPresented: $showDevicePicker) {
        SpatialPreviewDevicePicker(isPresented: $showDevicePicker) { endpoint in
            showDevicePicker = false
            Task {
                try await startPreview(filename: filename, endpoint: endpoint)
            }
        }
    }
}
```

### Update Document Contents — [5:20]

```swift
// Send and update documents using the Spatial Preview framework

import SwiftUI
import SpatialPreview

ForEach(contentURLs, id: \.self) { url in
    Button {
        Task { try await previewSession?.updateContents(url: url) }
    }
}
.task(id: previewSession.map { ObjectIdentifier($0) }) {
    for await state in Observations({ session.state }) {
        if state.isInvalidated {
            previewSession = nil
            break
        }
    }
}

try await previewSession?.close()
```

### Edit USD Live — [7:36]

```swift
// Edit USD live using USDKit and Spatial Preview

import SpatialPreview
import USDKit

let deviceObserver = ConnectedSpatialEndpointObserver()

var usdSession: USDPreviewSession?

func shareStage(to endpoint: SpatialPreviewEndpoint) async throws -> USDPreviewSession {
    let endpoint = try await deviceObserver.endpoint

    let stageURL = Bundle.main.url(forResource: "sampleScene", withExtension: "usdz")
    let stage = try USDStage.open(stageURL)
    usdSession = USDPreviewSession(stage: stage)

    try await usdSession?.start(endpoint: endpoint)
}
```

### Opt out of optimization — [8:56]

```swift
// Optimization

import SpatialPreview




let endpoint = try await deviceObserver.endpoint
do {
    try await usdSession.start(endpoint: endpoint, parameters: .unmodified)
} catch USDPreviewSession.Error.assetUnshareable {
    // Handle Asset Unshareable error
}
```

### USD Layout Variants — [10:10]

```swift
// LayoutVariants.usda
#usda 1.0
over "furniture" (
    variantSets = "Layout"
    variants = { string Layout = "LayoutA" }
)
{
    variantSet "Layout" = {
        "LayoutA" {
            // Default furniture position and rotation
        }
        "LayoutB" {
            // Moves furniture prims to a different position and rotation
        }
        ...
    }
}
```

### Edit USD live using USDKit and Spatial Preview — [10:17]

```swift
// Edit USD live using USDKit and Spatial Preview

import SpatialPreview
import USDKit

func applyLayoutVariant(named layoutVariantName: String) throws {
    let prim = stage.prim(at: SdfPath("/root/furniture"))
    try prim.variantSets?.setSelection("Layout", variantName: layoutVariantName)
}
```

### USD Stage Observations — [10:49]

```swift
// Edit USD live using Spatial Preview

import SpatialPreview
import USDKit

let observerToken: ObservationToken

observerToken = stage.addObserver(for: UsdStage.ObjectsDidChange.self) { notice in
    for path in notice.resyncedPaths {
        let prim = notice.stage.prim(at: path)
        guard prim.isValid else { continue }
        if prim.isAnnotation {
            // Handle annotation change
            break
        }
    }
}
```

### Annotation Spec — [11:13]

```swift
// Annotation spec example

AppleTextAnnotation {
    // The textual representation of this annotation
    string text

    // The identifier for this specific author
    uniform string author

    // An identifier that is unique to your data tracking system
    uniform string identifier
}

/__documentAnnotationGroup__
```

### Metadata for Object Manipulation — [11:33]

```swift
// Metadata required for object manipulation in Quick Look

customData = {
    dictionary apple = {
        bool spatialEditable = 1
    }
}
```

### Session Options and Events — [12:16]

```swift
// Spatial Preview session options and events

import SpatialPreview
import USDKit

session.start(endpoint: endpoint, options: [.annotations, .perObjectManipulation, .export])

func listenForEvents(session: USDPreviewSession) async {
    for await event in session.events {
        if case .timeChanged(let time) = event {
            playbackModel.timeCode = time
        } else if case .playbackStateChanged(let isPlaying) = event {
            playbackModel.playbackStateChanged(isPlaying)
        }
    }
}
```

### Observe Session Progress — [12:38]

```swift
// Observe Spatial Preview session progress

import SpatialPreview
import USDKit

@State private var sessionProgress: Double = 0

var body: some View {
    ...
    .task(id: usdSession.map { ObjectIdentifier($0) }) {
        guard let session = usdSession else { return }
        for await fraction in Observations({ session.progress.fractionCompleted }) {
            sessionProgress = fraction
        }
    }
    .overlay(alignment: .bottom) {
        ProgressView(value: sessionProgress)
            .padding()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/282/5/958c34c9-f20e-4c6d-826a-eeed7ce7ba9e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/282/5/958c34c9-f20e-4c6d-826a-eeed7ce7ba9e/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/282) — developer.apple.com. Indexed for agent consumption._