---
id: "wwdc2024-10220"
event: "wwdc2024"
year: 2024
title: "Bring expression to your app with Genmoji"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10220"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Bring expression to your app with Genmoji

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10220](https://developer.apple.com/videos/play/wwdc2024/10220)

Discover how to bring Genmoji to life in your app. We’ll go over how to render, store, and communicate text that includes Genmoji. If your app features a custom text engine, we’ll also cover techniques for adding support for Genmoji.

**Keywords:** `😀`, `animoji`, `emoji`, `memoji`, `nsadaptiveimageglyph`, `nstextview`, `stickers`, `textkit`, `uitextview`, `wkwebview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,541 words)

## Documentation & Resources

- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WebKit/WKWebView
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WebKit/WKWebView.json
- [AppKit](https://developer.apple.com/documentation/AppKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit.json
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Enable support for NSAdaptiveImageGlyph in a UITextView — [3:30]

```swift
let textView = UITextView()
    textView.supportsAdaptiveImageGlyph = true
```

### Read and write attributed string for serialization — [4:41]

```swift
// Extract contents of text view as an attributed string
let textContents = textView.textStorage

// Serialize as data for storage or transport
let rtfData = try textContents.data(from: NSRange(location: 0, length: textContents.length),
              documentAttributes: [.documentType: NSAttributedString.DocumentType.rtfd])


// Create attributed string from serialized data
let textFromData = try NSAttributedString(data: rtfData, documentAttributes: nil)

// Set on text view
textView.textStorage.setAttributedString(textFromData)
```

### Decompose and recompose an attributed string — [6:08]

```swift
// Decompose an attributed string

func decomposeAttributedString(_ attrStr: NSAttributedString) -> (String, [(NSRange, String)], [String: Data]) {
    let string = attrStr.string
    var imageRanges: [(NSRange, String)] = []
    var imageData: [String: Data] = [:]
    attrStr.enumerateAttribute(.adaptiveImageGlyph, in: NSMakeRange(0, attrStr.length)) { (value, range, stop) in
        if let glyph = value as? NSAdaptiveImageGlyph {
            let id = glyph.contentIdentifier
            imageRanges.append((range, id))
            if imageData[id] == nil {
                imageData[id] = glyph.imageContent
            }
        }
    }
    return (string, imageRanges, imageData)
}

// Recompose an attributed string

func recomposeAttributedString(string: String, imageRanges: [(NSRange, String)], imageData: [String: Data]) -> NSAttributedString {
    let attrStr: NSMutableAttributedString = .init(string: string)
    var images: [String: NSAdaptiveImageGlyph] = [:]
    for (id, data) in imageData {
        images[id] = NSAdaptiveImageGlyph(imageContent: data)
    }
    for (range, id) in imageRanges {
        attrStr.addAttribute(.adaptiveImageGlyph, value: images[id]!, range: range)
    }
    return attrStr
}
```

### Convert NSAttributedString to HTML — [6:30]

```swift
// Converting NSAttributedString to HTML

let htmlData = try textContent.data(from: NSRange(location: 0, length: textContent.length),
               documentAttributes: [.documentType: NSAttributedString.DocumentType.html])
```

### Support Genmoji in communication notifications — [7:33]

```swift
func didReceive(_ request: UNNotificationRequest,
      withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {

  ...
  let message: NSAttributedString = _myAttributedMessageStringWithGlyph
  let context = UNNotificationAttributedMessageContext(sendMessageIntent: sendMessageIntent,
                                                       attributedContent: _message)    

  do {
    let messageContent = try request.content.updating(from: context)
    contentHandler(messageContent)
  } catch {
    // Handle error
  }
}
```

### Render NSAdaptiveImageGlyph in custom typesetting solution — [9:45]

```swift
// Find typographic bounds for image in NSAdaptiveImageGlyph

let provider = adaptiveImageGlyph

let bounds = CTFontGetTypographicBoundsForAdaptiveImageProvider(font, provider)

// Draw it at the typographic origin point on the baseline

CTFontDrawImageFromAdaptiveImageProviderAtPoint(font, provider, point, context)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10220/5/66D08ED4-B7A1-415E-AB43-79704F82CE41/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10220/5/66D08ED4-B7A1-415E-AB43-79704F82CE41/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10220) — developer.apple.com. Indexed for agent consumption._
