---
id: "wwdc2023-111215"
event: "wwdc2023"
year: 2023
title: "Meet UIKit for spatial computing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/111215"
topics: ["Developer Tools", "Essentials", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Meet UIKit for spatial computing

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-111215](https://developer.apple.com/videos/play/wwdc2023/111215)

Learn how to bring your UIKit app to visionOS. We’ll show you how to build for a new destination, explore APIs and best practices for spatial computing, and take your content into the third dimension when you use SwiftUI with UIKit in visionOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,263 words)

## Code Snippets

### permittedArrowDirections — [16:15]

```swift
import UIKit

extension EditorViewController {

    @objc func showDocumentPopover(sender: UIBarButtonItem) {
        let controller = DocumentInfoViewController(document: pixelDocument)
        controller.modalPresentationStyle = .popover
        if let presentationController = controller.popoverPresentationController {
            presentationController.barButtonItem = sender
            if traitCollection.userInterfaceIdiom == .reality {
                presentationController.permittedArrowDirections = .any
            } else {
                presentationController.permittedArrowDirections = .right
            }
        }
        present(controller, animated: true, completion: nil)
    }

}
```

### Ornament — [19:46]

```swift
extension EditorViewController {

    func showEditingControlsOrnament() {
        let ornament = UIHostingOrnament(sceneAlignment: .bottom, contentAlignment: .center) {
            EditingControlsView(model: controlsViewModel)
                .glassBackgroundEffect()
        }

        self.ornaments = [ornament]

        editorView.style = .edgeToEdge
    }

}
```

### UIHostingController — [22:45]

```swift
extension EditorViewController {

    func showEntityPreview() {
        let entityView = PixelArtEntityView(model: entityViewModel)
        let controller = UIHostingController(rootView: entityView)
        addChild(controller)
        view.addSubview(controller.view)
        controller.didMove(toParent: self)
        prepareEditorInteractions()
    }

}
```

### Using Semantic Colors — [22:46]

```swift
private let titleLabelTextField: UITextField = {
    textField.textColor = UIColor.label
    return textField
}()

private let authorLabel: UILabel = {
    label.textColor = UIColor.secondaryLabel
    return label
}()
```

### Adding a recessed appearance to a text field — [22:47]

```swift
textField.borderStyle = .roundedRect
```

### Overriding preferredContainerBackgroundStyle — [22:48]

```swift
class MyViewController: UIViewController {
    override var preferredContainerBackgroundStyle: UIContainerBackgroundStyle {
        return .glass
    }
}
```

### Customizing hover style — [22:49]

```swift
class CollectionViewCell: UICollectionViewCell {
    init(document: PixelArtDocument) {
        self.hoverStyle = .init(
            effect: .highlight, 
            shape: .roundedRect(cornerRadius: 8.0))
    }
}
```

### Checking user interface idiom — [22:50]

```swift
func fourFingerSwipe() {
    let gesture = UISwipeGestureRecognizer(
        target: self, 
        action: #selector(self.deleteAll))
    gesture.direction = .left
    if traitCollection.userInterfaceIdiom == .reality {
        gesture.numberOfTouchesRequired = 2
    } else {
        gesture.numberOfTouchesRequired = 4
    }
    self.view.addGestureRecognizer(gesture)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/111215/4/E8A7CF44-A276-482B-9CFA-F264FD028F54/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/111215/4/E8A7CF44-A276-482B-9CFA-F264FD028F54/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/111215) — developer.apple.com. Indexed for agent consumption._
