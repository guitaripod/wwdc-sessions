---
id: "wwdc2025-273"
event: "wwdc2025"
year: 2025
title: "Meet SwiftUI spatial layout"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/273"
topics: ["Design", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Meet SwiftUI spatial layout

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-273](https://developer.apple.com/videos/play/wwdc2025/273)

Explore new tools for building spatial experiences using SwiftUI. Learn the basics of 3D SwiftUI views on visionOS, customize existing layouts with depth alignments, and use modifiers to rotate and position views in space. Discover how to use spatial containers to align views in the same 3D space, helping you create immersive and engaging apps.


## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,869 words)

## Documentation & Resources

- [Canyon Crosser: Building a volumetric hike-planning app](https://developer.apple.com/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/canyon-crosser-building-a-volumetric-hike-planning-app.json
- [Human Interface Guidelines: Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-visionos

## Code Snippets

### Robot Image Frame — [3:02]

```swift
// Some views have fixed frames

Image("RobotHead")
  .border(.red)
```

### Color Frame — [3:05]

```swift
// Some views have flexible frames

Color.blue
  .border(.red)
```

### Layout Composed Frame — [3:15]

```swift
// Layouts compose the frames of their children

VStack {
  Image("RobotHead")
    .border(.red)
  Image("RobotHead")
    .border(.red)
}
.border(.yellow)
```

### Model3D Frame — [4:00]

```swift
// Some views have fixed depth

Model3D(named: "Robot")
  .debugBorder3D(.red)
```

### Zero Depth Views — [4:25]

```swift
// Many views have 0 depth

HStack {
  Image("RobotHead")
    .debugBorder3D(.red)
  Text("Hello! I'm a piece of text. I have 0 depth.")
    .debugBorder3D(.red)
  Color.blue
    .debugBorder3D(.red)
    .frame(width: 200, height: 200)
}
```

### RealityView Depth — [4:41]

```swift
// RealityView takes up all available space including depth

RealityView { content in
  // Setup RealityView content
}
.debugBorder3D(.red)
```

### GeometryReader3D Depth — [4:56]

```swift
// GeometryReader3D uses all available depth

GeometryReader3D { proxy in
  // GeometryReader3D content
}
.debugBorder3D(.red)
```

### Model3D scaledToFit3D — [5:01]

```swift
// Scaling a Model3D to fit available space

Model3D(url: robotURL) {aresolved in
  resolved.resizable()
}aplaceholder: {
  ProgressView()
}
.scaledToFit3D()
.debugBorder3D(.red)
```

### ZStack depth — [6:15]

```swift
// ZStack composes subview depths

ZStack {
  Model3D(named: "LargeRobot")
    .debugBorder3D(.red)
  Model3D(named: "BabyBot")
    .debugBorder3D(.red)
}
.debugBorder3D(.yellow)
```

### ZStack with RealityView — [6:33]

```swift
// ZStack composes subview depths

ZStack {
  RealityView { ... }
    .debugBorder3D(.red)
  Model3D(named: "BabyBot")
    .debugBorder3D(.red)
}
.debugBorder3D(.yellow)
```

### Layouts are 3D — [6:57]

```swift
// HStack also composes subview depths

HStack {
  Model3D(named: "LargeRobot")
    .debugBorder3D(.red)
  Model3D(named: "BabyBot")
    .debugBorder3D(.red)
}
.debugBorder3D(.yellow)
```

### ResizableRobotView — [7:50]

```swift
struct ResizableRobotView: View {
  let asset: Model3DAsset

  var body: some View {
    Model3D(asset: asset) { resolved in
      resolved
        .resizable()
    }
    .scaledToFit3D()
  }
}
```

### Robot Profile 1 — [8:11]

```swift
//`Layout` types back align views by default

struct RobotProfile: View {
  let robot: Robot

  var body: some View {
    VStack {
      ResizableRobotView(asset: robot.model3DAsset)
      RobotNameCard(robot: robot)
    }
    .frame(width: 300)
  }
}
```

### Customizing Vertical Alignment — [8:38]

```swift
// Customizing vertical alignment

HStack(alignment: .bottom) {
  Image("RobotHead")
    .border(.red)
  Color.blue
    .frame(width: 100, height: 100)
    .border(.red)
}
.border(.yellow)
```

### Customizing Depth Alignment — [8:52]

```swift
// Customizing depth alignments

struct RobotProfile: View {
  let robot: Robot

  var body: some View {
    VStackLayout().depthAlignment(.front) {
      ResizableRobotView(asset: robot.model3DAsset)
      RobotNameCard(robot: robot)
    }
    .frame(width: 300)
  }
}
```

### Robot Favorite Row — [9:45]

```swift
struct FavoriteRobotsRow: View {
  let robots: [Robot]

  var body: some View {
    HStack {
      RobotProfile(robot: robots[2])
      RobotProfile(robot: robots[0])
      RobotProfile(robot: robots[1])
    }
  }
}
```

### Custom Depth Alignment ID — [10:27]

```swift
// Defining a custom depth alignment guide

struct DepthPodiumAlignment: DepthAlignmentID {
  static func defaultValue(in context: ViewDimensions3D) -> CGFloat {
    context[.front]
  }
}

extension DepthAlignment {
  static let depthPodium = DepthAlignment(DepthPodiumAlignment.self)
}
```

### Customizing Depth Alignment Guides — [10:51]

```swift
// Views can customize their alignment guides

struct FavoritesRow: View {
  let robots: [Robot]

  var body: some View {
    HStackLayout().depthAlignment(.depthPodium) {
        RobotProfile(robot: robots[2])
        RobotProfile(robot: robots[0])
          .alignmentGuide(.depthPodium) {
            $0[DepthAlignment.back]
          }
        RobotProfile(robot: robots[1])
      		.alignmentGuide(.depthPodium) {
            $0[DepthAlignment.center]
          }
    }
  }
}
```

### Rotation3DEffect — [12:00]

```swift
// Rotate views using visual effects

Model3D(named: "ToyRocket")
  .rotation3DEffect(.degrees(45), axis: .z)
```

### Rotation3DLayout — [12:10]

```swift
// Rotate using any axis or angle

HStackLayout().depthAlignment(.front) {
  RocketDetailsCard()
  Model3D(named: "ToyRocket")
  	.rotation3DLayout(.degrees(isRotated ? 45 : 0), axis: .z)
}
```

### Pet Radial Layout — [14:42]

```swift
// Custom radial Layout

struct PetRadialLayout: View {
  let pets: [Pet]

  var body: some View {
    MyRadialLayout {
      ForEach(pets) { pet in
        PetImage(pet: pet)
      }
    }
  }
}
```

### Rotated Robot Carousel — [14:56]

```swift
struct RobotCarousel: View {
  let robots: [Robot]

  var body: some View {
		VStack {
      Spacer()
      MyRadialLayout {
        ForEach(robots) { robot in
          ResizableRobotView(asset: robot.model3DAsset)
          	.rotation3DLayout(.degrees(-90), axis: .x)
        }
      }
      .rotation3DLayout(.degrees(90), axis: .x)
  }
}
```

### Spatial Container — [17:00]

```swift
// Aligning views in 3D space

SpatialContainer(alignment: .topTrailingBack) {
  LargeBox()
  MediumBox()
  SmallBox()
}
```

### Spatial Overlay — [17:35]

```swift
// Aligning overlayed content

LargeBox()
  .spatialOverlay(alignment: .bottomLeadingFront) {
    SmallBox()
  }
```

### Selection Ring Spatial Overlay — [17:47]

```swift
struct RobotCarouselItem: View {
  let robot: Robot
  let isSelected: Bool

  var body: some View {
    ResizableRobotView(asset: robot.model3DAsset)
			.spatialOverlay(alignment; .bottom) {
        if isSelected {
          ResizableSelectionRingModel()
        }
  }
}
```

### DebugBorder3D — [18:32]

```swift
extension View {
  func debugBorder3D(_ color: Color) -> some View {
    spatialOverlay {
			ZStack {
				Color.clear.border(color, width: 4)
        ZStack {
          Color.clear.border(color, width: 4)
          Spacer()
          Color.clear.border(color, width: 4)
        }
        .rotation3DLayout(.degrees(90), axis: .y)
				Color.clear.border(color, width: 4)
      }
    }
  }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/273/4/f5d120d6-7302-42ff-8ced-17923f0f6aa8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/273/4/f5d120d6-7302-42ff-8ced-17923f0f6aa8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/273) — developer.apple.com. Indexed for agent consumption._