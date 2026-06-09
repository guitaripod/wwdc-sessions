---
id: "wwdc2025-268"
event: "wwdc2025"
year: 2025
title: "Embracing Swift concurrency"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/268"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Embracing Swift concurrency

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-268](https://developer.apple.com/videos/play/wwdc2025/268)

Join us to learn the core Swift concurrency concepts. Concurrency helps you improve app responsiveness and performance, and Swift is designed to make asynchronous and concurrent code easier to write correctly. We’ll cover the steps you need to take an app through from single-threaded to concurrent. We’ll also help you determine how and when to make the best use of Swift concurrency features – whether it’s making your code more asynchronous, moving it to the background, or sharing data across concurrent tasks.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,444 words)

## Documentation & Resources

- [Swift Migration Guide](https://www.swift.org/migration/documentation/migrationguide/) _documentation_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### Single-threaded program — [3:20]

```swift
var greeting = "Hello, World!"

func readArguments() { }

func greet() {
  print(greeting)
}

readArguments()
greet()
```

### Data types in a the app — [4:13]

```swift
struct Image {
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
}

final class Library {
  static let shared: Library = Library()
}
```

### Load and display a local image — [4:57]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) throws {
    let data = try Data(contentsOf: url)
    let image = decodeImage(data)
    view.displayImage(image)
  }

  func decodeImage(_ data: Data) -> Image {
    Image()
  }
}

final class Library {
  static let shared: Library = Library()
}
```

### Fetch and display an image over the network — [5:36]

```swift
import Foundation

struct Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) throws {
    let (data, _) = try URLSession.shared.data(from: url)
    let image = decodeImage(data)
    view.displayImage(image)
  }

  func decodeImage(_ data: Data) -> Image {
    Image()
  }
}

final class Library {
  static let shared: Library = Library()
}
```

### Fetch and display image over the network asynchronously — [6:10]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = decodeImage(data)
    view.displayImage(image)
  }

  func decodeImage(_ data: Data) -> Image {
    Image()
  }
}

final class Library {
  static let shared: Library = Library()
}
```

### Creating a task to perform asynchronous work — [7:31]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()
  var url: URL = URL("https://swift.org")!

  func onTapEvent() {
    Task {
      do {
	try await fetchAndDisplayImage(url: url)
      } catch let error {
        displayError(error)
      }
    }
  }

  func displayError(_ error: any Error) {
  }

  func fetchAndDisplayImage(url: URL) async throws {
  }
}

final class Library {
  static let shared: Library = Library()
}
```

### Ordered operations in a task — [9:15]

```swift
import Foundation

class Image {
  func applyImageEffect() async { }
}

final class ImageModel {
  func displayImage(_ image: Image) {
  }

  func loadImage() async -> Image {
    Image()
  }

  func onButtonTap() {
    Task {
      let image = await loadImage()
      await image.applyImageEffect()
      displayImage(image)
    }
  }
}
```

### Fetch and display image over the network asynchronously — [9:38]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = decodeImage(data)
    view.displayImage(image)
  }

  func decodeImage(_ data: Data) -> Image {
    Image()
  }
}
```

### Fetch and display image over the network asynchronously — [10:40]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = decodeImage(data, at: url)
    view.displayImage(image)
  }

  func decodeImage(_ data: Data, at url: URL) -> Image {
    Image()
  }
}
```

### Fetch over network asynchronously and decode concurrently — [11:11]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = await decodeImage(data, at: url)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data, at url: URL) async -> Image {
    Image()
  }
}
```

### Implementation of decodeImage — [11:30]

```swift
final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var cachedImage: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = await decodeImage(data, at: url)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data, at url: URL) async -> Image {
    if let image = cachedImage[url] {
      return image
    }

    // decode image
    let image = Image()
    cachedImage[url] = image
    return image
  }
}
```

### Correct implementation of fetchAndDisplayImage with caching and concurrency — [12:37]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var cachedImage: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    if let image = cachedImage[url] {
      view.displayImage(image)
      return
    }

    let (data, _) = try await URLSession.shared.data(from: url)
    let image = await decodeImage(data)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data) async -> Image {
    // decode image
    Image()
  }
}
```

### JSONDecoder API should be non isolated — [13:30]

```swift
// Foundation
import Foundation

nonisolated
public class JSONDecoder {
  public func decode<T: Decodable>(_ type: T.Type, from data: Data) -> T {
    fatalError("not implemented")
  }
}
```

### Fetch over network asynchronously and decode concurrently — [15:18]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = await decodeImage(data, at: url)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data, at url: URL) async -> Image {
    Image()
  }
}
```

### Example of value types — [16:30]

```swift
// Value types are common in Swift
import Foundation

struct Post {
  var author: String
  var title: String
  var date: Date
  var categories: [String]
}
```

### Sendable value types — [16:56]

```swift
import Foundation

// Value types are Sendable
extension URL: Sendable {}

// Collections of Sendable elements
extension Array: Sendable where Element: Sendable {}

// Structs and enums with Sendable storage
struct ImageRequest: Sendable {
  var url: URL
}

// Main-actor types are implicitly Sendable
@MainActor class ImageModel {}
```

### Fetch over network asynchronously and decode concurrently — [17:25]

```swift
import Foundation

class Image {
}

final class View {
  func displayImage(_ image: Image) {
  }
}

final class ImageModel {
  var imageCache: [URL: Image] = [:]
  let view = View()

  func fetchAndDisplayImage(url: URL) async throws {
    let (data, _) = try await URLSession.shared.data(from: url)
    let image = await self.decodeImage(data, at: url)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data, at url: URL) async -> Image {
    Image()
  }
}
```

