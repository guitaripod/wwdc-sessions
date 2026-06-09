# What’s new in SwiftUI

**Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-269](https://developer.apple.com/videos/play/wwdc2026/269)

Explore the latest additions to SwiftUI and discover how they can improve your apps. We’ll introduce a new Document protocol with direct disk access and snapshot-based diffing for building high-performance apps; new APIs for reordering content in lists, grids, and sections; and toolbar enhancements including visibility priority and auto-minimizing behavior. We’ll also cover expanded presentation APIs — including swipe actions on any view — plus AsyncImage caching improvements and lazy state initialization for Observable types.

**Keywords:** `screenshots`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [State()](https://developer.apple.com/documentation/SwiftUI/State()) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/State()
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/State().json
- [ContentBuilder](https://developer.apple.com/documentation/SwiftUI/ContentBuilder) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ContentBuilder
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ContentBuilder.json
- [Swift Collections on GitHub](https://github.com/apple/swift-collections) _documentation_

## Code Snippets

### appearsActive environment value — [3:20]

```swift
struct SidebarFooterView: View {
    @Environment(\.appearsActive) private var appearsActive

    var body: some View {
        MyAccountView()
            .opacity(appearsActive ? 1 : 0.5)
    }
}
```

### Menu icon visibility — [3:34]

```swift
CommandMenu("Stickers") {
    Button { openStore() } label: {
        Label("Store", systemImage: "bag.fill")
            .labelStyle(.titleAndIcon)
        }
    }
    // Other menu items
}
```

### Prominent tab role — [5:12]

```swift
TabView {
    Tab { EventsTab() }
    Tab { HolidaysTab() }
    Tab { FunTab() }

    Tab(role: .prominent) {
        CartTab()
    }
}
```

### Toolbar item visibility and overflow menu — [6:15]

```swift
// Toolbar item visibility priority

StickerPageView()
    .toolbar {
        ToolbarItemGroup {
            UndoButton()
            RedoButton()
        }
        .visibilityPriority(.high)
        ToolbarOverflowMenu {
            ChoosePhotoButton()
            ExportAsImageButton()
            ClearAllStickersButton()
        }
        ToolbarItem(placement: .topBarPinnedTrailing) {
            ShareButton()
        }
    }
```

### Minimize toolbar on scroll with toolbarMinimizeBehavior — [7:37]

```swift
// Minimize toolbar when scrolling

ScrollView {
    StickerListView()
}
.toolbarMinimizeBehavior(.onScrollDown, for: .navigationBar)
```

### Document creation sources with context parameter — [9:47]

```swift
// Use the context to create a document

@main
struct Stickers: App {
    var body: some Scene {
        DocumentGroupLaunchScene("Create a Sticker Page") {
            NewDocumentButton("New Sticker Page", source: .blank)
            NewDocumentButton("Sticker Page from Photo…", source: .photo)
        }

        DocumentGroup { /* ... */ }
    }
}

extension DocumentCreationSource {
    static let blank = Self(id: "blank")
    static let photo = Self(id: "photo")
}
```

### Use the context to create a document — [10:01]

```swift
@main
struct Stickers: App {
    var body: some Scene {
        DocumentGroupLaunchScene("Create a Sticker Page") {
            NewDocumentButton("New Sticker Page", source: .blank)
            NewDocumentButton("Sticker Page from Photo…", source: .photo)
        }

        DocumentGroup { document in
            StickerPageDocumentView(document)
        } { configuration, context in
            StickerPageDocument(configuration: configuration, context: context)
        }
    }
}
```

### Document app declaration — [10:43]

```swift
@main
struct Stickers: App {
    var body: some Scene {
        DocumentGroup { /* ... */ }
        WindowGroup { /* ... */ }
    }
}
```

### Implement document writing — [11:25]

```swift
@Observable
final class StickerDocument {
    // ...
}
```

### Implement document writing: list writable formats — [11:34]

```swift
@Observable
final class StickerDocument {

    static let writableDocumentTypes: [UTType] = [.stickerDocument]

    // ...
}

import UniformTypeIdentifiers

extension UTType {
    static let stickerDocument = UTType(exportedAs: "stickerdocument")
}
```

### Implement document writing: provide snapshot — [11:45]

```swift
@Observable
final class StickerDocument {

    static let writableDocumentTypes: [UTType] = [.stickerDocument]

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending PageSnapshot { /* ... */ }

    // ...
}
```

### Implement document writing: represent the snapshot — [11:54]

```swift
struct PageSnapshot {
    var background: Image
    var metadata: StickerPlacements
    var stickers: [Image]
}

struct StickerPlacements { /* ... */ }
```

### Implement document writing: provide a DocumentWriter — [12:13]

```swift
@Observable
final class StickerDocument {

    static let writableDocumentTypes: [UTType] = [.stickerDocument]

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending PageSnapshot {
        makeSnapshot()
    }

    func writer(configuration: sending WriteConfiguration) -> sending Writer {
        Writer(contentType: configuration.contentType)
    }
}
```

### DocumentWriter: Snapshot — [12:33]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    // ...
}
```

### DocumentWriter: PageSnapshot as Snapshot — [12:36]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    let contentType: UTType

    // ...
}
```

### DocumentWriter protocol implementation — [12:42]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    let contentType: UTType

    nonisolated func write(
        snapshot: sending PageSnapshot, to destination: URL,
        previous: sending PageSnapshot?, progress: consuming Subprogress
    ) async throws {
        // write .stickerDocument
    }
}
```

### Progress reporting during writing — [13:18]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    let contentType: UTType

    nonisolated func write(
        snapshot: sending PageSnapshot, to destination: URL,
        previous: sending PageSnapshot?, progress: consuming Subprogress
    ) async throws {
        // report progress…
        // write .stickerDocument
    }
}
```

### Implement document reading with ReadableDocument protocol — [13:27]

```swift
extension StickerDocument: ReadableDocument {

}
```

### Add PNG to supported formats list — [14:35]

```swift
@Observable
final class StickerDocument: WritableDocument {

    static let writableContentTypes: [UTType] = [.stickerDocument, .png]
}
```

### Add content type checks — [14:48]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    let contentType: UTType

    nonisolated func write(
        snapshot: sending PageSnapshot, to destination: URL,
        previous: sending PageSnapshot?, progress: consuming Subprogress
    ) async throws {
        if contentType.conforms(to: .stickerDocument) {
            // write .stickerDocument
        } else if contentType.conforms(to: .png)

    }
}
```

### Writing multiple formats including PNG — [14:56]

```swift
struct Writer<Snapshot>: DocumentWriter {
    typealias Snapshot = PageSnapshot

    let contentType: UTType

    nonisolated func write(
        snapshot: sending PageSnapshot, to destination: URL, 
        previous: sending PageSnapshot?, progress: consuming Subprogress
    ) async throws {
        if contentType.conforms(to: .stickerDocument) {  
            // write .stickerDocument
        } else if contentType.conforms(to: .png) {
            let context = CGContext(/* ... */) 
            context.draw(/* ... */)
        }
    }
}
```

### Reorderable list with reorderContainer — [15:58]

```swift
List {
    ForEach(stickers) { sticker in
        StickerListItemView(sticker: sticker)
    }
    .reorderable()
}
.reorderContainer(for: Sticker.self) { difference in
    difference.apply(to: &stickers)
}
```

### Apply changes to a reorderable list's data source — [16:14]

```swift
import OrderedCollections // from https://github.com/apple/swift-collections

extension ReorderDifference where CollectionID == ReorderableSingleCollectionIdentifier {
    func apply(to values: inout [some Identifiable<ItemID>]) {
        var dictionary = OrderedDictionary(uniqueKeys: values.map { $0.id }, values: values)
        let destinationOffset: Int? = switch destination.position {
        case .before(let destination):
            dictionary.keys.firstIndex(of: destination)
        case .end:
            nil
        }
        dictionary.move(keys: sources, to: destinationOffset ?? values.endIndex)
        values = dictionary.values.elements
    }
}
```

### Reorderable grid with LazyVGrid — [16:48]

```swift
LazyVGrid {
    ForEach(stickers) { sticker in
        StickerListItemView(sticker: sticker)
    }
    .reorderable()
}
.reorderContainer(for: Sticker.self) { difference in
    difference.apply(to: &stickers)
}
```

### Swipe actions on List — [18:12]

```swift
List {
    ForEach(stickers) { sticker in
        StickerListItemView(sticker: sticker)
            .swipeActions {
                DeleteButton(sticker: sticker)
            }
    }
}
```

### Swipe actions on any view — [18:15]

```swift
ScrollView {
    LazyVStack {
        ForEach(stickers) { sticker in
            StickerListItemView(sticker: sticker)
                .swipeActions {
                    DeleteButton(sticker: sticker)
                }
        }
    }
}
.swipeActionsContainer()
```

### Confirmation dialog with item binding — [18:54]

```swift
struct StickerCanvasView: View {
    var stickers: [Sticker]
    @State private var stickerToDelete: Sticker?

    var body: some View {
        ZStack {
            ForEach(stickers) { sticker in
                PlacedStickerView(sticker: sticker)
                    .contextMenu {
                        // ...
                    }
            }
        }
        .confirmationDialog(
            "Delete?", item: $stickerToDelete
        ) { sticker in
            DeleteStickerButton(sticker)
        }   
    }
}
```

### Alert with item binding — [19:35]

```swift
struct StickerCanvasView: View {
    var stickers: [Sticker]
    @State private var stickerToDelete: Sticker?

    var body: some View {
        ZStack {
            ForEach(stickers) { sticker in
                PlacedStickerView(sticker: sticker)
                    .contextMenu {
                        // ...
                    }
            }
        }
        .alert(
            "Delete?", item: $stickerToDelete
        ) { sticker in
            DeleteStickerButton(sticker)
        }   
    }
}
```

### AsyncImage with URLRequest and custom URLSession — [21:18]

```swift
@Observable class StickerStore {
    static let imageSession: URLSession = {
        let config = URLSessionConfiguration.default
        config.urlCache = URLCache(
            memoryCapacity: 64 * 1024 * 1024,
            diskCapacity: 256 * 1024 * 1024)
        return URLSession(configuration: config)
    }()
}

ForEach(pets) { pet in
    AsyncImage(request: URLRequest(
        url: pet.imageURL,
        cachePolicy: .returnCacheDataElseLoad)
    )
}
.asyncImageURLSession(StickerStore.imageSession)
```

### @State converted to macro for lazy initialization — [23:08]

```swift
@Observable class StickerStore { }

struct StickerStoreView: View {
    // store is now lazily initialized, only
    // created once for the lifetime of the view
    @State private var store = StickerStore()

    var body: some View {
        // ...
    }
}
```

### @State macro init assignment error — [23:48]

```swift
struct StickerPageView: View {
    @State private var page = StickerPage()
    let title: String

    init(title: String) {
        self.page = StickerPage(title: title) // Variable 'self.title' used before being initialized
        self.title = title
    }

    var body: some View {
        // ...
    }
}
```

### Fixed @State macro init assignment error — [24:02]

```swift
struct StickerPageView: View {
    @State private var page: StickerPage // Removed default value to fix error
    let title: String

    init(title: String) {
        self.page = StickerPage(title: title)
        self.title = title
    }

    var body: some View {
        // ...
    }
}
```

### @ContentBuilder — [26:07]

```swift
@ContentBuilder
func stickerLibraryView() -> some View {
  // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/269/4/9215cf93-1308-4706-91e8-34d4e40939d1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/269/4/9215cf93-1308-4706-91e8-34d4e40939d1/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._