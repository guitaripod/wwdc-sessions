---
id: "wwdc2021-10132"
event: "wwdc2021"
year: 2021
title: "Meet async/await in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10132"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet async/await in Swift

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10132](https://developer.apple.com/videos/play/wwdc2021/10132)

Swift now supports asynchronous functions — a pattern commonly known as async/await. Discover how the new syntax can make your code easier to read and understand. Learn what happens when a function suspends, and find out how to adapt existing completion handlers to asynchronous functions.

**Keywords:** `await`, `bypreparingthumbnail`, `completionhandler`, `continuation`, `datatask`, `expectation`, `preparethumbnail`, `preparingthumbnail`, `resume`, `suspension`, `testing`, `urlsession`, `withcheckedcontinuation`, `withcheckedthrowingcontinuation`, `xctestexpectation`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,956 words)

## Documentation & Resources

- [SE-0310: Effectful read-only properties](https://github.com/apple/swift-evolution/blob/main/proposals/0310-effectful-readonly-properties.md) _documentation_
- [SE-0300: Continuations for interfacing async tasks with synchronous code](https://github.com/apple/swift-evolution/blob/main/proposals/0300-continuation.md) _documentation_
- [SE-0297: Concurrency Interoperability with Objective-C](https://github.com/apple/swift-evolution/blob/main/proposals/0297-concurrency-objc.md) _documentation_
- [SE-0296: Async/await](https://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md) _documentation_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Writing a function using completion handlers — [3:43]

```swift
func fetchThumbnail(for id: String, completion: @escaping (UIImage?, Error?) -> Void) {
    let request = thumbnailURLRequest(for: id)
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        if let error = error {
            completion(nil, error)
        } else if (response as? HTTPURLResponse)?.statusCode != 200 {
            completion(nil, FetchError.badID)
        } else {
            guard let image = UIImage(data: data!) else {
                completion(nil, FetchError.badImage)
                return
            }
            image.prepareThumbnail(of: CGSize(width: 40, height: 40)) { thumbnail in
                guard let thumbnail = thumbnail else {
                    completion(nil, FetchError.badImage)
                    return
                }
                completion(thumbnail, nil)
            }
        }
    }
    task.resume()
}
```

### Using completion handlers with the Result type — [8:00]

```swift
func fetchThumbnail(for id: String, completion: @escaping (Result<UIImage, Error>) -> Void) {
    let request = thumbnailURLRequest(for: id)
    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        if let error = error {
            completion(.failure(error))
        } else if (response as? HTTPURLResponse)?.statusCode != 200 {
            completion(.failure(FetchError.badID))
        } else {
            guard let image = UIImage(data: data!) else {
                completion(.failure(FetchError.badImage))
                return
            }
            image.prepareThumbnail(of: CGSize(width: 40, height: 40)) { thumbnail in
                guard let thumbnail = thumbnail else {
                    completion(.failure(FetchError.badImage))
                    return
                }
                completion(.success(thumbnail))
            }
        }
    }
    task.resume()
}
```

### Using async/await — [8:30]

```swift
func fetchThumbnail(for id: String) async throws -> UIImage {
    let request = thumbnailURLRequest(for: id)  
    let (data, response) = try await URLSession.shared.data(for: request)
    guard (response as? HTTPURLResponse)?.statusCode == 200 else { throw FetchError.badID }
    let maybeImage = UIImage(data: data)
    guard let thumbnail = await maybeImage?.thumbnail else { throw FetchError.badImage }
    return thumbnail
}
```

### Async properties — [13:15]

```swift
extension UIImage {
    var thumbnail: UIImage? {
        get async {
            let size = CGSize(width: 40, height: 40)
            return await self.byPreparingThumbnail(ofSize: size)
        }
    }
}
```

### Async sequences — [14:17]

```swift
for await id in staticImageIDsURL.lines {
    let thumbnail = await fetchThumbnail(for: id)
    collage.add(thumbnail)
}
let result = await collage.draw()
```

### Testing using XCTestExpectation — [21:22]

```swift
class MockViewModelSpec: XCTestCase {
    func testFetchThumbnails() throws {
        let expectation = XCTestExpectation(description: "mock thumbnails completion")
        self.mockViewModel.fetchThumbnail(for: mockID) { result, error in
            XCTAssertNil(error)
            expectation.fulfill()
        }
        wait(for: [expectation], timeout: 5.0)
    }
}
```

### Testing using async/await — [21:56]

```swift
class MockViewModelSpec: XCTestCase {
    func testFetchThumbnails() async throws {
        XCTAssertNoThrow(try await self.mockViewModel.fetchThumbnail(for: mockID))
    }
}
```

### Bridging from sync to async — [22:30]

```swift
struct ThumbnailView: View {
    @ObservedObject var viewModel: ViewModel
    var post: Post
    @State private var image: UIImage?

    var body: some View {
        Image(uiImage: self.image ?? placeholder)
            .onAppear {
                Task {
                    self.image = try? await self.viewModel.fetchThumbnail(for: post.id)
                }
            }
    }
}
```

### Async APIs in the SDK — [25:56]

```swift
import ClockKit

extension ComplicationController: CLKComplicationDataSource {
    func currentTimelineEntry(for complication: CLKComplication) async -> CLKComplicationTimelineEntry? {
        let date = Date()
        let thumbnail = try? await self.viewModel.fetchThumbnail(for: post.id)
        guard let thumbnail = thumbnail else {
            return nil
        }

        let entry = self.createTimelineEntry(for: thumbnail, date: date)
        return entry
    }
}
```

### Async alternatives and continuations — [26:59]

```swift
// Existing function
func getPersistentPosts(completion: @escaping ([Post], Error?) -> Void) {       
    do {
        let req = Post.fetchRequest()
        req.sortDescriptors = [NSSortDescriptor(key: "date", ascending: true)]
        let asyncRequest = NSAsynchronousFetchRequest<Post>(fetchRequest: req) { result in
            completion(result.finalResult ?? [], nil)
        }
        try self.managedObjectContext.execute(asyncRequest)
    } catch {
        completion([], error)
    }
}

// Async alternative
func persistentPosts() async throws -> [Post] {       
    typealias PostContinuation = CheckedContinuation<[Post], Error>
    return try await withCheckedThrowingContinuation { (continuation: PostContinuation) in
        self.getPersistentPosts { posts, error in
            if let error = error { 
                continuation.resume(throwing: error) 
            } else {
                continuation.resume(returning: posts)
            }
        }
    }
}
```

### Storing the continuation for delegate callbacks — [31:44]

```swift
class ViewController: UIViewController {
    private var activeContinuation: CheckedContinuation<[Post], Error>?
    func sharedPostsFromPeer() async throws -> [Post] {
        try await withCheckedThrowingContinuation { continuation in
            self.activeContinuation = continuation
            self.peerManager.syncSharedPosts()
        }
    }
}

extension ViewController: PeerSyncDelegate {
    func peerManager(_ manager: PeerManager, received posts: [Post]) {
        self.activeContinuation?.resume(returning: posts)
        self.activeContinuation = nil // guard against multiple calls to resume
    }

    func peerManager(_ manager: PeerManager, hadError error: Error) {
        self.activeContinuation?.resume(throwing: error)
        self.activeContinuation = nil // guard against multiple calls to resume
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10132/5/33A0E99C-1E53-4143-8A63-809D2E6CBA66/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10132/5/33A0E99C-1E53-4143-8A63-809D2E6CBA66/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10132) — developer.apple.com. Indexed for agent consumption._