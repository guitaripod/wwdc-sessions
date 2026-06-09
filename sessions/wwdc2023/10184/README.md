---
id: "wwdc2023-10184"
event: "wwdc2023"
year: 2023
title: "Meet ActivityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10184"
topics: ["Essentials", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet ActivityKit

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10184](https://developer.apple.com/videos/play/wwdc2023/10184)

Live Activities are a glanceable way for someone to keep track of the progress of a task within your app. We’ll teach you how you can create helpful experiences for the Lock Screen, the Dynamic Island, and StandBy. Learn how to update your app’s Live Activities, monitor activity state, and take advantage of WidgetKit and SwiftUI to build richer experiences.

**Keywords:** `activities`, `activity`, `activitykit`, `dynamic`, `dynamic island`, `island`, `live`, `live activities`, `live notification`, `live notifications`, `lock`, `lock screen`, `notification`, `notifications`, `screen`, `standby`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,166 words)

## Documentation & Resources

- [Human Interface Guidelines: Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/live-activities
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json
- [Displaying live data with Live Activities](https://developer.apple.com/documentation/ActivityKit/displaying-live-data-with-live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/displaying-live-data-with-live-activities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/displaying-live-data-with-live-activities.json
- [ActivityKit](https://developer.apple.com/documentation/ActivityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit.json
- [WidgetKit](https://developer.apple.com/documentation/WidgetKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit.json

## Code Snippets

### Define ActivityAttributes — [5:40]

```swift
import ActivityKit

struct AdventureAttributes: ActivityAttributes {
    let hero: EmojiRanger

    struct ContentState: Codable & Hashable {
        let currentHealthLevel: Double
        let eventDescription: String
    }
}
```

### Request Live Activity with initial content state — [6:28]

```swift
let adventure = AdventureAttributes(hero: hero)

let initialState = AdventureAttributes.ContentState(
    currentHealthLevel: hero.healthLevel,
    eventDescription: "Adventure has begun!"
)
let content = ActivityContent(state: initialState, staleDate: nil, relevanceScore: 0.0)

let activity = try Activity.request(
    attributes: adventure,
    content: content,
    pushType: nil
)
```

### Update Live Activity with new content — [8:00]

```swift
let heroName = activity.attributes.hero.name               
let contentState = AdventureAttributes.ContentState(
    currentHealthLevel: hero.healthLevel,
    eventDescription: "\(heroName) has taken a critical hit!"
)

var alertConfig = AlertConfiguration(
    title: "\(heroName) has taken a critical hit!",
    body: "Open the app and use a potion to heal \(heroName)",
    sound: .default
)  

activity.update(
    ActivityContent<AdventureAttributes.ContentState>(
        state: contentState,
        staleDate: nil
    ),
    alertConfiguration: alertConfig
)
```

### Observe activity state — [9:30]

```swift
// Observe activity state asynchronously
func observeActivity(activity: Activity<AdventureAttributes>) {
    Task {
        for await activityState in activity.activityStateUpdates {
            if activityState == .dismissed {
                self.cleanUpDismissedActivity()
            }
        }
    }
}

// Observe activity state synchronously
let activityState = activity.activityState
if activityState == .dismissed {
    self.cleanUpDismissedActivity()
}
```

### Dismiss Live Activity with final content state — [10:03]

```swift
let hero = activity.attributes.hero

let finalContent = AdventureAttributes.ContentState(
    currentHealthLevel: hero.healthLevel,
    eventDescription: "Adventure over! \(hero.name) has defeated the boss! Congrats!"
)

let dismissalPolicy: ActivityUIDismissalPolicy = .default

activity.end(
    ActivityContent(state: finalContent, staleDate: nil),
    dismissalPolicy: dismissalPolicy)
}
```

### Add ActivityConfiguration to WidgetBundle — [10:50]

```swift
import WidgetKit
import SwiftUI

@main
struct EmojiRangersWidgetBundle: WidgetBundle {
    var body: some Widget {
        EmojiRangerWidget()
        LeaderboardWidget()
        AdventureActivityConfiguration()
    }
}
```

### Define Lock Screen presentation — [11:05]

```swift
struct AdventureActivityConfiguration: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: AdventureAttributes.self) { context in
            AdventureLiveActivityView(
                hero: context.attributes.hero,
                isStale: context.isStale,
                contentState: context.state
            )
            .activityBackgroundTint(Color.navyBlue)
        } dynamicIsland: { context in
            // ...
        }
    }
}
```

### Define Dynamic Island compact presentation — [13:28]

```swift
struct AdventureActivityConfiguration: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: AdventureAttributes.self) { context in
            // ...
        } dynamicIsland: { context in
            DynamicIsland {
                // ...
            } compactLeading: {
                Avatar(hero: context.attributes.hero)
            } compactTrailing: {
                ProgressView(value: context.state.currentHealthLevel) {
                    Text("\(Int(context.state.currentHealthLevel * 100))")
                }
                .progressViewStyle(.circular)
                .tint(context.state.currentHealthLevel <= 0.2 ? Color.red : Color.green)
            } minimal: {
                // ...
            }
        }
    }
}
```

### Define Dynamic Island minimal presentation — [14:42]

```swift
struct AdventureActivityConfiguration: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: AdventureAttributes.self) { context in
            // ...
        } dynamicIsland: { context in
            DynamicIsland {
                // ...
            } compactLeading: {
                // ...
            } compactTrailing: {
                // ...
            } minimal: {
                ProgressView(value: context.state.currentHealthLevel) {
                    Avatar(hero: context.attributes.hero)
                }
                .progressViewStyle(.circular)
                .tint(context.state.currentHealthLevel <= 0.2 ? Color.red : Color.green)
            }
        }
    }
}
```

### Define Dynamic Island expanded presentation — [15:26]

```swift
struct AdventureActivityConfiguration: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: AdventureAttributes.self) { context in
            // ...
        } dynamicIsland: { context in
            DynamicIsland {
                // Leading region
                DynamicIslandExpandedRegion(.leading) {
                    LiveActivityAvatarView(hero: hero)
                }

                // Expanded region
                DynamicIslandExpandedRegion(.trailing) {
                    StatsView(hero: hero, isStale: isStale)
                }

                // Bottom region
                DynamicIslandExpandedRegion(.bottom) {
                    HealthBar(currentHealthLevel: contentState.currentHealthLevel)
                    EventDescriptionView(hero: hero, contentState: contentState)
                }
            } compactLeading: {
                // ...
            } compactTrailing: {
                // ...
            } minimal: {
                // ...
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10184/4/A7390924-2731-4B9B-925E-1CBDFB186C3E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10184/4/A7390924-2731-4B9B-925E-1CBDFB186C3E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10184) — developer.apple.com. Indexed for agent consumption._