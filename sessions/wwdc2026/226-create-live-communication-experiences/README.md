---
id: "wwdc2026-226"
event: "wwdc2026"
year: 2026
title: "Create live communication experiences"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/226"
topics: ["System Services", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Create live communication experiences

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-226](https://developer.apple.com/videos/play/wwdc2026/226)

LiveCommunicationKit transforms your real-time communication apps into integrated experiences. We’ll show you how to deliver a rich, native conversation UI that puts your app right where people need it: from a full-screen presentation on the Lock Screen to seamless multitasking with the Dynamic Island. Join us as we step through integrating the framework for incoming, outgoing, and group conversations.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,881 words)

## Documentation & Resources

- [Initiating VoIP conversations with LiveCommunicationKit](https://developer.apple.com/documentation/LiveCommunicationKit/initiating-voip-conversations-with-livecommunicationkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/LiveCommunicationKit/initiating-voip-conversations-with-livecommunicationkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/LiveCommunicationKit/initiating-voip-conversations-with-livecommunicationkit.json
- [Responding to VoIP Notifications from PushKit](https://developer.apple.com/documentation/PushKit/responding-to-voip-notifications-from-pushkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PushKit/responding-to-voip-notifications-from-pushkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PushKit/responding-to-voip-notifications-from-pushkit.json
- [LiveCommunicationKit](https://developer.apple.com/documentation/LiveCommunicationKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/LiveCommunicationKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/LiveCommunicationKit.json

## Code Snippets

### Set up a conversation manager — [6:41]

```swift
// Set up a conversation manager

import LiveCommunicationKit

let configuration = ConversationManager.Configuration(
  ringtoneName: "SampleRingtone.caf",
  iconTemplateImageData: UIImage(named: "SampleIcon")?.pngData(),
  maximumConversationGroups: 1,
  maximumConversationsPerConversationGroup: 2,
  includesConversationInRecents: true,
  supportsVideo: true,
  supportedHandleTypes: [.phoneNumber, .emailAddress]
)

let manager = ConversationManager(configuration: configuration)
manager.delegate = self
```

### Report the incoming conversation to the system — [9:22]

```swift
// Report the incoming conversation to the system

import LiveCommunicationKit
import PushKit

final class SamplePushHandler: NSObject, PKPushRegistryDelegate {
  func pushRegistry(
    _ registry: PKPushRegistry,
    didReceiveIncomingVoIPPushWith payload: PKPushPayload,
    metadata: PKVoIPPushMetadata) async {

    guard let (handle, uuid) = parseConversationPayload(from: payload) else { return }

    let capabilities = [.video, .pausing, .merging]
    let update = Conversation.Update(members: [handle], capabilities: capabilities)
    try? await manager.reportNewIncomingConversation(uuid: uuid, update: update)
  }
}
```

### Implement the delegate — [9:57]

```swift
// Implement the delegate

import LiveCommunicationKit

final class SampleDelegate: ConversationManagerDelegate {
  func conversationManager(
    _ manager: ConversationManager,
    perform action: ConversationAction
  ) {
    switch action {
    case let action as JoinConversationAction:
      handleJoinAction(action)
    default:
      action.fail()
    }
  }
}
```

### Fulfill the join action — [10:13]

```swift
// Handle a failed connection

extension SampleDelegate {
 func handleJoinAction(_ action: JoinConversationAction) {
    guard let conversation = manager.conversations.first(where: {$0.uuid == uuid })else {
      return action.fail()
    }

    manager.reportConversationEvent(.conversationStartedConnecting(.now), for: conversation)

    Task {
      do {
        try await setupMediaStream(with: action.conversationUUID)
        manager.reportConversationEvent(.conversationConnected(.now), for: conversation)
        action.fulfill(dateConnected: .now)
      } catch {
        action.fail()
      }
    }
  }
}
```

### Route end actions — [11:17]

```swift
// Route end actions

final class SampleDelegate: ConversationManagerDelegate {
  // …
  func conversationManager(
    _ manager: ConversationManager,
    perform action: ConversationAction
  ) {
    switch action {
    case let action as JoinConversationAction:
      handleJoinAction(action)
    case let action as EndConversationAction:
      handleEndAction(action)
    default:
      action.fail()
    }
  }
}
```

### Create a start action — [12:14]

```swift
let startAction = StartConversationAction(
  conversationUUID: UUID(),
  handles: [Handle(type: .phoneNumber, value: "+1-650-555-0199", displayName: "Ryan Notch")],
  isVideo: false
)
```

### Perform the action — [12:23]

```swift
try await manager.perform([startAction])
```

### Route start actions — [12:29]

```swift
// Route start actions

final class SampleDelegate: ConversationManagerDelegate {
  // …
  func conversationManager(
    _ manager: ConversationManager,
    perform action: ConversationAction
  ) {
    switch action {
    case let action as JoinConversationAction:
      handleJoinAction(action)
    case let action as EndConversationAction:
      handleEndAction(action)
    case let action as StartConversationAction:
      handleStartAction(action)
    default:
      action.fail()
    }
  }
}
```

### Start group conversations — [13:51]

```swift
// Start group conversations

let adam = Handle(type: .emailAddress,
                  value: "adam.halwani@icloud.com",
                  displayName: "Adam Halwani")
let david = Handle(type: .emailAddress,
                   value: "david@example.com",
                   displayName: "David Evans")
let ryan = Handle(type: .phoneNumber,
                  value: "+16505550199",
                  displayName: "Ryan Notch")

let startAction = StartConversationAction(
  conversationUUID: UUID(),
  handles: [david, ryan],
  isVideo: false
)
try await manager.perform([startAction])
```

### Report group membership updates — [14:01]

```swift
// Report group membership updates

let update = Conversation.Update(
  localMember: adam,
  members: [david, ryan],
  activeRemoteMembers: [david, ryan],
  capabilities: [.merging, .pausing, .unmerging]
)

manager.reportConversationEvent(
  .conversationUpdated(update),
  for: conversation
)
```

### Route merge actions — [15:26]

```swift
// Route merge actions

final class SampleDelegate: ConversationManagerDelegate {
  func conversationManager(
    _ manager: ConversationManager,
    perform action: ConversationAction
  ) {
    switch action {
    case let action as JoinConversationAction:
      handleJoinAction(action)
    case let action as EndConversationAction:
      handleEndAction(action)
    case let action as StartConversationAction:
        handleStartAction(action)
    case let action as MergeConversationAction:
      handleMergeAction(action)
    default:
      action.fail()
    }
  }
}
```

### Handle the merge action — [15:33]

```swift
// Handle the merge action

extension SampleDelegate {
  func handleMergeAction(_ action: MergeConversationAction) {
    let sourceUUID = action.conversationUUID
    let targetUUID = action.conversationUUIDToMergeWith
    guard manager.conversations.contains(where: { $0.uuid == sourceUUID }),
          manager.conversations.contains(where: { $0.uuid == targetUUID }) else {
      return action.fail()
    }

    Task {
      do {
        let update = try await combineStreams(from: sourceUUID, into: targetUUID)
        manager.reportConversationEvent(.conversationUpdated(update), for: target)
        action.fulfill()
      } catch {
        action.fail()
      }
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/226/4/f8343d5b-0c78-4396-be05-956666fb4ae0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/226/4/f8343d5b-0c78-4396-be05-956666fb4ae0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/226) — developer.apple.com. Indexed for agent consumption._
