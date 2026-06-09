---
id: "wwdc2023-10229"
event: "wwdc2023"
year: 2023
title: "Make features discoverable with TipKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10229"
topics: ["Design", "Essentials", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Make features discoverable with TipKit

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10229](https://developer.apple.com/videos/play/wwdc2023/10229)

Teach people how to use your app with TipKit! Learn how you can create effective educational moments through tips. We’ll share how you can build eligibility rules to reach the ideal audience, control tip frequency, and strategies for testing to ensure successful interactions.

**Keywords:** `coaching`, `discover`, `discovery`, `education`, `feature`, `features`, `hint`, `hints`, `in-app`, `instructional`, `teach`, `teaching`, `tip`, `tipkit`, `tips`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,351 words)

## Code Snippets

### Create a tip — [1:55]

```swift
struct FavoriteBackyardTip: Tip {

    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text {
        Text("Your favorite backyards always appear at the top of the list.")
    }
}
```

### Configure TipsCenter — [2:48]

```swift
@main
struct BackyardBirdsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }

    // ...

    init() {
        TipsCenter.shared.configure()
    }
}
```

### Add actions and an asset to a tip — [3:18]

```swift
struct FavoriteBackyardTip: Tip {

    var title: Text {
        Text("Save as a Favorite").foregroundColor(.indigo)
    }

    var message: Text {
        Text("Your favorite backyards always appear at the top of the list.")
    }

    var asset: Image {
        Image(systemName: "star")
    }

    var actions: [Action] {
        [
            Tip.Action(
                id: "learn-more", 
                title: "Learn More"
            )
        ]
    }
}
```

### Create a popover view — [4:53]

```swift
private let favoriteBackyardTip = FavoriteBackyardTip()

// ...

.toolbar {
    ToolbarItem {
        Button {
            backyard.isFavorite.toggle()
        } label: {
            Label("Favorite", systemImage: "star")
                .symbolVariant(
                    backyard.isFavorite ? .fill : .none
                )
        }
        .popoverMiniTip(tip: favoriteBackyardTip)
    }
}
```

### Add a parameter based rule — [6:38]

```swift
struct FavoriteBackyardTip: Tip {

    @Parameter
    static var isLoggedIn: Bool = false

    // ...

    var rules: Predicate<RuleInput...> {

        // User is logged in
        #Rule(Self.$isLoggedIn) { $0 == true }
    }
}
```

### Add an event based rule — [7:16]

```swift
struct FavoriteBackyardTip: Tip {

    @Parameter
    static var isLoggedIn: Bool = false

    static let enteredBackyardDetailView: Event = Event<DetailViewDonation>(
        id: "entered-backyard-detail-view"
    )

    // ...

    var rules: Predicate<RuleInput...> {
        // User is logged in
        #Rule(Self.$isLoggedIn) { $0 == true }

        // User has entered any backyard detail view at least 3 times
        #Rule(Self.enteredBackyardDetailView) { $0.count >= 3 }
    }
}
```

### Donate the event when a view appears — [7:34]

```swift
.onAppear {
     FavoriteBackyardTip.enteredBackyardDetailView.donate()
}
```

### Filter event donations in an event based rule — [7:59]

```swift
// User has entered any backyard detail view at least 3 times in the past 5 days
#Rule(Self.enteredBackyardDetailView) { 
    $0.donations.filter { 
        $0.date > Date.now.addingTimeInterval(-5 * 60 * 60 * 24)
    }
    .count >= 3
}
```

### Create a custom donation — [8:34]

```swift
// Create the associated type
extension BackyardDetailTip {
    struct DetailViewDonation: DonationValue {
        let backyardID: Int
    }
}

// Donate the unique id of the backyard detail being viewed
.onAppear {
     BackyardFavoriteTip.enteredBackyardDetailView.donate(
         with: .init(backyardID: backyard.id)
     )
}


struct FavoriteBackyardTip: Tip {

    // ...

    var rules: Predicate<RuleInput...> {
        // Update the rule to specify a backyardID
        #Rule(Self.enteredBackyardDetailView) {
            $0.donations.filter {
                $0.date > Date.now.addingTimeInterval(-5 * 60 * 60 * 24) 
            }
            .largestSubset(by: \.backyardID)
            .count >= 3
        }
    }
}
```

### Configure display frequency — [9:57]

```swift
// One tip per day.
TipsCenter.shared.configure {
    DisplayFrequency(.daily)
}

// One tip per hour.
TipsCenter.shared.configure {
    DisplayFrequency(.hourly)
}

// Custom configuration. Only show one tip every five days.
let fiveDays: TimeInterval = 5 * 24 * 60 * 60
TipsCenter.shared.configure {
    DisplayFrequency(fiveDays)
}

// No frequency control. Show all tips as soon as eligible.
TipsCenter.shared.configure {
    DisplayFrequency(.immediate)
}
```

### Turn off display frequency controls for a tip — [10:34]

```swift
struct FavoriteBackyardTip: Tip {

    // ...

    var options: [Option] {
        [.ignoresDisplayFrequency(true)]
    }
}
```

### Invalidate a tip — [11:27]

```swift
Button {
    backyard.isFavorite.toggle()

    // When user taps the favorite button, dismiss the tip
    favoriteBackyardTip.invalidate(reason: .userPerformedAction)
} label: {
    Label("Favorite", systemImage: "star")
        .symbolVariant(backyard.isFavorite ? .fill : .none)
}
.popoverMiniTip(tip: favoriteBackyardTip)
```

### Configure max display count on a tip — [11:41]

```swift
struct FavoriteBackyardTip: Tip {

    // ...

    var options: [Option] {
        [.maxDisplayCount(5)]
    }
}
```

### Programmatically call testing API — [12:46]

```swift
// Show all defined tips in the app
TipsCenter.showAllTips()

// Show some tips, but not all
TipsCenter.showTips([tip1, tip2, tip3])

// Hide some tips, but not all
TipsCenter.hideTips([tip1, tip2, tip3])

// Hide all tips defined in the app
TipsCenter.hideAllTips()

// Purge all TipKit related data
TipsCenter.resetDatastore()
```

### Configure launch arguments in your scheme — [13:31]

```swift
// Show all defined tips in the app
com.apple.TipKit.ShowAllTips 1

// Show some tips, but not all
com.apple.TipKit.ShowTips tipID,otherTipID

// Hide some tips, but not all
com.apple.TipKit.HideAllTips 1

// Hide all tips defined in the app
com.apple.TipKit.HideTips tipID,otherTipID

// Purge all TipKit related data
com.apple.TipKit.ResetDatastore 1
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10229/4/07E6CA29-01CD-4E03-A3FF-D7D8A3FB4CEF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10229/4/07E6CA29-01CD-4E03-A3FF-D7D8A3FB4CEF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10229) — developer.apple.com. Indexed for agent consumption._
