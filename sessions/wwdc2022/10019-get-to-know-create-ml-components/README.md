---
id: "wwdc2022-10019"
event: "wwdc2022"
year: 2022
title: "Get to know Create ML Components"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10019"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Get to know Create ML Components

**Event:** WWDC22 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10019](https://developer.apple.com/videos/play/wwdc2022/10019)

Create ML makes it easy to build custom machine learning models for image classification, object detection, sound classification, hand pose classification, action classification, tabular data regression, and more. And with the Create ML Components framework, you can further customize underlying tasks and improve your model. We’ll explore the feature extractors, transformers, and estimators that make up these tasks, and show you how you can combine them with other components and pre-processing steps to build custom tasks for concepts like image regression. For more information on creating complex customizable tasks, we recommend watching "Compose advanced models with Create ML Components" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,716 words)

## Documentation & Resources

- [Create ML](https://developer.apple.com/documentation/CreateML) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CreateML
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CreateML.json

## Code Snippets

### Image regressor — [8:59]

```swift
import CoreImage
import CreateMLComponents

struct ImageRegressor {
    static let trainingDataURL = URL(fileURLWithPath: "~/Desktop/bananas")
    static let parametersURL = URL(fileURLWithPath: "~/Desktop/parameters")

    static func train() async throws -> some Transformer<CIImage, Float> {
        let estimator = ImageFeaturePrint()
            .appending(LinearRegressor())

        // File name example: banana-5.jpg
        let data = try AnnotatedFiles(labeledByNamesAt: trainingDataURL, separator: "-", index: 1, type: .image)
            .mapFeatures(ImageReader.read)
            .mapAnnotations({ Float($0)! })

        let (training, validation) = data.randomSplit(by: 0.8)
        let transformer = try await estimator.fitted(to: training, validateOn: validation)
        try estimator.write(transformer, to: parametersURL)

        return transformer
    }
}
```

### Image regressor with metrics and augmentations — [12:18]

```swift
import CoreImage
import CreateMLComponents

struct ImageRegressor {
    static let trainingDataURL = URL(fileURLWithPath: "~/Desktop/bananas")
    static let parametersURL = URL(fileURLWithPath: "~/Desktop/parameters")

    static func train() async throws -> some Transformer<CIImage, Float> {
        let estimator = SaliencyCropper()
            .appending(ImageFeaturePrint())
            .appending(LinearRegressor())

        // File name example: banana-5.jpg
        let data = try AnnotatedFiles(labeledByNamesAt: trainingDataURL, separator: "-", index: 1, type: .image)
            .mapFeatures(ImageReader.read)
            .mapAnnotations({ Float($0)! })
            .flatMap(augment)

        let (training, validation) = data.randomSplit(by: 0.8)
        let transformer = try await estimator.fitted(to: training, validateOn: validation) { event in
            guard let trainingMaxError = event.metrics[.trainingMaximumError] else {
                return
            }
            guard let validationMaxError = event.metrics[.validationMaximumError] else {
                return
            }
            print("Training max error: \(trainingMaxError), Validation max error: \(validationMaxError)")
        }

        let validationError = try await meanAbsoluteError(
            transformer.applied(to: validation.map(\.feature)),
            validation.map(\.annotation)
        )
        print("Mean absolute error: \(validationError)")

        try estimator.write(transformer, to: parametersURL)

        return transformer
    }

    static func augment(_ original: AnnotatedFeature<CIImage, Float>) -> [AnnotatedFeature<CIImage, Float>] {
        let angle = CGFloat.random(in: -.pi ... .pi)
        let rotated = original.feature.transformed(by: .init(rotationAngle: angle))

        let scale = CGFloat.random(in: 0.8 ... 1.2)
        let scaled = original.feature.transformed(by: .init(scaleX: scale, y: scale))

        return [
            original,
            AnnotatedFeature(feature: rotated, annotation: original.annotation),
            AnnotatedFeature(feature: scaled, annotation: original.annotation),
        ]
    }
}
```

### Tabular regressor — [20:23]

```swift
import CreateMLComponents
import Foundation
import TabularData

struct TabularRegressor {
    static let dataURL = URL(fileURLWithPath: "~/Downloads/avocado.csv")
    static let parametersURL = URL(fileURLWithPath: "~/Downloads/parameters.pkg")

    static let priceColumnID = ColumnID("price", Double.self)

    static var task: some SupervisedTabularEstimator {
        let numeric = ColumnSelector(
            columns: ["volume"],
            estimator: OptionalUnwrapper()
                .appending(StandardScaler<Double>())
        )
        let regression = BoostedTreeRegressor<String>(
            annotationColumnName: priceColumnID.name,
            featureColumnNames: ["type", "region", "volume"]
        )

        return numeric.appending(regression)
    }

    static func train() async throws -> some TabularTransformer {
        let dataFrame = try DataFrame(contentsOfCSVFile: dataURL)
        let (training, validation) = dataFrame.randomSplit(by: 0.8)
        let transformer = try await task.fitted(to: DataFrame(training), validateOn: DataFrame(validation)) { event in
            guard let validationError = event.metrics[.validationError] as? Double else {
                return
            }
            print("Validation error: \(validationError)")
        }
        try task.write(transformer, to: parametersURL)
        return transformer
    }

    static func predict(
        type: String,
        region: String,
        volume: Double
    ) async throws -> Double {
        let model = try task.read(from: parametersURL)
        let dataFrame: DataFrame = [
            "type": [type],
            "region": [region],
            "volume": [volume]
        ]
        let result = try await model(dataFrame)
        return result[priceColumnID][0]!
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10019/4/CA2236CA-EAD0-454F-8556-FA583BA70590/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10019/4/CA2236CA-EAD0-454F-8556-FA583BA70590/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10019) — developer.apple.com. Indexed for agent consumption._
