---
id: "wwdc2025-300"
event: "wwdc2025"
year: 2025
title: "Enhance your app with machine-learning-based video effects"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/300"
topics: ["Photos & Camera", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance your app with machine-learning-based video effects

**Event:** WWDC25 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-300](https://developer.apple.com/videos/play/wwdc2025/300)

Discover how to add effects like frame rate conversion, super resolution, and noise filtering to improve video editing and live streaming experiences. We’ll explore the ML-based video processing algorithms optimized for Apple Silicon available in the Video Toolbox framework. Learn how to integrate these effects to enhance the capabilities of your app for real-world use cases.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,029 words)

## Documentation & Resources

- [Frame processing](https://developer.apple.com/documentation/VideoToolbox/frame-processing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VideoToolbox/frame-processing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VideoToolbox/frame-processing.json
- [Enhancing your app with machine learning-based video effects](https://developer.apple.com/documentation/VideoToolbox/enhancing-your-app-with-machine-learning-based-video-effects) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VideoToolbox/enhancing-your-app-with-machine-learning-based-video-effects
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VideoToolbox/enhancing-your-app-with-machine-learning-based-video-effects.json
- [Video Toolbox](https://developer.apple.com/documentation/VideoToolbox) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VideoToolbox
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VideoToolbox.json

## Code Snippets

### Frame rate conversion configuration — [8:06]

```swift
// Frame rate conversion configuration


let processor = VTFrameProcessor()

guard let configuration = VTFrameRateConversionConfiguration(frameWidth: width,
                                                            frameHeight: height,
                                                     usePrecomputedFlow: false,
                                                  qualityPrioritization: .normal,
                                                               revision: .revision1)
else {
     throw Fault.failedToCreateFRCConfiguration
}

try processor.startSession(configuration: configuration)
```

### Frame rate conversion buffer allocation — [8:56]

```swift
// Frame rate conversion buffer allocation

//use sourcePixelBufferAttributes and destinationPixelBufferAttributes property of VTFrameRateConversionConfiguration to create source and destination CVPixelBuffer pools

sourceFrame = VTFrameProcessorFrame(buffer: curPixelBuffer, presentationTimeStamp: sourcePTS)
nextFrame = VTFrameProcessorFrame(buffer: nextPixelBuffer, presentationTimeStamp: nextPTS)

// Interpolate 3 frames between reference frames for 4x slow-mo
var interpolationPhase: [Float] = [0.25, 0.5, 0.75]

//create destinationFrames
let destinationFrames = try framesBetween(firstPTS: sourcePTS,
                                           lastPTS: nextPTS,
                            interpolationIntervals: intervals)
```

### Frame rate conversion parameters — [9:48]

```swift
// Frame rate conversion parameters

guard let parameters = VTFrameRateConversionParameters(sourceFrame: sourceFrame,
                                                         nextFrame: nextFrame,
                                                       opticalFlow: nil,
                                                interpolationPhase: interpolationPhase,
                                                    submissionMode: .sequential,
                                                 destinationFrames: destinationFrames)
else {
     throw Fault.failedToCreateFRCParameters
}

try await processor.process(parameters: parameters)
```

### Motion blur process parameters — [12:35]

```swift
// Motion blur process parameters

sourceFrame = VTFrameProcessorFrame(buffer: curPixelBuffer, presentationTimeStamp: sourcePTS)
nextFrame = VTFrameProcessorFrame(buffer: nextPixelBuffer, presentationTimeStamp: nextPTS)
previousFrame = VTFrameProcessorFrame(buffer: prevPixelBuffer, presentationTimeStamp: prevPTS)
destinationFrame = VTFrameProcessorFrame(buffer: destPixelBuffer, presentationTimeStamp: sourcePTS)

guard let parameters = VTMotionBlurParameters(sourceFrame: currentFrame,
                                                nextFrame: nextFrame,
                                            previousFrame: previousFrame,
                                          nextOpticalFlow: nil,
                                      previousOpticalFlow: nil,
                                       motionBlurStrength: strength,
                                           submissionMode: .sequential,
                                         destinationFrame: destinationFrame) 
else {
    throw Fault.failedToCreateMotionBlurParameters
}

try await processor.process(parameters: parameters)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/300/4/be89fd99-ba12-4e24-96ed-a626da355488/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/300/4/be89fd99-ba12-4e24-96ed-a626da355488/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/300) — developer.apple.com. Indexed for agent consumption._