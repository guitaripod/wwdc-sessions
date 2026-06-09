---
id: "wwdc2023-10121"
event: "wwdc2023"
year: 2023
title: "What’s new in CSS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10121"
topics: ["Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# What’s new in CSS

**Event:** WWDC23 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10121](https://developer.apple.com/videos/play/wwdc2023/10121)

Explore the latest advancements in CSS. Learn techniques and best practices for working with wide-gamut color, creating gorgeous typography, and writing simple and robust code. We’ll also peer into the future and preview upcoming layout and typography features.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,127 words)

## Documentation & Resources

- [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/safari/technology-preview/
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/safari-release-notes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json
- [WebKit Open Source Project](https://webkit.org) _guide_
- [Web Inspector Reference](https://webkit.org/web-inspector/) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_
- [MDN Web Docs - Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API) _documentation_

## Code Snippets

### Masonry layout, example 1 — [2:49]

```markdown
main {
	display: grid;
  grid-template-columns: repeat(auto-fill, minmax(14rem, 1fr));
	grid-template-rows: masonry;
}
```

### Masonry layout, example 2 — [3:20]

```markdown
main {
	display: grid;
  grid-template-columns: 1fr 2fr 3fr;
	grid-template-rows: masonry;
}
```

### Masonry layout, example 3 — [3:24]

```markdown
main {
	display: grid;
  grid-template-columns: 10rem 1fr minmax(100px, 300px);
	grid-template-rows: masonry;
}
```

### Margin trim — [5:28]

```markdown
.card {
  background-color: #fcf5e7;
  padding: 2rlh;
  margin-trim: block;
}
h2, p {
  margin: 1rlh 0;
}
```

### Color gamut media query — [7:25]

```markdown
.card {
  background-color: #fcf5e7;
  padding: 2rlh;
  margin-trim: block;
}
h2, p {
  margin: 1rlh 0;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10121/5/583EB542-47B3-45F4-B7D2-35C88ED597C7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10121/5/583EB542-47B3-45F4-B7D2-35C88ED597C7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10121) — developer.apple.com. Indexed for agent consumption._
