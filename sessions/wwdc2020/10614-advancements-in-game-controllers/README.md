---
id: "wwdc2020-10614"
event: "wwdc2020"
year: 2020
title: "Advancements in Game Controllers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10614"
topics: ["System Services", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Advancements in Game Controllers

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10614](https://developer.apple.com/videos/play/wwdc2020/10614)

Let’s rumble! Discover how you can bring third-party game controllers and custom haptics into your games on iPhone, iPad, Mac, and Apple TV. We’ll show you how to add support for the latest controllers — including Xbox’s Elite Wireless Controller Series 2 and Adaptive Controller — and map your game’s controls accordingly. Learn how you can use the Game Controller framework in tandem with Core Haptics to enable rumble feedback. And find out how you can take your gaming experience to the next level with custom button mapping, nonstandard inputs, and control over specialty features like motion sensors, lights, and battery level. To get the most out of this session, you should be familiar with the Game Controller framework. Check the documentation link for a primer. And if you build games for iPad, be sure to check out "Bring keyboard and mouse gaming to iPad” for a guide on integrating keyboard, mouse, and trackpad inputs into your experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,123 words)

## Documentation & Resources

- [Playing Haptics on Game Controllers](https://developer.apple.com/documentation/CoreHaptics/playing-haptics-on-game-controllers) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreHaptics/playing-haptics-on-game-controllers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreHaptics/playing-haptics-on-game-controllers.json
- [Game Controller](https://developer.apple.com/documentation/GameController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameController.json

## Code Snippets

### Extensible input API — [2:53]

```swift
// Extensible input API example

var attackComboBtn: GCControllerButtonInput?
var mapBtn: GCControllerButtonInput?
var mappedButtons = Set<GCControllerButtonInput>()
var unmappedButtons = Set<GCControllerButtonInput>()

func setupConnectedController(_ controller: GCController) {
    let input = controller.physicalInputProfile

    // Set up standard button mapping
    setupBasicControls(input)

    // Map a shortcut to the player's special combo attack
    attackComboBtn = input.buttons["Paddle 1"]
    if (attackComboBtn != nil) { mappedButtons.insert(attackComboBtn!) }

    // Map a shortcut to the in-game map
    mapBtn = input.buttons[GCInputDualShockTouchpadButton]
    if (mapBtn != nil) { mappedButtons.insert(mapBtn!) }

    // Find buttons that havent' been mapped to any actions yet
    unmappedButtons = input.allButtons.filter { !mappedButtons.contains($0) }
}
```

### Starting the Haptic Engine — [8:45]

```swift
private func createAndStartHapticEngine() {
    // Create and configure a haptic engine for the active controller

    guard let controller = activeController else { return }

    hapticEngine = controller.haptics?.createEngine(withLocality: .handles)

    guard let engine = hapticEngine else {
        print("Active controller does not support handle haptics")
        return
    }
```

### Play haptics — [9:05]

```swift
// Play haptics whenever the player is damaged

private func playerWasDamaged(damage: Float) {
    do {
        // Calculate the magnitude of damage as percentage of range [0, maxPossibleDamage]
        let damageMagnitude: Float = ...

        // Create a haptic pattern player for the player being hit by an enemy
        let hapticPlayer = try patternPlayerForPlayerDamage(damageMagnitude)

        // Start player, "fire and forget".
        try hapticPlayer?.start(atTime: CHHapticTimeImmediate)
    } catch let error {
        print("Haptic Playback Error: \(error)")
    }
}
```

### Creating a haptic pattern — [9:49]

```swift
// Create a haptic pattern that scales to the damage dealt to the player

private func patternPlayerForPlayerDamage(_ damage: Float) throws -> CHHapticPatternPlayer? {
    let continuousEvent = CHHapticEvent(eventType: .hapticContinuous, parameters: [
        CHHapticEventParameter(parameterID: .hapticSharpness, value: 0.5),
        CHHapticEventParameter(parameterID: .hapticIntensity, value: 0.3),
    ], relativeTime: 0, duration: 0.6)

    let firstTransientEvent = CHHapticEvent(eventType: .hapticTransient, parameters: [
        CHHapticEventParameter(parameterID: .hapticSharpness, value: 0.5),
        CHHapticEventParameter(parameterID: .hapticIntensity, value: 0.9 * damage),
    ], relativeTime: 0.2)

    let secondTransientEvent = CHHapticEvent(eventType: .hapticTransient, parameters: [
        CHHapticEventParameter(parameterID: .hapticSharpness, value: 0.5),
        CHHapticEventParameter(parameterID: .hapticIntensity, value: 0.9 * damage),
    ], relativeTime: 0.4)

    let pattern = try CHHapticPattern(events: [continuousEvent, firstTransientEvent,
                                               secondTransientEvent], parameters: [])

    return try engine.makePlayer(with: pattern)
}
```

### Updating haptics every frame — [12:28]

```swift
// Update the state of the connected controller's haptics every frame

private func update() {
    updateHaptics()
}

private func updateHaptics() {
    // Update the controller's haptics by sending a dynamic intensity parameter each frame
    do {
        // Create dynamic parameter for the intensity.
        let intensityParam = CHHapticDynamicParameter(parameterID: .hapticIntensityControl,
                                                        value: hapticEngineMotorIntensity,
                                                        relativeTime: 0)

        // Send parameter to the pattern player.
        try hapticsUpdateLoopPatternPlayer?.sendParameters([intensityParam],
                                 atTime: CHHapticTimeImmediate)
    } catch let error {
        print("Dynamic Parameter Error: \(error)")
    }
}
```

### Current controller notifications — [14:11]

```swift
NSNotification.Name.GCControllerDidBecomeCurrent
NSNotification.Name.GCControllerDidStopBeingCurrentNotification
```

### Manual activation — [15:25]

```swift
if motion.sensorsRequireManualActivation {
    motion.sensorsActive = true
}
```

### Using total acceleration — [15:44]

```swift
if motion.hasGravityAndUserAcceleration {
    handleMotion(gravity: motion.gravity, userAccel: motion.userAcceleration)
} else {
    handleMotion(totalAccel: motion.acceleration)
}
```

### Setting up the lightbar — [16:27]

```swift
guard let controller = GCController.current else { return }
controller.light?.color = GCColor.init(red: 1.0, green: 0, blue: 0)
```

### Input glyphs with SF Symbols — [22:36]

```swift
let xboxButtonY = xboxController.physicalInputProfile[GCInputButtonY]!
guard let xboxSfSymbolsName = xboxButtonY.sfSymbolsName else { return }
let xboxButtonYGlyph = UIImage(systemName: xboxSfSymbolsName)

let ds4ButtonY = ds4Controller.physicalInputProfile[GCInputButtonY]!
guard let ds4SfSymbolsName = ds4ButtonY.sfSymbolsName else { return }
let ds4ButtonYGlyph = UIImage(systemName: ds4SfSymbolsName)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10614/4/E368D3E8-DCFB-445D-9ADC-E97C82AEE886/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10614) — developer.apple.com. Indexed for agent consumption._
