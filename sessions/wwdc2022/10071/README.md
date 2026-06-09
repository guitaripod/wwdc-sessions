---
id: "wwdc2022-10071"
event: "wwdc2022"
year: 2022
title: "Adopt desktop-class editing interactions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10071"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Adopt desktop-class editing interactions

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10071](https://developer.apple.com/videos/play/wwdc2022/10071)

Discover advanced desktop-class editing features that can help people accelerate their productivity in your app. Learn how you can provide more interactions inline with your UI to help people quickly access editing features and make your iPadOS app feel right at home on macOS with Mac Catalyst. We’ll also explore the highly-customizable find interaction and learn how the system UI can help people consistently find content in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,692 words)

## Documentation & Resources

- [UIFindInteraction](https://developer.apple.com/documentation/UIKit/UIFindInteraction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIFindInteraction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIFindInteraction.json
- [UIEditMenuInteraction](https://developer.apple.com/documentation/UIKit/UIEditMenuInteraction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIEditMenuInteraction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIEditMenuInteraction.json
- [Building a desktop-class iPad app](https://developer.apple.com/documentation/UIKit/building-a-desktop-class-ipad-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-a-desktop-class-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-a-desktop-class-ipad-app.json
- [Supporting desktop-class features in your iPad app](https://developer.apple.com/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app.json

## Code Snippets

### Adding items into text edit menus — [2:42]

```swift
func textView(
_ textView: UITextView, 
editMenuForTextIn range: NSRange, 
suggestedActions: [UIMenuElement]) -> UIMenu?
```

### Adding actions into a text view's menu — [4:03]

```swift
func textView(
    _ textView: UITextView,
    editMenuForTextIn range: NSRange,
    suggestedActions: [UIMenuElement]
) -> UIMenu? {
    var additionalActions: [UIMenuElement] = []
    if range.length > 0 {
        let highlightAction = UIAction(title: "Highlight", ...)
        additionalActions.append(highlightAction)
    }
    let insertPhotoAction = UIAction(title: "Insert Photo", ...)
    additionalActions.append(insertPhotoAction)
    return UIMenu(children: suggestedActions + additionalActions)
}
```

### Presenting an edit menu with a custom gesture — [5:24]

```swift
let editMenuInteraction = UIEditMenuInteraction(delegate: self)
view.addInteraction(editMenuInteraction)

let tapRecognizer = UITapGestureRecognizer(target: self, action: #selector(didTap(_:)))
tapRecognizer.allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
view.addGestureRecognizer(tapRecognizer)

@objc func didTap(_ recognizer: UITapGestureRecognizer) {
    let location = recognizer.location(in: self.view)
    if self.hasSelectedObjectView(at: location) {
        let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)
        editMenuInteraction.presentEditMenu(with: configuration)
    }
}
```

### Implementing UIEditMenuInteractionDelegate — [7:13]

```swift
func editMenuInteraction(
    _ interaction: UIEditMenuInteraction,
    targetRectFor configuration: UIEditMenuConfiguration
) -> CGRect {
    guard let selectedView = objectView(at: configuration.sourcePoint) else { return .null }
    return selectedView.frame
}

func editMenuInteraction(
    _ interaction: UIEditMenuInteraction,
    menuFor configuration: UIEditMenuConfiguration,
    suggestedActions: [UIMenuElement]
) -> UIMenu? {
    let duplicateAction = UIAction(title: "Duplicate") { ... }
    return UIMenu(children: suggestedActions + [duplicateAction])
}
```

### Using the "keeps menu presented" attribute — [10:34]

```swift
UIAction(title: "Increase",
         image: UIImage(systemName: "increase.indent"),
         attributes: .keepsMenuPresented) { ... }

UIAction(title: "Decrease",
         image: UIImage(systemName: "decrease.indent"),
         attributes: .keepsMenuPresented) { ... }
```

### Find with system views — [12:46]

```swift
open var findInteraction: UIFindInteraction? { get }
textView.isFindInteractionEnabled = true
```

### Installing a UIFindInteraction on a custom view — [17:22]

```swift
let customDocument = MyDocument(string: "")
lazy var customView = MyTextView(document: customDocument)

lazy var findInteraction = UIFindInteraction(sessionDelegate: self)

override var canBecomeFirstResponder: Bool { true }

override func viewDidLoad() {
    customView.addInteraction(findInteraction)
}

func findInteraction(_ interaction: UIFindInteraction, sessionFor view: UIView) -> UIFindSession? {
    return UITextSearchingFindSession(searchableObject: customDocument)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10071/4/A7198C26-97D7-49C3-8FE7-907808F342DE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10071/4/A7198C26-97D7-49C3-8FE7-907808F342DE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10071) — developer.apple.com. Indexed for agent consumption._