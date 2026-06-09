---
id: "wwdc2020-10041"
event: "wwdc2020"
year: 2020
title: "What's new in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10041"
topics: ["Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10041](https://developer.apple.com/videos/play/wwdc2020/10041)

SwiftUI can help you build better and more powerful apps for iPhone, iPad, Mac, Apple Watch, and Apple TV. Learn more about the latest refinements to SwiftUI, including interface improvements like outlines, grids, and toolbars. Take advantage of SwiftUI’s enhanced support across Apple frameworks to enable features like Sign In with Apple. Discover new visual effects, as well as new controls and styles. And find out how the new app and scene APIs enable you to create apps entirely in SwiftUI, as well as custom complications and all new widgets. To get the most out of this session, you should be familiar with SwiftUI. Watch "Introduction to SwiftUI" for a primer.

**Keywords:** `app api`, `apps`, `body property`, `commands`, `commands api`, `complications`, `containerrelativeshape`, `custom accent color`, `custom commands`, `custom complication`, `custom fonts`, `custom menus`, `declarative`, `default focus support`, `documentgroup`, `drag and drop`, `focus`, `font scaling`, `gauge`, `grids`, `.keyboardshortcut`, `keyboard shortcut`, `label`, `launch screen`, `launch screen info plist key`, `lazyhstack`, `lazy loading grid layout`, `lazy stacks`, `lazyvstack`, `link`, `list`, `.listitemtint`, `matchedgeometryeffect`, `multiplatform code`, `multiple trailing closure`, `multiple windows`, `opening url`, `openurl`, `outlines`, `progressview`, `@scaledmetric`, `scene`, `settings`, `settings scene`, `sign in with apple`, `swiftui`, `toolbar`, `.toolbar`, `uilaunchscreen`, `uniformtypeidentifiers`, `universal links`, `widgets`, `windowgroup`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,149 words)

## Documentation & Resources

