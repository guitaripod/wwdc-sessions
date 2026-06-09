---
id: "wwdc2025-256"
event: "wwdc2025"
year: 2025
title: "What’s new in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/256"
topics: ["Developer Tools", "Essentials", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in SwiftUI

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-256](https://developer.apple.com/videos/play/wwdc2025/256)

Learn what’s new in SwiftUI to build great apps for any Apple platform. We’ll explore how to give your app a brand new look and feel with Liquid Glass. Discover how to boost performance with framework enhancements and new instruments, and integrate advanced capabilities like web content and rich text editing. We’ll also show you how SwiftUI is expanding to more places, including laying out views in three dimensions.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,159 words)

## Documentation & Resources

- [Applying Liquid Glass to custom views](https://developer.apple.com/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Applying-Liquid-Glass-to-custom-views.json
- [Populating SwiftUI menus with adaptive controls](https://developer.apple.com/documentation/SwiftUI/Populating-SwiftUI-menus-with-adaptive-controls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Populating-SwiftUI-menus-with-adaptive-controls
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Populating-SwiftUI-menus-with-adaptive-controls.json
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TechnologyOverviews/adopting-liquid-glass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TechnologyOverviews/adopting-liquid-glass.json
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines

## Code Snippets

### Toolbar spacer — [2:27]

```swift
import SwiftUI

struct TripDetailView: View {
    var body: some View {
        NavigationStack {
            TripList()
                .toolbar {
                    ToolbarItemGroup(placement: .primaryAction) {
                        UpButton()
                        DownButton()
                    }

                    ToolbarSpacer(.fixed, placement: .primaryAction)

                    ToolbarItem(placement: .primaryAction) {
                        SettingsButton()
                    }
                }
        }
    }
}

struct TripList: View {
    var body: some View {
        Text("TripList")
    }
}

struct UpButton: View {
    var body: some View {
        Button("Up", systemImage: "chevron.up") { }
    }
}

struct DownButton: View {
    var body: some View {
        Button("Down", systemImage: "chevron.down") { }
    }
}

struct SettingsButton: View {
    var body: some View {
        Button("List Settings", systemImage: "ellipsis") { }
    }
}
```

### Toolbar item tint — [2:52]

```swift
import SwiftUI

struct InspectorView: View {
    var body: some View {
        NavigationStack {
            InspectorMap()
                .toolbar {
                    ToolbarItem(placement: .primaryAction) {
                        SaveLocationButton()
                            .buttonStyle(.borderedProminent)
                            .tint(.pink)
                    }
                }
        }
    }
}

struct InspectorMap: View {
    var body: some View {
        Text("InspectorMap")
    }
}

struct SaveLocationButton: View {
    var body: some View {
        Button("SaveLocationButton") { }
    }
}
```

### Searchable — [3:30]

```swift
import SwiftUI

struct PlannerSplitView: View {
    @State private var query: String = ""

    var body: some View {
        NavigationSplitView {
            Text("Sidebar")
        } detail: {
            Text("Detail")
        }
        .searchable(
            text: $query,
            prompt: "What are you looking for?"
        )
    }
}
```

### Search tab — [4:12]

```swift
import SwiftUI

struct HealthTabView: View {
    @State private var text: String = ""

    var body: some View {
        TabView {
            Tab("Summary", systemImage: "heart") {
                NavigationStack {
                    Text("Summary")
                }
            }
            Tab("Sharing", systemImage: "person.2") {
                NavigationStack {
                    Text("Sharing")
                }
            }
            Tab(role: .search) {
                NavigationStack {
                    Text("Search")
                }
            }
        }
        .searchable(text: $text)
    }
}
```

### Glass effect — [4:37]

```swift
import SwiftUI

struct ToTopButton: View {
    var body: some View {
        Button("To Top", systemImage: "chevron.up") {
            scrollToTop()
        }
        .padding()
        .glassEffect()
    }

    func scrollToTop() {
        // Scroll to top of view
    }
}
```

### Menu bar commands — [5:20]

```swift
import SwiftUI

@main
struct TravelPhotographyApp: App {
    var body: some Scene {
        WindowGroup {
            RootView()
        }
        .commands {
            TextEditingCommands()
        }
    }
}

struct RootView: View {
    var body: some View {
        Text("RootView")
    }
}
```

### Window resize anchor — [6:40]

```swift
import SwiftUI

struct SettingsTabView: View {
    @State private var selection: SectionTab = .general
    var body: some View {
        TabView(selection: $selection.animation()) {
            Tab("General", systemImage: "gear", value: .general) {
                Text("General")
            }
            Tab("Sections", systemImage: "list.bullet", value: .sections) {
                Text("Sections")
            }
        }
        .windowResizeAnchor(.top)
    }
}

enum SectionTab: Hashable {
    case general
    case sections
}
```

### @Animatable macro — [11:24]

```swift
import SwiftUI

@Animatable
struct LoadingArc: Shape {
    var center: CGPoint
    var radius: CGFloat
    var startAngle: Angle
    var endAngle: Angle
    @AnimatableIgnored var drawPathClockwise: Bool

    func path(in rect: CGRect) -> Path {
        // Creates a `Path` arc using properties
        return Path()
    }
}
```

### Spatial overlay — [12:15]

```swift
import RealityKit
import SwiftUI

struct Map: View {
    @Binding var timeAlignment: Alignment3D

    var body: some View {
        Model3D(named: "Map")
            .spatialOverlay(
                alignment: timeAlignment
            ) {
                Sun()
            }
    }
}

struct Sun: View {
    var body: some View {
        Model3D(named: "Sun")
    }
}
```

### Manipulable and surface snapping — [13:04]

```swift
import ARKit
import RealityKit
import SwiftUI

struct BackpackWaterBottle: View {
    @Environment(\.surfaceSnappingInfo) var snappingInfo: SurfaceSnappingInfo

    var body: some View {
        VStackLayout().depthAlignment(.center) {
            waterBottleView
                .manipulable()

            Pedestal()
                .opacity(
                    snappingInfo.classification == .table ? 1.0 : 0.0)
        }
    }

    var waterBottleView: some View {
        Model3D(named: "waterBottle")
    }
}

struct WaterBottleView: View {
    var body: some View {
        Model3D(named: "waterBottle")
    }
}

struct Pedestal: View {
    var body: some View {
        Model3D(named: "pedestal")
    }
}
```

### SwiftUI scenes — [15:00]

```swift
import SwiftUI

@main
struct PhotoWalk: App {
    var body: some Scene {
        WindowGroup(id: "AppContents") {
            PhotoWalkContent()
        }
    }
}

struct PhotoWalkContent: View {
    var body: some View {
        Text("PhotoWalkContent")
    }
}
```

### Assistive Access scene — [16:28]

```swift
import SwiftUI

@main
struct PhotoWalk: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
    }

    AssistiveAccess {
      AssistiveAccessContentView()
    }
  }
}

struct ContentView: View {
  var body: some View {
    Text("ContentView")
  }
}

struct AssistiveAccessContentView: View {
  var body: some View {
    Text("AssistiveAccessContentView")
  }
}
```

### SwiftUI presentations from RealityKit — [17:52]

```swift
import RealityKit
import SwiftUI

struct PopoverComponentView: View {
    @State private var popoverPresented: Bool = false
    var body: some View {
        RealityView { c in
            let mapEntity = Entity()

            let popover = Entity()
            mapEntity.addChild(popover)
            popover.components[PresentationComponent.self] = PresentationComponent(
                isPresented: $popoverPresented,
                configuration: .popover(arrowEdge: .bottom),
                content: DetailsView()
            )
        }
    }
}

struct DetailsView: View {
    var body: some View {
        Text("DetailsView")
    }
}
```

### Level of detail — [19:24]

```swift
import SwiftUI
import WidgetKit

struct PhotoCountdownView: View {
    @Environment(\.levelOfDetail) var levelOfDetail: LevelOfDetail
    var body: some View {
        switch levelOfDetail {
        case .default:
            RecentPhotosView()
        case .simplified:
            CountdownView()
        default:
            Text("Unknown level of detail")
        }
    }
}

struct RecentPhotosView: View {
    var body: some View {
        Text("RecentPhotosView")
    }
}

struct CountdownView: View {
    var body: some View {
        Text("CountdownView")
    }
}
```

### WebView — [20:28]

```swift
import SwiftUI
import WebKit

struct HikeGuideWebView: View {
    var body: some View {
        WebView(url: sunshineMountainURL)
    }

    var sunshineMountainURL: URL {
        URL(string: "sunshineMountainURL")!
    }
}
```

### WebView with WebPage — [20:44]

```swift
import SwiftUI
import WebKit

struct InAppBrowser: View {
    @State private var page = WebPage()

    var body: some View {
        WebView(page)
            .ignoresSafeArea()
            .onAppear {
                page.load(URLRequest(url: sunshineMountainURL))
            }
    }

    var sunshineMountainURL: URL {
        URL(string: "sunshineMountainURL")!
    }
}
```

### 3D charts — [21:35]

```swift
import Charts
import SwiftUI

struct HikePlotView: View {
    var body: some View {
        Chart3D {
            SurfacePlot(
                x: "x", y: "y", z: "z") { x, y in
                    sin(x) * cos(y)
                }
                .foregroundStyle(Gradient(colors: [.orange, .pink]))
        }
        .chartXScale(domain: -3 ... 3)
        .chartYScale(domain: -3 ... 3)
        .chartZScale(domain: -3 ... 3)
    }
}
```

### macOS drag and drop — [22:18]

```swift
import SwiftUI

struct DragDropExample: View {
    @State private var selectedPhotos: [Photo.ID] = []
    var body: some View {
        ScrollView {
            LazyVGrid(columns: gridColumns) {
                ForEach(model.photos) { photo in
                    view(photo: photo)
                        .draggable(containerItemID: photo.id)
                }
            }
        }
        .dragContainer(for: Photo.self, selection: selectedPhotos) { draggedIDs in
            photos(ids: draggedIDs)
        }
        .dragConfiguration(DragConfiguration(allowMove: false, allowDelete: true))
            .onDragSessionUpdated { session in
                let ids = session.draggedItemIDs(for: Photo.ID.self)
                    if session.phase == .ended(.delete) {
                        trash(ids)
                        deletePhotos(ids)
                    }
            }
        .dragPreviewsFormation(.stack)
    }
}
```

### Rich text view — [23:55]

```swift
import SwiftUI

struct CommentEditor: View {
    @Binding var commentText: AttributedString

    var body: some View {
        TextEditor(text: $commentText)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/256/4/353ed635-9639-48db-8c8c-69b2b7e499c1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/256/4/353ed635-9639-48db-8c8c-69b2b7e499c1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/256) — developer.apple.com. Indexed for agent consumption._