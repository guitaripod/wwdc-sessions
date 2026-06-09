---
id: "wwdc2020-10100"
event: "wwdc2020"
year: 2020
title: "Meet Watch Face Sharing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10100"
topics: ["Safari & Web", "SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Meet Watch Face Sharing

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10100](https://developer.apple.com/videos/play/wwdc2020/10100)

Show off your watchOS app’s complications and create a watch face worth sharing. Learn how to share watch faces inside your watchOS and iOS apps or host them on the web for anyone to find and download. We’ll also explore best practices for using watch face preview images, and show you how to create a smooth installation experience.

**Keywords:** `⌚️`, `☕️`, `clockkit`, `complications`, `watchkit`, `watchos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,398 words)

## Documentation & Resources

- [Human Interface Guidelines: Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/watch-faces
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/ClockKit/sharing-an-apple-watch-face) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit/sharing-an-apple-watch-face
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit/sharing-an-apple-watch-face.json
- [Apple Design Resources](https://developer.apple.com/design/resources/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/design/resources/

## Code Snippets

### Detect Paired Watch — [7:20]

```swift
var isPaired: Bool {
    if (WCSession.isSupported()) {
        let session = WCSession.default
        session.delegate = self
        session.activate()
        return session.isPaired
    } else {
        return false
    }
}
```

### Add Face Wrapper — [9:01]

```swift
private func addFaceWrapper(withName: String) {
    if let watchfaceURL = Bundle.main.url(forResource: withName, withExtension: "watchface") {
        CLKWatchFaceLibrary().addWatchFace(at: watchfaceURL, completionHandler: {
            (error: Error?) in
            if let nsError = error as NSError?, nsError.code == CLKWatchFaceLibrary.ErrorCode.faceNotAvailable.rawValue {
                print(nsError)
            }
            isLoading = false
        })
    }
}
```

### Add Face Wrapper with Fallback Face — [11:04]

```swift
private func addFaceWrapper(withName: String, fallbackName: String?) {
    if let watchfaceURL = Bundle.main.url(forResource: withName, withExtension: "watchface") {
        CLKWatchFaceLibrary().addWatchFace(at: watchfaceURL, completionHandler: {
            (error: Error?) in
            if let nsError = error as NSError?, nsError.code == CLKWatchFaceLibrary.ErrorCode.faceNotAvailable.rawValue {
                if let name = fallbackName {
                    // We failed, trying with fallbackName.
                    addFaceWrapper(withName: name, fallbackName: nil)
                }
            }
            isLoading = false
        })
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10100/2/880A8C5B-FB7B-456E-951B-5D13415E1B70/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10100) — developer.apple.com. Indexed for agent consumption._
