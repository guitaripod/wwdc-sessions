---
id: "wwdc2021-10225"
event: "wwdc2021"
year: 2021
title: "Coordinate media experiences with Group Activities"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10225"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Coordinate media experiences with Group Activities

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10225](https://developer.apple.com/videos/play/wwdc2021/10225)

Discover how you can help people watch or listen to content all in sync with SharePlay and the Group Activities framework. We’ll show you how to adapt a media app into a synchronized, SharePlay-enabled experience for multiple people. Learn how to add Group Activities to your app, explore the Picture in Picture layout, and find out how the playback coordinator object can help you fine-tune playback across multiple devices.

**Keywords:** `facetime`, `face time`, `groupactivities`, `group activities`, `groupsession`, `shareplay`, `share play`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,869 words)

## Documentation & Resources

- [Supporting coordinated media playback](https://developer.apple.com/documentation/AVFoundation/supporting-coordinated-media-playback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-coordinated-media-playback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-coordinated-media-playback.json
- [Group Activities](https://developer.apple.com/documentation/GroupActivities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities.json

## Code Snippets

### Define a GroupActivity — [3:06]

```swift
protocol GroupActivity: Codable {

    /// An identifier so the system knows how to reference this activity
    static var activityIdentifier: String { get }

    /// Information that the system uses to show this activity, such as title and a preview image
    var metadata: GroupActivityMetadata { get async }
}
```

### Making your play buttons automatically start a group session when appropriate — [4:42]

```swift
func playButtonTapped() {
    let activity = MovieWatchingActivity(movie: movie)

    Task {
        switch await activity.prepareForActivation() {
        case .activationDisabled:
            // Playback coordination isn't active. Queue movie
            // for local playback.
            self.enqueuedMovie = movie
        case .activationPreferred:
            // Activate the activity. The system enqueues the movie
            // when the activity starts.
            activity.activate()
        case .cancelled:
            // The user cancelled the operation. Nothing to perform.
            break
        default:
            break
        }
    }
}
```

### Receiving a GroupSession from the GroupSession AsyncSequence — [8:31]

```swift
// Receiving a GroupSession from the GroupSession AsyncSequence

func listenForGroupSession() {
    Task {
        for await session in MovieWatchingActivity.sessions() {
            ...
        }
    }
}
```

### Attaching an AVPlayer to the GroupSession — [9:03]

```swift
let player = AVPlayer()

...

func listenForGroupSession() {
    Task {
        for await groupSession in MovieWatchingActivity.sessions() {

            // Verify content is available, prepare for playback to begin

            player.playbackCoordinator.coordinateWithSession(groupSession)

            ...
        }
    }
}
```

### Custom suspensions — [31:26]

```swift
class AVPlaybackCoordinator {
    func beginSuspension(for reason: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension
}

class AVCoordinatedPlaybackSuspension { 	
    func end()
    func end(proposingNewTime newTime: CMTime)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10225/4/2C87FE7A-A19B-4138-92A4-29065B15DFB7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10225/4/2C87FE7A-A19B-4138-92A4-29065B15DFB7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10225) — developer.apple.com. Indexed for agent consumption._
