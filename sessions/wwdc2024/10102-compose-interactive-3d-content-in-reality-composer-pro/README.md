---
id: "wwdc2024-10102"
event: "wwdc2024"
year: 2024
title: "Compose interactive 3D content in Reality Composer Pro"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10102"
topics: ["Developer Tools", "Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Compose interactive 3D content in Reality Composer Pro

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10102](https://developer.apple.com/videos/play/wwdc2024/10102)

Discover how the Timeline view in Reality Composer Pro can bring your 3D content to life. Learn how to create an animated story in which characters and objects interact with each other and the world around them using inverse kinematics, blend shapes, and skeletal poses. We’ll also show you how to use built-in and custom actions, sequence your actions, apply triggers, and implement natural movements.

**Keywords:** `animation`, `blend shapes`, `content creation`, `cross platform`, `inverse kinematics`, `ios`, `macos`, `rcp`, `reality composer pro`, `realitykit`, `skeletal poses`, `timelines`, `visionos`, `vision pro`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,920 words)

## Documentation & Resources

- [Composing interactive 3D content with RealityKit and Reality Composer Pro](https://developer.apple.com/documentation/RealityKit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Setup IKComponent — [20:31]

```swift
// Setup IKComponent
import RealityKit

struct HeroRobotRuntimeComponent: Component {
        var rig = try? IKRig(for: modelSkeleton)

        rig.maxIterations = 30
        rig.globalFkWeight = 0.02

        let hipsJointName = "root/hips"
        let chestJointName = "root/hips/spine1/spine2/chest"
        let leftHandJointName = "root/hips/spine1/spine2/chest/…/L_arm3/L_arm4/L_arm5/L_wrist"

        rig.constraints = [
            .parent(named: "hips_constraint",
                    on: hipsJointName,
                    positionWeight: SIMD3(repeating: 90.0),
                    orientationWeight: SIMD3(repeating: 90.0)),
            .parent(named: "chest_constraint",
                    on: chestJointName,
                    positionWeight: SIMD3(repeating: 120.0),
                    orientationWeight: SIMD3(repeating: 120.0)),
            .point(named: "left_hand_constraint",
                   on: leftHandJointName,
                   positionWeight: SIMD3(repeating: 10.0))
                ]

        let resource = try? IKResource(rig: rig)                
        modelComponentEntity.components.set(IKComponent(resource: resource))
}
```

### Update IKComponent — [21:33]

```swift
// Update IKComponent
import RealityKit

struct HeroRobotRuntimeComponent: Component {
        guard let reachTarget = sceneRoot.findEntity(named: "reachTargetName") else {
            return
        }

        var reachPosition = reachTarget.position(relativeTo: entity)

        let time = sin(simTime)
        reachPosition.x += (20.0 + 50.0 * time)
        reachPosition.y += (40.0 + 30.0 * abs(time))
        reachPosition.z += (20.0 + 20.0 * abs(time))

       guard let ikComponent = modelComponentEntity.components[IKComponent.self] else {
           return
       }

       var reachPosition = reachTarget.position(relativeTo: entity)
       ...
       var leftHandConstraint = ikComponent.solvers.first?.constraints["left_hand_constraint"]
       leftHandConstraint?.target.translation = reachPosition

       // A blendValue = 0 means no influence on the constraint.
       // A blendValue = 1 means full influence on the constraint.
       var blendValue = isEnabled ? (time / totalBlendTime) : (1.0 - time / totalBlendTime)
       leftHandConstraint?.animationOverrideWeight.position = blendValue

       modelComponentEntity.components.set(ikComponent)
}
```

### Sequence and play animation actions — [24:36]

```swift
// Play Animation Actions
import RealityKit

struct HeroRobotRuntimeComponent: Component {
       let rotateAnimationResource = createRotateAnimationResource()
       let walkAndMoveAnimationGroup = createWalkAndMoveAnimationGroup()
       let alignAtHomeActionResource = createAlignAtHomeActionResource()
       let robotTravelHomeCompleteActionResource = createRobotTravelHomeCompleteAction()

       // Build a sequence of the rotate, move and align animations/actions to play.
       let moveHomeSequence = try? AnimationResource.sequence(with: [rotateAnimationResource,
                                                                    walkAndMoveAnimationGroup,
                                                                    alignAtHomeActionResource,
                                                       robotTravelHomeCompleteActionResource])

       // Play the move-to-home sequence.
       _ = robotEntity.playAnimation(moveHomeSequence)
}
```

### Setup EntityActions — [25:59]

```swift
// Setup EntityActions
import RealityKit

struct HeroRobotRuntimeComponent: Component {
    struct RobotMoveToHomeComplete: EntityAction {
        var animatedValueType: (any AnimatableData.Type)? { nil }
    }

    let travelCompleteAction = RobotMoveToHomeComplete()

    let actionResource = try! AnimationResource.makeActionAnimation(for: travelCompleteAction,
                                                                    duration: 0.1)

    let _ = robotEntity.playAnimation(actionResource)
}
```

### EntityAction subscription — [26:39]

```swift
// EntityAction subscription
import RealityKit

struct HeroRobotRuntimeComponent: Component {
                  // Subscribe to know when the EntityAction has started.
                RobotMoveToHomeComplete.subscribe(to: .started) { event in
                    if event.playbackController.entity != nil {
                        event.playbackController.stop()
                    }
                }

                // Possible states of the robot.
                public enum HeroRobotState: String, Codable {
                    case available
                    …
                    case arrivedHome
                }

               // Subscribe to know when the EntityAction has ended.
                RobotMoveToHomeComplete.subscribe(to: .ended) { event in
                    if let robotEntity = event.playbackController.entity,
                    var component = robotEntity.components[HeroRobotRuntimeComponent.self] {
                       component.setState(newState:.arrivedHome)
                    }
                }
}
```

### Setup BlendshapeWeightsComponent — [29:17]

```swift
// Setup BlendShapeWeightsComponent
import RealityKit

struct HeroPlantComponent: Component, Codable {
        guard let modelComponentEntity = findModelComponentEntity(entity: entity),
              let modelComponent = modelComponentEntity.components[ModelComponent.self]
        else { return }

            let blendShapeWeightsMapping
               = BlendShapeWeightsMapping(meshResource: modelComponent.mesh)

            // Create the blend shape weights component.
            entity.components.set(BlendShapeWeightsComponent(weightsMapping:
                                                            blendShapeWeightsMapping))
}
```

### Update BlendshapeWeightsComponent — [29:38]

```swift
// Update BlendShapeWeightsComponent

struct HeroPlantComponent: Component, Codable {
        guard let component = entity.components[BlendShapeWeightsComponent.self]
        else { return }

        var blendWeightSet = blendShapeComponent.weightSet

        // Update the weights in the BlendShapeWeightsSet
        for weightIndex in 0..<blendWeightSet[blendWeightsIndex].weights.count {
            blendWeightSet[blendWeightsIndex].weights[weightIndex] = 0.0
        }

        // Assign the new weights to the blend shape component.
       for index in 0..<blendWeightSet.count {
            component?.weightSet[blendWeightsIndex].weights = blendWeightSet[index].weights
        }
}
```

### Setup and update Skeletal Poses — [32:01]

```swift
// Update Skeletal Poses
import RealityKit

struct StationaryRobotRuntimeComponent: Component {

        guard var component = entity.components[SkeletalPosesComponent.self] 
        else {
            return
        }

        let neckRotation = calculateRotation()

        component.poses.default?.jointTransforms[neckJointIndex].rotation = neckRotation
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10102/4/5895A2B6-4F9A-4D45-A5F6-C7689F50F571/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10102/4/5895A2B6-4F9A-4D45-A5F6-C7689F50F571/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10102) — developer.apple.com. Indexed for agent consumption._
