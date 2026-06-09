# Unwrap PaperKit

**Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-372](https://developer.apple.com/videos/play/wwdc2026/372)

Craft a canvas-based application with PaperKit. Explore the new data model APIs that let you access, create, and modify markup elements. Learn how to add custom controls and annotations, and discover best practices for integrating these features into your app to build a fully featured creative canvas.

**Keywords:** `🎈`, `paper`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [PaperKit](https://developer.apple.com/documentation/PaperKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PaperKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PaperKit.json

## Code Snippets

### Creating markup subelements — [1:36]

```swift
import PaperKit

func generateMarkup(pageSize: CGSize, panelFrames: [CGRect], configuration: ShapeConfiguration) -> PaperMarkup {
    var markup = PaperMarkup(bounds: CGRect(origin: .zero, size: pageSize))
    var subelements: MarkupOrderedSet = markup.subelements
    for panelFrame: CGRect in panelFrames {
        let shape = ShapeMarkup(frame: panelFrame, configuration: configuration)
        subelements.append(shape)
    }
    markup.subelements = subelements
    return markup
}
```

### Making template elements read-only — [3:03]

```swift
import PaperKit

func generateMarkup(pageSize: CGSize, panelFrames: [CGRect], configuration: ShapeConfiguration) -> PaperMarkup {
    var markup = PaperMarkup(bounds: CGRect(origin: .zero, size: pageSize))
    var subelements: MarkupOrderedSet = markup.subelements
    for panelFrame: CGRect in panelFrames {
        var shape = ShapeMarkup(frame: panelFrame, configuration: configuration)
        shape.allowedInteractions = .readOnly
        subelements.append(shape)
    }
    markup.subelements = subelements
    return markup
}
```

### Apply style to template elements — [4:22]

```swift
import PaperKit

func updatePanelColor(_ selectedColor: CGColor) {
    guard var markup: PaperMarkup = paperMarkupViewController.markup else { return }
    var subelements: MarkupOrderedSet = markup.subelements
    for element in subelements {
        guard var shape = element as? ShapeMarkup else { continue }
        shape.strokeColor = selectedColor
        shape.fillColor = selectedColor.copy(alpha: 0.15)
        subelements.updateOrAppend(shape)
    }
    markup.subelements = subelements
    markup.backgroundColor = selectedColor.copy(alpha: 0.15)
    paperMarkupViewController.markup = markup
}
```

### Add adornments to each panel — [5:53]

```swift
import PaperKit

func addPanelAdornments(for page: Page) {
    var adornments: [MarkupAdornment] = []
    for (panelIndex, panel) in page.panels.enumerated() {
        let adornmentID = UUID()
        adornmentPanelMapping[adornmentID] = panelIndex
        let center = CGPoint(x: panel.midX, y: panel.midY)
        let adornment = MarkupAdornment(
            id: adornmentID,
            anchor: .canvas(location: center),
            imageConfiguration: .systemImage("photo.badge.plus"),
            dragRegion: .fixed,
            scalesWithZoom: false
        )
        adornments.append(adornment)
    }
    paperMarkupViewController.adornments = adornments
}
```

### Handle adornment taps — [6:08]

```swift
import ImagePlayground
import PaperKit

func paperMarkupViewController(_ paperMarkupViewController: PaperMarkupViewController, didTapAdornmentWithID id: UUID) {
    guard let panelIndex = adornmentPanelMapping[id] else { return }
    activeImageGenerationPanelIndex = panelIndex

    let imagePlaygroundViewController = ImagePlaygroundViewController()
    imagePlaygroundViewController.delegate = self
    present(imagePlaygroundViewController, animated: true)
}
```

### Place the generated image — [6:20]

```swift
import ImagePlayground
import PaperKit

func imageViewController(_ imageViewController: ImagePlaygroundViewController, didCreateImageAt imageURL: URL) {
    guard let panelFrame = activeGenerationPanelFrame,
          let paperMarkupViewController = pageViewController.paperViewController,
          var markup = paperMarkupViewController.markup,
          let image = UIImage(contentsOfFile: imageURL.path) else { return }

    let imageMarkup = ImageMarkup(frame: panelFrame, image: image)
    markup.subelements.append(imageMarkup)
    paperMarkupViewController.markup = markup
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/372/4/012a7de6-cf54-420f-aaf7-02ea568485bf/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/372/4/012a7de6-cf54-420f-aaf7-02ea568485bf/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._