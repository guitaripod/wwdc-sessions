---
id: "wwdc2021-10052"
event: "wwdc2021"
year: 2021
title: "What's new in Mac Catalyst"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10052"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# What's new in Mac Catalyst

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10052](https://developer.apple.com/videos/play/wwdc2021/10052)

Discover the latest updates to Mac Catalyst and find out how you can make your app feel even more at home on macOS. Learn about a variety of new and enhanced UIKit APIs that let you customize your Mac Catalyst app to take advantage of behaviors unique to macOS. To get the most out of this session, we recommend a basic familiarity with Mac Catalyst. Check out “Introducing iPad Apps for Mac” from WWDC19 to acquaint yourself. For more on refining your Mac Catalyst app, watch “Optimize the interface of your Mac Catalyst app” from WWDC20.

**Keywords:** `apple silicon`, `catalyst`, `ios`, `ipad`, `iphone`, `m1`, `macos`, `silicon`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,717 words)

## Documentation & Resources

- [Building and improving your app with Mac Catalyst](https://developer.apple.com/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst.json
- [Bring an iPad App to the Mac with Mac Catalyst](https://developer.apple.com/tutorials/Mac-Catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/tutorials/Mac-Catalyst
- [Human Interface Guidelines: Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/mac-catalyst
- [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/mac-catalyst.json

## Code Snippets

### Push Button — [2:26]

```swift
let button = UIButton(type: .system)
```

### Toggle Button — [2:29]

```swift
let button = UIButton(type: .system)
button.changesSelectionAsPrimaryAction = true
```

### Pull-down Menu — [2:40]

```swift
let button = UIButton(type: .system)
button.menu = UIMenu()
button.showsMenuAsPrimaryAction = true
```

### Pop-up Button — [2:48]

```swift
let button = UIButton(type: .system)
button.menu = UIMenu()
button.showsMenuAsPrimaryAction = true
button.changesSelectionAsPrimaryAction = true
```

### UIToolTipInteraction — [3:50]

```swift
let toolTipInteraction = UIToolTipInteraction(defaultToolTip: string)
view.addInteraction(tooltipInteraction)
```

### UIControl ToopTip — [4:06]

```swift
control.toolTip = "Enable updates"
```

### ToolTips: UILabel — [4:44]

```swift
label.showsExpansionTextWhenTruncated = true
```

### Printing APIs — [4:52]

```xml
<key>UIApplicationSupportsPrintCommand</key>
</true>
```

### Print Support — [5:44]

```swift
func printContent(_ sender: Any?) {
    let printInteractionController = UIPrintInteractionController.shared
    ...
}
```

### Window Subtitle — [6:01]

```swift
scene.subtitle = "My subtitle"
```

### Behavioral Style — [7:34]

```swift
let button = UIButton(configuration: config)
button.preferredBehavioralStyle = .pad
```

### Window Tab Opt-Out — [7:43]

```xml
<key>UIApplicationSceneManifest</key>
	<dict>
		<key>UIApplicationSupportsMultipleScenes</key>
		<true/>
		<key>UIApplicationSupportsTabbedSceneCollection</key>
		<false/>
	</dict>
```

### UIPointerShape — [8:23]

```swift
UIPointerShape.beam(preferredLength:0 axis: .horizontal)
UIPointerShape.beam(preferredLength:0 axis: .vertical)
```

### Hidden Cursor — [8:33]

```swift
UIPointerStyle.hidden
```

### Scene subtitles — [13:25]

```swift
let subtitle: String = "..."
let scene: UIScene = ...
scene.subtitle = subtitle
```

### ToolTips — [14:54]

```swift
// ToolTip Interaction
let imageView: UIImageView = UIImageView(frame: .zero)
let interaction = UIToolTipInteraction(defaultToolTip: "...")
imageView.addInteraction(interaction)

// ToolTips - Label Expansion Text
let label: UILabel = UILabel()
label.text = "..."
label.showsExpansionTextWhenTruncated = true

// ToolTips — On UIControls
let switchControl = UISwitch()
switchControl.toolTip = "..."
```

### Primary button — [17:49]

```swift
let submitButton = UIButton(type: .system)
submitButton.role = .primary
submitButton.setTitle("Submit", for: .normal)
```

### Toggle button with menu — [18:06]

```swift
// Toggle button with menu
let toggleButton = UIButton(configuration: .filled(), primaryAction: nil)
toggleButton.configuration?.title = "Points Multiplier"
toggleButton.changesSelectionAsPrimaryAction = true
toggleButton.menu = ...

// Elsewhere...
toggleButton.configuration?.baseBackgroundColor = .systemRed
```

### Plain, destructive button — [19:09]

```swift
let resetButton = UIButton(configuration: .plain(), primaryAction: nil)
resetButton.configuration?.title = "Reset"
resetButton.role = .destructive
resetButton.tintColor = .systemRed
```

### Pop-up button — [19:36]

```swift
let popup = UIButton(type: .system)
popup.changesSelectionAsPrimaryAction = true
popup.showsMenuAsPrimaryAction = true
popup.menu = ...
```

### iPad behavioral style toggle — [21:01]

```swift
let button = UIButton(configuration: .filled(), primaryAction: nil)
button.configuration?.image = UIImage(systemName: "leaf")
button.preferredBehavioralStyle = .pad
button.configuration?.preferredSymbolConfigurationForImage =   
    UIImage.SymbolConfiguration(pointSize: 60)
button.changesSelectionAsPrimaryAction = true
button.configurationUpdateHandler = colorUpdateHandler
```

### Printing — [24:21]

```swift
override func printContent(_: Any?) {
    ...
}

override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
    if action == #selector(self.printContent(_:)) {
        ...
    } else {
        return super.canPerformAction(action, withSender: sender)
    }
}

override func target(forAction action: Selector, withSender sender: Any?) -> Any? {
    switch action {
    case #selector(UIResponder.printContent(_:)):
        ...
    default:
        return super.target(forAction: action, withSender: sender)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10052/3/AEC7031C-E8E6-4F09-B845-F0DE96310C4D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10052/3/AEC7031C-E8E6-4F09-B845-F0DE96310C4D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10052) — developer.apple.com. Indexed for agent consumption._
