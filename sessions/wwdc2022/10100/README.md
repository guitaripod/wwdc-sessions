---
id: "wwdc2022-10100"
event: "wwdc2022"
year: 2022
title: "Create Safari Web Inspector Extensions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10100"
topics: ["Safari & Web"]
platforms: ["macOS"]
hasTranscript: true
---

# Create Safari Web Inspector Extensions

**Event:** WWDC22 · **Topic:** Safari & Web · **Platforms:** macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10100](https://developer.apple.com/videos/play/wwdc2022/10100)

Learn how to add your own tools directly into Web Inspector using the latest Web Extensions APIs. We'll show you how to create your own tab in Web Inspector, evaluate JavaScript in the inspected page, and use the result to help you troubleshoot and identify potential problems.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,642 words)

## Documentation & Resources

- [Adding a web development tool to Safari Web Inspector](https://developer.apple.com/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/adding-a-web-development-tool-to-safari-web-inspector.json
- [Web Inspector Reference](https://webkit.org/web-inspector/) _documentation_
- [Learn more about bug reporting](https://developer.apple.com/bug-reporting/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/bug-reporting/
- [MDN Web Docs - Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API) _documentation_
- [Safari web extensions](https://developer.apple.com/documentation/SafariServices/safari-web-extensions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/safari-web-extensions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/safari-web-extensions.json

## Code Snippets

### Evaluating scripts inside the inspected page — [12:11]

```swift
// Evaluating scripts inside the inspected page

let result = await browser.devtools.inspectedWindow.eval("foo.bar()");
```

### Evaluating scripts inside a frame in the inspected page — [12:40]

```javascript
// Evaluating scripts inside a frame in the inspected page

let result = await browser.devtools.inspectedWindow.eval("foo.bar()", {
    frameURL: "http://example.com/",
});
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10100/8/7E160FF7-856D-4B6E-BE75-633EF8C15CA5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10100/8/7E160FF7-856D-4B6E-BE75-633EF8C15CA5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10100) — developer.apple.com. Indexed for agent consumption._