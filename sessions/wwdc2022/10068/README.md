---
id: "wwdc2022-10068"
event: "wwdc2022"
year: 2022
title: "What's new in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10068"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in UIKit

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10068](https://developer.apple.com/videos/play/wwdc2022/10068)

Discover the latest updates and improvements to UIKit and learn how to build better iPadOS, iOS, and Mac Catalyst apps. We’ll take you through UI refinements, productivity updates, API enhancements, and more. We’ll also help you explore improvements to performance, security, and privacy.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,534 words)

## Documentation & Resources

- [UINavigationItem.ItemStyle](https://developer.apple.com/documentation/UIKit/UINavigationItem/ItemStyle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/ItemStyle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/ItemStyle.json
- [UIPageControl](https://developer.apple.com/documentation/UIKit/UIPageControl) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIPageControl
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIPageControl.json
- [UICalendarView](https://developer.apple.com/documentation/UIKit/UICalendarView) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UICalendarView
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UICalendarView.json
- [centerItemGroups](https://developer.apple.com/documentation/UIKit/UINavigationItem/centerItemGroups) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/centerItemGroups
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/centerItemGroups.json
- [Building a desktop-class iPad app](https://developer.apple.com/documentation/UIKit/building-a-desktop-class-ipad-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-a-desktop-class-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-a-desktop-class-ipad-app.json

## Code Snippets

### Configuring a UICalendarView with multi-date selection — [7:51]

```swift
// Configuring a calendar view with multi-date selection

let calendarView = UICalendarView()
calendarView.delegate = self
calendarView.calendar = Calendar(identifier: .gregorian)
view.addSubview(calendarView)

let multiDateSelection = UICalendarSelectionMultiDate(delegate: self)
multiDateSelection.selectedDates = myDatabase.selectedDates()
calendarView.selectionBehavior = multiDateSelection

func multiDateSelection(
    _ selection: UICalendarSelectionMultiDate,
    canSelectDate dateComponents: DateComponents
) -> Bool {
    return myDatabase.hasAvailabilities(for: dateComponents)
}
```

### Configure UICalendarView decorations. — [9:07]

```swift
// Configuring Decorations
func calendarView(
    _ calendarView: UICalendarView, 
    decorationFor dateComponents: DateComponents
) -> UICalendarView.Decoration? {
    switch myDatabase.eventType(on: dateComponents) {
    case .none:
        return nil
    case .busy:
        return .default()
    case .travel:
        return .image(airplaneImage, color: .systemOrange)
    case .party:
        return .customView {
            MyPartyEmojiLabel()
        }
    }
}
```

### Setting up a vertical UIPageControl with custom indicators — [10:16]

```swift
// Vertical page control with custom indicators

pageControl.direction = .topToBottom
pageControl.preferredIndicatorImage = UIImage(systemNamed: "square")
pageControl.preferredCurrentIndicatorImage = UIImage(systemNamed: "square.fill")
```

### Creating a custom sheet detent — [12:21]

```swift
// Create a custom detent
sheet.detents = [
    .large(),
    .custom { _ in
        200.0
    }
]
```

### Creating a custom sheet detent using a percentage of maximum detent height — [12:38]

```swift
// Create a custom detent
sheet.detents = [
    .large(),
    .custom { context in
        0.3 * context.maximumDetentValue
    }
]
```

### Assigning identifiers to custom sheet detents — [12:42]

```swift
// Define a custom identifier
extension UISheetPresentationController.Detent.Identifier {
    static let small = UISheetPresentationController.Detent.Identifier("small")
}

// Assign identifier to custom detent
sheet.detents = [
    .large(),
    .custom (identifier: .small) { context in
        0.3 * context.maximumDetentValue
    }
]

// Disable dimming above the custom detent
sheet.largestUndimmedDetentIdentifier = .small
```

### UIHostingConfiguration example — [22:16]

```swift
cell.contentConfiguration = UIHostingConfiguration {
    VStack {
        Image(systemName: "wand.and.stars")
            .font(.title)
        Text("Like magic!")
            .font(.title2).bold()
    }
    .foregroundStyle(Color.purple)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10068/4/CD436E87-CE6B-4E99-A7EA-66C5A424B38B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10068/4/CD436E87-CE6B-4E99-A7EA-66C5A424B38B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10068) — developer.apple.com. Indexed for agent consumption._