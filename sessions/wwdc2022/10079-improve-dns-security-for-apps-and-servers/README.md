---
id: "wwdc2022-10079"
event: "wwdc2022"
year: 2022
title: "Improve DNS security for apps and servers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10079"
topics: ["Privacy & Security", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Improve DNS security for apps and servers

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10079](https://developer.apple.com/videos/play/wwdc2022/10079)

Discover the latest ways to ensure that DNS — the foundation of internet addressing — is secure within your app. Learn how to authenticate DNS responses in your app with DNSSEC and enable DNS encryption automatically with Discovery of Designated Resolvers (DDR).

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,745 words)

## Code Snippets

### Require DNSSEC validation in your URL request at session level — [9:01]

```swift
let configuration = URLSessionConfiguration.default
configuration.requiresDNSSECValidation = true
let session = URLSession(configuration: configuration)
```

### Require DNSSEC validation in your URL request at request level — [9:38]

```swift
var request = URLRequest(url: URL(string: "https://www.example.org")!)
request.requiresDNSSECValidation = true
let (data, response) = try await URLSession.shared.data(for: request)
```

### Require DNSSEC validation in your network request — [10:08]

```swift
let parameters = NWParameters.tls
parameters.requiresDNSSECValidation = true
let connection = NWConnection(host: "www.example.org", port: .https, using: parameters)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10079/5/31E85A57-3035-4B6A-9BA4-4A73D156F55E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10079/5/31E85A57-3035-4B6A-9BA4-4A73D156F55E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10079) — developer.apple.com. Indexed for agent consumption._