- [SwiftUI](https://developer.apple.com/documentation/SwiftUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI.json

## Code Snippets

### Hello World — [1:26]

```swift
@main
struct HelloWorld: App {
    var body: some Scene {
        WindowGroup {
            Text("Hello, world!").padding()
        }
    }
}
```

### Book Club app — [1:56]

```swift
@main
struct BookClubApp: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        NavigationView {
            List(store.books) { book in
                Text(book.title)
            }
            .navigationTitle("Currently Reading")
        }
    }
}

class ReadingListStore: ObservableObject {
    init() {}

    var books = [
        Book(title: "Book #1", author: "Author #1"),
        Book(title: "Book #2", author: "Author #2"),
        Book(title: "Book #3", author: "Author #3")
    ]
}

struct Book: Identifiable {
    let id = UUID()
    let title: String
    let author: String
}
```

### Settings — [4:46]

```swift
@main
struct BookClubApp: App {
    @StateObject private var store = ReadingListStore()

    @SceneBuilder var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }

    #if os(macOS)
        Settings {
            BookClubSettingsView()
        }
    #endif
    }
}

struct BookClubSettingsView: View {
    var body: some View {
        Text("Add your settings UI here.")
            .padding()
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        NavigationView {
            List(store.books) { book in
                Text(book.title)
            }
            .navigationTitle("Currently Reading")
        }
    }
}

class ReadingListStore: ObservableObject {
    init() {}

    var books = [
        Book(title: "Book #1", author: "Author #1"),
        Book(title: "Book #2", author: "Author #2"),
        Book(title: "Book #3", author: "Author #3")
    ]
}

struct Book: Identifiable {
    let id = UUID()
    let title: String
    let author: String
}
```

### Document groups — [5:10]

```swift
import SwiftUI
import UniformTypeIdentifiers

@main
struct ShapeEditApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: ShapeDocument()) { file in
            DocumentView(document: file.$document)
        }
    }
}

struct DocumentView: View {
    @Binding var document: ShapeDocument

    var body: some View {
        Text(document.title)
            .frame(width: 300, height: 200)
    }
}

struct ShapeDocument: Codable {
    var title: String = "Untitled"
}

extension UTType {
    static let shapeEditDocument =
        UTType(exportedAs: "com.example.ShapeEdit.shapes")
}

extension ShapeDocument: FileDocument {
    static var readableContentTypes: [UTType] { [.shapeEditDocument] }

    init(fileWrapper: FileWrapper, contentType: UTType) throws {
        let data = fileWrapper.regularFileContents!
        self = try JSONDecoder().decode(Self.self, from: data)
    }

    func write(to fileWrapper: inout FileWrapper, contentType: UTType) throws {
        let data = try JSONEncoder().encode(self)
        fileWrapper = FileWrapper(regularFileWithContents: data)
    }
}
```

### Custom Commands — [5:49]

```swift
import SwiftUI
import UniformTypeIdentifiers

@main
struct ShapeEditApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: ShapeDocument()) { file in
            DocumentView(document: file.$document)
        }
        .commands {
            CommandMenu("Shapes") {
                Button("Add Shape...", action: addShape)
                    .keyboardShortcut("N")
                Button("Add Text", action: addText)
                    .keyboardShortcut("T")
            }
        }
    }

    func addShape() {}
    func addText() {}
}

struct DocumentView: View {
    @Binding var document: ShapeDocument

    var body: some View {
        Text(document.title)
            .frame(width: 300, height: 200)
    }
}

struct ShapeDocument: Codable {
    var title: String = "Untitled"
}

extension UTType {
    static let shapeEditDocument =
        UTType(exportedAs: "com.example.ShapeEdit.shapes")
}

extension ShapeDocument: FileDocument {
    static var readableContentTypes: [UTType] { [.shapeEditDocument] }

    init(fileWrapper: FileWrapper, contentType: UTType) throws {
        let data = fileWrapper.regularFileContents!
        self = try JSONDecoder().decode(Self.self, from: data)
    }

    func write(to fileWrapper: inout FileWrapper, contentType: UTType) throws {
        let data = try JSONEncoder().encode(self)
        fileWrapper = FileWrapper(regularFileWithContents: data)
    }
}
```

### Widgets — [7:55]

```swift
import SwiftUI
import WidgetKit

@main
struct RecommendedAlbum: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: "RecommendedAlbum",
            provider: Provider(),
            placeholder: PlaceholderView()
        ) { entry in
            AlbumWidgetView(album: entry.album)
        }
        .configurationDisplayName("Recommended Album")
        .description("Your recommendation for the day.")
    }
}

struct AlbumWidgetView: View {
    var album: Album

    var body: some View {
        Text(album.title)
    }
}

struct PlaceholderView: View {
    var body: some View {
        Text("Placeholder View")
    }
}

struct Album {
    var title: String
}

struct Provider: TimelineProvider {
    struct Entry: TimelineEntry {
        var album: Album
        var date: Date
    }

    public func snapshot(with context: Context, completion: @escaping (Entry) -> ()) {
        let entry = Entry(album: Album(title: "Untitled"), date: Date())
        completion(entry)
    }

    public func timeline(with context: Context, completion: @escaping (Timeline<Entry>) -> ()) {
        var entries: [Entry] = []

        // Generate a timeline consisting of five entries an hour apart, starting from the current date.
        let currentDate = Date()
        for hourOffset in 0 ..< 5 {
            let entryDate = Calendar.current.date(byAdding: .hour, value: hourOffset, to: currentDate)!
            let entry = Entry(album: Album(title: "Untitled #\(hourOffset)"), date: entryDate)
            entries.append(entry)
        }

        let timeline = Timeline(entries: entries, policy: .atEnd)
        completion(timeline)
    }
}
```

### Complications using SwiftUI — [8:31]

```swift
struct CoffeeHistoryChart: View {
    var body: some View {
        VStack {
            ComplicationHistoryLabel {
                Text("Weekly Coffee")
                    .complicationForeground()
            }
            HistoryChart()
        }
        .complicationChartFont()
    }
}

struct ComplicationHistoryLabel: View { ... }
struct HistoryChart: View { ... }

extension View {
    func complicationChartFont() -> some View { ... }
}
```

### Outlines — [9:22]

```swift
struct OutlineContentView: View {
    var graphics: [Graphic]

    var body: some View {
        List(graphics, children: \.children) { graphic in
            GraphicRow(graphic)
        }
        .listStyle(SidebarListStyle())
    }
}

struct Graphic: Identifiable {
    var id: String
    var name: String
    var icon: Image
    var children: [Graphic]?
}

struct GraphicRow: View {
    var graphic: Graphic

    init(_ graphic: Graphic) {
        self.graphic = graphic
    }

    var body: some View {
        Label {
            Text(graphic.name)
        } icon: {
            graphic.icon
        }
    }
}
```

### Adaptive grids — [10:09]

```swift
struct ContentView: View {
    var items: [Item]

    var body: some View {
        ScrollView {
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 176))]) {
                ForEach(items) { item in
                    ItemView(item: item)
                }
            }
            .padding()
        }
    }
}

struct Item: Identifiable {
    var name: String
    var id = UUID()

    var icon: Image {
        Image(systemName: name)
    }
    var color: Color {
        colors[colorIndex % (colors.count - 1)]
    }

    private static var nextColorIndex: Int = 0
    private var colorIndex: Int

    init(name: String) {
        self.name = name

        colorIndex = Self.nextColorIndex
        Self.nextColorIndex += 1
    }
}

struct ItemView: View {
    var item: Item

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .fill()
                .layoutPriority(1)
                .foregroundColor(item.color)
            item.icon
                .resizable()
                .aspectRatio(contentMode: .fit)
                .padding(.all, 16)
                .foregroundColor(.white)
        }
        .frame(width: 176, height: 110)
    }
}
```

### Fixed-column grids — [10:28]

```swift
struct ContentView: View {
    var items: [Item]

    var body: some View {
        ScrollView {
            LazyVGrid(columns: Array(repeating: GridItem(), count: 4)]) {
                ForEach(items) { item in
                    ItemView(item: item)
                }
            }
            .padding()
        }
    }
}

struct Item: Identifiable {
    var name: String
    var id = UUID()

    var icon: Image {
        Image(systemName: name)
    }
    var color: Color {
        colors[colorIndex % (colors.count - 1)]
    }

    private static var nextColorIndex: Int = 0
    private var colorIndex: Int

    init(name: String) {
        self.name = name

        colorIndex = Self.nextColorIndex
        Self.nextColorIndex += 1
    }
}

struct ItemView: View {
    var item: Item

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .fill()
                .layoutPriority(1)
                .foregroundColor(item.color)
            item.icon
                .resizable()
                .aspectRatio(contentMode: .fit)
                .padding(.all, 16)
                .foregroundColor(.white)
        }
        .frame(width: 176, height: 110)
    }
}
```

### Horizontal grids — [10:38]

```swift
struct ContentView: View {
    var items: [Item]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHGrid(rows: [GridItem(.adaptive(minimum: 110))]) {
                ForEach(items) { item in
                    ItemView(item: item)
                }
            }
            .padding()
        }
    }
}

struct Item: Identifiable {
    var name: String
    var id = UUID()

    var icon: Image {
        Image(systemName: name)
    }
    var color: Color {
        colors[colorIndex % (colors.count - 1)]
    }

    private static var nextColorIndex: Int = 0
    private var colorIndex: Int

    init(name: String) {
        self.name = name
        colorIndex = Self.nextColorIndex
        Self.nextColorIndex += 1
    }
}

struct ItemView: View {
    var item: Item

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 8, style: .continuous)
                .fill()
                .layoutPriority(1)
                .foregroundColor(item.color)
            item.icon
                .resizable()
                .aspectRatio(contentMode: .fit)
                .padding(.all, 16)
                .foregroundColor(.white)
        }
        .frame(width: 176, height: 110)
    }
}
```

### Lazy stacks — [10:58]

```swift
struct WildlifeList: View {
    var rows: [ImageRow]

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 2) {
                ForEach(rows) { row in
                    switch row.content {
                    case let .singleImage(image):
                        SingleImageLayout(image: image)
                    case let .imageGroup(images):
                        ImageGroupLayout(images: images)
                    case let .imageRow(images):
                        ImageRowLayout(images: images)
                    }
                }
            }
        }
    }
}
```

### Toolbar modifier — [12:24]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Book List")
        }
        .toolbar {
            Button(action: recordProgress) {
                Label("Record Progress", systemImage: "book.circle")
            }
        }
    }

    private func recordProgress() {}
}
```

### ToolbarItem — [12:40]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Book List")
        }
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                Button(action: recordProgress) {
                    Label("Record Progress", systemImage: "book.circle")
                }
            }
        }
    }

    private func recordProgress() {}
}
```

