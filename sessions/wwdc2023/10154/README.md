---
id: "wwdc2023-10154"
event: "wwdc2023"
year: 2023
title: "Build an app with SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10154"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build an app with SwiftData

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10154](https://developer.apple.com/videos/play/wwdc2023/10154)

Discover how SwiftData can help you persist data in your app. Code along with us as we bring SwiftData to a multi-platform SwiftUI app. Learn how to convert existing model classes into SwiftData models, set up the environment, reflect model layer changes in UI, and build document-based applications backed by SwiftData storage.

To get the most out of this session, you should be familiar SwiftData. For an introduction, check out "Meet SwiftData" from WWDC23.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,199 words)

## Documentation & Resources

- [Building a document-based app using SwiftData](https://developer.apple.com/documentation/SwiftUI/Building-a-document-based-app-using-SwiftData) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Building-a-document-based-app-using-SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Building-a-document-based-app-using-SwiftData.json

## Code Snippets

### Defining a SwiftData model — [3:33]

```swift
@Model
final class Card {
    var front: String
    var back: String
    var creationDate: Date

    init(front: String, back: String, creationDate: Date = .now) {
        self.front = front
        self.back = back
        self.creationDate = creationDate
    }
}
```

### Binding to a SwiftData model — [4:25]

```swift
@Bindable var card: Card
```

### Query models from SwiftData storage — [5:52]

```swift
@Query private var cards: [Card]
```

### Setting up a model container for the window group — [8:27]

```swift
WindowGroup {
    ContentView()
}
.modelContainer(for: Card.self)
```

### Providing a preview with sample data — [9:24]

```swift
#Preview {
    ContentView()
        .frame(minWidth: 500, minHeight: 500)
        .modelContainer(previewContainer)
}
```

### Accessing the model context of the ContentView — [10:30]

```swift
@Environment(\.modelContext) private var modelContext
```

### Insert a new model in the context — [10:51]

```swift
let newCard = Card(front: "Sample Front", back: "Sample Back")
modelContext.insert(object: newCard)
```

### Start document-based application setup — [13:34]

```swift
@main
struct SwiftDataFlashCardSample: App {
    var body: some Scene {
        #if os(iOS) || os(macOS)
        DocumentGroup(editing: Card.self, contentType: <#UTType#>) {
            <#code#>
        }
        #else
        WindowGroup {
            ContentView()
                .modelContainer(for: Card.self)
        }
        #endif
    }
}
```

### Finish document-based application setup — [16:51]

```swift
@main
struct SwiftDataFlashCardSample: App {
    var body: some Scene {
        #if os(iOS) || os(macOS)
        DocumentGroup(editing: Card.self, contentType: .flashCards) {
            ContentView()
        }
        #else
        WindowGroup {
            ContentView()
                .modelContainer(for: Card.self)
        }
        #endif
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10154/6/00F52EA1-7867-49C3-9DA6-88D0D9D637E1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10154/6/00F52EA1-7867-49C3-9DA6-88D0D9D637E1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10154) — developer.apple.com. Indexed for agent consumption._