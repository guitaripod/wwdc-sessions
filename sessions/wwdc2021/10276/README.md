---
id: "wwdc2021-10276"
event: "wwdc2021"
year: 2021
title: "Use the camera for keyboard input in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10276"
topics: ["Photos & Camera"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Use the camera for keyboard input in your app

**Event:** WWDC21 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10276](https://developer.apple.com/videos/play/wwdc2021/10276)

Learn how you can support Live Text and intelligently pull information from the camera to fill out forms and text fields in your app. We’ll show you how to apply content filtering to capture the correct information when someone uses the camera as keyboard input and apply it to a relevant UITextField, helping your app input data like phone numbers, addresses, and flight information. And we’ll explore how you can create a custom interface, extend other controls like UIImageViews to support this capability, and more.

For more on supporting Autofill in your app, we recommend watching “Autofill everywhere” from WWDC20 and “The Keys to a Better Text Input Experience” from WWDC17.

**Keywords:** `camera`, `input`, `keyboard`, `keyboard as input`, `ocr`, `text recognition`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,861 words)

## Code Snippets

### Filtering text field input — [3:33]

```swift
phone.keyboardType = .phonePad
phone.autocorrectionType = .no

address.textContentType = .fullStreetAddress
```

### Custom action to capture text from camera — [5:07]

```swift
let textFromCamera = UIAction.captureTextFromCamera(responder: self.notes, identifier: nil)
```

### Adding custom UIAction for capture text to a menu — [5:41]

```swift
let textFromCamera = UIAction.captureTextFromCamera(responder: self.notes, identifier: nil)

let choosePhotoOrVideo = UIAction(…)
let takePhotoOrVideo = UIAction(…)
let scanDocuments = UIAction(…)

let cameraMenu = UIMenu(children: [choosePhotoOrVideo, takePhotoOrVideo, scanDocuments, textFromCamera])

let menuToolbarItem = UIBarButtonItem(title: nil, image: UIImage(systemName: "camera.badge.ellipsis"), primaryAction: nil, menu: cameraMenu)
```

### Implementing UIKeyInput on a custom image view — [9:59]

```swift
class HeadlineImageView: UIImageView, UIKeyInput {
    var headlineLabel: UILabel = UILabel()
    var hasText: Bool = false

    override init(image: UIImage?) {
        super.init(image: image)
        initializeLabel()
    }

    func insertText(_ text: String) {
        headlineLabel.text = text
    }

    func deleteBackward() { }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10276/3/35E33348-1E17-4FF5-92BB-618ED251B0EC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10276/3/35E33348-1E17-4FF5-92BB-618ED251B0EC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10276) — developer.apple.com. Indexed for agent consumption._