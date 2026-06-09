---
id: "wwdc2023-10109"
event: "wwdc2023"
year: 2023
title: "Meet SwiftUI for spatial computing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10109"
topics: ["Essentials", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Meet SwiftUI for spatial computing

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10109](https://developer.apple.com/videos/play/wwdc2023/10109)

Take a tour of the solar system with us and explore SwiftUI for visionOS! Discover how you can build an entirely new universe of apps with windows, volumes, and spaces. We’ll show you how to get started with SwiftUI on this platform as we build an astronomy app, add 3D content, and create a fully immersive experience to transport people to the stars.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,447 words)

## Documentation & Resources

- [Hello World](https://developer.apple.com/documentation/visionOS/World) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/World
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/World.json

## Code Snippets

### Button — [2:02]

```swift
Button("Of course") {
  // perform action
}
```

### Toggle Favorite — [2:41]

```swift
Toggle(isOn: $favorite) {
    Label("Favorite", systemImage: "star")
}
```

### TabView — [2:48]

```swift
TabView {
    DogsTab()
        .tabItem {
            Label("Dogs", systemImage: "pawprint")
        }

    CatsTab()
        .tabItem {
            Label("Cats", image: "cat")
        }

    BirdsTab()
        .tabItem {
            Label("Birds", systemImage: "bird")
        }
}
```

### World App — [3:37]

```swift
@main
struct WorldApp: App {
    var body: some Scene {
        WindowGroup("Hello, world") {
            ContentView()
        }
    }
}
```

### World TabView — [7:03]

```swift
@main
struct WorldApp: App {
    var body: some Scene {
        WindowGroup("Hello, world") {
            TabView {
                Modules()
                    .tag(Tabs.menu)
                    .tabItem {
                        Label("Experience", systemImage: "globe.americas")
                    }
                FunFactsTab()
              	    .tag(Tabs.library)
                    .tabItem {
                        Label("Library", systemImage: "book")
                    }                    
            }
        }
    }
}
```

### Stats Grid Section — [8:42]

```swift
VStack(alignment: .leading, spacing: 12) {
    Text("Stats")
        .font(.title)

    StatsGrid(stats: stats)
        .padding()
        .background(.regularMaterial, in: .rect(cornerRadius: 12))
}
```

### Fun Fact Button — [9:23]

```swift
Button(action: {
    // perform button action
}) {
    VStack(alignment: .leading, spacing: 12) {
        Text(fact.title)
            .font(.title2)
            .lineLimit(2)
        Text(fact.details)
            .font(.body)
            .lineLimit(4)
        Text("Learn more")
            .font(.caption)
            .foregroundStyle(.secondary)
    }
    .frame(width: 180, alignment: .leading)
}
.buttonStyle(.funFact)
```

### FunFactButtonStyle — [13:15]

```swift
struct FunFactButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(.regularMaterial, in: .rect(cornerRadius: 12))
            .hoverEffect()
            .scaleEffect(configuration.isPressed ? 0.95 : 1)
    }
}
```

### Globe Volume — [14:17]

```swift
@main
struct WorldApp: App {
    var body: some Scene {
        WindowGroup {
            Globe()
        }
        .windowStyle(.volumetric)
        .defaultSize(width: 600, height: 600, depth: 600)
    }
}
```

### Model3D — [14:36]

```swift
import SwiftUI
import RealityKit

struct Globe: View {
    var body: some View {
        Model3D(named: "Earth")
    }
}
```

### Globe with rotation and controls — [15:40]

```swift
struct Globe: View {
    @State var rotation = Angle.zero
    var body: some View {
        ZStack(alignment: .bottom) {
            Model3D(named: "Earth")
                .rotation3DEffect(rotation, axis: .y)
                .onTapGesture {
                    withAnimation(.bouncy) {
                        rotation.degrees += randomRotation()
                    }
                }
                .padding3D(.front, 200)

            GlobeControls()
                .glassBackgroundEffect(in: .capsule)
        }
    }

    func randomRotation() -> Double {
        Double.random(in: 360...720)
    }
}
```

### RealityView — [17:30]

```swift
RealityView { content in
    if let earth = try? await
        ModelEntity(named: "Earth")
    {
       earth.addImageBasedLighting()
       content.add(earth)
    }
}
```

### RealityView Gesture — [18:57]

```swift
struct Earth: View {
		@State private var pinLocation: GlobeLocation?

    var body: some View {
        RealityView { content in
            if let earth = try? await
                ModelEntity(named: "Earth")
            {
               earth.addImageBasedLighting()
               content.add(earth)
            }
        }
				.gesture(
            SpatialTapGesture()
                .targetedToAnyEntity()
                .onEnded { value in
                    withAnimation(.bouncy) {
                        rotation.degrees += randomRotation()
                        animatingRotation = true
                    } completion: {
                        animatingRotation = false
                    }
                    pinLocation = lookUpLocation(at: value)
                }
        )
    }
}
```

### RealityView Attachments — [19:34]

```swift
struct Earth: View {
		@State private var pinLocation: GlobeLocation?

    var body: some View {
        RealityView { content in
            if let earth = try? await
                ModelEntity(named: "Earth")
            {
               earth.addImageBasedLighting()
               content.add(earth)
            }
        } update: { content, attachments in
            if let pin = attachments.entity(for: "pin") {
                content.add(pin)
                placePin(pin)
            }
        } attachments: {
            if let pinLocation {
                GlobePin(pinLocation: pinLocation)
                    .tag("pin")
            }
        }
				.gesture(
            SpatialTapGesture()
                .targetedToAnyEntity()
                .onEnded { value in
                    withAnimation(.bouncy) {
                        rotation.degrees += randomRotation()
                        animatingRotation = true
                    } completion: {
                        animatingRotation = false
                    }
                    pinLocation = lookUpLocation(at: value)
                }
        )
    }
}
```

### ImmersiveSpace — [21:11]

```swift
@main
struct WorldApp: App {
    var body: some Scene {
				// (other WindowGroup scenes)

        ImmersiveSpace(id: "solar-system") {
            SolarSystem()
        }
    }
}
```

### Open ImmersiveSpace Action — [21:25]

```swift
@Environment(\.openImmersiveSpace)
private var openImmersiveSpace

Button("View Outer Space") {
    openImmersiveSpace(id: "solar-system")
}
```

### ImmersionStyle — [22:50]

```swift
@main
struct WorldApp: App {
    @State private var selectedStyle: ImmersionStyle = .full
    var body: some Scene {
				// (other WindowGroup scenes)

        ImmersiveSpace(id: "solar-system") {
            SolarSystem()
        }
        .immersionStyle(selection: $selectedStyle, in: .full)
    }
}
```

### Starfield — [23:17]

```swift
struct Starfield: View {
    var body: some View {
        RealityView { content in
            let starfield = await loadStarfield()
            content.add(starfield)
        }
    }
}
```

### SolarSystem — [23:28]

```swift
struct SolarSystem: View {
    var body: some View {
        Earth()
        Sun()
      	Starfield()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10109/4/F4A066BD-28D9-4CF8-AAF3-D35EA776504F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10109/4/F4A066BD-28D9-4CF8-AAF3-D35EA776504F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10109) — developer.apple.com. Indexed for agent consumption._
