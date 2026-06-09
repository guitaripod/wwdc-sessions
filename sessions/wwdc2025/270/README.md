---
id: "wwdc2025-270"
event: "wwdc2025"
year: 2025
title: "Code-along: Elevate an app with Swift concurrency"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/270"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Code-along: Elevate an app with Swift concurrency

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-270](https://developer.apple.com/videos/play/wwdc2025/270)

Learn how to optimize your app’s user experience with Swift concurrency as we update an existing sample app. We’ll start with a main-actor app, then gradually introduce asynchronous code as we need to. We’ll use tasks to optimize code running on the main actor, and discover how to parallelize code by offloading work to the background. We’ll explore what data-race safety provides, and work through interpreting and fixing data-race safety errors. Finally, we’ll show how you can make the most out of structured concurrency in the context of an app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,975 words)

## Documentation & Resources

- [Code-along: Elevating an app with Swift concurrency](https://developer.apple.com/documentation/Swift/code-along-elevating-an-app-with-swift-concurrency) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/code-along-elevating-an-app-with-swift-concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/code-along-elevating-an-app-with-swift-concurrency.json
- [Swift Migration Guide](https://www.swift.org/migration/documentation/migrationguide/) _documentation_

## Code Snippets

### Asynchronously loading the selected photo from the photo library — [6:29]

```swift
func loadPhoto(_ item: SelectedPhoto) async {
    var data: Data? = try? await item.loadTransferable(type: Data.self)

    if let cachedData = getCachedData(for: item.id) { data = cachedData }

    guard let data else { return }
    processedPhotos[item.id] = Image(data: data)

    cacheData(item.id, data)
}
```

### Calling an asynchronous function when the SwiftUI View appears — [6:59]

```swift
StickerPlaceholder()
.task {
    await viewModel.loadPhoto(selectedPhoto)
}
```

### Synchronously extracting the sticker and the colors from a photo — [9:45]

```swift
func loadPhoto(_ item: SelectedPhoto) async {
    var data: Data? = try? await item.loadTransferable(type: Data.self)

    if let cachedData = getCachedData(for: item.id) { data = cachedData }

    guard let data else { return }
    processedPhotos[item.id] = PhotoProcessor().process(data: data)

    cacheData(item.id, data)
}
```

### Storing the processed photo in the dictionary — [9:56]

```swift
var processedPhotos = [SelectedPhoto.ID: ProcessedPhoto]()
```

### Displaying the sticker with a gradient background in the carousel — [10:45]

```swift
import SwiftUI
import PhotosUI

struct StickerCarousel: View {
    @State var viewModel: StickerViewModel
    @State private var sheetPresented: Bool = false

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 16) {
                ForEach(viewModel.selection) { selectedPhoto in
                    VStack {
                        if let processedPhoto = viewModel.processedPhotos[selectedPhoto.id] {
                            GradientSticker(processedPhoto: processedPhoto)
                        } else if viewModel.invalidPhotos.contains(selectedPhoto.id) {
                            InvalidStickerPlaceholder()
                        } else {
                            StickerPlaceholder()
                                .task {
                                    await viewModel.loadPhoto(selectedPhoto)
                                }
                        }
                    }
                    .containerRelativeFrame(.horizontal)
                }
            }
        }
        .configureCarousel(
            viewModel,
            sheetPresented: $sheetPresented
        )
        .sheet(isPresented: $sheetPresented) {
            StickerGrid(viewModel: viewModel)
        }
    }
}
```

### Allowing photo processing to run on the background thread — [14:13]

```swift
nonisolated struct PhotoProcessor {

    let colorExtractor = ColorExtractor()

    @concurrent
    func process(data: Data) async -> ProcessedPhoto? {
        let sticker = extractSticker(from: data)
        let colors = extractColors(from: data)

        guard let sticker = sticker, let colors = colors else { return nil }

        return ProcessedPhoto(sticker: sticker, colorScheme: colors)
    }

    private func extractColors(from data: Data) -> PhotoColorScheme? {
        // ...
    }

    private func extractSticker(from data: Data) -> Image? {
        // ...
    }
}
```

### Running the photo processing operations off the main thread — [15:31]

```swift
func loadPhoto(_ item: SelectedPhoto) async {
    var data: Data? = try? await item.loadTransferable(type: Data.self)

    if let cachedData = getCachedData(for: item.id) { data = cachedData }

    guard let data else { return }
    processedPhotos[item.id] = await PhotoProcessor().process(data: data)

    cacheData(item.id, data)
}
```

### Running sticker and color extraction in parallel. — [20:55]

```swift
nonisolated struct PhotoProcessor {

    @concurrent
    func process(data: Data) async -> ProcessedPhoto? {
        async let sticker = extractSticker(from: data)
        async let colors = extractColors(from: data)

        guard let sticker = await sticker, let colors = await colors else { return nil }

        return ProcessedPhoto(sticker: sticker, colorScheme: colors)
    }

    private func extractColors(from data: Data) -> PhotoColorScheme? {
        let colorExtractor = ColorExtractor()
        return colorExtractor.extractColors(from: data)
    }

    private func extractSticker(from data: Data) -> Image? {
        // ...
    }
}
```

### Applying the visual effect on each sticker in the carousel — [24:20]

```swift
import SwiftUI
import PhotosUI

struct StickerCarousel: View {
    @State var viewModel: StickerViewModel
    @State private var sheetPresented: Bool = false

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: 16) {
                ForEach(viewModel.selection) { selectedPhoto in
                    VStack {
                        if let processedPhoto = viewModel.processedPhotos[selectedPhoto.id] {
                            GradientSticker(processedPhoto: processedPhoto)
                        } else if viewModel.invalidPhotos.contains(selectedPhoto.id) {
                            InvalidStickerPlaceholder()
                        } else {
                            StickerPlaceholder()
                                .task {
                                    await viewModel.loadPhoto(selectedPhoto)
                                }
                        }
                    }
                    .containerRelativeFrame(.horizontal)
                    .visualEffect { [selection = viewModel.selection] content, proxy in
                        let frame = proxy.frame(in: .scrollView(axis: .horizontal))
                        let distance = min(0, frame.minX)
                        let isLast = selectedPhoto.id == selection.last?.id

                        return content
                            .hueRotation(.degrees(frame.origin.x / 10))
                            .scaleEffect(1 + distance / 700)
                            .offset(x: isLast ? 0 : -distance / 1.25)
                            .brightness(-distance / 400)
                            .blur(radius: isLast ? 0 : -distance / 50)
                            .opacity(isLast ? 1.0 : min(1.0, 1.0 - (-distance / 400)))
                    }
                }
            }
        }
        .configureCarousel(
            viewModel,
            sheetPresented: $sheetPresented
        )
        .sheet(isPresented: $sheetPresented) {
            StickerGrid(viewModel: viewModel)
        }
    }
}
```

### Accessing a reference type from a concurrent task — [26:15]

```swift
Task { @concurrent in
    await viewModel.loadPhoto(selectedPhoto)      
}
```

### Processing all photos at once with a task group — [29:00]

```swift
func processAllPhotos() async {
    await withTaskGroup { group in
        for item in selection {
            guard processedPhotos[item.id] == nil else { continue }
            group.addTask {
                let data = await self.getData(for: item)
                let photo = await PhotoProcessor().process(data: data)
                return photo.map { ProcessedPhotoResult(id: item.id, processedPhoto: $0) }
            }
        }

        for await result in group {
            if let result {
                processedPhotos[result.id] = result.processedPhoto
            }
        }
    }
}
```

### Kicking off photo processing and configuring the share link in a sticker grid view. — [30:00]

```swift
import SwiftUI

struct StickerGrid: View {
    let viewModel: StickerViewModel
    @State private var finishedLoading: Bool = false

    var body: some View {
        NavigationStack {
            VStack {
                if finishedLoading {
                    GridContent(viewModel: viewModel)
                } else {
                    ProgressView()
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .padding()
                }
            }
            .task {
                await viewModel.processAllPhotos()
                finishedLoading = true
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    if finishedLoading {
                        ShareLink("Share", items: viewModel.selection.compactMap {
                            viewModel.processedPhotos[$0.id]?.sticker
                        }) { sticker in
                            SharePreview(
                                "Sticker Preview",
                                image: sticker,
                                icon: Image(systemName: "photo")
                            )
                        }
                    }
                }
            }
            .configureStickerGrid()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/270/4/fec27360-7913-4e07-8025-e80187a8d00a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/270/4/fec27360-7913-4e07-8025-e80187a8d00a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/270) — developer.apple.com. Indexed for agent consumption._