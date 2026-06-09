---
id: "wwdc2021-10079"
event: "wwdc2021"
year: 2021
title: "Discover geometry-aware audio with the Physical Audio Spatialization Engine (PHASE)"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10079"
topics: ["Graphics & Games", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Discover geometry-aware audio with the Physical Audio Spatialization Engine (PHASE)

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10079](https://developer.apple.com/videos/play/wwdc2021/10079)

Explore how geometry-aware audio can help you build complex, interactive, and immersive audio scenes for your apps and games. Meet PHASE, Apple’s spatial audio API, and learn how the Physical Audio Spatialization Engine (PHASE) keeps the sound aligned with your experience at all times — helping you create spatial soundscapes and scenes during the development process, rather than waiting until post production. We’ll take you through an overview of the API and its classes, including Sources, Listeners, Acoustic Geometry, and Materials, and introduce the concept of Spatial Modeling. We’ll also show you how to quickly combine PHASE’s basic building blocks to start building an integrated audio experience for your app or game.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,272 words)

## Documentation & Resources

- [PHASE](https://developer.apple.com/documentation/PHASE) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PHASE
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PHASE.json

## Code Snippets

### Create an Engine and Register a Sound Asset — [18:31]

```swift
// Create an Engine in Automatic Update Mode.
let engine = PHASEEngine(updateMode: .automatic)

// Retrieve the URL to an Audio File stored in our Application Bundle.
let audioFileUrl = Bundle.main.url(forResource: "DrumLoop_24_48_Mono", withExtension: "wav")!

// Register the Audio File at the URL.
// Name it "drums", load it into resident memory and apply dynamic normalization to prepare it for playback.
let soundAsset = try engine.assetRegistry.registerSoundAsset(url: audioFileUrl,
                                                             identifier: "drums",
                                                             assetType: .resident,
                                                             channelLayout: nil,
                                                             normalizationMode: .dynamic)
```

### Register a Sound Event Asset — [20:47]

```swift
// Create a Channel Layout from a Mono Layout Tag.
let channelLayout = AVAudioChannelLayout(layoutTag: kAudioChannelLayoutTag_Mono)!

// Create a Channel Mixer from the Channel Layout.
let channelMixerDefinition = PHASEChannelMixerDefinition(channelLayout: channelLayout)

// Create a Sampler Node from "drums" and hook it into the downstream Channel Mixer.
let samplerNodeDefinition = PHASESamplerNodeDefinition(soundAssetIdentifier: "drums",
                                                       mixerDefinition: channelMixerDefinition)

// Set the Sampler Node's Playback Mode to Looping.
samplerNodeDefinition.playbackMode = .looping;

// Set the Sampler Node's Calibration Mode to Relative SPL and Level to 0 dB.
samplerNodeDefinition.setCalibrationMode(.relativeSpl, level: 0)

// Register a Sound Event Asset with the Engine named "drumEvent".
let soundEventAsset = try engine.assetRegistry.registerSoundEventAsset(rootNode:samplerNodeDefinition,
                                             identifier: "drumEvent")
```

### Start a Sound Event — [22:21]

```swift
// Create a Sound Event from the Sound Event Asset "drumEvent".
let soundEvent = try PHASESoundEvent(engine: engine, assetIdentifier: "drumEvent")

// Start the Engine.
// This will internally start the Audio IO Thread.
try engine.start()

// Start the Sound Event.
try soundEvent.start()
```

### Cleanup — [23:05]

```swift
// Stop and invalidate the Sound Event.
soundEvent.stopAndInvalidate()

// Stop the Engine.
// This will internally stop the Audio IO Thread.
engine.stop()

// Unregister the Sound Event Asset.
engine.assetRegistry.unregisterAsset(identifier: "drumEvent", completionHandler:nil)

// Unregister the Audio File.
engine.assetRegistry.unregisterAsset(identifier: "drums", completionHandler:nil)

// Destroy the Engine.
engine = nil
```

### Create a Sound Event Asset — [25:14]

```swift
// Create a Spatial Pipeline.
let spatialPipelineOptions: PHASESpatialPipeline.Options = [.directPathTransmission, .lateReverb]
let spatialPipeline = PHASESpatialPipeline(options: spatialPipelineOptions)!
spatialPipeline.entries[PHASESpatialCategory.lateReverb]!.sendLevel = 0.1;
engine.defaultReverbPreset = .mediumRoom

// Create a Spatial Mixer with the Spatial Pipeline.
let spatialMixerDefinition = PHASESpatialMixerDefinition(spatialPipeline: spatialPipeline)

// Set the Spatial Mixer's Distance Model.
let distanceModelParameters = PHASEGeometricSpreadingDistanceModelParameters()
distanceModelParameters.fadeOutParameters = PHASEDistanceModelFadeOutParameters(cullDistance: 10.0)
distanceModelParameters.rolloffFactor = 0.25
spatialMixerDefinition.distanceModelParameters = distanceModelParameters

// Create a Sampler Node from "drums" and hook it into the downstream Spatial Mixer.
let samplerNodeDefinition = PHASESamplerNodeDefinition(soundAssetIdentifier: "drums", mixerDefinition:spatialMixerDefinition)

// Set the Sampler Node's Playback Mode to Looping.
samplerNodeDefinition.playbackMode = .looping

// Set the Sampler Node's Calibration Mode to Relative SPL and Level to 12 dB.
samplerNodeDefinition.setCalibrationMode(.relativeSpl, level: 12)

// Set the Sampler Node's Cull Option to Sleep.
samplerNodeDefinition.cullOption = .sleepWakeAtRealtimeOffset;

// Register a Sound Event Asset with the Engine named "drumEvent".
let soundEventAsset = try engine.assetRegistry.registerSoundEventAsset(rootNode: samplerNodeDefinition, identifier: "drumEvent")
```

### Set Up a Listener — [27:05]

```swift
// Create a Listener.
let listener = PHASEListener(engine: engine)

// Set the Listener's transform to the origin with no rotation.
listener.transform = matrix_identity_float4x4;

// Attach the Listener to the Engine's Scene Graph via its Root Object.
// This actives the Listener within the simulation.
try engine.rootObject.addChild(listener)
```

### Set Up a Volumetric Source — [27:46]

```swift
// Create an Icosahedron Mesh.
let mesh = MDLMesh.newIcosahedron(withRadius: 0.0142, inwardNormals: false, allocator:nil)

// Create a Shape from the Icosahedron Mesh.
let shape = PHASEShape(engine: engine, mesh: mesh)

// Create a Volumetric Source from the Shape.
let source = PHASESource(engine: engine, shapes: [shape])

// Translate the Source 2 meters in front of the Listener and rotated back toward the Listener.
var sourceTransform: simd_float4x4
sourceTransform.columns.0 = simd_make_float4(-1.0, 0.0, 0.0, 0.0)
sourceTransform.columns.1 = simd_make_float4(0.0, 1.0, 0.0, 0.0)
sourceTransform.columns.2 = simd_make_float4(0.0, 0.0, -1.0, 0.0)
sourceTransform.columns.3 = simd_make_float4(0.0, 0.0, 2.0, 1.0)
source.transform = sourceTransform;

// Attach the Source to the Engine's Scene Graph.
// This actives the Listener within the simulation.
try engine.rootObject.addChild(source)
```

### Set Up an Occluder — [29:15]

```swift
// Create a Box Mesh.
let boxMesh = MDLMesh.newBox(withDimensions: simd_make_float3(0.6096, 0.3048, 0.1016),
                             segments: simd_uint3(repeating: 6),
                             geometryType: .triangles,
                             inwardNormals: false,
                             allocator: nil)

// Create a Shape from the Box Mesh.
let boxShape = PHASEShape(engine: engine, mesh:boxMesh)

// Create a Material.
// In this case, we'll make it 'Cardboard'.
let material = PHASEMaterial(engine: engine, preset: .cardboard)

// Set the Material on the Shape.
boxShape.elements[0].material = material

// Create an Occluder from the Shape.
let occluder = PHASEOccluder(engine: engine, shapes: [boxShape])

// Translate the Occluder 1 meter in front of the Listener and rotated back toward the Listener.
// This puts the Occluder half way between the Source and Listener.
var occluderTransform: simd_float4x4
occluderTransform.columns.0 = simd_make_float4(-1.0, 0.0, 0.0, 0.0)
occluderTransform.columns.1 = simd_make_float4(0.0, 1.0, 0.0, 0.0)
occluderTransform.columns.2 = simd_make_float4(0.0, 0.0, -1.0, 0.0)
occluderTransform.columns.3 = simd_make_float4(0.0, 0.0, 1.0, 1.0)
occluder.transform = occluderTransform

// Attach the Occluder to the Engine's Scene Graph.
// This actives the Occluder within the simulation.
try engine.rootObject.addChild(occluder)
```

### Start a Spatial Sound Event — [30:33]

```swift
// Associate the Source and Listener with the Spatial Mixer in the Sound Event.
let mixerParameters = PHASEMixerParameters()
mixerParameters.addSpatialMixerParameters(identifier: spatialMixerDefinition.identifier, source: source, listener: listener)

// Create a Sound Event from the built Sound Event Asset "drumEvent".
let soundEvent = try PHASESoundEvent(engine: engine, assetIdentifier: "drumEvent", mixerParameters: mixerParameters)
```

### Example 1: Footstep on creaky wood — [31:28]

```swift
// Create a Sampler Node from "footstep_wood_clip_1" and hook it into a Channel Mixer.
let footstep_wood_sampler_1 = PHASESamplerNodeDefinition(soundAssetIdentifier: "footstep_wood_clip_1", mixerDefinition: channelMixerDefinition)
```

### Example 2: Random footsteps on creaky wood — [31:54]

```swift
// Create a Sampler Node from "footstep_wood_clip_1" and hook it into a Channel Mixer.
let footstep_wood_sampler_1 = PHASESamplerNodeDefinition(soundAssetIdentifier: "footstep_wood_clip_1", mixerDefinition: channelMixerDefinition)

// Create a Sampler Node from "footstep_wood_clip_2" and hook it into a Channel Mixer.
let footstep_wood_sampler_2 = PHASESamplerNodeDefinition(soundAssetIdentifier: "footstep_wood_clip_2", mixerDefinition: channelMixerDefinition)

// Create a Random Node.
// Add 'Footstep on Creaky Wood' Sampler Nodes as children of the Random Node.
// Note that higher weights increase the likelihood of that child being chosen.
let footstep_wood_random = PHASERandomNodeDefinition()
footstep_wood_random.addSubtree(footstep_wood_sampler_1, weight: 2)
footstep_wood_random.addSubtree(footstep_wood_sampler_2, weight: 1)
```

### Example 3: Random footsteps on creaky wood or soft gravel — [32:47]

```swift
// Create a Sampler Node from "footstep_gravel_clip_1" and hook it into a Channel Mixer.
let footstep_gravel_sampler_1 = PHASESamplerNodeDefinition(soundAssetIdentifier: "footstep_gravel_clip_1", mixerDefinition: channelMixerDefinition)

// Create a Sampler Node from "footstep_gravel_clip_2" and hook it into a Channel Mixer.
let footstep_gravel_sampler_2 = PHASESamplerNodeDefinition(soundAssetIdentifier: "footstep_gravel_clip_2", mixerDefinition: channelMixerDefinition)

// Create a Random Node.
// Add 'Footstep on Soft Gravel' Sampler Nodes as children of the Random Node.
// Note that higher weights increase the likelihood of that child being chosen.
let footstep_gravel_random = PHASERandomNodeDefinition()
footstep_gravel_random.addSubtree(footstep_gravel_sampler_1, weight: 2)
footstep_gravel_random.addSubtree(footstep_gravel_sampler_2, weight: 1)

// Create a Terrain String MetaParameter.
// Set the default value to "creaky_wood".
let terrain = PHASEStringMetaParameterDefinition(value: "creaky_wood")

// Create a Terrain Switch Node.
// Add 'Random Footstep on Creaky Wood' and 'Random Footstep on Soft Gravel' as Children.
let terrain_switch = PHASESwitchNodeDefinition(switchMetaParameterDefinition: terrain)
terrain_switch.addSubtree(footstep_wood_random, switchValue: "creaky_wood")
terrain_switch.addSubtree(footstep_gravel_random, switchValue: "soft_gravel")
```

### Example 4: Random footsteps on changing terrain with a variably wet surface — [34:08]

```swift
// Create a Sampler Node from "splash_clip_1" and hook it into a Channel Mixer.
let splash_sampler_1 = PHASESamplerNodeDefinition(soundAssetIdentifier: "splash_clip_1", mixerDefinition: channelMixerDefinition)

// Create a Sampler Node from "splash_clip_2" and hook it into a Channel Mixer.
let splash_sampler_2 = PHASESamplerNodeDefinition(soundAssetIdentifier: "splash_clip_2", mixerDefinition: channelMixerDefinition)

// Create a Random Node.
// Add 'Splash' Sampler Nodes as children of the Random Node.
// Note that higher weights increase the likelihood of that child being chosen.
let splash_random = PHASERandomNodeDefinition()
splash_random.addSubtree(splash_sampler_1, weight: 9)
splash_random.addSubtree(splash_sampler_2, weight: 7)

// Create a Wetness Number MetaParameter.
// The range is [0, 1], from dry to wet. The default value is 0.5.
let wetness = PHASENumberMetaParameterDefinition(value: 0.5, minimum: 0, maximum: 1)

// Create a 'Wetness' Blend Node that blends between dry and wet terrain.
// Add 'Terrain' Switch Node and 'Splash' Random Node as children.
// As you increase the wetness, the mix between the dry footsteps and splashes will change.
let wetness_blend = PHASEBlendNodeDefinition(blendMetaParameterDefinition: wetness)
wetness_blend.addRangeForInputValues(belowValue: 1, fullGainAtValue: 0, fadeCurveType: .linear, subtree: terrain_switch)
wetness_blend.addRangeForInputValues(aboveValue: 0, fullGainAtValue: 1, fadeCurveType: .linear, subTree: splash_random)
```

### Example 5: Random footsteps on changing terrain with a variably wet surface and noisy Gore-Tex Jacket — [35:53]

```swift
// Create a Sampler Node from "gortex_clip_1" and hook it into a Channel Mixer.
let noisy_clothing_sampler_1 = PHASESamplerNodeDefinition(soundAssetIdentifier: "gortex_clip_1", mixerDefinition: channelMixerDefinition)

// Create a Sampler Node from "gortex_clip_2" and hook it into a Channel Mixer.
let noisy_clothing_sampler_2 = PHASESamplerNodeDefinition(soundAssetIdentifier: "gortex_clip_2", mixerDefinition: channelMixerDefinition)

// Create a Random Node.
// Add 'Noisy Clothing' Sampler Nodes as children of the Random Node.
// Note that higher weights increase the likelihood of that child being chosen.
let noisy_clothing_random = PHASERandomNodeDefinition()
noisy_clothing_random.addSubtree(noisy_clothing_sampler_1, weight: 3)
noisy_clothing_random.addSubtree(noisy_clothing_sampler_2, weight: 5)

// Create a Container Node.
// Add 'Wetness' Blend Node and 'Noisy Clothing' Random Node as children.
let actor_container = PHASEContainerNodeDefinition()
actor_container.addSubtree(wetness_blend)
actor_container.addSubtree(noisy_clothing_random)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10079/4/B49836DD-46CA-49CD-81CF-9D08B251FDFA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10079/4/B49836DD-46CA-49CD-81CF-9D08B251FDFA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10079) — developer.apple.com. Indexed for agent consumption._
