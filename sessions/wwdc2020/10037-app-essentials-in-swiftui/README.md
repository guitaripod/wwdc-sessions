---
id: "wwdc2020-10037"
event: "wwdc2020"
year: 2020
title: "App essentials in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10037"
topics: ["Swift", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# App essentials in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10037](https://developer.apple.com/videos/play/wwdc2020/10037)

Thanks to the new App protocol, SwiftUI now supports building entire apps! See how Apps, Scenes, and Views fit together. Learn how easy it is to implement the features people expect from a best-in-class product while saving time and reducing complexity. Easily add expected functionality to your interface using the new commands modifier, and explore the ins and outs of the new WindowGroup API. To get the most out of this session, you should have some experience with SwiftUI. Watch “Introduction to SwiftUI” for a primer. Want more SwiftUI? Take your pick: “What’s new in SwiftUI”, “Data essentials in Swift UI ”, "Stacks, grids, and outlines in SwiftUI", and “Build document-based apps in SwiftUI”.

**Keywords:** `app protocol`, `apps`, `body property`, `commands`, `commands modifier`, `custom commands`, `data-driven app`, `documentgroup`, `navigationtitle`, `scene`, `scenes`, `scenestorage`, `scenestorage property wrapper`, `settings`, `settings scene`, `stateobject`, `view definition`, `view modifier`, `views`, `windowgroup`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,180 words)

## Documentation & Resources

- [Scene](https://developer.apple.com/documentation/SwiftUI/Scene) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Scene
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Scene.json
- [WindowGroup](https://developer.apple.com/documentation/SwiftUI/WindowGroup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/WindowGroup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/WindowGroup.json
- [App](https://developer.apple.com/documentation/SwiftUI/App) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/App
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/App.json

## Code Snippets

### Book club app — [3:57]

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

### Window groups — [10:21]

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

### Scene storage — [12:07]

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
    @SceneStorage("selectedItem") private var selectedItem: String?

    var selectedID: Binding<UUID?> {
        Binding<UUID?>(
            get: { selectedItem.flatMap { UUID(uuidString: $0) } },
            set: { selectedItem = $0?.uuidString }
        )
    }

    var body: some View {
        NavigationView {
            List(store.books) { book in
                NavigationLink(
                    destination: Text(book.title),
                    tag: book.id,
                    selection: selectedID
                ) {
                    Text(book.title)
                }
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

### Document groups — [12:59]

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

### Settings scene — [13:27]

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
        Book2(title: "Book #1", author: "Author #1"),
        Book2(title: "Book #2", author: "Author #2"),
        Book2(title: "Book #3", author: "Author #3")
    ]
}

struct Book: Identifiable {
    let id = UUID()
    let title: String
    let author: String
}
```

### BookCommands — [14:07]

```swift
struct BookCommands: Commands {
    @FocusedBinding(\.selectedBook) private var selectedBook: Book?

    var body: some Commands {
        CommandMenu("Book") {
            Section {
                Button("Update Progress...", action: updateProgress)
                    .keyboardShortcut("u")
                Button("Mark Completed", action: markCompleted)
                    .keyboardShortcut("C")
            }
            .disabled(selectedBook == nil)
        }
    }

    private func updateProgress() {
        selectedBook?.updateProgress()
    }
    private func markCompleted() {
        selectedBook?.markCompleted()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10037/4/5067872D-87D8-44F5-9E73-28180361AC31/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10037) — developer.apple.com. Indexed for agent consumption._
