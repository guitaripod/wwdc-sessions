---
id: "wwdc2024-10069"
event: "wwdc2024"
year: 2024
title: "Broadcast updates to your Live Activities"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10069"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "watchOS"]
hasTranscript: true
---

# Broadcast updates to your Live Activities

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS, iPadOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10069](https://developer.apple.com/videos/play/wwdc2024/10069)

With broadcast push notifications, your app can send updates to thousands of Live Activities with a single request. We’ll discover how broadcast push notifications work between an app, a server, and the Apple Push Notification service, then we’ll walk through best practices for this capability and how to implement it.

**Keywords:** `apns`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,733 words)

## Documentation & Resources

- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010
- [Sending broadcast push notification requests to APNs](https://developer.apple.com/documentation/UserNotifications/sending-broadcast-push-notification-requests-to-apns) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-broadcast-push-notification-requests-to-apns
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-broadcast-push-notification-requests-to-apns.json
- [Sending channel management requests to APNs](https://developer.apple.com/documentation/UserNotifications/sending-channel-management-requests-to-apns) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-channel-management-requests-to-apns
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-channel-management-requests-to-apns.json
- [Setting up broadcast push notifications](https://developer.apple.com/documentation/UserNotifications/setting-up-broadcast-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/setting-up-broadcast-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/setting-up-broadcast-push-notifications.json
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json

## Code Snippets

### Subscribe a Live Activity to broadcast push notification updates — [7:50]

```swift
// Request a Live Activity and subscribe to broadcast push notifications

import ActivityKit

func startLiveActivity(channelId: String) {
    let gameAttributes = GameAttributes()
    let initialState = GameAttributes.ContentState(
            home: 0, away: 0, update: "First Half"
    )
    try Activity.request(
            attributes: gameAttributes,
            content: .init(state: initialState, staleDate: nil),
            pushType: .channel(channelId)
    )
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10069/4/4BD768EC-9A6C-492A-ADB0-C17EF9F7110C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10069/4/4BD768EC-9A6C-492A-ADB0-C17EF9F7110C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10069) — developer.apple.com. Indexed for agent consumption._
