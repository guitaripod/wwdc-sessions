---
id: "wwdc2023-10138"
event: "wwdc2023"
year: 2023
title: "Design and build apps for watchOS 10"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10138"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["watchOS"]
hasTranscript: true
---

# Design and build apps for watchOS 10

**Event:** WWDC23 · **Topic:** Design · **Platforms:** watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10138](https://developer.apple.com/videos/play/wwdc2023/10138)

Dive into the details of watchOS design principles and learn how to apply them in your app using SwiftUI. We’ll show you how to build an app for the redesigned user interface to surface timely information, communicate focused content at a glance, and make navigation consistent and predictable.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,687 words)

## Documentation & Resources

- [Human Interface Guidelines: watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-watchos
- [Apple Design Resources](https://developer.apple.com/design/resources/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/design/resources/

## Code Snippets

### Dial Based View — [13:26]

```swift
// This is an example of using scene padding to position a Circle according
// to the Dial layout grid
struct DialBasedView: View {
    var body: some View {
        ZStack {
            // Add a view to make the ZStack fill the available width, allowing the
            // Circle to position correctly. As an example, we use a rectangle.
            Rectangle()
                .foregroundStyle(Color.clear)

            // Use .scenePadding(.horizontal) on the dial to get the correct
            // width. In a ZStack with centered alignment, it is correctly
            // positioned.
            Circle()
                .foregroundStyle(Color.red)
                .scenePadding(.horizontal)
        }
        // Ignore vertical safe areas to allow the view to draw into the bottom
        // safe areas. This achieves the centering for the dial.
        .edgesIgnoringSafeArea(.vertical)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10138/4/AFF87063-B0C4-49E6-A866-D89017622393/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10138/4/AFF87063-B0C4-49E6-A866-D89017622393/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10138) — developer.apple.com. Indexed for agent consumption._
