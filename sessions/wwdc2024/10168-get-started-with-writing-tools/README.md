---
id: "wwdc2024-10168"
event: "wwdc2024"
year: 2024
title: "Get started with Writing Tools"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10168"
topics: ["AI & Machine Learning", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Get started with Writing Tools

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10168](https://developer.apple.com/videos/play/wwdc2024/10168)

Learn how Writing Tools help users proofread, rewrite, and transform text in your app. Get the details on how Writing Tools interact with your app so users can refine what they have written in any text view. Understand how text is retrieved and processed, and how to support Writing Tools in custom text views.

**Keywords:** `nsservices`, `nstextview`, `textkit`, `uitextview`, `wkwebview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,714 words)

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

### Text view delegate methods for Writing Tools — [5:28]

```swift
func textViewWritingToolsWillBegin(_ textView: UITextView) {
    // Take necessary steps to prepare. For example, disable iCloud sync.
}

func textViewWritingToolsDidEnd(_ textView: UITextView) {
    // Take necessary steps to recover. For example, reenable iCloud sync.
}

if !textView.isWritingToolsActive {
    // Do work that needs to be avoided when Writing Tools is interacting with text view
    // For example, in the textViewDidChange callback, app may want to avoid certain things
       when Writing Tools is active
}
```

### Opt-out of the full experience — [7:11]

```swift
textView.writingToolsBehavior = .limited

textView.writingToolsBehavior = .none
```

### Specify accepted text formats — [7:31]

```swift
textView.writingToolsAllowedInputOptions = [.plainText]

textView.writingToolsAllowedInputOptions = [.plainText, .richText, .table]
```

### WKWebView — [7:55]

```swift
// For `WKWebView`, the `default` behavior is equivalent to `.limited`

extension WKWebViewConfiguration {
    @available(iOS 18.0, *)
    open var writingToolsBehavior: UIWritingToolsBehavior { get set }
}

extension WKWebViewConfiguration {
    @available(macOS 15.0, *)
    open var writingToolsBehavior: NSWritingToolsBehavior { get set }
}

extension WKWebView {
    /// @discussion If the Writing Tools behavior on the configuration is `.limited`, this will always be `false`.
    @available(iOS 18.0, macOS 15.0, *)
    open var isWritingToolsActive: Bool { get }
}
```

### Protecting ranges — [8:48]

```swift
// Returned `NSRange`s are relative to the substring of the textView’s textStorage from `enclosingRange`
func textView(_ textView: UITextView, writingToolsIgnoredRangesIn
        enclosingRange: NSRange) -> [NSRange] {
    let text = textView.textStorage.attributedSubstring(from: enclosingRange)
    return rangesInappropriateForWritingTools(in: text)
}
```

### Indicate your text view supports editing — [9:58]

```swift
protocol UITextInput {
    @available(iOS 18.0, macOS 15.0, *)
    optional var isEditable: Bool { get }
}
```

### Simple view that supports Copy — [10:58]

```swift
class CustomTextView: NSView, NSServicesMenuRequestor {
    required init?(coder: NSCoder) {
        super.init(coder: coder)

        self.menu = NSMenu()
        self.menu?.addItem(NSMenuItem(title: "Custom Text View", action: nil,
            keyEquivalent: ""))
        self.menu?.addItem(NSMenuItem(title: "Copy", action: #selector(copy(_:)), 
            keyEquivalent: ""))
    }

    override func draw(_ dirtyRect: NSRect) {
        super.draw(dirtyRect)

        // Custom text drawing code...
    }
}
```

### View extension to support Writing Tools — [11:05]

```swift
class CustomTextView: NSView, NSServicesMenuRequestor {
    override func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, 
                                 returnType: NSPasteboard.PasteboardType?) -> Any? {
        if sendType == .string || sendType == .rtf {
            return self
        }
        return super.validRequestor(forSendType: sendType, returnType: returnType)
    }

    nonisolated func writeSelection(to pboard: NSPasteboard,
                                    types: [NSPasteboard.PasteboardType]) -> Bool {
        // Write plain text and/or rich text to pasteboard
        return true
    }

    // Implement readSelection(from pboard: NSPasteboard)
       as well for editable view
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10168/4/D8EBB581-CA62-4601-A3DF-BCF4C7805EBE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10168/4/D8EBB581-CA62-4601-A3DF-BCF4C7805EBE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10168) — developer.apple.com. Indexed for agent consumption._
