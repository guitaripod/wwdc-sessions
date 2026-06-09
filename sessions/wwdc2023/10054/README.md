---
id: "wwdc2023-10054"
event: "wwdc2023"
year: 2023
title: "What’s new in AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10054"
topics: ["App Services", "Essentials", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What’s new in AppKit

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10054](https://developer.apple.com/videos/play/wwdc2023/10054)

Discover the latest advances in Mac app development. We’ll share improvements to controls and menus and explore the tools that can help you break free from your (view) bounds. Learn how to add motion to your user interface, take advantage of improvements to text input, and integrate your existing code with Swift and SwiftUI.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,821 words)

## Code Snippets

### Configure NSTableView column customization menu — [1:36]

```swift
func tableView(_ tableView: NSTableView, 
               userCanChangeVisibilityOf column: NSTableColumn) -> Bool {
    return column.identifier != "Name"
}
```

### Configuring NSProgressIndicator to sync with Progress — [1:53]

```swift
func fetchData() {
    let url = URL(string: "https://developer.apple.com/wwdc23/")!
    let task = URLSession.shared.dataTask(with: .init(url: url))
    progressIndicator.observedProgress = task.progress

    task.resume()
}
```

### Adding an inspector to your app — [3:48]

```swift
let inspectorItem = NSSplitViewItem(inspectorWithViewController: inspectorViewController)
splitViewController.addSplitViewItem(inspectorItem)

func toolbarDefaultItemIdentifiers(_ toolbar: NSToolbar) -> [NSToolbarItem.Identifier] {
    [.toggleSidebar, .sidebarTrackingSeparator, .flexibleSpace, .addPlant, 
     .inspectorTrackingSeparator, .flexibleSpace, .toggleInspector]
}
```

### Show a NSPopover relative to a NSToolbarItem — [4:38]

```swift
func toolbarAction(_ toolbarItem: NSToolbarItem) {
    let popover = NSPopover()
    popover.contentViewController = PopoverViewController()
    popover.show(relativeTo: toolbarItem)
}
```

### Adding symbol effects to a image view — [18:30]

```swift
wifiImageView.image = NSImage(systemSymbolName: "wifi", accessibilityDescription: "wifi icon")
wifiImageView.addSymbolEffect(.variableColor.iterative, options: .repeating)
```

### Using @ViewLoading to remove optionality on properties — [24:56]

```swift
class ViewController: NSViewController {
    @ViewLoading var datePicker: NSDatePicker
    var date = Date() {
        didSet {
            datePicker.dateValue = date
        }
    }

    override func loadView() {
        super.loadView()
        datePicker = NSDatePicker()
        datePicker.dateValue = date
        view.addSubview(datePicker)
    }
}
```

### Preview NSView and NSViewController using the Preview macro — [25:26]

```swift
#Preview("Tree Species") {
    let treeCellView = TreeCellView()
    treeCellView.species = .spruce
    return treeCellView
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10054/4/80B02B85-8293-43F0-A6B1-210B6B6DD1F7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10054/4/80B02B85-8293-43F0-A6B1-210B6B6DD1F7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10054) — developer.apple.com. Indexed for agent consumption._