---
id: "wwdc2024-10094"
event: "wwdc2024"
year: 2024
title: "Explore game input in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10094"
topics: ["Design", "Spatial Computing", "Graphics & Games"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore game input in visionOS

**Event:** WWDC24 · **Topic:** Graphics & Games · **Platforms:** visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10094](https://developer.apple.com/videos/play/wwdc2024/10094)

Discover how to design and implement great input for your game in visionOS. Learn how system gestures let you provide frictionless ways for players to interact with your games. And explore best practices for supporting custom gestures and game controllers.


**Keywords:** `apple vision pro`, `avp`, `gestures`, `mixed reality`, `spatial`, `spatial design`, `virtual reality`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,634 words)

## Documentation & Resources

- [Human Interface Guidelines: Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/gestures
- [Forum: Graphics & Games](https://developer.apple.com/forums/topics/graphics-and-games?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/graphics-and-games?cid=vf-a-0010
- [Human Interface Guidelines: Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-controls
- [Composing SwiftUI gestures](https://developer.apple.com/documentation/SwiftUI/Composing-SwiftUI-Gestures) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Composing-SwiftUI-Gestures
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Composing-SwiftUI-Gestures.json

## Code Snippets

### Respond to a tap gesture — [5:16]

```swift
// Respond to a tap gesture.

struct ContentView: View {
  var body: some View {
    RealityView { content in
      // For entity targeting to work, entities must have an InputTargetComponent
      // and a CollisionComponent!
    }
    .gesture(TapGesture().targetedToAnyEntity().onEnded { value in
      print("Tapped entity \(value.entity)!")
    })
  }
}
```

### Combine dragging, magnification, and 3D rotation gestures — [7:08]

```swift
// Gesture combining dragging, magnification, and 3D rotation all at once.
var manipulationGesture: some Gesture<AffineTransform3D> {
  DragGesture()
    .simultaneously(with: MagnifyGesture())
    .simultaneously(with: RotateGesture3D())
    .map {bgesture in
      let (translation, scale, rotation) = gesture.components()

      return AffineTransform3D(
        scale: scale,
        rotation: rotation,
        translation: translation
      )
    }
}
```

### Create and detect a custom circle gesture — [9:33]

```swift
// Create and detect a custom circle gesture.

// Get all required joints and check if they are tracked.
let leftHandIndexFingerTip = leftHandAnchor.skeleton.joint(named: .handIndexFingerTip)
// ...
// Get the position of all joints in world coordinates.
let leftHandIndexFingerTipWorldPosition = matrix_multiply(leftHandAnchor.originFromAnchorTransform, 
                leftHandIndexFingerTip.anchorFromJointTransform).columns.3.xyz
// ...

// Circle gesture detection is true when the distance between the index finger tips centers
// and the distance between the thumb tip centers is each less than four centimeters.
let isCircleShapeGesture = indexFingersDistance < 0.04 && thumbsDistance < 0.04
if isCircleShapeGesture {
  // respond to gesture
}
```

### Detect a connected game controller — [14:00]

```swift
// Detect connected game controller.

// Add handler for when controller connects.
    NotificationCenter.default.addObserver(
	      forName: NSNotification.Name.GCControllerDidConnect,
  	    object: nil, queue: nil) {
    	      (note) in
      	      guard let _controller = note.object? as GCController else { return }
        	    // Add controller input change handlers.
          	  _controller.physicalInputProfile[GCInputButtonA]?.valueChangedHandler = {
            	  //... 
            	}
       	}

// Poll for controller input
    if controller.physicalInputProfile[GCInputButtonA]?.pressed {... }
    if controller.physicalInputProfile[GCInputButtonB]?.pressed {... }
```

### Tag a RealityView to handle controller input — [14:24]

```swift
// Tag a RealityView to handle controller input.

struct ContentView: View {
  var body: some View {
    RealityView { content in
      // Tag your RealityView to respond to controller input events.
    }
    .handlesGameControllerEvents(matching .gamepad)
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10094/8/0A68B37C-75FF-4E8E-BA54-BA0865E665A3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10094/8/0A68B37C-75FF-4E8E-BA54-BA0865E665A3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10094) — developer.apple.com. Indexed for agent consumption._