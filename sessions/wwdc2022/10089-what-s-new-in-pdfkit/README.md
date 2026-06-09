---
id: "wwdc2022-10089"
event: "wwdc2022"
year: 2022
title: "What's new in PDFKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10089"
topics: ["Essentials", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in PDFKit

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10089](https://developer.apple.com/videos/play/wwdc2022/10089)

Discover PDFKit — a full-featured framework that helps your app view, edit, and save PDF documents. We'll take you through the latest features in PDFKit, including support for live text and forms, creating PDFs from images, building interactive overlays, and saving annotations.

**Keywords:** `pencilkit`, `pencil kit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,088 words)

## Documentation & Resources

- [PDFAnnotationWidgetsAdvanced](https://developer.apple.com/sample-code/wwdc/2017/PDFAnnotationWidgetsAdvanced.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/wwdc/2017/PDFAnnotationWidgetsAdvanced.zip

## Code Snippets

### Implementing the overlay protocol — [6:54]

```swift
class Coordinator: NSObject, PDFPageOverlayViewProvider {

    var pageToViewMapping = [PDFPage: UIView]()

    func pdfView(_ view: PDFView, overlayViewFor page: PDFPage) -> UIView? {
        var resultView: PKCanvasView? = nil

        if let overlayView = pageToViewMapping[page] {
            resultView = overlayView
        } else {
            let canvasView = PKCanvasView(frame: .zero)
            canvasView.drawingPolicy = .anyInput
            canvasView.tool = PKInkingTool(.pen, color: .systemYellow, width: 20)
            canvasView.backgroundColor = UIColor.clear
            pageToViewMapping[page] = canvasView
            resultView = canvasView
        }

        // If we have stored a drawing on the page, set it on the canvas
        let page = page as! MyPDFPage
        if let drawing = page.drawing {
            resultView?.drawing = drawing;
        }
        return resultView
    }

    func pdfView(_ pdfView: PDFView, willEndDisplayingOverlayView
        overlayView: UIView, for page: PDFPage) {
        let overlayView = overlayView as! PKCanvasView
        let page = page as! MyPDFPage
        page.drawing = overlayView.drawing
        pageToViewMapping.removeValue(forKey: page)
    }
}
```

### Create a subclass of PDFAnnotation — [10:22]

```swift
// Implement a subclass with a drawing override

class MyPDFAnnotation: PDFAnnotation {

    override func draw(with box: PDFDisplayBox, in context: CGContext) {
        UIGraphicsPushContext(context)
        context.saveGState()

        let page = self.page as! MyPDFPage
        if let drawing = page.drawing {
            let image = drawing.image(from: drawing.bounds, scale: 1)
            image.draw(in: drawing.bounds)
        }

        context.restoreGState()
        UIGraphicsPopContext()
    }
}
```

### Add annotations to your document when saving — [10:35]

```swift
override func contents(forType typeName: String) throws -> Any {

    if let pdfDocument = pdfDocument {

        // Go through all pages in the document
        for i in 0...pdfDocument.pageCount-1 {
            if let page = pdfDocument.page(at: i) {                       
                if let drawing = (page as! MyPDFPage).drawing {

                    // Create an annotation of our custom subclass
                    let newAnnotation = MyPDFAnnotation(bounds: drawing.bounds,
                                                        forType: .stamp, withProperties: nil)

                    // Add our custom data
                    let codedData = try! NSKeyedArchiver.archivedData(withRootObject: drawing,
                                                                      requiringSecureCoding: true)
                    newAnnotation.setValue(codedData,
                                           forAnnotationKey: PDFAnnotationKey(rawValue: "drawingData"))

                    // Add our annotation to the page
                    page.addAnnotation(newAnnotation)
                }
            }
        }

        // -- Option #1: Save the document to a data representation
        if let resultData = pdfDocument.dataRepresentation() {
            return resultData
        }

        // -- Option #2: Save the document to a data representation and "burn in" annotations
        let options = [PDFDocumentWriteOption.burnInAnnotationsOption: true]
        if let resultData = pdfDocument.dataRepresentation(options: options) {
            return resultData
        }
    }

    // Fall through to returning empty data
    return Data()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10089/3/473B1E55-B2A6-42BB-AA96-EE2599D6E779/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10089/3/473B1E55-B2A6-42BB-AA96-EE2599D6E779/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10089) — developer.apple.com. Indexed for agent consumption._
