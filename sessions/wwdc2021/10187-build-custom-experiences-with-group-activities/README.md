---
id: "wwdc2021-10187"
event: "wwdc2021"
year: 2021
title: "Build custom experiences with Group Activities"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10187"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Build custom experiences with Group Activities

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10187](https://developer.apple.com/videos/play/wwdc2021/10187)

Go beyond basic streaming and interaction and discover how you can build advanced SharePlay experiences using the full power of the Group Activities framework. We’ll show you how to adapt a simple drawing app into a real-time shared canvas, explore APIs like GroupSessionMessenger — which helps send and receive custom messages between participants in the group — and learn how to put the finishing touches on a custom SharePlay experience.

**Keywords:** `draw`, `draw together`, `facetime`, `face time`, `groupactivities`, `group activities`, `groupsession`, `shareplay`, `share play`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,801 words)

## Documentation & Resources

- [Drawing content in a group session](https://developer.apple.com/documentation/groupactivities/drawing_content_in_a_group_session) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/groupactivities/drawing_content_in_a_group_session
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/groupactivities/drawing_content_in_a_group_session.json
- [Supporting coordinated media playback](https://developer.apple.com/documentation/AVFoundation/supporting-coordinated-media-playback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-coordinated-media-playback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-coordinated-media-playback.json
- [Group Activities](https://developer.apple.com/documentation/GroupActivities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities.json

## Code Snippets

### Configuring your application’s activity — [3:50]

```swift
struct DrawTogether: GroupActivity {

    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.title = NSLocalizedString("Draw Together",
                                           comment: "Title of group activity")
        metadata.type = .generic
        return metadata
    }

}
```

### Define, Receive and Send messages — [10:06]

```swift
let messenger = GroupSessionMessenger(session: groupSession)

// 1. Define
struct UpsertStrokeMessage: Codable {
    let id: UUID
    let color: Color
    let point: CGPoint
}

// 2. Receive
for await (message, context) in messenger.messages(of: UpsertStrokeMessage.self) {
    // Handle message
}

// 3. Send
do {
    try await messenger.send(UpsertStrokeMessage(id: stroke.id, color: .red, point: point))
} catch {
    // Handle error
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10187/3/53AD885C-179C-4013-A2D3-D985CE932C87/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10187/3/53AD885C-179C-4013-A2D3-D985CE932C87/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10187) — developer.apple.com. Indexed for agent consumption._
