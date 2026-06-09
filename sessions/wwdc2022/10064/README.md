---
id: "wwdc2022-10064"
event: "wwdc2022"
year: 2022
title: "Reach new players with Game Center dashboard"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10064"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Reach new players with Game Center dashboard

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10064](https://developer.apple.com/videos/play/wwdc2022/10064)

Meet the Game Center activity dashboard and discover how it can help your game reach new players. We'll introduce you to the dashboard and profiles and explore how they can track player achievements, high scores, and leaderboard changes for your game. We'll also show you how to add Game Center to your Unity game project using the Game Center plug-in.

**Keywords:** `game center`, `game dev`, `game developer`, `gamekit`, `game kit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,488 words)

## Documentation & Resources

- [GKLocalPlayer](https://developer.apple.com/documentation/GameKit/GKLocalPlayer) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameKit/GKLocalPlayer
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameKit/GKLocalPlayer.json
- [Human Interface Guidelines: Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-center

## Code Snippets

### Authenticate the local player — [4:11]

```swift
// Authenticate the local player
import GameKit

class TitleScreenViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Authenticate the local player
        GKLocalPlayer.local.authenticateHandler = { viewController, error in
            if let viewController = viewController {
                // Present the view controller from Game Center.
                return
            }
        }
    }
}
```

### Authenticate the local player — [4:30]

```csharp
// Authenticate the local player
using Apple.GameKit;

public class MyGameManager : MonoBehaviour
{
    private GKLocalPlayer _localPlayer;

    private async Task Start()
    {
        try
        {
            _localPlayer = await GKLocalPlayer.Authenticate();
        }
        catch (Exception exception)
        {
            // Handle exception...
        }
    }
}
```

### Show the Access Point — [5:25]

```swift
// Show the Access Point
import GameKit

class MenuScreenViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        GKAccessPoint.shared.location = .topLeading
        GKAccessPoint.shared.isActive = true
    }
}
```

### Show the Access Point — [5:40]

```csharp
// Show the Access Point
GKAccessPoint.Shared.Location = 
    GKAcessPoint.GKAccessPointLocation.TopLeading;

GKAccessPoint.Shared.IsActive = true;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10064/9/B7DD74D7-2555-495C-9DA2-8A9B7D0C6D8B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10064/9/B7DD74D7-2555-495C-9DA2-8A9B7D0C6D8B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10064) — developer.apple.com. Indexed for agent consumption._