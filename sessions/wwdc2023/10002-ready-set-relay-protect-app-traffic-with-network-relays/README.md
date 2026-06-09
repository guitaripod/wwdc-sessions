---
id: "wwdc2023-10002"
event: "wwdc2023"
year: 2023
title: "Ready, set, relay: Protect app traffic with network relays"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10002"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Ready, set, relay: Protect app traffic with network relays

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10002](https://developer.apple.com/videos/play/wwdc2023/10002)

Learn how relays can make your app’s network traffic more private and secure without the overhead of a VPN. We’ll show you how to integrate relay servers in your own app and explore how enterprise networks can use relays to securely access internal resources.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,695 words)

## Documentation & Resources

- [Relays](https://developer.apple.com/documentation/NetworkExtension/relays) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/relays
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/relays.json
- [ProxyConfiguration](https://developer.apple.com/documentation/Network/ProxyConfiguration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/ProxyConfiguration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/ProxyConfiguration.json

## Code Snippets

### Configuring a relay — [4:52]

```swift
import Network

let relayEndpoint = NWEndpoint.url(URL(string: "https://relay.example.com")!)
let relayServer = ProxyConfiguration.RelayHop(http3RelayEndpoint: relayEndpoint)

let relayConfig = ProxyConfiguration(relayHops: [relayServer])
```

### Configuring a relay in Network framework — [5:40]

```swift
import Network

let relayEndpoint = NWEndpoint.url(URL(string: "https://relay.example.com")!)
let relayServer = ProxyConfiguration.RelayHop(http3RelayEndpoint: relayEndpoint)

let relayConfig = ProxyConfiguration(relayHops: [relayServer])

var context = NWParameters.PrivacyContext(description: "my relay")
context.proxyConfigurations = [relayConfig]

let parameters = NWParameters.tls
parameters.setPrivacyContext(context)

let connection = NWConnection(host: "www.example.com", port: 443, using: parameters)
connection.start(queue: .main)
```

### Configuring a relay in URLSession — [6:07]

```swift
import Network

let relayEndpoint = NWEndpoint.url(URL(string: "https://relay.example.com")!)
let relayServer = ProxyConfiguration.RelayHop(http3RelayEndpoint: relayEndpoint)

let relayConfig = ProxyConfiguration(relayHops: [relayServer])

let config = URLSessionConfiguration.default
config.proxyConfigurations = [relayConfig]

let mySession = URLSession(configuration: config)
let url = URL(string: "https://www.example.com/api/v1/employees")!
let (data, response) = try await mySession.data(from: url)
```

### Configuring a relay in WebKit — [6:30]

```swift
import Network

let relayEndpoint = NWEndpoint.url(URL(string: "https://relay.example.com")!)
let relayServer = ProxyConfiguration.RelayHop(http3RelayEndpoint: relayEndpoint)

let relayConfig = ProxyConfiguration(relayHops: [relayServer])

let webkitConfig = WKWebViewConfiguration()
webkitConfig.websiteDataStore = WKWebsiteDataStore.nonPersistent()
webkitConfig.websiteDataStore.proxyConfigurations = [relayConfig]
let webView = WKWebView(frame: .zero, configuration: webkitConfig)

let url = URL(string: "https://www.example.com/api/v1/employees")!
webView.load(URLRequest(url: url))
```

### Configuring a relay on the device with a configuration profile — [9:15]

```xml
<dict>
    <key>PayloadType</key>
    <string>com.apple.relay.managed</string>
    <key>Relays</key>
    <array>
        <dict>
            <key>HTTP3RelayURL</key>
            <string>https://relay.example.com</string>
            <key>PayloadCertificateUUID</key>
            <string>5AB702EC-32F3-48A9-94FE-8EA1C67ACF46</string>
        </dict>
    </array>
    <key>MatchDomains</key>
    <array>
        <string>internal.example.com</string>
    </array>
</dict>
```

### Configuring a relay on the device with NetworkExtension — [9:42]

```swift
import NetworkExtension

let newRelay = NERelay()
let relayURL = URL(string: "https://relay.example.com:443/")
newRelay.http3RelayURL = relayURL
newRelay.http2RelayURL = relayURL

newRelay.additionalHTTPHeaderFields = ["Authorization" : "PrivateToken=123"]

let manager = NERelayManager.shared()
manager.relays = [newRelay]
manager.matchDomains = ["internal.example.com"]

manager.isEnabled = true
do {
    try await manager.saveToPreferences()
} catch let saveError {
    // Handle error
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10002/5/F08830EB-6B56-4461-837E-ADE708BAA71C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10002/5/F08830EB-6B56-4461-837E-ADE708BAA71C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10002) — developer.apple.com. Indexed for agent consumption._
