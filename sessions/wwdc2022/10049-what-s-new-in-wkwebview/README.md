---
id: "wwdc2022-10049"
event: "wwdc2022"
year: 2022
title: "What's new in WKWebView"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10049"
topics: ["Essentials", "Safari & Web", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in WKWebView

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10049](https://developer.apple.com/videos/play/wwdc2022/10049)

Explore the latest updates to WKWebView, our framework for incorporating web content into your app’s interface. We’ll show you how to use the JavaScript fullscreen API, explore CSS viewport units, and learn more about find interactions. We’ll also take you through refinements to content blocking controls, embedding encrypted media, and using the Web Inspector.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,171 words)

## Documentation & Resources

- [Introduction to WebKit Content Blockers](https://webkit.org/blog/3476/content-blockers-first-look/) _documentation_
- [SFSafariViewController](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/SFSafariViewController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/SFSafariViewController.json
- [WebKit Open Source Project](https://webkit.org) _guide_
- [WebKit](https://developer.apple.com/documentation/WebKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WebKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WebKit.json

## Code Snippets

### Fullscreen API support — [2:26]

```swift
webView.configuration.preferences.isElementFullscreenEnabled = true

webView.loadHTMLString("""
<script>
    button.addEventListener('click', () => {
        canvas.webkitRequestFullscreen()
    }, false);
</script>
…
""", baseURL:nil)

let observation = webView.observe(\.fullscreenState, options: [.new]) { object, change in
    print("fullscreenState: \(object.fullscreenState)")
}
```

### CSS viewport unit range inputs — [3:50]

```swift
let minimum = UIEdgeInsets(top: 0, left: 0, bottom: 30, right: 0)
let maximum = UIEdgeInsets(top: 0, left: 0, bottom: 200, right: 0)
webView.setMinimumViewportInset(minimum, maximumViewportInset: maximum)
```

### Using UIFindInteraction with WKWebView — [4:17]

```swift
webView.findInteractionEnabled = true

if let interaction = webView.findInteraction {
  interaction.presentFindNavigator(showingReplace:false)
}
```

### WKContentRuleList if-frame-url — [5:46]

```swift
let json = """
[{
    "action":{"type":"block"},
    "trigger":{
        "resource-type":["image"],
        "url-filter":".*",
        "if-frame-url":["https?://([^/]*\\\\.)wikipedia.org/"]
    }
}]
"""

WKContentRuleListStore.default().compileContentRuleList(forIdentifier: "example_blocker",
    encodedContentRuleList: json) { list, error in
    guard let list = list else { return }
    let configuration = WKWebViewConfiguration()
    configuration.userContentController.add(list)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10049/3/47260DC4-814E-466D-AD96-D29DFC5459BA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10049/3/47260DC4-814E-466D-AD96-D29DFC5459BA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10049) — developer.apple.com. Indexed for agent consumption._
