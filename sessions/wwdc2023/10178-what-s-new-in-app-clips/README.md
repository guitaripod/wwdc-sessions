---
id: "wwdc2023-10178"
event: "wwdc2023"
year: 2023
title: "What’s new in App Clips"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10178"
topics: ["App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What’s new in App Clips

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10178](https://developer.apple.com/videos/play/wwdc2023/10178)

Explore the latest updates to App Clips. We’ll show you how to build App Clips more easily using default App Clip links. Learn how you can take advantage of the increased App Clip size limit to build richer and more engaging experiences, and find out how you can launch App Clips directly from your app.

**Keywords:** `app`, `app clip`, `app clip code`, `clip`, `download`, `experience`, `in app`, `in-app`, `install`, `launch`, `launch app clip`, `lightweight`, `preview`, `qr code`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,017 words)

## Documentation & Resources

- [App Clips](https://developer.apple.com/documentation/AppClip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip.json
- [Human Interface Guidelines: App Clips](https://developer.apple.com/design/human-interface-guidelines/app-clips) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/app-clips

## Code Snippets

### Parsing URL parameters as components — [3:53]

```swift
ContentView(parameters: $parameters)
    .onContinueUserActivity(NSUserActivityTypeBrowsingWeb, perform: { userActivity in
        guard let inputURL = userActivity.webpageURL else {
            return
        }

        let components = NSURLComponents(url: inputURL, resolvingAgainstBaseURL: true)
        guard let parameters = components?.queryItems else {
            return
        }

        self.parameters = parameters
    }
```

### Providing metadata to an LPLinkView — [4:39]

```swift
let provider = LPMetadataProvider()

provider.startFetchingMetadata(for: url) { (metadata, error) in
    guard let metadata = metadata else {
        return
    }

    DispatchQueue.main.async {
        lpView.metadata = metadata
    }
}
```

### Launching App Clips from a SwiftUI app — [5:00]

```swift
var body: some View {
    let appClipURL = URL(
        string: "https://appclip.apple.com/id?p=com.example.naturelab.backyardbirds.Clip"
    )!

    Link("Backyard Birds", destination: appClipURL)
}
```

### Launching App Clips with UIApplication — [5:11]

```swift
func launchAppClip() {
    let appClipURL = URL(
        string: "https://appclip.apple.com/id?p=com.example.naturelab.backyardbirds.Clip"
    )!

    UIApplication.shared.open(appClipURL)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10178/4/9DD6B041-9DA7-4F78-82A1-B2E17AFA61CB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10178/4/9DD6B041-9DA7-4F78-82A1-B2E17AFA61CB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10178) — developer.apple.com. Indexed for agent consumption._
