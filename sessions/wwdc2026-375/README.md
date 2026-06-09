# Create high quality images using Image Playground

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-375](https://developer.apple.com/videos/play/wwdc2026/375)

Enable high-quality image creation in your app using Image Playground. With a new generative model that runs on Private Cloud Compute, users can make images in virtually any style, including photorealistic, in your app. You can also specify dimensions for use in even more places, and allow people to modify images using natural language descriptions and touch. Explore how to adopt Image Playground, generate images from descriptions and photos, and manage feature availability in your app.

**Keywords:** `imagecreator`

## Transcript

[Read the full transcript](transcript.md)

## Code Snippets

### Adopt Image Playground in SwiftUI — [5:28]

```swift
// Adopt Image Playground in SwiftUI

func imagePlaygroundSheet(
    isPresented: Binding<Bool>,
    concepts: [ImagePlaygroundConcept] = [],
    sourceImage: Image? = nil,
    onCompletion: @escaping (URL) -> Void,
    onCancellation: (() -> Void)? = nil
) -> some View
```

### Add Image Playground sheet with binding to @State — [5:39]

```swift
// Adopt Image Playground

@State private var showingPlayground = false

var body: some View {
    Button("Create image") {
        showingPlayground = true
    }
    .imagePlaygroundSheet(
        isPresented: $showingPlayground,
        onCompletion: { url in
            var updated = currentCard
            store.saveImage(url, for: &updated)
        }
    )
}
```

### Seeding the sheet with context from your card — [6:29]

```swift
// Seeding the sheet with context from your card

var concepts: [ImagePlaygroundConcept] {
    [
        .text(card.theme),
        .extracted(from: card.message, title: card.theme),
    ]
}

var body: some View {
    Button("Create image") {
        showingPlayground = true
    }
    .imagePlaygroundSheet(
        isPresented: $showingPlayground,
        concepts: concepts,
        onCompletion: { url in
            var updated = card
            store.saveImage(url, for: &updated)
        }
    )
}
```

### Starting from a reference photo — [7:11]

```swift
// Starting from a reference photo

@State private var sourceImage: Image?

var body: some View {
    Button("Create image") {
        showingPlayground = true
    }
    .imagePlaygroundSheet(
        isPresented: $showingPlayground,
        concepts: concepts,
        sourceImage: sourceImage,
        onCompletion: { url in
            var updated = card
            store.saveImage(url, for: &updated)
        }
    )
}
```

### Providing a visual suggestion using a drawing — [7:42]

```swift
// Providing a visual suggestion using a drawing

@State private var drawing = PKDrawing()

var concepts: [ImagePlaygroundConcept] {
    var result: [ImagePlaygroundConcept] = [
        .text(card.theme),
        .extracted(from: card.message)
    ]
    if !drawing.strokes.isEmpty {
        result.append(.drawing(drawing))
    }
    return result
}
```

### Adopt Image Playground in UIKit or AppKit — [8:06]

```swift
// Adopt Image Playground in UIKit or AppKit

func presentViewController() {
    let viewController = ImagePlaygroundViewController()
    viewController.concepts = [
        .text(card.theme),
        .extracted(from: card.message)
    ]
    viewController.delegate = self
    present(viewController, animated: true)
}

func imagePlaygroundViewController(
    _ viewController: ImagePlaygroundViewController,
    didCreateImageAt url: URL
) {
    var updated = card
    store.saveImage(url, for: &updated)
    dismiss(animated: true)
}
```

### Size Specification — [9:02]

```swift
// Size Specification

var options: ImagePlaygroundOptions {
    var options = ImagePlaygroundOptions()
    options.sizeSpecification = .closest(to: card.format.size)
    return options
}

var body: some View {
    Button("Create image") { showingPlayground = true }
        .imagePlaygroundSheet(
            isPresented: $showingPlayground,
            concepts: concepts,
            onCompletion: { url in
                var updated = card
                store.saveImage(url, for: &updated)
            }
        )
        .imagePlaygroundOptions(options)
}
```

### Styles — [9:39]

```swift
// Styles

var options: ImagePlaygroundOptions {
    var options = ImagePlaygroundOptions()
    options.sizeSpecification = .closest(to: card.format.size)
    return options
}

var body: some View {
    Button("Create image") { showingPlayground = true }
        .imagePlaygroundSheet(
            isPresented: $showingPlayground,
            concepts: concepts,
            onCompletion: { url in
                var updated = card
                store.saveImage(url, for: &updated)
            }
        )
        .imagePlaygroundOptions(options)
        .imagePlaygroundGenerationStyle(
            pendingStylePreset.defaultStyle,
            in: pendingStylePreset.allowedStyles
        )
}
```

### External Provider Style — [10:27]

```swift
// External Provider Style

var options: ImagePlaygroundOptions {
    var options = ImagePlaygroundOptions()
    options.sizeSpecification = .closest(to: card.format.size)
    return options
}

var body: some View {
    Button("Create image") { showingPlayground = true }
        .imagePlaygroundSheet(
            isPresented: $showingPlayground,
            concepts: concepts,
            onCompletion: { url in
                var updated = card
                store.saveImage(url, for: &updated)
            }
        )
        .imagePlaygroundOptions(options)
        .imagePlaygroundGenerationStyle(
            pendingStylePreset.defaultStyle,
            in: pendingStylePreset.allowedStyles + [.externalProvider]
        )
}
```

### Generating an expressive icon for the card thumbnail — [11:02]

```swift
// Generating an expressive icon for the card thumbnail

@State private var showingIconPlayground = false

var body: some View {
    Button("Create icon") {
        showingIconPlayground = true
    }
    Color.clear
        .imagePlaygroundSheet(
            isPresented: $showingIconPlayground,
            concepts: concepts,
            onCompletion: { _ in
            } ,
            onAdaptiveImageGlyphCreation: { glyph in
                var updatedCard = card
                store.saveIcon(glyph, for: &updatedCard)
            }
        )
        .imagePlaygroundGenerationStyle(.emoji, in: [.emoji])
}
```

### Disabling personalization when it doesn't fit your context — [12:01]

```swift
// Disabling personalization when it doesn't fit your context

var options: ImagePlaygroundOptions {
    var options = ImagePlaygroundOptions()
    options.sizeSpecification = .closest(to: card.format.size)
    options.personalization = .disabled
    return options
}
```

### Supports image generation — [12:32]

```swift
// Supports image generation

@Environment(\.supportsImageGeneration)
private var supportsImageGeneration

var body: some View {
    NavigationLink(card.recipient) {
        if supportsImageGeneration {
            CardEditorView(card: card)
        }γelse {
            CardPickerView(card: card)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/375/4/01104285-3253-4b2d-80c3-0d5cdf95c97e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/375/4/01104285-3253-4b2d-80c3-0d5cdf95c97e/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._