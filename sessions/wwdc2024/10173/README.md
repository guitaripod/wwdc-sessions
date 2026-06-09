---
id: "wwdc2024-10173"
event: "wwdc2024"
year: 2024
title: "Analyze heap memory"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10173"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Analyze heap memory

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10173](https://developer.apple.com/videos/play/wwdc2024/10173)

Dive into the basis for your app’s dynamic memory: the heap! Explore how to use Instruments and Xcode to measure, analyze, and fix common heap issues. We’ll also cover some techniques and best practices for diagnosing transient growth, persistent growth, and leaks in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,769 words)

## Documentation & Resources

- [The Swift Programming Language: Automatic Reference Counting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) _documentation_
- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010

## Code Snippets

### ThumbnailLoader.makeThumbnail(from:) implementation — [10:01]

```swift
func makeThumbnail(from photoURL: URL) -> PhotoThumbnail {
  validate(url: photoURL)
  var coreImage = CIImage(contentsOf: photoURL)!

  let sepiaTone = CIFilter.sepiaTone()
  sepiaTone.inputImage = coreImage
  sepiaTone.intensity = 0.4
  coreImage = sepiaTone.outputImage!

  let squareSize = min(coreImage.extent.width, coreImage.extent.height)
  coreImage = coreImage.cropped(to: CGRect(x: 0, y: 0, width: squareSize, height: squareSize))

  let targetSize = CGSize(width:64, height:64)
  let scalingFilter = CIFilter.lanczosScaleTransform()

  scalingFilter.inputImage = coreImage
  scalingFilter.scale = Float(targetSize.height / coreImage.extent.height)
  scalingFilter.aspectRatio = Float(Double(coreImage.extent.width) / Double(coreImage.extent.height))
  coreImage = scalingFilter.outputImage!

  let imageData = context.generateImageData(of: coreImage)

  return PhotoThumbnail(size: targetSize, data: imageData, url: photoURL)
}
```

### ThumbnailLoader.loadThumbnails(with:), with autorelease pool growth issues — [10:23]

```swift
func loadThumbnails(with renderer: ThumbnailRenderer) {
  for photoURL in urls {
    renderer.faultThumbnail(from: photoURL)
  }
}
```

### Simple autorelease example — [10:33]

```swift
print("Now is \(Date.now)") // Produces autoreleased .description String
```

### Autorelease pool growth in loop — [11:08]

```swift
autoreleasepool {
  // ...

  for _ in 1...1000 {
    // Autoreleases into single pool, causing growth as loop runs
    print("Now is \(Date.now)")
  }

  // ...
}
```

### Autorelease pool growth in loop, managed by nested pool — [11:50]

```swift
autoreleasepool {
  // ...

  for _ in 1...1000 {
    autoreleasepool {
      // Autoreleases into nested pool, preventing outer pool from bloating
      print("Now is \(Date.now)")
    }
  }

  // ...
}
```

### ThumbnailLoader.loadThumbnails(with:), with nested autorelease pool growth issues fixed — [12:16]

```swift
func loadThumbnails(with renderer: ThumbnailRenderer) {
    for photoURL in urls {
        autoreleasepool {
            renderer.faultThumbnail(from: photoURL)
        }
    }
}
```

### C++ class with virtual method — [17:27]

```cpp
class Coconut {
  Swallow *swallow;
  virtual void virtualMethod() {}
};
```

### C++ class without virtual method — [17:40]

```cpp
class Coconut {
  Swallow *swallow;
};
```

### ThumbnailRenderer.faultThumbnail(from:), caching thumbnails incorrectly — [18:41]

```swift
func faultThumbnail(from photoURL: URL) {
  // Cache the thumbnail based on url + creationDate
  let timestamp = UInt64(Date.now.timeIntervalSince1970) // Bad - caching with wrong timestamp
  let cacheKey = CacheKey(url: photoURL, timestamp: timestamp)

  let thumbnail = cacheProvider.thumbnail(for: cacheKey) {
    return makeThumbnail(from: photoURL)
  }
  images.append(thumbnail.image)
}
```

### ThumbnailRenderer.faultThumbnail(from:), caching thumbnails correctly — [19:28]

