---
id: "wwdc2024-10073"
event: "wwdc2024"
year: 2024
title: "Catch up on accessibility in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10073"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Catch up on accessibility in SwiftUI

**Event:** WWDC24 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10073](https://developer.apple.com/videos/play/wwdc2024/10073)

SwiftUI makes it easy to build amazing experiences that are accessible to everyone. We’ll discover how assistive technologies understand and navigate your app through the rich accessibility elements provided by SwiftUI. We’ll also discuss how you can further customize these experiences by providing more information about your app’s content and interactions by using accessibility modifiers. 

**Keywords:** `accessibilityactions`, `accessibilityelements`, `accessibilitylabel`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,875 words)

## Documentation & Resources

- [Forum: Accessibility & Inclusion](https://developer.apple.com/forums/topics/accessibility-and-inclusion?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/accessibility-and-inclusion?cid=vf-a-0010
- [Enhancing the accessibility of your SwiftUI app](https://developer.apple.com/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app.json
- [Performing accessibility testing for your app](https://developer.apple.com/documentation/Accessibility/performing-accessibility-testing-for-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/performing-accessibility-testing-for-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/performing-accessibility-testing-for-your-app.json
- [Accessibility updates](https://developer.apple.com/documentation/Updates/Accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Accessibility.json

## Code Snippets

### Accessibility Label Modifier & Opacity — [7:27]

```swift
struct UnreadIndicatorView: View {
    var isUnread: Bool

    var body: some View {
        Circle()
            .foregroundStyle(.blue)
            .accessibilityLabel("Unread")
            .opacity(isUnread ? 1 : 0)
    }
}
```

### Accessibility Element Children Combine Modifier — [8:02]

```swift
var body: some View {
    HStack {
        UnreadIndicatorView(isUnread: message.isUnread)
        MessageContentsView(message: message)
        Spacer()
        Button(action: favorite) { favoriteLabel }
        Button(action: reply) { replyLabel }
    }
    .accessibilityElement(children: .combine)
}
```

### Accessibility Conditional Modifiers — [10:37]

```swift
var body: some View {
    Button(action: favorite) {
        Image(systemName: isSuperFavorite ? "sparkles" : "star.fill")
    }
    .accessibilityLabel("Super Favorite", isEnabled: isSuperFavorite)
}
```

### Accessibility Actions Modifier — [13:38]

```swift
var body: some View {
    TripView(trip: trip)
        .onHover { showAttachments = $0 }
        .overlay {
            MessageAttachments(attachments: trip.attachments)
                .opacity(showAttachments ? 1 : 0)
        }
        .accessibilityActions {
             MessageAttachments(attachments: trip.attachments)
        }
}
```

### Accessibility Label Modifier — [15:16]

```swift
var body: some View {
  TripView(trip: trip)
      .accessibilityLabel { label in
         if let rating = trip.rating {
            Text(rating)
         }
         label
      }
}
```

### Accessibility Drop Point Modifier — [17:42]

```swift
var body: some View {
    CommentAlertView(contact: contact)
        .onDrop(of: [.audio], delegate: delegate)
        .accessibilityDropPoint(.leading, description: "Set Sound 1")
        .accessibilityDropPoint(.center, description: "Set Sound 2")
        .accessibilityDropPoint(.trailing, description: "Set Sound 3")
}
```

### Accessibility App Intent Action Modifier — [19:45]

```swift
var body: some View {
    ForEach(beaches) { beach in
        BeachView(beach)
            .accessibilityAction(
                named: "Favorite",
                intent: ToggleRatingIntent(beach: beach, rating: .fullStar))
            .accessibilityAction(
                .magicTap,
                intent: ComposeIntent(type: .photo))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10073/5/769C76D4-F43B-4E18-A6DB-1E3F3A4A8648/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10073/5/769C76D4-F43B-4E18-A6DB-1E3F3A4A8648/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10073) — developer.apple.com. Indexed for agent consumption._