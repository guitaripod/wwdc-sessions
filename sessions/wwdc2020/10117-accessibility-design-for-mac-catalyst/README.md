---
id: "wwdc2020-10117"
event: "wwdc2020"
year: 2020
title: "Accessibility design for Mac Catalyst"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10117"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Accessibility design for Mac Catalyst

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10117](https://developer.apple.com/videos/play/wwdc2020/10117)

Make your Mac Catalyst app accessible to all — and bring those improvements back to your iPad app. Discover how a great accessible iPad app automatically becomes a great accessible Mac app when adding support for Mac Catalyst. Learn how to further augment your experience with support for mouse and keyboard actions and accessibility element grouping and navigation. And explore how to use new Accessibility Inspector features to test your app and iterate to create a truly great experience for everyone. To get the most out of this session, you should be familiar with Mac Catalyst, UIKit, and basic accessibility APIs for iOS. To get started, check out “Introducing iPad apps for Mac” and "Auditing your apps for accessibility."

**Keywords:** `accessibility inspector`, `accessibility tree`, `accessible`, `catalyst`, `grouping`, `keyboard shortcuts`, `voiceover`, `voice over`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,612 words)

## Documentation & Resources

- [Accessibility design for Mac Catalyst](https://developer.apple.com/documentation/Accessibility/accessibility_design_for_mac_catalyst) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/accessibility_design_for_mac_catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/accessibility_design_for_mac_catalyst.json
- [Delivering an exceptional accessibility experience](https://developer.apple.com/documentation/Accessibility/delivering_an_exceptional_accessibility_experience) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/delivering_an_exceptional_accessibility_experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/delivering_an_exceptional_accessibility_experience.json

## Code Snippets

### Ensuring selection automatically triggers when focus moves to a different cell — [4:11]

```swift
myTableView.selectionFollowsFocus = true
```

### Creating a keyboard shortcut — [6:01]

```swift
extension AppDelegate {
  override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    let shareCommand = UIKeyCommand(title: NSLocalizedString("Share", comment: ""),
                                    action: #selector(Self.handleShareMenuAction),
                                    input: "I",
                                    modifierFlags: [.command])
    let shareMenu = UIMenu(title: "",
                           identifier: UIMenu.Identifier("com.example.apple-samplecode.RoastedBeans.share"),
                           options: .displayInline,
                           children: [shareCommand])
    builder.insertChild(shareMenu, atEndOfMenu: .edit)
  }

  @objc func handleShareMenuAction() {
  }
}
```

### Responding to raw key codes — [7:20]

```swift
extension MyViewController {
  override func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
    switch presses.first?.key?.keyCode {
    case .keyboardLeftGUI:
      // Handle command key pressed
    case .keyboardB:
      // Handle B key pressed
    default:
    }
  }
}
```

### Adding accessibility labels to containers, such as UITableView and UICollectionView — [15:45]

```swift
tableView.accessibilityLabel = NSLocalizedString("Coffee list", comment: "")
```

### Making great accessibility labels that include state — [15:50]

```swift
extension RBListViewController {

    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let data = tableData[indexPath.row]
        let label = NSLocalizedString("Coffee list", comment: "")
        let selectedLabel = NSLocalizedString("%@ selected", comment: "")
        tableView.accessibilityLabel = label + ", " + String(format: selectedLabel, data.coffee.brand)
    }

}
```

### Adding accessibility containers to improve the navigation experience — [16:45]

```swift
let stackView = UIStackView()
stackView.axis = .vertical
stackView.translatesAutoresizingMaskIntoConstraints = false

let locationsAvailable = viewModel.locationsAvailable

let titleLabel = UILabel()
titleLabel.font = UIFont.preferredFont(forTextStyle: .body).bold()
titleLabel.text = NSLocalizedString("Availability: ", comment: "")
stackView.addArrangedSubview(titleLabel)

for location in locationsAvailable {
  let label = UILabel()
  label.font = UIFont.preferredFont(forTextStyle: .body)
  label.text = "• " + location
  label.accessibilityLabel = location
  stackView.addArrangedSubview(label)
}

stackView.accessibilityLabel = String(format: NSLocalizedString("Available at %@ locations", comment: ""), String(locationsAvailable.count))
stackView.accessibilityContainerType = .semanticGroup
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10117/4/59AF0B72-76C2-4442-8160-967F2A9FDB96/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10117) — developer.apple.com. Indexed for agent consumption._
