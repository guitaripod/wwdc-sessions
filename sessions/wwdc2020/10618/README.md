---
id: "wwdc2020-10618"
event: "wwdc2020"
year: 2020
title: "Tap into Game Center: Dashboard, Access Point, and Profile"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10618"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Tap into Game Center: Dashboard, Access Point, and Profile

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10618](https://developer.apple.com/videos/play/wwdc2020/10618)

Apple’s social gaming network is ready to play. We’ll walk you through the latest updates to Game Center, starting with its in-game interface and all-new player experience. Learn how to integrate GameKit into your app and authenticate players effectively, and discover the Access Point, which brings players into the in-game dashboard. From there, we’ll explore player profiles and their options for privacy.

After exploring Game Center’s interface, Dashboard, and player profiles, continue to the next video to learn about Leaderboards, Achievements, and Multiplayer gaming. 

And for more about preparing your game’s interface for these new capabilities, see “Design for Game Center.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,458 words)

## Documentation & Resources

- [Human Interface Guidelines: Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-center

## Code Snippets

### Presenting the main dashboard — [10:05]

```swift
// GKGameCenterViewController

public init(state:)
[...]

// Example: Display Main Dashboard
let vc = GKGameCenterViewController(state: .dashboard)
vc.gameCenterDelegate = self
present(vc, animated: true, completion: nil) 

[...]
enum GKGameCenterViewControllerState : Int {
   case `default`
   case leaderboards
   case achievements
   case challenges
   case localPlayerProfile
   case dashboard
}
```

### Display a specific leaderboard — [10:51]

```swift
// Display scores for a specific leaderboard
let vc = GKGameCenterViewController(
                leaderboardID: "grp.xyz.laketahoe",
                playerScope: .global,
                timeScope: .allTime)
vc.gameCenterDelegate = self
present(vc, animated: true, completion: nil)
```

### Configure and show Access Point — [13:18]

```swift
// Configure and show Access Point
func showMainMenu() {
    // Call your code to setup the main menu
    self.setupMainMenu()

    // Place access point on top left   
    GKAccessPoint.shared.location = .topLeading    

    // Show highlights
    GKAccessPoint.shared.showHighlights = true

    // Show it!
    GKAccessPoint.shared.isActive = true
}
```

### Observing isPresentingGameCenter — [14:00]

```swift
let observation = GKAccessPoint.shared.observe(
           \.isPresentingGameCenter
    ) { [weak self] _,_ in
    self.paused = GKAccessPoint.shared.isPresentingGameCenter
}
```

### Changing the frame — [14:44]

```swift
// Observable properties
// frameInScreenCoordinates

let observation = GKAccessPoint.shared.observe(
           \.frameInScreenCoordinates
    ) { [weak self] _,_ in
    let screenFrame = GKAccessPoint.shared.frameInScreenCoordinates
    let accessPointFrame = myView.convert(screenFrame, from: nil)
    // adjust your layout
}
```

### Handling focus — [15:18]

```swift
// Apple TV and controllers

// track and update focus
func trackController(position: CGPoint) {
  let screenFrame = GKAccessPoint.shared.frameInScreenCoordinates
  let accessFrame = myView.convert(screenFrame, from: nil)
  // if the point is in the access point turn on feedback
  accessPointElement.focusFeedback = CGRectContainsPoint(accessFrame, position)
}
```

### Handling selection — [15:38]

```swift
// Apple TV and controllers

// Handle selection
func accessPointSelected() {
  GKAccessPoint.shared.triggerAccessPoint {}
}
```

### Showing the player profile — [20:01]

```swift
// Local player profile

let profileVC = GKGameCenterViewController(state: .localPlayerProfile)
profileVC.gameCenterDelegate = self

present(profileVC, animated: true, completion: nil)
```

### Player restrictions — [20:28]

```swift
// Local player restrictions

GKLocalPlayer.local.authenticateHandler = { viewController, error in
    let isGameCenterReady = (viewController == nil) && (error == nil)

    if isGameCenterReady {
        if GKLocalPlayer.local.isUnderage {
            // Hide explicit game content
        }

        if GKLocalPlayer.local.isMultiplayerGamingRestricted {
            // Disable multiplayer game features
        } 

        if GKLocalPlayer.local.isPersonalizedCommunicationRestricted {
            // Disable in game communication UI
        }    
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10618/5/02361057-A8F2-462F-A302-376CF48B17FF/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10618) — developer.apple.com. Indexed for agent consumption._