---
id: "wwdc2022-10117"
event: "wwdc2022"
year: 2022
title: "Enhance voice communication with Push to Talk"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10117"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance voice communication with Push to Talk

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10117](https://developer.apple.com/videos/play/wwdc2022/10117)

We’re coming in loud and clear to help you bring walkie-talkie communication to your app — over! Discover how you can add prominent system UI to your Push to Talk app, enabling rapid communication with the tap of a button. We’ll introduce you to the PushToTalk framework and show you how to configure your apps to transmit and receive audio — even from the background. To get the most out of this session, we recommend familiarity with handling audio transmission on your app backend. We also recommend a basic understanding of APNs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,162 words)

## Documentation & Resources

- [Push to Talk](https://developer.apple.com/documentation/PushToTalk) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PushToTalk
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PushToTalk.json

## Code Snippets

### Creating a Channel Manager — [6:52]

```swift
func setupChannelManager() async throws {
    channelManager = try await PTChannelManager.channelManager(delegate: self,
                                                               restorationDelegate: self)
}
```

### Joining a Channel — [7:33]

```swift
func joinChannel(channelUUID: UUID) {
    let channelImage = UIImage(named: "ChannelIcon")
    channelDescriptor = PTChannelDescriptor(name: "Awesome Crew", image: channelImage)

    // Ensure that your channel descriptor and UUID are persisted to disk for later use.
    channelManager.requestJoinChannel(channelUUID: channelUUID, 
                                      descriptor: channelDescriptor)
}
```

### PTChannelManagerDelegate didJoinChannel — [8:11]

```swift
func channelManager(_ channelManager: PTChannelManager, 
                    didJoinChannel channelUUID: UUID,
                    reason: PTChannelJoinReason) {
    // Process joining the channel
    print("Joined channel with UUID: \(channelUUID)")
}

func channelManager(_ channelManager: PTChannelManager,
                    receivedEphemeralPushToken pushToken: Data) {
    // Send the variable length push token to the server
    print("Received push token")
}
```

### PTChannelManagerDelegate failedToJoinChannel — [8:45]

```swift
func channelManager(_ channelManager: PTChannelManager, 
                    failedToJoinChannel channelUUID: UUID, 
                    error: Error) {
    let error = error as NSError

    switch error.code {
    case PTChannelError.channelLimitReached.rawValue:
        print("The user has already joined a channel")
    default:
        break
    }
}
```

### PTChannelManagerDelegate didLeaveChannel — [9:00]

```swift
func channelManager(_ channelManager: PTChannelManager,
                    didLeaveChannel channelUUID: UUID,
                    reason: PTChannelLeaveReason) {
    // Process leaving the channel
    print("Left channel with UUID: \(channelUUID)")
}
```

### PTChannelRestorationDelegate — [9:22]

```swift
func channelDescriptor(restoredChannelUUID channelUUID: UUID) -> PTChannelDescriptor {
    return getCachedChannelDescriptor(channelUUID)
}
```

### Provide channel descriptor updates — [10:12]

```swift
func updateChannel(_ channelDescriptor: PTChannelDescriptor) async throws {
    try await channelManager.setChannelDescriptor(channelDescriptor, 
                                                  channelUUID: channelUUID)
}
```

### Provide service status updates — [10:20]

```swift
func reportServiceIsReconnecting() async throws {
    try await channelManager.setServiceStatus(.connecting, channelUUID: channelUUID)
}

func reportServiceIsConnected() async throws {
    try await channelManager.setServiceStatus(.ready, channelUUID: channelUUID)
}
```

### Start transmission from within your app — [11:48]

```swift
func startTransmitting() {
    channelManager.requestBeginTransmitting(channelUUID: channelUUID)
}

// PTChannelManagerDelegate

func channelManager(_ channelManager: PTChannelManager, 
                    failedToBeginTransmittingInChannel channelUUID: UUID,
                    error: Error) {
    let error = error as NSError

    switch error.code {
    case PTChannelError.callIsActive.rawValue:
        print("The system has another ongoing call that is preventing transmission.")
    default:
        break
    }
}
```

### Stop transmission from within your app — [12:22]

```swift
func stopTransmitting() {
    channelManager.stopTransmitting(channelUUID: channelUUID)
}

func channelManager(_ channelManager: PTChannelManager, 
                    failedToStopTransmittingInChannel channelUUID: UUID, 
                    error: Error) {
    let error = error as NSError

    switch error.code {
    case PTChannelError.transmissionNotFound.rawValue:
        print("The user was not in a transmitting state")
    default:
        break
    }
}
```

### Responding to begin transmission delegate events — [12:41]

```swift
func channelManager(_ channelManager: PTChannelManager,
                    channelUUID: UUID, 
                    didBeginTransmittingFrom source: PTChannelTransmitRequestSource) {
    print("Did begin transmission from: \(source)")
}

func channelManager(_ channelManager: PTChannelManager,
                    didActivate audioSession: AVAudioSession) {
    print("Did activate audio session")
    // Configure your audio session and begin recording
}
```

### Responding to end transmission delegate events — [13:19]

```swift
func channelManager(_ channelManager: PTChannelManager,
                    channelUUID: UUID, 
                    didEndTransmittingFrom source: PTChannelTransmitRequestSource) {
    print("Did end transmission from: \(source)")
}

func channelManager(_ channelManager: PTChannelManager,
                    didDeactivate audioSession: AVAudioSession) {
    print("Did deactivate audio session")
    // Stop recording and clean up resources
}
```

### Receiving Push to Talk Pushes — [15:29]

```swift
func incomingPushResult(channelManager: PTChannelManager, 
                        channelUUID: UUID, 
                        pushPayload: [String : Any]) -> PTPushResult {

    guard let activeSpeaker = pushPayload["activeSpeaker"] as? String else {
        // If no active speaker is set, the only other valid operation 
        // is to leave the channel
        return .leaveChannel
    }

    let activeSpeakerImage = getActiveSpeakerImage(activeSpeaker)    
    let participant = PTParticipant(name: activeSpeaker, image: activeSpeakerImage)
    return .activeRemoteParticipant(participant)
}
```

### Stop receiving audio — [17:03]

```swift
func stopReceivingAudio() {
    channelManager.setActiveRemoteParticipant(nil, channelUUID: channelUUID)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10117/3/BC2A00F7-7836-4346-B4DD-143192926205/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10117/3/BC2A00F7-7836-4346-B4DD-143192926205/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10117) — developer.apple.com. Indexed for agent consumption._
