---
id: "wwdc2021-10066"
event: "wwdc2021"
year: 2021
title: "What’s new in Game Center: Widgets, friends, and multiplayer improvements"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10066"
topics: ["App Services", "App Store, Distribution & Marketing", "Essentials", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# What’s new in Game Center: Widgets, friends, and multiplayer improvements

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10066](https://developer.apple.com/videos/play/wwdc2021/10066)

Power up your online gaming experience with GameKit and adopt features like multiplayer, leaderboards, and achievements in your game. We’ll take you through the latest improvements to Game Center, including player matching and multiplayer APIs, and explore how you can boost discovery of your game.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,550 words)

## Documentation & Resources

- [Finding multiple players for a game](https://developer.apple.com/documentation/GameKit/finding-multiple-players-for-a-game) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameKit/finding-multiple-players-for-a-game
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameKit/finding-multiple-players-for-a-game.json
- [GKLocalPlayer](https://developer.apple.com/documentation/GameKit/GKLocalPlayer) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameKit/GKLocalPlayer
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameKit/GKLocalPlayer.json
- [Human Interface Guidelines: Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-center

## Code Snippets

### Friending API — [8:23]

```swift
// Call Friend Requests API to present friend request view from a view controller, when player click on Add Friends Button in your game
let error = GKLocalPlayer.local
.presentFriendRequestCreatorFromViewController(using: navigationController)

if error != nil {
    print("Fail to send friend request with error: \(error!.localizedDescription).")
}
```

### loadFriendsAuthorizationStatus — [11:47]

```swift
// Checking authorization
GKLocalPlayer.local.loadFriendsAuthorizationStatus { (authorizationStatus, error) in
    guard error == nil else {
       // Error handling
       print(“Fail to load friends list with error: \(error!.localizedDescription).”)
       return
    }

    // Handle GKFriendsAuthorizationStatus
    switch authorizationStatus {
      case .notDetermined:
         // Player have not made a choice on friends list sharing
      case .denied:
         // Player have denied your request to access their friends list
      case .restricted:
         // You should delete collected player data from your end
      case .authorized:
         // Player have authorized your request to access their friends list
    }
}
```

### loadFriends — [12:53]

```swift
func loadFriendsOnProgressionMap() async {
    do {
        let friends = try await GKLocalPlayer.local.loadFriends()
        if friends.count > 0 {
            let leaderboards = try await GKLeaderboard.loadLeaderboards(IDs: [“progress"])
            if let leaderboard = leaderboards.first {
                let entries = try await leaderboard.loadEntries(for: friends, timeScope: .allTime)
               for entry in entries.1 {
                    let avatar = try await entry.player.loadPhoto(for: .normal)
                    let name = entry.player.displayName
                    let friendLevel = entry.score
                    // Display player on progression map
                }
            }
        }
    } catch {
        print("Error: \(error.localizedDescription).")
    }
}
```

### Enable Fast Start Mode — [20:17]

```swift
// Set canStartWithMinimumPlayers to true to enable Fast Start mode
let request = GKMatchRequest()
request.minPlayers = 2
request.maxPlayers = 6
request.playerGroup = 2021

let vc = GKMatchmakerViewController(matchRequest: request)
vc.canStartWithMinimumPlayers = true
vc.delegate = self
self.present(vc, animated: true, completion: nil)
```

### Handle Players Who Join The Game — [20:39]

```swift
// Set the GKMatch delegate and present your game scene when didFindMatch is called
func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFind match: GKMatch) {
    viewController.dismiss(animated: true, completion: nil)
    let gameVC = GameSceneViewController()
    gameVC.match = match
    match.delegate = gameVC
    self.present(gameVC, animated: true, completion: nil)
}

// Add players who join later by implementing didChangeState delegate
func match(_ match: GKMatch, player: GKPlayer, didChange state: GKPlayerConnectionState) {
    if state == .connected {
        self.addPlayer(player)
    }
}
```

### Present GKMatchmakerViewController on The Invitee Side — [20:54]

```swift
// On the invitee side, present GKMatchmakerViewController with the invite
func player(_ player: GKPlayer, didAccept invite: GKInvite) {
    if let vc = GKMatchmakerViewController(invite: invite) {
        vc.matchmakerDelegate = self
        self.present(vc, animated: true, completion: nil)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10066/4/41B04DA6-0AE3-41B6-9CE1-CF48AAAF9439/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10066/4/41B04DA6-0AE3-41B6-9CE1-CF48AAAF9439/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10066) — developer.apple.com. Indexed for agent consumption._
