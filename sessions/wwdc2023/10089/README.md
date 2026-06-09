---
id: "wwdc2023-10089"
event: "wwdc2023"
year: 2023
title: "Discover Metal for immersive apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10089"
topics: ["Spatial Computing", "Graphics & Games"]
platforms: ["visionOS"]
hasTranscript: true
---

# Discover Metal for immersive apps

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** visionOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10089](https://developer.apple.com/videos/play/wwdc2023/10089)

Find out how you can use Metal to render fully immersive experiences for visionOS. We’ll show you how to set up a rendering session on the platform and create a basic render loop, and share how you can make your experience interactive by incorporating spatial input.

**Keywords:** `compositor`, `compositorservices`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,159 words)

## Documentation & Resources

- [Drawing fully immersive content using Metal](https://developer.apple.com/documentation/CompositorServices/drawing-fully-immersive-content-using-metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CompositorServices/drawing-fully-immersive-content-using-metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CompositorServices/drawing-fully-immersive-content-using-metal.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### App architecture — [4:45]

```swift
@main
struct MyApp: App {
    var body: some Scene {
        ImmersiveSpace {
            CompositorLayer { layerRenderer in
                let engine = my_engine_create(layerRenderer)
                let renderThread = Thread {
                    my_engine_render_loop(engine)
                }
                renderThread.name = "Render Thread"
                renderThread.start()
            }
        }
    }
}
```

### CompositorLayer Configuration — [10:32]

```swift
// CompositorLayer configuration

struct MyConfiguration: CompositorLayerConfiguration {
    func makeConfiguration(capabilities: LayerRenderer.Capabilities,
                           configuration: inout LayerRenderer.Configuration) {

        let supportsFoveation = capabilities.supportsFoveation
        let supportedLayouts = capabilities.supportedLayouts(options: supportsFoveation ?
                                                             [.foveationEnabled] : [])

        configuration.layout = supportedLayouts.contains(.layered) ? .layered : .dedicated

        configuration.isFoveationEnabled = supportsFoveation

        // HDR support
        configuration.colorFormat = .rgba16Float
   }
}
```

### Render loop — [12:20]

```objectivec
void my_engine_render_loop(my_engine *engine) {
    my_engine_setup_render_pipeline(engine);

    bool is_rendering = true;
    while (is_rendering) @autoreleasepool {
        switch (cp_layer_renderer_get_state(engine->layer_renderer)) {
            case cp_layer_renderer_state_paused:
                cp_layer_renderer_wait_until_running(engine->layer_renderer);
                break;
            case cp_layer_renderer_state_running:
                my_engine_render_new_frame(engine);
                break;
            case cp_layer_renderer_state_invalidated:
                is_rendering = false;
                break;
        }
    }

    my_engine_invalidate(engine);
}
```

### Render new frame — [15:56]

```objectivec
void my_engine_render_new_frame(my_engine *engine) {

    cp_frame_t frame = cp_layer_renderer_query_next_frame(engine->layer_renderer);
    if (frame == nullptr) { return; }

    cp_frame_timing_t timing = cp_frame_predict_timing(frame);
    if (timing == nullptr) { return; }

    cp_frame_start_update(frame);

    my_input_state input_state = my_engine_gather_inputs(engine, timing);
    my_engine_update_frame(engine, timing, input_state);

    cp_frame_end_update(frame);

    // Wait until the optimal time for querying the input
    cp_time_wait_until(cp_frame_timing_get_optimal_input_time(timing));

    cp_frame_start_submission(frame);

    cp_drawable_t drawable = cp_frame_query_drawable(frame);
    if (drawable == nullptr) { return; }

    cp_frame_timing_t final_timing = cp_drawable_get_frame_timing(drawable);
    ar_pose_t pose = my_engine_get_ar_pose(engine, final_timing);
    cp_drawable_set_ar_pose(drawable, pose);

    my_engine_draw_and_submit_frame(engine, frame, drawable);

    cp_frame_end_submission(frame);
}
```

### App architecture + input support — [18:57]

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
                layerRenderer.onSpatialEvent = { eventCollection in
                    var events = eventCollection.map { my_spatial_event($0) }
                    my_engine_push_spatial_events(engine, &events, events.count)
                }
            }
        }
        .upperLimbVisibility(.hidden)
    }
}
```

### Push spatial events — [18:57]

```objectivec
void my_engine_push_spatial_events(my_engine *engine,
                                   my_spatial_event *spatial_event_collection,
                                   size_t event_count) {
    os_unfair_lock_lock(&engine->input_event_lock);

    // Copy events into an internal queue

    os_unfair_lock_unlock(&engine->input_event_lock);
}
```

### Gather inputs — [19:57]

```objectivec
my_input_state my_engine_gather_inputs(my_engine *engine,
                                       cp_frame_timing_t timing) {
    my_input_state input_state = my_input_state_create();

    os_unfair_lock_lock(&engine->input_event_lock);
    input_state.current_pinch_collection = my_engine_pop_spatial_events(engine);
    os_unfair_lock_unlock(&engine->input_event_lock);

    ar_hand_tracking_provider_get_latest_anchors(engine->hand_tracking_provider,
                                                 input_state.left_hand,
                                                 input_state.right_hand);

    return input_state;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10089/5/49D0E645-DBE8-4D7A-9637-C4D744C86894/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10089/5/49D0E645-DBE8-4D7A-9637-C4D744C86894/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10089) — developer.apple.com. Indexed for agent consumption._