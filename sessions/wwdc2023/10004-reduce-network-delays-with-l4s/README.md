---
id: "wwdc2023-10004"
event: "wwdc2023"
year: 2023
title: "Reduce network delays with L4S"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10004"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Reduce network delays with L4S

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10004](https://developer.apple.com/videos/play/wwdc2023/10004)

Streaming video, multiplayer games, and other real-time experiences depend on responsive, low latency networking. Learn how Low Latency, Low Loss, Scalable throughput (L4S) can reduce network delays and improve the overall experience in your app. We’ll show you how to set up and test your app, network, and server with L4S.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,121 words)

## Documentation & Resources

- [Testing and Debugging L4S in Your App](https://developer.apple.com/documentation/Network/testing-and-debugging-l4s-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Network/testing-and-debugging-l4s-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Network/testing-and-debugging-l4s-in-your-app.json

## Code Snippets

### Throttle Internet Sharing — [14:38]

```bash
sudo ifconfig en1 tbr 10Mbps
```

### Turn on L4S — [15:36]

```bash
sudo defaults write -g network_enable_l4s -bool true
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10004/4/49EBBF59-4DE7-42C2-AC03-9CD32C46DE74/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10004/4/49EBBF59-4DE7-42C2-AC03-9CD32C46DE74/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10004) — developer.apple.com. Indexed for agent consumption._
