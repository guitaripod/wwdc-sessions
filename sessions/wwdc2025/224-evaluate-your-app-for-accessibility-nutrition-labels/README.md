---
id: "wwdc2025-224"
event: "wwdc2025"
year: 2025
title: "Evaluate your app for Accessibility Nutrition Labels"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/224"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Evaluate your app for Accessibility Nutrition Labels

**Event:** WWDC25 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-224](https://developer.apple.com/videos/play/wwdc2025/224)

Use Accessibility Nutrition Labels on your App Store product page to highlight the accessibility features supported by your app. You’ll learn how to evaluate your app’s accessibility features — such as VoiceOver, Larger Text, Captions, and more — and choose accurate and informative Accessibility Nutrition Labels. You’ll also find out how to approach accessibility throughout the design phase.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,698 words)

## Documentation & Resources

- [Overview of Accessibility Nutrition Labels](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels
- [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility
- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json

## Code Snippets

### Add an accessibility label — [13:07]

```swift
// Add an accessibility label

import SwiftUI

struct LandmarkDetailView: View {
  @Environment(ModelData.self) var modelData
  let landmark: Landmark

  var body: some View {
    @Bindable var modelData = modelData
    DetailContentView()
      .toolbar {
        ToolbarItemGroup {
          Button {
          } label: {
            Image(systemName: "square.arrow.up")
          }
					.accessibilityLabel("Share")
        }
      }
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/224/5/da32cbb0-5f05-4589-8055-fe7a473056e9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/224/5/da32cbb0-5f05-4589-8055-fe7a473056e9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/224) — developer.apple.com. Indexed for agent consumption._
