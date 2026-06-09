---
id: "wwdc2026-358"
event: "wwdc2026"
year: 2026
title: "Make your game great with touch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/358"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Make your game great with touch

**Event:** WWDC26 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-358](https://developer.apple.com/videos/play/wwdc2026/358)

Dive deeper into the techniques you can use to create compelling touch experiences for your games. We’ll share expert insights from indie to AAA game development, explore best practices for intuitive touch controls, and show you how to take advantage of Apple technologies like Touch Controller framework and Metal for great performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,094 words)

## Code Snippets

### GCController polling vs. change handlers — [2:04]

```swift
// Polling
if (button.isPressed) {
    // ...
}

// Change handlers
pressedInput.pressedDidChangeHandler = { (element: any GCPhysicalInputElement,
                                           input: any GCPressedStateInput,
                                           pressed: Bool)
    // ...
}
```

### Set up a TCTouchController — [3:14]

```swift
// Set up a TCTouchController
private(set) var touchController: TCTouchController?

let descriptor = TCTouchControllerDescriptor(mtkView: mtkView)
if TCTouchController.isSupported {
    touchController = TCTouchController(descriptor: descriptor)
}
touchController?.connect()
touchController?.render(using: renderEncoder)

override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    for touch in touches {
        touchControls.handleTouchBegan(at: touch.location(in: view), index: touch.hash)
    }
}

buttonA?.valueChangedHandler = { (_ button: GCControllerButtonInput, _ value: Float,
                                  _ pressed: Bool) in
    // ...
}
```

### Create a standard circular button B — [8:33]

```swift
// Create a standard circular button B
let buttonBDesc = TCButtonDescriptor()
buttonBDesc.label = TCControlLabel.buttonB
buttonBDesc.anchor = .bottomRight
buttonBDesc.offset = adjustedOffset(CGPoint(x: -35, y: -106), for: buttonBDesc.anchor)
buttonBDesc.contents = .buttonContents(forSystemImageNamed: "b.circle",
                                       size: buttonBDesc.size, shape: .circle,
                                       controller: touchController)
// Set other properties ...
touchController.addButton(descriptor: buttonBDesc)

func adjustedOffset(_ offset: CGPoint, for anchor: TCControlLayoutAnchor) -> CGPoint {
    // Adjust offset for other anchors ...
    case .bottomRight:
        x -= safeArea.right
        y -= safeArea.bottom
}
```

### Change icon image — [10:48]

```swift
// Change icon image
buttonBDesc.contents = .buttonContents(forSystemImageNamed: "figure.fencing",
                                       size: buttonBDesc.size,
                                       shape: .circle,
                                       controller: touchController)
```

### Update contents for button B based on context — [11:51]

```swift
// Update contents for button B based on context
func setButtonBContents(symbolName: String) {
    for button in touchController.buttons {
        if button.label == TCControlLabel.buttonB {
            button.contents = .buttonContents(forSystemImageNamed: symbolName, size: buttonSize,
                                              shape: .circle, controller: touchController)
        }
    }
}

func cyclePower() {
    // Get the current power type ...
    switch currentPower {
        case .strike:       touchControls?.setButtonBContents(symbolName: "figure.fencing")
        case .fireball:     touchControls?.setButtonBContents(symbolName: "flame.fill")
        case .waterBlaster: touchControls?.setButtonBContents(symbolName: "drop.fill")
    }
}
```

### Hide left thumbstick when not touched — [13:01]

```swift
// Hide left thumbstick when it is not touched
let leftStickDesc = TCThumbstickDescriptor()
leftStickDesc.hidesWhenNotPressed = true
// Set other properties ...
touchController.addThumbstick(descriptor: leftStickDesc)
```

### Show/hide the pick-up button — [13:19]

```swift
// Show pickup button when there's an item nearby
func showPickupButton(at projectedPosition: CGPoint) {
    // Calculate the position(ptX, ptY) for pickup button ...
    descriptor.offset = CGPoint(x: ptX, y: ptY)
    // Set other properties ...
    touchController.addButton(descriptor: descriptor)
}

func hidePickupButton() {
    for button in touchController.buttons {
        if button.label == TCControlLabel.buttonY {
            touchController.removeControl(button)
        }
    }
}
```

