---
id: "wwdc2022-10070"
event: "wwdc2022"
year: 2022
title: "Build a desktop-class iPad app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10070"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build a desktop-class iPad app

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10070](https://developer.apple.com/videos/play/wwdc2022/10070)

Discover how you can create iPad apps that take advantage of desktop class features. Join Mohammed from the UIKit team as we explore the latest navigation, collection view, menu, and editing APIs and learn best practices for building powerful iPad apps. Code along with this session in real time or download our sample app to use as a reference for updating your own code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,760 words)

## Documentation & Resources

- [collectionView(_:performPrimaryActionForItemAt:)](https://developer.apple.com/documentation/UIKit/UICollectionViewDelegate/collectionView(_:performPrimaryActionForItemAt:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UICollectionViewDelegate/collectionView(_:performPrimaryActionForItemAt:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UICollectionViewDelegate/collectionView(_:performPrimaryActionForItemAt:).json
- [titleMenuProvider](https://developer.apple.com/documentation/UIKit/UINavigationItem/titleMenuProvider) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/titleMenuProvider
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/titleMenuProvider.json
- [UINavigationItem.ItemStyle](https://developer.apple.com/documentation/UIKit/UINavigationItem/ItemStyle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/ItemStyle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/ItemStyle.json
- [collectionView(_:contextMenuConfigurationForItemsAt:point:)](https://developer.apple.com/documentation/UIKit/UICollectionViewDelegate/collectionView(_:contextMenuConfigurationForItemsAt:point:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UICollectionViewDelegate/collectionView(_:contextMenuConfigurationForItemsAt:point:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UICollectionViewDelegate/collectionView(_:contextMenuConfigurationForItemsAt:point:).json
- [centerItemGroups](https://developer.apple.com/documentation/UIKit/UINavigationItem/centerItemGroups) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/centerItemGroups
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/centerItemGroups.json
- [UINavigationItemRenameDelegate](https://developer.apple.com/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws.json
- [UIDocumentProperties](https://developer.apple.com/documentation/UIKit/UIDocumentProperties) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIDocumentProperties
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIDocumentProperties.json
- [Building a desktop-class iPad app](https://developer.apple.com/documentation/UIKit/building-a-desktop-class-ipad-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-a-desktop-class-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-a-desktop-class-ipad-app.json
- [Supporting desktop-class features in your iPad app](https://developer.apple.com/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app.json

## Code Snippets

### Enable UINavigationBar editor style. — [3:36]

```swift
navigationItem.style = .editor
```

### Set a back action. — [3:52]

```swift
navigationItem.backAction = UIAction(…)
```

### Create a document properties header. — [4:48]

```swift
let properties = UIDocumentProperties(url: document.fileURL)

if let itemProvider = NSItemProvider(contentsOf: document.fileURL) {
    properties.dragItemsProvider = { _ in
        [UIDragItem(itemProvider: itemProvider)]
    }
    properties.activityViewControllerProvider = {
        UIActivityViewController(activityItems: [itemProvider], applicationActivities: nil)
    }
}

navigationItem.documentProperties = properties
```

### Adopt rename title menu action and rename UI — [6:36]

```swift
override func viewDidLoad() {
    navigationItem.renameDelegate = self
}

func navigationItem(_ navigationItem: UINavigationItem, didEndRenamingWith title: String) {
    // Rename document using methods appropriate to the app’s data model
}
```

### Adopt system provided title menu actions. — [7:09]

```swift
override func duplicate(_ sender: Any?) {
    // Duplicate document
}

override func move(_ sender: Any?) {
    // Move document
}

func didOpenDocument() {
    ...
    navigationItem.titleMenuProvider = { [unowned self] suggested in
        var children = suggested

        ...

        return UIMenu(children: children)
    }
}
```

### Add custom title menu actions — [7:10]

```swift
func didOpenDocument() {
    ...
    navigationItem.titleMenuProvider = { [unowned self] suggested in
        var children = suggested
        children += [
            UIMenu(title: "Export…", 
                   image: UIImage(systemName: "arrow.up.forward.square"), 
                   children: [
                UIAction(title: "HTML", image: UIImage(systemName: "safari")) { ... },
                UIAction(title: "PDF", image: UIImage(systemName: "doc")) { ... }
            ])
        ]
        return UIMenu(children: children)
    }
}
```

### Enable customization for center items — [9:35]

```swift
navigationItem.customizationIdentifier = "editorView"
```

### Define a fixed center item group. — [10:00]

```swift
UIBarButtonItem(title: "Sync Scrolling", ...).creatingFixedGroup()
```

### Define an optional (customizable) center item group. — [10:23]

```swift
UIBarButtonItem(title: "Add Link", ...).creatingOptionalGroup(customizationIdentifier: "addLink")
```

### Define a non-default optional center item group. — [10:56]

```swift
UIBarButtonItemGroup.optionalGroup(customizationIdentifier: "textFormat",
																	 isInDefaultCustomization: false,
																	 representativeItem: UIBarButtonItem(title: "Format", ...)
																	 items: [
																	      UIBarButtonItem(title: "Bold", ...),
																	      UIBarButtonItem(title: "Italics", ...),
																	      UIBarButtonItem(title: "Underline", ...),
																	 ])
```

### Define a custom menu representation for a bar button item group. — [13:16]

```swift
sliderGroup.menuRepresentation = UIMenu(title: "Text Size",
                                        preferredElementSize: .small,
                                        children: [
    UIAction(title: "Decrease",
             image: UIImage(systemName: "minus.magnifyingglass"),
             attributes: .keepsMenuPresented) { ... },
    UIAction(title: "Reset",
             image: UIImage(systemName: "1.magnifyingglass"),
             attributes: .keepsMenuPresented) { ... },
    UIAction(title: "Increase",
             image: UIImage(systemName: "plus.magnifyingglass"),
             attributes: .keepsMenuPresented) { ... },
])
```

### Enable multiple selection and keyboard focus in a UICollectionView. — [15:10]

```swift
// Enable multiple selection
collectionView.allowsMultipleSelection = true

// Enable keyboard focus
collectionView.allowsFocus = true

// Allow keyboard focus to drive selection 
collectionView.selectionFollowsFocus = true
```

### Add a primary action to UICollectionView items. — [16:11]

```swift
func collectionView(_ collectionView: UICollectionView, 
                    performPrimaryActionForItemAt indexPath: IndexPath) {

    // Scroll to the tapped element
    if let element = dataSource.itemIdentifier(for: indexPath) {
        delegate?.outline(self, didChoose: element)
    }
}
```

### Add a multi-item menu to UICollectionView. — [16:56]

```swift
func collectionView(_ collectionView: UICollectionView, 
                      contextMenuConfigurationForItemsAt indexPaths: [IndexPath], 
                      point: CGPoint) -> UIContextMenuConfiguration? {

    if indexPaths.count == 0 {
        // Construct an empty space menu
    } 
    else if indexPaths.count == 1 {
        // Construct a single item menu
    } 
    else {
        // Construct a multi-item menu
    }
}
```

### Enable Find and Replace in UITextView. — [18:12]

```swift
textView.isFindInteractionEnabled = true
```

### Add custom actions to UITextView's edit menu. — [18:34]

```swift
func textView(_ textView: UITextView,
              editMenuForTextIn range: NSRange,
              suggestedActions: [UIMenuElement]) -> UIMenu? {

    if textView.selectedRange.length > 0 {
        let customActions = [ UIAction(title: "Hide", ... ) { ... } ]
        return UIMenu(children: customActions + suggestedActions)
    }

    return nil
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10070/3/03E2BD27-04DD-4C07-A662-B94B7F784C65/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10070/3/03E2BD27-04DD-4C07-A662-B94B7F784C65/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10070) — developer.apple.com. Indexed for agent consumption._