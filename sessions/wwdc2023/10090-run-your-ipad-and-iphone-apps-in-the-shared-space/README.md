---
id: "wwdc2023-10090"
event: "wwdc2023"
year: 2023
title: "Run your iPad and iPhone apps in the Shared Space"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10090"
topics: ["Developer Tools", "Essentials", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Run your iPad and iPhone apps in the Shared Space

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10090](https://developer.apple.com/videos/play/wwdc2023/10090)

Discover how you can run your existing iPad and iPhone apps on Vision Pro. Learn how iPadOS and iOS apps operate on this platform, find out about the Designed for iPad experience, and explore the paths available for enhancing your app experience on visionOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,917 words)

## Code Snippets

### Default orientation Info.plist key — [4:37]

```swift
UIPreferredDefaultInterfaceOrientation
```

### Supported orientations Info.plist key — [5:03]

```swift
UISupportedInterfaceOrientations
```

### Required capabilities Info.plist key — [5:13]

```swift
UIRequiredDeviceCapabilities
```

### Look to Dictate enablement — [7:59]

```swift
// SwiftUI
@State private var searchText = ""

var body: some View {
    NavigationStack {
        Text("Query: \(searchText)")
    }
    .searchable(text: $searchText)
    .searchDictationBehavior(.inline(activation: .onLook))
}


// UIKit
let searchController = UISearchController()
searchController.searchBar.isLookToDictateEnabled = true
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10090/4/F9896DEE-8E84-49C1-AEAF-10D7628B2662/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10090/4/F9896DEE-8E84-49C1-AEAF-10D7628B2662/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10090) — developer.apple.com. Indexed for agent consumption._
