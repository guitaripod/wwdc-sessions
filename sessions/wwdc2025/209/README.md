---
id: "wwdc2025-209"
event: "wwdc2025"
year: 2025
title: "Level up your games"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/209"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Level up your games

**Event:** WWDC25 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-209](https://developer.apple.com/videos/play/wwdc2025/209)

Learn how to make your games shine on the unified gaming platform. We’ll give you a map of the technologies you can use to level up your game and further improve your player experience. Get an overview of the fundamental tools essential to build, debug, and profile your game. 

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,560 words)

## Documentation & Resources

- [Ray tracing with Intersection Function Buffer](https://developer.apple.com/metal/RaytracingWithIFB.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/RaytracingWithIFB.zip
- [Function constants and Framebuffer fetch](https://developer.apple.com/metal/FunctionConstantsAndFramebufferFetch.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/FunctionConstantsAndFramebufferFetch.zip
- [Human Interface Guidelines: Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-games

## Code Snippets

### React to Low Power Mode state — [0:01]

```swift
static let NSProcessInfoPowerStateDidChange: NSNotification.Name
var isLowPowerModeEnabled: Bool { get }
```

### GameSave code sample — [12:13]

```objectivec
// Objective-C GameSave code sample
#import <GameSave/GameSave.h>
NSString* containerIdentifier = ///… container entitlement string, nil specifies the first in the entitlement array

GSSyncedDirectory* directory = [GSSyncedDirectory openDirectoryForContainerIdentifier:containerIdentifier];

/// Where statusDisplay is an NSWindow or UIWindow where the alert will be anchored to
[directory finishSyncing:statusDisplay completionHandler:^{
 }];

GSSyncedDirectoryState* directoryState = [directory directoryState];
switch (directoryState.state) {
    case GSSyncStateError:
        error = directoryState.error;
        break;
    default:
        NSLog(@"Sync has finished");
}

NSURL* saveURL = directoryState.url;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/209/4/45dc1092-c205-4dc3-8e6c-fa075886dce8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/209/4/45dc1092-c205-4dc3-8e6c-fa075886dce8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/209) — developer.apple.com. Indexed for agent consumption._