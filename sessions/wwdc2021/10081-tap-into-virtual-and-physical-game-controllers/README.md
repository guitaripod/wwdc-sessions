---
id: "wwdc2021-10081"
event: "wwdc2021"
year: 2021
title: "Tap into virtual and physical game controllers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10081"
topics: ["Design", "Essentials", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Tap into virtual and physical game controllers

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10081](https://developer.apple.com/videos/play/wwdc2021/10081)

It’s time to up your input game: Learn about the latest improvements to virtual and physical game controllers for iPhone, iPad, Mac, and Apple TV. Meet the virtual on-screen controller, which turns touch input into game controller input, and find out how to add controller sharing features to your app. We’ll also show you how to support adaptive trigger technology found in DualSense controllers, provide best practices for controller support, and take you through some common pre-flight checks around accessible and customizable input before submitting to the App Store. For more information on saving highlight clips from a game controller, check out “Discover rolling clips in ReplayKit” from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,643 words)

## Documentation & Resources

- [GCVirtualController](https://developer.apple.com/documentation/GameController/GCVirtualController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameController/GCVirtualController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameController/GCVirtualController.json
- [Game Controller](https://developer.apple.com/documentation/GameController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameController.json

## Code Snippets

### GameController Basics — [2:06]

```swift
func setupGameController() {
    // Add handler for when controller connects.
    NotificationCenter.default.addObserver(
        forName: NSNotification.Name.GCControllerDidConnect,
        object: nil,
        queue: nil)
        { (note) in
            guard let _controller = note.object? as GCController else {
              return
            }
            // Add controller input change handlers.
            _controller.physicalInputProfile[GCInputButtonA]?.valueChangedHandler = { ... }
            _controller.physicalInputProfile[GCInputButtonB]?.valueChangedHandler = { ... }
        }

    // Add handler for when controller disconnects.
    NotificationCenter.default.addObserver(
        forName: NSNotification.Name.GCControllerDidDisconnect,
        object: nil,
        queue: nil)
        { (note) in ... }
}

// Polling for controller input.
func checkInput() {
    if controller.physicalInputProfile[GCInputButtonA]?.pressed { ... }
    if controller.physicalInputProfile[GCInputButtonB]?.pressed { ... }
}
```

### Virtual Controller Initial — [8:42]

```swift
// Creating an on-screen controller

let virtualConfiguration = GCVirtualControllerConfiguration()

virtualConfiguration.elements = [GCInputLeftThumbstick,
                                 GCInputRightThumbstick,
                                 GCInputButtonA,
                                 GCInputButtonB]

let virtualController = GCVirtualController(configuration: virtualConfiguration)

virtualController.connect()
```

### Customizing Buttons — [9:17]

```swift
// Creating customized buttons

vc.changeElement(GCInputButtonA) { 
  config in
    let spinningPath = UIBezierPath()
    // load or draw the spinning attack path
    config.path = spinningPath
    return config
}

vc.changeElement(GCInputButtonB) {
  config in
    let jumpPath = UIBezierPath()
    // load or draw the jump path
    config.path = jumpPath
    return config
}
```

### DualSense Adaptive Triggers — [12:06]

```swift
func updateControllerAdaptiveTriggers() {
  guard let dualSense = GCController.current?.physicalInputProfile as? GCDualSenseGamepad
    else {
        return
    }
  let adaptiveTrigger = dualSense.rightTrigger
  if playerIsPullingSlingshot {
    let resistiveStrength = min(1, 0.4 + adaptiveTrigger.value)
    if adaptiveTrigger.value < 0.9 {
      adaptiveTrigger.setModeFeedbackWithStartPosition(
        0,
        resistiveStrength: resistiveStrength)
    } else {
      adaptiveTrigger.setModeVibrationWithStartPosition(
        0,
        amplitude: resistiveStrength,
        frequency: 0.03)
    }
  } else if adaptiveTrigger.mode != .off {
    adaptiveTrigger.setModeOff()
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10081/5/113EE58D-480B-4192-A7E1-8088B2A0BC72/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10081/5/113EE58D-480B-4192-A7E1-8088B2A0BC72/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10081) — developer.apple.com. Indexed for agent consumption._
