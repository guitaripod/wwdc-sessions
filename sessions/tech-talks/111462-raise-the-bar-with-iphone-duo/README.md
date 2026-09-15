---
id: "tech-talks-111462"
event: "tech-talks"
year: 2026
title: "Raise the bar with iPhone Duo"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/111462"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["iOS"]
hasTranscript: true
---

# Raise the bar with iPhone Duo

**Event:** Tech Talks · **Topic:** Design · **Platforms:** iOS · **Published:** 2026-09-09 · **Session:** [tech-talks-111462](https://developer.apple.com/videos/play/tech-talks/111462)

Discover how to adapt your navigation, toolbars, and tab bars for the unique displays of iPhone Duo. Explore the design principles behind the new bar layout, and learn how to configure custom view representations and manage overflow to build powerful, responsive apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,393 words)

## Code Snippets

### Use system containers for vertical bar in SwiftUI — [2:24]

```swift
var body: some View {
    NavigationStack {
        ContentView()
            .toolbar {
                ToolbarItem(placement: .bottomBar) {
                    ...
                }
            }
    }
}
```

### Use navigation containers for vertical bar in UIKit — [2:39]

```swift
// Content from a custom bars (UINavigationBar, UITabBar, UIToolbar)
// won't be considered. Prefer UINavigationController 
// and UITabBarController, which manage their own bars.
let toolbar = UIToolbar()
toolbar.items = [...]
```

### Place a back or close button — [5:00]

```swift
// SwiftUI
.toolbar {
    ToolbarItem(placement: .cancellationAction) {
        ...
    }
}

// UIKit
navigationItem.leftItemsSupplementBackButton = false
navigationItem.leadingItemGroups
    = [UIBarButtonItemGroup(...)]
```

### Place prominent actions — [5:24]

```swift
// SwiftUI
.toolbar {
    ToolbarItem(placement: .topBarPinnedTrailing) {
        ...
    }
}

// UIKit
navigationItem.pinnedTrailingGroup
    = UIBarButtonItemGroup(...)
```

### Set a preferred axis for a custom view — [8:08]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarItem {
                ProfileView()
            }
            .axisBehavior(.verticalPreferred)
        }
}

// UIKit
let item = UIBarButtonItem(customView: ProfileView())
item.axisBehavior = .verticalPreferred
```

### Keep an item in the horizontal bar — [8:36]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarItem {
                SelectOrDoneButton()
            }
            .axisBehavior(.horizontalOnly)
        }
}

// UIKit
item.axisBehavior = .horizontalOnly
```

### Allow a custom view go in vertical bar — [8:52]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarItem {
                CompassView()
            }
            .axisBehavior(.verticalPreferred)
        }
}

// UIKit
let item = UIBarButtonItem(customView: CompassView())
item.axisBehavior = .verticalPreferred
```

### Use badges — [9:27]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarItem(...) {
                InboxButton()
                    .badge(7)
            }
        }
}

// UIKit
let item = UIBarButtonItem(...)
item.badge = .count(7)
```

### Read the vertical bar edge — [10:36]

```swift
// SwiftUI
struct ContentView: View {
    @Environment(\.toolbarVerticalEdge) var edge

    var body: some View {
        switch edge {
            ...
        }
    }
}

// UIKit
switch traitCollection.verticalBarEdge {
    ...
}
```

### Configure toolbar compression behavior — [12:23]

```swift
// SwiftUI
var body: some View {
    TabView {
        Tab("Recents", systemImage: "clock") {
            ContentView()
                .toolbarVerticalCompressionBehavior(.prefersToolbarItems)
        }
    }
}

// UIKit
navigationItem.verticalBarCompressionBehavior = .prefersBarItems
```

### Use system overflow menu — [12:43]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarOverflowMenu {
                Button("Scan") { ... }
                Button("Connect") { ... }
            }
        }
}

// UIKit
navigationItem.additionalOverflowItems = UIDeferredMenuElement({ provider in
    provider(self.persistentOverflowItems())
})
```

### Set item visibility priority — [13:21]

```swift
// SwiftUI
var body: some View {
    ContentView()
        .toolbar {
            ToolbarItem {
                Button(...) { ... }
            }
            .visibilityPriority(.high)
        }
}

// UIKit
let item = UIBarButtonItem(...)
item.visibilityPriority = .high
```

### Disable the vertical bar — [14:47]

```swift
// SwiftUI
var body: some View {
    NavigationStack {
        ContentView()
            .toolbarVerticalBehavior(.disabled)
    }
}

// UIKit
class MyViewController: UIViewController {
    override var preferredVerticalBarBehavior: UIVerticalBarBehavior {
        .disabled
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/111462/1/9a60db88-d15d-4892-8b56-18e11523d8e4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/111462/1/9a60db88-d15d-4892-8b56-18e11523d8e4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/111462) — developer.apple.com. Indexed for agent consumption._
