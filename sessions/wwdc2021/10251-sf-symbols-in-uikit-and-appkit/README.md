---
id: "wwdc2021-10251"
event: "wwdc2021"
year: 2021
title: "SF Symbols in UIKit and AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10251"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# SF Symbols in UIKit and AppKit

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10251](https://developer.apple.com/videos/play/wwdc2021/10251)

Learn how you can create colorized symbols with SF Symbols 3 and customize them to match the visual design of your app’s interface. We’ll take you through the latest UIKit and AppKit APIs for integrating colorized symbols, as well as best practices for implementation. To get the most out of this session, we recommend watching “Introducing SF Symbols” from WWDC19.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,556 words)

## Documentation & Resources

- [Download SF Symbols](https://developer.apple.com/sf-symbols/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sf-symbols/
- [Human Interface Guidelines: SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/sf-symbols

## Code Snippets

### Monochrome symbols — [1:52]

```swift
// Play

let playImage = UIImage(systemName: "play")

playImageView.image = playImage 
playImageView.tintColor = .systemBlue
```

### Hierarchical symbols — [3:00]

```swift
// Device image

var image = NSImage(systemSymbolName: "ipad.landscape",
                    accessibilityDescription: "iPad")

let config = NSImage.SymbolConfiguration(hierarchicalColor: .label)

deviceView.image = image
deviceView.symbolConfiguration = config
```

### Setup button configurations — [4:13]

```swift
// Initialize button configuration

let speakerConfig = UIButtonConfiguration.plain
speakerConfig.image = UIImage(systemName: "speaker.wave.2")

let callConfig = UIButtonConfiguration.plain
callConfig.image = UIImage(systemName: "phone")

let deleteConfig = UIButtonConfiguration.plain
deleteConfig.image = UIImage(systemName: "trash")
```

### Image variants — [4:40]

```swift
// Button container view

actionsView.imageVariant = .none
```

### Image variants — [4:44]

```swift
// Button container view

actionsView.imageVariant = .circle
```

### Image variants — [4:51]

```swift
// Button container view

actionsView.imageVariant = .circle.fill
```

### Speaker button color configuration — [5:09]

```swift
// Speaker button color configuration

let config = UIImage.SymbolConfiguration(paletteColors: [.tintColor, .systemGray2])

speakerConfig.preferredSymbolConfigurationForImage = config
speakerButton.configuration = speakerConfig
```

### Call button color configuration — [5:40]

```swift
// Call button color configuration

let config = UIImage.SymbolConfiguration(paletteColors: [.white, .tintColor])

callConfig.preferredSymbolConfigurationForImage = config
callButton.configuration = callConfig
```

### Delete button color configuration — [5:56]

```swift
// Delete button color configuration

let config = UIImage.SymbolConfiguration(paletteColors: [.white, .systemRed])

deleteConfig.preferredSymbolConfigurationForImage = config
deleteButton.configuration = deleteConfig
```

### Colors matter — [6:10]

```swift
// Colors matter!

let config = UIImage.SymbolConfiguration(paletteColors: [.tintColor, .systemGray2])

let config = UIImage.SymbolConfiguration(paletteColors: [.white, .tintColor])

let config = UIImage.SymbolConfiguration(paletteColors: [.white, .systemRed])
```

### Tint color — [6:46]

```swift
view.backgroundColor = .tintColor
label.textColor = .tintColor
searchField.tokenBackgroundColor = .tintColor
tabBarItem.badgeColor = .tintColor
```

### Multicolor symbols — [9:03]

```swift
// configure table view cell

let image = UIImage(systemName: category.iconName)

cell.imageView.image = image
```

### Multicolor symbols — [9:13]

```swift
// configure table view cell

let image = UIImage(systemName: category.iconName)

let config = UIImage.SymbolConfiguration.preferringMultiColor

let tintColor = category.colorForIcon

cell.imageView.image = image
cell.imageView.preferredSymbolConfiguration = config
cell.imageView.tintColor = tintColor
```

### Multicolor symbols — [9:58]

```swift
// configure table view cell

let image = UIImage(systemName: category.iconName)

let config = UIImage.SymbolConfiguration.preferringMultiColor

let tintColor = category.colorForIcon

cell.imageView.image = image
cell.imageView.preferredSymbolConfiguration = config
cell.imageView.tintColor = tintColor
```

### Combining configurations — [12:25]

```swift
// combined configuration

let image = UIImage(systemImage: "ipad.and.iphone")
headerView.image = image
```

### Combining configurations — [12:40]

```swift
// Combined configuration

let image = UIImage(systemImage: "ipad.and.iphone")
headerView.image = image

let fontConfig = UIImage.SymbolConfiguration(pointSize: 60, scale: .large)
let colorConfig = UIImage.SymbolConfiguration(hierarchicalColor: .systemBlue)
let config = fontConfig.applying(colorConfig)

headerView.preferredSymbolConfiguration = config
```

### Symbols in attributed strings — [13:20]

```swift
// Hotel amenities

let amenitiesString = NSMutableAttributedString(...)

if (room.amenities.contains(.tv)) {
    let config = UIImage.SymbolConfiguration(
                         hierarchicalColor: .systemGreen)
    let tvImage = UIImage(systemImage: "tv", 
                          withConfiguration: config)

    let attachment = NSTextAttachment(image: tvImage)
    let attachmentString = NSAttributedString(attachment: 
                                               attachment)
    let tvString = attachmentString.mutableCopy()
    tvString.append(NSAttributedString(" TV, ")

    amenitiesString.append(tvString)
}
```

### Symbols in attributed strings — [13:51]

```swift
// hotel amenities

let amenitiesLabel = UILabel()

amenitiesLabel.textColor = .systemGreen
amenitiesLabel.font = UIFont.systemFont(ofSize: 25)

amenitiesLabel.attributedString = amenitiesString
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10251/8/1F3B1961-5626-4737-BFCB-442B8F6A6CC3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10251/8/1F3B1961-5626-4737-BFCB-442B8F6A6CC3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10251) — developer.apple.com. Indexed for agent consumption._
