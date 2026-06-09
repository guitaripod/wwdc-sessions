---
id: "wwdc2022-10058"
event: "wwdc2022"
year: 2022
title: "SwiftUI on iPad: Organize your interface"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10058"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# SwiftUI on iPad: Organize your interface

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10058](https://developer.apple.com/videos/play/wwdc2022/10058)

It’s time to supercharge the interface of your iPad app with SwiftUI lists and tables. We’ll show how you can add selection interactions and context menus and help people who use your app be more productive. We'll also give you best practices on structuring your navigation and explore how you can avoid modality using split views to ensure a top-notch desktop-class iPad experience.

This is the first session in a two-part series. To get the most out of this video, we recommend you have some basic familiarity with SwiftUI. After watching this session, check out "SwiftUI on iPad: Add toolbars, titles, and more" to learn how SwiftUI can help you make even better toolbars for your iPad app.

**Keywords:** `.balanced`, `column builder`, `comparator`, `contextmenu`, `context menu`, `desktop class`, `edit mode`, `foreach`, `identifier`, `keyboard`, `keypathcomparator`, `list`, `lists`, `menu`, `modality`, `multicolumn`, `multi-column`, `multiple selection`, `multi select context menu`, `navigation`, `navigation split view`, `.prominentdetail`, `section`, `selection`, `selection state`, `sidebar`, `slide over`, `split view`, `state`, `supplementary`, `supplementary column`, `table`, `tables`, `tag`, `three column layout`, `trackpad`, `two column layout`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,083 words)

## Documentation & Resources

- [NavigationSplitViewStyle](https://developer.apple.com/documentation/SwiftUI/NavigationSplitViewStyle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/NavigationSplitViewStyle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/NavigationSplitViewStyle.json
- [contextMenu(menuItems:preview:)](https://developer.apple.com/documentation/SwiftUI/View/contextMenu(menuItems:preview:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View/contextMenu(menuItems:preview:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View/contextMenu(menuItems:preview:).json
- [EditMode](https://developer.apple.com/documentation/SwiftUI/EditMode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/EditMode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/EditMode.json
- [Tables](https://developer.apple.com/documentation/SwiftUI/Tables) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Tables
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Tables.json
- [List](https://developer.apple.com/documentation/SwiftUI/List) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/List
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/List.json
- [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/NavigationSplitView
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/NavigationSplitView.json

## Code Snippets

### Places List — [3:10]

```swift
struct PlacesList: View {
    @Binding var modelData: ModelData


    var body: some View {
        List(modelData.places) { place in
            PlaceCell(place)
        }
    }
}
```

### Places Table — [3:18]

```swift
struct PlacesTable: View {
    @Binding var modelData: ModelData     @State private var sortOrder = [KeyPathComparator(\Place.name)]

    var body: some View {
        Table(modelData.places, sortOrder: $sortOrder) {
            TableColumn("Name", value: \.name) { place in
                PlaceCell(place)
            }
            TableColumn("Comfort Level", value: \.comfortDescription).width(200)
            TableColumn("Noise", value: \.noiseLevel) { place in
                NoiseLevelView(level: place.noiseLevel)
            }
        }
        .onChange(of: sortOrder) {
            modelData.sort(using: $0)
        }
    }
}
```

### Places Table with selection — [10:25]

```swift
struct PlacesTable: View {
    @EnvironmentObject var modelData: ModelData
    @State private var sortOrder = [KeyPathComparator(\Place.name)]
    @State private var selection: Set<Place.ID> = []

    var body: some View {
        Table(modelData.places, selection: $selection, sortOrder: $sortOrder) {
            // columns
        }
    }
}
```

### Places Table toolbar additions — [10:26]

```swift
Table(modelData.places, selection: $selection, sortOrder: $sortOrder) {
    ...
}
.toolbar {
    ToolbarItemGroup(placement: .navigationBarTrailing) {
        if !selection.isEmpty {
           AddToGuideButton(selection)
        }
    }

    ToolbarItemGroup(placement: .navigationBarLeading) {
        EditButton()
    }
}
```

### Item context menus — [12:34]

```swift
// Item context menus

Table(modelData.places, selection: $selection, sortOrder: $sortOrder) {
    ...
}
.contextMenu(forSelectionType: Place.ID.self) { items in
    if items.isEmpty {
        // Empty area
        AddPlaceButton()
    } else {
        if items.count == 1 {
            // Single item
            FavoriteButton(isSet: $modelData.places[items.first!].isFavorite)
        }

        // Single and multiple items
        AddToGuideButton(items)
    }
}
```

### Navigation Split View example — [16:55]

```swift
// Navigation Split View example

struct ContentView: View {
    var body: some View {
        NavigationSplitView {
            SidebarView()
       } detail: {
            Text("Select a place")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10058/3/A2E41140-1058-4AFF-BF2C-5058A6588994/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10058/3/A2E41140-1058-4AFF-BF2C-5058A6588994/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10058) — developer.apple.com. Indexed for agent consumption._