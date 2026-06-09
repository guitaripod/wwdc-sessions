---
id: "wwdc2021-10041"
event: "wwdc2021"
year: 2021
title: "Extract document data using Vision"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10041"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Extract document data using Vision

**Event:** WWDC21 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10041](https://developer.apple.com/videos/play/wwdc2021/10041)

Discover how Vision can provide expert image recognition and analysis in your app to extract information from documents, recognize text in multiple languages, and identify barcodes. We’ll explore the latest updates to Text Recognition and Barcode Detection, show you how to bring all these tools together with Core ML, and help your app make greater sense of the world through images or the live camera.

To learn more about Vision, watch “Detect people, faces, and poses using Vision” from WWDC21 as well as “Explore Computer Vision APIs” from WWDC20.

For further understanding of all that Vision has to offer, watch “Detect people, faces, and poses using Vision” from WWDC21 as well as “Explore Computer Vision APIs” from WWDC20.

**Keywords:** `barcode`, `barcode detection`, `computer vision`, `core ml`, `machine learning`, `ocr`, `text recognition`, `vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,688 words)

## Documentation & Resources

- [Vision](https://developer.apple.com/documentation/Vision) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision.json

## Code Snippets

### Barcode Scan — [6:18]

```swift
import Foundation
import Vision

let url = URL(fileReferenceLiteralResourceName: "codeall_4.png") as CFURL

guard let imageSource = CGImageSourceCreateWithURL(url, nil),
      let barcodeImage = CGImageSourceCreateImageAtIndex(imageSource, 0, nil) else {
    fatalError("Unable to create barcode image.")
}

let imageRequestHandler = VNImageRequestHandler(cgImage: barcodeImage)

let detectBarcodesRequest = VNDetectBarcodesRequest()
detectBarcodesRequest.revision = VNDetectBarcodesRequestRevision2
detectBarcodesRequest.symbologies = [.codabar]

try imageRequestHandler.perform([detectBarcodesRequest])

if let detectedBarcodes = detectBarcodesRequest.results {

    drawBarcodes(detectedBarcodes, sourceImage: barcodeImage)

    detectedBarcodes.forEach {
        print($0.payloadStringValue ?? "")
    }
}




public func createCGPathForTopLeftCCWQuadrilateral(_ topLeft: CGPoint,
                                            _ bottomLeft: CGPoint,
                                            _ bottomRight: CGPoint,
                                            _ topRight: CGPoint,
                                            _ transform: CGAffineTransform) -> CGPath
{
    let path = CGMutablePath()
    path.move(to: topLeft, transform: transform)
    path.addLine(to: bottomLeft, transform: transform)
    path.addLine(to: bottomRight, transform: transform)
    path.addLine(to: topRight, transform: transform)
    path.addLine(to: topLeft, transform: transform)
    path.closeSubpath()
    return path
}


public func drawBarcodes(_ observations: [VNBarcodeObservation], sourceImage: CGImage) -> CGImage? {
    let size = CGSize(width: sourceImage.width, height: sourceImage.height)
    let imageSpaceTransform = CGAffineTransform(scaleX:size.width, y:size.height)
    let colorSpace = CGColorSpace.init(name: CGColorSpace.sRGB)
    let cgContext = CGContext.init(data: nil, width: Int(size.width), height: Int(size.height), bitsPerComponent: 8, bytesPerRow: 8 * 4 * Int(size.width), space: colorSpace!, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
    cgContext.setStrokeColor(CGColor.init(srgbRed: 1.0,  green: 0.0,  blue: 0.0,  alpha: 0.7))
    cgContext.setLineWidth(25.0)
    cgContext.draw(sourceImage, in: CGRect(x: 0.0, y: 0.0, width: size.width, height: size.height))

    for currentObservation in observations {
        let path = createCGPathForTopLeftCCWQuadrilateral(currentObservation.topLeft,
                                                        currentObservation.bottomLeft,
                                                        currentObservation.bottomRight,
                                                        currentObservation.topRight,
                                                        imageSpaceTransform)
        cgContext.addPath(path)
        cgContext.strokePath()
    }
    return cgContext.makeImage()
}
```

### Survey Scan — [14:02]

```swift
import Foundation
import CoreImage
import Vision
import CoreML

guard var inputImage = CIImage(contentsOf: #fileLiteral(resourceName: "IMG_0001.HEIC"))
else { fatalError("image not found") }

inputImage

let requestHandler = VNImageRequestHandler(ciImage: inputImage)
let documentDetectionRequest = VNDetectDocumentSegmentationRequest()
try requestHandler.perform([documentDetectionRequest])

guard let document = documentDetectionRequest.results?.first,
      let documentImage = perspectiveCorrectedImage(from: inputImage, rectangleObservation: document) else {
          fatalError("Unable to get document image.")
      }

documentImage
let documentRequestHandler = VNImageRequestHandler(ciImage: documentImage)

/*
 TODO
  Detect barcodes
  Detect rectangles
  Recognize text
  Perform those requests
  Scan checkboxes
 */

var documentTitle = "Don't know yet"

let barcodesDetection = VNDetectBarcodesRequest() { request, _ in
    guard let result = request.results?.first as? VNBarcodeObservation,
          let payload = result.payloadStringValue else { return }
    documentTitle = "\(payload) was: "
}
barcodesDetection.symbologies = [.qr]

var checkBoxImages: [CIImage] = []
var rectangles: [VNRectangleObservation] = []

let rectanglesDetection = VNDetectRectanglesRequest { request, error in
    rectangles = request.results as! [VNRectangleObservation]
    // sort by vertical coordinates
    rectangles.sort{$0.boundingBox.origin.y > $1.boundingBox.origin.y}

    for rectangle in rectangles {
        guard let checkBoxImage = perspectiveCorrectedImage(from: documentImage, rectangleObservation: rectangle)
        else { print("Could not extract document"); return }
        checkBoxImages.append(checkBoxImage)
    }
}
rectanglesDetection.minimumSize = 0.1
rectanglesDetection.maximumObservations = 0

var textBlocks: [VNRecognizedTextObservation] = []

let ocrRequest = VNRecognizeTextRequest { request, error in
    textBlocks = request.results as! [VNRecognizedTextObservation]
}

do {
    try documentRequestHandler.perform([ocrRequest, rectanglesDetection, barcodesDetection])
} catch {
    print(error)
}


let classificationRequest = createclassificationRequest()

var index = 0
for checkBoxImage in checkBoxImages {
    let checkBoxRequestHandler = VNImageRequestHandler(ciImage: checkBoxImage)
    do {
        try checkBoxRequestHandler.perform([classificationRequest])
        if let classifications = classificationRequest.results as? [VNClassificationObservation] {
            if let topClassification = classifications.first
            {
                if topClassification.identifier == "Yes" && topClassification.confidence >= 0.9 {
                    for currentText in textBlocks {
                        if observationLinesUp(rectangles[index], with: currentText) {
                            let foundTextObservation = currentText.topCandidates(1)
                            documentTitle += foundTextObservation.first!.string + " "
                        }
                    }
                }
            }
        }
    } catch {
        print(error)
    }
    index += 1
}

print(documentTitle)



extension CGPoint {
    func scaled(to size: CGSize) -> CGPoint {
        return CGPoint(x: self.x * size.width, y: self.y * size.height)
    }
}
extension CGRect {
    func scaled(to size: CGSize) -> CGRect {
        return CGRect(
            x: self.origin.x * size.width,
            y: self.origin.y * size.height,
            width: self.size.width * size.width,
            height: self.size.height * size.height
        )
    }
}

public func observationLinesUp(_ observation: VNRectangleObservation, with textObservation: VNRecognizedTextObservation ) -> Bool {
    // calculate center
    let midPoint =  CGPoint(x:textObservation.boundingBox.midX, y:observation.boundingBox.midY)
    return textObservation.boundingBox.contains(midPoint)
}

public func perspectiveCorrectedImage(from inputImage: CIImage, rectangleObservation: VNRectangleObservation ) -> CIImage? {
    let imageSize = inputImage.extent.size

    // Verify detected rectangle is valid.
    let boundingBox = rectangleObservation.boundingBox.scaled(to: imageSize)
    guard inputImage.extent.contains(boundingBox)
    else { print("invalid detected rectangle"); return nil}

    // Rectify the detected image and reduce it to inverted grayscale for applying model.
    let topLeft = rectangleObservation.topLeft.scaled(to: imageSize)
    let topRight = rectangleObservation.topRight.scaled(to: imageSize)
    let bottomLeft = rectangleObservation.bottomLeft.scaled(to: imageSize)
    let bottomRight = rectangleObservation.bottomRight.scaled(to: imageSize)
    let correctedImage = inputImage
        .cropped(to: boundingBox)
        .applyingFilter("CIPerspectiveCorrection", parameters: [
            "inputTopLeft": CIVector(cgPoint: topLeft),
            "inputTopRight": CIVector(cgPoint: topRight),
            "inputBottomLeft": CIVector(cgPoint: bottomLeft),
            "inputBottomRight": CIVector(cgPoint: bottomRight)
        ])
    return correctedImage
}

public func createclassificationRequest() -> VNCoreMLRequest
{
    let classificationRequest: VNCoreMLRequest = {
        // Load the ML model through its generated class and create a Vision request for it.
        do {
            let coreMLModel = try MLModel(contentsOf: #fileLiteral(resourceName: "CheckboxClassifier.mlmodelc"))
            let model = try VNCoreMLModel(for: coreMLModel)

            return VNCoreMLRequest(model: model)
        } catch {
            fatalError("can't load Vision ML model: \(error)")
        }
    }()
    return classificationRequest
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10041/6/1CB4D0E9-CCA8-4C66-80DA-5887CF8F06C5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10041/6/1CB4D0E9-CCA8-4C66-80DA-5887CF8F06C5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10041) — developer.apple.com. Indexed for agent consumption._