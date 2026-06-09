---
id: "wwdc2025-294"
event: "wwdc2025"
year: 2025
title: "What’s new in Metal rendering for immersive apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/294"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# What’s new in Metal rendering for immersive apps

**Event:** WWDC25 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-294](https://developer.apple.com/videos/play/wwdc2025/294)

Discover the latest improvements in Metal rendering for immersive apps with Compositor Services. Learn how to add hover effects to highlight your app’s interactive elements, and how to render in higher fidelity with dynamic render quality. Find out about the new progressive immersion style. And explore how you can bring immersive experiences to macOS apps by directly rendering Metal content from Mac to Vision Pro. 

To get the most out of this session, first watch “Discover Metal for immersive apps” from WWDC23.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,412 words)

## Documentation & Resources

- [Analyzing the performance of your Metal app](https://developer.apple.com/documentation/Xcode/Analyzing-the-performance-of-your-Metal-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Analyzing-the-performance-of-your-Metal-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Analyzing-the-performance-of-your-Metal-app.json
- [Rendering hover effects in Metal immersive apps](https://developer.apple.com/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CompositorServices/rendering_hover_effects_in_metal_immersive_apps.json
- [Optimizing GPU performance](https://developer.apple.com/documentation/Xcode/Optimizing-GPU-performance) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Optimizing-GPU-performance
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Optimizing-GPU-performance.json

## Code Snippets

### Scene render loop — [0:01]

```swift
// Scene render loop

extension Renderer {
    func renderFrame(with scene: MyScene) {
        guard let frame = layerRenderer.queryNextFrame() else { return }

        frame.startUpdate()
        scene.performFrameIndependentUpdates()
        frame.endUpdate()

        let drawables = frame.queryDrawables()
        guard !drawables.isEmpty else { return }

        guard let timing = frame.predictTiming() else { return }
        LayerRenderer.Clock().wait(until: timing.optimalInputTime)
        frame.startSubmission()
        scene.render(to: drawable)
        frame.endSubmission()
    }
}
```

### Layer configuration — [5:54]

```swift
// Layer configuration

struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {
        // Configure other aspects of LayerRenderer

        let trackingAreasFormat: MTLPixelFormat = .r8Uint
        if capabilities.supportedTrackingAreasFormats.contains(trackingAreasFormat) {
            configuration.trackingAreasFormat = trackingAreasFormat
        }
    }
}
```

### Object render function — [7:54]

```swift
// Object render function

extension MyObject {
    func render(drawable: Drawable, renderEncoder: MTLRenderCommandEncoder) {
        var renderValue: LayerRenderer.Drawable.TrackingArea.RenderValue? = nil
        if self.isInteractive {
            let trackingArea = drawable.addTrackingArea(identifier: self.identifier)
            if self.usesHoverEffect {
                trackingArea.addHoverEffect(.automatic)
            }
            renderValue = trackingArea.renderValue
        }
		self.draw(with: commandEncoder, trackingAreaRenderValue: renderValue)
    }
}
```

### Metal fragment shader — [8:26]

```cpp
// Metal fragment shader

struct FragmentOut
{
    float4 color [[color(0)]];
    uint16_t trackingAreaRenderValue [[color(1)]];
};

fragment FragmentOut fragmentShader( /* ... */ )
{
    // ...

    return FragmentOut {
        float4(outColor, 1.0),
        uniforms.trackingAreaRenderValue
    };
}
```

### Event processing — [10:09]

```swift
// Event processing

extension Renderer {
    func processEvent(_ event: SpatialEventCollection.Event) {
       let object = scene.objects.first {
           $0.identifier == event.trackingAreaIdentifier
       }
       if let object {
           object.performAction()
       }
   }
}
```

### Quality constants — [13:08]

```swift
// Quality constants

extension MyScene {
    struct Constants {
        static let menuRenderQuality: LayerRenderer.RenderQuality = .init(0.8)
        static let worldRenderQuality: LayerRenderer.RenderQuality = .init(0.6)
        static var maxRenderQuality: LayerRenderer.RenderQuality { menuRenderQuality }
    }
}
```

### Layer configuration — [13:32]

```swift
// Layer configuration

struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {
       // Configure other aspects of LayerRenderer

       if configuration.isFoveationEnabled {
           configuration.maxRenderQuality = MyScene.Constants.maxRenderQuality
       }
}
```

### Set runtime render quality — [13:57]

```swift
// Set runtime render quality

extension MyScene {
    var renderQuality: LayerRenderer.RenderQuality {
        switch type {
        case .world: Constants.worldRenderQuality
        case .menu: Constants.menuRenderQuality
        }
    }
}

extension Renderer {
    func adjustRenderQuality(for scene: MyScene) {
        guard layerRenderer.configuration.isFoveationEnabled else {
            return;
        }
        layerRenderer.renderQuality = scene.renderQuality
    }
}
```

### SwiftUI immersion style — [16:58]

```swift
// SwiftUI immersion style

@main
struct MyApp: App {
    @State var immersionStyle: ImmersionStyle

    var body: some Scene {
        ImmersiveSpace(id: "MyImmersiveSpace") {
            CompositorLayer(configuration: MyConfiguration()) { @MainActor layerRenderer in
                Renderer.startRenderLoop(layerRenderer)
            }
        }
        .immersionStyle(selection: $immersionStyle, in: .progressive, .full)
    }
}
```

### Layer configuration — [17:12]

```swift
// Layer configuration

struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {
        // Configure other aspects of LayerRenderer

        if configuration.layout == .layered {
            let stencilFormat: MTLPixelFormat = .stencil8 
            if capabilities.drawableRenderContextSupportedStencilFormats.contains(
                stencilFormat
            ) {
                configuration.drawableRenderContextStencilFormat = stencilFormat 
            }
            configuration.drawableRenderContextRasterSampleCount = 1
        }
    }
}
```

### Render loop — [17:40]

```swift
// Render loop

struct Renderer {
    let portalStencilValue: UInt8 = 200 // Value not used in other stencil operations

    func renderFrame(with scene: MyScene,
                     drawable: LayerRenderer.Drawable,
                     commandBuffer: MTLCommandBuffer) {
        let drawableRenderContext = drawable.addRenderContext(commandBuffer: commandBuffer)
        let renderEncoder = configureRenderPass(commandBuffer: commandBuffer)
        drawableRenderContext.drawMaskOnStencilAttachment(commandEncoder: renderEncoder,
                                                          value: portalStencilValue)
        renderEncoder.setStencilReferenceValue(UInt32(portalStencilValue))

        scene.render(to: drawable, renderEncoder: renderEncoder)

        drawableRenderContext.endEncoding(commandEncoder: commandEncoder)
        drawable.encodePresent(commandBuffer: commandBuffer)
    }
}
```

### App structure — [20:55]

```swift
// App structure

@main
struct MyImmersiveMacApp: App {
    @State var immersionStyle: ImmersionStyle = .full

    var body: some Scene {
        WindowGroup {
            MyAppContent()
        }

        RemoteImmersiveSpace(id: "MyRemoteImmersiveSpace") {
            MyCompositorContent()
        }
        .immersionStyle(selection: $immersionStyle, in: .full, .progressive)
   }
}
```

### App UI — [21:14]

```swift
// App UI

struct MyAppContent: View {
    @Environment(\.supportsRemoteScenes) private var supportsRemoteScenes
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace
    @State private var spaceState: OpenImmersiveSpaceAction.Result?

    var body: some View {
        if !supportsRemoteScenes {
            Text("Remote SwiftUI scenes are not supported on this Mac.")
        } else if spaceState != nil {
            MySpaceStateView($spaceState)
        } else {
            Button("Open remote immersive space") {
                Task {
                    spaceState = await openImmersiveSpace(id: "MyRemoteImmersiveSpace")
                }
            }
        }
    }
}
```

### Compositor content and ARKit session — [21:35]

```swift
// Compositor content and ARKit session

struct MyCompositorContent: CompositorContent {
    @Environment(\.remoteDeviceIdentifier) private var remoteDeviceIdentifier

    var body: some CompositorContent {
        CompositorLayer(configuration: MyConfiguration()) { @MainActor layerRenderer in
            guard let remoteDeviceIdentifier else { return }
            let arSession = ARKitSession(device: remoteDeviceIdentifier)
            Renderer.startRenderLoop(layerRenderer, arSession)
        }
    }
}
```

### C interoperability — [23:17]

```cpp
// Swift
let remoteDevice: ar_device_t = remoteDeviceIdentifier.cDevice Renderer.start_rendering(layerRenderer, remoteDevice)

// C
void start_rendering(cp_layer_renderer_t layer_renderer, ar_device_t remoteDevice) {     ar_session_t session = ar_session_create_with_device(remoteDevice);     // ... }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/294/4/e0a53a43-a861-4846-9d3a-45232b5e959a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/294/4/e0a53a43-a861-4846-9d3a-45232b5e959a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/294) — developer.apple.com. Indexed for agent consumption._