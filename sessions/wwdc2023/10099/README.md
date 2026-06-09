---
id: "wwdc2023-10099"
event: "wwdc2023"
year: 2023
title: "Meet RealityKit Trace"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10099"
topics: ["Spatial Computing", "Developer Tools"]
platforms: ["visionOS"]
hasTranscript: true
---

# Meet RealityKit Trace

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10099](https://developer.apple.com/videos/play/wwdc2023/10099)

Discover how you can use RealityKit Trace to improve the performance of your spatial computing apps. Explore performance profiling guidelines for this platform and learn how the RealityKit Trace template can help you optimize rendering for your apps. We’ll also provide guidance on profiling various types of content in your app to help pinpoint performance issues.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,330 words)

## Documentation & Resources

- [Analyzing the performance of your visionOS app](https://developer.apple.com/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app.json

## Code Snippets

### SwiftUI View with High Offscreens — [10:50]

```swift
private struct Item: View {
    var module: Module

    // The corner radius of the item's hightlight when selected or hovering.
    let cornerRadius = 20.0

    var body: some View {
        NavigationLink(value: module) {
            VStack(alignment: .leading, spacing: 3) {
                Text(module.eyebrow)
                    .font(.titleHeading)
                    .foregroundStyle(.secondary)
                VStack(alignment: .leading, spacing: 7) {
                    Text(module.heading)
                        .font(.largeTitle)
                    Text(module.abstract)
                }
            }
            .padding(.horizontal, 5)
            .padding(.vertical, 20)
        }
        .buttonStyle(.bordered)
        .shadow(radius: 10)
        .buttonBorderShape(.roundedRectangle(radius: cornerRadius))
        .frame(minWidth: 150, maxWidth: 280)
    }
}
```

### EarthEntity Factory — [16:33]

```swift
class EarthEntity: Entity {
    static func makeGlobe() -> EarthEntity {
        EarthEntity(earthModel: Entity.makeModel(
            name: "Earth",
            filename: "Globe",
            radius: 0.35,
            color: .blue)
        )
    }

    static func makeCloudyEarth() -> EarthEntity {
        let earthModel = Entity()
        earthModel.name = "Earth"

        Task {
            if let scene = await loadFromRealityComposerPro(
                named: WorldAssets.rootNodeName,
                fromSceneNamed: WorldAssets.sceneName
            ) {
                earthModel.addChild(scene)
            } else {
                fatalError("Unable to load earth model")
            }
        }

        return EarthEntity(earthModel: earthModel)
    }
}
```

### Orbit SwiftUI View Body — [16:53]

```swift
struct Orbit: View {
    @EnvironmentObject private var model: ViewModel

    var body: some View {
        Earth(
            world: EarthEntity.makeGlobe(),
            earthConfiguration: model.orbitEarth,
            satelliteConfiguration: [model.orbitSatellite],
            moonConfiguration: model.orbitMoon,

            showSun: true,
            sunAngle: model.orbitSunAngle,

            animateUpdates: true
        )
        .place(
            initialPosition: Point3D([475, -1200.0, -1200.0]),
            useCustomGesture: model.useCustomGesture,
            handOffset: model.customGestureHandOffset,
            isCustomGestureAnimated: model.isCustomGestureAnimated,
            debugCustomGesture: model.debugCustomGesture,
            scale: $model.orbitEarth.scale)
    }
}
```

### SwiftUI ViewModel — [17:26]

```swift
class ViewModel: ObservableObject {
    // MARK: - Navigation
    @Published var navigationPath: [Module] = []
    @Published var titleText: String = ""
    @Published var isTitleFinished: Bool = false
    var finalTitle: String = "Hello World"

    // MARK: - Globe
    @Published var globeEarthEntity: EarthEntity = .makeGlobe()

    @Published var isShowingGlobe: Bool = false
    @Published var globeEarth: EarthEntity.Configuration = .globeEarthDefault
    @Published var globeEarthOffset: SIMD3<Double> = [0, 0, 0]
    @Published var globePanelOffset: SIMD3<Double> = [0, -50, 30]

    @Published var showSatelliteButton: Bool = false
    @Published var isShowingSatellite: Bool = false

    // MARK: - Orbit
    @Published var orbitEarthEntity: EarthEntity = .makeGlobe()

    @Published var useCustomGesture: Bool = true
    @Published var customGestureHandOffset: SIMD3<Float> = [0, 0.21, -0.07]
    @Published var isCustomGestureAnimated: Bool = false
    @Published var debugCustomGesture: Bool = false

    @Published var orbitSatelliteScale: Float = 0.9
    @Published var orbitMoonScale: Float = 0.9
    @Published var orbitTelescopeScale: Float = 0.8
    @Published var orbitSatelliteZOffset: Double = 100
    @Published var orbitMoonZOffset: Double = 100
    @Published var orbitTelescopeZOffset: Double = 100

    @Published var isShowingOrbit: Bool = false
    @Published var orbitImmersionStyle: ImmersionStyle = .mixed
    @Published var orbitEarth: EarthEntity.Configuration = .orbitEarthDefault
    @Published var orbitSatellite: SatelliteEntity.Configuration = .orbitSatelliteDefault
    @Published var orbitMoon: SatelliteEntity.Configuration = .orbitMoonDefault

    @Published var orbitSunAngle: Angle = .degrees(150)
    var orbitSunAngleBinding: Binding<Float> {
        Binding<Float>(
            get: { Float(self.orbitSunAngle.degrees) },
            set: { self.orbitSunAngle = .degrees(Double($0)) }
        )
    }

    // MARK: - Solar System
    @Published var solarEarthEntity: EarthEntity = .makeCloudyEarth()

    @Published var isShowingSolar: Bool = false
    @Published var solarImmersionStyle: ImmersionStyle = .full
    @Published var solarEarth: EarthEntity.Configuration = .solarEarthDefault
    @Published var solarSatellite: SatelliteEntity.Configuration = .solarTelescopeDefault
    @Published var solarMoon: SatelliteEntity.Configuration = .solarMoonDefault

    @Published var solarSunDistance: Double = 700
    @Published var solarSunAngle: Angle = .degrees(280)
    @Published var solarSunSpotIntensity: Float = 10.5
    @Published var solarSunEmissionIntensity: Float = 10.5
    var solarSunPosition: SIMD3<Float> {
        [Float(solarSunDistance * sin(solarSunAngle.radians)),
         0,
         Float(solarSunDistance * cos(solarSunAngle.radians))]
    }
}
```

### SwiftUI Orbit View Body — [17:33]

```swift
struct Orbit: View {
    @EnvironmentObject private var model: ViewModel

    var body: some View {
        Earth(
            world: model.globeEarthEntity,
            earthConfiguration: model.orbitEarth,
            satelliteConfiguration: [model.orbitSatellite],
            moonConfiguration: model.orbitMoon,

            showSun: true,
            sunAngle: model.orbitSunAngle,

            animateUpdates: true
        )
        .place(
            initialPosition: Point3D([475, -1200.0, -1200.0]),
            useCustomGesture: model.useCustomGesture,
            handOffset: model.customGestureHandOffset,
            isCustomGestureAnimated: model.isCustomGestureAnimated,
            debugCustomGesture: model.debugCustomGesture,
            scale: $model.orbitEarth.scale)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10099/5/3AFC66A2-7703-40D9-BB5A-874A5091FE1A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10099/5/3AFC66A2-7703-40D9-BB5A-874A5091FE1A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10099) — developer.apple.com. Indexed for agent consumption._