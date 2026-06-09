---
id: "wwdc2021-10133"
event: "wwdc2021"
year: 2021
title: "Protect mutable state with Swift actors"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10133"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Protect mutable state with Swift actors

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10133](https://developer.apple.com/videos/play/wwdc2021/10133)

Data races occur when two separate threads concurrently access the same mutable state. They are trivial to construct, but are notoriously hard to debug. Discover how you can stop these data races in their tracks with Swift actors, which help synchronize access to data in your code. Discover how actors work and how to share values between them. Learn about how actor isolation affects protocol conformances. And finally, meet the main actor, a new way of ensuring that your code always runs on the main thread when needed. To get the most out of this session, we recommend first watching “Meet async/await in Swift.”

**Keywords:** `😸`, `😿`, `books`, `cache`, `cat`, `classes`, `counter`, `detached`, `equatable`, `global`, `hashable`, `immutable`, `isolated`, `isolation`, `libraryaccount`, `nonisolated`, `sad`, `sendable`, `synchronization`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,326 words)

## Documentation & Resources

- [SE-0316: Global actors](https://github.com/apple/swift-evolution/blob/main/proposals/0316-global-actors.md) _documentation_
- [SE-0313: Improved control over actor isolation](https://github.com/apple/swift-evolution/blob/main/proposals/0313-actor-isolation-control.md) _documentation_
- [SE-0306: Actors](https://github.com/apple/swift-evolution/blob/main/proposals/0306-actors.md) _documentation_
- [SE-0302: Sendable and @Sendable closures](https://github.com/apple/swift-evolution/blob/main/proposals/0302-concurrent-value-and-concurrent-closures.md) _documentation_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Data races make concurrency hard — [0:42]

```swift
class Counter {
    var value = 0

    func increment() -> Int {
        value = value + 1
        return value
    }
}

let counter = Counter()

Task.detached {
    print(counter.increment()) // data race
}

Task.detached {
    print(counter.increment()) // data race
}
```

### Value semantics help eliminate data races — [2:20]

```swift
var array1 = [1, 2]
var array2 = array1

array1.append(3)
array2.append(4)

print(array1)        // [1, 2, 3]
print(array2)        // [1, 2, 4]
```

### Sometimes shared mutable state is required — [2:59]

```swift
struct Counter {
    var value = 0

    mutating func increment() -> Int {
        value = value + 1
        return value
    }
}

let counter = Counter()

Task.detached {
    var counter = counter
    print(counter.increment()) // always prints 1
}

Task.detached {
    var counter = counter
    print(counter.increment()) // always prints 1
}
```

### Actor isolation prevents unsynchronized access — [5:23]

```swift
actor Counter {
    var value = 0

    func increment() -> Int {
        value = value + 1
        return value
    }
}

let counter = Counter()

Task.detached {
    print(await counter.increment())
}

Task.detached {
    print(await counter.increment())
}
```

### Synchronous interation within an actor — [7:51]

```swift
extension Counter {
    func resetSlowly(to newValue: Int) {
        value = 0
        for _ in 0..<newValue {
            increment()
        }
        assert(value == newValue)
    }
}
```

### Check your assumptions after an await: The sad cat — [9:02]

```swift
actor ImageDownloader {
    private var cache: [URL: Image] = [:]

    func image(from url: URL) async throws -> Image? {
        if let cached = cache[url] {
            return cached
        }

        let image = try await downloadImage(from: url)

        // Potential bug: `cache` may have changed.
        cache[url] = image
        return image
    }
}
```

### Check your assumptions after an await: One solution — [11:50]

```swift
actor ImageDownloader {
    private var cache: [URL: Image] = [:]

    func image(from url: URL) async throws -> Image? {
        if let cached = cache[url] {
            return cached
        }

        let image = try await downloadImage(from: url)

        // Replace the image only if it is still missing from the cache.
        cache[url] = cache[url, default: image]
        return cache[url]
    }
}
```

### Check your assumptions after an await: A better solution — [11:59]

```swift
actor ImageDownloader {

    private enum CacheEntry {
        case inProgress(Task<Image, Error>)
        case ready(Image)
    }

    private var cache: [URL: CacheEntry] = [:]

    func image(from url: URL) async throws -> Image? {
        if let cached = cache[url] {
            switch cached {
            case .ready(let image):
                return image
            case .inProgress(let task):
                return try await task.value
            }
        }

        let task = Task {
            try await downloadImage(from: url)
        }

        cache[url] = .inProgress(task)

        do {
            let image = try await task.value
            cache[url] = .ready(image)
            return image
        } catch {
            cache[url] = nil
            throw error
        }
    }
}
```

### Protocol conformance: Static declarations are outside the actor — [13:30]

```swift
actor LibraryAccount {
    let idNumber: Int
    var booksOnLoan: [Book] = []
}

extension LibraryAccount: Equatable {
    static func ==(lhs: LibraryAccount, rhs: LibraryAccount) -> Bool {
        lhs.idNumber == rhs.idNumber
    }
}
```

### Protocol conformance: Non-isolated declarations are outside the actor — [14:15]

```swift
actor LibraryAccount {
    let idNumber: Int
    var booksOnLoan: [Book] = []
}

extension LibraryAccount: Hashable {
    nonisolated func hash(into hasher: inout Hasher) {
        hasher.combine(idNumber)
    }
}
```

### Closures can be isolated to the actor — [15:32]

```swift
extension LibraryAccount {
    func readSome(_ book: Book) -> Int { ... }

    func read() -> Int {
        booksOnLoan.reduce(0) { book in
            readSome(book)
        }
    }
}
```

### Closures executed in a detached task are not isolated to the actor — [16:29]

```swift
extension LibraryAccount {
    func readSome(_ book: Book) -> Int { ... }
    func read() -> Int { ... }

    func readLater() {
        Task.detached {
            await read()
        }
    }
}
```

### Passing data into and out of actors: structs — [17:15]

```swift
actor LibraryAccount {
    let idNumber: Int
    var booksOnLoan: [Book] = []
    func selectRandomBook() -> Book? { ... }
}

struct Book {
    var title: String
    var authors: [Author]
}

func visit(_ account: LibraryAccount) async {
    guard var book = await account.selectRandomBook() else {
        return
    }
    book.title = "\(book.title)!!!" // OK: modifying a local copy
}
```

### Passing data into and out of actors: classes — [17:39]

```swift
actor LibraryAccount {
    let idNumber: Int
    var booksOnLoan: [Book] = []
    func selectRandomBook() -> Book? { ... }
}

class Book {
    var title: String
    var authors: [Author]
}

func visit(_ account: LibraryAccount) async {
    guard var book = await account.selectRandomBook() else {
        return
    }
    book.title = "\(book.title)!!!" // Not OK: potential data race
}
```

### Check Sendable by adding a conformance — [20:08]

```swift
struct Book: Sendable {
    var title: String
    var authors: [Author]
}
```

### Propagate Sendable by adding a conditional conformance — [20:43]

```swift
struct Pair<T, U> {
    var first: T
    var second: U
}

extension Pair: Sendable where T: Sendable, U: Sendable {
}
```

### Interacting with the main thread: Using a DispatchQueue — [24:19]

```swift
func checkedOut(_ booksOnLoan: [Book]) {
    booksView.checkedOutBooks = booksOnLoan
}

// Dispatching to the main queue is your responsibility.
DispatchQueue.main.async {
    checkedOut(booksOnLoan)
}
```

### Interacting with the main thread: The main actor — [25:01]

```swift
@MainActor func checkedOut(_ booksOnLoan: [Book]) {
    booksView.checkedOutBooks = booksOnLoan
}

// Swift ensures that this code is always run on the main thread.
await checkedOut(booksOnLoan)
```

### Main actor types — [26:21]

```swift
@MainActor class MyViewController: UIViewController {
    func onPress(...) { ... } // implicitly @MainActor

    nonisolated func fetchLatestAndDisplay() async { ... } 
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10133/5/C303A256-7F2C-401E-9986-E877F8C7525E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10133/5/C303A256-7F2C-401E-9986-E877F8C7525E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10133) — developer.apple.com. Indexed for agent consumption._
