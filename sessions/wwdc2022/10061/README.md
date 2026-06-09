---
id: "wwdc2022-10061"
event: "wwdc2022"
year: 2022
title: "Bring multiple windows to your SwiftUI app "
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10061"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring multiple windows to your SwiftUI app 

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10061](https://developer.apple.com/videos/play/wwdc2022/10061)

Discover the latest SwiftUI APIs to help you present windows within your app’s scenes. We’ll explore how scene types like MenuBarExtra can help you easily build more kinds of apps using SwiftUI. We’ll also show you how to use modifiers that customize the presentation and behavior of your app windows to make even better macOS apps.

**Keywords:** `apps`, `auxiliary scene`, `book club`, `codable`, `.commandsremoved`, `context menu`, `customize windows`, `.defaultposition`, `.defaultsize`, `documentgroup`, `filedocument`, `hashable`, `identifiable`, `.keyboardshortcut`, `menu`, `menubarextra`, `menu bar extra`, `newdocument`, `openwindow`, `presented value`, `referencefiledocument`, `scene`, `settings`, `single window`, `state restoration`, `topleading`, `toptrailing`, `views`, `window`, `window customization`, `windowgroup`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,193 words)

## Documentation & Resources

- [Bringing multiple windows to your SwiftUI app](https://developer.apple.com/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/bringing-multiple-windows-to-your-swiftui-app.json
- [OpenDocumentAction](https://developer.apple.com/documentation/SwiftUI/OpenDocumentAction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/OpenDocumentAction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/OpenDocumentAction.json
- [NewDocumentAction](https://developer.apple.com/documentation/SwiftUI/NewDocumentAction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/NewDocumentAction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/NewDocumentAction.json
- [OpenWindowAction](https://developer.apple.com/documentation/SwiftUI/OpenWindowAction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/OpenWindowAction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/OpenWindowAction.json
- [Window](https://developer.apple.com/documentation/SwiftUI/Window) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Window
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Window.json
- [MenuBarExtra](https://developer.apple.com/documentation/SwiftUI/MenuBarExtra) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/MenuBarExtra
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/MenuBarExtra.json
- [Value and Reference Types](https://developer.apple.com/swift/blog/?id=10) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/swift/blog/?id=10
- [DocumentGroup](https://developer.apple.com/documentation/SwiftUI/DocumentGroup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/DocumentGroup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/DocumentGroup.json
- [WindowGroup](https://developer.apple.com/documentation/SwiftUI/WindowGroup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/WindowGroup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/WindowGroup.json

## Code Snippets

### Scene composition — [2:01]

```swift
import SwiftUI
import UniformTypeIdentifiers

@main
struct MultiSceneApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        #if os(iOS) || os(macOS)
        DocumentGroup(viewing: CustomImageDocument.self) { file in
            ImageViewer(file.document)
        }
        #endif

        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}

struct ContentView: View {
    var body: some View {
        Text("Content")
    }
}

struct ImageViewer: View {
    var document: CustomImageDocument

    init(_ document: CustomImageDocument) {
        self.document = document
    }

    var body: some View {
        Text("Image")
    }
}

struct SettingsView: View {
    var body: some View {
        Text("Settings")
    }
}

struct CustomImageDocument: FileDocument {
    var data: Data

    static var readableContentTypes: [UTType] { [UTType.image] }

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents
        else {
            throw CocoaError(.fileReadCorruptFile)
        }
        self.data = data
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        FileWrapper(regularFileWithContents: data)
    }
}
```

### Adding a window scene — [2:34]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

class ReadingListStore: ObservableObject {
}
```

### Standalone menu bar extra app — [3:01]

```swift
import SwiftUI

@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("Utility App", systemImage: "hammer") {
            AppMenu()
        }
    }
}

struct AppMenu: View {
    var body: some View {
        Text("App Menu Item")
    }
}
```

### Windowed app with menu bar extra — [3:35]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        #if os(macOS)
        MenuBarExtra("Book Club", systemImage: "book") {
            AppMenu()
        }
        #endif
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct AppMenu: View {
    var body: some View {
        Text("App Menu Item")
    }
}

class ReadingListStore: ObservableObject {
}
```

### Menu bar extra with default style — [3:42]

```swift
import SwiftUI

@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("Utility App", systemImage: "hammer") {
            AppMenu()
        }
    }
}

struct AppMenu: View {
    var body: some View {
        Text("App Menu Item")
    }
}
```

### Menu bar extra with window style — [3:49]

```swift
import SwiftUI

@main
struct UtilityApp: App {
    var body: some Scene {
        MenuBarExtra("Time Tracker", systemImage: "rectangle.stack.fill") {
            TimeTrackerChart()
        }
        .menuBarExtraStyle(.window)
    }
}

struct TimeTrackerChart: View {
    var body: some View {
        Text("Time Tracker Chart")
    }
}
```

### Book Club app definition — [4:14]

```swift
import SwiftUI

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
        Text("Reading List")
    }
}

class ReadingListStore: ObservableObject {
}
```

### Adding an auxiliary Window Scene — [4:38]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

class ReadingListStore: ObservableObject {
}
```

### Open book context menu button — [5:28]

```swift
import SwiftUI

struct OpenBookButton: View {
    var book: Book

    var body: some View {
        Button("Open In New Window") {
        }
    }
}

struct Book: Identifiable {
    var id: UUID
}
```

### Opening a window using an identifier — [5:34]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
    }
}

struct OpenWindowButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open Activity Window") {
            openWindow(id: "activity")
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

class ReadingListStore: ObservableObject {
}
```

### Opening a window using a presented value — [5:57]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        WindowGroup("Book Details", for: Book.ID.self) { $bookId in
            BookDetail(id: $bookId, store: store)
        }
    }
}

struct OpenWindowButton: View {
    var book: Book
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open In New Window") {
            openWindow(value: book.id)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

struct BookDetail: View {
    @Binding var id: Book.ID?
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Book Details")
    }
}

struct Book: Identifiable {
    var id: UUID
}

class ReadingListStore: ObservableObject {
}
```

### Opening a window with a new document — [6:16]

```swift
import SwiftUI
import UniformTypeIdentifiers

@main
struct TextFileApp: App {
    var body: some Scene {
        DocumentGroup(viewing: TextFile.self) { file in
            TextEditor(text: file.$document.text)
        }
    }
}

struct NewDocumentButton: View {
    @Environment(\.newDocument) private var newDocument

    var body: some View {
        Button("Open New Document") {
            newDocument(TextFile())
        }
    }
}

struct TextFile: FileDocument {
    var text: String

    static var readableContentTypes: [UTType] { [UTType.plainText] }

    init() {
        text = ""
    }

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents,
              let string = String(data: data, encoding: .utf8)
        else {
            throw CocoaError(.fileReadCorruptFile)
        }
        text = string
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        let data = text.data(using: .utf8)!
        return FileWrapper(regularFileWithContents: data)
    }
}
```

### Opening a window with an existing document — [6:41]

```swift
import SwiftUI
import UniformTypeIdentifiers

@main
struct TextFileApp: App {
    var body: some Scene {
        DocumentGroup(viewing: TextFile.self) { file in
            TextEditor(text: file.$document.text)
        }
    }
}

struct OpenDocumentButton: View {
    var documentURL: URL
    @Environment(\.openDocument) private var openDocument

    var body: some View {
        Button("Open Document") {
            Task {
                do {
                    try await openDocument(at: documentURL)
                } catch {
                    // Handle error
                }
            }
        }
    }
}

struct TextFile: FileDocument {
    var text: String

    static var readableContentTypes: [UTType] { [UTType.plainText] }

    init() {
        text = ""
    }

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents,
              let string = String(data: data, encoding: .utf8)
        else {
            throw CocoaError(.fileReadCorruptFile)
        }
        text = string
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        let data = text.data(using: .utf8)!
        return FileWrapper(regularFileWithContents: data)
    }
}
```

### Book details context menu button — [7:03]

```swift
struct OpenWindowButton: View {
    var book: Book
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open In New Window") {
            openWindow(value: book.id)
        }
    }
}

