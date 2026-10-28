---
id: "tech-talks-111467"
event: "tech-talks"
year: 2026
title: "Bring Live Activities to Mac"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111467"
topics: ["SwiftUI & UI Frameworks", "System Services"]
platforms: ["macOS"]
hasTranscript: true
---

# Bring Live Activities to Mac

**Event:** Tech Talks · **Topic:** System Services · **Platforms:** macOS · **Published:** 2026-10-28 · **Session:** [tech-talks-111467](https://developer.apple.com/videos/play/tech-talks/111467)

Discover how to drive Live Activities from your Mac app. Explore how Live Activities appear in the menu bar and Dynamic Island. Learn how to define your data model, create compact and expanded views with SwiftUI, and drive interactive updates using App Intents.

**Keywords:** `dynamic island`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,327 words)

## Documentation & Resources

- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json
- [Displaying live data with Live Activities](https://developer.apple.com/documentation/ActivityKit/displaying-live-data-with-live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/displaying-live-data-with-live-activities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/displaying-live-data-with-live-activities.json

## Code Snippets

### Define the Live Activity data model — [2:36]

```swift
import ActivityKit

struct CurtainActivityAttributes: ActivityAttributes {
    let scenesPerAct: [Int]
    let showTitle: String

    struct ContentState: Codable, Hashable {
        var isPlaying: Bool
        var curtainOpen: Bool
        var actIndex: Int
        var sceneIndexInAct: Int
    }
}
```

### Configure compact, minimal, and expanded views — [3:20]

```swift
import SwiftUI
import WidgetKit

struct CurtainActivityWidget: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(
            for: CurtainActivityAttributes.self
        ) { context in
            CurtainActivityMenuBarExpandedContent(
                state: context.state,
                showTitle: context.attributes.showTitle)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    CurtainLabel(state: context.state)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    ActLabel(state: context.state)
                }
                DynamicIslandExpandedRegion(.center) {
                    SceneLabel(state: context.state)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    ExpandedBottom(state: context.state)
                }
            } compactLeading: {
                StatusGlyph(state: context.state)
            } compactTrailing: {
                CompactTrailing(state: context.state)
            } minimal: {
                StatusGlyph(state: context.state)
            }
        }
    }
}
```

### Update a running Live Activity — [5:23]

```swift
contentState.curtainOpen = false
let content = ActivityContent(
    state: self.currentContentState, staleDate: nil
)
await activity.update(
    content, alertConfiguration: alertConfiguration
)
```

### Define an App Intent action — [6:02]

```swift
struct SetPlacesReadyIntent: AppIntent {
    // ...
    func perform() async throws -> some IntentResult {
        // ...
        var state = activity.content.state
        state.placesReady = self.ready
        let content = ActivityContent(state: state, staleDate: nil)
        await activity.update(
            content,
            alertConfiguration: .announcement(self.ready ? "Ready" : "Not Ready")
        )
        return .result()
    }
}
```

### Trigger the intent from buttons — [6:16]

```swift
private struct PlacesReadyButtons: View {
    var body: some View {
        HStack {
            Button(intent: SetPlacesReadyIntent(ready: false)) {
                Text("Not Ready")
            }
            .tint(.red)
            Button(intent: SetPlacesReadyIntent(ready: true)) {
                Text("Ready")
            }
            .tint(.green)
        }
    }
}
```

### End a Live Activity — [6:32]

```swift
// End a Live Activity
await activity.end(nil, dismissalPolicy: .immediate)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111467/1/29eb0348-372b-4b4b-8b26-1aef42d0456a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111467/1/29eb0348-372b-4b4b-8b26-1aef42d0456a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111467) — developer.apple.com. Indexed for agent consumption._
