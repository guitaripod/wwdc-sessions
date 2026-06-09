---
id: "wwdc2021-10073"
event: "wwdc2021"
year: 2021
title: "Explore ARKit 5"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10073"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Explore ARKit 5

**Event:** WWDC21 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10073](https://developer.apple.com/videos/play/wwdc2021/10073)

Build the next generation of augmented reality apps with ARKit 5. Explore how you can use Location Anchors in additional regions and more easily onboard people into your location-based AR experience. Learn more about Face Tracking and Motion Capture. And discover best practices for placing your AR content in the real world. We’ll also show you how you can integrate App Clip Codes into your AR app for easy discovery and precise positioning of your virtual content.

**Keywords:** `app clip codes`, `ar`, `arkit`, `augmented reality`, `body tracking`, `depth map`, `face tracking`, `lidar`, `location anchor`, `realitykit`, `scene reconstruction`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,516 words)

## Documentation & Resources

- [Human Interface Guidelines: App Clip Codes](https://developer.apple.com/design/human-interface-guidelines/app-clips/overview/app-clip-codes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/app-clips/overview/app-clip-codes
- [Interacting with App Clip Codes in AR](https://developer.apple.com/documentation/AppClip/interacting-with-app-clip-codes-in-ar) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/interacting-with-app-clip-codes-in-ar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/interacting-with-app-clip-codes-in-ar.json
- [Explore the ARKit Developer Forums](https://developer.apple.com/forums/tags/arkit) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/arkit
- [Tracking geographic locations in AR](https://developer.apple.com/documentation/ARKit/tracking-geographic-locations-in-ar) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/tracking-geographic-locations-in-ar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/tracking-geographic-locations-in-ar.json
- [ARKit](https://developer.apple.com/documentation/ARKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit.json

## Code Snippets

### Geo Tracking Recap I — [3:29]

```swift
// Check device support for geo-tracking
guard ARGeoTrackingConfiguration.isSupported else {
    // Geo-tracking not supported on this device
    return
}

// Check current location is supported for geo-tracking
ARGeoTrackingConfiguration.checkAvailability { (available, error) in
    guard available else {
        // Geo-tracking is not available at this location
        return
    }

    // Run ARSession
    let arView = ARView()
    arView.session.run(ARGeoTrackingConfiguration())
}
```

### Geo Tracking Recap II — [3:42]

```swift
// Create Location Anchor and add to session
let coordinate = CLLocationCoordinate2D(latitude: 37.795313, longitude: -122.393792)
let geoAnchor = ARGeoAnchor(name: “Ferry Building”, coordinate: coordinate)
arView.session.add(anchor: geoAnchor)

// Monitor geo-tracking status updates
func session(_ session: ARSession, didChange geoTrackingStatus: ARGeoTrackingStatus) {
    …
}
```

### Geo Tracking Coaching Overlay — [6:02]

```swift
// Declare coaching view
let coachingOverlay = ARCoachingOverlayView()

// Set up coaching view (assuming ARView already exists)
coachingOverlay.session = self.arView.session
coachingOverlay.delegate = self
coachingOverlay.goal = .geoTracking

coachingOverlay.translatesAutoresizingMaskIntoConstraints = false
self.arView.addSubview(coachingOverlay)

NSLayoutConstraint.activate([
    coachingOverlay.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    coachingOverlay.centerYAnchor.constraint(equalTo: view.centerYAnchor),
    coachingOverlay.widthAnchor.constraint(equalTo: view.widthAnchor),
    coachingOverlay.heightAnchor.constraint(equalTo: view.heightAnchor),
])
```

### GeoTracking Distance Method — [8:53]

```swift
// Method to compute distance (in meters) between points
func distance(from location: CLLocation) -> CLLocationDistance
```

### App Clip Code: check device support — [12:16]

```swift
func viewDidLoad() {
    // Check device support for app clip code tracking
    guard ARWorldTrackingConfiguration.supportsAppClipCodeTracking else { return }

    let worldConfig = ARWorldTrackingConfiguration()
    worldConfig.appClipCodeTrackingEnabled = true
    arSession.run(worldConfig)
}
```

### Accessing the URL of an App Clip Code — [12:34]

```swift
/// Accessing the URL of an App Clip Code 
override func session(_ session: ARSession, didUpdate anchors: [ARAnchor]) {
    for anchor in anchors {
        guard let appClipCodeAnchor = anchor as? ARAppClipCodeAnchor, appClipCodeAnchor.isTracked else { return }

        switch appClipCodeAnchor.urlDecodingState {
        case .decoding:
            displayPlaceholderVisualizationOnTopOf(anchor: appClipCodeAnchor)
        case .failed:
            displayNoURLErrorMessageOnTopOf(anchor: appClipCodeAnchor)
        case .decoded:
            let url = appClipCodeAnchor.url!
            let anchorEntity = AnchorEntity(anchor: appClipCodeAnchor)
            arView.scene.addAnchor(anchorEntity)
            let visualization = AppClipCodeVisualization(url: url, radius: appClipCodeAnchor.radius)
            anchorEntity.addChild(visualization)
          }
    }
}
```

### Adding a gesture recognizer — [15:34]

```swift
/// Adding a gesture recognizer for user interaction
func viewDidLoad() {
    initializeARView()
    initializeCoachingOverlays()

    // Place sunflower on the ground when the user taps the screen
    let tapGestureRecognizer = UITapGestureRecognizer(
     target: self,
     action: #selector(handleTap(recognizer:)))
    arView.addGestureRecognizer(tapGestureRecognizer)
}
```

### Tap to place the sunflower — [15:45]

```swift
func handleTap(recognizer: UITapGestureRecognizer) {
    let location = recognizer.location(in: arView)
    // Attempt to find a 3D location on a horizontal
    // surface underneath the user's touch location.
    let results = arView.raycast(
      from: location, 
      allowing: .estimatedPlane,
      alignment: .horizontal)
    guard let firstResult = results.first else { return }
    // Fetch the last decoded app clip code URL
    guard let appClipCodeURL = decodedURLs.last else { return }
    // Add an ARAnchor & AnchorEntity at the touch location
    let anchor = ARAnchor(transform: firstResult.worldTransform)
    arView.session.add(anchor: anchor)
    let anchorEntity = AnchorEntity(anchor: anchor)
    arView.scene.addAnchor(anchorEntity)    
    // Download the 3D model associated with this app clip code.
    downloadAndDisplay(appClipCodeURL, on: anchorEntity)
}
```

### Checking for supported video formats for face tracking — [18:33]

```swift
// Check if the ultra wide video format is available.
// If so, set it on a face tracking configuration & run the session with that.

let config = ARFaceTrackingConfiguration()
for videoFormat in ARFaceTrackingConfiguration.supportedVideoFormats {
    if videoFormat.captureDeviceType == .builtInUltraWideCamera {
        config.videoFormat = videoFormat
        break
    }
}
session.run(config)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10073/7/53148F9F-7E28-46AA-AD05-CC2ABEC68EDC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10073/7/53148F9F-7E28-46AA-AD05-CC2ABEC68EDC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10073) — developer.apple.com. Indexed for agent consumption._
