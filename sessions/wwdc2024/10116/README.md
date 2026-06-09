---
id: "wwdc2024-10116"
event: "wwdc2024"
year: 2024
title: "Explore multiview video playback in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10116"
topics: ["Design", "Spatial Computing", "Audio & Video"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore multiview video playback in visionOS

**Event:** WWDC24 · **Topic:** Audio & Video · **Platforms:** visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10116](https://developer.apple.com/videos/play/wwdc2024/10116)

Learn how AVExperienceController can enable playback of multiple videos on Apple Vision Pro. Review best practices for adoption and explore great use cases, like viewing a sports broadcast from different angles or watching multiple games simultaneously. And discover how to design a compelling and intuitive multiview experience in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,826 words)

## Documentation & Resources

- [Forum: Media Technologies](https://developer.apple.com/forums/topics/media-technologies?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/media-technologies?cid=vf-a-0010

## Code Snippets

### Supply a custom browser view controller — [7:47]

```swift
import AVKit

AVMultiViewManager
	.default
	.contentSelectionViewController = multiViewController()
```

### Add content to multiview — [8:09]

```swift
import AVKit

let controller = AVPlayerViewController()

let experienceController = controller.experienceController
experienceController.allowedExperiences = .recommended(including: [.multiView])

await experienceController.transition(to: .multiView)
```

### Remove content from multiview — [8:47]

```swift
import AVKit

let experienceController = …

await experienceController.transition(to: .embedded)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10116/4/E50DFC91-1CB7-4E9B-B204-72EA322434D8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10116/4/E50DFC91-1CB7-4E9B-B204-72EA322434D8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10116) — developer.apple.com. Indexed for agent consumption._