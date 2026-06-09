---
id: "wwdc2024-10139"
event: "wwdc2024"
year: 2024
title: "Introducing enterprise APIs for visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10139"
topics: ["AI & Machine Learning", "App Services", "Audio & Video", "Photos & Camera", "Spatial Computing", "Business & Education"]
platforms: ["visionOS"]
hasTranscript: true
---

# Introducing enterprise APIs for visionOS

**Event:** WWDC24 · **Topic:** Business & Education · **Platforms:** visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10139](https://developer.apple.com/videos/play/wwdc2024/10139)

Find out how you can use new enterprise APIs for visionOS to create spatial experiences that enhance employee and customer productivity on Apple Vision Pro.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,774 words)

## Documentation & Resources

- [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis.json
- [Forum: Business & Education](https://developer.apple.com/forums/topics/business-and-education-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/business-and-education-topic?cid=vf-a-0010

## Code Snippets

### Main Camera Feed Access Example — [3:36]

```swift
// Main Camera Feed Access Example

let formats = CameraVideoFormat.supportedVideoFormats(for: .main, cameraPositions:[.left])
let cameraFrameProvider = CameraFrameProvider()

var arKitSession = ARKitSession()
var pixelBuffer: CVPixelBuffer?

await arKitSession.queryAuthorization(for: [.cameraAccess])

do {
    try await arKitSession.run([cameraFrameProvider])
} catch {
    return
}

guard let cameraFrameUpdates = 
    cameraFrameProvider.cameraFrameUpdates(for: formats[0]) else {
    return
}

for await cameraFrame in cameraFrameUpdates {
    guard let mainCameraSample = cameraFrame.sample(for: .left) else {
        continue
    }
    self.pixelBuffer = mainCameraSample.pixelBuffer
}
```

### Spatial barcode & QR code scanning example — [7:47]

```swift
// Spatial barcode & QR code scanning example

await arkitSession.queryAuthorization(for: [.worldSensing])
let barcodeDetection = BarcodeDetectionProvider(symbologies: [.code39, .qr, .upce])

do {
    try await arkitSession.run([barcodeDetection])
} catch {
    return
}

for await anchorUpdate in barcodeDetection.anchorUpdates {
    switch anchorUpdate.event {
        case .added:
           // Call our app method to add a box around a new barcode
           addEntity(for: anchorUpdate.anchor)
        case .updated:
            // Call our app method to move a barcode's box
            updateEntity(for: anchorUpdate.anchor)
       case .removed:
            // Call our app method to remove a barcode's box
            removeEntity(for: anchorUpdate.anchor)
    }
}
```

### Apple Neural Engine access example — [13:17]

```swift
// Apple Neural Engine access example

let availableComputeDevices = MLModel.availableComputeDevices

for computeDevice in availableComputeDevices {
    switch computeDevice {
        case .cpu: setCpuEnabledForML(true) // Example method name
        case .gpu: setGpuEnabledForML(true) // Example method name
        case .neuralEngine: runMyMLModelWithNeuralEngineAvailable() // Example method name
        default: continue
    }
}
```

### Object tracking enhancements example — [15:39]

```swift
// Object tracking enhancements example

var trackingParameters = ObjectTrackingProvider.TrackingConfiguration()

// Increasing our maximum items tracked from 10 to 15
trackingParameters.maximumTrackableInstances = 15

// Leaving all our other parameters at their defaults
trackingParameters.maximumInstancesPerReferenceObject = 1
trackingParameters.detectionRate = 2.0
trackingParameters.stationaryObjectTrackingRate = 5.0
trackingParameters.movingObjectTrackingRate = 5.0

let objectTracking = ObjectTrackingProvider(
        referenceObjects: Array(referenceObjectDictionary.values),
        trackingConfiguration: trackingParameters)

var arkitSession = ARKitSession()
arkitSession.run([objectTracking])
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10139/5/6269882C-FCC9-45DB-ADB4-DAAF5297CFEF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10139/5/6269882C-FCC9-45DB-ADB4-DAAF5297CFEF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10139) — developer.apple.com. Indexed for agent consumption._