---
id: "wwdc2023-10273"
event: "wwdc2023"
year: 2023
title: "Work with Reality Composer Pro content in Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10273"
topics: ["Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Work with Reality Composer Pro content in Xcode

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10273](https://developer.apple.com/videos/play/wwdc2023/10273)

Learn how to bring content from Reality Composer Pro to life in Xcode. We’ll show you how to load 3D scenes into Xcode, integrate your content with your code, and add interactivity to your app. We’ll also share best practices and tips for using these tools together in your development workflow. To get the most out of this session, we recommend first watching “Meet Reality Composer Pro” and “Explore materials in Reality Composer Pro" to learn more about creating 3D scenes.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,909 words)

## Code Snippets

### Loading an entity — [3:12]

```swift
RealityView { content in
    do {
        let entity = try await Entity(named: "DioramaAssembled", in: realityKitContentBundle)
        content.add(entity)
    } catch {
        // Handle error
    }
}
```

### Adding a component — [6:39]

```swift
let component = MyComponent()
entity.components.set(component)
```

### Attachments data flow — [12:21]

```swift
RealityView { _, _ in
    // load entities from your Reality Composer Pro package bundle
} update: { content, attachments in

   if let attachmentEntity = attachments.entity(for: "🐠") {
     		content.add(attachmentEntity)
 	 }

} attachments: {
    Button { ... }
       .background(.green)
       .tag("🐠")
}
```

### Adding attachments — [15:48]

```swift
let myEntity = Entity()

RealityView { content, _ in
    if let entity = try? await Entity(named: "MyScene", in: realityKitContentBundle) {
        content.add(entity)
    }
} update: { content, attachments in

    if let attachmentEntity = attachments.entity(for: "🐠") {
        content.add(attachmentEntity)
    }

    content.add(myEntity)

} attachments: {
    Button { ... }
       .background(.green)
       .tag("🐠")
}
```

### Adding point of interest attachment entities — [20:43]

```swift
static let markersQuery = EntityQuery(where: .has(PointOfInterestComponent.self))
@State var attachmentsProvider = AttachmentsProvider()

rootEntity.scene?.performQuery(Self.markersQuery).forEach { entity in
  guard let pointOfInterest = entity.components[PointOfInterestComponent.self] else { return }

  let attachmentTag: ObjectIdentifier = entity.id

  let view = LearnMoreView(name: pointOfInterest.name, description: pointOfInterest.description)
                           .tag(attachmentTag)

   attachmentsProvider.attachments[attachmentTag] = AnyView(view)
}
```

### AttachmentsProvider — [21:40]

```swift
@Observable final class AttachmentsProvider {
    var attachments: [ObjectIdentifier: AnyView] = [:]
    var sortedTagViewPairs: [(tag: ObjectIdentifier, view: AnyView)] { ... }
}

...

@State var attachmentsProvider = AttachmentsProvider()

RealityView { _, _ in

} update: { _, _ in

} attachments: {
    ForEach(attachmentsProvider.sortedTagViewPairs, id: \.tag) { pair in
        pair.view
    }
}
```

### Design-time and Run-time components — [22:31]

```swift
// Design-time component
public struct PointOfInterestComponent: Component, Codable {
    public var region: Region = .yosemite
    public var name: String = "Ribbon Beach"
    public var description: String?
}

// Run-time component
public struct PointOfInterestRuntimeComponent: Component {
    public let attachmentTag: ObjectIdentifier
}
```

### Adding a run-time component for each design-time component — [25:38]

```swift
static let markersQuery = EntityQuery(where: .has(PointOfInterestComponent.self))
@State var attachmentsProvider = AttachmentsProvider()

rootEntity.scene?.performQuery(Self.markersQuery).forEach { entity in
  guard let pointOfInterest = entity.components[PointOfInterestComponent.self] else { return }

  let attachmentTag: ObjectIdentifier = entity.id

  let view = LearnMoreView(name: pointOfInterest.name, description: pointOfInterest.description)
                           .tag(attachmentTag)

   attachmentsProvider.attachments[attachmentTag] = AnyView(view)
   let runtimeComponent = PointOfInterestRuntimeComponent(attachmentTag: attachmentTag)
   entity.components.set(runtimeComponent)
}
```

### Adding and positioning the attachment entities — [26:19]

```swift
static let runtimeQuery = EntityQuery(where: .has(PointOfInterestRuntimeComponent.self))

RealityView { _, _ in

} update: { content, attachments in x

    rootEntity.scene?.performQuery(Self.runtimeQuery).forEach { entity in
        guard let component = entity.components[PointOfInterestRuntimeComponent.self],
              let attachmentEntity = attachments.entity(for: component.attachmentTag) else { 
            return 
        }        
        content.add(attachmentEntity)
        attachmentEntity.setPosition([0, 0.5, 0], relativeTo: entity)
    }
} attachments: {
    ForEach(attachmentsProvider.sortedTagViewPairs, id: \.tag) { pair in
        pair.view
    }
}
```

### Audio Playback — [28:55]

```swift
func playOceanSound() {

    guard let entity = entity.findEntity(named: "OceanEmitter"),
        let resource = try? AudioFileResource(named: "/Root/Resources/Ocean_Sounds_wav",
                                   from: "DioramaAssembled.usda",
                                   in: RealityContent.realityContentBundle) else { return }

    let audioPlaybackController = entity.prepareAudio(resource)
    audioPlaybackController.play()
}
```

### Terrain material transition using the slider — [31:02]

```swift
@State private var sliderValue: Float = 0.0

Slider(value: $sliderValue, in: (0.0)...(1.0))
    .onChange(of: sliderValue) { _, _ in
        guard let terrain = rootEntity.findEntity(named: "DioramaTerrain"),
                var modelComponent = terrain.components[ModelComponent.self],
                var shaderGraphMaterial = modelComponent.materials.first 
                    as? ShaderGraphMaterial else { return }
        do {
            try shaderGraphMaterial.setParameter(name: "Progress", value: .float(sliderValue))
            modelComponent.materials = [shaderGraphMaterial]
            terrain.components.set(modelComponent)
        } catch { }
    }
}
```

### Audio transition using the slider — [31:57]

```swift
@State private var sliderValue: Float = 0.0
static let audioQuery = EntityQuery(where: .has(RegionSpecificComponent.self) 
                                    && .has(AmbientAudioComponent.self))

Slider(value: $sliderValue, in: (0.0)...(1.0))
    .onChange(of: sliderValue) { _, _ in
        // ... Change the terrain material property ...

        rootEntity?.scene?.performQuery(Self.audioQuery).forEach({ audioEmitter in
            guard var audioComponent = audioEmitter.components[AmbientAudioComponent.self],
                  let regionComponent = audioEmitter.components[RegionSpecificComponent.self]
            else { return }

            let gain = regionComponent.region.gain(forSliderValue: sliderValue)
            audioComponent.gain = gain
            audioEmitter.components.set(audioComponent)
        })
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10273/5/056632D0-3346-457D-97ED-B1F066A11C1A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10273/5/056632D0-3346-457D-97ED-B1F066A11C1A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10273) — developer.apple.com. Indexed for agent consumption._
