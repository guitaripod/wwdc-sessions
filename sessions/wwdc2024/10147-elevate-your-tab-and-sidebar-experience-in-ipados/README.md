---
id: "wwdc2024-10147"
event: "wwdc2024"
year: 2024
title: "Elevate your tab and sidebar experience in iPadOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10147"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Elevate your tab and sidebar experience in iPadOS

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10147](https://developer.apple.com/videos/play/wwdc2024/10147)

iPadOS 18 introduces a new navigation system that gives people the flexibility to choose between using a tab bar or sidebar. The newly redesigned tab bar provides more space for content and other functionality. Learn how to use SwiftUI and UIKit to enable customization features – like adding, removing and reordering tabs – to enable a more personal touch in your app.

**Keywords:** `design`, `side bar`, `tab bar`, `tabs`, `zoom`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,888 words)

## Documentation & Resources

- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation.json
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Destination Video](https://developer.apple.com/documentation/visionOS/destination-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/destination-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/destination-video.json

## Code Snippets

### TabView updates in SwiftUI — [4:27]

```swift
TabView {
    Tab("Watch Now", systemImage: "play") {
        WatchNowView()
    }
    Tab("Library", systemImage: "books.vertical") {
        LibraryView()
    }
    // ...
}
```

### UITabBarController updates in UIKIt — [4:58]

```swift
tabBarController.tabs = [
    UITab(title: "Watch Now", image: UIImage(systemName: "play"), identifier: "Tabs.watchNow") { _ in
       WatchNowViewController()
    },
    UITab(title: "Library", image: UIImage(systemName: "books.vertical"), identifier: "Tabs.library") { _ in
       LibraryViewController()
    },
    // ...
]
```

### Search tab — [5:58]

```swift
// SwiftUI
Tab(role: .search) {
    SearchView()
}

// UIKit
let searchTab = UISearchTab {
    SearchViewController()
}
```

### Adding a sidebar in SwiftUI — [6:41]

```swift
TabView {
    Tab("Watch Now", systemImage: "play") {
        // ...
    }
    Tab("Library", systemImage: "books.vertical") {
        // ...
    }
    // ...
    TabSection("Collections") {
        Tab("Cinematic Shots", systemImage: "list.and.film") {
            // ...
        }
        Tab("Forest Life", systemImage: "list.and.film") {
            // ...
        }
        // ...
    }
    TabSection("Animations") {
        // ...
    }
    Tab(role: .search) {
        // ...
    }
}
.tabViewStyle(.sidebarAdaptable)
```

### Adding a sidebar in UIKit — [7:16]

```swift
let collectionsGroup = UITabGroup(
    title: "Collections",
    image: UIImage(systemName: "folder"),
    identifier: "Tabs.CollectionsGroup"
    children: self.collectionsTabs()) { _ in
        // ...
}

tabBarController.mode = .tabSidebar
tabBarController.tabs = [
    UITab(title: "Watch Now", ...) { _ in
        // ...
    },
    UITab(title: "Library", ...) { _ in
        // ...
    },
    // ...
    collectionsGroup,
    UITabGroup(title: "Animations", ...) { _ in
        // ...
    },
    UISearchTab { _ in
        // ...
    },
]
```

### Updating a tab group in UIKit — [7:35]

```swift
let collectionsGroup = UITabGroup(
    title: "Collections",
    image: UIImage(systemName: "folder"),
    identifier: "Tabs.CollectionsGroup"
    children: self.collectionsTabs()) { _ in
        // ...
}


let newCollection = UITab(...)
collectionsGroup.children.append(newCollection)
```

### Sidebar actions — [7:45]

```swift
TabSection(...) {
    // ...
}
.sectionActions {
    Button("New Station", ...) {
        // action
    }
}

// UIKit

let tabGroup = UITabGroup(...)
tabGroup.sidebarActions = [
    UIAction(title: "New Station", ...) { _ in
        // action
    },
]
```

### Drop destinations in SwiftUI — [8:12]

```swift
Tab(collection.name, image: collection.image) {
    CollectionDetailView(collection)
}
.dropDestination(for: Photo.self) { photos in
    // Add 'photos' to the specified collection
}
```

### Drop destinations in UIKit — [8:24]

```swift
func tabBarController(
    _ tabBarController: UITabBarController,
    tab: UITab, operationForAcceptingItemsFrom dropSession: any UIDropSession
) -> UIDropOperation {
    session.canLoadObjects(ofClass: Photo.self) ? .copy : .cancel
}

func tabBarController(
    _ tabBarController: UITabBarController,
    tab: UITab, acceptItemsFrom dropSession: any UIDropSession) {
    session.loadObjects(ofClass: Photo.self) { photos in
        // Add 'photos' to the specified collection
    }
}
```

### TabView customization in SwiftUI — [10:45]

```swift
@AppStorage("MyTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Watch Now", systemImage: "play", value: .watchNow) {
        // ...
    }
    .customizationID("Tab.watchNow")
    // ...
    TabSection("Collections") {
        ForEach(MyCollectionsTab.allCases) { tab in
            Tab(...) {
                // ...
            }
            .customizationID(tab.customizationID)
        }
    }
    .customizationID("Tab.collections")
    // ...
}
.tabViewCustomization($customization)
```

### Customization behavior and visibility in SwiftUI — [11:40]

```swift
Tab("Watch Now", systemImage: "play", value: .watchNow) {
    // ...
}
.customizationBehavior(.disabled, for: .sidebar, .tabBar)


Tab("Optional Tab", ...) {
    // ...
}
.customizationID("Tab.example.optional")
.defaultVisibility(.hidden, for: .tabBar)
```

### Tab customization in UIKit — [12:38]

```swift
let myTab = UITab(...)
myTab.allowsHiding = true
print(myTab.isHidden)


// .default, .optional, .movable, .pinned, .fixed, .sidebarOnly
myTab.preferredPlacement = .fixed


let myTabGroup = UITabGroup(...)
myTabGroup.allowsReordering = true
myTabGroup.displayOrderIdentifiers = [...]
```

### Observing customization changes in UIKit — [12:39]

```swift
func tabBarController(_ tabBarController: UITabBarController, visibilityDidChangeFor tabs: [UITab]) {
    // Read 'tab.isHidden' for the updated visibility.
}

func tabBarController(_ tabBarController: UITabBarController, displayOrderDidChangeFor group: UITabGroup) {
    // Read 'group.displayOrderIdentifiers' for the updated order.
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10147/4/4B3986F3-DBA0-4C52-8A2E-783346D6D1BA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10147/4/4B3986F3-DBA0-4C52-8A2E-783346D6D1BA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10147) — developer.apple.com. Indexed for agent consumption._
