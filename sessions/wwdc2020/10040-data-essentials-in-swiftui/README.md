---
id: "wwdc2020-10040"
event: "wwdc2020"
year: 2020
title: "Data Essentials in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10040"
topics: ["Swift", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Data Essentials in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10040](https://developer.apple.com/videos/play/wwdc2020/10040)

Data is a complex part of any app, but SwiftUI makes it easy to ensure a smooth, data-driven experience from prototyping to production. Discover @State and @Binding, two powerful tools that can preserve and seamlessly update your Source of Truth. We'll also show you how ObservableObject lets you connect your views to your data model. Learn about some tricky challenges and cool new ways to solve them — directly from the experts! To get the most out of this session, you should be familiar with SwiftUI. Watch “App essentials in SwiftUI” and "Introduction to SwiftUI"

**Keywords:** `$`, `appstorage`, `@binding`, `bindings`, `body a pure function`, `data dependency`, `data model`, `model`, `objectwillchange`, `observableobject`, `onchange`, `onreceive`, `performance`, `projectedvalue`, `property wrapper`, `prototyping`, `@published`, `publisher`, `scenes`, `scenestorage`, `source of truth`, `state`, `@state`, `@stateobject`, `view`, `willset`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,942 words)

## Documentation & Resources

- [Model data](https://developer.apple.com/documentation/SwiftUI/Model-data) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Model-data
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Model-data.json

## Code Snippets

### BookCard — [2:09]

```swift
struct BookCard : View {
    let book: Book
    let progress: Double

    var body: some View {
        HStack {
            Cover(book.coverName)
            VStack(alignment: .leading) {
                TitleText(book.title)
                AuthorText(book.author)
            }
            Spacer()
            RingProgressView(value: progress)              
        }
    }
}
```

### EditorConfig — [3:35]

```swift
struct EditorConfig {
    var isEditorPresented = false
    var note = ""
    var progress: Double = 0
    mutating func present(initialProgress: Double) {
        progress = initialProgress
        note = ""
        isEditorPresented = true
    }
}
struct BookView: View {
    @State private var editorConfig = EditorConfig()
    func presentEditor() { editorConfig.present(…) }
    var body: some View {
        …
        Button(action: presentEditor) { … }
        …
    }
}
```

### ProgressEditor — [5:59]

```swift
struct EditorConfig {
    var isEditorPresented = false
    var note = ""
    var progress: Double = 0
}
struct BookView: View {
    @State private var editorConfig = EditorConfig()
    var body: some View {
        …
        ProgressEditor(editorConfig: $editorConfig)
        …
    }
}

struct ProgressEditor: View {
    @Binding var editorConfig: EditorConfig
    …
        TextEditor($editorConfig.note)
    …
}
```

### CurrentlyReading — [13:15]

```swift
/// The current reading progress for a specific book.
class CurrentlyReading: ObservableObject {
    let book: Book
    @Published var progress: ReadingProgress

    // …
}

struct ReadingProgress {
    struct Entry : Identifiable {
        let id: UUID
        let progress: Double
        let time: Date
        let note: String?
    }

    var entries: [Entry]
}
```

### BookView — [15:36]

```swift
struct BookView: View {
    @ObservedObject var currentlyReading: CurrentlyReading

    var body: some View {
        VStack {
            BookCard(
                currentlyReading: currentlyReading)

            //…

            ProgressDetailsList(
                progress: currentlyReading.progress)
        }
    }
}
```

### CurrentlyReading with isFinished — [17:50]

```swift
class CurrentlyReading: ObservableObject {
    let book: Book
    @Published var progress = ReadingProgress()
    @Published var isFinished = false

    var currentProgress: Double {
        isFinished ? 1.0 : progress.progress
    }
}
```

### BookView with Toggle — [18:21]

```swift
struct BookView: View {
    @ObservedObject var currentlyReading: CurrentlyReading

    var body: some View {
        VStack {
            BookCard(
                currentlyReading: currentlyReading)

            HStack {
                Button(action: presentEditor) { /* … */ }
                    .disabled(currentlyReading.isFinished)

                Toggle(
                    isOn: $currentlyReading.isFinished
                ) {
                    Label(
                        "I'm Done",
                        systemImage: "checkmark.circle.fill")
                }
            }
            //…
        }
    }
}
```

### CoverImageLoader — [19:58]

```swift
class CoverImageLoader: ObservableObject {
    @Published public private(set) var image: Image? = nil

    func load(_ name: String) {
        // …
    }

    func cancel() {
        // …
    }

    deinit {
        cancel()
    }
}
```

### BookCoverView — [20:20]

```swift
struct BookCoverView: View {
    @StateObject var loader = CoverImageLoader()

    var coverName: String
    var size: CGFloat

    var body: some View {
        CoverImage(loader.image, size: size)
            .onAppear { loader.load(coverName) }
    }
}
```

### ReadingListViewer (Bad) — [25:36]

```swift
struct ReadingListViewer: View {
    var body: some View {
        NavigationView {
            ReadingList()
            Placeholder()
        }
    }
}

struct ReadingList: View {
    @ObservedObject var store = ReadingListStore()

    var body: some View {
        // ...
    }
}
```

### ReadingListViewer (Good) — [26:39]

```swift
struct ReadingListViewer: View {
    var body: some View {
        NavigationView {
            ReadingList()
            Placeholder()
        }
    }
}

struct ReadingList: View {
    @StateObject var store = ReadingListStore()

    var body: some View {
        // ...
    }
}
```

### App-wide Source of Truth — [30:52]

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
```

### SceneStorage — [32:43]

```swift
struct ReadingListViewer: View {
    @SceneStorage("selection") var selection: String?

    var body: some View {
        NavigationView {
            ReadingList(selection: $selection)
            BookDetailPlaceholder()
        }
    }
}
```

### AppStorage — [33:49]

```swift
struct BookClubSettings: View {
    @AppStorage("updateArtwork") private var updateArtwork = true
    @AppStorage("syncProgress") private var syncProgress = true

    var body: some View {
        Form {
            Toggle(isOn: $updateArtwork) {
                //...
            }

            Toggle(isOn: $syncProgress) {
                //...
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10040/3/76E05CA6-5C92-45FC-8DB0-0009FC6D18F0/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10040) — developer.apple.com. Indexed for agent consumption._
