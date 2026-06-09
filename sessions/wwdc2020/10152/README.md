---
id: "wwdc2020-10152"
event: "wwdc2020"
year: 2020
title: "Use model deployment and security with Core ML"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10152"
topics: ["Developer Tools", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Use model deployment and security with Core ML

**Event:** WWDC20 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10152](https://developer.apple.com/videos/play/wwdc2020/10152)

Discover how to deploy Core ML models outside of your app binary, giving you greater flexibility and control when bringing machine learning features to your app. And learn how Core ML Model Deployment enables you to deliver revised models to your app without requiring an app update. We’ll also walk you through how you can protect custom machine learning models through encryption, and preview your model performance in Xcode.

For more information on working with Core ML, including bringing over models trained in environments like TensorFlow and PyTorch, we also recommend watching "Get your models on device using Core ML Converters.”

**Keywords:** `ai`, `artificial intelligence`, `cloud`, `cloudkit`, `core ml`, `core ml tools`, `create ml`, `deep learning`, `encryption`, `learning`, `machine learning`, `model`, `model deployment`, `model encryption`, `neural network`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,925 words)

## Documentation & Resources

- [Core ML](https://developer.apple.com/documentation/CoreML) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreML
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreML.json

## Code Snippets

### Flower Classifier using Core ML Model Deployment — [4:34]

```swift
private func classifyFlower(in image: CGImage) {
    // Check for a loaded model
    if let model = flowerClassifier {
        classify(image, using: model)
        return
    }

    MLModelCollection.beginAccessing(identifier: "FlowerModels") { [self] result in
        var modelURL: URL?
        switch result {
        case .success(let collection):
            modelURL = collection.entries["FlowerClassifier"]?.modelURL
        case .failure(let error):
            handleModelCollectionFailure(for: error)
        }

        let result = loadFlowerClassifier(from: modelURL)

        switch result {
        case .success(let model):
            classify(image, using: model)
        case .failure(let error):
            handleModelLoadFailure(for: error)
        }
    }
}

func loadFlowerClassifier(from modelURL: URL?) -> Result<FlowerClassifier, Error> {
    if let modelURL = modelURL {
        return Result { try FlowerClassifier(contentsOf: modelURL) }
    } else {
        return Result { try FlowerClassifier(configuration: .init()) }
    }
}
```

### Compiler flag for encrypting a model — [20:03]

```swift
--encrypt "$SRCROOT/HelloFlowers/Models/FlowerStylizer.mlmodelkey"

[Production note] or if we're tight for horizontal space we can use this:

--encrypt "$SRCROOT/.../FlowerStylizer.mlmodelkey"
```

### Working with an encrypted model — [20:50]

```swift
func stylizeImage() {
    // If we already loaded the model, apply the effect
    if let model = flowerStylizer {
        applyStyledEffect(using: model)
        return
    }

    // Otherwise load and apply
    FlowerStylizer.load { [self] result in

        switch result {

        case .success(let model):
            flowerStylizer = model
            DispatchQueue.main.async {
                applyStyledEffect(using: model)
            }

        case .failure(let error):
            handleFailure(for: error)

        }
    }
}

func handleFailure(for error: Error) {
    switch error {
    case MLModelError.modelKeyFetch:
        handleNetworkFailure()

    default:
        handleModelLoadError(error)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10152/7/2EDC8089-D292-4CE8-828D-DCD22EFAD2F9/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10152) — developer.apple.com. Indexed for agent consumption._