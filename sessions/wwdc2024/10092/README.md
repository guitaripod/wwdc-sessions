---
id: "wwdc2024-10092"
event: "wwdc2024"
year: 2024
title: "Render Metal with passthrough in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10092"
topics: ["Spatial Computing", "Graphics & Games"]
platforms: ["visionOS"]
hasTranscript: true
---

# Render Metal with passthrough in visionOS

**Event:** WWDC24 · **Topic:** Graphics & Games · **Platforms:** visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10092](https://developer.apple.com/videos/play/wwdc2024/10092)

Get ready to extend your Metal experiences for visionOS. Learn best practices for integrating your rendered content with people’s physical environments with passthrough. Find out how to position rendered content to match the physical world, reduce latency with trackable anchor prediction, and more.

**Keywords:** `compositorservices`, `metal`, `mixed immersion`, `mixed reality`, `visionos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,801 words)

## Documentation & Resources

- [Interacting with virtual content blended with passthrough](https://developer.apple.com/documentation/CompositorServices/interacting-with-virtual-content-blended-with-passthrough) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CompositorServices/interacting-with-virtual-content-blended-with-passthrough
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CompositorServices/interacting-with-virtual-content-blended-with-passthrough.json
- [Improving rendering performance with vertex amplification](https://developer.apple.com/documentation/Metal/improving-rendering-performance-with-vertex-amplification) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/improving-rendering-performance-with-vertex-amplification
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/improving-rendering-performance-with-vertex-amplification.json
- [Rendering a scene with deferred lighting in Swift](https://developer.apple.com/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-a-scene-with-deferred-lighting-in-swift.json
- [How to start designing assets in Display P3](https://developer.apple.com/news/?id=5cda5ipr) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/news/?id=5cda5ipr
- [Forum: Graphics & Games](https://developer.apple.com/forums/topics/graphics-and-games?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/graphics-and-games?cid=vf-a-0010
- [Metal Developer Resources](https://developer.apple.com/metal/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/
- [Rendering at different rasterization rates](https://developer.apple.com/documentation/Metal/rendering-at-different-rasterization-rates) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/rendering-at-different-rasterization-rates
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/rendering-at-different-rasterization-rates.json

## Code Snippets

### Add mixed immersion — [3:07]

```swift
@main
struct MyApp: App {
    var body: some Scene {
        ImmersiveSpace {
            CompositorLayer(configuration: MyConfiguration()) { layerRenderer in
                 let engine = my_engine_create(layerRenderer)
                 let renderThread = Thread {
                     my_engine_render_loop(engine)
                 }
                 renderThread.name = "Render Thread"
                 renderThread.start()
            }
            .immersionStyle(selection: $style, in: .mixed, .full)
        }
    }
}
```

### Create a renderPassDescriptor — [4:43]

```swift
let renderPassDescriptor = MTLRenderPassDescriptor()

renderPassDescriptor.colorAttachments[0].texture = drawable.colorTextures[0]
renderPassDescriptor.colorAttachments[0].loadAction = .clear
renderPassDescriptor.colorAttachments[0].storeAction = .store
renderPassDescriptor.colorAttachments[0].clearColor = .init(red: 0.0, green: 0.0, blue: 0.0, alpha: 0.0)            

renderPassDescriptor.depthAttachment.texture = drawable.depthTextures[0]
renderPassDescriptor.depthAttachment.loadAction = .clear
renderPassDescriptor.depthAttachment.storeAction = .store
renderPassDescriptor.depthAttachment.clearDepth = 0.0
```

### Set Upper Limb Visibility — [9:08]

```swift
@main
struct MyApp: App {
    var body: some Scene {
        ImmersiveSpace {
            CompositorLayer(configuration: MyConfiguration()) { layerRenderer in
                 let engine = my_engine_create(layerRenderer)
                 let renderThread = Thread {
                     my_engine_render_loop(engine)
                 }
                 renderThread.name = "Render Thread"
                 renderThread.start()
            }
            .immersionStyle(selection: $style, in: .mixed, .full)
						.upperLimbVisiblity(.automatic)
        }
    }
}
```

### Compose a projection view matrix — [13:37]

```swift
func renderLoop {
    //...

    let deviceAnchor = worldTracking.queryDeviceAnchor(atTimestamp: presentationTime)
    drawable.deviceAnchor = deviceAnchor

    for viewIndex in 0...drawable.views.count {
        let view = drawable.views[viewIndex]
        let originFromDevice = deviceAnchor?.originFromAnchorTransform
        let deviceFromView = view.transform
        let viewMatrix = (originFromDevice * deviceFromView).inverse
        let projection = drawable.computeProjection(normalizedDeviceCoordinatesConvention:
                                                    .rightUpBack,
                                                    viewIndex: viewIndex)

        let projectionViewMatrix = projection * viewMatrix;

        //...
    }
}
```

### Trackable anchor prediction — [18:27]

```swift
func renderFrame() {
//...

// Get the trackable anchor and presentation time.
let presentationTime = drawable.frameTiming.presentationTime
let trackableAnchorTime = drawable.frameTiming.trackableAnchorTime

// Convert the timestamps into units of seconds
let devicePredictionTime = LayerRenderer.Clock.Instant.epoch.duration(to:     presentationTime).timeInterval
let anchorPredictionTime = LayerRenderer.Clock.Instant.epoch.duration(to:     trackableAnchorTime).timeInterval

let deviceAnchor = worldTracking.queryDeviceAnchor(atTimestamp: devicePredictionTime)
let leftAnchor = handTracking.handAnchors(at: anchorPredictionTime)

if (leftAnchor.isTracked) {
    //...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10092/4/B9AC5FF0-C58C-4608-AC8D-7AD3A82ABD42/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10092/4/B9AC5FF0-C58C-4608-AC8D-7AD3A82ABD42/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10092) — developer.apple.com. Indexed for agent consumption._