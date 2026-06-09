---
id: "wwdc2025-266"
event: "wwdc2025"
year: 2025
title: "Explore concurrency in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/266"
topics: ["SwiftUI & UI Frameworks", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Explore concurrency in SwiftUI

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-266](https://developer.apple.com/videos/play/wwdc2025/266)

Discover how SwiftUI leverages Swift concurrency to build safe and responsive apps. Explore how SwiftUI uses the main actor by default and offloads work to other actors. Learn how to interpret concurrency annotations and manage async tasks with SwiftUI’s event loop for smooth animations and UI updates. You’ll leave knowing how to avoid data races and write code fearlessly.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,017 words)

## Documentation & Resources

- [Mutex](https://developer.apple.com/documentation/Synchronization/Mutex) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Synchronization/Mutex
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Synchronization/Mutex.json
- [Concurrency](https://developer.apple.com/documentation/Swift/concurrency) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/concurrency.json
- [Updating an App to Use Swift Concurrency](https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swift/updating_an_app_to_use_swift_concurrency
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swift/updating_an_app_to_use_swift_concurrency.json
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### UI for extracting colors — [2:45]

```swift
// UI for extracting colors

struct ColorScheme: Identifiable, Hashable {
    var id = UUID()
    let imageName: String
    var colors: [Color]
}

@Observable
final class ColorExtractor {
    var imageName: String
    var scheme: ColorScheme?
    var isExtracting: Bool = false
    var colorCount: Float = 5

    func extractColorScheme() async {}
}

struct ColorExtractorView: View {
    @State private var model = ColorExtractor()

    var body: some View {
            ImageView(
                imageName: model.imageName,
                isLoading: model.isExtracting
            )
            EqualWidthVStack {
                ColorSchemeView(
                    isLoading: model.isExtracting,
                    colorScheme: model.scheme,
                    extractCount: Int(model.colorCount)
                )
                .onTapGesture {
                    guard !model.isExtracting else { return }
                    withAnimation { model.isExtracting = true }
                    Task {
                        await model.extractColorScheme()
                        withAnimation { model.isExtracting = false }
                    }
                }
                Slider(value: $model.colorCount, in: 3...10, step: 1)
                    .disabled(model.isExtracting)
            }
        }
    }
}
```

### AppKit and UIKit require @MainActor: an example — [5:55]

```swift
// AppKit and UIKit require @MainActor
// Example: UIViewRepresentable

struct FancyUILabel: UIViewRepresentable {
    func makeUIView(context: Context) -> UILabel {
        let label = UILabel()
        // customize the label...
        return label
    }
}
```

### UI for extracting colors — [6:42]

```swift
// UI for extracting colors

struct ColorScheme: Identifiable, Hashable {
    var id = UUID()
    let imageName: String
    var colors: [Color]
}

@Observable
final class ColorExtractor {
    var imageName: String
    var scheme: ColorScheme?
    var isExtracting: Bool = false
    var colorCount: Float = 5

    func extractColorScheme() async {}
}

struct ColorExtractorView: View {
    @State private var model = ColorExtractorModel()

    var body: some View {
            ImageView(
                imageName: model.imageName,
                isLoading: model.isExtracting
            )
            EqualWidthVStack(spacing: 30) {
                ColorSchemeView(
                    isLoading: model.isExtracting,
                    colorScheme: model.scheme,
                    extractCount: Int(model.colorCount)
                )
                .onTapGesture {
                    guard !model.isExtracting else { return }
                    withAnimation { model.isExtracting = true }
                    Task {
                        await model.extractColorScheme()
                        withAnimation { model.isExtracting = false }
                    }
                }
                Slider(value: $model.colorCount, in: 3...10, step: 1)
                    .disabled(model.isExtracting)
            }
        }
    }
}
```

### Animated circle, part of color scheme view — [8:26]

```swift
// Part of color scheme view

struct SchemeContentView: View {
    let isLoading: Bool
    @State private var pulse: Bool = false

    var body: some View {
        ZStack {
            // Color wheel …

            Circle()
                .scaleEffect(isLoading ? 1.5 : 1)

            VStack {
                Text(isLoading ? "Please wait" : "Extract")

                if !isLoading {
                    Text("^[\(extractCount) color](inflect: true)")
                }
            }
            .visualEffect { [pulse] content, _ in
                content
                    .blur(radius: pulse ? 2 : 0)
            }
            .onChange(of: isLoading) { _, newValue in
                withAnimation(newValue ? kPulseAnimation : nil) {
                    pulse = newValue
                }
            }
        }
    }
}
```

### UI for extracting colors — [13:10]

```swift
// UI for extracting colors

struct ColorExtractorView: View {
    @State private var model = ColorExtractor()

    var body: some View {
            ImageView(
                imageName: model.imageName,
                isLoading: model.isExtracting
            )
            EqualWidthVStack {
                ColorSchemeView(
                    isLoading: model.isExtracting,
                    colorScheme: model.scheme,
                    extractCount: Int(model.colorCount)
                )
                .onTapGesture {
                    guard !model.isExtracting else { return }
                    withAnimation { model.isExtracting = true }
                    Task {
                        await model.extractColorScheme()
                        withAnimation { model.isExtracting = false }
                    }
                }
                Slider(value: $model.colorCount, in: 3...10, step: 1)
                    .disabled(model.isExtracting)
            }
        }
    }
}
```

### Part of color scheme view — [13:47]

```swift
// Part of color scheme view

struct SchemeContentView: View {
    let isLoading: Bool
    @State private var pulse: Bool = false

    var body: some View {
        ZStack {
            // Color wheel …

            Circle()
                .scaleEffect(isLoading ? 1.5 : 1)

            VStack {
                Text(isLoading ? "Please wait" : "Extract")

                if !isLoading {
                    Text("^[\(extractCount) color](inflect: true)")
                }
            }
            .visualEffect { [pulse] content, _ in
                content
                    .blur(radius: pulse ? 2 : 0)
            }
            .onChange(of: isLoading) { _, newValue in
                withAnimation(newValue ? kPulseAnimation : nil) {
                    pulse = newValue
                }
            }
        }
    }
}
```

### UI for extracting colors — [17:42]

```swift
// UI for extracting colors

struct ColorExtractorView: View {
    @State private var model = ColorExtractor()

    var body: some View {
            ImageView(
                imageName: model.imageName,
                isLoading: model.isExtracting
            )
            EqualWidthVStack {
                ColorSchemeView(
                    isLoading: model.isExtracting,
                    colorScheme: model.scheme,
                    extractCount: Int(model.colorCount)
                )
                .onTapGesture {
                    guard !model.isExtracting else { return }
                    withAnimation { model.isExtracting = true }
                    Task {
                        await model.extractColorScheme()
                        withAnimation { model.isExtracting = false }
                    }
                }
                Slider(value: $model.colorCount, in: 3...10, step: 1)
                    .disabled(model.isExtracting)
            }
        }
    }
}
```

### Animate colors as they appear by scrolling — [18:55]

```swift
// Animate colors as they appear by scrolling

struct SchemeHistoryItemView: View {
    let scheme: ColorScheme
    @State private var isShown: Bool = false

    var body: some View {
        HStack(spacing: 0) {
            ForEach(scheme.colors) { color in
                color
                    .offset(x: 0, y: isShown ? 0 : 60)
            }
        }
        .onScrollVisibilityChange(threshold: 0.9) {
            guard !isShown else { return }
            withAnimation {
                isShown = $0
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/266/7/c7837487-ed14-4560-8c2c-a583596027ca/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/266/7/c7837487-ed14-4560-8c2c-a583596027ca/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/266) — developer.apple.com. Indexed for agent consumption._