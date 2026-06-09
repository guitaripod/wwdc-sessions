---
id: "wwdc2022-10059"
event: "wwdc2022"
year: 2022
title: "The craft of SwiftUI API design: Progressive disclosure"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10059"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# The craft of SwiftUI API design: Progressive disclosure

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10059](https://developer.apple.com/videos/play/wwdc2022/10059)

Explore progressive disclosure — one of SwiftUI’s core principles — and learn how it influences the design of our APIs. We’ll show you how we use progressive disclosure, discuss how it can support quick iteration and exploration, and help you take advantage of it in your own code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,150 words)

## Code Snippets

### Declaration Site Example — [1:59]

```swift
struct BookView: View {
    let pageNumber: Int
    let book: Book

    init(book: Book, pageNumber: Int) {
        self.book = book
        self.pageNumber = pageNumber
    }

    var body: some View { ... }
}
```

### Call Site Example — [2:13]

```swift
VStack {
    BookView(book: favoriteBook, page: 1)
    BookView(book: savedBook, page: 234)
}
```

### Button Label — [4:18]

```swift
Button("Next Page") {
    currentPage += 1
}
```

### Button label expanded — [4:36]

```swift
Button {
    currentPage += 1
} label: {
    Text("Next Page")
}
```

### Button label advanced case — [4:43]

```swift
Button {
    currentPage += 1
} label: {
    HStack {
        Text("Next Page")
        NextPagePreview()
    }
}
```

### Button label common case — [4:56]

```swift
Button("Next Page") {
    currentPage += 1
}
```

### Text example — [5:30]

```swift
Text("Hello WWDC22!")
```

### Stacks of Text — [6:12]

```swift
VStack {
    Text("Hello WWDC22!")
    Text("Call to Code.")
}
```

### Toolbar — [6:46]

```swift
.toolbar {
    Button {
        addItem()
    } label: {
        Label("Add", systemImage: "plus")
    }

    Button {
        sort()
    } label: {
        Label("Sort", systemImage: "arrow.up.arrow.down")
    }

    Button {
        openShareSheet()
    }: label: {
        Label("Share", systemImage: "square.and.arrow.up")
    }
}
```

### Toolbar with explicit placement — [7:20]

```swift
.toolbar {
    ToolbarItemGroup(placement: .navigationBarLeading) {
        Button {
            addItem()
        } label: {
            Label("Add", systemImage: "plus")
        }

        Button {
            sort()
        } label: {
            Label("Sort", systemImage: "arrow.up.arrow.down")
        }

        Button {
            openShareSheet()
        }: label: {
            Label("Share", systemImage: "square.and.arrow.up")
        }
    }
}
```

### Advanced use case table — [8:09]

```swift
@State var sortOrder = [KeyPathComparator(\Book.title)]

var body: some View {
    Table(sortOrder: $sortOrder) {
        TableColumn("Title", value: \Book.title) { book in
            Text(book.title).bold()
        }
        TableColumn("Author", value: \Book.author) { book in
            Text(book.author).italic()
        }
    } rows: {
        Section("Favorites") {
            ForEach(favorites) { book in
                TableRow(book)
            }
        }
        Section("Currently Reading") {
            ForEach(currentlyReading) { book in
                TableRow(book)
            }
        }
    }
    .onChange(of: sortOrder) { newValue in
        favorites.sort(using: newValue)
        currentlyReading.sort(using: newValue)
    }
}
```

### Simpler table use case — [8:41]

```swift
@State var sortOrder = [KeyPathComparator(\Book.title)]

var body: some View {
    Table(sortOrder: $sortOrder) {
        TableColumn("Title", value: \Book.title) { book in
            Text(book.title)
        }
        TableColumn("Author", value: \Book.author) { book in
            Text(book.author)
        }
    } rows: {
        ForEach(currentlyReading) { book in
            TableRow(book)
        }
    }
    .onChange(of: sortOrder) { newValue in
        currentlyReading.sort(using: newValue)
    }
}
```

### Table collection convenience — [9:58]

```swift
@State var sortOrder = [KeyPathComparator(\Book.title)]

var body: some View {
    Table(currentlyReading, sortOrder: $sortOrder) {
        TableColumn("Title", value: \.title) { book in
            Text(book.title)
        }
        TableColumn("Author", value: \.author) { book in
            Text(book.author)
        }
    }
    .onChange(of: sortOrder) { newValue in
        currentlyReading.sort(using: newValue)
    }
}
```

### Table string key path convenience — [10:23]

```swift
@State var sortOrder = [KeyPathComparator(\Book.title)]

var body: some View {
    Table(currentlyReading, sortOrder: $sortOrder) {
        TableColumn("Title", value: \.title)
        TableColumn("Author", value: \.author)
    }
    .onChange(of: sortOrder) { newValue in
        currentlyReading.sort(using: newValue)
    }
}
```

### Table without sorting — [10:51]

```swift
var body: some View {
    Table(currentlyReading) {
        TableColumn("Title", value: \.title)
        TableColumn("Author", value: \.author)
    }
}
```

### Stack example: leading — [13:37]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // leading
            Box().tint(.red)
            Box().tint(.green)
            Box().tint(.blue)
        }
    }
}
```

### Stack example: centered — [13:40]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // centered
            Spacer()
            Box().tint(.red)
            Box().tint(.green)
            Box().tint(.blue)
            Spacer()
        }
    }
}
```

### Stack example: evenly spaced — [13:42]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // evenly spaced
            Spacer()
            Box().tint(.red)
            Spacer()
            Box().tint(.green)
            Spacer()
            Box().tint(.blue)
            Spacer()
        }
    }
}
```

### Stack example: space only between elements — [13:43]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // space only between elements
            Box().tint(.red)
            Spacer()
            Box().tint(.green)
            Spacer()
            Box().tint(.blue)
        }
    }
}
```

### Stack example: space only before last element — [13:46]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // space only before last element
            Box().tint(.red)
            Box().tint(.green)
            Spacer()
            Box().tint(.blue)
        }
    }
}
```

### Stack example: space only after first element — [13:47]

```swift
struct StackExample: View {
    var body: some View {
        HStack { // space only after first element
            Box().tint(.red)
            Spacer()
            Box().tint(.green)
            Box().tint(.blue)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10059/3/689200F0-E14A-4B93-A3B2-7D95D747540F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10059/3/689200F0-E14A-4B93-A3B2-7D95D747540F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10059) — developer.apple.com. Indexed for agent consumption._