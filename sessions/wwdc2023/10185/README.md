---
id: "wwdc2023-10185"
event: "wwdc2023"
year: 2023
title: "Update Live Activities with push notifications"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10185"
topics: ["App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Update Live Activities with push notifications

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10185](https://developer.apple.com/videos/play/wwdc2023/10185)

Discover how you can remotely update Live Activities in your app when you push content through Apple Push Notification service (APNs). We’ll show you how to configure your first Live Activity push locally so you can quickly iterate on your implementation. Learn best practices for determining your push priority and configuring alerting updates, and explore how to further improve your Live Activities with relevance score and stale date.

To get the most out of this session, you should be familiar with ActivityKit and Live Activities. Check out “Meet ActivityKit” for an introduction to Live Activities.

**Keywords:** `activities`, `activity`, `activitykit`, `dynamic`, `dynamic island`, `island`, `live`, `live activities`, `live notification`, `live notifications`, `lock`, `lock screen`, `notification`, `notifications`, `screen`, `standby`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,876 words)

## Documentation & Resources

- [Sending push notifications using command-line tools](https://developer.apple.com/documentation/UserNotifications/sending-push-notifications-using-command-line-tools) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-push-notifications-using-command-line-tools
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-push-notifications-using-command-line-tools.json
- [Establishing a token-based connection to APNs](https://developer.apple.com/documentation/UserNotifications/establishing-a-token-based-connection-to-apns) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/establishing-a-token-based-connection-to-apns
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/establishing-a-token-based-connection-to-apns.json
- [Human Interface Guidelines: Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/live-activities
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json
- [ActivityKit](https://developer.apple.com/documentation/ActivityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit.json
- [Sending notification requests to APNs](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-notification-requests-to-apns
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-notification-requests-to-apns.json

## Code Snippets

### Enabling push updates — [3:53]

```swift
func startActivity(hero: EmojiRanger) throws {
    let adventure = AdventureAttributes(hero: hero)
    let initialState = AdventureAttributes.ContentState(
        currentHealthLevel: hero.healthLevel,
        eventDescription: "Adventure has begun!"
    )

    let activity = try Activity.request(
        attributes: adventure,
        content: .init(state: initialState, staleDate: nil),
        pushType: .token
    )

    Task {
        for await pushToken in activity.pushTokenUpdates {
            let pushTokenString = pushToken.reduce("") { $0 + String(format: "%02x", $1) }

            Logger().log("New push token: \(pushTokenString)")

            try await self.sendPushToken(hero: hero, pushTokenString: pushTokenString)
        }
    }
}
```

### APNs push payload: Updating — [6:54]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "content-state": {
            "currentHealthLevel": 0.941,
            "eventDescription": "Power Panda found a sword!"
        }
    }
}
```

### Printing content state JSON — [7:37]

```swift
let contentState = AdventureAttributes.ContentState(
    currentHealthLevel: 0.941,
    eventDescription: "Power Panda found a sword!"
)

let encoder = JSONEncoder()
encoder.outputFormatting = .prettyPrinted

let json = try! encoder.encode(contentState)
Logger().log("\(String(data: json, encoding: .utf8)!)")
```

### Terminal: Constructing an APNs request with curl — [9:18]

```bash
curl \
--header "apns-topic: com.example.apple-samplecode.Emoji-Rangers.push-type.liveactivity" \
--header "apns-push-type: liveactivity" \
--header "apns-priority: 10" \
--header "authorization: bearer $AUTHENTICATION_TOKEN" \
--data '{
    "aps": {
        "timestamp": '$(date +%s)',
        "event": "update",
        "content-state": {
            "currentHealthLevel": 0.941,
            "eventDescription": "Power Panda found a sword!"
        }
    }
}' \
--http2 https://api.sandbox.push.apple.com/3/device/$ACTIVITY_PUSH_TOKEN
```

### APNs push payload: Alerting — [14:21]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "content-state": {
            "currentHealthLevel": 0.0,
            "eventDescription": "Power Panda has been knocked down!"
        },
        "alert": {
            "title": "Power Panda is knocked down!",
            "body": "Use a potion to heal Power Panda!",
            "sound": "default"
        }
    }
}
```

### APNs push payload: Alert localization — [14:56]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "content-state": {
            "currentHealthLevel": 0.0,
            "eventDescription": "Power Panda has been knocked down!"
        },
        "alert": {
            "title": {
                "loc-key": "%@ is knocked down!",
                "loc-args": ["Power Panda"]
            },
            "body": {
                "loc-key": "Use a potion to heal %@!",
                "loc-args": ["Power Panda"]
            },
            "sound": "HeroDown.mp4"
        }
    }
}
```

### APNs push payload: Alert sound — [15:25]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "content-state": {
            "currentHealthLevel": 0.0,
            "eventDescription": "Power Panda has been knocked down!"
        },
        "alert": {
            "title": {
                "loc-key": "%@ is knocked down!",
                "loc-args": ["Power Panda"]
            },
            "body": {
                "loc-key": "Use a potion to heal %@!",
                "loc-args": ["Power Panda"]
            },
            "sound": "HeroDown.mp4"
        }
    }
}
```

### APNs push payload: Dismissal — [15:52]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "end",
        "dismissal-date": 1685959200,
        "content-state": {
            "currentHealthLevel": 0.23,
            "eventDescription": "Adventure over! Power Panda is taking a nap."
        }
    }
}
```

### APNs push payload: Stale date — [16:44]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "stale-date": 1685959200,
        "content-state": {
            "currentHealthLevel": 0.79,
            "eventDescription": "Egghead is in the woods and lost connection."
        }
    }
}
```

### Displaying a stale Live Activity UI — [16:54]

```swift
struct AdventureActivityConfiguration: Widget {

    var body: some WidgetConfiguration {

        ActivityConfiguration(for: AdventureAttributes.self) { context in
            AdventureLiveActivityView(
                hero: context.attributes.hero,
                isStale: context.isStale,
                contentState: context.state
            )
            .activityBackgroundTint(Color.gameWidgetBackground)
        }  dynamicIsland: { context in
            // ...
        }

    }

}
```

### APNs push payload: Relevance score — [17:19]

```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "relevance-score": 100,
        "content-state": {
            "currentHealthLevel": 0.941,
            "eventDescription": "Power Panda found a sword!"
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10185/4/1867F512-50A9-4907-A90A-34A7E198BDB7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10185/4/1867F512-50A9-4907-A90A-34A7E198BDB7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10185) — developer.apple.com. Indexed for agent consumption._