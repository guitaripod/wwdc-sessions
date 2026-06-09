---
id: "wwdc2024-10115"
event: "wwdc2024"
year: 2024
title: "Enhance the immersion of media viewing in custom environments"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10115"
topics: ["Spatial Computing", "Audio & Video"]
platforms: ["visionOS"]
hasTranscript: true
---

# Enhance the immersion of media viewing in custom environments

**Event:** WWDC24 · **Topic:** Audio & Video · **Platforms:** visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10115](https://developer.apple.com/videos/play/wwdc2024/10115)

Extend your media viewing experience using Reality Composer Pro components like Docking Region, Reverb, and Virtual Environment Probe. Find out how to further enhance immersion using Reflections, Tint Surroundings Effect, SharePlay, and the Immersive Environment Picker.

**Keywords:** `brightness`, `custom environments`, `diffuse`, `docking region component`, `group session`, `immersive environment picker`, `light spill`, `media playback`, `reality composer pro`, `realitykit`, `reflections`, `reverb`, `shareplay`, `specular`, `tint`, `virtual environment probe`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,773 words)

## Documentation & Resources

- [Enabling video reflections in an immersive environment](https://developer.apple.com/documentation/visionOS/enabling-video-reflections-in-an-immersive-environment) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/enabling-video-reflections-in-an-immersive-environment
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/enabling-video-reflections-in-an-immersive-environment.json
- [Building an immersive media viewing experience](https://developer.apple.com/documentation/visionOS/building-an-immersive-media-viewing-experience) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/building-an-immersive-media-viewing-experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/building-an-immersive-media-viewing-experience.json
- [Forum: Media Technologies](https://developer.apple.com/forums/topics/media-technologies?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/media-technologies?cid=vf-a-0010
- [Destination Video](https://developer.apple.com/documentation/visionOS/destination-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/destination-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/destination-video.json

## Code Snippets

### Add environments to the Immersive Environment Picker — [15:14]

```swift
WindowGroup {
    ContentView()
        .immersiveEnvironmentPicker {
            ForEach(viewModel.environmentItems) { item in
                Button(item.title, image: item.thumbnail) {
                    Task { 
                        await openImmersiveSpace(id: item.id)
                    }
                }
            }
        }
}
```

### Synchronization of an environment state using SharePlay — [15:47]

```swift
import AVKit
import GroupActivities

   for await session in MyActivity.sessions() {

        // join the session, activate the activity, etc.

        playerViewController
            .player?
            .playbackCoordinator
            .coordinateWithSession(session)

        playerViewController
            .groupExperienceCoordinator
            .coordinateWithSession(session)
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10115/4/6A9F8C82-702C-4646-8039-A898373DFDAD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10115/4/6A9F8C82-702C-4646-8039-A898373DFDAD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10115) — developer.apple.com. Indexed for agent consumption._