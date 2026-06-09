---
id: "wwdc2021-10063"
event: "wwdc2021"
year: 2021
title: "Customize and resize sheets in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10063"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Customize and resize sheets in UIKit

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10063](https://developer.apple.com/videos/play/wwdc2021/10063)

Discover how you can create a layered and customized sheet experience in UIKit. We’ll explore how you can build a non-modal experience in your app to allow interaction with content both in a sheet and behind the sheet at the same time. We’ll also take you through sheet size customization, revealing or hiding grabber controls, and adapting between popovers and customized sheets in your app. To get the most out of this session, we recommend watching the Presentations portion of “Modernizing Your UI for iOS 13” from WWDC19 beginning at 9:45.

**Keywords:** `card`, `presentation`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,980 words)

## Documentation & Resources

- [Customizing and resizing sheets in UIKit](https://developer.apple.com/documentation/UIKit/customizing-and-resizing-sheets-in-uikit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/customizing-and-resizing-sheets-in-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/customizing-and-resizing-sheets-in-uikit.json
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Get a sheet — [0:01]

```swift
if let sheet = viewController.sheetPresentationController {
    // Customize the sheet
}
present(viewController, animated: true)
```

### Detents (large only) — [0:02]

```swift
if let sheet = picker.sheetPresentationController {
    sheet.detents = [.large()]
}
present(picker, animated: true)
```

### Detents (medium and large) — [0:03]

```swift
if let sheet = picker.sheetPresentationController {
    sheet.detents = [.medium(), .large()]
}
present(picker, animated: true)
```

### Detents (medium only) — [0:04]

```swift
if let sheet = picker.sheetPresentationController {
    sheet.detents = [.medium()]
}
present(picker, animated: true)
```

### Present image picker in a standard sheet — [0:05]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
    dismiss(animated: true)
}
```

### Present at medium detent, and don’t dismiss automatically — [0:06]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    if let sheet = picker.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
    }
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
}
```

### Prevent scrolling from expanding the sheet — [0:07]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    if let sheet = picker.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
    }
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
}
```

### Select medium detent when a photo is picked — [0:08]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    if let sheet = picker.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
    }
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
    if let sheet = picker.sheetPresentationController {
        sheet.selectedDetentIdentifier = .medium
    }
}
```

### Animate selection of medium detent — [0:09]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    if let sheet = picker.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
    }
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
    if let sheet = picker.sheetPresentationController {
        sheet.animateChanges {
            sheet.selectedDetentIdentifier = .medium
        }
    }
}
```

### Remove dimming at medium detent — [0:10]

```swift
func showImagePicker() {
    let picker = PHPickerViewController()
    picker.delegate = self
    if let sheet = picker.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
        sheet.smallestUndimmedDetentIdentifier = .medium
    }
    present(picker, animated: true)
}

func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
    if let sheet = picker.sheetPresentationController {
        sheet.animateChanges {
            sheet.selectedDetentIdentifier = .medium
        }
    }
}
```

### iPhone in landscape — [0:11]

```swift
if let sheet = fontPicker.sheetPresentationController {
    sheet.prefersEdgeAttachedInCompactHeight = true
    sheet.widthFollowsPreferredContentSizeWhenEdgeAttached = true
}
present(fontPicker, animated: true)
```

### Show a grabber — [0:12]

```swift
if let sheet = fontPicker.sheetPresentationController {
    sheet.prefersGrabberVisible = true
}
present(fontPicker, animated: true)
```

### Customize the corner radius — [0:13]

```swift
if let sheet = fontPicker.sheetPresentationController {
    sheet.preferredCornerRadius = 20.0
}
present(fontPicker, animated: true)
```

### Adapt a popover to a customized sheet — [0:14]

```swift
func showImagePicker(_ sender: UIBarButtonItem) {
    let picker = PHPickerViewController()
    picker.delegate = self
    picker.modalPresentationStyle = .popover
    if let popover = picker.popoverPresentationController {
        popover.barButtonItem = sender

        let sheet = popover.adaptiveSheetPresentationController
        sheet.detents = [.medium(), .large()]
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
        sheet.smallestUndimmedDetentIdentifier = .medium
    }
    present(picker, animated: true)
}
```

### Be consistent when using adaptiveSheetPresentationController — [0:15]

```swift
func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
    // assign result to imageView.image
    if let sheet = picker.popoverPresentationController?.adaptiveSheetPresentationController {
        sheet.animateChanges {
            sheet.selectedDetentIdentifier = .medium
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10063/8/0D794296-1707-4A1D-8CBB-B2CAFEA82AAC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10063/8/0D794296-1707-4A1D-8CBB-B2CAFEA82AAC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10063) — developer.apple.com. Indexed for agent consumption._
