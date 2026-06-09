---
id: "wwdc2025-214"
event: "wwdc2025"
year: 2025
title: "Get started with Game Center"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/214"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# Get started with Game Center

**Event:** WWDC25 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-214](https://developer.apple.com/videos/play/wwdc2025/214)

Explore the features of Game Center and learn how to get started. We’ll show you best practices for implementing achievements, challenges, leaderboards, and activities to maximize your game’s discoverability, attract new players, and increase engagement.

To get the most out of this session, we also recommend watching “Engage players with the Apple Games app”.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,350 words)

## Documentation & Resources

- [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/GameKit/creating-engaging-challenges-from-leaderboards) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameKit/creating-engaging-challenges-from-leaderboards
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameKit/creating-engaging-challenges-from-leaderboards.json
- [Creating activities for your game](https://developer.apple.com/documentation/GameKit/creating-activities-for-your-game) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameKit/creating-activities-for-your-game
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameKit/creating-activities-for-your-game.json
- [Game Center overview](https://developer.apple.com/game-center/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/game-center/
- [Apple Unity Plug-Ins on GitHub](https://github.com/apple/unityplugins) _download_
- [Human Interface Guidelines: Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-center

## Code Snippets

### Initialize GameKit — [4:17]

```swift
GKLocalPlayer.local.authenticateHandler = { _, error in
    print("\(GKLocalPlayer.local.alias) is ready to play!")
}
```

### Initialize GameKit (Unity) — [4:29]

```csharp
var player = await GKLocalPlayer.Authenticate();
Debug.Log($"{player.alias} is ready to play!");
```

### Submit score to challenge — [13:07]

```swift
// Submit score

GKLeaderboard.submitScore(points, 
         context: 0, 
         player: GKLocalPlayer.local,
         leaderboardIDs: ["thecoast.lb.capecod"])
```

### Activity properties — [20:24]

```swift
// Activity properties 

extension AppDelegate: GKLocalPlayerListener {

    func player(_ player: GKPlayer, wantsToPlay activity: GKGameActivity) async -> Bool {
        let activityId = activity.activityDefinition.identifier

        if activityId == "thecoast.activity" {
            let level = activity.properties["level"]

            if level == "capecod" {
                startCapeCod(activity)
            }
        }

        return true
    }

}
```

### Managing score submission with activity — [20:48]

```swift
// Managing score submission with activity 

class GameplayManager {
    let activity: GKGameActivity
    let leaderboard: GKLeaderboard

    init(activity: GKGameActivity, leaderboard: GKLeaderboard) {
        self.activity = activity
        self.leaderboard = leaderboard

        activity.start()
    }

    func setScore(_ newScore: Int) {
        activity.setScore(on: leaderboard, to: newScore)
    }

    deinit {
        activity.end()
    }
}
```

### Access the Party Code — [22:35]

```swift
extension AppDelegate: GKLocalPlayerListener {
    func player(_ player: GKPlayer, wantsToPlay activity: GKGameActivity) async -> Bool {
        let activityId = activity.activityDefinition.identifier

        if activityId == "thecoast.multiplayer" {
            startMultiplayer(partyCode: activity.partyCode)
        }

        return true
    }
}
```

### Game Center Matchmaking — [22:48]

```swift
let match = try await activity.findMatch()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/214/5/c6c0d647-5ddc-44aa-869b-d27b44774678/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/214/5/c6c0d647-5ddc-44aa-869b-d27b44774678/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/214) — developer.apple.com. Indexed for agent consumption._