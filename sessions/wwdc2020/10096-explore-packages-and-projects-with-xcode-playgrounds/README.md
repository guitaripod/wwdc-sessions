---
id: "wwdc2020-10096"
event: "wwdc2020"
year: 2020
title: "Explore Packages and Projects with Xcode Playgrounds"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10096"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore Packages and Projects with Xcode Playgrounds

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10096](https://developer.apple.com/videos/play/wwdc2020/10096)

Xcode Playgrounds helps developers explore Swift and framework APIs and provides a scratchpad for rapid experimentation. Learn how Xcode Playgrounds utilizes Xcode's modern build system, provides improved support for resources, and integrates into your projects, frameworks, and Swift packages to improve your documentation and development workflow.

**Keywords:** `documentation`, `playgrounds`, `resources`, `swift packages`, `xcode`, `xcode playgrounds`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,735 words)

## Documentation & Resources

- [Fruta: Building a feature-rich app with SwiftUI](https://developer.apple.com/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui.json

## Code Snippets

### Playgrounds and resources Demo: Part 1 — [8:53]

```swift
import UIKit
let image = UIImage(named: "ingredient/orange")
```

### Playgrounds and resources Demo: Part 2 — [10:18]

```swift
import CoreML
let yoloModel = try YOLOv3(configuration: MLModelConfiguration()).model
```

### Playgrounds and resources Demo: Part 3 — [10:54]

```swift
import UIKit
import CoreML
import Vision

let ingredientNames = [
    "banana",
    "orange",
    "almond-milk",
]

let yoloModel = try YOLOv3(configuration: MLModelConfiguration()).model
let model = try VNCoreMLModel(for: yoloModel)

let request = VNCoreMLRequest(model: model) {_,_ in }
```

### Recognized Object Visualizer — [11:24]

```swift
import Foundation
import SwiftUI
import UIKit

// MARK: Model

/// The result of object detection on an image.
public struct ObjectDetectionResult : Identifiable {
    public var name: String
    public var image: UIImage
    public var id: String
    public var objects: [RecognizedObject]

    public init(name: String, image: UIImage, id: String, objects: [RecognizedObject]) {
        self.id = id
        self.name = name
        self.image = image
        self.objects = objects
    }
}

/// An object recognized by an image classifier.
public struct RecognizedObject : Identifiable {
    public var id: Int
    public var label: String
    public var confidence: Double
    public var boundingBox: CGRect

    public init(id: Int, label: String, confidence: Double, boundingBox: CGRect) {
        self.id = id
        self.label = label
        self.confidence = confidence
        self.boundingBox = boundingBox
    }
}

// MARK: Views

public struct RecognizedObjectVisualizer : View {
    public var results: [ObjectDetectionResult]
    public var imageSize: CGFloat = 400

    public init(withResults results: [ObjectDetectionResult]) {
        self.results = results
    }

    public var body: some View {
        List(results) { result in
            Spacer()

            VStack(alignment: .center) {
                RecognizedObjectsView(
                    image: result.image,
                    objects: result.objects
                )
                .frame(width: imageSize, height: imageSize)

                Text(result.name.capitalized)

                Spacer(minLength: 20)
            }

            Spacer()
        }
    }
}

struct RecognizedObjectsView : View {
    var image: UIImage
    var objects: [RecognizedObject]

    var body: some View {
        GeometryReader { geometry in
            Image(uiImage: image)
                .resizable()
                .overlay(
                    ZStack {
                        ForEach(objects) { object in
                            Rectangle()
                                .stroke(Color.red)
                                .shadow(radius: 2.0)
                                .frame(
                                    width: object.boundingBox.width * geometry.size.width / image.size.width,
                                    height: object.boundingBox.height * geometry.size.height / image.size.height
                                )
                                .position(
                                    x: (object.boundingBox.origin.x + object.boundingBox.size.width / 2.0) * geometry.size.width / image.size.width,
                                    y: geometry.size.height - (object.boundingBox.origin.y + object.boundingBox.size.height / 2.0) * geometry.size.height / image.size.height
                                )
                                .overlay(
                                    Text("\(object.label.capitalized) (\(String(format: "%0.0f", object.confidence * 100.0))%)")
                                        .foregroundColor(Color.red)
                                        .position(
                                            x: (object.boundingBox.origin.x + object.boundingBox.size.width / 2.0) * geometry.size.width / image.size.width,
                                            y: geometry.size.height - (object.boundingBox.origin.y - 20.0) * geometry.size.height / image.size.height
                                        )
                                )
                        }
                    }
                )
        }
    }
}
```

### Playgrounds and resources Demo: Part 4 — [11:48]

```swift
let results = ingredientNames.compactMap { ingredient -> ObjectDetectionResult? in

    guard let image = UIImage(named: "ingredient/\(ingredient)") else { return nil }

    let handler = VNImageRequestHandler(cgImage: image.cgImage!)
    try? handler.perform([request])
    let observations = request.results as! [VNRecognizedObjectObservation]

    let detectedObjects = observations.enumerated().map { (index, observation) -> RecognizedObject in

        // Select only the label with the highest confidence.
        let topLabelObservation = observation.labels[0]
        let objectBounds = VNImageRectForNormalizedRect(observation.boundingBox, Int(image.size.width), Int(image.size.height))

        return RecognizedObject(id: index, label: topLabelObservation.identifier, confidence: Double(topLabelObservation.confidence), boundingBox: objectBounds)
    }

    return ObjectDetectionResult(name: ingredient, image: image, id: ingredient, objects: detectedObjects)
}

results
```

### Playgrounds and resources Demo: Part 5 — [12:33]

```swift
import PlaygroundSupport

PlaygroundPage.current.setLiveView(
    RecognizedObjectVisualizer(withResults: results)
        .frame(width: 500, height: 800)
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10096/4/9D01022D-66DF-4B16-B5B6-B01F57252226/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10096) — developer.apple.com. Indexed for agent consumption._
