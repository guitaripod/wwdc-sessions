---
id: "wwdc2021-10036"
event: "wwdc2021"
year: 2021
title: "Discover built-in sound classification in SoundAnalysis"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10036"
topics: ["AI & Machine Learning", "SwiftUI & UI Frameworks", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Discover built-in sound classification in SoundAnalysis

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10036](https://developer.apple.com/videos/play/wwdc2021/10036)

Explore how you can use the Sound Analysis framework in your app to detect and classify discrete sounds from any audio source — including live sounds from a microphone or from a video or audio file — and identify precisely in a moment where that sound occurs. Learn how the built-in sound classifier makes it easy for you to identify over 300 different types of sounds without the need for a custom trained model. This includes a variety of noises, ranging from human sounds, musical instruments, animals, and various items.

For custom models, see how you can leverage the Audio Feature Print feature extractor to create smaller models with variable sound window control to better serve your app’s purposes.

For more about Sound Classification and the Sound Analysis framework, watch “Training Sound Classification Models in Create ML” from WWDC19.

**Keywords:** `audio`, `core ml`, `create ml`, `create ml framework`, `machine learning`, `sound`, `sound analysis`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,688 words)

## Documentation & Resources

- [Classifying Live Audio Input with a Built-in Sound Classifier](https://developer.apple.com/documentation/SoundAnalysis/classifying-live-audio-input-with-a-built-in-sound-classifier) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SoundAnalysis/classifying-live-audio-input-with-a-built-in-sound-classifier
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SoundAnalysis/classifying-live-audio-input-with-a-built-in-sound-classifier.json
- [Sound Analysis](https://developer.apple.com/documentation/SoundAnalysis) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SoundAnalysis
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SoundAnalysis.json

## Code Snippets

### Get list of recognized sounds — [8:12]

```swift
func getListOfRecognizedSounds() throws -> [String] {
    let request = try SNClassifySoundRequest(classifierIdentifier: .version1)
    return request.knownClassifications
}
```

### Create sound classification request — [9:19]

```swift
let request = try SNClassifySoundRequest(classifierIdentifier: .version1)

let analyzer = try SNAudioFileAnalyzer(url: url)

var observer: SNResultsObserving // TODO

try analyzer.add(request, withObserver: observer)
analyzer.analyze()
```

### Implement sound classification observer — [9:52]

```swift
class FirstDetectionObserver: NSObject, SNResultsObserving {
    var firstDetectionTime = CMTime.invalid
    var label: String

    init(label: String) {
        self.label = label
    }

    func request(_ request: SNRequest, didProduce result: SNResult) {
        if let result = result as? SNClassificationResult,
           let classification = result.classification(forIdentifier: label),
           classification.confidence > 0.5,
           firstDetectionTime == CMTime.invalid {
                firstDetectionTime = result.timeRange.start
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10036/7/E21A5457-DFA1-405D-87E4-EBCCB8A6F0C1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10036/7/E21A5457-DFA1-405D-87E4-EBCCB8A6F0C1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10036) — developer.apple.com. Indexed for agent consumption._