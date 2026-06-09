---
id: "wwdc2022-110356"
event: "wwdc2022"
year: 2022
title: "Meet distributed actors in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110356"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet distributed actors in Swift

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110356](https://developer.apple.com/videos/play/wwdc2022/110356)

Discover distributed actors — an extension of Swift’s actor model that simplifies development of distributed systems. We'll explore how distributed actor isolation and location transparency can help you avoid the accidental complexity of networking, serialization, and other transport concerns when working with distributed apps and systems. To get the most out of this session, watch “Protect mutable state with Swift actors” from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,368 words)

## Documentation & Resources

- [TicTacFish: Implementing a game using distributed actors](https://developer.apple.com/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors.json
- [Swift Forums: Distributed Actors](https://forums.swift.org/c/server/distributed-actors/79) _documentation_
- [SE-0344: Distributed Actor Runtime](https://github.com/apple/swift-evolution/blob/main/proposals/0344-distributed-actor-runtime.md) _guide_
- [SE-0336: Distributed Actor Isolation](https://github.com/apple/swift-evolution/blob/main/proposals/0336-distributed-actor-isolation.md) _guide_
- [Swift Distributed Actors Cluster Library](https://github.com/apple/swift-distributed-actors/) _guide_

## Code Snippets

### actor OfflinePlayer — [4:49]

```swift
public actor OfflinePlayer: Identifiable {
    nonisolated public let id: ActorIdentity = .random

    let team: CharacterTeam
    let model: GameViewModel
    var movesMade: Int = 0

    public init(team: CharacterTeam, model: GameViewModel) {
        self.team = team
        self.model = model
    }

    public func makeMove(at position: Int) async throws -> GameMove {
        let move = GameMove(
            playerID: id,
            position: position,
            team: team,
            teamCharacterID: team.characterID(for: movesMade))
        await model.userMadeMove(move: move)

        movesMade += 1 
        return move
    }

    public func opponentMoved(_ move: GameMove) async throws {
        do {
            try await model.markOpponentMove(move)
        } catch {
            log("player", "Opponent made illegal move! \(move)")
        }
    }

}
```

### actor BotPlayer — [5:39]

```swift
public actor BotPlayer: Identifiable {
    nonisolated public let id: ActorIdentity = .random

    var ai: RandomPlayerBotAI
    var gameState: GameState

    public init(team: CharacterTeam) {
        self.gameState = .init()
        self.ai = RandomPlayerBotAI(playerID: self.id, team: team)
    }

    public func makeMove() throws -> GameMove {
        return try ai.decideNextMove(given: &gameState)
    }

    public func opponentMoved(_ move: GameMove) async throws {
        try gameState.mark(move)
    }
}
```

### distributed actor BotPlayer — [6:11]

```swift
import Distributed 

public distributed actor BotPlayer: Identifiable {
    typealias ActorSystem = LocalTestingDistributedActorSystem

    var ai: RandomPlayerBotAI
    var gameState: GameState

    public init(team: CharacterTeam, actorSystem: ActorSystem) {
        self.actorSystem = actorSystem // first, initialize the implicitly synthesized actor system property
        self.gameState = .init()
        self.ai = RandomPlayerBotAI(playerID: self.id, team: team) // use the synthesized `id` property
    }

    public distributed func makeMove() throws -> GameMove {
        return try ai.decideNextMove(given: &gameState)
    }

    public distributed func opponentMoved(_ move: GameMove) async throws {
        try gameState.mark(move)
    }
}
```

### Resolving a remote BotPlayer — [12:08]

```swift
let sampleSystem: SampleWebSocketActorSystem

let opponentID: BotPlayer.ID = .randomID(opponentFor: self.id)
let bot = try BotPlayer.resolve(id: opponentID, using: sampleSystem) // resolve potentially remote bot player
```

### Server-side actor system app — [13:35]

```swift
import Distributed
import TicTacFishShared

/// Stand alone server-side swift application, running our SampleWebSocketActorSystem in server mode.
@main
struct Boot {

    static func main() {
        let system = try! SampleWebSocketActorSystem(mode: .serverOnly(host: "localhost", port: 8888))

        system.registerOnDemandResolveHandler { id in
            // We create new BotPlayers "ad-hoc" as they are requested for.
            // Subsequent resolves are able to resolve the same instance.
            if system.isBotID(id) {
                return system.makeActorWithID(id) {
                    OnlineBotPlayer(team: .rodents, actorSystem: system)
                }
            }

            return nil // unable to create-on-demand for given id
        }

        print("========================================================")
        print("=== TicTacFish Server Running on: ws://\(system.host):\(system.port) ==")
        print("========================================================")

        try await server.terminated // waits effectively forever (until we shut down the system)
    }
}
```

### Receptionist listing — [20:02]

```swift
/// As we are playing for our `model.team` team, we try to find a player of the opposing team
let opponentTeam = model.team == .fish ? CharacterTeam.rodents : CharacterTeam.fish

/// The local network actor system provides a receptionist implementation that provides us an async sequence
/// of discovered actors (past and new)
let listing = await localNetworkSystem.receptionist.listing(of: OpponentPlayer.self, tag: opponentTeam.tag)
for try await opponent in listing where opponent.id != self.player.id {
    log("matchmaking", "Found opponent: \(opponent)")
    model.foundOpponent(opponent, myself: self.player, informOpponent: true)
    // inside foundOpponent:
    // if informOpponent {
    //     Task {
    //         try await opponent.startGameWith(opponent: myself, startTurn: false)
    //     }
    // }

    return // make sure to return here, we only need to discover a single opponent
}
```

### distributed actor LocalNetworkPlayer — [20:23]

```swift
public distributed actor LocalNetworkPlayer: GamePlayer {
    public typealias ActorSystem = SampleLocalNetworkActorSystem

    let team: CharacterTeam
    let model: GameViewModel

    var movesMade: Int = 0

    public init(team: CharacterTeam, model: GameViewModel, actorSystem: ActorSystem) {
        self.team = team
        self.model = model
        self.actorSystem = actorSystem
    }

    public distributed func makeMove() async -> GameMove {
        let field = await model.humanSelectedField()

        movesMade += 1
        let move = GameMove(
            playerID: self.id,
            position: field,
            team: team,
            teamCharacterID: movesMade % 2)

        return move
    }

    public distributed func makeMove(at position: Int) async -> GameMove {
        let move = GameMove(
            playerID: id,
            position: position,
            team: team,
            teamCharacterID: movesMade % 2)

        log("player", "Player makes move: \(move)")
        _ = await model.userMadeMove(move: move)

        movesMade += 1
        return move
    }

    public distributed func opponentMoved(_ move: GameMove) async throws {
        do {
            try await model.markOpponentMove(move)
        } catch {
            log("player", "Opponent made illegal move! \(move)")
        }
    }

    public distributed func startGameWith(opponent: OpponentPlayer, startTurn: Bool) async {
        log("local-network-player", "Start game with \(opponent.id), startTurn:\(startTurn)")
        await model.foundOpponent(opponent, myself: self, informOpponent: false)

        await model.waitForOpponentMove(shouldWaitForOpponentMove(myselfID: self.id, opponentID: opponent.id))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110356/6/AAC6A083-0D2D-4FFF-B60E-86EF01E37EE2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110356/6/AAC6A083-0D2D-4FFF-B60E-86EF01E37EE2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110356) — developer.apple.com. Indexed for agent consumption._
