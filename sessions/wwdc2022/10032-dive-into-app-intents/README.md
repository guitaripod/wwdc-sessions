---
id: "wwdc2022-10032"
event: "wwdc2022"
year: 2022
title: "Dive into App Intents"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10032"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Dive into App Intents

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10032](https://developer.apple.com/videos/play/wwdc2022/10032)

Learn how you can make your app more discoverable and increase app engagement when you use the App Intents framework. We'll take you through the powerful capabilities of this Swift framework, explore the differences between App Intents and SiriKit Intents, and show you how you can expose your app's functionality to the system. We'll also share how you can build entities and queries to create rich App Shortcuts experiences. To learn more about App Intents, watch "Implement App Shortcuts with App Intents" and "Design App Shortcuts" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,698 words)

## Documentation & Resources

- [App Intents](https://developer.apple.com/documentation/AppIntents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents.json

## Code Snippets

### Open Currently Reading — [5:33]

```swift
struct OpenCurrentlyReading: AppIntent {
    static var title: LocalizedStringResource = "Open Currently Reading"

    @MainActor
    func perform() async throws -> some IntentResult {
        Navigator.shared.openShelf(.currentlyReading)
        return .result()
    }

    static var openAppWhenRun: Bool = true
}
```

### App Shortcuts — [6:42]

```swift
struct LibraryAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: OpenCurrentlyReading(),
            phrases: ["Open Currently Reading in \(.applicationName)"],
            systemImageName: "books.vertical.fill"
        )
    }
}
```

### Shelf Enum — [7:11]

```swift
enum Shelf: String {
    case currentlyReading
    case wantToRead
    case read
}

extension Shelf: AppEnum {
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Shelf"

    static var caseDisplayRepresentations: [Shelf: DisplayRepresentation] = [
        .currentlyReading: "Currently Reading",
        .wantToRead: "Want to Read",
        .read: "Read",
    ]
}
```

### Open Shelf — [7:49]

```swift
struct OpenShelf: AppIntent {
    static var title: LocalizedStringResource = "Open Shelf"

    @Parameter(title: "Shelf")
    var shelf: Shelf

    @MainActor
    func perform() async throws -> some IntentResult {
        Navigator.shared.openShelf(shelf)
        return .result()
    }

    static var parameterSummary: some ParameterSummary {
        Summary("Open \(\.$shelf)")
    }

    static var openAppWhenRun: Bool = true
}
```

### Book Entity — [10:56]

```swift
struct BookEntity: AppEntity, Identifiable {
    var id: UUID

    var displayRepresentation: DisplayRepresentation { "\(title)" }

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Book"

    static var defaultQuery = BookQuery()
}
```

### Book Query — [12:29]

```swift
struct BookQuery: EntityQuery {
    func entities(for identifiers: [UUID]) async throws -> [BookEntity] {
        identifiers.compactMap { identifier in
            Database.shared.book(for: identifier)
        }
    }
}
```

### Open Book — [13:16]

```swift
struct OpenBook: AppIntent {
    @Parameter(title: "Book")
    var book: BookEntity

    static var title: LocalizedStringResource = "Open Book"

    static var openAppWhenRun = true

    @MainActor
    func perform() async throws -> some IntentResult {
        guard try await $book.requestConfirmation(for: book, dialog: "Are you sure you want to clear read state for \(book)?") else {
            return .result()
        }
        Navigator.shared.openBook(book)
        return .result()
    }

    static var parameterSummary: some ParameterSummary {
        Summary("Open \(\.$book)")
    }

    init() {}

    init(book: BookEntity) {
        self.book = book
    }
}
```

### Suggested Entities and String Book Query — [13:40]

```swift
struct BookQuery: EntityStringQuery {
    func entities(for identifiers: [UUID]) async throws -> [BookEntity] {
        identifiers.compactMap { identifier in
            Database.shared.book(for: identifier)
        }
    }

    func suggestedEntities() async throws -> [BookEntity] {
        Database.shared.books
    }

    func entities(matching string: String) async throws -> [BookEntity] {
        Database.shared.books.filter { book in
            book.title.lowercased().contains(string.lowercased())
        }
    }
}
```

### Add Book Intent — [15:11]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult & ReturnsValue<BookEntity> & OpensIntent {
        guard var book = await BooksAPI.shared.findBooks(named: title, author: authorName).first else {
            throw Error.notFound
        }
        book.recommendedBy = recommendedBy
        Database.shared.add(book: book)

        return .result(
            value: book,
            openIntent: OpenBook(book: book)
        )
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Book Entity with Properties — [18:21]

```swift
struct BookEntity: AppEntity, Identifiable {
    var id: UUID

    @Property(title: "Title")
    var title: String

    @Property(title: "Publishing Date")
    var datePublished: Date

    @Property(title: "Read Date")
    var dateRead: Date?

    var recommendedBy: String?

    var displayRepresentation: DisplayRepresentation { "\(title)" }

    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Book"

    static var defaultQuery = BookQuery()

    init(id: UUID) {
        self.id = id
    }

    init(id: UUID, title: String) {
        self.id = id
        self.title = title
    }
}
```

### Books Property Query — [20:59]

```swift
struct BookQuery: EntityPropertyQuery {
    static var sortingOptions = SortingOptions {
        SortableBy(\BookEntity.$title)
        SortableBy(\BookEntity.$dateRead)
        SortableBy(\BookEntity.$datePublished)
    }

    static var properties = QueryProperties {
        Property(\BookEntity.$title) {
            EqualToComparator { NSPredicate(format: "title = %@", $0) }
            ContainsComparator { NSPredicate(format: "title CONTAINS %@", $0) }
        }
        Property(\BookEntity.$datePublished) {
            LessThanComparator { NSPredicate(format: "datePublished < %@", $0 as NSDate) }
            GreaterThanComparator { NSPredicate(format: "datePublished > %@", $0 as NSDate) }
        }
        Property(\BookEntity.$dateRead) {
            LessThanComparator { NSPredicate(format: "dateRead < %@", $0 as NSDate) }
            GreaterThanComparator { NSPredicate(format: "dateRead > %@", $0 as NSDate) }
        }
    }

    func entities(for identifiers: [UUID]) async throws -> [BookEntity] {
        identifiers.compactMap { identifier in
            Database.shared.book(for: identifier)
        }
    }

    func suggestedEntities() async throws -> [BookEntity] {
        Model.shared.library.books.map { BookEntity(id: $0.id, title: $0.title) }
    }

    func entities(matching string: String) async throws -> [BookEntity] {
        Database.shared.books.filter { book in
            book.title.lowercased().contains(string.lowercased())
        }
    }

    func entities(
        matching comparators: [NSPredicate],
        mode: ComparatorMode,
        sortedBy: [Sort<BookEntity>],
        limit: Int?
    ) async throws -> [BookEntity] {
        Database.shared.findBooks(matching: comparators, matchAll: mode == .and, sorts: sortedBy.map { (keyPath: $0.by, ascending: $0.order == .ascending) })
    }
}
```

### Dialog — [24:10]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult & ReturnsValue<BookEntity> & ProvidesDialog {
        guard var book = await BooksAPI.shared.findBooks(named: title, author: authorName).first else {
            throw Error.notFound
        }
        book.recommendedBy = recommendedBy
        Database.shared.add(book: book)

        return .result(
            value: book,
            dialog:"Added \(book) to Library!"
        )
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Snippet — [24:25]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult & ShowsSnippetView {
        guard var book = await BooksAPI.shared.findBooks(named: title, author: authorName).first else {
            throw Error.notFound
        }
        book.recommendedBy = recommendedBy
        Database.shared.add(book: book)

        return .result(value: book) {
            CoverView(book: book)
        }
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Request Value — [24:50]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult {
        let books = await BooksAPI.shared.findBooks(named: title, author: authorName)
        guard !books.isEmpty else {
            throw Error.notFound
        }
        if books.count > 1 && authorName == nil {
            throw $authorName.requestValue("Who wrote the book?")
        }

        return .result()
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Request Disambiguation — [25:22]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult {
        let books = await BooksAPI.shared.findBooks(named: title, author: authorName)
        guard !books.isEmpty else {
            throw Error.notFound
        }
        if books.count > 1 {
            let chosenAuthor = try await $authorName.requestDisambiguation(among: books.map { $0.authorName }, dialog: "Which author?")
        }
        return .result()
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Request Parameter Confirmation — [25:48]

```swift
struct AddBook: AppIntent {
    static var title: LocalizedStringResource = "Add Book"

    @Parameter(title: "Title")
    var title: String

    @Parameter(title: "Author Name")
    var authorName: String?

    @Parameter(title: "Recommended By")
    var recommendedBy: String?

    func perform() async throws -> some IntentResult & ReturnsValue<BookEntity> {
        guard var book = await BooksAPI.shared.findBooks(named: title, author: authorName).first else {
            throw Error.notFound
        }
        let confirmed = try await $title.requestConfirmation(for: book.title, dialog: "Did you mean \(book)?")
        book.recommendedBy = recommendedBy
        Database.shared.add(book: book)
        return .result(value: book)
    }

    enum Error: Swift.Error, CustomLocalizedStringResourceConvertible {
        case notFound

        var localizedStringResource: LocalizedStringResource {
            switch self {
                case .notFound: return "Book Not Found"
            }
        }
    }
}
```

### Request Result Confirmation — [26:26]

```swift
struct BuyBook: AppIntent {
    @Parameter(title: "Book")
    var book: BookEntity

    @Parameter(title: "Count")
    var count: Int

    static var title: LocalizedStringResource = "Buy Book"

    func perform() async throws -> some IntentResult & ShowsSnippetView & ProvidesDialog {
        let order = OrderEntity(book: book, count: count)
        try await requestConfirmation(output: .result(value: order, dialog: "Are you ready to order?") {
            OrderPreview(order: order)
        })

        return .result(value: order, dialog: "Thank you for your order!") {
            OrderConfirmation(order: order)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10032/6/69FD8F9D-5C29-4114-9C81-DF1ACC4B4BCA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10032/6/69FD8F9D-5C29-4114-9C81-DF1ACC4B4BCA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10032) — developer.apple.com. Indexed for agent consumption._
