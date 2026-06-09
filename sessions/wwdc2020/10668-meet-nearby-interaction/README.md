---
id: "wwdc2020-10668"
event: "wwdc2020"
year: 2020
title: "Meet Nearby Interaction"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10668"
topics: ["Maps & Location"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet Nearby Interaction

**Event:** WWDC20 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10668](https://developer.apple.com/videos/play/wwdc2020/10668)

The Nearby Interaction framework streams distance and direction between opted-in Apple devices containing the U1 chip. Discover how this powerful combination of hardware and software allow you to create intuitive spatial interactions based on the relative position of two or more devices. We'll walk you through this session-based API and show you how to deliver entirely new interactive experiences — all with privacy in mind.

**Keywords:** `interactive`, `proximity`, `sharing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,300 words)

## Documentation & Resources

- [Implementing interactions between users in close proximity](https://developer.apple.com/documentation/NearbyInteraction/implementing-interactions-between-users-in-close-proximity) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NearbyInteraction/implementing-interactions-between-users-in-close-proximity
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NearbyInteraction/implementing-interactions-between-users-in-close-proximity.json
- [Nearby Interaction](https://developer.apple.com/documentation/NearbyInteraction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NearbyInteraction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NearbyInteraction.json

## Code Snippets

### Basic session setup — [6:01]

```swift
// A session instance. Store in whichever data structure makes the most sense for your app.
var niSession: NISession?

// Instantiate a new session object and set the session's delegate.
func prepareMySession() {
  // Verify hardware support.
  guard NISession.isSupported else {
    print("Nearby Interaction is not available on this device.")
    return
  }

  // Create a new session for each peer.
  niSession = NISession()

  // Set the session’s delegate.
  niSession?.delegate = self // This class of 'self' needs to conform to NISessionDelegate.
}

// Share the encoded discovery token to the peer you intend to interact with.
func sendDiscoveryTokenToMyPeer(myPeer: Any /* change to whichever type represents peers in your app */) {                                
	guard let myToken = niSession?.discoveryToken else {
		// The session object is not initialized or has been invalidated.
		return
	}

	if let encodedToken = try? NSKeyedArchiver.archivedData(withRootObject: myToken, requiringSecureCoding: true) {
		<# share token using your app's networking layer #>
	}
}

// Once you receive a token from the peer, create a configuration and run the session.
// This functions shows how to decode token data that was previously encoded using NSKeyedArchiver.
func runMySession(peerTokenData: Data) {
  guard let peerDiscoveryToken = try? NSKeyedUnarchiver.unarchivedObject(ofClass: NIDiscoveryToken.self, from: peerTokenData) else {
    print("Unexpectedly failed to decode discovery token.")
    return
  }

  // Create a session configuration using the discovery token received from the peer.
  let config = NINearbyPeerConfiguration(peerToken: peerDiscoveryToken)

  // Run the session with the configuration.
  niSession?.run(config)
}
```

### Verify hardware support — [12:40]

```swift
// Always verify hardware support.
guard NISession.isSupported else {
  print("Nearby Interaction is not available on this device.")
  return
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10668/6/69354ABA-CE3E-4420-A19A-DBF26B4788ED/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10668) — developer.apple.com. Indexed for agent consumption._
