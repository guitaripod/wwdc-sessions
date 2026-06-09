---
id: "wwdc2024-10068"
event: "wwdc2024"
year: 2024
title: "Bring your Live Activity to Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10068"
topics: ["App Services"]
platforms: ["iOS", "watchOS"]
hasTranscript: true
---

# Bring your Live Activity to Apple Watch

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10068](https://developer.apple.com/videos/play/wwdc2024/10068)

Bring Live Activities into the Smart Stack on Apple Watch with iOS 18 and watchOS 11. We’ll cover how Live Activities are presented on Apple Watch, as well as how you can enhance their presentation for the Smart Stack. We’ll also explore additional considerations to ensure Live Activities on Apple Watch always present up-to-date information.

**Keywords:** `activityattributes`, `activitykit`, `supplementalactivityfamilies`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,378 words)

## Documentation & Resources

- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/starting-and-updating-live-activities-with-activitykit-push-notifications.json
- [Displaying live data with Live Activities](https://developer.apple.com/documentation/ActivityKit/displaying-live-data-with-live-activities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ActivityKit/displaying-live-data-with-live-activities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ActivityKit/displaying-live-data-with-live-activities.json

## Code Snippets

### Existing Live Activity views — [1:28]

```swift
struct DeliveryLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(
            for: DeliveryActivityAttributes.self
        ) { context in
            DeliveryActivityContent(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    DeliveryExpandedLeadingView(context: context)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    DeliveryExpandedTrailingView(context: context)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    DeliveryExpandedBottomView(context: context)
                }
            } compactLeading: {
                DeliveryCompactLeading(context: context)
            } compactTrailing: {
                DeliveryCompactTrailing(context: context)
            } minimal: {
                DeliveryMinimal(context: context)
            }
        }
    }
}
```

### Preview Live Activities with Xcode Previews — [3:43]

```swift
extension DeliveryActivityAttributes.ContentState {
    static var shippedOrder: DeliveryActivityAttributes.ContentState {
        .init(
            status: .shipped,
            courierName: "Johnny"
        )
     }

     static var packedOrder: DeliveryActivityAttributes.ContentState {
         .init(
            status: .packed,
            courierName: "Contacting Courier...")
     }
}

#Preview(
    "Dynamic Island Compact",
    as: .dynamicIsland(.compact),
    using: DeliveryActivityAttributes.preview
) {
    DeliveryLiveActivity()
} contentStates: {
    DeliveryActivityAttributes.ContentState.packedOrder
    DeliveryActivityAttributes.ContentState.shippedOrder
}
```

### Add .supplementalActivityFamilies to indicate support for the Smart Stack — [4:15]

```swift
struct DeliveryLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(
            for: DeliveryActivityAttributes.self
        ) { context in
            DeliveryActivityContent(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                DynamicIslandExpandedRegion(.leading) {
                    DeliveryExpandedLeadingView(context: context)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    DeliveryExpandedTrailingView(context: context)
                }
                DynamicIslandExpandedRegion(.bottom) {
                    DeliveryExpandedBottomView(context: context)
                }
            } compactLeading: {
                DeliveryCompactLeading(context: context)
            } compactTrailing: {
                DeliveryCompactTrailing(context: context)
            } minimal: {
                DeliveryMinimal(context: context)
            }
        }
        .supplementalActivityFamilies([.small])
    }
}
```

### Customize view layout for the small activity family — [4:49]

```swift
struct DeliveryActivityContent: View {
    @Environment(\.activityFamily) var activityFamily
    var context: ActivityViewContext<DeliveryActivityAttributes>

    var body: some View {
        switch activityFamily {
        case .small:
            DeliverySmallContent(context: context)
        case .medium:
            DeliveryMediumContent(context: context)
        @unknown default:
            DeliveryMediumContent(context: context)
        }
    }
}
```

### Preview customized layouts for the Smart Stack — [5:06]

```swift
#Preview("Content", as: .content, using: DeliveryActivityAttributes.preview) {
   DeliveryLiveActivity()
} contentStates: {
    DeliveryActivityAttributes.ContentState.packedOrder
    DeliveryActivityAttributes.ContentState.shippedOrder
}
```

### Use isLuminanceReduced to remove bright elements with Always On Display — [8:37]

```swift
struct DeliveryGauge: View {
    @Environment(\.isLuminanceReduced) private var isLuminanceReduced
    var context: ActivityViewContext<DeliveryActivityAttributes>

    var body: some View {
        Gauge(value: context.state.progressPercent) {
            GaugeLabel(context: context)
        }
        .tint(isLuminanceReduced ? .gaugeDim : .gauge)
    }
}
```

### For Live Activities with a light appearance, use a light preferredColorScheme — [8:57]

```swift
struct DeliveryActivityContent: View {
    @Environment(\.activityFamily) var activityFamily
    var context: ActivityViewContext<DeliveryActivityAttributes>

    var body: some View {
        switch activityFamily {
        case .small:
            DeliverySmallContent(context: context)
                .preferredColorScheme(.light)
        case .medium:
            DeliveryMediumContent(context: context)
        @unknown default:
            DeliveryMediumContent(context: context)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10068/4/C621DA91-3F64-481C-8D10-25A5C5FCD587/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10068/4/C621DA91-3F64-481C-8D10-25A5C5FCD587/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10068) — developer.apple.com. Indexed for agent consumption._