### Show power options as touch controls — [13:56]

```swift
// Show power options as touch controls
buttonX?.pressedChangedHandler = { (_ button: GCControllerButtonInput, _ value: Float,
                                    _ pressed: Bool) -> Void in
    if pressed {
        self.openPowerWheel()
    }
}

func openPowerWheel() {
    touchControls?.showPowerWheelButtons(fireballCount: fireballCount, has: hasWaterBlaster)
    wirePowerWheelHandlers()
    DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) { [weak self] in
        guard let self = self, self.powerWheelActive else { return }
        self.closePowerWheel()
    }
}
```

### Use the left half of the screen for character movement — [15:34]

```swift
// Use the left half of the screen for character movement
let leftStickDesc = TCThumbstickDescriptor()
leftStickDesc.colliderShape = .leftSide // Don't set as .circle
// Set other properties ...
touchController.addThumbstick(descriptor: leftStickDesc)
```

### Calculate thumbstick tilt magnitude to trigger sprint — [16:39]

```swift
// Calculate left thumbstick's tilt magnitude to trigger sprint
func pollInput() {
    if let gamePad = gameController.extendedGamepad {
        let gamePadLeft = gamePad.leftThumbstick
        var moveInput = simd_make_float2(gamePadLeft.xAxis.value, -gamePadLeft.yAxis.value)
        let magnitude = simd_length(moveInput)
        if magnitude > 0.8 {
            self.runModifier = 1.3
        }
        self.characterDirection = moveInput
    }
}
```

### Replace right thumbstick with a touchpad — [17:36]

```swift
// Replace right thumbstick with touchpad
let touchpadDesc = TCTouchpadDescriptor()
touchpadDesc.label = TCControlLabel.rightThumbstick
touchpadDesc.colliderShape = .rightSide
touchpadDesc.reportsRelativeValues = true
// Set other properties ...
touchController.addTouchpad(descriptor: touchpadDesc)
```

### Collapse two QTE buttons into one — [19:30]

```swift
// Collapse 2 QTE buttons into 1 single button
func setupControls() {
    let desc = TCButtonDescriptor()
    desc.label = TCControlLabel(name: "escape_button", role: .button)
    // Set up other properties ...
    touchController.addButton(descriptor: desc)
}

func showEscapeButton() {
    // Find escape button in touchController ...
    escapeButton.isEnabled = true
}

func hideEscapeButton() {
    // Find escape button in touchController ...
    escapeButton.isEnabled = false
}
```

### Use button B to aim, move, and release power — [20:28]

```swift
// Use button B to aim, move, and release power
buttonB?.valueChangedHandler = { (_ button: GCControllerButtonInput, _ value: Float,
                                  _ pressed: Bool) -> Void in
    self.releasePower(pressed: pressed)
}

override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
    for touch in touches {
        let point = touch.location(in: metalView)
        // Handle touch input ...
        if let gc = gameController, gc.isAiming {
            let prev = touch.previousLocation(in: metalView)
            gc.aimTouchDelta += simd_float2(Float(point.x - prev.x), Float(point.y - prev.y))
        }
    }
}
```

### Add a halo effect with custom TCControlContents — [21:52]

```swift
// Add a halo effect around left thumbstick with customized TCControlContents
let haloLayer = TCControlImage(texture: haloTexture, size: haloSize, highlight: nil,
                               offset: .zero, tintColor: tint)
let normalBgImages = TCControlContents.thumbstickStickBackgroundContents(size: bgSize,
                                                                         controller: controller).images
haloThumbstickBg = TCControlContents(images: [haloLayer] + normalBgImages)
thumbstick.backgroundContents = active ? haloThumbstickBg : normalThumbstickBg
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/358/4/fdd21d54-a233-49d4-8d00-4dc51284515d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/358/4/fdd21d54-a233-49d4-8d00-4dc51284515d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/358) — developer.apple.com. Indexed for agent consumption._
