---
id: "wwdc2021-10037"
event: "wwdc2021"
year: 2021
title: "Build dynamic iOS apps with the Create ML framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10037"
topics: ["Photos & Camera", "Privacy & Security", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build dynamic iOS apps with the Create ML framework

**Event:** WWDC21 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10037](https://developer.apple.com/videos/play/wwdc2021/10037)

Discover how your app can train Core ML models fully on device with the Create ML framework, enabling adaptive and customized app experiences, all while preserving data privacy. We'll explore the types of models that can be created on-the-fly for image-based tasks like Style Transfer and Image Classification, audio tasks like custom Sound Classification, or tasks that build on a rich set of Text Classification, Tabular Data Classification, and Tabular Regressors. And we'll take you through the many opportunities these models offer to make your app more personal and dynamic.

For even more inspiration, check out “Classify hand poses and actions with Create ML” and “Discover built-in sound classification in SoundAnalysis” from WWDC21.

**Keywords:** `ai`, `core ml`, `create ml`, `create ml framework`, `machine learning`, `on-device training`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,525 words)

## Documentation & Resources

- [Create ML](https://developer.apple.com/documentation/CreateML) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CreateML
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CreateML.json

## Code Snippets

### Training a style transfer model — [7:58]

```swift
// define training data source
let data = MLStyleTransfer.DataSource.images(styleImage: styleUrl, contentDirectory: contentUrl)

// define session parameter
let sessionParameters = MLTrainingSessionParameters(sessionDirectory: sessionUrl)

// define training job
let job = try MLStyleTransfer.train(trainingData: data, sessionParameters: sessionParameters)

// dispatch training job 
// save out model upon receiving successful completion, compile for later use
// make prediction with CoreML model
try model.write(to: writeToUrl)
let compiledURL = try MLModel.compileModel(at: writeToUrl)
let mlModel = try MLModel(contentsOf: compiledURL)
let inputImage = try MLDictionaryFeatureProvider(dictionary: ["image": image])
let stylizedImage = try mlModel.prediction(from: inputImage)
```

### Collecting features for a regressor — [13:39]

```swift
func featuresFromMealAndKeywords(meal: String, keywords: [String]) -> [String: Double] {

    // Capture interactions between content (the dish keywords) and context (meal) by
    // adding a copy of each keyword modified to include the meal.
    let featureNames = keywords + keywords.map { meal + ":" + $0 }

    // For each keyword, create an entry in a dictionary of features with a value of 1.0.
    return featureNames.reduce(into: [:]) { features, name in
        features[name] = 1.0
    }
}
```

### Preparing training data — [14:08]

```swift
var trainingKeywords: [[String: Double]] = []
var trainingTargets: [Double] = []

for item in userPurchasedItems {
    // Add in the positive example.
    trainingKeywords.append(
       featuresFromMealAndKeywords(meal: item.meal, keywords: item.keywords))
    trainingTargets.append(1.0)

    // Add in the negative example.
    let negativeKeywords = allKeywords.subtracting(item.keywords)
    trainingKeywords.append(
       featuresFromMealAndKeywords(meal: item.meal, keywords: Array(negativeKeywords)))
    trainingTargets.append(-1.0)
}
```

### Training a linear regressor model — [14:37]

```swift
// Create the training data.
var trainingData = DataFrame()
trainingData.append(column: Column(name: "keywords" contents: trainingKeywords))
trainingData.append(column: Column(name: "target", contents: trainingTargets))

// Create the model.
let model = try MLLinearRegressor(trainingData: trainingData, targetColumn: "target")
```

### Making a prediction — [14:58]

```swift
// Setup the data to run an inference on.
var inputData = DataFrame()
inputData.append(column: Column(name: "keywords", contents: dishKeywords))

// Call predictions on the trained model with the data.
let predictions = try model.predictions(from: inputData)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10037/3/4705B592-C85E-4872-A252-5C377A1022D6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10037/3/4705B592-C85E-4872-A252-5C377A1022D6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10037) — developer.apple.com. Indexed for agent consumption._