---
id: "wwdc2022-10094"
event: "wwdc2022"
year: 2022
title: "Add Shared with You to your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10094"
topics: ["App Services", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Add Shared with You to your app

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10094](https://developer.apple.com/videos/play/wwdc2022/10094)

Shared with You helps people easily find content in your app that someone has shared with them in Messages. Learn how you can support Shared with You in your app and continue the messaging experience right with the content. We'll show you how pinning can give implicit Shared with You permission and can elevate content to be automatically shared. We'll also go over how to present Shared with You content in a Shared with You shelf and visually represent shared items with a Shared with You attribution view.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,225 words)

## Code Snippets

### Enumerate Shared with You shelf — [12:06]

```swift
// Enumerate Shared with You shelf

class SharedWithYouViewController: UIViewController, SWHighlightCenterDelegate {
    let highlightCenter = SWHighlightCenter()

    override func viewDidLoad() {
        super.viewDidLoad()
        highlightCenter.delegate = self
    }

    func highlightCenterHighlightsDidChange(_ highlightCenter: SWHighlightCenter) {
        for highlight in highlightCenter.highlights {
            let highlightURL = highlight.url
            // Generate a rich preview for the Highlight
        }
    }
}
```

### Setting appearance of Attribution View — [13:42]

```swift
// Setting appearance of Attribution View

let attributionView = SWAttributionView()
attributionView.highlight = self.highlightCenter.highlights[index]
attributionView.preferredMaxLayoutWidth = maximumWidthForView
```

### Horizontal Alignment for Attribution View — [14:36]

```swift
// Horizontal Alignment for Attribution View

let attributionView = SWAttributionView()
attributionView.highlight = self.highlightCenter.highlights[index]
attributionView.preferredMaxLayoutWidth = maximumWidthForView
attributionView.horizontalAlignment = .leading
```

### Display Context for Attribution View — [15:19]

```swift
// Display Context for Attribution View

let attributionView = SWAttributionView()
attributionView.highlight = self.highlightCenter.highlights[index]
attributionView.preferredMaxLayoutWidth = maximumWidthForView
attributionView.horizontalAlignment = .center
attributionView.displayContext = .summary
```

### Add Shared with You Content Menu to your app’s content — [17:12]

```swift
// Add Shared with You Content Menu to your app’s content

let attributionView = SWAttributionView()
attributionView.highlight = self.highlightCenter.highlights[index]
attributionView.menuTitleForHideAction = "Remove Item"

let contextMenuConfig = UIContextMenuConfiguration(identifier: nil,previewProvider: nil) { [weak self] _ in
        let additionalMenu = attributionView.supplementalMenu
        // Append additionalMenu items to your content’s menu items
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10094/4/6D2459BF-7717-4646-BE9A-E73C7E602DB9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10094/4/6D2459BF-7717-4646-BE9A-E73C7E602DB9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10094) — developer.apple.com. Indexed for agent consumption._