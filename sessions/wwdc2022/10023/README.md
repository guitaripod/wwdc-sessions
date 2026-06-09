---
id: "wwdc2022-10023"
event: "wwdc2022"
year: 2022
title: "What's new in the Photos picker"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10023"
topics: ["Essentials", "Photos & Camera"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What's new in the Photos picker

**Event:** WWDC22 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10023](https://developer.apple.com/videos/play/wwdc2022/10023)

PHPicker provides simple and secure integration between your app and the system Photos library. Learn how SwiftUI and Transferable can help you offer integration across iOS, iPadOS, macOS, and watchOS.

We’ll also show you how you can use AppKit and NSOpenPanel to bring the Photos picker on Mac into your macOS apps.

For even more on the Photos picker, watch "Improve access to Photos in your app" from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,954 words)

## Documentation & Resources

- [Selecting Photos and Videos in iOS](https://developer.apple.com/documentation/PhotoKit/selecting-photos-and-videos-in-ios) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PhotoKit/selecting-photos-and-videos-in-ios
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PhotoKit/selecting-photos-and-videos-in-ios.json
- [PhotoKit](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json

## Code Snippets

### PHPicker Example (UIKit) — [0:01]

```swift
var configuration = PHPickerConfiguration()
configuration.filter = .images
configuration.selection = .ordered
configuration.selectionLimit = 10

let picker = PHPickerViewController(configuration: configuration)
```

### PHPickerFilter — [0:02]

```swift
var configuration = PHPickerConfiguration()

// iOS 15
// Shows videos and Live Photos
configuration.filter = .any(of: [.videos, .livePhotos])

// New: iOS 15
// Shows screenshots only
configuration.filter = .screenshots

// New: iOS 15
// Shows images excluding screenshots
configuration.filter = .all(of: [.images, .not(.screenshots)])

// New: iOS 16
// Shows cinematic videos
configuration.filter = .cinematicVideos
```

### PHPicker Example (AppKit) — [0:03]

```swift
var configuration = PHPickerConfiguration()
configuration.filter = .images
configuration.selectionLimit = 10

let picker = PHPickerViewController(configuration: configuration)
```

### PhotosPicker Example (SwiftUI) — [0:04]

```swift
struct ContentView: View {
    @Binding selection: [PhotosPickerItem]

    var body: some View {
        PhotosPicker(
            selection: $selection,
            matching: .images
        ) {
            Text("Select Photos")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10023/3/7AAE9501-211F-4201-B017-2AAC7F0C2556/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10023/3/7AAE9501-211F-4201-B017-2AAC7F0C2556/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10023) — developer.apple.com. Indexed for agent consumption._