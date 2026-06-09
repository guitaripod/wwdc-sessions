---
id: "wwdc2026-223"
event: "wwdc2026"
year: 2026
title: "Live Activities essentials"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/223"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Live Activities essentials

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-223](https://developer.apple.com/videos/play/wwdc2026/223)

Elevate your app experience with Live Activities. Explore many of the places where Live Activities appear, including a new style in the Dynamic Island that delivers more information when iPhone is used in landscape. Learn how to tailor your Live Activity for each space, structure your content and data, and drive real time updates from start to finish using ActivityKit and push notifications.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,205 words)

## Documentation & Resources

- [Human Interface Guidelines: Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/live-activities
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json
- [ActivityKit](https://developer.apple.com/documentation/ActivityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit.json

## Code Snippets

### Define initial Live Activity — [4:16]

```swift
// Define initial Live Activity.

import ActivityKit
import Foundation

public struct DrinkOrderAttributes: ActivityAttributes {
    let shopName: String
    let drink: Drink
    let orderID: UUID

    public struct ContentState: Codable, Hashable {
        var phase: DrinkOrder.Phase = .waiting
        var estimatedReadyDate: Date
        var rating: DrinkOrder.Rating?
    }
}
```

### Create each Live Activity view — [5:35]

```swift
// Create each Live Activity view

import ActivityKit
import SwiftUI
import WidgetKit

struct DrinkOrderLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: DrinkOrderAttributes.self) { context in
            ActivityView(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    ExpandedLeadingView(context: context)
                }
                DynamicIslandExpandedRegion(.center) {
                    ExpandedCenterView(context: context)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    ExpandedTrailingView(context: context)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    ExpandedBottomView(context: context)
                }
            } compactLeading: {
                CompactLeadingView(context: context)
            } compactTrailing: {
                CompactTrailingView(context: context)
            } minimal: {
                MinimalView(context: context)
            }
        }
    }
}
```

### Start and update a Live Activity — [7:43]

```swift
// Start a Live Activity

func launchLiveActivity(order: DrinkOrder) throws {
    guard ActivityAuthorizationInfo().areActivitiesEnabled else { return }
    let attributes = DrinkOrderAttributes(shopName: "Coffee Shop", drink: order.drink, orderID: order.id)
    let estimatedReadyDate = Date.now + (15 * 60)
    let contentState = DrinkOrderAttributes.ContentState(phase: .waiting, estimatedReadyDate: estimatedReadyDate)
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    let activity = try Activity.request(attributes: attributes, content: activityContent)

}

// Update a Live Activity

await activity.update(
    ActivityContent(
        state: DrinkOrderAttributes.ContentState(
            phase: .preparing,
            estimatedReadyDate: estimatedReadyDate
        ),
        staleDate: nil
    )
)
```

### Optimize for limited width in the Dynamic Island — [10:33]

```swift
// Optimize for limited width in the Dynamic Island

struct CompactTrailingView: View {
    @Environment(\.isDynamicIslandLimitedInWidth) var isDynamicIslandLimitedInWidth
    var context: ActivityViewContext<DrinkOrderAttributes>
    var body: some View {
        if isDynamicIslandLimitedInWidth {
            StepProgressIconView(context: context)
        } else if context.state.phase.showsTimer {
            EstimatedReadyView(context: context, font: .system(.body).monospacedDigit())
                .multilineTextAlignment(.trailing)
                .frame(maxWidth: maximumTimerLabelWidth)
        } else {
            OrderPhaseLabelView(context: context, font: .caption2.bold(), color: .brown)
                .multilineTextAlignment(.trailing)
        }
    }
}
```

### Extend background color in StandBy — [11:34]

```swift
// Extend background color in StandBy

struct ActivityView: View {

    @Environment(\.showsWidgetContainerBackground) var showsWidgetContainerBackground
    var context: ActivityViewContext<DrinkOrderAttributes>

    var body: some View {
        DetailView(context: context)
            .background {
                if showsWidgetContainerBackground {
                    LinearGradient.barista
                }
            }
            .activityBackgroundTint(.espresso)
    }
}
```

### Add support for activityFamily small — [12:30]

```swift
// Add support for activityFamily small

import ActivityKit
import SwiftUI
import WidgetKit

struct DrinkOrderLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: DrinkOrderAttributes.self) { context in
            ActivityView(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    ExpandedLeadingView(context: context)
                }
                DynamicIslandExpandedRegion(.center) {
                    ExpandedCenterView(context: context)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    ExpandedTrailingView(context: context)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    ExpandedBottomView(context: context)
                }
            } compactLeading: {
                CompactLeadingView(context: context)
            } compactTrailing: {
                CompactTrailingView(context: context)
            } minimal: {
                MinimalView(context: context)
            }
        }
        .supplementalActivityFamilies([.small])
    }
}
```

### Optimize for small family — [12:43]

```swift
// Optimize for small family

struct ActivityView: View {
    @Environment(\.showsWidgetContainerBackground) var showsWidgetContainerBackground
    @Environment(\.activityFamily) var activityFamily

    var context: ActivityViewContext<DrinkOrderAttributes>

    var body: some View {
        contentView
            .background {
                if showsWidgetContainerBackground {
                    LinearGradient.barista
                }
            }
            .activityBackgroundTint(.espresso)
    }

    @ViewBuilder
    var contentView: some View {
        if activityFamily == .small {
            SmallView(context: context)
        } else {
            DetailView(context: context)
        }
    }
}
```

### Add interactivity with App Intents — [13:36]

```swift
// Add interactivity with App Intents

struct RateDrinkIntent: LiveActivityIntent {
    static var title: LocalizedStringResource = "Rate Drink"

    @Parameter(title: "Order ID")
    var orderID: String

    @Parameter(title: "Positive")
    var isPositive: Bool

    func perform() async throws -> some IntentResult {
        await updateLocalDatastore(rating: isPositive ? .great : .poor, dismissPolicy: .after(.now + 15))
        return .result()
    }
}
```

### Associate an intent with a button — [14:06]

```swift
// Associate an intent with a button

struct RatingButtons: View {
    var context: ActivityViewContext<DrinkOrderAttributes>
    var body: some View {
        HStack(spacing: 12) {
            Button(intent: RateDrinkIntent(
                orderID: context.attributes.orderID.uuidString, isPositive: false)) {
                Label("Not Good", systemImage: "hand.thumbsdown.fill")
            }
            .buttonStyle(RatingButtonStyle(color: .red))

            Button(intent: RateDrinkIntent(
                orderID: context.attributes.orderID.uuidString, isPositive: true)) {
                Label("Great", systemImage: "hand.thumbsup.fill")
            }
            .buttonStyle(RatingButtonStyle(color: .green))
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/223/4/9098c495-ea8b-44f9-b852-f6eb64840161/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/223/4/9098c495-ea8b-44f9-b852-f6eb64840161/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/223) — developer.apple.com. Indexed for agent consumption._