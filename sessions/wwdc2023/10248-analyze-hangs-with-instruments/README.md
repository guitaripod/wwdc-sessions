---
id: "wwdc2023-10248"
event: "wwdc2023"
year: 2023
title: "Analyze hangs with Instruments"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10248"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Analyze hangs with Instruments

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10248](https://developer.apple.com/videos/play/wwdc2023/10248)

User interface elements often mimic real-world interactions, including real-time responses. Apps with a noticeable delay in user interaction — a hang — can break that illusion and create frustration. We’ll show you how to use Instruments to analyze, understand, and fix hangs in your apps on all Apple platforms. Discover how you can efficiently navigate an Instruments trace document, interpret trace data, and record additional profiling data to better understand your specific hang. If you aren’t familiar with using Instruments, we recommend first watching "Getting Started with Instruments." And to learn about other tools that can help you discover hangs in your app, check out "Track down hangs with Xcode and on-device detection."

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,758 words)

## Documentation & Resources

- [Analyzing responsiveness issues in your shipping app](https://developer.apple.com/documentation/Xcode/analyzing-responsiveness-issues-in-your-shipping-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/analyzing-responsiveness-issues-in-your-shipping-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/analyzing-responsiveness-issues-in-your-shipping-app.json
- [Improving app responsiveness](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/improving-app-responsiveness
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/improving-app-responsiveness.json

## Code Snippets

### BackgroundThumbnailView — [19:38]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground

    var body: some View {
        Image(uiImage: background.thumbnail)
    }
}
```

### BackgroundSelectionView with Grid — [19:58]

```swift
var body: some View {
        ScrollView {
            Grid {
                ForEach(backgroundsGrid) { row in
                    GridRow {
                        ForEach(row.items) { background in
                            BackgroundThumbnailView(background: background)
                                .onTapGesture {
                                    selectedBackground = background
                                }
                        }
                    }
                }
            }
        }
    }
```

### BackgroundSelectionView with Grid (simplified) — [20:03]

```swift
var body: some View {
    ScrollView {
        Grid {
            ForEach(backgroundsGrid) { row in
                GridRow {
                    ForEach(row.items) { background in
                        BackgroundThumbnailView(background: background)
                    }
                }
            }
        }
    }
}
```

### LazyVGrid variant — [20:26]

```swift
var body: some View {
    ScrollView {
        LazyVGrid(columns: [.init(.adaptive(minimum: BackgroundThumbnailView.thumbnailSize.width))]) {
            ForEach(BackyardBackground.allBackgrounds) { background in
                BackgroundThumbnailView(background: background)
            }
        }
    }
}
```

### BackgroundThumbnailView — [24:05]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground

    var body: some View {
        Image(uiImage: background.thumbnail)
    }
}
```

### BackgroundThumbnailView with progress (but without loading) — [24:59]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground
    @State private var image: UIImage?

    var body: some View {
        if let image {
            Image(uiImage: image)
        } else {
            ProgressView()
                .frame(width: Self.thumbnailSize.width, height: Self.thumbnailSize.height, alignment: .center)
        }
    }
}
```

### BackgroundThumbnailView with async loading on main thread — [25:26]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground
    @State private var image: UIImage?

    var body: some View {
        if let image {
            Image(uiImage: image)
        } else {
            ProgressView()
                .frame(width: Self.thumbnailSize.width, height: Self.thumbnailSize.height, alignment: .center)
                .task {
                    image = background.thumbnail
                }
        }
    }
}
```

### BackgroundThumbnailView with async loading on main thread — [29:59]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground
    @State private var image: UIImage?

    var body: some View {
        if let image {
            Image(uiImage: image)
        } else {
            ProgressView()
                .frame(width: Self.thumbnailSize.width, height: Self.thumbnailSize.height, alignment: .center)
                .task {
                    image = background.thumbnail
                }
        }
    }
}
```

### BackgroundThumbnailView with async loading on main thread (simplified) — [31:41]

```swift
struct BackgroundThumbnailView: View {
    // [...]

    var body: some View {
        // [...]
        ProgressView()
            .task {
                image = background.thumbnail
            }
        // [...]
    }
}
```

### BackgroundThumbnailView with async loading on main thread — [33:40]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground
    @State private var image: UIImage?

    var body: some View {
        if let image {
            Image(uiImage: image)
        } else {
            ProgressView()
                .frame(width: Self.thumbnailSize.width, height: Self.thumbnailSize.height, alignment: .center)
                .task {
                    image = background.thumbnail
                }
        }
    }
}
```

### synchronous thumbnail property — [33:59]

```swift
public var thumbnail: UIImage {
    get {
        // compute and cache thumbnail
    }
}
```

### asynchronous thumbnail property — [34:03]

```swift
public var thumbnail: UIImage {
    get async {
        // compute and cache thumbnail
    }
}
```

### BackgroundThumbnailView with async loading in background — [34:08]

```swift
struct BackgroundThumbnailView: View {
    static let thumbnailSize = CGSize(width:128, height:128)

    var background: BackyardBackground
    @State private var image: UIImage?

    var body: some View {
        if let image {
            Image(uiImage: image)
        } else {
            ProgressView()
                .frame(width: Self.thumbnailSize.width, height: Self.thumbnailSize.height, alignment: .center)
                .task {
                    image = await background.thumbnail
                }
        }
    }
}
```

### shared property causes blocked main thread — [38:52]

```swift
var body: some View {
    mainContent
        .task(id: imageMode) {
            defer {
                loading = false
            }
            do {
                var image = await background.thumbnail
                if imageMode == .colorized {
                    let colorizer = ColorizingService.shared
                    image = try await colorizer.colorize(image)
                }
                self.image = image
            } catch {
                self.error = error
            }
        }
}
```

### shared property causes blocked main thread (simplified) — [39:00]

```swift
struct ImageTile: View {
    // [...]

    // implicit @MainActor
    var body: some View {
        mainContent
            .task() { // inherits @MainActor isolation
                // [...]
                let colorizer = ColorizingService.shared
                result = try await colorizer.colorize(image)
            }
    }
}
```

### shared property causes blocked main thread + ColorizingService (simplified) — [39:10]

```swift
class ColorizingService {
    static let shared = ColorizingService()


    // [...]
}

struct ImageTile: View {
    // [...]

    // implicit @MainActor
    var body: some View {
        mainContent
            .task() { // inherits @MainActor isolation
                // [...]
                let colorizer = ColorizingService.shared
                result = try await colorizer.colorize(image)
            }
    }
}
```

### shared synchronous property after await keyword still causes blocked main thread — [39:25]

```swift
class ColorizingService {
    static let shared = ColorizingService()


    // [...]
}

struct ImageTile: View {
    // [...]

    // implicit @MainActor
    var body: some View {
        mainContent
            .task() { // inherits @MainActor isolation
                // [...]
                result = try await ColorizingService.shared.colorize(image)
            }
    }
}
```

### shared synchronous property after await keyword still causes blocked main thread (+colorize function) — [39:39]

```swift
class ColorizingService {
    static let shared = ColorizingService()

    func colorize(_ grayscaleImage: CGImage) async throws -> CGImage
    // [...]
}

struct ImageTile: View {
    // [...]

    // implicit @MainActor
    var body: some View {
        mainContent
            .task() { // inherits @MainActor isolation
                // [...]
                result = try await ColorizingService.shared.colorize(image)
            }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10248/6/AB6FF62D-3A9D-4816-95E8-2E7B464CA1DF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10248/6/AB6FF62D-3A9D-4816-95E8-2E7B464CA1DF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10248) — developer.apple.com. Indexed for agent consumption._