struct Book: Identifiable {
    var id: UUID
}
```

### Book details context menu button — [7:08]

```swift
struct OpenWindowButton: View {
    var book: Book
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open In New Window") {
            openWindow(value: book.id)
        }
    }
}

struct Book: Identifiable {
    var id: UUID
}
```

### Book Club app with book details Scene — [9:06]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        WindowGroup("Book Details", for: Book.ID.self) { $bookId in
            BookDetail(id: $bookId, store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

struct BookDetail: View {
    @Binding var id: Book.ID?
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Book Details")
    }
}

struct Book: Identifiable {
    var id: UUID
}

class ReadingListStore: ObservableObject {
}
```

### Book Club app with book details Scene — [10:32]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        WindowGroup("Book Details", for: Book.ID.self) { $bookId in
            BookDetail(id: $bookId, store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

struct BookDetail: View {
    @Binding var id: Book.ID?
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Book Details")
    }
}

struct Book: Identifiable {
    var id: UUID
}

class ReadingListStore: ObservableObject {
}
```

### Removing default commands for the book details scene — [11:16]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        WindowGroup("Book Details", for: Book.ID.self) { $bookId in
            BookDetail(id: $bookId, store: store)
        }
        .commandsRemoved()
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

struct BookDetail: View {
    @Binding var id: Book.ID?
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Book Details")
    }
}

struct Book: Identifiable {
    var id: UUID
}

class ReadingListStore: ObservableObject {
}
```

