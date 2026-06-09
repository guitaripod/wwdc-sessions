---
id: "wwdc2022-10065"
event: "wwdc2022"
year: 2022
title: "Plug-in and play: Add Apple frameworks to your Unity game projects"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10065"
topics: ["Accessibility & Inclusion", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Plug-in and play: Add Apple frameworks to your Unity game projects

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10065](https://developer.apple.com/videos/play/wwdc2022/10065)

Help make your Unity app or game an even better experience on Apple platforms. Learn how you can add Apple technologies directly to your projects with six plug-ins: Apple.Core, Game Center, Game Controller, Accessibility, Core Haptics, and PHASE. We'll show you how you can add new gameplay mechanics, make your games more accessible, and tap into the latest Apple features and services.

**Keywords:** `game center`, `game controller`, `game controllers`, `game dev`, `game developer`, `haptic`, `haptics`, `phase`, `plugin`, `plug-in`, `plugins`, `unity`, `unity plug-ins`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,698 words)

## Documentation & Resources

- [Apple Unity Plug-Ins on GitHub](https://github.com/apple/unityplugins) _download_
- [Delivering Rich App Experiences with Haptics](https://developer.apple.com/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics.json
- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json
- [PHASE](https://developer.apple.com/documentation/PHASE) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PHASE
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PHASE.json
- [Human Interface Guidelines: Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/game-center
- [Game Controller](https://developer.apple.com/documentation/GameController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GameController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GameController.json

## Code Snippets

### Game Center - Example game manager component - C# — [9:02]

```csharp
using Apple.GameKit;

public class GameManager : MonoBehaviour
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

### Game Center - Example game manager component continued - C# — [9:23]

```csharp
try
{
    _localPlayer = await GKLocalPlayer.Authenticate();

    if (_localPlayer.IsUnderage)
    {
        // Hide explicit game content.
    }

    if (_localPlayer.IsMultiplayerGamingRestricted)
    {
        // Disable multiplayer game features.
    }

    if (_localPlayer.IsPersonalizedCommunicationRestricted)
    {
        // Disable in-game communication UI.
    }
}
```

### Game Controller - Example input manager component - C# — [13:11]

```csharp
using Apple.GameController;

public class InputManager : MonoBehaviour
{
    void Start()
    {
        // Initialize the Game Controller service
        GCControllerService.Initialize();

        // Check for connected controllers
        var controllers = GCControllerService.GetConnectedControllers();
        foreach (GCController controller in controllers)
        {
            // Handle controllers
        }

        // Set up callbacks to handle connected/disconnected controllers
        GCControllerService.ControllerConnected    += _onControllerConnected;
        GCControllerService.ControllerDisconnected += _onControllerDisconnected;
    }
}
```

### Game Controller - polling and input handling - C# — [13:50]

```csharp
foreach (GCController controller in _myConnectedControllers)
{
    controller.Poll();

    // Check the 'South' button ('A' button on most controllers)
    if (controller.GetButton(GCControllerInputName.ButtonSouth))
    {
        //Handle button pressed
    }

    // Check other controller inputs…
}
```

### Core Haptics - Example haptics component - C# — [20:30]

```csharp
using Apple.CoreHaptics;

public class Haptics : MonoBehaviour
{
    private CHHapticEngine _hapticEngine;
    private CHHapticPatternPlayer _hapticPlayer;
    [SerializeField] private AHAPAsset _hapticAsset;

    private void PrepareHaptics()
    {
        _hapticEngine = new CHHapticEngine();
        _hapticEngine.Start();
        _hapticPlayer = _hapticEngine.MakePlayer(_hapticAsset.GetPattern());
    }

    private void Play()
    {
        _hapticPlayer.Start();
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10065/5/C221E77C-502C-47CD-B0C4-9091B529DD77/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10065/5/C221E77C-502C-47CD-B0C4-9091B529DD77/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10065) — developer.apple.com. Indexed for agent consumption._