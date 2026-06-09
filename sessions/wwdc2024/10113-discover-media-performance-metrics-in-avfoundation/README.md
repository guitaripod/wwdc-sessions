---
id: "wwdc2024-10113"
event: "wwdc2024"
year: 2024
title: "Discover media performance metrics in AVFoundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10113"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Discover media performance metrics in AVFoundation

**Event:** WWDC24 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10113](https://developer.apple.com/videos/play/wwdc2024/10113)

Discover how you can monitor, analyze, and improve user experience with the new media performance APIs. Explore how to monitor AVPlayer performance for HLS assets using different AVMetricEvents, and learn how to use these metrics to understand and triage player performance issues.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,096 words)

## Documentation & Resources

- [Forum: Media Technologies](https://developer.apple.com/forums/topics/media-technologies?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/media-technologies?cid=vf-a-0010

## Code Snippets

### AVMetric Publishers — [6:27]

```swift
public protocol AVMetricEventStreamPublisher 
{
	func metrics<MetricType: AVMetricEvent>(forType metricType: MetricType.Type) -> AVMetrics<MetricType>

	func allMetrics() -> AVMetrics<AVMetricEvent>
}

extension AVPlayerItem : AVMetricEventStreamPublisher
```

### Example showing how to obtain likely to keep up and summary metrics from AVPlayerItem - Swift — [6:50]

```swift
let playerItem : AVPlayerItem = ...

let ltkuMetrics = item.metrics(forType: AVMetricPlayerItemLikelyToKeepUpEvent.self)
let summaryMetrics = item.metrics(forType: AVMetricPlayerItemPlaybackSummaryEvent.self)

for await (metricEvent, publisher) in ltkuMetrics.chronologicalMerge(with: summaryMetrics) 
{
	// send metricEvent to server
}
```

### Example showing how to obtain likely to keep up and summary metrics from AVPlayerItem - Objective-C — [7:26]

```swift
AVPlayerItem *item = ...

AVMetricEventStream *eventStream = [AVMetricEventStream eventStream];
id<AVMetricEventStreamSubscriber> subscriber = [[MyMetricSubscriber alloc] init];
[eventStream setSubscriber:subscriber queue:mySerialQueue]

[eventStream subscribeToMetricEvent:[AVMetricPlayerItemLikelyToKeepUpEvent class]];
[eventStream subscribeToMetricEvent:[AVMetricPlayerItemPlaybackSummaryEvent class]];

[eventStream addPublisher:item];
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10113/4/FADD3DD1-246C-483B-BA77-5D9BE374E39B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10113/4/FADD3DD1-246C-483B-BA77-5D9BE374E39B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10113) — developer.apple.com. Indexed for agent consumption._
