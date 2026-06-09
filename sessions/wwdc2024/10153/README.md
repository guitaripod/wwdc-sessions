---
id: "wwdc2024-10153"
event: "wwdc2024"
year: 2024
title: "Dive deep into volumes and immersive spaces"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10153"
topics: ["Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Dive deep into volumes and immersive spaces

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10153](https://developer.apple.com/videos/play/wwdc2024/10153)

Discover powerful new ways to customize volumes and immersive spaces in visionOS. Learn to fine-tune how volumes resize and respond to people moving around them. Make volumes and immersive spaces interact through the power of coordinate conversions. Find out how to make your app react when people adjust immersion with the Digital Crown, and use a surrounding effect to dynamically customize the passthrough tint in your immersive space experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,301 words)

## Documentation & Resources

- [BOT-anist](https://developer.apple.com/documentation/visionOS/BOT-anist) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/BOT-anist
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/BOT-anist.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### Baseplate — [3:09]

```swift
// Baseplate

WindowGroup(id: "RobotExploration") {
    ExplorationView()
        .volumeBaseplateVisibility(.visible) // Default!
}
.windowStyle(.volumetric)
```

### Enabling resizability — [4:29]

```swift
// Enabling resizability

WindowGroup(id: "RobotExploration") {
    let initialSize = Size3D(width: 900, height: 500, depth: 900)

    ExplorationView()
        .frame(minWidth: initialSize.width, maxWidth: initialSize.width * 2,
               minHeight: initialSize.height, maxHeight: initialSize.height * 2)
        .frame(minDepth: initialSize.depth, maxDepth: initialSize.depth * 2)
}
.windowStyle(.volumetric)
.windowResizability(.contentSize) // Default!
```

### Programmatic resize — [6:10]

```swift
// Programmatic resize

struct ExplorationView: View {
    @State private var levelScale: Double = 1.0

    var body: some View {
        RealityView { content in
            // Level code here
        } update: { content in
            appState.explorationLevel?.setScale(
                [levelScale, levelScale, levelScale], relativeTo: nil)
        }
        .frame(width: levelSize.value.width * levelScale,
               height: levelSize.value.height * levelScale)
        .frame(depth: levelSize.value.depth * levelScale)
        .overlay { Button("Change Size") { levelScale = levelScale == 1.0 ? 2.0 : 1.0 } }
    }
}
```

### Toolbar ornament — [7:39]

```swift
// Toolbar ornament

ExplorationView()
.toolbar {
		ToolbarItem {
      	Button("Next Size") {
          	levelScale = levelScale == 1.0 ? 2.0 : 1.0
        }
    }
  	ToolbarItemGroup {
      	Button("Replay") {
          	resetExploration()
        }
      	Button("Exit Game") {
          	exitExploration()
          	openWindow(id: "RobotCreation")
        }
    }
}
```

### Ornaments — [10:41]

```swift
// Ornaments

WindowGroup(id: "RobotExploration") {
    ExplorationView()
    .ornament(attachmentAnchor: .scene(.topBack)) {
        ProgressView()
    }
}
.windowStyle(.volumetric)
```

### Volume viewpoint — [12:08]

```swift
// Volume viewpoint

struct ExplorationView: View {
    var body: some View {
        RealityView { content in
            // Some RealityKit code
        }
        .onVolumeViewpointChange { oldValue, newValue in
            appState.robot?.currentViewpoint = newValue.squareAzimuth
        }
    }
}
```

### Using volume viewpoint — [13:06]

```swift
// Volume viewpoint

class RobotCharacter {

    func handleMovement(deltaTime: Float) {
        if self.robotState == .idle {
            characterModel.performRotation(toFace: self.currentViewpoint, duration: 0.5)
            self.animationState.transition(to: .wave)
        } else {
            // Handle normal movement
        }
    }
}
```

### Supported viewpoints — [13:43]

```swift
// Supported viewpoints
struct ExplorationView: View {
  	let supportedViewpoints: Viewpoint3D.SquareAzimuth.Set = [.front, .left, .right]

  	var body: some View {
      	RealityView { content in
        		// Some RealityKit code
        }
      	.supportedVolumeViewpoints(supportedViewpoints)
      	.onVolumeViewpointChange { _, newValue in
        		appState.robot?.currentViewpoint = newValue.squareAzimuth
        }
    }
}
```

### Viewpoint update strategy — [14:30]

```swift
// Viewpoint update strategy

struct ExplorationView: View {
    let supportedViewpoints: Viewpoint3D.SquareAzimuth.Set = [.front, .left, .right]

    var body: some View {
        RealityView { content in
            // Some RealityKit code
        }
        .supportedVolumeViewpoints(supportedViewpoints)
        .onVolumeViewpointChange(updateStrategy: .all) { _, newValue in
            appState.robot?.currentViewpoint = newValue.squareAzimuth
            if !supportedViewpoints.contains(newValue) {
                appState.robot?.animationState.transition(to: .annoyed)
            }
        }
    }
}
```

### World alignment — [16:42]

```swift
// World alignment

WindowGroup {
    ExplorationView()
    .volumeWorldAlignment(.gravityAligned)
}
.windowStyle(.volumetric)
```

### Dynamic scale — [18:05]

```swift
// Dynamic scale

WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
.defaultWorldScalingBehavior(.dynamic)
```

### Starting with an empty immersive space — [19:16]

```swift
struct BotanistApp: App {
    var body: some Scene {
        // Volume
        WindowGroup(id: "Exploration") {
            VolumeExplorationView()
        }
        .windowStyle(.volumetric)

        // Immersive Space
        ImmersiveSpace(id: "Immersive") {
            EmptyView()
        }
    }
}
```

### Callout to convert function from volume view — [20:52]

```swift
// Coordinate conversions
// Convert from RealityKit entity in volume to SwiftUI space
struct VolumeExplorationView: View {
    @Environment(ImmersiveSpaceAppModel.self) var appModel

    var body: some View {
        RealityView { content in
            content.add(appModel.volumeRoot)
            // ...
        } update: { content in
            guard appModel.convertingRobotFromVolume else { return }

            // Convert the robot transform from RealityKit scene space for
            // the volume to SwiftUI immersive space
            convertRobotFromRealityKitToImmersiveSpace(content: content)
        }
    }
}
```

### Convert robot's transform to SwiftUI immersive space — [21:08]

```swift
// Coordinate conversions
// Convert from RealityKit entity in volume to SwiftUI space
func convertRobotFromRealityKitToImmersiveSpace(content: RealityViewContent) {
    // Convert the robot transform from RealityKit scene space for
    // the volume to SwiftUI immersive space
    appModel.immersiveSpaceFromRobot =
        content.transform(from: appModel.robot, to: .immersiveSpace)

    // Reparent robot from volume to immersive space
    appModel.robot.setParent(appModel.immersiveSpaceRoot)

    // Handoff to immersive space view to continue conversions.
    appModel.convertingRobotFromVolume = false
    appModel.convertingRobotToImmersiveSpace = true
}
```

### Callout to convert function from immersive space view — [21:42]

```swift
// Coordinate conversions
// Convert from SwiftUI immersive space back to RealityKit local space
struct ImmersiveExplorationView: View {
    @Environment(ImmersiveSpaceAppModel.self) var appModel

    var body: some View {
        RealityView { content in
            content.add(appModel.immersiveSpaceRoot)
        } update: { content in
            guard appModel.convertingRobotToImmersiveSpace else { return }

            // Convert the robot transform from SwiftUI space for the immersive
            // space to RealityKit scene space
            convertRobotFromSwiftUIToRealityKitSpace(content: content)
        }
    }
}
```

### Compute transform to place robot in matching position in immersive space — [21:48]

```swift
// Coordinate conversions
// Calculate transform from SwiftUI to RealityKit scene space
func convertRobotFromSwiftUIToRealityKitSpace(content: RealityViewContent) {
    // Calculate transform from SwiftUI immersive space to RealityKit
    // scene space
    let realityKitSceneFromImmersiveSpace =
    content.transform(from: .immersiveSpace, to: .scene)

    // Multiply with the robot's transform in SwiftUI immersive space to build a
    // transformation which converts from the robot's local
    // coordinate space in the volume and ends with the robot's local
    // coordinate space in an immersive space.
    let realityKitSceneFromRobot =
    realityKitSceneFromImmersiveSpace * appModel.immersiveSpaceFromRobot

    // Place the robot in the immersive space to match where it
    // appeared in the volume
    appModel.robot.transform = Transform(realityKitSceneFromRobot)

    // Start the jump!
    appModel.startJump()
}
```

### Customizing immersion — [23:54]

```swift
// Customizing immersion
struct BotanistApp: App {
    // Custom immersion amounts
    @State private var immersionStyle: ImmersionStyle = .progressive(0.2...1.0, initialAmount: 0.8)

    var body: some Scene {
        // Immersive Space
        ImmersiveSpace(id: "ImmersiveSpace") {
            ImmersiveSpaceExplorationView()
        }
        .immersionStyle(selection: $immersionStyle, in: .mixed, .progressive, .full)
    }
}
```

### Callout to function to handle immersion amount changed — [25:17]

```swift
// Reacting to immersion
struct ImmersiveView: View {
    @State var immersionAmount: Double?

    var body: some View {
        ImmersiveSpaceExplorationView()
            .onImmersionChange { context in
                immersionAmount = context.amount
            }
            .onChange(of: immersionAmount) { oldValue, newValue in
                handleImmersionAmountChanged(newValue: newValue, oldValue: oldValue)
            }
    }
}
```

### Handle function to make robot react to changed immersion amount — [25:39]

```swift
// Reacting to immersion
func handleImmersionAmountChanged(newValue: Double?, oldValue: Double?) {
    guard let newValue, let oldValue else {
        return
    }

    if newValue > oldValue {
        // Move the robot outward to react to increasing immersion
        moveRobotOutward()
    } else if newValue < oldValue {
        // Move the robot inward to react to decreasing immersion
        moveRobotInward()
    }
}
```

### Create spatial tracking session — [26:57]

```swift
// Create and run spatial tracking session
struct ImmersiveExplorationView {
    @State var spatialTrackingSession: SpatialTrackingSession
        = SpatialTrackingSession()

    var body: some View {
        RealityView { content in
            // ...
        }
        .task {
            await runSpatialTrackingSession()
        }
    }
}
```

### Run spatial tracking session — [27:11]

```swift
// Create and run the spatial tracking session
func runSpatialTrackingSession() async {
    // Configure the session for plane anchor tracking
    let configuration =
        SpatialTrackingSession.Configuration(tracking: [.plane])

    // Run the session to request plane anchor transforms
    let _ = await spatialTrackingSession.run(configuration)
}
```

### Create a floor anchor to track — [27:32]

```swift
// Create a floor anchor to track
struct ImmersiveExplorationView {
    @State var spatialTrackingSession: SpatialTrackingSession
        = SpatialTrackingSession()

    let floorAnchor = AnchorEntity(
        .plane(.horizontal, classification: .floor, minimumBounds: .init(x: 0.01, y: 0.01))
    )

    var body: some View {
        RealityView { content in
            content.add(floorAnchor)
        }
        .task {
            await runSpatialTrackingSession()
        }
    }
}
```

### Detect taps on entities in immersive space — [27:54]

```swift
// Detect taps on entities in immersive space
RealityView { content in
    // ...
}
.gesture(
    SpatialTapGesture(
        coordinateSpace: .immersiveSpace
    )
    .targetedToAnyEntity()
    .onEnded { value in
        handleTapOnFloor(value: value)
    }
)
```

### Handle tap event to place plant — [28:09]

```swift
// Handle tap event
func handleTapOnFloor(value: EntityTargetValue<SpatialTapGesture.Value>) {
    let location =
        value.convert(value.location3D, from: .immersiveSpace, to: floorAnchor)

    plantEntity.position = location
    floorAnchor.addChild(plantEntity)
}
```

### Add tint color to custom plant component — [29:47]

```swift
// Add tint color to custom plant component
struct PlantComponent: Component {
    var tintColor: Color {
        switch plantType {
        case .coffeeBerry:
            // Light blue
            return Color(red: 0.3, green: 0.3, blue: 1.0)
        case .poppy:
            // Magenta
            return Color(red: 1.0, green: 0.0, blue: 1.0)
        case .yucca:
            // Light green
            return Color(red: 0.2, green: 1.0, blue: 0.2)
        }
    }
}
```

### Handle collisions with robot — [30:09]

```swift
// Handle collisions with robot
//
// Handle movement of the robot between frames
func handleMovement(deltaTime: Float) {
    // Move character in the collision world
    appModel.robot.moveCharacter(by: SIMD3<Float>(...), deltaTime: deltaTime, relativeTo: nil) { collision in
        handleCollision(collision)
    }
}
```

### Set active tint color when colliding with plant — [30:29]

```swift
// Set active tint color when colliding with plant
//
// Handle collision between robot and hit entity
func handleCollision(_ collision: CharacterControllerComponent.Collision) {
    guard let plantComponent = collision.hitEntity.components[PlantComponent.self] else {
        return
    }

    // Play the plant growth celebration animation
    playPlantGrowthAnimation(plantComponent: plantComponent)

    if inImmersiveSpace {
        appModel.tintColor = plantComponent.tintColor
    }
}
```

### Apply effect to tint passthrough — [30:48]

```swift
// Apply effect to tint passthrough
struct ImmersiveExplorationView: View {
    var body: some View {
        RealityView { content in
            // ...
        }
        .preferredSurroundingsEffect(surroundingsEffect)
    }

    // The resolved surroundings effect based on tint color
    var surroundingsEffect: SurroundingsEffect? {
        if let color = appModel.tintColor {
            return SurroundingsEffect.colorMultiply(color)
        } else {
            return nil
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10153/4/0A359A0C-A9DB-4D61-872E-FCEA96763C78/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10153/4/0A359A0C-A9DB-4D61-872E-FCEA96763C78/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10153) — developer.apple.com. Indexed for agent consumption._