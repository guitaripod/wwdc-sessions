---
id: "wwdc2025-250"
event: "wwdc2025"
year: 2025
title: "Use structured concurrency with Network framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/250"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Use structured concurrency with Network framework

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-250](https://developer.apple.com/videos/play/wwdc2025/250)

Network framework is the best way to make low-level network connections on Apple platforms — and in iOS, iPadOS, and macOS 26, it’s a perfect fit for your structured concurrency code. We’ll explore how you can make connections, send and receive data and framed messages, listen for incoming connections, and browse the network for services. We’ll also cover key best practices along the way.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,892 words)

## Documentation & Resources

- [NetworkBrowser](https://developer.apple.com/documentation/Network/NetworkBrowser) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/NetworkBrowser
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/NetworkBrowser.json
- [NetworkListener](https://developer.apple.com/documentation/Network/NetworkListener) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/NetworkListener
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/NetworkListener.json
- [NetworkConnection](https://developer.apple.com/documentation/Network/NetworkConnection) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/NetworkConnection
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/NetworkConnection.json
- [Building a custom peer-to-peer protocol](https://developer.apple.com/documentation/Network/building-a-custom-peer-to-peer-protocol) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/building-a-custom-peer-to-peer-protocol
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/building-a-custom-peer-to-peer-protocol.json
- [Network](https://developer.apple.com/documentation/Network) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network.json

## Code Snippets

### Make a connection with TLS — [4:04]

```swift
// Make a connection

import Network

let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
  TLS() 
}
```

### Make a connection with TLS and IP options — [4:41]

```swift
// Make a connection

import Network

let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029) {
  TLS {
    TCP {
      IP()
        .fragmentationEnabled(false)
    }
  }
}
```

### Make a connection with customized parameters — [5:07]

```swift
// Make a connection

import Network

let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029),
                                   using: .parameters {
  TLS {
    TCP {
      IP()
        .fragmentationEnabled(false)
    }
  }
}
.constrainedPathsProhibited(true))
```

### Send and receive on a connection — [7:30]

```swift
// Send and receive on a connection

import Network

public func sendAndReceiveWithTLS() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    TLS()
  }

  let outgoingData = Data("Hello, world!".utf8)
  try await connection.send(outgoingData)

  let incomingData = try await connection.receive(exactly: 98).content
  print("Received data: \(incomingData)")
}
```

### Send and receive on a connection — [8:29]

```swift
// Send and receive on a connection

import Network

public func sendAndReceiveWithTLS() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    TLS()
  }

  let outgoingData = Data("Hello, world!".utf8)
  try await connection.send(outgoingData)

  let remaining32 = try await connection.receive(as: UInt32.self).content
  guard var remaining = Int(exactly: remaining32) else { /* ... throw an error ... */ }
  while remaining > 0 {
    let imageChunk = try await connection.receive(atLeast: 1, atMost: remaining).content
    remaining -= imageChunk.count

    // Parse the next portion of the image before continuing
  }
}
```

### Tic-Tac-Toe game messages — [11:06]

```swift
// TicTacToe game messages

import Network

enum GameMessage: Int {
  case selectedCharacter = 0
  case move = 1
}

struct GameCharacter: Codable {
  let character: String
}

struct GameMove: Codable {
  let row: Int
  let column: Int
}
```

### Send TicTacToe game messages with TLV — [11:24]

```swift
// Send TicTacToe game messages with TLV

import Network

public func sendWithTLV() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    TLV {
      TLS()
    }
  }

  let characterData = try JSONEncoder().encode(GameCharacter(character: "🐨"))
  try await connection.send(characterData, type: GameMessage.selectedCharacter.rawValue)
}
```

### Receive TicTacToe game messages with TLV — [11:53]

```swift
import Network

public func receiveWithTLV() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    TLV {
      TLS()
    }
  }

  let (incomingData, metadata) = try await connection.receive()
  switch GameMessage(rawValue: metadata.type) {
  case .selectedCharacter:
    let character = try JSONDecoder().decode(GameCharacter.self, from: incomingData)
    print("Character selected: \(character)")
  case .move:
    let move = try JSONDecoder().decode(GameMove.self, from: incomingData)
    print("Move: \(move)")
  case .none:
    print("Unknown message")
  }
}
```

### Tic-Tac-Toe game messages with Coder — [12:50]

```swift
// TicTacToe game messages with Coder

import Network

enum GameMessage: Codable {
  case selectedCharacter(String)
  case move(row: Int, column: Int)
}
```

### Send TicTacToe game messages with Coder — [13:13]

```swift
// Send TicTacToe game messages with Coder

import Network

public func sendWithCoder() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    Coder(GameMessage.self, using: .json) {
      TLS()
    }
  }

  let selectedCharacter: GameMessage = .selectedCharacter("🐨")
  try await connection.send(selectedCharacter)
}
```

### Receive TicTacToe game messages with Coder — [13:53]

```swift
// Receive TicTacToe game messages with Coder

import Network

public func receiveWithCoder() async throws {
  let connection = NetworkConnection(to: .hostPort(host: "www.example.com", port: 1029)) {
    Coder(GameMessage.self, using: .json) {
      TLS()
    }
  }

  let gameMessage = try await connection.receive().content
  switch gameMessage {
  case .selectedCharacter(let character):
    print("Character selected: \(character)")
  case .move(let row, let column):
    print("Move: (\(row), \(column))")
  }
}
```

### Listen for incoming connections with NetworkListener — [15:16]

```swift
// Listen for incoming connections with NetworkListener

import Network

public func listenForIncomingConnections() async throws {
  try await NetworkListener {
    Coder(GameMessage.self, using: .json) {
      TLS()
    }
  }.run { connection in
    for try await (gameMessage, _) in connection.messages {
      // Handle the GameMessage
    }
  }
}
```

### Browse for nearby paired Wi-Fi Aware devices — [17:39]

```swift
// Browse for nearby paired Wi-Fi Aware devices

import Network
import WiFiAware

public func findNearbyDevice() async throws {
  let endpoint = try await NetworkBrowser(for: .wifiAware(.connecting(to: .allPairedDevices, from: .ticTacToeService))).run { endpoints in
    .finish(endpoints.first!)
  }

  // Make a connection to the endpoint
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/250/4/ffac19d6-02fb-4abc-a491-fc009e5d38e3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/250/4/ffac19d6-02fb-4abc-a491-fc009e5d38e3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/250) — developer.apple.com. Indexed for agent consumption._
