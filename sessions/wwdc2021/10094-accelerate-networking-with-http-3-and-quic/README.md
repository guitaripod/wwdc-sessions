---
id: "wwdc2021-10094"
event: "wwdc2021"
year: 2021
title: "Accelerate networking with HTTP/3 and QUIC"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10094"
topics: ["Safari & Web", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Accelerate networking with HTTP/3 and QUIC

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10094](https://developer.apple.com/videos/play/wwdc2021/10094)

The web is changing, and the next major version of HTTP is here. Learn how HTTP/3 reduces latency and improves reliability for your app and discover how its underlying transport, QUIC, unlocks new innovations in your own custom protocols using new transport functionality and multi-streaming connection groups.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,615 words)

## Code Snippets

### Using QUIC in your app — [13:20]

```swift
// Create a connection using QUIC
let connection = NWConnection(host: "example.com", port: 443, using: .quic(alpn: ["myproto"]))

// Set the state update handler to be notified when the connection is ready
connection.stateUpdateHandler = { newState in
    switch newState {
    case .ready:
        print("Connected using QUIC!")
    default:
        break
    }
}

// Start the connection with callback queue
connection.start(queue: queue)
```

### Establish a tunnel with NWMultiplexGroup — [15:08]

```swift
// Establish a tunnel with NWMultiplexGroup

// Create a group
let descriptor = NWMultiplexGroup(to: .hostPort(host: "example.com", port: 443))
let group = NWConnectionGroup(with: descriptor, using: .quic(alpn: ["myproto"]))

// Set the state update handler to be notified when the group is ready
group.stateUpdateHandler = { newState in
    switch newState {
    case .ready:
        print("Connected using QUIC!")
    default:
        break
    }
}

// Start the group with callback queue
group.start(queue: queue)
```

### Manage streams with NWConnectionGroup — [15:45]

```swift
// Manage streams with NWConnectionGroup

// Create a new outgoing stream
let connection = NWConnection(from: group)

// Receive new incoming streams initiated by the remote endpoint
group.newConnectionHandler = { newConnection in

    // Set state update handler on incoming stream
    newConnection.stateUpdateHandler = { newState in
        // Handle stream states
    }

    // Start the incoming stream
    newConnection.start(queue: queue)

}
```

### Receive incoming QUIC tunnels from NWListener — [16:43]

```swift
// Receive incoming QUIC tunnels from NWListener

// Set the new connection group handler
listener.newConnectionGroupHandler = { group in

    group.stateUpdateHandler = { newState in
        // Handle tunnel states
    }

    group.newConnectionHandler = { stream in
        // Set up and start new incoming streams
    }

    group.start(queue: queue)

}
```

### Access QUIC metadata — [17:22]

```swift
// Access QUIC metadata to learn about and modify streams

// Find the stream ID of a particular QUIC stream
if let metadata = connection.metadata(definition: NWProtocolQUIC.definition)
                             as? NWProtocolQUIC.Metadata {
    print("QUIC Stream ID is \(metadata.streamIdentifier)")

    // Some time later...

    // Set the application error, if appropriate, before cancelling the stream
    metadata.applicationError = 0x100
    connection.cancel()

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10094/7/81661D98-9D24-4A8F-8805-9460365F986B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10094/7/81661D98-9D24-4A8F-8805-9460365F986B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10094) — developer.apple.com. Indexed for agent consumption._
