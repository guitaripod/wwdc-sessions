---
id: "wwdc2021-10254"
event: "wwdc2021"
year: 2021
title: "Swift concurrency: Behind the scenes"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10254"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Swift concurrency: Behind the scenes

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10254](https://developer.apple.com/videos/play/wwdc2021/10254)

Dive into the details of Swift concurrency and discover how Swift provides greater safety from data races and thread explosion while simultaneously improving performance. We’ll explore how Swift tasks differ from Grand Central Dispatch, how the new cooperative threading model works, and how to ensure the best performance for your apps.

To get the most out of this session, we recommend first watching “Meet async/await in Swift,” “Explore structured concurrency in Swift,” and “Protect mutable state with Swift actors.”

**Keywords:** `actors`, `async`, `await`, `continuation`, `dispatchqueue`, `feed`, `gcd`, `heap`, `hopping`, `newsfeed`, `pool`, `queue`, `reader`, `stack`, `threads`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,629 words)

## Documentation & Resources

- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### GCD code with hidden performance pitfalls — [4:57]

```swift
func deserializeArticles(from data: Data) throws -> [Article] { /* ... */ }
func updateDatabase(with articles: [Article], for feed: Feed) { /* ... */ }

let urlSession = URLSession(configuration: .default, delegate: self, delegateQueue: concurrentQueue)

for feed in feedsToUpdate {
    let dataTask = urlSession.dataTask(with: feed.url) { data, response, error in
        // ...
        guard let data = data else { return }
        do {
            let articles = try deserializeArticles(from: data)
            databaseQueue.sync {
                updateDatabase(with: articles, for: feed)
            }
        } catch { /* ... */ }
    }
    dataTask.resume()
}
```

### Swift concurrency equivalent using a task group — [13:18]

```swift
func deserializeArticles(from data: Data) throws -> [Article] { /* ... */ }
func updateDatabase(with articles: [Article], for feed: Feed) async { /* ... */ }

await withThrowingTaskGroup(of: [Article].self) { group in
    for feed in feedsToUpdate {
        group.async {
            let (data, response) = try await URLSession.shared.data(from: feed.url)
            // ...
            let articles = try deserializeArticles(from: data)
            await updateDatabase(with: articles, for: feed)
            return articles
        }
    }
}
```

### Async functions: stack frames and async frames — [15:16]

```swift
// on Database
func save(_ newArticles: [Article], for feed: Feed) async throws -> [ID] { /* ... */ }

// on Feed
func add(_ newArticles: [Article]) async throws {
    let ids = try await database.save(newArticles, for: self)
    for (id, article) in zip(ids, newArticles) {
        articles[id] = article
    }
}

func updateDatabase(with articles: [Article], for feed: Feed) async throws {
    // skip old articles ...
    try await feed.add(articles)
}
```

### Excessive context switching due to Main actor hoppping — [37:13]

```swift
// on database actor
func loadArticle(with id: ID) async throws -> Article { /* ... */ }

@MainActor func updateUI(for article: Article) async { /* ... */ }

@MainActor func updateArticles(for ids: [ID]) async throws {
    for id in ids {
        let article = try await database.loadArticle(with: id)
        await updateUI(for: article)
    }
}
```

### Batch UI work to reduce the number of context switches — [38:18]

```swift
// on database actor
func loadArticles(with ids: [ID]) async throws -> [Article]

@MainActor func updateUI(for articles: [Article]) async

@MainActor func updateArticles(for ids: [ID]) async throws {
    let articles = try await database.loadArticles(with: ids)
    await updateUI(for: articles)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10254/5/3F33D18D-8193-437C-A413-0281E15A1DDA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10254/5/3F33D18D-8193-437C-A413-0281E15A1DDA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10254) — developer.apple.com. Indexed for agent consumption._