### Confirmation and cancellation toolbar placements — [12:47]

```swift
struct ContentView: View {
    var body: some View {
        Form {
            Slider(value: .constant(0.39))
        }
        .toolbar {
            ToolbarItem(placement: .confirmationAction) {
                Button("Save", action: saveProgress)
            }
            ToolbarItem(placement: .cancellationAction) {
                Button("Cancel", action: dismissSheet)
            }
        }
    }

    private func saveProgress() {}
    private func dismissSheet() {}
}
```

### Principal toolbar placement — [13:00]

```swift
struct ContentView: View {
    enum ViewMode {
        case details
        case notes
    }

    @State private var viewMode: ViewMode = .details

    var body: some View {
        List {
            Text("Book Detail")
        }
        .toolbar {
            ToolbarItem(placement: .principal) {
                Picker("View", selection: $viewMode) {
                    Text("Details").tag(ViewMode.details)
                    Text("Notes").tag(ViewMode.notes)
                }
            }
        }
    }
}
```

### Bottom bar toolbar placement — [13:17]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Book Detail")
        }
        .toolbar {
            ToolbarItem {
                Button(action: recordProgress) {
                    Label("Progress", systemImage: "book.circle")
                }
            }
            ToolbarItem(placement: .bottomBar) {
                Button(action: shareBook) {
                    Label("Share", systemImage: "square.and.arrow.up")
                }
            }
        }
    }

    private func recordProgress() {}
    private func shareBook() {}
}
```

### Label — [13:38]

```swift
Label("Progress", systemImage: "book.circle")
```

### Label expanded form — [14:06]

```swift
Label {
    Text("Progress")
} icon: {
    Image(systemName: "book.circle")
}
```

### Bottom bar toolbar placement — [14:24]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Book Detail")
        }
        .toolbar {
            ToolbarItem {
                Button(action: recordProgress) {
                    Label("Progress", systemImage: "book.circle")
                }
            }
            ToolbarItem(placement: .bottomBar) {
                Button(action: shareBook) {
                    Label("Share", systemImage: "square.and.arrow.up")
                }
            }
        }
    }

    private func recordProgress() {}
    private func shareBook() {}
}
```

