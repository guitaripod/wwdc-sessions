---
id: "wwdc2025-285"
event: "wwdc2025"
year: 2025
title: "Meet PaperKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/285"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Meet PaperKit

**Event:** WWDC25 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-285](https://developer.apple.com/videos/play/wwdc2025/285)

Discover how to bring PaperKit to your iOS, iPadOS, macOS, and visionOS apps. We’ll cover how to seamlessly integrate PencilKit drawing with markup features like shapes and images, and how to customize the user interface. Learn best practices for forward compatibility, and discover advanced customization options to create truly unique markup experiences in your apps.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,435 words)

## Documentation & Resources

- [PaperKit](https://developer.apple.com/documentation/PaperKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PaperKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PaperKit.json

## Code Snippets

### Adopt PaperKit in iOS — [3:47]

```swift
// Adopt PaperKit in iOS

override func viewDidLoad() {
    super.viewDidLoad()

    let markupModel = PaperMarkup(bounds: view.bounds)
    let paperViewController = PaperMarkupViewController(markup: markupModel, supportedFeatureSet: .latest)
    view.addSubview(paperViewController.view)
    addChild(paperViewController)
    paperViewController.didMove(toParent: self)
    becomeFirstResponder()    

    let toolPicker = PKToolPicker()
    toolPicker.addObserver(paperViewController)

    pencilKitResponderState.activeToolPicker = toolPicker
    pencilKitResponderState.toolPickerVisibility = .visible

    toolPicker.accessoryItem = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(plusButtonPressed(_:)))
}

@objc func plusButtonPressed(_ button: UIBarButtonItem) {
    let markupEditViewController = MarkupEditViewController(supportedFeatureSet: .latest)    
    markupEditViewController.delegate = paperViewController
    markupEditViewController.modalPresentationStyle = .popover
    markupEditViewController.popoverPresentationController?.barButtonItem = button
    present(markupEditViewController, animated: true)
}
```

### Adopt PaperKit in macOS — [6:11]

```swift
// Adopt PaperKit in macOS

override func viewDidLoad() {
    super.viewDidLoad()

    let markupModel = PaperMarkup(bounds: view.bounds)
    let paperViewController = PaperMarkupViewController(markup: markupModel, supportedFeatureSet: .latest)
    view.addSubview(paperViewController.view)
    addChild(paperViewController)

    // Create toolbar for macOS
    let toolbarViewController = MarkupToolbarViewController(supportedFeatureSet: .latest)
    toolbarViewController.delegate = paperViewController
    view.addSubview(toolbarViewController.view)

    // Set layout
    setupLayoutConstraints()
}
```

### Auto-save markup changes — [7:18]

```swift
// Auto-save markup changes

func paperMarkupViewControllerDidChangeMarkup(_ paperMarkupViewController: PaperMarkupViewController) {
    let markupModel = paperMarkupViewController.markup
    Task {
        // Create a data blob and save it
        let data = try await markupModel.dataRepresentation()
        try data.write(toFile: paperKitDataURL)
    }
}
```

### Thumbnail for forward compatibility — [8:02]

```swift
// Thumbnail for forward compatibility

func updateThumbnail(_ markupModel: PaperMarkup) async throws {
    // Set up CGContext to render thumbnail in
    let thumbnailSize = CGSize(width: 200, height: 200)
    let context = makeCGContext(size: thumbnailSize)
    context.setFillColor(gray: 1, alpha: 1)
    context.fill(renderer.format.bounds)            

    // Render the PaperKit markup
    await markupModel.draw(in: context, frame: CGRect(origin: .zero, size: thumbnailSize))

    thumbnail = context.makeImage()
}
```

### Customized markup FeatureSet — [9:02]

```swift
// Customized markup FeatureSet

var featureSet: FeatureSet = .latest

featureSet.remove(.text)
featureSet.insert(.stickers)

// HDR support
featureSet.colorMaximumLinearExposure = 4
toolPicker.colorMaximumLinearExposure = 4

let paperViewController = PaperMarkupViewController(supportedFeatureSet: featureSet)
let markupEditViewController = MarkupEditViewController(supportedFeatureSet: featureSet)
```

### Custom background on markup controller — [10:50]

```swift
// Custom background on markup controller

let template = UIImage(named: "MyTemplate.jpg")
let templateView = UIImageView(image: template)
paperViewController.contentView = templateView
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/285/4/338ce5dc-94ee-4f86-a122-4bd01d8b1239/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/285/4/338ce5dc-94ee-4f86-a122-4bd01d8b1239/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/285) — developer.apple.com. Indexed for agent consumption._