---
id: "tech-talks-111464"
event: "tech-talks"
year: 2026
title: "Leverage multiple displays and scenes on iPhone Duo"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111464"
topics: ["Photos & Camera", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS"]
hasTranscript: true
---

# Leverage multiple displays and scenes on iPhone Duo

**Event:** Tech Talks · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS · **Published:** 2026-09-09 · **Session:** [tech-talks-111464](https://developer.apple.com/videos/play/tech-talks/111464)

Discover how to build rich multiwindow and multidisplay experiences for iPhone Duo. Explore how to handle dynamic window sizes and request new scenes in side-by-side multitasking. Learn how to observe hinge angle changes in SwiftUI and UIKit to create interactive effects. And find out how to use scene accessories to present supplementary content across both displays simultaneously.

**Keywords:** `duo preview`, `kid cue`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,116 words)

## Code Snippets

### Hold pitch bend as state — [1:33]

```swift
struct InstrumentView: View {
    /// Normalized bend, 0 is no bend, 1 is deepest bend
    @State private var pitchBend: Double = 0

    var body: some View {
        GuitarView(pitchBend: pitchBend)
    }
}
```

### Add the onHingeChange modifier — [1:44]

```swift
struct InstrumentView: View {
    /// Normalized bend, 0 is no bend, 1 is deepest bend
    @State private var pitchBend: Double = 0

    var body: some View {
        GuitarView(pitchBend: pitchBend)
            .onHingeChange { _, context in

            }
    }
}
```

### Check for a hinge and the partially open state — [1:57]

```swift
var body: some View {
    GuitarView(pitchBend: pitchBend)
        .onHingeChange { _, context in
            // A null hinge means the device doesn't have one
            if let hinge = context.hinge, hinge.status == .partiallyOpen {

            }
        }
}
```

### Reset the pitch bend — [2:10]

```swift
var body: some View {
    GuitarView(pitchBend: pitchBend)
        .onHingeChange { _, context in
            if let hinge = context.hinge, hinge.status == .partiallyOpen {

            }
            else {
                pitchBend = 0
            }
        }
}
```

### Calculate the pitch bend from the hinge angle — [2:17]

```swift
struct InstrumentView: View {
    /// Normalized bend, 0 is no bend, 1 is deepest bend
    @State private var pitchBend: Double = 0

    var body: some View {
        GuitarView(pitchBend: pitchBend)
            .onHingeChange { _, context in
                if let hinge = context.hinge, hinge.status == .partiallyOpen {
                    pitchBend = calculatePitchBend(angle: hinge.angle)
                }
                else {
                    pitchBend = 0
                }
            }
    }

    private func calculatePitchBend(angle: Angle) -> Double { ... }
}
```

### Register a camera capture accessory — [5:43]

```swift
struct CameraRootView: View {
    @State private var model = TeleprompterModel()

    var body: some View {
        CameraView(model: model)
            .sceneAccessory {
                CameraCaptureAccessory {
                    TeleprompterView(model: model)
                }
            }
    }
}
```

### Add a toolbar toggle — [6:14]

```swift
struct CameraRootView: View {
    @State private var model = TeleprompterModel()

    var body: some View {
        CameraView(model: model)
            .sceneAccessory {
                CameraCaptureAccessory(isEnabled: $model.isEnabled) {
                    TeleprompterView(model: model)
                }
            }
            .toolbar {
                TeleprompterToggle(isEnabled: $model.isEnabled)
            }
    }
}
```

### Observe accessory availability — [6:25]

```swift
struct CameraRootView: View {
    @State private var model = TeleprompterModel()

    var body: some View {
        CameraView(model: model)
            .sceneAccessory {
                CameraCaptureAccessory(isEnabled: $model.isEnabled) {
                    TeleprompterView(model: model)
                }
                .onAvailabilityChange { newValue in
                    model.isAvailable = newValue
                }
            }
            .toolbar {
                TeleprompterToggle(isEnabled: $model.isEnabled)
                    .disabled(!model.isAvailable)
            }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111464/1/b6d9b8a0-71ba-4f7a-acfc-4fb339dae7ff/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111464/1/b6d9b8a0-71ba-4f7a-acfc-4fb339dae7ff/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111464) — developer.apple.com. Indexed for agent consumption._