### Context menu Labels — [14:36]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Text("Book List Row")
            .contextMenu {
                Button(action: recordProgress) {
                    Label("Progress", systemImage: "book.circle")
                }
                Button(action: addToFavorites) {
                    Label("Add to Favorites", systemImage: "heart")
                }
                Button(action: shareBook) {
                    Label("Share", systemImage: "square.and.arrow.up")
                }
            }
        }
    }

    private func recordProgress() {}
    private func addToFavorites() {}
    private func shareBook() {}
}
```

### List Labels — [14:39]

```swift
struct ContentView: View {
    var body: some View {
        List {
            Group {
                Label("Introducing SwiftUI", systemImage: "hand.wave")
                Label("SwiftUI Essentials", systemImage: "studentdesk")
                Label("Data Essentials in SwiftUI", systemImage: "flowchart")
                Label("App Essentials in SwiftUI", systemImage: "macwindow.on.rectangle")
            }
            Group {
                Label("Build Document-based apps in SwiftUI", systemImage: "doc")
                Label("Stacks, Grids, and Outlines", systemImage: "list.bullet.rectangle")
                Label("Building Custom Views in SwiftUI", systemImage: "sparkles")
                Label("Build SwiftUI Apps for tvOS", systemImage: "tv")
                Label("Build SwiftUI Views for Widgets", systemImage: "square.grid.2x2.fill")
                Label("Create Complications for Apple Watch", systemImage: "gauge")
                Label("SwiftUI on All Devices", systemImage: "laptopcomputer.and.iphone")
                Label("Integrating SwiftUI", systemImage: "rectangle.connected.to.line.below")
            }
        }
    }
}
```

### Help modifier — [15:28]

```swift
struct ContentView: View {
    var body: some View {
        Button(action: recordProgress) {
            Label("Progress", systemImage: "book.circle")
        }
        .help("Record new progress entry")
    }

