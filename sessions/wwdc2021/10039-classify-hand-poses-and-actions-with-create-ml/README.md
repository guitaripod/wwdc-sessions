---
id: "wwdc2021-10039"
event: "wwdc2021"
year: 2021
title: "Classify hand poses and actions with Create ML"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10039"
topics: ["Spatial Computing", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Classify hand poses and actions with Create ML

**Event:** WWDC21 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10039](https://developer.apple.com/videos/play/wwdc2021/10039)

With Create ML, your app’s ability to understand the expressiveness of the human hand has never been easier. Discover how you can build off the support for Hand Pose Detection in Vision and train custom Hand Pose and Hand Action classifiers using the Create ML app and framework. Learn how simple it is to collect data, train a model, and integrate it with Vision, Camera, and ARKit to create a fun, entertaining app experience. To learn more about Create ML and related concepts around model training, check out “Build an Action Classifier with Create ML” from WWDC20. And don’t miss “Build dynamic iOS apps with the Create ML framework” to learn how your models can be trained on-the-fly and on device from within your app.

**Keywords:** `ai`, `body pose`, `core ml`, `create ml`, `fitness`, `hand action classification`, `hand pose`, `hand pose classification`, `machine learning`, `vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,311 words)

## Documentation & Resources

- [Create ML](https://developer.apple.com/documentation/CreateML) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CreateML
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CreateML.json
- [Vision](https://developer.apple.com/documentation/Vision) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision.json

## Code Snippets

### Detecting hands in a frame — [9:31]

```swift
func session(_ session: ARSession, didUpdate frame: ARFrame) {

    let pixelBuffer = frame.capturedImage 
    let handPoseRequest = VNDetectHumanHandPoseRequest()
    handPoseRequest.maximumHandCount = 1
    handPoseRequest.revision = VNDetectHumanHandPoseRequestRevision1

    let handler = VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:])
    do { 
        try handler.perform([humanBodyPoseRequest]) 
    } catch {
        assertionFailure("Human Pose Request failed: \(error)")
    }

    guard let handPoses = request.results, !handPoses.isEmpty else {
        // No effects to draw, so clear out current graphics
        return
    }
    let handObservation = handPoses.first
```

### Predicting hand pose — [11:03]

```swift
if frameCounter % handPosePredictionInterval == 0 {

    guard let keypointsMultiArray = try? handObservation.keypointsMultiArray() 
else { fatalError() }
    let handPosePrediction = try model.prediction(poses: keypointsMultiArray)
    let confidence = handPosePrediction.labelProbabilities[handPosePrediction.label]!

    if confidence > 0.9 {
       renderHandPoseEffect(name: handPosePrediction.label)
    }
}

func renderHandPoseEffect(name: String) {
	switch name {
        case "One": 
            if effectNode == nil {
               effectNode = addParticleNode(for: .one)
            }
        default:
			removeAllParticleNode()
	}
}
```

### Getting tip of index finger to use as anchor — [12:25]

```swift
let landmarkConfidenceThreshold: Float = 0.2

let indexFingerName = VNHumanHandPoseObservation.JointName.indexTip

let width = viewportSize.width
let height = viewportSize.height

if let indexFingerPoint = try? observation.recognizedPoint(indexFingerName),
   indexFingerPoint.confidence > landmarkConfidenceThreshold {

    let normalizedLocation = indexFingerPoint.location
    indexFingerTipLocation = CGPoint((x: normalizedLocation.x * width,
                                      y: normalizedLocation.y * height))
} else {
    indexFingerTipLocation = nil
}
```

### Getting hand chirality — [15:47]

```swift
// Working with chirality

let handPoseRequest = VNDetectHumanHandPoseRequest()
try handler.perform([handPoseRequest])
let detectedHandPoses = handPoseRequest.results!

for hand in detectedHandPoses where hand.chirality == .right {
    // Take action on every right hand, or prune the results
}
```

### Hand action classification by accumulating queue of hand poses — [22:16]

```swift
var queue = [MLMultiArray]()
// . . .
frameCounter += 1
if frameCounter % 2 == 0 {
    let hands: [(MLMultiArray, VNHumanHandPoseObservation.Chirality)] = getHands()
    for (pose, chirality) in hands where chirality == .right {
        queue.append(pose)
        queue = Array(queue.suffix(queueSize))
        queueSamplingCounter += 1
        if queue.count == queueSize && queueSamplingCounter % queueSamplingCount == 0 {
            let poses = MLMultiArray(concatenating: queue, axis: 0, dataType: .float32)
            let prediction = try? handActionModel?.prediction(poses: poses)
            guard let label = prediction?.label, 
              let confidence = prediction?.labelProbabilities[label] else { continue }
            if confidence > handActionConfidenceThreshold {
                DispatchQueue.main.async {
                    self.renderer?.renderHandActionEffect(name: label)
                }
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10039/6/21ABF0C5-D90C-4198-9791-027910A0EE4A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10039/6/21ABF0C5-D90C-4198-9791-027910A0EE4A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10039) — developer.apple.com. Indexed for agent consumption._
