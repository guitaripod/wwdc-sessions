---
id: "wwdc2024-10146"
event: "wwdc2024"
year: 2024
title: "Demystify SwiftUI containers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10146"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Demystify SwiftUI containers

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10146](https://developer.apple.com/videos/play/wwdc2024/10146)

Learn about the capabilities of SwiftUI container views and build a mental model for how subviews are managed by their containers. Leverage new APIs to build your own custom containers, create modifiers to customize container content, and give your containers that extra polish that helps your apps stand out.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,515 words)

## Documentation & Resources

- [Creating custom container views](https://developer.apple.com/documentation/SwiftUI/Creating-custom-container-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Creating-custom-container-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Creating-custom-container-views.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### SwiftUI Lists — [0:20]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}
```

### SwiftUI Lists — [0:36]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(otherSongs) { song in
    Text(song.title)
  }
}
```

### SwiftUI Lists — [0:54]

```swift
List {
  Section("Favorite Songs") {
    Text("Scrolling in the Deep")
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }

  Section("Other Songs") {
    ForEach(otherSongs) { song in
      Text(song.title)
    }
  }
}
```

### SwiftUI Lists — [1:00]

```swift
List {
  Section("Favorite Songs") {
    Text("Scrolling in the Deep")
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }

  Section("Other Songs") {
    ForEach(otherSongs) { song in
      Text(song.title)
        .listRowSeparator(.hidden)
    }
  }
}
```

### Data-driven DisplayBoard — [2:35]

```swift
@State private var songs: [Song] = [
  Song("Scrolling in the Deep"),
  Song("Born to Build & Run"),
  Song("Some Body Like View"),
]

var body: some View {
  DisplayBoard(songs) { song in
    Text(song.title)
  }
}
```

### DisplayBoard implementation — [2:47]

```swift
// Insert code snvar data: Data
@ViewBuilder var content: (Data.Element) -> Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(data) { item in
      CardView {
        content(item)
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### Data-driven DisplayBoard — [3:08]

```swift
@State private var songs: [Song] = [
  Song("Scrolling in the Deep"),
  Song("Born to Build & Run"),
  Song("Some Body Like View"),
]

var body: some View {
  DisplayBoard(songs) { song in
    Text(song.title)
  }
}
```

### List composition — [3:30]

```swift
List(songsFromSam) { song in
  Text(song.title)
}
```

### List composition — [3:46]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}
```

### List composition — [3:56]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}

List(songsFromSam) { song in
  Text(song.title)
}
```

### List composition — [4:05]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}

List {
  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### List composition — [4:24]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### DisplayBoard implementation — [4:59]

```swift
var data: Data
@ViewBuilder var content: (Data.Element) -> Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(data) { item in
      CardView {
        content(item)
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### DisplayBoard implementation — [5:15]

```swift
// DisplayBoard implementation

@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(data) { item in
      CardView {
        content(item)
      }
    }
  }
  .background { BoardBackgroundView() }
}

DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}

DisplayBoard {
  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### DisplayBoard implementation — [5:27]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(subviewOf: content) { subview in
      CardView {
        subview
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### List composition — [5:52]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### DisplayBoard composition — [5:57]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### DisplayBoard implementation — [6:12]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(subviewOf: content) { subview in
      CardView {
        subview
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### DisplayBoard subviews — [6:23]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### Declared vs. resolved views — [6:36]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}

// 3 resolved subviews
Text("Scrolling in the Deep")
Text("Born to Build & Run")
Text("Some Body Like View")

// 9 resolved subviews
Text("I Container Multitudes")
…
Text("Love Stack")
```

### List subviews — [7:11]

```swift
List {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### Declared vs. resolved views — [7:19]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}

// 3 resolved subviews
Text("Scrolling in the Deep")
Text("Born to Build & Run")
Text("Some Body Like View")

// 9 resolved subviews
Text("I Container Multitudes")
…
Text("Love Stack")
```

### Resolved ForEach — [8:00]

```swift
// 1 declared view
ForEach(songsFromSam) { song in
  Text(song.title)
}

// 9 resolved subviews
Text("I Container Multitudes")
…
Text("Love Stack")
```

### Resolved Group — [8:16]

```swift
// 1 declared view
Group {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}

// 3 resolved subviews
Text("Scrolling in the Deep")

Text("Born to Build & Run")

Text("Some Body Like View")
```

### Resolved EmptyView — [8:32]

```swift
// 1 declared view
EmptyView()	

// Zero resolved subviews
```

### Resolved if expression — [8:39]

```swift
// 1 declared view
if showFavoriteSongs {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")
}

// true → 3 resolved subviews
Text("Scrolling in the Deep")
Text("Born to Build & Run")
Text("Some Body Like View")

// false → Zero resolved subviews
```

### DisplayBoard implementation — [8:48]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(subviewOf: content) { subview in
      CardView {
        subview
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### DisplayBoard composition — [9:11]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }
}
```

### DisplayBoard composition — [9:17]

```swift
DisplayBoard {
  Text("Scrolling in the Deep")
  Text("Born to Build & Run")
  Text("Some Body Like View")

  ForEach(songsFromSam) { song in
    Text(song.title)
  }

  ForEach(songsFromSommer) { song in
    Text(song.title)
  }
}
```

### DisplayBoard implementation — [9:44]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    ForEach(subviewOf: content) { subview in
      CardView {
        subview
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### DisplayBoard implementation — [9:55]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    Group(subviewsOf: content) { subviews in
      ForEach(subviews) { subview in
        CardView {
          subview
        }
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### DisplayBoard implementation — [10:19]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    Group(subviewsOf: content) { subviews in
      ForEach(subviews) { subview in
        CardView(
          scale: subviews.count > 15 ? .small : .normal
        ) {
          subview
        }
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### List sections — [10:47]

```swift
List {
  Section("Favorite Songs") {
    Text("Scrolling in the Deep")
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }

  Section("Other Songs") {
    ForEach(otherSongs) { song in
      Text(song.title)
    }
  }
}
```

### DisplayBoard sections — [11:03]

```swift
DisplayBoard {
  Section("Matt's Favorites") {
    Text("Scrolling in the Deep")
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }
  Section("Sam's Favorites") {
    ForEach(songsFromSam) { song in
      Text(song.title)
    }
  }
  Section("Sommer's Favorites") {
    ForEach(songsFromSommer) { song in
      Text(song.title)
    }
  }
}
```

### Implementing DisplayBoard sections — [11:26]

```swift
DisplayBoard sections
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardCardLayout {
    Group(subviewsOf: content) { subviews in
      ForEach(subviews) { subview in
        CardView(
          scale: subviews.count > 15 ? .small : .normal
        ) {
          subview
        }
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### Implementing DisplayBoard sections — [11:35]

```swift
@ViewBuilder var content: Content

var body: some View {
  DisplayBoardSectionContent {
    content
  }
  .background { BoardBackgroundView() }
}

struct DisplayBoardSectionContent<Content: View>: View {
  @ViewBuilder var content: Content
  ...
}
```

### Implementing DisplayBoard sections — [11:42]

```swift
@ViewBuilder var content: Content

var body: some View {
  HStack(spacing: 80) {
    ForEach(sectionOf: content) { section in
      DisplayBoardSectionContent {
        section.content
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### Implementing DisplayBoard section headers — [12:48]

```swift
@ViewBuilder var content: Content

var body: some View {
  HStack(spacing: 80) {
    ForEach(sectionOf: content) { section in
      VStack(spacing: 20) {
        if !section.header.isEmpty {
          DisplayBoardSectionHeaderCard { section.header }
        } 
        DisplayBoardSectionContent {
          section.content
        }
        .background { BoardSectionBackgroundView() }
      }
    }
  }
  .background { BoardBackgroundView() }
}
```

### List customization — [13:30]

```swift
List {
  Section("Favorite Songs") {
    Text("Scrolling in the Deep")
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }

  Section("Other Songs") {
    ForEach(otherSongs) { song in
      Text(song.title)
        .listRowSeparator(.hidden)
    }
  }
}
```

### Custom container values — [14:46]

```swift
extension ContainerValues {
  @Entry var isDisplayBoardCardRejected: Bool = false
}

extension View {
  func displayBoardCardRejected(_ isRejected: Bool) -> some View {
    containerValue(\.isDisplayBoardCardRejected, isRejected)
  }
}
```

### Implementing DisplayBoard customization — [15:42]

```swift
struct DisplayBoardSectionContent<Content: View>: View {
  @ViewBuilder var content: Content

  var body: some View {
    DisplayBoardCardLayout {
      Group(subviewsOf: content) { subviews in
        ForEach(subviews) { subview in
          let values = subview.containerValues
          CardView(
            scale: (subviews.count > 15) ? .small : .normal,
            isRejected: values.isDisplayBoardCardRejected
          ) {
            subview
          }
        }
      }
    }
  }
}
```

### DisplayBoard customization — [16:15]

```swift
DisplayBoard {
  Section("Matt's Favorites") {
    Text("Scrolling in the Deep")
      .displayBoardCardRejected(true)
    Text("Born to Build & Run")
    Text("Some Body Like View")
  }
  Section("Sam's Favorites") {
    ForEach(songsFromSam) { song in
      Text(song.title)
        .displayBoardCardRejected(song.samHasDibs)
    }
  }
  Section("Sommer's Favorites") {
    ForEach(songsFromSommer) { Text($0.title) }}}
  }
  .displayBoardCardRejected(true)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10146/4/F3988ADA-0BF0-447C-BE07-01C07F99F11E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10146/4/F3988ADA-0BF0-447C-BE07-01C07F99F11E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10146) — developer.apple.com. Indexed for agent consumption._