    private func recordProgress() {}
}
```

### Keyboard shortcut modifier — [16:12]

```swift
@main
struct BookClubApp: App {
    var body: some Scene {
        WindowGroup {
            List {
                Text("Reading List Viewer")
            }
        }
        .commands {
            Button("Previous Book", action: selectPrevious)
                .keyboardShortcut("[")
            Button("Next Book", action: selectNext)
                .keyboardShortcut("]")
        }
    }

    private func selectPreviousBook() {}
    private func selectNextBook() {}
}
```

### Cancel and default action keyboard shortcuts — [16:28]

```swift
struct ContentView: View {
    var body: some View {
        HStack {
            Button("Cancel", action: dismissSheet)
                .keyboardShortcut(.cancelAction)

            Button("Save", action: saveProgress)
                .keyboardShortcut(.defaultAction)
        }
    }

    private func dismissSheet() {}
    private func saveProgress() {}
}
```

### ProgressView — [17:08]

```swift
struct ContentView: View {
    var percentComplete: Double

    var body: some View {
        ProgressView("Downloading Photo", value: percentComplete)
    }
}
```

### Circular ProgressView — [17:19]

```swift
struct ContentView: View {
    var percentComplete: Double

    var body: some View {
        ProgressView("Downloading Photo", value: percentComplete)
            .progressViewStyle(CircularProgressViewStyle())
    }
}
```

### Activity indicator ProgressView — [17:25]

```swift
struct ContentView: View {
    var body: some View {
        ProgressView()
    }
}
```

### Gauge — [17:32]

```swift
struct ContentView: View {
    var acidity: Double

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Label("Soil Acidity", systemImage: "drop.fill")
                .foregroundColor(.green)
        }
    }
}
```

### Gauge with current value label — [17:52]

```swift
struct ContentView: View {
    var acidity: Double

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Label("Soil Acidity", systemImage: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        }
    }
}
```

### Gauge with minimum and maximum value labels — [18:00]

```swift
struct ContentView: View {
    var acidity: Double

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Label("Soil Acidity", systemImage: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        } minimumValueLabel: {
            Text("3")
        } maximumValueLabel: {
            Text("10")
        }
    }
}
```

### Initial Album Picker — [18:57]

```swift
struct ContentView: View {
    @State private var selectedAlbumIDs: Set<Album.ID> = []

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                albumGrid.padding(.horizontal)
            }

            Divider().zIndex(-1)

            selectedAlbumRow
                .frame(height: AlbumCell.albumSize)
                .padding(.top, 8)
        }
        .buttonStyle(PlainButtonStyle())
    }

    private var albumGrid: some View {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: AlbumCell.albumSize))], spacing: 8) {
           ForEach(unselectedAlbums) { album in
              Button(action: { select(album) }) {
                 AlbumCell(album)
              }
           }
        }
    }

    private var selectedAlbumRow: some View {
        HStack {
            ForEach(selectedAlbums) { album in
                AlbumCell(album)
            }
        }
    }

    private var unselectedAlbums: [Album] {
        Album.allAlbums.filter { !selectedAlbumIDs.contains($0.id) }
    }
    private var selectedAlbums: [Album] {
        Album.allAlbums.filter { selectedAlbumIDs.contains($0.id) }
    }

    private func select(_ album: Album) {
        withAnimation(.spring(response: 0.5)) {
            _ = selectedAlbumIDs.insert(album.id)
        }
    }
}

struct AlbumCell: View {
    static let albumSize: CGFloat = 100

    var album: Album

    init(_ album: Album) {
        self.album = album
    }

    var body: some View {
        album.image
            .frame(width: AlbumCell.albumSize, height: AlbumCell.albumSize)
            .background(Color.pink)
            .cornerRadius(6.0)
    }
}