### Extracting reading activity into custom scene — [11:46]

```swift
import SwiftUI

@main
struct BookClub: App {
    @StateObject private var store = ReadingListStore()

    var body: some Scene {
        WindowGroup {
            ReadingListViewer(store: store)
        }

      	ReadingActivityScene(store: store)

        WindowGroup("Book Details", for: Book.ID.self) { $bookId in
            BookDetail(id: $bookId, store: store)
        }
        .commandsRemoved()
    }
}

struct ReadingActivityScene: Scene {
    @ObservedObject var store: ReadingListStore

    var body: some Scene {
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
    }
}

struct ReadingListViewer: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading List")
    }
}

struct ReadingActivity: View {
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Reading Activity")
    }
}

struct BookDetail: View {
    @Binding var id: Book.ID?
    @ObservedObject var store: ReadingListStore

    var body: some View {
        Text("Book Details")
    }
}

struct Book: Identifiable {
    var id: UUID
}

class ReadingListStore: ObservableObject {
}
```

### Applying the defaultPosition modifier — [12:04]

```swift
struct ReadingActivityScene: Scene {
    @ObservedObject var store: ReadingListStore

    var body: some Scene {
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        .defaultPosition(.topTrailing)
    }
}

class ReadingListStore: ObservableObject {
}
```

### Applying the defaultSize modifier — [12:32]

```swift
struct ReadingActivityScene: Scene {
    @ObservedObject var store: ReadingListStore

    var body: some Scene {
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        #if os(macOS)
        .defaultPosition(.topTrailing)
      	.defaultSize(width: 400, height: 800)
        #endif
    }
}

class ReadingListStore: ObservableObject {
}
```

### Applying the keyboardShortcut modifier — [12:50]

```swift
struct ReadingActivityScene: Scene {
    @ObservedObject var store: ReadingListStore

    var body: some Scene {
        Window("Activity", id: "activity") {
            ReadingActivity(store: store)
        }
        #if os(macOS)
        .defaultPosition(.topTrailing)
      	.defaultSize(width: 400, height: 800)
        #endif
        #if os(macOS) || os(iOS)
        .keyboardShortcut("0", modifiers: [.option, .command])
        #endif
    }
}

class ReadingListStore: ObservableObject {
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10061/4/012AFD7A-B26E-4C25-9C6C-AB01D5336EA7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10061/4/012AFD7A-B26E-4C25-9C6C-AB01D5336EA7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10061) — developer.apple.com. Indexed for agent consumption._