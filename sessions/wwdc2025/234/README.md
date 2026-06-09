---
id: "wwdc2025-234"
event: "wwdc2025"
year: 2025
title: "Filter and tunnel network traffic with NetworkExtension"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/234"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Filter and tunnel network traffic with NetworkExtension

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-234](https://developer.apple.com/videos/play/wwdc2025/234)

Learn about the APIs in the NetworkExtension framework that give your app the power and flexibility to extend the system’s core networking features — like implementing network content filters, creating and managing VPN configurations, and more. In iOS, iPadOS and macOS 26, you can now build robust content filters that make traffic decisions using the entire URL — not just the hostname — all without compromising privacy and security. We’ll start by briefly covering many of the key use cases for the NetworkExtension framework, including network relays and VPN. Then, we’ll dive into the new URL filter API and its key components, including Private Information Retrieval, Privacy Pass, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,608 words)

## Documentation & Resources

- [verdict(for:)](https://developer.apple.com/documentation/NetworkExtension/NEURLFilter/verdict(for:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/NEURLFilter/verdict(for:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/NEURLFilter/verdict(for:).json
- [NEHotspotManager](https://developer.apple.com/documentation/NetworkExtension/NEHotspotManager) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/NEHotspotManager
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/NEHotspotManager.json
- [NEURLFilterManager](https://developer.apple.com/documentation/NetworkExtension/NEURLFilterManager) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/NEURLFilterManager
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/NEURLFilterManager.json
- [TN3165: Packet Filter is not API](https://developer.apple.com/documentation/Technotes/tn3165-packet-filter-is-not-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3165-packet-filter-is-not-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3165-packet-filter-is-not-api.json
- [TN3120: Expected use cases for Network Extension packet tunnel providers](https://developer.apple.com/documentation/Technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Technotes/tn3120-expected-use-cases-for-network-extension-packet-tunnel-providers.json
- [PIRService](https://swiftpackageindex.com/apple/pir-service-example/main/documentation/pirservice) _documentation_
- [Filtering traffic by URL](https://developer.apple.com/documentation/NetworkExtension/filtering-traffic-by-url) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/filtering-traffic-by-url
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/filtering-traffic-by-url.json
- [Network Extension](https://developer.apple.com/documentation/NetworkExtension) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension.json

## Code Snippets

### Use participation API to check URLs before sending requests — [22:15]

```swift
// Use participation API to check URLs before sending requests

import NetworkExtension

func checkURL(url: URL) async throws -> Bool {
  var passRequest : Bool = true

  let verdict = await NEURLFilter.verdict(for: url)

  if verdict == .deny {
    passRequest = false
  }
  return passRequest
}
```

### Configure and manage URL Filter — [25:01]

```swift
// Configure and manage URL Filter

import NetworkExtension

let manager = NEURLFilterManager.shared

try await manager.loadFromPreferences()

try manager.setConfiguration(
    pirServerURL: URL(string:"https://pir.example.com")!,
    pirPrivacyPassIssuerURL: URL(string:"https://privacypass.example.com")!,
    pirAuthenticationToken: "1234",
    controlProviderBundleIdentifier: "com.example.myURLFilter.extension")

manager.prefilterFetchInterval = 86400 // fetch every 1 day
manager.shouldFailClosed = false
manager.localizedDescription = "Alice's URL Filter"
manager.isEnabled = true

try await manager.saveToPreferences()
```

### Implement NEURLFilterControlProvider protocol — [26:41]

```swift
// Implement NEURLFilterControlProvider protocol

import NetworkExtension

class URLFilterControlProvider: NEURLFilterControlProvider {

  func fetchPrefilter() async throws -> NEURLFilterPrefilter? {

    // Fetch your Bloom filters data from your app bundle or from your server
    let data = NEURLFilterPrefilter.PrefilterData.temporaryFilepath(fileURL)
    let result = NEURLFilterPrefilter(data: data,
                                      bitCount: numberOfBits,
                                      hashCount: numberOfHashes,
                                      murmurSeed: murmurSeed)
    return result
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/234/4/54f59553-dbd4-48aa-8240-99dbbc735d7b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/234/4/54f59553-dbd4-48aa-8240-99dbbc735d7b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/234) — developer.apple.com. Indexed for agent consumption._