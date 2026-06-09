---
id: "wwdc2024-111801"
event: "wwdc2024"
year: 2024
title: "Enhance your spatial computing app with RealityKit audio"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/111801"
topics: ["Developer Tools", "Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Enhance your spatial computing app with RealityKit audio

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-111801](https://developer.apple.com/videos/play/wwdc2024/111801)

Elevate your spatial computing experience using RealityKit audio. Discover how spatial audio can make your 3D immersive experiences come to life. From ambient audio, reverb, to real-time procedural audio that can add character to your 3D content, learn how RealityKit audio APIs can help make your app more engaging.

**Keywords:** `attenuation`, `audio`, `audio mix groups`, `collision`, `collision sounds`, `entity`, `gain`, `immersive music`, `music`, `play audio`, `reality composer pro`, `realitykit`, `realitykit audio`, `reverb`, `reverbcomponent`, `rolloff`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,852 words)

## Documentation & Resources

- [Creating a Spaceship game](https://developer.apple.com/documentation/RealityKit/creating-a-spaceship-game) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-a-spaceship-game
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-a-spaceship-game.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Play vapor trail audio — [3:11]

```swift
// Vapor trail audio

import RealityKit

func playVaporTrailAudio(from engine: Entity) async throws {
    let resource = try await AudioFileResource(named: "VaporTrail")
    engine.playAudio(resource)
}
```

### Make vapor trail audio playback more dynamic — [4:02]

```swift
// Vapor trail audio

import RealityKit

func playVaporTrailAudio(from engine: Entity) async throws {
    let resource = try await AudioFileResource(
        named: "VaporTrail",
        configuration: AudioFileResource.Configuration(
           shouldLoop: true,
           shouldRandomizeStartTime: true
        )
    )
    let controller: AudioPlaybackController = engine.playAudio(resource)
    controller.gain = -.infinity
    controller.fade(to: .zero, duration: 1)

    let audioSource = Entity()
    audioSource.orientation = .init(angle: .pi, axis: [0, 1, 0])
    audioSource.components.set(
        SpatialAudioComponent(directivity: .beam(focus: 0.25))
    )
    engine.addChild(audioSource)
    let controller = audioSource.playAudio(resource)

}
```

### Exhaust audio — [7:10]

```swift
// Exhaust audio

import RealityKit

func updateAudio(for exhaust: Entity, throttle: Float) {
    let gain = decibels(amplitude: throttle)
    exhaust.components[SpatialAudioComponent.self]?.gain = Audio.Decibel(gain)
}

func decibels(amplitude: Float) -> Float { 20 * log10(amplitude) }
```

### Turbine audio — [8:17]

```swift
// Turbine audio

import RealityKit

var turbineController: AudioGeneratorController?

func playTurbineAudio(from engine: Entity) {
    let audioUnit = try await AudioUnitTurbine.instantiate()
    let configuration = AudioGeneratorConfiguration(layoutTag: kAudioChannelLayoutTag_Mono)
    let format = AVAudioFormat(
        standardFormatWithSampleRate: Double(AudioGeneratorConfiguration.sampleRate),
        channelLayout: .init(layoutTag: configuration.layoutTag)!
    )
    try audioUnit.outputBusses[0].setFormat(format)
		try audioUnit.allocateRenderResources()
    let renderBlock = audioUnit.internalRenderBlock
    turbineController = try engine.playAudio(configuration: configuration) { 
        isSilence, timestamp, frameCount, outputData in
        var renderFlags = AudioUnitRenderActionFlags()
        return renderBlock(&renderFlags, timestamp, frameCount, 0, outputData, nil, nil)
    }
}
```

### Setting distance attenuation and gain — [11:28]

```swift
import RealityKit

func configureDistanceAttenuation(for spaceshipHifi: Entity) {
    spaceshipHifi.components.set(
        SpatialAudioComponent(
            gain: -18,
            distanceAttenuation: .rolloff(factor: 4)
        )
    )
}
```

### Loudness variation — [12:36]

```swift
// Loudness variation

import RealityKit

func handleCollisionBegan(_ collision: CollisionEvents.Began) {
    let resource: AudioFileGroupResource // …
    let controller = collision.entityA.playAudio(resource)
    controller.gain = relativeLoudness(for: collision)
}
```

### Defining audio materials — [14:44]

```swift
// Audio materials

import RealityKit

enum AudioMaterial {
    case none
    case plastic
    case rock
    case metal
    case drywall
    case wood
    case glass
    case concrete
    case fabric
}

struct AudioMaterialComponent: Component {
    var material: AudioMaterial
}
```

### Setting audio materials — [14:53]

```swift
// Setting Audio Materials

asteroid.components.set(
    AudioMaterialComponent(material: .rock)
)

spaceship.components.set(
    AudioMaterialComponent(material: .plastic)
)
```

### Handling collision audio — [15:04]

```swift
// Audio materials

import RealityKit

func handleCollisionBegan(_ collision: CollisionEvents.Began) {
    guard 
        let audioMaterials = audioMaterials(for: collision),
        let resource: AudioFileGroupResource = collisionAudio[audioMaterials] 
    else {
        return 
    }
    let controller = collision.entityA.playAudio(resource)
    controller.gain = relativeLoudness(for: collision)
}
```

### Reverb presets — [17:18]

```swift
// Reverb presets

import Studio

func prepareStudioEnvironment() async throws {
    let studio = try await Entity(named: "Studio", in: studioBundle)
    studio.components.set(
       ReverbComponent(reverb: .preset(.veryLargeRoom))
    )
    rootEntity.addChild(studio)
}
```

### Immersive music — [20:05]

```swift
// Immersive music

import RealityKit

func playJoyRideMusic(from entity: Entity) async throws {
    let resource = try await AudioFileResource(
        named: “JoyRideMusic”,
        configuration: .init(
            loadingStrategy: .stream,
            shouldLoop: true       
        )
    )
    entity.components.set(AmbientAudioComponent())
    entity.playAudio(resource)
}
```

### Using AudioMixGroup with a RealityKit entity — [21:57]

```swift
// Audio mix groups

import RealityKit

let resource = try await AudioFileResource(
    named: “JoyRideMusic”,
    configuration: .init(
        loadingStrategy: .stream,
        shouldLoop: true,
        mixGroupName: “Music”
    )
)

var audioMixerEntity = Entity()

func updateMixGroup(named mixGroupName: String, to level: Audio.Decibel) {
    var mixGroup = AudioMixGroup(name: mixGroupName)
    mixGroup.gain = level
    let component = AudioMixGroupsComponent(mixGroups: [mixGroup])
    audioMixerEntity.components.set(component)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/111801/4/8F764313-3800-4A2E-AD3F-92C75F4A02C2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/111801/4/8F764313-3800-4A2E-AD3F-92C75F4A02C2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/111801) — developer.apple.com. Indexed for agent consumption._