struct Album: Identifiable {
    static let allAlbums: [Album] = [
        .init(name: "Sample", image: Image(systemName: "music.note")),
        .init(name: "Sample 2", image: Image(systemName: "music.note.list")),
        .init(name: "Sample 3", image: Image(systemName: "music.quarternote.3")),
        .init(name: "Sample 4", image: Image(systemName: "music.mic")),
        .init(name: "Sample 5", image: Image(systemName: "music.note.house")),
        .init(name: "Sample 6", image: Image(systemName: "tv.music.note"))
    ]

    var name: String
    var image: Image

    var id: String { name }
}
```

### Matched geometry effect Album Picker — [19:17]

```swift
struct ContentView: View {
    @Namespace private var namespace
    @State private var selectedAlbumIDs: Set<Album.ID> = []

    var body: some View {
        VStack(spacing: 0) {
            ScrollView {
                albumGrid.padding(.horizontal)
            }

            Divider().zIndex(-1)

            selectedAlbumRow
                .frame(height: AlbumCell.albumSize)
                .padding(.top, 8)
        }
        .buttonStyle(PlainButtonStyle())
    }

    private var albumGrid: some View {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: AlbumCell.albumSize))], spacing: 8) {
           ForEach(unselectedAlbums) { album in
              Button(action: { select(album) }) {
                 AlbumCell(album)
              }
              .matchedGeometryEffect(id: album.id, in: namespace)
           }
        }
    }

    private var selectedAlbumRow: some View {
        HStack {
            ForEach(selectedAlbums) { album in
                AlbumCell(album)
                .matchedGeometryEffect(id: album.id, in: namespace)
            }
        }
    }

    private var unselectedAlbums: [Album] {
        Album.allAlbums.filter { !selectedAlbumIDs.contains($0.id) }
    }
    private var selectedAlbums: [Album] {
        Album.allAlbums.filter { selectedAlbumIDs.contains($0.id) }
    }

    private func select(_ album: Album) {
        withAnimation(.spring(response: 0.5)) {
            _ = selectedAlbumIDs.insert(album.id)
        }
    }
}

struct AlbumCell: View {
    static let albumSize: CGFloat = 100

    var album: Album

    init(_ album: Album) {
        self.album = album
    }

    var body: some View {
        album.image
            .frame(width: AlbumCell.albumSize, height: AlbumCell.albumSize)
            .background(Color.pink)
            .cornerRadius(6.0)
    }
}

struct Album: Identifiable {
    static let allAlbums: [Album] = [
        .init(name: "Sample", image: Image(systemName: "music.note")),
        .init(name: "Sample 2", image: Image(systemName: "music.note.list")),
        .init(name: "Sample 3", image: Image(systemName: "music.quarternote.3")),
        .init(name: "Sample 4", image: Image(systemName: "music.mic")),
        .init(name: "Sample 5", image: Image(systemName: "music.note.house")),
        .init(name: "Sample 6", image: Image(systemName: "tv.music.note"))
    ]

    var name: String
    var image: Image

    var id: String { name }
}
```

### Container Relative Shape — [19:53]

```swift
struct AlbumWidgetView: View {
    var album: Album

    var body: some View {
        album.image
            .clipShape(ContainerRelativeShape())
            .padding()
    }
}

struct Album {
    var name: String
    var artist: String
    var image: Image
}
```

### Dynamic Type scaling — [20:34]

```swift
struct ContentView: View {
    var album: Album
    @ScaledMetric private var padding: CGFloat = 10

    var body: some View {
        VStack {
            Text(album.name)
                .font(.custom("AvenirNext-Bold", size: 30))

            Text("\(Image(systemName: "music.mic")) \(album.artist)")
                .font(.custom("AvenirNext-Bold", size: 17))

        }
        .padding(padding)
        .background(RoundedRectangle(cornerRadius: 16, style: .continuous).fill(Color.purple))
    }
}

