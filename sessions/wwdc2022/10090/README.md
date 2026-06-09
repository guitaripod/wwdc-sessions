---
id: "wwdc2022-10090"
event: "wwdc2022"
year: 2022
title: "What's new in TextKit and text views"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10090"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in TextKit and text views

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10090](https://developer.apple.com/videos/play/wwdc2022/10090)

Discover the latest updates to TextKit and text views in UI frameworks. Explore layout refinements and API enhancements, learn how you can maintain compatibility across multiple OS versions, and find out how to modernize your app with TextKit 2. 

To get the most out of this session, watch “Meet TextKit 2” from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,134 words)

## Code Snippets

### Check for NSTextLayoutManager first — [13:21]

```swift
if let textLayoutManager = textView.textLayoutManager {
    // TextKit 2 code goes here
}
else {
    let layoutManager = textView.layoutManager    
    // TextKit 1 code goes here
}
```

### Counting number of lines of wrapped text in a text view with TextKit 2 — [17:41]

```swift
// Example: Updating glyph-based code 

var numberOfLines = 0
let textLayoutManager = textView.textLayoutManager

textLayoutManager.enumerateTextLayoutFragments(from:
                                               textLayoutManager.documentRange.location,
                                               options: [.ensuresLayout]) { layoutFragment in
        numberOfLines += layoutFragment.textLineFragments.count
}
```

### Convert NSRange to NSTextRange — [21:10]

```swift
let textContentManager = textLayoutManager.textContentManager

let startLocation = textContentManager.location(textContentManager.documentRange.location, 
                                                offsetBy: nsRange.location)!

let endLocation = textContentManager.location(startLocation, 
                                              offsetBy: nsRange.length)

let nsTextRange = NSTextRange(location: startLocation, end: endLocation)
```

### Convert NSTextRange to NSRange — [21:40]

```swift
let textContentManager = textLayoutManager.textContentManager

let location = textContentManager.offset(from: textContentManager.documentRange.location,
                                         to: nsTextRange!.location)

let length = textContentManager.offset(from: nsTextRange!.location,
                                       to: nsTextRange!.endLocation)

let nsRange = NSRange(location: location, length: length)
```

### Convert UITextRange to NSTextRange — [22:02]

```swift
let offset = textView.offset(from: textview.beginningOfDocument, to: uiTextRange.start)

let startLocation = textContentManager.location(textContentManager.documentRange.location, 
                                                offsetBy: offset)!

let nsTextRange = NSTextRange(location: startLocation)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10090/4/5A0AE4B4-BE39-434E-8B9E-0910F2FD152D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10090/4/5A0AE4B4-BE39-434E-8B9E-0910F2FD152D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10090) — developer.apple.com. Indexed for agent consumption._