### MyImage class with reference semantics — [18:34]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scale(by factor: Double) {
  }
}

let image = MyImage()
let otherImage = image // refers to the same object as 'image'
image.scale(by: 0.5)   // also changes otherImage!
```

### Concurrently scaling while displaying an image is a data race — [19:19]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scaleImage(by factor: Double) {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  // Slide content start
  func scaleAndDisplay(imageName: String) {
    let image = loadImage(imageName)
    Task { @concurrent in
      image.scaleImage(by: 0.5)
    }

    view.displayImage(image)
  }
  // Slide content end

  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Scaling and then displaying an image eliminates the data race — [20:38]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scaleImage(by factor: Double) {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  func scaleAndDisplay(imageName: String) {
    Task { @concurrent in
      let image = loadImage(imageName)
      image.scaleImage(by: 0.5)
      await view.displayImage(image)
    }
  }

  nonisolated
  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Scaling and then displaying an image within a concurrent asynchronous function — [20:54]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scaleImage(by factor: Double) {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  @concurrent
  func scaleAndDisplay(imageName: String) async {
    let image = loadImage(imageName)
    image.scaleImage(by: 0.5)
    await view.displayImage(image)
  }

  nonisolated
  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Scaling, then displaying and concurrently modifying an image is a data race — [21:11]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scaleImage(by factor: Double) {
  }

  func applyAnotherEffect() {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  // Slide content start
  @concurrent
  func scaleAndDisplay(imageName: String) async {
    let image = loadImage(imageName)
    image.scaleImage(by: 0.5)
    await view.displayImage(image)
    image.applyAnotherEffect()
  }
  // Slide content end

  nonisolated
  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Applying image transforms before sending to the main actor — [21:20]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scaleImage(by factor: Double) {
  }

  func applyAnotherEffect() {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  // Slide content start
  @concurrent
  func scaleAndDisplay(imageName: String) async {
    let image = loadImage(imageName)
    image.scaleImage(by: 0.5)
    image.applyAnotherEffect()
    await view.displayImage(image)
  }
  // Slide content end

  nonisolated
  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Closures create shared state — [22:06]

```swift
import Foundation

struct Color { }

nonisolated class MyImage {
  var width: Int
  var height: Int
  var pixels: [Color]
  var url: URL

  init() {
    width = 100
    height = 100
    pixels = []
    url = URL("https://swift.org")!
  }

  func scale(by factor: Double) {
  }

  func applyAnotherEffect() {
  }
}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()

  // Slide content start
  @concurrent
  func scaleAndDisplay(imageName: String) async throws {
    let image = loadImage(imageName)
    try await perform(afterDelay: 0.1) {
      image.scale(by: 0.5)
    }
    await view.displayImage(image)
  }

  nonisolated
  func perform(afterDelay delay: Double, body: () -> Void) async throws {
    try await Task.sleep(for: .seconds(delay))
    body()
  }
  // Slide content end

  nonisolated
  func loadImage(_ imageName: String) -> MyImage {
    // decode image
    return MyImage()
  }
}pet.
```

### Network manager class — [23:47]

```swift
import Foundation

nonisolated class MyImage { }

struct Connection {
  func data(from url: URL) async throws -> Data { Data() }
}

final class NetworkManager {
  var openConnections: [URL: Connection] = [:]

  func openConnection(for url: URL) async -> Connection {
    if let connection = openConnections[url] {
      return connection
    }

    let connection = Connection()
    openConnections[url] = connection
    return connection
  }

  func closeConnection(_ connection: Connection, for url: URL) async {
    openConnections.removeValue(forKey: url)
  }

}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()
  let networkManager: NetworkManager = NetworkManager()

  func fetchAndDisplayImage(url: URL) async throws {
    if let image = cachedImage[url] {
      view.displayImage(image)
      return
    }

    let connection = await networkManager.openConnection(for: url)
    let data = try await connection.data(from: url)
    await networkManager.closeConnection(connection, for: url)

    let image = await decodeImage(data)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data) async -> MyImage {
    // decode image
    return MyImage()
  }
}
```

### Network manager as an actor — [25:10]

```swift
import Foundation

nonisolated class MyImage { }

struct Connection {
  func data(from url: URL) async throws -> Data { Data() }
}

actor NetworkManager {
  var openConnections: [URL: Connection] = [:]

  func openConnection(for url: URL) async -> Connection {
    if let connection = openConnections[url] {
      return connection
    }

    let connection = Connection()
    openConnections[url] = connection
    return connection
  }

  func closeConnection(_ connection: Connection, for url: URL) async {
    openConnections.removeValue(forKey: url)
  }

}

final class View {
  func displayImage(_ image: MyImage) {
  }
}

final class ImageModel {
  var cachedImage: [URL: MyImage] = [:]
  let view = View()
  let networkManager: NetworkManager = NetworkManager()

  func fetchAndDisplayImage(url: URL) async throws {
    if let image = cachedImage[url] {
      view.displayImage(image)
      return
    }

    let connection = await networkManager.openConnection(for: url)
    let data = try await connection.data(from: url)
    await networkManager.closeConnection(connection, for: url)

    let image = await decodeImage(data)
    view.displayImage(image)
  }

  @concurrent
  func decodeImage(_ data: Data) async -> MyImage {
    // decode image
    return MyImage()
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/268/4/9de10aea-96a5-468d-a7b9-211a8f9b2d0a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/268/4/9de10aea-96a5-468d-a7b9-211a8f9b2d0a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/268) — developer.apple.com. Indexed for agent consumption._