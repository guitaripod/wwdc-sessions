---
id: "wwdc2021-10239"
event: "wwdc2021"
year: 2021
title: "Reduce network delays for your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10239"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Reduce network delays for your app

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10239](https://developer.apple.com/videos/play/wwdc2021/10239)

CPU performance and network throughput rates keep improving, but the speed of light is one limit that isn’t going any higher. Learn the APIs and best practices to maximize your app’s responsiveness and efficiency by keeping network round-trip times low and minimizing the number of round trips when performing network operations.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,034 words)

## Code Snippets

### Fast open with TCP handshake — [9:28]

```swift
/* Allow fast open on the connection parameters */
parameters.allowFastOpen = true

let connection = NWConnection(to: endpoint, using: parameters)

/* Call send with idempotent initial data before starting the connection */
connection.send(content: initialData, completion: .idempotent)
connection.start(queue: myQueue)
```

### Sockets with fast open — [11:01]

```swift
connectx(fd, ..., CONNECT_DATA_IDEMPOTENT | CONNECT_RESUME_ON_READ_WRITE, ...); // delay SYN
write(fd, ...); // SYN goes out with first data segment
```

### Save round-trips when switching networks with Multipath TCP — [13:35]

```swift
// Multipath TCP
// Save multiple round-trips when switching networks

// On URLSessionConfiguration
let configuration = URLSessionConfiguration.default
configuration.multipathServiceType = .interactive

// On NWParameters
let parameters = NWParameters.tcp
parameters.multipathServiceType = .interactive
```

### Background service type, App in foreground — [20:09]

```swift
//Use default  URLSession, set background on URLRequest
var request = URLRequest(url: myurl)
request.networkServiceType = .background

//Set service class on parameters to apply to the  NWConnection
let parameters = NWParameters.tls
parameters.serviceClass = .background
```

### Time insensitive tasks running in background — [20:10]

```swift
//Configure background URL Session

lazy var urlSession: URLSession = {
    let configuration = URLSessionConfiguration.background(withIdentifier: "MySession")
    configuration.isDiscretionary = true
    return URLSession(configuration: configuration, delegate: self, delegateQueue: nil)
}()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10239/4/8C138558-C5F3-4328-AA26-1F2D924B69F9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10239/4/8C138558-C5F3-4328-AA26-1F2D924B69F9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10239) — developer.apple.com. Indexed for agent consumption._
