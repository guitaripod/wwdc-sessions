---
id: "wwdc2024-10201"
event: "wwdc2024"
year: 2024
title: "Customize spatial Persona templates in SharePlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10201"
topics: ["Audio & Video", "Spatial Computing", "App Services"]
platforms: ["visionOS"]
hasTranscript: true
---

# Customize spatial Persona templates in SharePlay

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** visionOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10201](https://developer.apple.com/videos/play/wwdc2024/10201)

Learn how to use custom spatial Persona templates in your visionOS SharePlay experience to fine-tune the placement of Personas relative to your app. We’ll show you how to adopt custom spatial Persona templates in a sample app with SharePlay, move participants between seats, and test your changes in Simulator. We’ll also share best practices for designing custom spatial templates that will make your experience shine.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,921 words)

## Documentation & Resources

- [Building a guessing game for visionOS](https://developer.apple.com/documentation/GroupActivities/building-a-guessing-game-for-visionos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities/building-a-guessing-game-for-visionos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities/building-a-guessing-game-for-visionos.json
- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010
- [Group Activities](https://developer.apple.com/documentation/GroupActivities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities.json

## Code Snippets

### Initial team selection template — [12:32]

```swift
// Team selection template – custom spatial template

import GroupActivities

struct TeamSelectionTemplate: SpatialTemplate {
    let elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x: 0, z: 4)),

        .seat(position: .app.offsetBy(x: 1, z: 4)),
        .seat(position: .app.offsetBy(x: -1, z: 4)),

        .seat(position: .app.offsetBy(x: 2, z: 4)),
        .seat(position: .app.offsetBy(x: -2, z: 4)),
    ]
}
```

### Completed team selection template with seat roles — [13:31]

```swift
import GroupActivities

/// The custom spatial template used to arrange Spatial Personas
/// during Guess Together's team-selection stage.
///
/// The team selection template contains three sets of seats:
///
/// 1. Five audience seats that participants are initially placed in.
/// 2. Three Blue Team seats that participants are moved to
///    when they join team Blue.
/// 3. Three Red Team seats.
///
/// ```
///                ┌────────────────────┐
///                │   Guess Together   │
///                │     app window     │
///                └────────────────────┘
///
///
///              %                       $
///                %                   $
///   Blue Team      %               $      Red Team
///                    *  *  *  *  *
///
///                       Audience
/// ```
struct TeamSelectionTemplate: SpatialTemplate {
    enum Role: String, SpatialTemplateRole {
        case blueTeam
        case redTeam
    }

    let elements: [any SpatialTemplateElement] = [
        // Blue team:
        .seat(position: .app.offsetBy(x: -2.5, z: 3.5), role: Role.blueTeam),
        .seat(position: .app.offsetBy(x: -3.0, z: 3.0), role: Role.blueTeam),
        .seat(position: .app.offsetBy(x: -3.5, z: 2.5), role: Role.blueTeam),

        // Starting positions:
        .seat(position: .app.offsetBy(x: 0, z: 4)),
        .seat(position: .app.offsetBy(x: 1, z: 4)),
        .seat(position: .app.offsetBy(x: -1, z: 4)),
        .seat(position: .app.offsetBy(x: 2, z: 4)),
        .seat(position: .app.offsetBy(x: -2, z: 4)),

        // Red team:
        .seat(position: .app.offsetBy(x: 2.5, z: 3.5), role: Role.redTeam),
        .seat(position: .app.offsetBy(x: 3.0, z: 3.0), role: Role.redTeam),
        .seat(position: .app.offsetBy(x: 3.5, z: 2.5), role: Role.redTeam)
    ]
}
```

### Configuring a custom spatial template — [14:59]

```swift
systemCoordinator.configuration.spatialTemplatePreference = .custom(TeamSelectionTemplate())
```

### Assigning the local participant a spatial template role — [15:39]

```swift
systemCoordinator.assignRole(TeamSelectionTemplate.Role.blueTeam)
```

### Resigning the local participant from a spatial template role — [16:00]

```swift
systemCoordinator.resignRole()
```

### Spatial template roles — [17:00]

```swift
// Associating a role with a seat

.seat(position: .app.offsetBy(x: -2.5, z: 3.5), role: TeamSelectionTemplate.Role.blueTeam)

// Assigning the local participant a role

systemCoordinator.assignRole(TeamSelectionTemplate.Role.blueTeam)

// Resigning the local participant from their current role

systemCoordinator.resignRole()
```

### Game template with seat direction — [18:42]

```swift
import GroupActivities

/// The custom spatial template used to arrange spatial Personas
/// during Guess Together's game stage.
///
/// The team selection template contains three sets of seats:
///
/// 1. An seat to the left of the app window for the active player.
/// 2. Two seats to the right of the app window for the active player's
///    teammates.
/// 3. Five seats in front of the app window for the inactive team-members
///    and any audience members.
///
/// ```
///                  ┌────────────────────┐
///                  │   Guess Together   │
///                  │     app window     │
///                  └────────────────────┘
///
///
/// Active Player  %                       $  Active Team
///                                        $
///
///                      *  *  *  *  *
///
///                         Audience
///
/// ```
struct GameTemplate: SpatialTemplate {
    enum Role: String, SpatialTemplateRole {
        case player
        case activeTeam
    }

    var elements: [any SpatialTemplateElement] {
        let activeTeamCenterPosition = SpatialTemplateElementPosition.app.offsetBy(x: 2, z: 3)

        let playerSeat = SpatialTemplateSeatElement(
            position: .app.offsetBy(x: -2, z: 3),
            direction: .lookingAt(activeTeamCenterPosition),
            role: Role.player
        )

        let activeTeamSeats: [any SpatialTemplateElement] = [
            .seat(
                position: activeTeamCenterPosition.offsetBy(x: 0, z: -0.5),
                direction: .lookingAt(playerSeat),
                role: Role.activeTeam
            ),
            .seat(
                position: activeTeamCenterPosition.offsetBy(x: 0, z: 0.5),
                direction: .lookingAt(playerSeat),
                role: Role.activeTeam
            )
        ]

        let audienceSeats: [any SpatialTemplateElement] = [
            .seat(position: .app.offsetBy(x: 0, z: 5)),
            .seat(position: .app.offsetBy(x: 1, z: 5)),
            .seat(position: .app.offsetBy(x: -1, z: 5)),
            .seat(position: .app.offsetBy(x: 2, z: 5)),
            .seat(position: .app.offsetBy(x: -2, z: 5))
        ]

        return audienceSeats + [playerSeat] + activeTeamSeats
    }
}
```

### Configure group immersive space — [21:41]

```swift
// Configure group immersive space

for await session in GuessingActivity.sessions() {
    guard let systemCoordinator = await session.systemCoordinator else { continue }

    systemCoordinator.configuration.supportsGroupImmersiveSpace = true
}
```

### SimpleLine Template — [30:35]

```swift
// SimpleLine.swift

struct SimpleLine: SpatialTemplate {

    let elements: [any SpatialTemplateElement] = [
        .seat(position: .app.offsetBy(x:  0, z: 2)),
        .seat(position: .app.offsetBy(x:  1, z: 2)),
        .seat(position: .app.offsetBy(x: -1, z: 2)),
        .seat(position: .app.offsetBy(x:  2, z: 2)),
        .seat(position: .app.offsetBy(x: -2, z: 2))
    ]

}
```

### lookingAt Method — [31:35]

```swift
// Look at a given position or seat
.seat(
    position: teamSeatPosition,
    direction: .lookingAt(activePlayerSeat)
)
```

### alignedWith Method — [31:46]

```swift
// Look at a given position or seat
.seat(
    position: teamSeatPosition,
    direction: .lookingAt(activePlayerSeat)
)

// Align with a given app axis
.seat(
    position: teamSeatPosition,
    direction: .alignedWith(appAxis: .z)
)
```

### rotatedBy Method — [32:02]

```swift
// Look at a given position or seat
.seat(
    position: teamSeatPosition,
    direction: .lookingAt(activePlayerSeat)
)

// Align with a given app axis
.seat(
    position: teamSeatPosition,
    direction: .alignedWith(appAxis: .z)
)

// Rotate by a given angle
.seat(
    position: teamSeatPosition,
    direction: .lookingAt(.app).rotatedBy(.degrees(30))
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10201/5/10E5E470-0946-416B-AEC8-E601A8CC6045/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10201/5/10E5E470-0946-416B-AEC8-E601A8CC6045/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10201) — developer.apple.com. Indexed for agent consumption._
