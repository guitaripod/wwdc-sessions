---
id: "wwdc2025-323"
event: "wwdc2025"
year: 2025
title: "Build a SwiftUI app with the new design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/323"
topics: ["Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build a SwiftUI app with the new design

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-323](https://developer.apple.com/videos/play/wwdc2025/323)

Explore the ways Liquid Glass transforms the look and feel of your app. Discover how this stunning new material enhances toolbars, controls, and app structures across platforms, providing delightful interactions and seamlessly integrating your app with the system. Learn how to adopt new APIs that can help you make the most of Liquid Glass.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,669 words)

## Documentation & Resources

- [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views.json
- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass.json
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TechnologyOverviews/adopting-liquid-glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TechnologyOverviews/adopting-liquid-glass.json

## Code Snippets

### Segmented Picker — [1:11]

```swift
Picker("View", selection: $selection) {
    Text("Map").tag(ViewMode.map)
    Text("List").tag(ViewMode.list)
}
.pickerStyle(.segmented)
```

### Extend background images — [3:59]

```swift
// Extend background images

struct LandmarkDetailView: View {
    let landmark: Landmark

    var body: some View {
        ScrollView {
            VStack {
                Image(landmark.backgroundImageName)
                    .resizable()
                    .aspectRatio(contentMode: .fill)
                    .backgroundExtensionEffect()
            }
        }
    }
}
```

### Adding an inspector — [4:23]

```swift
// Adding an inspector

NavigationSplitView {
    // sidebar
} detail: {
    // detail
}
.inspector(isPresented: $presentInspector) {
    LandmarkDetailInspectorView(landmark: landmark)
}
```

### Minimize tab bar on scroll — [5:07]

```swift
// Minimize tab bar on scroll

TabView {
    // tabs
}
.tabBarMinimizeBehavior(.onScrollDown)
```

### Tab bar accessory — [5:39]

```swift
// Tab bar accessory

TabView {
    // tabs
}
.tabBarMinimizeBehavior(.onScrollDown)
.tabViewBottomAccessory {
    MusicPlaybackView()
}

struct MusicPlaybackView: View {
    @Environment(\.tabViewBottomAccessoryPlacement)
    var placement

    var body: some View {
        if placement == .inline {
            // compact layout
        } else {
            // full layout
        }
    }
}
```

### Sheets with presentation detents — [6:20]

```swift
// Sheets

CollectionDetailView()
    .sheet(isPresented: $isShowingLandmarksSelection) {
        LandmarksSelectionList()
            .presentationDetents([.height(180), .medium, .large])
    }
```

### Presentation background — [6:53]

```swift
// Presentation background

CollectionDetailView()
    .sheet(isPresented: $isShowingLandmarksSelection) {
        LandmarksSelectionList()
            .presentationDetents([.height(180), .medium, .large])
            .presentationBackground(.thickMaterial)
    }
```

### Zoom transition — [7:10]

```swift
// Zoom transition

@Namespace private var namespace

ContentView()
    .toolbar {
        ToolbarItem(placement: .bottomBar) {
            Button {
                isPresented = true
            } label: {
                Image(systemName: "map")
            }
            .matchedTransitionSource(
                id: "transition-id", in: namespace)
        }
    }
    .sheet(isPresented: $isPresented) {
        SheetContent()
            .navigationTransition(
                .zoom(
                    sourceID: "transition-id", in: namespace))
    }
```

### Toolbar menus — [7:27]

```swift
// Toolbar menus

LandmarkDetailView()
    .toolbar {
        ToolbarItemGroup {
            Button { } label: {
                Image(systemName: "square.and.arrow.up")
            }

            Menu(
                "Collections",
                systemImage: "book.closed"
            ) {
                // menu items
            }
        }
    }
```

### Confirmation dialog — [7:41]

```swift
// Confirmation dialog

CollectionDetailView()
    .toolbar {
        Button("Delete", systemImage: "trash") {
            presentDialog = true
        }
        .confirmationDialog(
            "Delete?",
            isPresented: $presentDialog
        ) {
            Button("Delete", role: .destructive) { }
        }
    }
```

### Visually separate toolbar items — [8:26]

```swift
// Visually separate toolbar items

struct LandmarkDetailView: View {
    var body: some View {
        ScrollView {
            ScrollContent()
        }
        .toolbar {
            ToolbarItem { ShareLink() }
            ToolbarSpacer(.fixed)
            ToolbarItem { FavoriteButton() }
            ToolbarItem { CollectionsButton() }
            ToolbarSpacer(.fixed)
            ToolbarItem { InspectorToggle() }
        }
    }
}
```

### Toolbar items with flexible spacing — [8:47]

```swift
// Toolbar items with flexible spacing

struct InboxView: View {
    var body: some View {
        ScrollView {
            ScrollContent()
        }
        .toolbar {
            ToolbarItem(placement: .bottomBar) {
                FilterPicker()
            }
            ToolbarSpacer(.flexible, placement: .bottomBar)
            DefaultToolbarItem(
                kind: .search, placement: .bottomBar)
            ToolbarSpacer(.fixed, placement: .bottomBar)
            ToolbarItem(placement: .bottomBar) {
                NewMessageButton()
            }
        }
    }
}
```

### Hide shared glass background — [9:07]

```swift
// Hide shared glass background

struct HomeView: View {
    var body: some View {
        ContentView()
            .toolbar {
                ToolbarItem {
                    ProfileButton()
                }
                .sharedBackgroundVisibility(.hidden)
            }
    }
}
```

### Toolbar item with a badge — [9:40]

```swift
// Toolbar item with a badge

@Environment(ModelData.self) var modelData

CollectionsView()
    .toolbar {
        ToolbarItemGroup {
            Button("Notifications", systemImage: "bell") { }
                .badge(modelData.notifications.count)
            Button("Add", systemImage: "plus") { }
        }
    }
```

### Hard scroll edge effect — [10:57]

```swift
// Hard scroll edge effect

ScrollView {
    // content
}
.scrollEdgeEffectStyle(.hard, for: .top)
```

### Search in top-trailing position — [11:44]

```swift
// Search in the top-trailing position

struct TopTrailingSearch: View {
    @State private var searchText = ""

    var body: some View {
        NavigationSplitView {
            SidebarContent()
        } detail: {
            DetailContent()
        }
        .searchable(text: $searchText)
    }
}
```

### Minimized search in toolbar — [12:51]

```swift
// Minimized search in the toolbar

struct MinimizedSearch: View {
    @State private var searchText = ""

    var body: some View {
        NavigationStack {
            DetailContent()
        }
        .searchable(text: $searchText)
        .searchToolbarBehavior(.minimize)
    }
}
```

### TabView with a search tab — [13:17]

```swift
// TabView with a search tab

struct ContentView: View {
    @State private var searchText = ""

    var body: some View {
        TabView {
            // other tabs

            Tab(role: .search) {
                NavigationStack {
                    SearchTabContent()
                }
            }
        }
        .searchable(text: $searchText)
    }
}
```

### Capsule buttons — [14:25]

```swift
Button(…)
.buttonBorderShape(.capsule)
```

### Button sizes: high density layouts — [15:09]

```swift
// Button sizes: high density layouts

VStack {
    Picker("Inspector View Mode", selection: $mode) {
        // options
    }
    .controlSize(.large)

    InspectorStackView()
        .controlSize(.small)
}
```

### Glass button styles — [15:33]

```swift
// Prominent glass button
Button("Get Started") { }
    .buttonStyle(.glassProminent)

// Standard glass button
Button("Learn More") { }
    .buttonStyle(.glass)
```

### macOS menu icons — [16:32]

```swift
// Menus

Menu("Edit") {
    Section {
        Button("Undo",
               systemImage: "arrow.uturn.backward") { }
        Button("Redo",
               systemImage: "arrow.uturn.forward") { }
    }

    Section {
        Button("Copy",
               systemImage: "document.on.document") { }
        Button("Duplicate",
               systemImage: "plus.square.on.square") { }
    }
}
```

### Concentric rectangle shape — [17:27]

```swift
// Concentric rectangle shape

CustomControl()
    .background(.tint, in: .rect(corner: .containerConcentric))
```

### Glass effect — [18:30]

```swift
// Glass effect

Label("Desert", systemImage: "sun.max.fill")
    .padding()
    .glassEffect()
```

### Glass effect: custom shape — [18:52]

```swift
// Customize shape

Label("Desert", systemImage: "sun.max.fill")
    .padding()
    .glassEffect(in: .rect(cornerRadius: 16))
```

### Glass effect: tinted — [18:59]

```swift
// Tinted glass

Label("Desert", systemImage: "sun.max.fill")
    .padding()
    .glassEffect(.regular.tint(.green))
```

### Glass effect: interactive — [19:21]

```swift
// Interactive glass

Label("Desert", systemImage: "sun.max.fill")
    .padding()
    .glassEffect(.regular.interactive())
```

### Glass morphing with GlassEffectContainer — [19:51]

```swift
// GlassEffectContainer

@Namespace var namespace

GlassEffectContainer {
    VStack {
        if isExpanded {
            VStack(spacing: 16) {
                ForEach(badges) { badge in
                    BadgeLabel(badge: badge)
                        .glassEffect()
                        .glassEffectID(badge.id, in: namespace)
                }
            }
        }

        BadgeToggle()
            .buttonStyle(.glass)
            .glassEffectID("badgeToggle", in: namespace)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/323/4/0fd37581-632a-4827-b656-d192163cece0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/323/4/0fd37581-632a-4827-b656-d192163cece0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/323) — developer.apple.com. Indexed for agent consumption._