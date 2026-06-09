---
id: "wwdc2020-10052"
event: "wwdc2020"
year: 2020
title: "Build with iOS pickers, menus and actions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10052"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build with iOS pickers, menus and actions

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10052](https://developer.apple.com/videos/play/wwdc2020/10052)

Build iPhone and iPad apps with fluid interfaces and easily-accessible contextual information. We’ll show you how to integrate the latest UIKit controls into your app to best take advantage of menus, date pickers, page controls, and segmented controllers. Learn how to adopt Menus throughly your user interface, and explore how UIAction can help unify your event handling. Once you’ve learned about these new controls, watch “Design with iOS pickers, menus and actions” to discover how to design great interfaces with these tools and APIs.

**Keywords:** `uicontrol`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,938 words)

## Documentation & Resources

- [Adopting menus and UIActions in your user interface](https://developer.apple.com/documentation/UIKit/adopting-menus-and-uiactions-in-your-user-interface) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adopting-menus-and-uiactions-in-your-user-interface
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adopting-menus-and-uiactions-in-your-user-interface.json

## Code Snippets

### UIPageControl example — [4:34]

```swift
let pageControl = UIPageControl()
pageControl.numberOfPages = 5

pageControl.backgroundStyle = .prominent

pageControl.preferredIndicatorImage =
    UIImage(systemName: "bookmark.fill")

pageControl.setIndicatorImage(
    UIImage(systemName: "heart.fill"), forPage: 0)
```

### UIColorPickerViewController example — [6:56]

```swift
var color = UIColor.blue
var colorPicker = UIColorPickerViewController()

func pickColor() {
    colorPicker.supportsAlpha = true
    colorPicker.selectedColor = color
    self.present(colorPicker,
        animated: true,
      completion: nil)
}

func colorPickerViewControllerDidSelectColor(_
  viewController: UIColorPickerViewController) {
    color = viewController.selectedColor
}

func colorPickerViewControllerDidFinish(_
  viewController: UIColorPickerViewController) {
    // Do nothing
}
```

### UIDatePicker example — [10:04]

```swift
let datePicker = UIDatePicker()
datePicker.date = Date(timeIntervalSinceReferenceDate:
                       timeInterval)

datePicker.preferredDatePickerStyle = .compact

datePicker.calendar = Calendar(identifier: .japanese)
datePicker.datePickerMode = .date

datePicker.addTarget(self,
             action: #selector(dateSet),
                for: .valueChanged)
```

### UIDeferredMenuElement example — [14:20]

```swift
button.menu = UIMenu(title: "", children: [
    UIMenu(title: "", options: .displayInline, children: (1...2).map { UIAction(title: "Static Item \($0)") { action in }}),
    UIDeferredMenuElement({ completion in
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            completion([UIMenu(title: "", options: .displayInline, children: (1...2).map { UIAction(title: "Dynamic Item \($0)") { action in }})])
        }
    }),
])
```

### updateVisibleMenu example — [14:50]

```swift
self.contextMenuInteraction.updateVisibleMenu { currentMenu -> UIMenu in
    currentMenu.children.forEach { element in
        guard let action = element as? UIAction else { return }

        action.state = Bool.random() ? .off : .on
        action.attributes = Bool.random() ? [.hidden] : []
    }
    return currentMenu
}
```

### UIBarButtonItem example — [16:05]

```swift
let saveAction = UIAction(title: "") { action in }
let saveMenu = UIMenu(title: "", children: [
    UIAction(title: "Copy", image: UIImage(systemName: "doc.on.doc")) { action in },
    UIAction(title: "Rename", image: UIImage(systemName: "pencil")) { action in },
    UIAction(title: "Duplicate", image: UIImage(systemName: "plus.square.on.square")) { action in },
    UIAction(title: "Move", image: UIImage(systemName: "folder")) { action in },
])
let optionsImage = UIImage(systemName: "ellipsis.circle")
let optionsMenu = UIMenu(title: "", children: [
    UIAction(title: "Info", image: UIImage(systemName: "info.circle")) { action in },
    UIAction(title: "Share", image: UIImage(systemName: "square.and.arrow.up")) { action in },
    UIAction(title: "Collaborate", image: UIImage(systemName: "person.crop.circle.badge.plus")) { action in },
])
let revertAction = UIAction(title: "Revert") { action in }
self.toolbarItems = [
    UIBarButtonItem(systemItem: .save, primaryAction: saveAction, menu: saveMenu),
    .fixedSpace(width:20.0),
    UIBarButtonItem(image: optionsImage, menu: optionsMenu),
    .flexibleSpace(),
    UIBarButtonItem(primaryAction: revertAction),
]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10052/5/C534955F-BDE1-4CDE-87C3-320B97F2AF8E/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10052) — developer.apple.com. Indexed for agent consumption._
