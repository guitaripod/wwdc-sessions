---
id: "wwdc2020-10104"
event: "wwdc2020"
year: 2020
title: "Adopt the new look of macOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10104"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["macOS"]
hasTranscript: true
---

# Adopt the new look of macOS

**Event:** WWDC20 · **Topic:** Design · **Platforms:** macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10104](https://developer.apple.com/videos/play/wwdc2020/10104)

Make over your Mac apps: Discover how you can embrace the new design of macOS Big Sur and adopt its visual hierarchy, design patterns, and behaviors. We’ll explore the latest updates to AppKit around structural items and common controls, and show you how you can adapt more customized interfaces with just a bit of adoption work. And find out how you can incorporate custom accent colors and symbols to further personalize your app.

To get the most out of this session, you should be familiar with AppKit and SF Symbols. For additional information on symbols, watch "SF Symbols 2.0”.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,519 words)

## Code Snippets

### Using a monochrome tint for "secondary" sidebar groups — [3:45]

```swift
func outlineView(_ outlineView: NSOutlineView, tintConfigurationForItem item: Any) -> NSTintConfiguration? {
  if case let sectionItem as SectionItem = item {
    /* 
       This outline view uses a type called "SectionItem" to populate its top-level sections.
       Here we choose a tint configuration based on a hypothetical `isSecondarySection` property on that type.
     */
    return sectionItem.isSecondarySection ? .monochrome : .default
  }
  // For all other cases, a return value of `nil` indicates that the item should inherit a tint from its parent.
  return nil
}
```

### Adopting NSSearchToolbarItem — [11:32]

```swift
var searchItem = NSSearchToolbarItem(itemIdentifier: searchIdentifier)
searchItem.searchField = searchField
```

### Creating a split view tracking toolbar item — [13:30]

```swift
var trackingItem = NSTrackingSeparatorToolbarItem(itemIdentifier: identifier,
splitView: splitView,
dividerIndex: 1)
```

### Creating a large push button — [18:39]

```swift
let button = NSButton(title: "Get Started", 
                      target: self, 
                      action: #selector(finishOnboarding(_:)))
button.controlSize = .large
```

### Instantiating a system symbol image — [24:35]

```swift
/* 
  Symbol image names are literal descriptions of the symbol glyph, so we must
  include an accessibility description to provide semantic meaning to the image.
 */
let newFolderImage = NSImage(systemSymbolName: "plus.rectangle.on.folder"
                             accessibilityDescription: "New Folder")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10104/8/2EE89376-B9BB-467A-B0F9-76651B382977/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10104) — developer.apple.com. Indexed for agent consumption._