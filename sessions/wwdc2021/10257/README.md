---
id: "wwdc2021-10257"
event: "wwdc2021"
year: 2021
title: "Meet ClassKit for file-based apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10257"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet ClassKit for file-based apps

**Event:** WWDC21 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10257](https://developer.apple.com/videos/play/wwdc2021/10257)

The ClassKit framework can help surface educational activities within your app to teachers using the Schoolwork app. Discover how you can provide teachers with greater insights into student learning by adopting the latest file-based API to report student progress data within your app. We’ll also show you how to use ClassKit to report out different data types, and how to test your implementation in developer mode.

**Keywords:** `document`, `school`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,225 words)

## Documentation & Resources

- [fetchActivity(for:completion:)](https://developer.apple.com/documentation/ClassKit/CLSDataStore/fetchActivity(for:completion:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClassKit/CLSDataStore/fetchActivity(for:completion:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClassKit/CLSDataStore/fetchActivity(for:completion:).json
- [Incorporating ClassKit into an Educational App](https://developer.apple.com/documentation/ClassKit/incorporating-classkit-into-an-educational-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClassKit/incorporating-classkit-into-an-educational-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClassKit/incorporating-classkit-into-an-educational-app.json
- [ClassKit](https://developer.apple.com/documentation/ClassKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClassKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClassKit.json

## Code Snippets

### openFile() — [7:25]

```swift
func openFile() async throws {
     // Your existing code for opening a file goes here.
     let activity = await try CLSDataStore.shared.fetchActivity(for: fileURL)
     activity.start()
     await try CLSDataStore.shared.save()
}
```

### closeFile() — [8:07]

```swift
func closeFile() async throws {
     let activity = await try CLSDataStore.shared.fetchActivity(for: fileURL)
     let wordCount = activity.primaryActivityItem as? CLSQuantityItem ??
         CLSQuantityItem(identifier: "total_word_count", title: "Word Count")
     wordCount.quantity = currentDocumentWordCount()
     activity.primaryActivityItem = wordCount
     activity.progress = progress()
     activity.stop()
     await try CLSDataStore.shared.save()
}
```

### closeFile()2 — [8:48]

```swift
func closeFile() async throws {
     let activity = await try CLSDataStore.shared.fetchActivity(for: fileURL)
     let wordCount = activity.primaryActivityItem as? CLSQuantityItem ??
         CLSQuantityItem(identifier: "total_word_count", title: "Word Count")
     wordCount.quantity = currentDocumentWordCount()
     activity.primaryActivityItem = wordCount
     activity.progress = progress()
     activity.stop()
     await try CLSDataStore.shared.save()
}
```

### openFile() BreakPointHit — [11:20]

```swift
func openFile() async throws {
     // Your existing code for opening a file goes here.
     let activity = await try CLSDataStore.shared.fetchActivity(for: fileURL)
     activity.start()
     await try CLSDataStore.shared.save()
}
```

### closeFile() BreakPointhit — [11:55]

```swift
func closeFile() async throws {
     let activity = await try CLSDataStore.shared.fetchActivity(for: fileURL)
     let wordCount = activity.primaryActivityItem as? CLSQuantityItem ??
         CLSQuantityItem(identifier: "total_word_count", title: "Word Count")
     wordCount.quantity = currentDocumentWordCount()
     activity.primaryActivityItem = wordCount
     activity.progress = progress()
     activity.stop()
     await try CLSDataStore.shared.save()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10257/6/1A9F8965-41D7-4A10-A0B1-36FE84E977EE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10257/6/1A9F8965-41D7-4A10-A0B1-36FE84E977EE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10257) — developer.apple.com. Indexed for agent consumption._