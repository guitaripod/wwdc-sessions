---
id: "wwdc2025-319"
event: "wwdc2025"
year: 2025
title: "Capture cinematic video in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/319"
topics: ["Photos & Camera", "Audio & Video"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Capture cinematic video in your app

**Event:** WWDC25 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-319](https://developer.apple.com/videos/play/wwdc2025/319)

Discover how the Cinematic Video API enables your app to effortlessly capture cinema-style videos. We’ll cover how to configure a Cinematic capture session and introduce the fundamentals of building a video capture UI. We’ll also explore advanced Cinematic features such as applying a depth of field effect to achieve both tracking and rack focus.

**Keywords:** `camera`, `capture`, `cinematic`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,532 words)

## Documentation & Resources

- [Capturing Cinematic video](https://developer.apple.com/documentation/AVFoundation/capturing-cinematic-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-cinematic-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-cinematic-video.json
- [Cinematic](https://developer.apple.com/documentation/Cinematic) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Cinematic
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Cinematic.json
- [AVCam: Building a camera app](https://developer.apple.com/documentation/AVFoundation/avcam-building-a-camera-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/avcam-building-a-camera-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/avcam-building-a-camera-app.json
- [AVFoundation](https://developer.apple.com/documentation/AVFoundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation.json

## Code Snippets

### Select a video device — [4:26]

```swift
// Select a video device

let deviceDiscoverySession = AVCaptureDevice.DiscoverySession(deviceTypes: [.builtInDualWideCamera], mediaType: .video, position: .back)

guard let camera = deviceDiscoverySession.devices.first else {
    print("Failed to find the capture device")
    return
}
```

### Select a format that supports Cinematic Video capture — [5:07]

```swift
// Select a format that supports Cinematic Video capture

for format in camera.formats {

    if format.isCinematicVideoCaptureSupported {

       try! camera.lockForConfiguration()
       camera.activeFormat = format
       camera.unlockForConfiguration()

       break
    }

}
```

### Select a microphone — [5:51]

```swift
// Select a microphone

let audioDeviceDiscoverySession = AVCaptureDevice.DiscoverySession(deviceTypes [.microphone], mediaType: .audio, position: .unspecified)

guard let microphone = audioDeviceDiscoverySession.devices.first else {
    print("Failed to find a microphone")
    return
}
```

### Add devices to input & add inputs to the capture session & enable Cinematic Video capture — [6:00]

```swift
// Add devices to inputs

let videoInput = try! AVCaptureDeviceInput(device: camera)
guard captureSession.canAddInput(videoInput) else {
    print("Can't add the video input to the session")
    return
}

let audioInput = try! AVCaptureDeviceInput(device: microphone)
guard captureSession.canAddInput(audioInput) else {
    print("Can't add the audio input to the session")
    return
}

// Add inputs to the capture session

captureSession.addInput(videoInput)
captureSession.addInput(audioInput)

// Enable Cinematic Video capture

if (videoInput.isCinematicVideoCaptureSupported) {
  videoInput.isCinematicVideoCaptureEnabled = true
}
```

### Capture spatial audio — [6:17]

```swift
// Configure spatial audio

if audioInput.isMultichannelAudioModeSupported(.firstOrderAmbisonics) {
    audioInput.multichannelAudioMode = .firstOrderAmbisonics
}
```

### Add outputs to the session & configure video stabilization & associate the preview layer with the capture session — [6:33]

```swift
// Add outputs to the session

let movieFileOutput = AVCaptureMovieFileOutput()
guard captureSession.canAddOutput(movieFileOutput) else {
    print("Can't add the movie file output to the session")
    return
}
captureSession.addOutput(movieFileOutput)


// Configure video stabilization

if let connection = movieFileOutput.connection(with: .video), 
    connection.isVideoStabilizationSupported {
    connection.preferredVideoStabilizationMode = .cinematicExtendedEnhanced
}

// Add a preview layer as the view finder

let previewLayer = AVCaptureVideoPreviewLayer()
previewLayer.session = captureSession
```

### Display the preview layer with SwiftUI — [7:11]

```swift
// Display the preview layer with SwiftUI

struct CameraPreviewView: UIViewRepresentable {

    func makeUIView(context: Context) -> PreviewView {
        return PreviewView()
    }

    class CameraPreviewUIView: UIView {

			override class var layerClass: AnyClass {
    		AVCaptureVideoPreviewLayer.self
			}

			var previewLayer: AVCaptureVideoPreviewLayer {
  	  	layer as! AVCaptureVideoPreviewLayer
			}

			...
		}

...
}
```

### Display the preview layer with SwiftUI — [7:54]

```swift
// Display the preview layer with SwiftUI

@MainActor
struct CameraView: View {       

    var body: some View {
        ZStack {
            CameraPreviewView()  
          	CameraControlsView()
        }
    }
}
```

### Adjust bokeh strength with simulated aperture — [8:05]

```swift
// Adjust bokeh strength with simulated aperture


open class AVCaptureDeviceInput : AVCaptureInput {

	open var simulatedAperture: Float

	...

}
```

### Find min, max, and default simulated aperture — [8:40]

```swift
// Adjust bokeh strength with simulated aperture


extension AVCaptureDeviceFormat {

	open var minSimulatedAperture: Float { get }

	open var maxSimulatedAperture: Float { get }

	open var defaultSimulatedAperture: Float { get }

	...

}
```

### Add a metadata output — [9:12]

```swift
// Add a metadata output

let metadataOutput = AVCaptureMetadataOutput()

guard captureSession.canAddOutput(metadataOutput) else {
    print("Can't add the metadata output to the session")
    return
}
captureSession.addOutput(metadataOutput)

metadataOutput.metadataObjectTypes = metadataOutput.requiredMetadataObjectTypesForCinematicVideoCapture

metadataOutput.setMetadataObjectsDelegate(self, queue: sessionQueue)
```

### Update the observed manager object — [9:50]

```swift
// Update the observed manager object

func metadataOutput(_ output: AVCaptureMetadataOutput, didOutput metadataObjects: [AVMetadataObject], from connection: AVCaptureConnection) {

   self.metadataManager.metadataObjects = metadataObjects

}

// Pass metadata to SwiftUI

@Observable
class CinematicMetadataManager {

    var metadataObjects: [AVMetadataObject] = []

}
```

### Observe changes and update the view — [10:12]

```swift
// Observe changes and update the view

struct FocusOverlayView : View {

    var body: some View {

	        ForEach(
	      metadataManager.metadataObjects, id:\.objectID)
		  	{ metadataObject in

    		  rectangle(for: metadataObject)

			  }
		}
}
```

### Make a rectangle for a metadata — [10:18]

```swift
// Make a rectangle for a metadata

private func rectangle(for metadata: AVMetadataObjects) -> some View {

    let transformedRect = previewLayer.layerRectConverted(fromMetadataOutputRect: metadata.bounds)

    return Rectangle()
        .frame(width:transformedRect.width,
               height:transformedRect.height)
        .position(
            x:transformedRect.midX,
            y:transformedRect.midY)
}
```

### Focus methods — [10:53]

```swift
open func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)

open func setCinematicVideoTrackingFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)

open func setCinematicVideoFixedFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

### Focus method 1 & CinematicVideoFocusMode — [10:59]

```swift
// Focus methods

open func setCinematicVideoTrackingFocus(detectedObjectID: Int, focusMode: AVCaptureDevice.CinematicVideoFocusMode)


public enum CinematicVideoFocusMode : Int, @unchecked Sendable {

    case none = 0

    case strong = 1

    case weak = 2
}

extension AVMetadataObject {

   open var cinematicVideoFocusMode: Int32 { get }

}
```

### Focus method no.2 — [12:19]

```swift
// Focus method no.2

open func setCinematicVideoTrackingFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

### Focus method no.3 — [12:41]

```swift
// Focus method no.3

open func setCinematicVideoFixedFocus(at point: CGPoint, focusMode: AVCaptureDevice.CinematicVideoFocusMode)
```

### Create the spatial tap gesture — [13:54]

```swift
var body: some View {

let spatialTapGesture = SpatialTapGesture()
    .onEnded { event in
        Task {
            await camera.focusTap(at: event.location)
        }
     }

...
}
```

### Simulate a long press gesture with a drag gesture — [14:15]

```swift
@State private var pressLocation: CGPoint = .zero
@State private var isPressing = false
private let longPressDuration: TimeInterval = 0.3

var body: some View {

  ...

	let longPressGesture = DragGesture(minimumDistance: 0).onChanged { value in
		if !isPressing {
			isPressing = true
			pressLocation = value.location
			startLoopPressTimer()
		}
	}.onEnded { _ in
		isPressing = false
	}

	...

}

private func startLoopPressTimer() {
	DispatchQueue.main.asyncAfter(deadline: .now() + longPressDuration) {
		if isPressing {
			Task {
				await camera.focusLongPress(at: pressLocation)
			}
		}
	}
}
```

### Create a rectangle view to receive gestures. — [14:36]

```swift
var body: some View {

let spatialTapGesture = ...
let longPressGesture = ...

ZStack {
  ForEach(
    metadataManager.metadataObjects,
    id:\.objectID)
  { metadataObject in

    rectangle(for: metadataObject)

  }
  Rectangle()
      .fill(Color.clear)
      .contentShape(Rectangle())
      .gesture(spatialTapGesture)
  .gesture(longPressGesture)}

  }
}
```

### Create the rectangle view — [15:03]

```swift
private func rectangle(for metadata: AVMetadataObject) -> some View {

    let transformedRect = previewLayer.layerRectConverted(fromMetadataOutputRect: metadata.bounds)
    var color: Color
    var strokeStyle: StrokeStyle

    switch metadata.focusMode {
    case .weak:
        color = .yellow
        strokeStyle = StrokeStyle(lineWidth: 2, dash: [5,4])
    case .strong:
        color = .yellow
        strokeStyle = StrokeStyle(lineWidth: 2)
    case .none:
        color = .white
        strokeStyle = StrokeStyle(lineWidth: 2)
    }

    return Rectangle()
        .stroke(color, style: strokeStyle)
        .contentShape(Rectangle())
        .frame(width: transformedRect.width, height: transformedRect.height)
        .position(x: transformedRect.midX, 
                  y: transformedRect.midY)
}
```

### Implement focusTap — [15:30]

```swift
func focusTap(at point:CGPoint) {

   try! camera.lockForConfiguration()

    if let metadataObject = findTappedMetadataObject(at: point) {
        if metadataObject.cinematicVideoFocusMode == .weak {
            camera.setCinematicVideoTrackingFocus(detectedObjectID: metadataObject.objectID, focusMode: .strong)

        }
        else {
            camera.setCinematicVideoTrackingFocus(detectedObjectID: metadataObject.objectID, focusMode: .weak)
        }
    }
    else {
        let transformedPoint = previewLayer.metadataOutputRectConverted(fromLayerRect: CGRect(origin:point, size:.zero)).origin
        camera.setCinematicVideoTrackingFocus(at: transformedPoint, focusMode: .weak)
    }

    camera.unlockForConfiguration()
}
```

### Implement findTappedMetadataObject — [15:42]

```swift
private func findTappedMetadataObject(at point: CGPoint) -> AVMetadataObject? {

    var metadataObjectToReturn: AVMetadataObject?

    for metadataObject in metadataObjectsArray {
        let layerRect = previewLayer.layerRectConverted(fromMetadataOutputRect: metadataObject.bounds)
        if layerRect.contains(point) {
            metadataObjectToReturn = metadataObject
            break
        }
    }

    return metadataObjectToReturn
}
```

### focusTap implementation continued — [16:01]

```swift
func focusTap(at point:CGPoint) {

   try! camera.lockForConfiguration()

    if let metadataObject = findTappedMetadataObject(at: point) {
        if metadataObject.cinematicVideoFocusMode == .weak {
            camera.setCinematicVideoTrackingFocus(detectedObjectID: metadataObject.objectID, focusMode: .strong)

        }
        else {
            camera.setCinematicVideoTrackingFocus(detectedObjectID: metadataObject.objectID, focusMode: .weak)
        }
    }
    else {
        let transformedPoint = previewLayer.metadataOutputRectConverted(fromLayerRect: CGRect(origin:point, size:.zero)).origin
        camera.setCinematicVideoTrackingFocus(at: transformedPoint, focusMode: .weak)
    }

    camera.unlockForConfiguration()
}
```

### Implement focusLongPress — [16:23]

```swift
func focusLongPress(at point:CGPoint) {

   try! camera.lockForConfiguration()

   let transformedPoint = previewLayer.metadataOutputRectConverted(fromLayerRect:CGRect(origin: point, size: CGSizeZero)).origin
       camera.setCinematicVideoFixedFocus(at: pointInMetadataOutputSpace, focusMode: .strong)

    camera.unlockForConfiguration()
}
```

### Introduce cinematicVideoCaptureSceneMonitoringStatuses — [17:10]

```swift
extension AVCaptureDevice {

   open var cinematicVideoCaptureSceneMonitoringStatuses: Set<AVCaptureSceneMonitoringStatus> { get }

}

extension AVCaptureSceneMonitoringStatus {

   public static let notEnoughLight: AVCaptureSceneMonitoringStatus

}
```

### KVO handler for cinematicVideoCaptureSceneMonitoringStatuses — [17:42]

```swift
private var observation: NSKeyValueObservation?

observation = camera.observe(\.cinematicVideoCaptureSceneMonitoringStatuses, options: [.new, .old]) { _, value in

    if let newStatuses = value.newValue {
        if newStatuses.contains(.notEnoughLight) {
            // Update UI (e.g., "Not enough light")
        }
        else if newStatuses.count == 0 {
            // Back to normal.
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/319/4/55797f51-c074-44e8-85fe-5aaa0780ba91/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/319/4/55797f51-c074-44e8-85fe-5aaa0780ba91/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/319) — developer.apple.com. Indexed for agent consumption._
