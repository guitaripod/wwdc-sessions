---
id: "wwdc2023-10239"
event: "wwdc2023"
year: 2023
title: "Add SharePlay to your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10239"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Add SharePlay to your app

**Event:** WWDC23 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10239](https://developer.apple.com/videos/play/wwdc2023/10239)

Discover how your app can take advantage of SharePlay to turn any activity into a shareable experience with friends! We’ll share the latest updates to SharePlay, explore the benefits of creating shared activities, dive into some exciting use cases, and take you through best practices to create engaging and fun moments of connection in your app.

**Keywords:** `group activities`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,201 words)

## Code Snippets

### Defining your GroupActivity type — [4:15]

```swift
var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()

    metadata.title = “Order Tacos Together”

    metadata.type = .generic

    return metadata
}
```

### Add SharePlay — [9:50]

```swift
import GroupActivities

struct OrderTogether: GroupActivity {
    // Define a unique activity identifier for system to reference
    static let activityIdentifier = "com.example.apple-samplecode.TacoTruck.OrderTogether"

    // App-specific data so your app can launch the activity on others' devices
    let orderUUID: UUID
    let truckName: String

    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.title = "Order Tacos Together"
        metadata.subtitle = truckName
        metadata.previewImage = UIImage(named: "ActivityImage")?.cgImage
        metadata.type = .shopTogether
        return metadata
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10239/5/0F1CDDAF-2EAD-43A1-8B09-806ED4EE707A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10239/5/0F1CDDAF-2EAD-43A1-8B09-806ED4EE707A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10239) — developer.apple.com. Indexed for agent consumption._