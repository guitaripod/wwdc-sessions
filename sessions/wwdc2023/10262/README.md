---
id: "wwdc2023-10262"
event: "wwdc2023"
year: 2023
title: "Rediscover Safari developer features"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10262"
topics: ["Developer Tools", "Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Rediscover Safari developer features

**Event:** WWDC23 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10262](https://developer.apple.com/videos/play/wwdc2023/10262)

Get ready to explore Safari’s rich set of tools for web developers and designers. Learn how you can inspect web content, find out about Responsive Design Mode and WebDriver, and get started with simulators and devices. We’ll also show you how to pair with Vision Pro, make content inspectable in your apps, and use Open with Simulator in Responsive Design Mode to help you test your websites on any device.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,285 words)

## Documentation & Resources

- [Adding a web development tool to Safari Web Inspector](https://developer.apple.com/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector.json
- [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/safari/technology-preview/
- [WebKit Open Source Project](https://webkit.org) _guide_
- [Web Inspector Reference](https://webkit.org/web-inspector/) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### HTML image source set — [6:20]

```xml
<img
  src="astronaut_1x.jpg"
  srcset="astronaut_2x.jpg 2x astronaut_3x.jpg 3x"
/>
```

### CSS image set — [6:27]

```swift
.starfield {
  background-image: image-set("stars_1x.jpg" 1x, "stars_2x.jpg" 2x);
}
```

### CSS resolution media query — [6:32]

```swift
@media (min-resolution: 2dppx) {
  .divider-line {
    border: 0.5px solid grey;
  }
}
```

### Inspectable WKWebViews and JSContexts — [13:41]

```swift
let webConfiguration = WKWebViewConfiguration()
let webView = WKWebView(frame: .zero, configuration: webConfiguration)

if #available(macOS 13.3, iOS 16.4, *) {
  webView.isInspectable = true
}

let jsContext = JSContext()
jsContext?.name = "Context name"

if #available(macOS 13.3, iOS 16.4, tvOS 16.4, *) {
  jsContext?.isInspectable = true
}
```

### WebDriver test — [15:32]

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.options import Options as SafariOptions

options = SafariOptions()
driver = webdriver.Safari(options=options)

driver.get("https://webkit.org/web-inspector/")

search_element = driver.find_element(by=By.ID, value="search")
search_element.send_keys("device")

assert(driver.find_element(by=By.LINK_TEXT, value="Device Settings"))

driver.quit()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10262/4/5A68BE0E-CC0F-4DF7-8982-F315B0ED6A2D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10262/4/5A68BE0E-CC0F-4DF7-8982-F315B0ED6A2D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10262) — developer.apple.com. Indexed for agent consumption._