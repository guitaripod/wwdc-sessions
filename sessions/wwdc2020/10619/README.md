---
id: "wwdc2020-10619"
event: "wwdc2020"
year: 2020
title: "Tap into Game Center: Leaderboards, Achievements, and Multiplayer"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10619"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Tap into Game Center: Leaderboards, Achievements, and Multiplayer

**Event:** WWDC20 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10619](https://developer.apple.com/videos/play/wwdc2020/10619)

Level up your Game Center integration and enable players to compare scores on leaderboards, earn valuable achievements, and engage with other players. Organize special events like weekly championships, daily showdowns, or 1-hour competitions using recurring leaderboards. Create up to 100 unique achievements for your game. And we'll show you how to set up real-time or turn-based multiplayer matches for your Game Center players.

If you want to learn more about Game Center’s interface, Dashboard, and player profiles, check out “Tap into Game Center: Dashboard, Access Point, and Profile.”

And for more about preparing your game’s interface for these new capabilities, see “Design for Game Center.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,842 words)

## Code Snippets

### Submitting a score — [4:05]

```swift
// Use the class method to submit score to one or more leaderboards at once
GKLeaderboard.submitScore(self.points, context: 0, player: GKLocalPlayer.local,
    leaderboardIDs: ["my.leaderboard.id"]) { error in
}
```

### Submitting a score - recurring leaderboard ID — [4:30]

```swift
// Use the class method to submit score to one or more leaderboards at once
GKLeaderboard.submitScore(self.points, context: 0, player: GKLocalPlayer.local,
    leaderboardIDs: ["my.recurring.leaderboard.id"]) { error in
}
```

### Submitting to a specific occurrence of a recurring leaderboard — [4:48]

```swift
// Submitting to a specific occurrence of a recurring leaderboard
GKLeaderboard.loadLeaderboards(IDs:["my.recurring.leaderboard.id"]) { (fetchedLBs, error) in
    if let lb = fetchedLBs?.first {
       lb.submitScore(self.points, context: 0, player: GKLocalPlayer.local) { error in
       }
    }
}
```

### Launching in-game UI — [5:33]

```swift
// Launching in-game UI

// Display a list of leaderboards
let vc = GKGameCenterViewController(
             state: .leaderboards)
vc.gameCenterDelegate = self
present(vc, animated: true, completion: nil)


// Or directly display scores for a specific leaderboard
let vc = GKGameCenterViewController(
             leaderboardID: "YOUR_ASC_LEADERBOARD_ID",
             playerScope: .global,
             timeScope: .allTime)
vc.gameCenterDelegate = self
present(vc, animated: true, completion: nil)
```

### Accessing previous occurrence — [7:14]

```swift
// Accessing previous occurrence

// Load current occurrence of a recurring leaderboard
GKLeaderboard.loadLeaderboards(IDs:["my.recurring.leaderboard.id"]) { (fetchedLBs, error) in
    if let current = fetchedLBs?.first {
       // Load previous occurrence using the current occurrence
       current.loadPreviousOccurrence { (prevOccurrence, error) in
           // Do something with the previous occurrence
       }
    }
}
```

### Reporting achievement progress — [14:34]

```swift
if let achievement = GKAchievement(identifier: identifier) {
    achievement.percentComplete = percentComplete
    GKAchievement.report([achievement]) { error in
        if let error = error {
            print("Error in reporting achievements: \(error)")
        }
    }
}
```

### Displaying Game Center achievements — [16:05]

```swift
// Showing the Game Center achievements page

let viewController = GKGameCenterViewController(state: .achievements)
viewController.gameCenterDelegate = self
present(viewController, animated: true)
```

### Check if personalized communication is restricted — [23:50]

```swift
// Check if personalized communication is restricted
if GKLocalPlayer.local.personalizedCommunicationRestricted {
    // Disable UI for Voice chat
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10619/4/05AE01B8-DBEB-4628-B955-167A86ECB3AE/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10619) — developer.apple.com. Indexed for agent consumption._