struct Album {
    var name: String
    var artist: String
    var image: Image
}
```

### Initial Sidebar List — [22:08]

```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                Label("Menu", systemImage: "list.bullet")

                Label("Favorites", systemImage: "heart")

                Label("Rewards", systemImage: "seal")

                Section(header: Text("Recipes")) {
                    ForEach(1..<4) {
                        Label("Recipes \($0)", systemImage: "book.closed")
                    }
                }
            }
            .listStyle(SidebarListStyle())
        }
    }
}
```

### List Item Tint in Sidebars — [22:17]

```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                Label("Menu", systemImage: "list.bullet")

                Label("Favorites", systemImage: "heart")
                    .listItemTint(.red)

                Label("Rewards", systemImage: "seal")
                    .listItemTint(.purple)

                Section(header: Text("Recipes")) {
                    ForEach(1..<4) {
                        Label("Recipes \($0)", systemImage: "book.closed")
                    }
                }
                .listItemTint(.monochrome)
            }
            .listStyle(SidebarListStyle())
        }
    }
}
```

### List Item Tint on watchOS — [22:33]

```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                Label("Menu", systemImage: "list.bullet")

                Label("Favorites", systemImage: "heart")
                    .listItemTint(.red)

                Label("Rewards", systemImage: "seal")
                    .listItemTint(.purple)

                Section(header: Text("Recipes")) {
                    ForEach(1..<4) {
                        Label("Recipes \($0)", systemImage: "book.closed")
                    }
                }
                .listItemTint(.monochrome)
            }
        }
    }
}
```

### SwitchToggleStyle tint — [22:46]

```swift
struct ContentView: View {
    @State var order = Order()

    var body: some View {
        Toggle("Send notification when ready", isOn: $order.notifyWhenReady)
            .toggleStyle(SwitchToggleStyle(tint: .accentColor))
    }
}

struct Order {
    var notifyWhenReady = true
}
```

### Link — [23:15]

```swift
let appleURL = URL(string: "https://developer.apple.com/tutorials/swiftui/")!
let wwdcAnnouncementURL = URL(string: "https://apple.news/AjriX1CWUT-OfjXu_R4QsnA")!

struct ContentView: View {
    var body: some View {
        Form {
            Section {
                Link(destination: apple) {
                    Label("SwiftUI Tutorials", systemImage: "swift")
                }
                Link(destination: wwdcAnnouncementURL) {
                    Label("WWDC 2020 Announcement", systemImage: "chevron.left.slash.chevron.right")
                }
            }
        }
    }
}
```

### OpenURL Environment Action — [23:56]

```swift
let customPublisher = NotificationCenter.default.publisher(for: .init("CustomURLRequestNotification"))
let apple = URL(string: "https://developer.apple.com/tutorials/swiftui/")!

struct ContentView: View {
    @Environment(\.openURL) private var openURL

    var body: some View {
        Text("OpenURL Environment Action")
            .onReceive(customPublisher) { output in
                if output.userInfo!["shouldOpenURL"] as! Bool {
                    openURL(apple)
                }
            }
    }
}
```

### Uniform Type Identifiers — [24:44]

```swift
import UniformTypeIdentifiers

extension UTType {
    static let myFileFormat = UTType(exportedAs: "com.example.myfileformat")
}

func introspecContentType(_ fileURL: URL) throws {
    // Get this file's content type.
    let resourceValues = try fileURL.resourceValues(forKeys: [.contentTypeKey])
    if let type = resourceValues.contentType {
        // Get the human presentable description of the type.
        let description = type.localizedDescription

        if type.conforms(to: .myFileFormat) {
            // The file is our app’s format.
        } else if type.conforms(to: .image) {
            // The file is an image.
        }
    }
}
```

### Sign in with Apple Button — [25:16]

```swift
import AuthenticationServices
import SwiftUI

struct ContentView: View {
    var body: some View {
        SignInWithAppleButton(
            .signUp,
            onRequest: handleRequest,
            onCompletion: handleCompletion
        )
        .signInWithAppleButtonStyle(.black)
    }

    private func handleRequest(request: ASAuthorizationAppleIDRequest) {}
    private func handleCompletion(result: Result<ASAuthorization, Error>) {}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10041/7/85DB087C-0A27-4779-B73A-7C5C888A7C82/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10041) — developer.apple.com. Indexed for agent consumption._
