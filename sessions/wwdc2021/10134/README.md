---
id: "wwdc2021-10134"
event: "wwdc2021"
year: 2021
title: "Explore structured concurrency in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10134"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore structured concurrency in Swift

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10134](https://developer.apple.com/videos/play/wwdc2021/10134)

When you have code that needs to run at the same time as other code, it’s important to choose the right tool for the job. We'll take you through the different kinds of concurrent tasks you can create in Swift, show you how to create groups of tasks, and find out how to cancel tasks in progress. We'll also provide guidance on when you may want to use unstructured tasks.

To get the most out of this session, we first recommend watching “Meet async/await in Swift.”

**Keywords:** `asyncdetached`, `async-let`, `bindings`, `detached`, `let`, `programming`, `scope`, `thumbnails`, `withtaskgroup`, `withthrowingtaskgroup`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,616 words)

## Documentation & Resources

- [SE-0317: async let](https://github.com/apple/swift-evolution/blob/main/proposals/0317-async-let.md) _documentation_
- [SE-0304: Structured concurrency](https://github.com/apple/swift-evolution/blob/main/proposals/0304-structured-concurrency.md) _documentation_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Asynchronous code with completion handlers is unstructured — [1:57]

```swift
func fetchThumbnails(
    for ids: [String],
    completion handler: @escaping ([String: UIImage]?, Error?) -> Void
) {
    guard let id = ids.first else { return handler([:], nil) }
    let request = thumbnailURLRequest(for: id)
    let dataTask = URLSession.shared.dataTask(with: request) { data, response, error in
        guard let response = response,
              let data = data
        else {
            return handler(nil, error)
        }
        // ... check response ...
        UIImage(data: data)?.prepareThumbnail(of: thumbSize) { image in
            guard let image = image else {
                return handler(nil, ThumbnailFailedError())
            }
            fetchThumbnails(for: Array(ids.dropFirst())) { thumbnails, error in
                // ... add image to thumbnails ...
            }
        }
    }
    dataTask.resume()
}
```

### Asynchronous code with async/await is structured — [2:56]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    for id in ids {
        let request = thumbnailURLRequest(for: id)
        let (data, response) = try await URLSession.shared.data(for: request)
        try validateResponse(response)
        guard let image = await UIImage(data: data)?.byPreparingThumbnail(ofSize: thumbSize) else {
            throw ThumbnailFailedError()
        }
        thumbnails[id] = image
    }
    return thumbnails
}
```

### Structured concurrency with async-let — [7:59]

```swift
func fetchOneThumbnail(withID id: String) async throws -> UIImage {
    let imageReq = imageRequest(for: id), metadataReq = metadataRequest(for: id)
    async let (data, _) = URLSession.shared.data(for: imageReq)
    async let (metadata, _) = URLSession.shared.data(for: metadataReq)
    guard let size = parseSize(from: try await metadata),
          let image = try await UIImage(data: data)?.byPreparingThumbnail(ofSize: size)
    else {
        throw ThumbnailFailedError()
    }
    return image
}
```

### Checking for cancellation by calling a method that throws — [11:46]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    for id in ids {
        try Task.checkCancellation()
        thumbnails[id] = try await fetchOneThumbnail(withID: id)
    }
    return thumbnails
}
```

### Obtaining the cancellation status of the current task — [12:16]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    for id in ids {
        if Task.isCancelled { break }
        thumbnails[id] = try await fetchOneThumbnail(withID: id)
    }
    return thumbnails
}
```

### Async-let is for concurrency with static width — [13:13]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    for id in ids {
        thumbnails[id] = try await fetchOneThumbnail(withID: id)
    }
    return thumbnails
}

func fetchOneThumbnail(withID id: String) async throws -> UIImage {
    // ...

    async let (data, _) = URLSession.shared.data(for: imageReq)
    async let (metadata, _) = URLSession.shared.data(for: metadataReq)

    // ...
}
```

### A task group is for concurrency with dynamic width — [13:58]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    try await withThrowingTaskGroup(of: Void.self) { group in
        for id in ids {
            group.async {
                // Error: Mutation of captured var 'thumbnails' in concurrently executing code
                thumbnails[id] = try await fetchOneThumbnail(withID: id)
            }
        }
    }
    return thumbnails
}
```

### Accessing the results of tasks within a group — [16:32]

```swift
func fetchThumbnails(for ids: [String]) async throws -> [String: UIImage] {
    var thumbnails: [String: UIImage] = [:]
    try await withThrowingTaskGroup(of: (String, UIImage).self) { group in
        for id in ids {
            group.async {
                return (id, try await fetchOneThumbnail(withID: id))
            }
        }
        // Obtain results from the child tasks, sequentially, in order of completion.
        for try await (id, thumbnail) in group {
            thumbnails[id] = thumbnail
        }
    }
    return thumbnails
}
```

### Creating an unstructured task — [20:39]

```swift
@MainActor
class MyDelegate: UICollectionViewDelegate {
    func collectionView(_ view: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt item: IndexPath) {
        let ids = getThumbnailIDs(for: item)
        Task {
            let thumbnails = await fetchThumbnails(for: ids)
            display(thumbnails, in: cell)
        }
    }
}
```

### Cancelling unstructured tasks — [22:11]

```swift
@MainActor
class MyDelegate: UICollectionViewDelegate {
    var thumbnailTasks: [IndexPath: Task<Void, Never>] = [:]

    func collectionView(_ view: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt item: IndexPath) {
        let ids = getThumbnailIDs(for: item)
        thumbnailTasks[item] = Task {
            defer { thumbnailTasks[item] = nil }
            let thumbnails = await fetchThumbnails(for: ids)
            display(thumbnails, in: cell)
        }
    }

    func collectionView(_ view: UICollectionView, didEndDisplay cell: UICollectionViewCell, forItemAt item: IndexPath) {
        thumbnailTasks[item]?.cancel()
    }
}
```

### Detaching a task — [24:09]

```swift
@MainActor
class MyDelegate: UICollectionViewDelegate {
    var thumbnailTasks: [IndexPath: Task<Void, Never>] = [:]

    func collectionView(_ view: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt item: IndexPath) {
        let ids = getThumbnailIDs(for: item)
        thumbnailTasks[item] = Task {
            defer { thumbnailTasks[item] = nil }
            let thumbnails = await fetchThumbnails(for: ids)
            Task.detached(priority: .background) {
                writeToLocalCache(thumbnails)
            }
            display(thumbnails, in: cell)
        }
    }
}
```

### Creating a task group inside a detached task — [24:57]

```swift
@MainActor
class MyDelegate: UICollectionViewDelegate {
    var thumbnailTasks: [IndexPath: Task<Void, Never>] = [:]

    func collectionView(_ view: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt item: IndexPath) {
        let ids = getThumbnailIDs(for: item)
        thumbnailTasks[item] = Task {
            defer { thumbnailTasks[item] = nil }
            let thumbnails = await fetchThumbnails(for: ids)
            Task.detached(priority: .background) {
                withTaskGroup(of: Void.self) { g in
                    g.async { writeToLocalCache(thumbnails) }
                    g.async { log(thumbnails) }
                    g.async { ... }
                }
            }
            display(thumbnails, in: cell)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10134/6/9155AF54-72F8-4BFA-BAB6-0B8830753666/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10134/6/9155AF54-72F8-4BFA-BAB6-0B8830753666/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10134) — developer.apple.com. Indexed for agent consumption._