```swift
func faultThumbnail(from photoURL: URL) {
  // Cache the thumbnail based on url + creationDate
  let timestamp = cacheKeyTimestamp(for: photoURL) // Fixed - caching with correct timestamp
  let cacheKey = CacheKey(url: photoURL, timestamp: timestamp)

  let thumbnail = cacheProvider.thumbnail(for: cacheKey) {
    return makeThumbnail(from: photoURL)
  }
  images.append(thumbnail.image)
}
```

### Code creating reference cycle with closure context — [22:19]

```swift
let swallow = Swallow()
swallow.completion = {
  print("\(swallow) finished carrying a coconut")
}
```

### PhotosView image loading code, with leak — [23:11]

```swift
// ...
let renderer = ThumbnailRenderer(style: .vibrant)
let loader = ThumbnailLoader(bundle: .main, completionQueue: .main)
loader.completionHandler = {
  self.thumbnails = renderer.images // implicit strong capture of renderer causes strong reference cycle
}
loader.beginLoading(with: renderer)
// ...
```

### PhotosView image loading code, with leak fixed — [23:40]

```swift
// ...
let renderer = ThumbnailRenderer(style: .vibrant)
let loader = ThumbnailLoader(bundle: .main, completionQueue: .main)
loader.completionHandler = { [weak renderer] in
	guard let renderer else { return }

  self.thumbnails = renderer.images
}
loader.beginLoading(with: renderer)
// ...
```

### Intentional leak of manually-managed allocation — [24:24]

```swift
let oops = UnsafeMutablePointer<Int>.allocate(capacity: 16)
// intentional mistake: missing `oops.deallocate()`
```

### Loop over intentional leak of manually-managed allocations — [25:12]

```swift
for _ in 0..<100 {
  let oops = UnsafeMutablePointer<Int>.allocate(capacity: 16)
  // intentional mistake: missing `oops.deallocate()`
}
```

### Nonreturning function which can see leaks of allocations owned by local variables — [26:11]

```swift
func beginServer() {
  let singleton = Server(delegate: self)
  dispatchMain() // __attribute__((noreturn))
}
```

### Fix for reported leak in nonreturning function — [26:22]

```swift
static var singleton: Server?

func beginServer() {
  Self.singleton = Server(delegate: self)
  dispatchMain()
}
```

### Weak reference example — [27:21]

```swift
weak var holder: Swallow?
```

### Unowned reference example — [27:43]

```swift
unowned let holder: Swallow
```

### Implicit use of self by method causes reference cycle — [29:07]

```swift
class ByteProducer {
  let data: Data
  private var generator: ((Data) -> UInt8)? = nil

  init(data: Data) {
    self.data = data
    generator = defaultAction // Implicitly uses `self`
  }

  func defaultAction(_ data: Data) -> UInt8 {
    // ...
  }
}
```

### Break reference cycle cause day implicit use of self by method, using weak — [29:25]

```swift
class ByteProducer {
  let data: Data
  private var generator: ((Data) -> UInt8)? = nil

  init(data: Data) {
    self.data = data
    generator = { [weak self] data in
      return self?.defaultAction(data)
    }
  }

  func defaultAction(_ data: Data) -> UInt8 {
    // ...
  }
}
```

### Break reference cycle cause day implicit use of self by method, using unowned — [29:41]

```swift
class ByteProducer {
  let data: Data
  private var generator: ((Data) -> UInt8)? = nil

  init(data: Data) {
    self.data = data
    generator = { [unowned self] data in
      return self.defaultAction(data)
    }
  }

  func defaultAction(_ data: Data) -> UInt8 {
    // ...
  }
}
```

### Struct with non-trivial init/copy/deinit — [31:14]

```swift
struct Nontrivial {
  var number: Int64
  var simple: CGPoint?
  var complex: String // Copy-on-write, requires non-trivial struct init/copy/destroy
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10173/4/5ADD00F7-AAD5-4C66-A3ED-9FC7E27C7720/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10173/4/5ADD00F7-AAD5-4C66-A3ED-9FC7E27C7720/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10173) — developer.apple.com. Indexed for agent consumption._