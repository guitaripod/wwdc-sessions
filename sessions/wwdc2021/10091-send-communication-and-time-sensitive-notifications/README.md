---
id: "wwdc2021-10091"
event: "wwdc2021"
year: 2021
title: "Send communication and Time Sensitive notifications"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10091"
topics: ["App Services", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Send communication and Time Sensitive notifications

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10091](https://developer.apple.com/videos/play/wwdc2021/10091)

Learn more about the evolution of notifications on Apple platforms. We’ll explore how you can help people manage notifications within your app, including how you can craft meaningful moments with interruption levels and Time Sensitive notifications. And we’ll introduce you to communication notifications, providing a richer experience for calls and messages in your app through SiriKit. To get the most out of this session, we recommend having experience creating local and remote notifications, as well as some familiarity with SiriKit intents.

**Keywords:** `apns`, `focus`, `intents`, `interruption`, `notification service extension`, `passive`, `push`, `pushkit`, `siri`, `sirikit`, `status`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,369 words)

## Documentation & Resources

- [INStartCallIntent](https://developer.apple.com/documentation/Intents/INStartCallIntent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Intents/INStartCallIntent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Intents/INStartCallIntent.json
- [INSendMessageIntent](https://developer.apple.com/documentation/Intents/INSendMessageIntent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Intents/INSendMessageIntent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Intents/INSendMessageIntent.json
- [User Notifications](https://developer.apple.com/documentation/UserNotifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications.json
- [SiriKit](https://developer.apple.com/documentation/SiriKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit.json

## Code Snippets

### Notification Action Icons — [1:57]

```swift
// Setting up notification actions with icons

let likeActionIcon = UNNotificationActionIcon(systemImageName: "hand.thumbsup")
let likeAction = UNNotificationAction(identifier: "like-action",
                                           title: "Like",
                                         options: [],
                                            icon: likeActionIcon)

let commentActionIcon = UNNotificationActionIcon(templateImageName: "text.bubble")
let commentAction = UNTextInputNotificationAction(identifier: "comment-action",
                                                       title: "Comment",
                                                     options: [],
                                                        icon: commentActionIcon,
                                        textInputButtonTitle: "Post",
                                        textInputPlaceholder: "Type here…")

let category = UNNotificationCategory(identifier: "update-actions",
                                         actions: [likeAction, commentAction],
                               intentIdentifiers: [], options: [])
```

### Notification Interruption Levels — [8:19]

```swift
// Interruption levels

let enum UNNotificationInterruptionLevel : Int {
    case passive = 0
    case active = 1
    case timeSensitive = 2
    case critical = 3
    public static var `default`: UNNotificationInterruptionLevel { get }
}
```

### Passive Notification: Local — [8:31]

```swift
// Interruption levels
// Local notification

import UserNotifications

let content = UNMutableNotificationContent()
content.title = "Passive"
content.body = "I’m a passive notification, so I won’t interrupt you."
content.interruptionLevel = .passive

let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5, repeats: false)

let request = UNNotificationRequest(identifier: "passive-request-example",
                                       content: content,
                                       trigger: trigger)
```

### Passive Notification: Push — [8:47]

```json
// Interruption levels
// Push notification

{
    "aps" : {
        "alert" : {
            "title" : "Passive",
            "body" : "I’m a passive notification, so I won’t interrupt you."
        }
        "interruption-level" : "passive"
    }
}
```

### Time Sensitive Notification: Local — [11:13]

```swift
// Time Sensitive
// Local notification

let content = UNMutableNotificationContent()
content.title = "Urgent"
content.body = "Your account requires attention."
content.interruptionLevel = .timeSensitive

let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 0, repeats: false)

let request = UNNotificationRequest(identifier: "time-sensitive—example",
                                       content: content,
                                       trigger: trigger)
```

### Time Sensitive Notification: Push — [11:20]

```json
// Time Sensitive
// Push notification

{
    "aps" : {
        "alert" : {
            "title" : "Urgent",
            "body" : "Your account requires attention."
        }
        "interruption-level" : "time-sensitive"
    }
}
```

### Notification Content Providing — [15:20]

```swift
// New UserNotifications API

@available(macOS 12.0, *)
public protocol UNNotificationContentProviding : NSObjectProtocol {}

open class UNNotificationContent : NSObject, NSCopying, NSMutableCopying, NSSecureCoding {
    // ...

    @available(macOS 12.0, *)
    open func updating(from provider: UNNotificationContentProviding) throws 
                                                    -> UNNotificationContent

    // ...
}
```

### Communication Notification: Incoming message — [16:08]

```swift
// Create a messaging notification
// In UNNotificationServiceExtension subclass

func didReceive(_ request: UNNotificationRequest,
                withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
    let incomingMessageIntent: INSendMessageIntent = // ...
    let interaction = INInteraction(intent: incomingMessageIntent, response: nil)
    interaction.direction = .incoming
    interaction.donate(completion: nil)
    do {
        let messageContent = try request.content.updating(from: incomingMessageIntent)
        contentHandler(messageContent)
    } catch {
       // Handle error
    }
}
```

### Communication Notification: Incoming call — [16:20]

```swift
// Create a call notification
// In UNNotificationServiceExtension subclass

func didReceive(_ request: UNNotificationRequest,
                withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
    let incomingCallIntent: INStartCallIntent = // ...
    let interaction = INInteraction(intent: incomingCallIntent, response: nil)
    interaction.direction = .incoming
    interaction.donate(completion: nil)
    do {
        let callContent = try request.content.updating(from: incomingCallIntent)
        contentHandler(callContent)
    } catch {
       // Handle error
    }
}
```

### Communication Notification: Outgoing message — [17:48]

```swift
func sendMessage(...) {
    // ...

    let intent: INSendMessageIntent = // ...
    let interaction = INInteraction(intent: intent, response: nil)

    interaction.direction = .outgoing
    interaction.donate(completion: nil)
}
```

### Communication Notification: INPerson — [18:29]

```swift
// Create INPerson

let person = INPerson(personHandle: handle,
                    nameComponents: nameComponents,
                       displayName: displayName,
                             image: image,
                 contactIdentifier: contactIdentifier,
                  customIdentifier: customIdentifier,
                           aliases: nil,
                    suggestionType: suggestionType)
```

### Communication Notification: INSendMessageIntent — [18:43]

```swift
// Create INSendMessageIntent
// In your notification service extension

let intent = INSendMessageIntent(recipients: [person2],
                        outgoingMessageType: .outgoingMessageText,
                                    content: content,
                         speakableGroupName: speakableGroupName,
                     conversationIdentifier: conversationIdentifier,
                                serviceName: serviceName,
                                     sender: person1,
                                attachments: nil)

let interaction = INInteraction(intent: intent, response: nil)
interaction.direction = .incoming
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10091/4/A4152468-BE8D-45E4-BB60-043AC7854981/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10091/4/A4152468-BE8D-45E4-BB60-043AC7854981/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10091) — developer.apple.com. Indexed for agent consumption._
