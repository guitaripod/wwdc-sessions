---
id: "wwdc2024-10091"
event: "wwdc2024"
year: 2024
title: "Meet TabletopKit for visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10091"
topics: ["Spatial Computing", "Graphics & Games"]
platforms: ["visionOS"]
hasTranscript: true
---

# Meet TabletopKit for visionOS

**Event:** WWDC24 · **Topic:** Graphics & Games · **Platforms:** visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10091](https://developer.apple.com/videos/play/wwdc2024/10091)

Build a board game for visionOS from scratch using TabletopKit. We’ll show you how to set up your game, add powerful rendering using RealityKit, and enable multiplayer using spatial Personas in FaceTime with only a few extra lines of code.

**Keywords:** `arkit`, `facetime`, `games`, `shareplay`, `spatial personas`, `tabletopkit`, `visionos games`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,457 words)

## Documentation & Resources

- [TabletopKit](https://developer.apple.com/documentation/TabletopKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TabletopKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TabletopKit.json
- [Creating tabletop games](https://developer.apple.com/documentation/TabletopKit/creating-tabletop-games) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TabletopKit/creating-tabletop-games
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TabletopKit/creating-tabletop-games.json
- [Forum: Graphics & Games](https://developer.apple.com/forums/topics/graphics-and-games?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/graphics-and-games?cid=vf-a-0010

## Code Snippets

### Make a rectangular table — [3:52]

```swift
// Make a rectangular table.

let entity = try! Entity.load(named: "table", in: table_Top_KitBundle)
let table: Tabletop = .rectangular(entity: entity)
```

### Place seats — [4:25]

```swift
// Place 3 seats around the table, facing the center.

static let seatPoses: [TableVisualState.Pose2D] = [
  .init(position: .init(x: 0, y: Double(GameMetrics.tableDimensions.z)),
        rotation: .degrees(0)),
  .init(position: .init(x: -Double(GameMetrics.tableDimensions.x), y: 0),
        rotation: .degrees(-90)),
  .init(position: .init(x: Double(GameMetrics.tableDimensions.x), y: 0),
        rotation: .degrees(90))
]
```

### Define player pawns — [5:40]

```swift
// Define an object that describes a pawn for each player.

struct PlayerPawn: EntityEquipment {
  let id: ID
  let entity: Entity
  var initialState: BaseEquipmentState

  init(id: ID, seat: PlayerSeat, pose: TableVisualState.Pose2D, entity: Entity) {
    self.id = id
    self.entity = entity
    initialState = .init(seatControl: .restricted([seat.id]),
                pose: pose,
                entity: entity)
  }
}
```

### Define an object that describes a tile — [6:55]

```swift
// Define an object that describes a tile on the conveyor belt

struct ConveyorTile: Equipment {
  enum Category: String {
    case red
    case green
    case grey
  }

  let id: ID
  let category: ConveyorTile.Category
  let initialState: BaseEquipmentState

  init(id: ID, boardID: EquipmentIdentifier, position: TableVisualState.Point2D, category: ConveyorTile.Category) {
    self.id = id
    self.category = category
    initialState = .init(parentID: boardID,
              pose: .init(position: position, rotation: .init()),
              boundingBox: .init(center: .zero, size: .init(x: 0.06, y: 0, z: 0.06)))
```

### Monitor interactions — [9:53]

```swift
// The view contains all the content in the game.

RealityView { (content: inout RealityViewContent) in
  content.entities.append(loadedGame.renderer.root)
}.tabletopGame(loadedGame.tabletop, parent: loadedGame.renderer.root) { _ in
  GameInteraction(game: loadedGame)
}


// Define an object that manages player interactions.

struct GameInteraction: TabletopInteraction {
  func update(context: TabletopKit.TabletopInteractionContext, 
                value: TabletopKit.TabletopInteractionValue) {
    switch value.phase {
      //...
  }
```

### Respond to interaction updates — [10:48]

```swift
// Respond to interaction updates.

func update(context: TabletopKit.TabletopInteractionContext, 
              value: TabletopKit.TabletopInteractionValue) {
  switch value.phase {
    //...
    case .ended: {
      guard let dst = value.proposedDestination.equipmentID else {
        return
      }
      context.addAction(.moveEquipment(matching: value.startingEquipmentID, childOf: dst))
    }
 }
```

### Add a sound effect to the die roll — [12:52]

```swift
// Respond to interaction updates.

func update(context: TabletopKit.TabletopInteractionContext, 
              value: TabletopKit.TabletopInteractionValue) {
  switch value.gesturePhase {
    //...
    case .ended: {
      if let die = game.tabletop.equipment(of: Die.self, 
                                     matching: value.startingEquipmentID) {
        if let audioLibraryComponent = die.entity.components[AudioLibraryComponent.self] {
          if let soundResource = audioLibraryComponent.resources["dieSoundShort.mp3"] {
            die.entity.playAudio(soundResource)
          }
        }
      }
    }
  }
}
```

### Set up multiplayer with SharePlay — [14:44]

```swift
// Set up multiplayer using SharePlay.
// Provide a button to begin SharePlay.

import GroupActivities
func shareplayButton() -> some View {
  Button("SharePlay", systemImage: "shareplay") {
  Task {try! await Activity().activate() }
  }
}


// After joining the SharePlay session, start multiplayer.

    sessionTask = Task.detached { @MainActor in
      for await session in Activity.sessions() {
        tabletopGame.coordinateWithSession(session)
      }
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10091/4/67E4D497-91F1-4537-9344-F08BBADDCD3F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10091/4/67E4D497-91F1-4537-9344-F08BBADDCD3F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10091) — developer.apple.com. Indexed for agent consumption._