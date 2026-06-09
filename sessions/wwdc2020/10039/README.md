---
id: "wwdc2020-10039"
event: "wwdc2020"
year: 2020
title: "Build document-based apps in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10039"
topics: ["Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build document-based apps in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10039](https://developer.apple.com/videos/play/wwdc2020/10039)

Learn how to build a document-based app entirely in SwiftUI! We’ll walk you through the DocumentGroup API and how it composes with your App and Scenes, allowing you to add out-of-the-box support for document management — such as document browsing and standard commands — no heavy lifting required. You’ll learn to set up Universal Type Identifiers as well as gain understanding into what makes a top-notch document-based app.

To get the most out of this session, you should first familiarize yourself with building apps in SwiftUI. Check out "App essentials in SwiftUI" to learn more.

**Keywords:** `document`, `document app`, `document based app`, `document-based apps`, `documentgroup`, `exportedas`, `importedas`, `imported type identifier`, `windowgroup`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,389 words)

## Documentation & Resources

- [DocumentGroup](https://developer.apple.com/documentation/SwiftUI/DocumentGroup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/DocumentGroup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/DocumentGroup.json
- [Uniform Type Identifiers](https://developer.apple.com/documentation/UniformTypeIdentifiers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UniformTypeIdentifiers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UniformTypeIdentifiers.json

## Code Snippets

### DocumentGroup TextEditor — [2:12]

```swift
@main
struct TextEdit: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditor(text: file.$document.text)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10039/3/AB4F8C69-7A45-4CDB-A382-7D749ADB0891/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10039) — developer.apple.com. Indexed for agent consumption._