---
id: "wwdc2020-10027"
event: "wwdc2020"
year: 2020
title: "Modern cell configuration"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10027"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Modern cell configuration

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10027](https://developer.apple.com/videos/play/wwdc2020/10027)

Discover new techniques for configuring collection view and table view cells to quickly build dynamic interfaces in your app. Explore configuration types you can use to easily populate cells with content and apply common styles. Take advantage of powerful APIs to customize the appearance of cells for different states. Find out about patterns and best practices that simplify your code, eliminate bugs, and improve performance.

**Keywords:** `collectionview`, `tableview`, `uicollectionview`, `uitableview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,258 words)

## Documentation & Resources

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/implementing-modern-collection-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/implementing-modern-collection-views.json

## Code Snippets

### Configuring a UITableViewCell — [1:31]

```swift
cell.imageView?.image = UIImage(systemName: "star")
cell.textLabel?.text = "Hello WWDC!"
```

### Configuring a UITableViewCell Using a Content Configuration — [1:59]

```swift
var content = cell.defaultContentConfiguration()

content.image = UIImage(systemName: "star")
content.text = "Hello WWDC!"

cell.contentConfiguration = content
```

### Updating Configurations — [13:10]

```swift
let updatedConfiguration = configuration.updated(for: state)
```

### Customizing Appearance for Different States — [16:33]

```swift
override func updateConfiguration(using state: UICellConfigurationState) {
    var content = self.defaultContentConfiguration().updated(for: state)

    content.image = self.item.icon
    content.text = self.item.title

    if state.isHighlighted || state.isSelected {
        content.imageProperties.tintColor = .white
        content.textProperties.color = .white
    }

    self.contentConfiguration = content
}
```

### Default Configurations — [19:45]

```swift
var background = UIBackgroundConfiguration.listSidebarCell()

var content = UIListContentConfiguration.sidebarCell()
```

### Creating a List Content View — [26:23]

```swift
var content = UIListContentConfiguration.cell()

// Set up the content configuration as desired...

let contentView = UIListContentView(configuration: content)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10027/2/8BF22D86-7C86-4813-980B-183CC5B693DE/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10027) — developer.apple.com. Indexed for agent consumption._