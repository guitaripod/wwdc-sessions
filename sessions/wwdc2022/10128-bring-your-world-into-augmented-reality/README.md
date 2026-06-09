---
id: "wwdc2022-10128"
event: "wwdc2022"
year: 2022
title: "Bring your world into augmented reality"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10128"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring your world into augmented reality

**Event:** WWDC22 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10128](https://developer.apple.com/videos/play/wwdc2022/10128)

Follow along as we demonstrate how you can use Object Capture and RealityKit to bring real-world objects into an augmented reality game. We'll show you how to capture detailed items using the Object Capture framework, add them to a RealityKit project in Xcode, apply stylized shaders and animations, and use them as part of an AR experience. We'll also share best practices when working with ARKit, RealityKit, and Object Capture. To get the most out of this session, we recommend first watching "Dive into RealityKit 2" and "Create 3D models with Object Capture" from WWDC21.

**Keywords:** `ar`, `arkit`, `augmented reality`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,741 words)

## Documentation & Resources

- [Using object capture assets in RealityKit](https://developer.apple.com/documentation/RealityKit/using-object-capture-assets-in-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/using-object-capture-assets-in-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/using-object-capture-assets-in-realitykit.json
- [Creating a photogrammetry command-line app](https://developer.apple.com/documentation/RealityKit/creating-a-photogrammetry-command-line-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-a-photogrammetry-command-line-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-a-photogrammetry-command-line-app.json
- [Capturing photographs for RealityKit Object Capture](https://developer.apple.com/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture.json
- [Capturing photographs for RealityKit Object Capture](https://developer.apple.com/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/capturing-photographs-for-realitykit-object-capture.json
- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/RealityKit/building-an-immersive-experience-with-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/building-an-immersive-experience-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/building-an-immersive-experience-with-realitykit.json
- [RealityKit](https://developer.apple.com/documentation/RealityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit.json

## Code Snippets

### HighRes capturing — [6:20]

```swift
if let hiResCaptureVideoFormat = ARWorldTrackingConfiguration.recommendedVideoFormatForHighResolutionFrameCapturing {
    // Assign the video format that supports hi-res capturing.
config.videoFormat = hiResCaptureVideoFormat
}
// Run the session.
session.run(config)

session.captureHighResolutionFrame { (frame, error) in
   if let frame = frame {
      // save frame.capturedImage 
      // …   
   }
}
```

### Chessboard animation — [17:00]

```swift
// Board Animation
class Chessboard: Entity {
    func playAnimation() {
        checkers
            .forEach { entity in
                let currentTransform = entity.transform
        // Move checker square 10cm up
                entity.transform.translation += SIMD3<Float>(0, 0.1, 0)
                entity.move(to: currentTransform,
                    relativeTo: entity.parent,
                    duration: BoardGame.startupAnimationDuration)
            }

        // Play built-in animation for board border
        border.availableAnimations.forEach {
            border.playAnimation($0)
        }
    }
}
```

### select chess piece — [18:00]

```swift
// Select chess piece
class ChessViewport: ARView {
    @objc
    func handleTap(sender: UITapGestureRecognizer) {
        guard let ray = ray(through: sender.location(in: self)) else { return }

        // No piece is selected yet, we want to select one
        guard let raycastResult = scene.raycast(origin: ray.origin,
                                                direction: ray.direction,
                                                length: 5,
                                                query: .nearest,
                                                mask: .piece).first,
              let piece = raycastResult.entity.parentChessPiece else {
            return
        }
        boardGame.select(piece)
        gameManager.selectedPiece = piece
    }
}
```

### capture geometry modifier — [21:16]

```swift
// Capture Geometry Modifier
class ChessPiece: Entity, HasChessPiece {
    var capturedProgress: Float
        get {
            (pieceEntity?.model?.materials.first as? CustomMaterial)?.custom.value[0] ?? 0
        }
        set {
            pieceEntity?.modifyMaterials { material in
                guard var customMaterial = material as? CustomMaterial else {
                    return material
                }
                customMaterial.custom.value = SIMD4<Float>(newValue, 0, 0, 0)
                return customMaterial
            }
        }
    }
}
```

### highlight potential moves using bloom — [23:00]

```swift
// Checker animation to show potential moves
void checkerSurface(realitykit::surface_parameters params,
                    float amplitude,
                    bool isBlack = false)
{
    // ...
    bool isPossibleMove = params.uniforms().custom_parameter()[0];
    if (isPossibleMove) {
        const float a = amplitude * sin(params.uniforms().time() * M_PI_F) + amplitude;
        params.surface().set_emissive_color(half3(a));
        if (isBlack) {
            params.surface().set_base_color(half3(a));
        }
    }
}
```

### Import MetalPerformanceShaders — [23:20]

```swift
import MetalPerformanceShaders

class ChessViewport: ARView {
    init(gameManager: GameManager) {
        /// ...
        renderCallbacks.postProcess = postEffectBloom
    }

    func postEffectBloom(context: ARView.PostProcessContext) {
        let brightness = MPSImageThresholdToZero(device: context.device,
                                                 thresholdValue: 0.85,
                                                 linearGrayColorTransform: nil)
        brightness.encode(commandBuffer: context.commandBuffer,
                          sourceTexture: context.sourceColorTexture,
                          destinationTexture: bloomTexture!)
        /// ...
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10128/3/A48642CC-4EA4-478D-BC86-9AD9FE213885/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10128/3/A48642CC-4EA4-478D-BC86-9AD9FE213885/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10128) — developer.apple.com. Indexed for agent consumption._
