---
id: "wwdc2021-10018"
event: "wwdc2021"
year: 2021
title: "What's new in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10018"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in SwiftUI

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10018](https://developer.apple.com/videos/play/wwdc2021/10018)

There’s never been a better time to develop your apps with SwiftUI. Discover the latest updates to the UI framework — including lists, buttons, and text fields — and learn how these features can help you more fully adopt SwiftUI in your app. Find out how to create beautiful, visually-rich graphics using the canvas view, materials, and enhancements to symbols. Explore multi-column tables on macOS, refinements to focus and keyboard interaction, and the multi-platform search API. And we’ll show you how to take advantage of features like Swift concurrency, a brand new AttributedString, format styles, localization, and so much more.

**Keywords:** `accessibility`, `accessibilitychildren`, `accessibility modifiers`, `accessibility preview`, `.accessibilityrotor`, `access to bindings`, `add a gesture`, `alteratesrowbackground`, `always on display`, `animation schedule`, `aod`, `asyncimage`, `async images`, `async sequence`, `attributedstring`, `await`, `background`, `blending of content`, `blurred background`, `button improvement`, `buttons`, `canvas`, `code style`, `colors`, `concurrency`, `confirmationdialog`, `confirmation dialog`, `controlgroup`, `control group`, `controlprominence`, `controlsize`, `core data fetch request`, `custom refresh`, `custom shape`, `custom views`, `data`, `destructive`, `dismiss keyboard`, `dollar sign operator`, `dynamic type`, `editable text`, `emoji`, `exportsitemproviders`, `fetchnewitems`, `filter`, `focus`, `focused`, `focusstate`, `foregroundstyle`, `generate strings`, `gestures`, `graphics`, `grids`, `hide user sensitive information`, `hierarchical`, `keyboard`, `keyboardbar`, `keyboard improvement`, `keyboard navigation`, `landscape previews`, `language sensitive attributes`, `links`, `list row background`, `listrowseparator`, `list row separator`, `lists`, `live accessibility information`, `localization`, `localize`, `markdown`, `markdown support`, `material`, `menuindicator`, `monochrome`, `multicolor`, `onsubmit`, `opacity`, `outlines`, `palette`, `popover`, `press state`, `preview orientation`, `primaryaction`, `primary actions`, `privacysensitive`, `privacy sensitive modifier`, `prominent button`, `prominent tint support`, `pull to refresh`, `redacted content`, `refreshable`, `rotor`, `.safeareainset`, `safe area inset`, `schedule`, `search`, `searchable`, `sectionedfetchrequest`, `selectable text`, `separator`, `shortcuts`, `sidebar`, `strong emphasis`, `submitlabel`, `swipe actions`, `symbols`, `symbolvariant`, `symbol variant`, `table`, `tablecolumn`, `.task`, `textfield`, `textselection`, `timelineview`, `tint separator`, `toggle`, `toolbar buttons`, `update based on environment`, `update based on state`, `updated colors`, `update over time`, `vibrancy`, `view`, `xcode previews`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,706 words)

## Documentation & Resources

- [SwiftUI](https://developer.apple.com/documentation/SwiftUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI.json
- [Human Interface Guidelines: Designing for iOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-ios) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/Human-Interface-Guidelines/designing-for-ios

## Code Snippets

### AsyncImage — [3:29]

```swift
struct ContentView: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      ScrollView {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 420))]) {
          ForEach(photoStore.photos) { photo in
            AsyncImage(url: photo.url)
              .frame(width: 400, height: 266)
              .mask(RoundedRectangle(cornerRadius: 16))
          }
        }
        .padding()
      }
      .navigationTitle("Superhero Recruits")
    }
    .navigationViewStyle(.stack)
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}
```

### AsyncImage with custom placeholder — [3:45]

```swift
struct ContentView: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      ScrollView {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 420))]) {
          ForEach(photoStore.photos) { photo in
            AsyncImage(url: photo.url) { image in
              image
                .resizable()
                .aspectRatio(contentMode: .fill)
            } placeholder: {
              randomPlaceholderColor()
                .opacity(0.2)
            }
            .frame(width: 400, height: 266)
            .mask(RoundedRectangle(cornerRadius: 16))
          }
        }
        .padding()
      }
      .navigationTitle("Superhero Recruits")
    }
    .navigationViewStyle(.stack)
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}

func randomPlaceholderColor() -> Color {
  placeholderColors.randomElement()!
}

let placeholderColors: [Color] = [
  .red, .blue, .orange, .mint, .purple, .yellow, .green, .pink
]
```

### AsyncImage with custom animations and error handling — [4:00]

```swift
struct Contentiew: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      ScrollView {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 420))]) {
          ForEach(photoStore.photos) { photo in
            AsyncImage(url: photo.url, transaction: .init(animation: .spring())) { phase in
              switch phase {
              case .empty:
                randomPlaceholderColor()
                  .opacity(0.2)
                  .transition(.opacity.combined(with: .scale))
              case .success(let image):
                image
                  .resizable()
                  .aspectRatio(contentMode: .fill)
                  .transition(.opacity.combined(with: .scale))
              case .failure(let error):
                ErrorView(error)
              @unknown default:
                ErrorView()
              }
            }
            .frame(width: 400, height: 266)
            .mask(RoundedRectangle(cornerRadius: 16))
          }
        }
        .padding()
      }
      .navigationTitle("Superhero Recruits")
    }
    .navigationViewStyle(.stack)
  }
}

struct ErrorView: View {
  var error: Error?

  init(_ error: Error? = nil) {
    self.error = error
  }

  var body: some View {
    Text("Error") // Display the error
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}

func randomPlaceholderColor() -> Color {
  placeholderColors.randomElement()!
}

let placeholderColors: [Color] = [
  .red, .blue, .orange, .mint, .purple, .yellow, .green, .pink
]
```

### refreshable() modifier — [4:24]

```swift
struct ContentView: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      List {
        ForEach(photoStore.photos) { photo in
          AsyncImage(url: photo.url)
            .frame(minHeight: 200)
            .mask(RoundedRectangle(cornerRadius: 16))
            .listRowSeparator(.hidden)
        }
      }
      .listStyle(.plain)
      .navigationTitle("Superhero Recruits")
      .refreshable {
        await photoStore.update()
      }
    }
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]

  func update() async {
    // Fetch new photos
  }
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}
```

### task() modifier — [4:58]

```swift
struct ContentView: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      List {
        ForEach(photoStore.photos) { photo in
          AsyncImage(url: photo.url)
            .frame(minHeight: 200)
            .mask(RoundedRectangle(cornerRadius: 16))
            .listRowSeparator(.hidden)
        }
      }
      .listStyle(.plain)
      .navigationTitle("Superhero Recruits")
      .refreshable {
        await photoStore.update()
      }
      .task {
        await photoStore.update()
      }
    }
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]

  func update() async {
    // Fetch new photos
  }
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}
```

### task() modifier iterating over an AsyncSequence — [5:28]

```swift
struct ContentView: View {
  @StateObject private var photoStore = PhotoStore()

  var body: some View {
    NavigationView {
      List {
        ForEach(photoStore.photos) { photo in
          AsyncImage(url: photo.url)
            .frame(minHeight: 200)
            .mask(RoundedRectangle(cornerRadius: 16))
            .listRowSeparator(.hidden)
        }
      }
      .listStyle(.plain)
      .navigationTitle("Superhero Recruits")
      .refreshable {
        await photoStore.update()
      }
      .task {
        for await photo in photoStore.newestPhotos {
          photoStore.push(photo)
        }
      }
    }
  }
}

class PhotoStore: ObservableObject {
  @Published var photos: [Photo] = [/* Default photos */]

  var newestPhotos: NewestPhotos {
    NewestPhotos()
  }

  func update() async {
    // Fetch new photos from remote service
  }

  func push(_ photo: Photo) {
    photos.append(photo)
  }
}

struct NewestPhotos: AsyncSequence {
  struct AsyncIterator: AsyncIteratorProtocol {
    func next() async -> Photo? {
      // Fetch next photo from remote service
    }
  }

  func makeAsyncIterator() -> AsyncIterator {
    AsyncIterator()
  }
}

struct Photo: Identifiable {
  var id: URL { url }
  var url: URL
}
```

### Non-interactive directions list — [7:02]

```swift
struct ContentView: View {
  @State var directions: [Direction] = [
    Direction(symbol: "car", color: .mint, text: "Drive to SFO"),
    Direction(symbol: "airplane", color: .blue, text: "Fly to SJC"),
    Direction(symbol: "tram", color: .purple, text: "Ride to Cupertino"),
    Direction(symbol: "bicycle", color: .orange, text: "Bike to Apple Park"),
    Direction(symbol: "figure.walk", color: .green, text: "Walk to pond"),
    Direction(symbol: "lifepreserver", color: .blue, text: "Swim to the center"),
    Direction(symbol: "drop", color: .indigo, text: "Dive to secret airlock"),
    Direction(symbol: "tram.tunnel.fill", color: .brown, text: "Ride through underground tunnels"),
    Direction(symbol: "key", color: .red, text: "Enter door code:"),
  ]

  var body: some View {
    NavigationView {
      List(directions) { direction in
        Label {
          Text(direction.text)
        } icon: {
          DirectionsIcon(direction)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Secret Hideout")
    }
  }
}

struct Direction: Identifiable {
  var id = UUID()
  var symbol: String
  var color: Color
  var text: String
}

private struct DirectionsIcon: View {
  var direction: Direction

  init(_ direction: Direction) {
    self.direction = direction
  }

  var body: some View {
    Image(systemName: direction.symbol)
      .resizable()
      .aspectRatio(contentMode: .fit)
      .foregroundStyle(.white)
      .padding(6)
      .frame(width: 33, height: 33)
      .background(direction.color, in: RoundedRectangle(cornerRadius: 8))
  }
}
```

### Interactive directions list — [8:08]

```swift
struct ContentView: View {
  @State var directions: [Direction] = [
    Direction(symbol: "car", color: .mint, text: "Drive to SFO"),
    Direction(symbol: "airplane", color: .blue, text: "Fly to SJC"),
    Direction(symbol: "tram", color: .purple, text: "Ride to Cupertino"),
    Direction(symbol: "bicycle", color: .orange, text: "Bike to Apple Park"),
    Direction(symbol: "figure.walk", color: .green, text: "Walk to pond"),
    Direction(symbol: "lifepreserver", color: .blue, text: "Swim to the center"),
    Direction(symbol: "drop", color: .indigo, text: "Dive to secret airlock"),
    Direction(symbol: "tram.tunnel.fill", color: .brown, text: "Ride through underground tunnels"),
    Direction(symbol: "key", color: .red, text: "Enter door code:"),
  ]

  var body: some View {
    NavigationView {
      List($directions) { $direction in
        Label {
          TextField("Instructions", text: $direction.text)
        } icon: {
          DirectionsIcon(direction)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Secret Hideout")
    }
  }
}

struct Direction: Identifiable {
  var id = UUID()
  var symbol: String
  var color: Color
  var text: String
}

private struct DirectionsIcon: View {
  var direction: Direction

  init(_ direction: Direction) {
    self.direction = direction
  }

  var body: some View {
    Image(systemName: direction.symbol)
      .resizable()
      .aspectRatio(contentMode: .fit)
      .foregroundStyle(.white)
      .padding(6)
      .frame(width: 33, height: 33)
      .background(direction.color, in: RoundedRectangle(cornerRadius: 8))
  }
}
```

### Interactive directions list using ForEach — [8:49]

```swift
struct ContentView: View {
  @State var directions: [Direction] = [
    Direction(symbol: "car", color: .mint, text: "Drive to SFO"),
    Direction(symbol: "airplane", color: .blue, text: "Fly to SJC"),
    Direction(symbol: "tram", color: .purple, text: "Ride to Cupertino"),
    Direction(symbol: "bicycle", color: .orange, text: "Bike to Apple Park"),
    Direction(symbol: "figure.walk", color: .green, text: "Walk to pond"),
    Direction(symbol: "lifepreserver", color: .blue, text: "Swim to the center"),
    Direction(symbol: "drop", color: .indigo, text: "Dive to secret airlock"),
    Direction(symbol: "tram.tunnel.fill", color: .brown, text: "Ride through underground tunnels"),
    Direction(symbol: "key", color: .red, text: "Enter door code:"),
  ]

  var body: some View {
    NavigationView {
      List {
        ForEach($directions) { $direction in
          Label {
            TextField("Instructions", text: $direction.text)
          } icon: {
            DirectionsIcon(direction)
          }
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Secret Hideout")
    }
  }
}

struct Direction: Identifiable {
  var id = UUID()
  var symbol: String
  var color: Color
  var text: String
}

private struct DirectionsIcon: View {
  var direction: Direction

  init(_ direction: Direction) {
    self.direction = direction
  }

  var body: some View {
    Image(systemName: direction.symbol)
      .resizable()
      .aspectRatio(contentMode: .fit)
      .foregroundStyle(.white)
      .padding(6)
      .frame(width: 33, height: 33)
      .background(direction.color, in: RoundedRectangle(cornerRadius: 8))
  }
}
```

### listRowSeparatorTint() modifier — [9:09]

```swift
struct ContentView: View {
  @State var directions: [Direction] = [
    Direction(symbol: "car", color: .mint, text: "Drive to SFO"),
    Direction(symbol: "airplane", color: .blue, text: "Fly to SJC"),
    Direction(symbol: "tram", color: .purple, text: "Ride to Cupertino"),
    Direction(symbol: "bicycle", color: .orange, text: "Bike to Apple Park"),
    Direction(symbol: "figure.walk", color: .green, text: "Walk to pond"),
    Direction(symbol: "lifepreserver", color: .blue, text: "Swim to the center"),
    Direction(symbol: "drop", color: .indigo, text: "Dive to secret airlock"),
    Direction(symbol: "tram.tunnel.fill", color: .brown, text: "Ride through underground tunnels"),
    Direction(symbol: "key", color: .red, text: "Enter door code:"),
  ]

  var body: some View {
    NavigationView {
      List {
        ForEach($directions) { $direction in
          Label {
            TextField("Instructions", text: $direction.text)
          } icon: {
            DirectionsIcon(direction)
          }
          .listRowSeparatorTint(direction.color)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Secret Hideout")
    }
  }
}

struct Direction: Identifiable {
  var id = UUID()
  var symbol: String
  var color: Color
  var text: String
}

private struct DirectionsIcon: View {
  var direction: Direction

  init(_ direction: Direction) {
    self.direction = direction
  }

  var body: some View {
    Image(systemName: direction.symbol)
      .resizable()
      .aspectRatio(contentMode: .fit)
      .foregroundStyle(.white)
      .padding(6)
      .frame(width: 33, height: 33)
      .background(direction.color, in: RoundedRectangle(cornerRadius: 8))
  }
}
```

### listRowSeparator() modifier — [9:38]

```swift
struct ContentView: View {
  @State var directions: [Direction] = [
    Direction(symbol: "car", color: .mint, text: "Drive to SFO"),
    Direction(symbol: "airplane", color: .blue, text: "Fly to SJC"),
    Direction(symbol: "tram", color: .purple, text: "Ride to Cupertino"),
    Direction(symbol: "bicycle", color: .orange, text: "Bike to Apple Park"),
    Direction(symbol: "figure.walk", color: .green, text: "Walk to pond"),
    Direction(symbol: "lifepreserver", color: .blue, text: "Swim to the center"),
    Direction(symbol: "drop", color: .indigo, text: "Dive to secret airlock"),
    Direction(symbol: "tram.tunnel.fill", color: .brown, text: "Ride through underground tunnels"),
    Direction(symbol: "key", color: .red, text: "Enter door code:"),
  ]

  var body: some View {
    NavigationView {
      List {
        ForEach($directions) { $direction in
          Label {
            TextField("Instructions", text: $direction.text)
          } icon: {
            DirectionsIcon(direction)
          }
          .listRowSeparator(.hidden)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Secret Hideout")
    }
  }
}

struct Direction: Identifiable {
  var id = UUID()
  var symbol: String
  var color: Color
  var text: String
}

private struct DirectionsIcon: View {
  var direction: Direction

  init(_ direction: Direction) {
    self.direction = direction
  }

  var body: some View {
    Image(systemName: direction.symbol)
      .resizable()
      .aspectRatio(contentMode: .fit)
      .foregroundStyle(.white)
      .padding(6)
      .frame(width: 33, height: 33)
      .background(direction.color, in: RoundedRectangle(cornerRadius: 8))
  }
}
```

### Swipe actions — [10:08]

```swift
struct ContentView: View {
  @State private var characters = CharacterStore(StoryCharacter.previewData)

  var body: some View {
    NavigationView {
      List {
        if !characters.pinned.isEmpty {
          Section("Pinned") {
            sectionContent(for: $characters.pinned)
          }
        }
        Section("Heroes & Villains") {
          sectionContent(for: $characters.unpinned)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Characters")
    }
  }

  @ViewBuilder
  private func sectionContent(for characters: Binding<[StoryCharacter]>) -> some View {
    ForEach(characters) { $character in
      CharacterProfile(character)
        .swipeActions {
          Button {
            togglePinned(for: $character)
          } label: {
            if character.isPinned {
              Label("Unpin", systemImage: "pin.slash")
            } else {
              Label("Pin", systemImage: "pin")
            }
          }
          .tint(.yellow)
        }
    }
  }

  private func togglePinned(for character: Binding<StoryCharacter>) {
    withAnimation {
      var tmp = character.wrappedValue
      tmp.isPinned.toggle()
      tmp.lastModified = Date()
      character.wrappedValue = tmp
    }
  }

  private func delete<C: RangeReplaceableCollection & MutableCollection>(
    _ character: StoryCharacter, in characters: Binding<C>
  ) where C.Element == StoryCharacter {
    withAnimation {
      if let i = characters.wrappedValue.firstIndex(where: {
        $0.id == character.id
      }) {
        characters.wrappedValue.remove(at: i)
      }
    }
  }
}

struct CharacterProfile: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    NavigationLink {
      Text(character.name)
    } label: {
      HStack {
        HStack {
          let symbol = Image(systemName: character.symbol)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .foregroundStyle(.white)
            .padding(6)
            .frame(width: 33, height: 33)

          if character.isVillain {
            symbol
              .background(character.color, in: RoundedRectangle(cornerRadius: 8))
          } else {
            symbol
              .background(character.color, in: Circle())
          }
        }
        VStack(alignment: .leading, spacing: 2) {
          HStack(alignment: .center) {
            Text(character.name)
              .bold()
              .foregroundStyle(.primary)
          }
          HStack(spacing: 4) {
            Text(character.isVillain ? "VILLAIN" : "HERO")
              .bold()
              .font(.caption2.weight(.heavy))
              .foregroundStyle(.white)
              .padding(.vertical, 1)
              .padding(.horizontal, 3)
              .background(.quaternary, in: RoundedRectangle(cornerRadius: 3))

            Text(character.powers)
              .font(.footnote)
              .foregroundStyle(.secondary)
          }
        }
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Swipe actions on the leading edge — [10:27]

```swift
struct ContentView: View {
  @State private var characters = CharacterStore(StoryCharacter.previewData)

  var body: some View {
    NavigationView {
      List {
        if !characters.pinned.isEmpty {
          Section("Pinned") {
            sectionContent(for: $characters.pinned)
          }
        }
        Section("Heroes & Villains") {
          sectionContent(for: $characters.unpinned)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Characters")
    }
  }

  @ViewBuilder
  private func sectionContent(for characters: Binding<[StoryCharacter]>) -> some View {
    ForEach(characters) { $character in
      CharacterProfile(character)
        .swipeActions(edge: .leading) {
          Button {
            togglePinned(for: $character)
          } label: {
            if character.isPinned {
              Label("Unpin", systemImage: "pin.slash")
            } else {
              Label("Pin", systemImage: "pin")
            }
          }
          .tint(.yellow)
        }
    }
  }

  private func togglePinned(for character: Binding<StoryCharacter>) {
    withAnimation {
      var tmp = character.wrappedValue
      tmp.isPinned.toggle()
      tmp.lastModified = Date()
      character.wrappedValue = tmp
    }
  }

  private func delete<C: RangeReplaceableCollection & MutableCollection>(
    _ character: StoryCharacter, in characters: Binding<C>
  ) where C.Element == StoryCharacter {
    withAnimation {
      if let i = characters.wrappedValue.firstIndex(where: {
        $0.id == character.id
      }) {
        characters.wrappedValue.remove(at: i)
      }
    }
  }
}

struct CharacterProfile: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    NavigationLink {
      Text(character.name)
    } label: {
      HStack {
        HStack {
          let symbol = Image(systemName: character.symbol)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .foregroundStyle(.white)
            .padding(6)
            .frame(width: 33, height: 33)

          if character.isVillain {
            symbol
              .background(character.color, in: RoundedRectangle(cornerRadius: 8))
          } else {
            symbol
              .background(character.color, in: Circle())
          }
        }
        VStack(alignment: .leading, spacing: 2) {
          HStack(alignment: .center) {
            Text(character.name)
              .bold()
              .foregroundStyle(.primary)
          }
          HStack(spacing: 4) {
            Text(character.isVillain ? "VILLAIN" : "HERO")
              .bold()
              .font(.caption2.weight(.heavy))
              .foregroundStyle(.white)
              .padding(.vertical, 1)
              .padding(.horizontal, 3)
              .background(.quaternary, in: RoundedRectangle(cornerRadius: 3))

            Text(character.powers)
              .font(.footnote)
              .foregroundStyle(.secondary)
          }
        }
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Swipe actions on both edges — [10:32]

```swift
struct ContentView: View {
  @State private var characters = CharacterStore(StoryCharacter.previewData)

  var body: some View {
    NavigationView {
      List {
        if !characters.pinned.isEmpty {
          Section("Pinned") {
            sectionContent(for: $characters.pinned)
          }
        }
        Section("Heroes & Villains") {
          sectionContent(for: $characters.unpinned)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Characters")
    }
  }

  @ViewBuilder
  private func sectionContent(for characters: Binding<[StoryCharacter]>) -> some View {
    ForEach(characters) { $character in
      CharacterProfile(character)
        .swipeActions(edge: .leading) {
          Button {
            togglePinned(for: $character)
          } label: {
            if character.isPinned {
              Label("Unpin", systemImage: "pin.slash")
            } else {
              Label("Pin", systemImage: "pin")
            }
          }
          .tint(.yellow)
        }
        .swipeActions(edge: .trailing) {
          Button(role: .destructive) {
            delete(character, in: characters)
          } label: {
            Label("Delete", systemImage: "trash")
          }
          Button {
            // Open "More" menu
          } label: {
            Label("More", systemImage: "ellipsis.circle")
          }
          .tint(Color(white: 0.8))
        }
    }
  }

  private func togglePinned(for character: Binding<StoryCharacter>) {
    withAnimation {
      var tmp = character.wrappedValue
      tmp.isPinned.toggle()
      tmp.lastModified = Date()
      character.wrappedValue = tmp
    }
  }

  private func delete<C: RangeReplaceableCollection & MutableCollection>(
    _ character: StoryCharacter, in characters: Binding<C>
  ) where C.Element == StoryCharacter {
    withAnimation {
      if let i = characters.wrappedValue.firstIndex(where: {
        $0.id == character.id
      }) {
        characters.wrappedValue.remove(at: i)
      }
    }
  }
}

struct CharacterProfile: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    NavigationLink {
      Text(character.name)
    } label: {
      HStack {
        HStack {
          let symbol = Image(systemName: character.symbol)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .foregroundStyle(.white)
            .padding(6)
            .frame(width: 33, height: 33)

          if character.isVillain {
            symbol
              .background(character.color, in: RoundedRectangle(cornerRadius: 8))
          } else {
            symbol
              .background(character.color, in: Circle())
          }
        }
        VStack(alignment: .leading, spacing: 2) {
          HStack(alignment: .center) {
            Text(character.name)
              .bold()
              .foregroundStyle(.primary)
          }
          HStack(spacing: 4) {
            Text(character.isVillain ? "VILLAIN" : "HERO")
              .bold()
              .font(.caption2.weight(.heavy))
              .foregroundStyle(.white)
              .padding(.vertical, 1)
              .padding(.horizontal, 3)
              .background(.quaternary, in: RoundedRectangle(cornerRadius: 3))

            Text(character.powers)
              .font(.footnote)
              .foregroundStyle(.secondary)
          }
        }
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Basic macOS list — [11:14]

```swift
struct ContentView: View {
  @State private var characters = StoryCharacter.previewData
  @State private var selection = Set<StoryCharacter.ID>()

  var body: some View {
    List(selection: $selection) {
      ForEach(characters) { character in
        Label {
          Text(character.name)
        } icon: {
          CharacterIcon(character)
        }
        .padding(.leading, 4)
      }
    }
    .listStyle(.inset)
    .navigationTitle("All Characters")
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(4)
        .frame(width: 20, height: 20)

      if character.isVillain {
        symbol
          .background(character.color, in: RoundedRectangle(cornerRadius: 4))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Inset list style alternating row backgrounds — [11:35]

```swift
struct ContentView: View {
  @State private var characters = StoryCharacter.previewData
  @State private var selection = Set<StoryCharacter.ID>()

  var body: some View {
    List(selection: $selection) {
      ForEach(characters) { character in
        Label {
          Text(character.name)
        } icon: {
          CharacterIcon(character)
        }
        .padding(.leading, 4)
      }
    }
    .listStyle(.inset(alternatesRowBackgrounds: true))
    .navigationTitle("All Characters")
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(4)
        .frame(width: 20, height: 20)

      if character.isVillain {
        symbol
          .background(character.color, in: RoundedRectangle(cornerRadius: 4))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Tables — [12:13]

```swift
struct ContentView: View {
  @State private var characters = StoryCharacter.previewData

  var body: some View {
    Table(characters) {
      TableColumn("􀟈") { CharacterIcon($0) }
        .width(20)
      TableColumn("Villain") { Text($0.isVillain ? "Villain" : "Hero") }
        .width(40)
      TableColumn("Name", value: \.name)
      TableColumn("Powers", value: \.powers)
    }
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(4)
        .frame(width: 20, height: 20)

      if character.isVillain {
        symbol
          .background(character.color, in: RoundedRectangle(cornerRadius: 4))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Tables with selection — [12:49]

```swift
struct ContentView: View {
  @State private var characters = StoryCharacter.previewData

  // Single selection
  @State private var singleSelection: StoryCharacter.ID?

  // Multiple selection
  @State private var multipleSelection: Set<StoryCharacter.ID>()

  var body: some View {
    Table(characters, selection: $singleSelection) { // or `$multipleSelection`
      TableColumn("􀟈") { CharacterIcon($0) }
        .width(20)
      TableColumn("Villain") { Text($0.isVillain ? "Villain" : "Hero") }
        .width(40)
      TableColumn("Name", value: \.name)
      TableColumn("Powers", value: \.powers)
    }
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(4)
        .frame(width: 20, height: 20)

      if character.isVillain {
        symbol
          .background(character.color, in: RoundedRectangle(cornerRadius: 4))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Tables with selection and sorting — [12:57]

```swift
struct ContentView: View {
  @State private var characters = StoryCharacter.previewData
  @State private var selection = Set<StoryCharacter.ID>()

  @State private var sortOrder = [KeyPathComparator(\StoryCharacter.name)]
  @State private var sorted: [StoryCharacter]?

  var body: some View {
    Table(sorted ?? characters, selection: $selection, sortOrder: $sortOrder) {
      TableColumn("􀟈") { CharacterIcon($0) }
        .width(20)
      TableColumn("Villain") { Text($0.isVillain ? "Villain" : "Hero") }
        .width(40)
      TableColumn("Name", value: \.name)
      TableColumn("Powers", value: \.powers)
    }
    .onChange(of: characters) { sorted = $0.sorted(using: sortOrder) }
    .onChange(of: sortOrder) { sorted = characters.sorted(using: $0) }
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(4)
        .frame(width: 20, height: 20)

      if character.isVillain {
        symbol
          .background(character.color, in: RoundedRectangle(cornerRadius: 4))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    get {
      all.prefix { $0.isPinned }
    }
    set {
      if let end = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(all.startIndex..<end, with: newValue)
      }
    }
  }

  var unpinned: [StoryCharacter] {
    get {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        return Array(all.suffix(from: start))
      } else {
        return []
      }
    }
    set {
      if let start = all.firstIndex(where: { !$0.isPinned }) {
        all.replaceSubrange(start..<all.endIndex, with: newValue)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### CoreData Tables — [13:15]

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.name)])
private var characters: FetchedResults<StoryCharacter>
@State private var selection = Set<StoryCharacter.ID>()

Table(characters, selection: $selection, sortOrder: $characters.sortDescriptors) {
  TableColumn("􀟈") { CharacterIcon($0) }
    .width(20)
  TableColumn("Villain") { Text($0.isVillain ? "Villain" : "Hero") }
    .width(40)
  TableColumn("Name", value: \.name)
  TableColumn("Powers", value: \.powers)
}
```

### Sectioned fetch requests — [13:34]

```swift
@SectionedFetchRequest(
  sectionIdentifier: \.isPinned,
  sortDescriptors: [
    SortDescriptor(\.isPinned, order: .reverse),
    SortDescriptor(\.lastModified)
  ],
  animation: .default)
private var characters: SectionedFetchResults<...>

List {
  ForEach(characters) { section in
    Section(section.id ? "Pinned" : "Heroes & Villains") {
      ForEach(section) { character in
        CharacterRowView(character)
      }
    }
  }
}
```

### searchable() modifier — [15:20]

```swift
struct ContentView: View {
  @State private var characters = CharacterStore(StoryCharacter.previewData)

  var body: some View {
    NavigationView {
      List {
        if characters.filterText.isEmpty {
          if !characters.pinned.isEmpty {
            Section("Pinned") {
              sectionContent(for: characters.pinned)
            }
          }
          Section("Heroes & Villains") {
            sectionContent(for: characters.unpinned)
          }
        } else {
          sectionContent(for: characters.filtered)
        }
      }
      .listStyle(.sidebar)
      .searchable(text: $characters.filterText)
      .navigationTitle("Characters")
    }
  }

  @ViewBuilder
  private func sectionContent(for characters: [StoryCharacter]) -> some View {
    ForEach(characters) { character in
      CharacterProfile(character)
    }
  }
}

struct CharacterProfile: View {
  var character: StoryCharacter

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    NavigationLink {
      Text(character.name)
    } label: {
      HStack {
        HStack {
          let symbol = Image(systemName: character.symbol)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .foregroundStyle(.white)
            .padding(6)
            .frame(width: 33, height: 33)

          if character.isVillain {
            symbol
              .background(character.color, in: RoundedRectangle(cornerRadius: 8))
          } else {
            symbol
              .background(character.color, in: Circle())
          }
        }
        VStack(alignment: .leading, spacing: 2) {
          HStack(alignment: .center) {
            Text(character.name)
              .bold()
              .foregroundStyle(.primary)
          }
          HStack(spacing: 4) {
            Text(character.isVillain ? "VILLAIN" : "HERO")
              .bold()
              .font(.caption2.weight(.heavy))
              .foregroundStyle(.white)
              .padding(.vertical, 1)
              .padding(.horizontal, 3)
              .background(.quaternary, in: RoundedRectangle(cornerRadius: 3))

            Text(character.powers)
              .font(.footnote)
              .foregroundStyle(.secondary)
          }
        }
      }
    }
  }
}

struct CharacterStore {
  var all: [StoryCharacter] {
    get { _all }
    set { _all = newValue; sortAll() }
  }
  var _all: [StoryCharacter]

  var pinned: [StoryCharacter] {
    all.prefix { $0.isPinned }
  }

  var unpinned: [StoryCharacter] {
    if let start = all.firstIndex(where: { !$0.isPinned }) {
      return Array(all.suffix(from: start))
    } else {
      return []
    }
  }

  var filterText: String = ""
  var filtered: [StoryCharacter] {
    if filterText.isEmpty {
      return all
    } else {
      return all.filter {
        $0.name.contains(filterText) || $0.powers.contains(filterText)
      }
    }
  }

  init(_ characters: [StoryCharacter]) {
    _all = characters
    sortAll()
  }

  private mutating func sortAll() {
    _all.sort { lhs, rhs in
      if lhs.isPinned && !rhs.isPinned {
        return true
      } else if !lhs.isPinned && rhs.isPinned {
        return false
      } else {
        return lhs.lastModified < rhs.lastModified
      }
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
}

extension StoryCharacter {
  static let previewData: [StoryCharacter] = [
    StoryCharacter(
      id: 0,
      name: "The View Builder",
      symbol: "hammer",
      color: .pink,
      powers: "Conjures objects on-demand.",
      isPinned: true),
    StoryCharacter(
      id: 1,
      name: "The Truth Duplicator",
      symbol: "eyes",
      color: .blue,
      powers: "Distorts reality.",
      isVillain: true),
    StoryCharacter(
      id: 2,
      name: "The Previewer",
      symbol: "viewfinder",
      color: .indigo,
      powers: "Reveals the future.",
      isPinned: true),
    StoryCharacter(
      id: 3,
      name: "The Type Eraser",
      symbol: "eye.slash",
      color: .black,
      powers: "Steals identities.",
      isVillain: true,
      isPinned: true),
    StoryCharacter(
      id: 4,
      name: "The Environment Modifier",
      symbol: "leaf",
      color: .green,
      powers: "Controls the physical world."),
    StoryCharacter(
      id: 5,
      name: "The Unstable Identifier",
      symbol: "shuffle",
      color: .brown,
      powers: "Shape-shifter, uncatchable.",
      isVillain: true),
    StoryCharacter(
      id: 6,
      name: "The Stylizer",
      symbol: "wand.and.stars.inverse",
      color: .red,
      powers: "Quartermaster of heroes."),
    StoryCharacter(
      id: 7,
      name: "The Singleton",
      symbol: "diamond",
      color: .purple,
      powers: "An evil robotic hive mind.",
      isVillain: true),
    StoryCharacter(
      id: 8,
      name: "The Geometry Reader",
      symbol: "ruler",
      color: .orange,
      powers: "Instantly scans any structure."),
    StoryCharacter(
      id: 9,
      name: "The Opaque Typist",
      symbol: "app.fill",
      color: .teal,
      powers: "Creates impenetrable disguises."),
    StoryCharacter(
      id: 10,
      name: "The Unobservable Man",
      symbol: "hand.raised.slash",
      color: .black,
      powers: "Impervious to detection.",
      isVillain: true),
  ]
}
```

### Drag previews — [16:22]

```swift
struct ContentView: View {
  let character = StoryCharacter(
    id: 0,
    name: "The View Builder",
    symbol: "hammer",
    color: .pink,
    powers: "Conjures objects on-demand.",
    isPinned: true
  )

  var body: some View {
    CharacterIcon(character)
      .controlSize(.large)
      .padding()
      .onDrag {
        character.itemProvider
      } preview: {
        Label {
          Text(character.name)
        } icon: {
          CharacterIcon(character)
            .controlSize(.small)
        }
        .padding(.vertical, 8)
        .frame(width: 150)
        .background(.white, in: RoundedRectangle(cornerRadius: 8))
      }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()

  var itemProvider: NSItemProvider {
    let item = NSItemProvider()
    item.registerObject(name as NSString, visibility: .all)
    return item
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  #if os(iOS) || os(macOS)
  @Environment(\.controlSize) private var controlSize
  #endif

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(symbolPadding)
        .frame(width: symbolLength, height: symbolLength)

      if character.isVillain {
        symbol
          .background(
            character.color, in: RoundedRectangle(cornerRadius: cornerRadius))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }

  var symbolPadding: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 10
    default: return 6
    }
  }

  var symbolLength: CGFloat {
    switch controlSize {
    case .small: return 20
    case .large: return 60
    default: return 33
    }
  }

  var cornerRadius: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 16
    default: return 8
    }
  }
}
```

### importsItemProviders() modifier — [16:48]

```swift
import UniformTypeIdentifiers

@main
private struct Catalog: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .commands {
      ImportFromDevicesCommands()
    }
  }
}

struct ContentView: View {
  @State private var character: StoryCharacter = StoryCharacter(
    id: 0,
    name: "The View Builder",
    symbol: "hammer",
    color: .pink,
    powers: "Conjures objects on-demand.",
    isPinned: true
  )

  var body: some View {
    VStack {
      CharacterIcon(character)
        .controlSize(.large)
        .onDrag {
          character.itemProvider
        } preview: {
          Label {
            Text(character.name)
          } icon: {
            CharacterIcon(character)
              .controlSize(.small)
          }
          .padding(.vertical, 8)
          .frame(width: 150)
          .background(.white, in: RoundedRectangle(cornerRadius: 8))
        }

      if let headerImage = character.headerImage {
        headerImage
          .resizable()
          .aspectRatio(contentMode: .fill)
          .frame(width: 150, height: 150)
          .mask(RoundedRectangle(cornerRadius: 16, style: .continuous))
      }
    }
    .padding()
    .importsItemProviders(StoryCharacter.headerImageTypes) { itemProviders in
      guard let first = itemProviders.first else { return false }
      async {
        character.headerImage = await StoryCharacter.loadHeaderImage(from: first)
      }
      return true
    }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
  var headerImage: Image?

  static var headerImageTypes: [UTType] {
    NSImage.imageTypes.compactMap { UTType($0) }
  }

  var itemProvider: NSItemProvider {
    let item = NSItemProvider()
    item.registerObject(name as NSString, visibility: .all)
    return item
  }

  static func loadHeaderImage(from itemProvider: NSItemProvider) async -> Image? {
    for type in Self.headerImageTypes.map(\.identifier) {
      if itemProvider.hasRepresentationConforming(toTypeIdentifier: type) {
        return await withCheckedContinuation { continuation in
          itemProvider.loadDataRepresentation(forTypeIdentifier: type) { data, error in
            guard let data = data, let image = NSImage(data: data) else { return }
            continuation.resume(returning: Image(nsImage: image))
          }
        }
      }
    }
    return nil
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  #if os(iOS) || os(macOS)
  @Environment(\.controlSize) private var controlSize
  #endif

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(symbolPadding)
        .frame(width: symbolLength, height: symbolLength)

      if character.isVillain {
        symbol
          .background(
            character.color, in: RoundedRectangle(cornerRadius: cornerRadius))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }

  var symbolPadding: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 10
    default: return 6
    }
  }

  var symbolLength: CGFloat {
    switch controlSize {
    case .small: return 20
    case .large: return 60
    default: return 33
    }
  }

  var cornerRadius: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 16
    default: return 8
    }
  }
}
```

### exportsItemProviders() modifier — [18:17]

```swift
import UniformTypeIdentifiers

@main
private struct Catalog: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
    }
    .commands {
      ImportFromDevicesCommands()
    }
  }
}

struct ContentView: View {
  @State private var character: StoryCharacter = StoryCharacter(
    id: 0,
    name: "The View Builder",
    symbol: "hammer",
    color: .pink,
    powers: "Conjures objects on-demand.",
    isPinned: true
  )

  var body: some View {
    VStack {
      CharacterIcon(character)
        .controlSize(.large)
        .onDrag {
          character.itemProvider
        } preview: {
          Label {
            Text(character.name)
          } icon: {
            CharacterIcon(character)
              .controlSize(.small)
          }
          .padding(.vertical, 8)
          .frame(width: 150)
          .background(.white, in: RoundedRectangle(cornerRadius: 8))
        }

      if let headerImage = character.headerImage {
        headerImage
          .resizable()
          .aspectRatio(contentMode: .fill)
          .frame(width: 150, height: 150)
          .mask(RoundedRectangle(cornerRadius: 16, style: .continuous))
      }
    }
    .padding()
    .importsItemProviders(StoryCharacter.headerImageTypes) { itemProviders in
      guard let first = itemProviders.first else { return false }
      async {
        character.headerImage = await StoryCharacter.loadHeaderImage(from: first)
      }
      return true
    }
    .exportsItemProviders(StoryCharacter.contentTypes) { [character.itemProvider] }
  }
}

struct StoryCharacter: Identifiable, Equatable {
  var id: Int64
  var name: String
  var symbol: String
  var color: Color
  var powers: String
  var isVillain: Bool = false
  var isPinned: Bool = false
  var lastModified = Date()
  var headerImage: Image?

  static var contentTypes: [UTType] { [.utf8PlainText] }
  static var headerImageTypes: [UTType] {
    NSImage.imageTypes.compactMap { UTType($0) }
  }

  var itemProvider: NSItemProvider {
    let item = NSItemProvider()
    item.registerObject(name as NSString, visibility: .all)
    return item
  }

  static func loadHeaderImage(from itemProvider: NSItemProvider) async -> Image? {
    for type in Self.headerImageTypes.map(\.identifier) {
      if itemProvider.hasRepresentationConforming(toTypeIdentifier: type) {
        return await withCheckedContinuation { continuation in
          itemProvider.loadDataRepresentation(forTypeIdentifier: type) { data, error in
            guard let data = data, let image = NSImage(data: data) else { return }
            continuation.resume(returning: Image(nsImage: image))
          }
        }
      }
    }
    return nil
  }
}

struct CharacterIcon: View {
  var character: StoryCharacter

  #if os(iOS) || os(macOS)
  @Environment(\.controlSize) private var controlSize
  #endif

  init(_ character: StoryCharacter) {
    self.character = character
  }

  var body: some View {
    HStack {
      let symbol = Image(systemName: character.symbol)
        .resizable()
        .aspectRatio(contentMode: .fit)
        .foregroundStyle(.white)
        .padding(symbolPadding)
        .frame(width: symbolLength, height: symbolLength)

      if character.isVillain {
        symbol
          .background(
            character.color, in: RoundedRectangle(cornerRadius: cornerRadius))
      } else {
        symbol
          .background(character.color, in: Circle())
      }
    }
  }

  var symbolPadding: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 10
    default: return 6
    }
  }

  var symbolLength: CGFloat {
    switch controlSize {
    case .small: return 20
    case .large: return 60
    default: return 33
    }
  }

  var cornerRadius: CGFloat {
    switch controlSize {
    case .small: return 4
    case .large: return 16
    default: return 8
    }
  }
}
```

### Symbol rendering modes — [19:47]

```swift
struct ContentView: View {
    var body: some View {
        VStack {
            HStack { symbols }
                .symbolRenderingMode(.monochrome)
            HStack { symbols }
                .symbolRenderingMode(.multicolor)
            HStack { symbols }
                .symbolRenderingMode(.hierarchical)
            HStack { symbols }
                .symbolRenderingMode(.palette)
                .foregroundStyle(Color.cyan, Color.purple)
        }
        .foregroundStyle(.blue)
        .font(.title)
    }
    @ViewBuilder var symbols: some View {
        Group {
            Image(systemName: "exclamationmark.triangle.fill")
            Image(systemName: "pc")
            Image(systemName: "phone.down.circle")
            Image(systemName: "hourglass")
            Image(systemName: "heart.fill")
            Image(systemName: "airplane.circle.fill")
        }
        .frame(width: 40, height: 40)
    }
}
```

### Symbol variants — [20:27]

```swift
struct ContentView: View {
    var body: some View {
        VStack {
            HStack { symbols }
            HStack { symbols }
                .symbolVariant(.fill)
        }
        .foregroundStyle(.blue)
    }
    @ViewBuilder var symbols: some View {
        let heart = Image(systemName: "heart")
        Group {
            heart
            heart.symbolVariant(.slash)
            heart.symbolVariant(.circle)
            heart.symbolVariant(.square)
            heart.symbolVariant(.rectangle)
        }
        .frame(width: 40, height: 40)
    }
}
```

### Tab symbol variants: iOS 13 — [20:42]

```swift
struct TabExample: View {
    var body: some View {
        TabView {
            CardsView().tabItem {
                Label("Cards", systemImage: "rectangle.portrait.on.rectangle.portrait.fill")
            }
            RulesView().tabItem {
                Label("Rules", systemImage: "character.book.closed.fill")
            }
            ProfileView().tabItem {
                Label("Profile", systemImage: "person.circle.fill")
            }
            SearchPlayersView().tabItem {
                Label("Magic", systemImage: "sparkles")
            }
        }
    }
}

struct CardsView: View {
    var body: some View { Color.clear }
}
struct RulesView: View {
    var body: some View { Color.clear }
}
struct ProfileView: View {
    var body: some View { Color.clear }
}
struct SearchPlayersView: View {
    var body: some View { Color.clear }
}
```

### Tab symbol variants — [20:50]

```swift
@main
struct SnippetsApp: App {
    var body: some Scene {
        WindowGroup {
            #if os(iOS)
            TabExample()
            #else
            VStack{
                Text("Open Preferences")
                Text("⌘,").font(.title.monospaced())
            }
            .fixedSize()
            .scenePadding()
            #endif
        }

        #if os(macOS)
        Settings {
            TabExample()
        }
        #endif
    }
}


struct TabExample: View {
    var body: some View {
        TabView {
            CardsView().tabItem {
                Label("Cards", systemImage: "rectangle.portrait.on.rectangle.portrait")
            }
            RulesView().tabItem {
                Label("Rules", systemImage: "character.book.closed")
            }
            ProfileView().tabItem {
                Label("Profile", systemImage: "person.circle")
            }
            SearchPlayersView().tabItem {
                Label("Magic", systemImage: "sparkles")
            }
        }
    }
}

struct CardsView: View {
    var body: some View { Color.clear }
}
struct RulesView: View {
    var body: some View { Color.clear }
}
struct ProfileView: View {
    var body: some View { Color.clear }
}
struct SearchPlayersView: View {
    var body: some View { Color.clear }
}
```

### Canvas — [21:31]

```swift
struct ContentView: View {
    let symbols = Array(repeating: Symbol("swift"), count: 3166)

    var body: some View {
        Canvas { context, size in
            let metrics = gridMetrics(in: size)
            for (index, symbol) in symbols.enumerated() {
                let rect = metrics[index]
                let image = context.resolve(symbol.image)
                context.draw(image, in: rect.fit(image.size))
            }
        }
    }

    func gridMetrics(in size: CGSize) -> SymbolGridMetrics {
        SymbolGridMetrics(size: size, numberOfSymbols: symbols.count)
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}

struct SymbolGridMetrics {
    let symbolWidth: CGFloat
    let symbolsPerRow: Int
    let numberOfSymbols: Int
    let insetProportion: CGFloat

    init(size: CGSize, numberOfSymbols: Int, insetProportion: CGFloat = 0.1) {
        let areaPerSymbol = (size.width * size.height) / CGFloat(numberOfSymbols)
        self.symbolsPerRow = Int(size.width / sqrt(areaPerSymbol))
        self.symbolWidth = size.width / CGFloat(symbolsPerRow)
        self.numberOfSymbols = numberOfSymbols
        self.insetProportion = insetProportion
    }

    /// Returns the frame in the grid for the symbol at `index` position.
    /// It is not valid to pass an index less than `0` or larger than the number of symbols the grid metrics was created for.
    subscript(_ index: Int) -> CGRect {
        precondition(index >= 0 && index < numberOfSymbols)
        let row = index / symbolsPerRow
        let column = index % symbolsPerRow
        let rect = CGRect(
            x: CGFloat(column) * symbolWidth,
            y: CGFloat(row) * symbolWidth,
            width: symbolWidth, height: symbolWidth)
        return rect.insetBy(dx: symbolWidth * insetProportion, dy: symbolWidth * insetProportion)
    }
}

extension CGRect {
    /// Returns a rect with the aspect ratio of `otherSize`, fitting within `self`.
    func fit(_ otherSize: CGSize) -> CGRect {
        let scale = min(size.width / otherSize.width, size.height / otherSize.height)
        let newSize = CGSize(width: otherSize.width * scale, height: otherSize.height * scale)
        let newOrigin = CGPoint(x: midX - newSize.width/2, y: midY - newSize.height/2)
        return CGRect(origin: newOrigin, size: newSize)
    }
}
```

### Canvas with gesture — [22:03]

```swift
struct ContentView: View {
    let symbols = Array(repeating: Symbol("swift"), count: 3166)
    @GestureState private var focalPoint: CGPoint? = nil

    var body: some View {
        Canvas { context, size in
            let metrics = gridMetrics(in: size)
            for (index, symbol) in symbols.enumerated() {
                let rect = metrics[index]
                let (sRect, opacity) = rect.fishEyeTransform(around: focalPoint)

                context.opacity = opacity
                let image = context.resolve(symbol.image)
                context.draw(image, in: sRect.fit(image.size))
            }
        }
        .gesture(DragGesture(minimumDistance: 0).updating($focalPoint) { value, focalPoint, _ in
            focalPoint = value.location
        })
    }

    func gridMetrics(in size: CGSize) -> SymbolGridMetrics {
        SymbolGridMetrics(size: size, numberOfSymbols: symbols.count)
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}

struct SymbolGridMetrics {
    let symbolWidth: CGFloat
    let symbolsPerRow: Int
    let numberOfSymbols: Int
    let insetProportion: CGFloat

    init(size: CGSize, numberOfSymbols: Int, insetProportion: CGFloat = 0.1) {
        let areaPerSymbol = (size.width * size.height) / CGFloat(numberOfSymbols)
        self.symbolsPerRow = Int(size.width / sqrt(areaPerSymbol))
        self.symbolWidth = size.width / CGFloat(symbolsPerRow)
        self.numberOfSymbols = numberOfSymbols
        self.insetProportion = insetProportion
    }

    /// Returns the frame in the grid for the symbol at `index` position.
    /// It is not valid to pass an index less than `0` or larger than the number of symbols the grid metrics was created for.
    subscript(_ index: Int) -> CGRect {
        precondition(index >= 0 && index < numberOfSymbols)
        let row = index / symbolsPerRow
        let column = index % symbolsPerRow
        let rect = CGRect(
            x: CGFloat(column) * symbolWidth,
            y: CGFloat(row) * symbolWidth,
            width: symbolWidth, height: symbolWidth)
        return rect.insetBy(dx: symbolWidth * insetProportion, dy: symbolWidth * insetProportion)
    }
}

extension CGRect {
    /// Returns a rect with the aspect ratio of `otherSize`, fitting within `self`.
    func fit(_ otherSize: CGSize) -> CGRect {
        let scale = min(size.width / otherSize.width, size.height / otherSize.height)
        let newSize = CGSize(width: otherSize.width * scale, height: otherSize.height * scale)
        let newOrigin = CGPoint(x: midX - newSize.width/2, y: midY - newSize.height/2)
        return CGRect(origin: newOrigin, size: newSize)
    }

    /// Returns a transformed rect and relative opacity based on a fish eye effect centered around `point`.
    /// The rectangles closer to the center of that point will be larger and brighter, and those further away will be smaller, up to a distance of `radius`.
    func fishEyeTransform(around point: CGPoint?, radius: CGFloat = 300, zoom: CGFloat = 1.0) -> (frame: CGRect, opacity: CGFloat) {
        guard let point = point else {
            return (self, 1.0)
        }

        let deltaX = midX - point.x
        let deltaY = midY - point.y
        let distance = sqrt(deltaX*deltaX + deltaY*deltaY)
        let theta = atan2(deltaY, deltaX)

        let scaledClampedDistance = pow(min(1, max(0, distance/radius)), 0.7)
        let scale = (1.0 - scaledClampedDistance)*zoom + 0.5

        let newOffset = distance * (2.0 - scaledClampedDistance)*sqrt(zoom)
        let newDeltaX = newOffset * cos(theta)
        let newDeltaY = newOffset * sin(theta)

        let newSize = CGSize(width: size.width * scale, height: size.height * scale)
        let newOrigin = CGPoint(x: (newDeltaX + point.x) - newSize.width/2, y: (newDeltaY + point.y) - newSize.height/2)

        // Clamp the opacity to be 0.1 at the lowest
        let opacity = max(0.1, 1.0 - scaledClampedDistance)
        return (CGRect(origin: newOrigin, size: newSize), opacity)
    }
}
```

### Canvas with accessibility children — [22:24]

```swift
struct ContentView: View {
    let symbols = Array(repeating: Symbol("swift"), count: 3166)
    @GestureState private var focalPoint: CGPoint? = nil

    var body: some View {
        Canvas { context, size in
            let metrics = gridMetrics(in: size)
            for (index, symbol) in symbols.enumerated() {
                let rect = metrics[index]
                let (sRect, opacity) = rect.fishEyeTransform(around: focalPoint)

                context.opacity = opacity
                let image = context.resolve(symbol.image)
                context.draw(image, in: sRect.fit(image.size))
            }
        }
        .gesture(DragGesture(minimumDistance: 0).updating($focalPoint) { value, focalPoint, _ in
            focalPoint = value.location
        })
        .accessibilityLabel("Symbol Browser")
        .accessibilityChildren {
            List(symbols) {
                Text($0.name)
            }
        }
    }

    func gridMetrics(in size: CGSize) -> SymbolGridMetrics {
        SymbolGridMetrics(size: size, numberOfSymbols: symbols.count)
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}

struct SymbolGridMetrics {
    let symbolWidth: CGFloat
    let symbolsPerRow: Int
    let numberOfSymbols: Int
    let insetProportion: CGFloat

    init(size: CGSize, numberOfSymbols: Int, insetProportion: CGFloat = 0.1) {
        let areaPerSymbol = (size.width * size.height) / CGFloat(numberOfSymbols)
        self.symbolsPerRow = Int(size.width / sqrt(areaPerSymbol))
        self.symbolWidth = size.width / CGFloat(symbolsPerRow)
        self.numberOfSymbols = numberOfSymbols
        self.insetProportion = insetProportion
    }

    /// Returns the frame in the grid for the symbol at `index` position.
    /// It is not valid to pass an index less than `0` or larger than the number of symbols the grid metrics was created for.
    subscript(_ index: Int) -> CGRect {
        precondition(index >= 0 && index < numberOfSymbols)
        let row = index / symbolsPerRow
        let column = index % symbolsPerRow
        let rect = CGRect(
            x: CGFloat(column) * symbolWidth,
            y: CGFloat(row) * symbolWidth,
            width: symbolWidth, height: symbolWidth)
        return rect.insetBy(dx: symbolWidth * insetProportion, dy: symbolWidth * insetProportion)
    }
}

extension CGRect {
    /// Returns a rect with the aspect ratio of `otherSize`, fitting within `self`.
    func fit(_ otherSize: CGSize) -> CGRect {
        let scale = min(size.width / otherSize.width, size.height / otherSize.height)
        let newSize = CGSize(width: otherSize.width * scale, height: otherSize.height * scale)
        let newOrigin = CGPoint(x: midX - newSize.width/2, y: midY - newSize.height/2)
        return CGRect(origin: newOrigin, size: newSize)
    }

    /// Returns a transformed rect and relative opacity based on a fish eye effect centered around `point`.
    /// The rectangles closer to the center of that point will be larger and brighter, and those further away will be smaller, up to a distance of `radius`.
    func fishEyeTransform(around point: CGPoint?, radius: CGFloat = 300, zoom: CGFloat = 1.0) -> (frame: CGRect, opacity: CGFloat) {
        guard let point = point else {
            return (self, 1.0)
        }

        let deltaX = midX - point.x
        let deltaY = midY - point.y
        let distance = sqrt(deltaX*deltaX + deltaY*deltaY)
        let theta = atan2(deltaY, deltaX)

        let scaledClampedDistance = pow(min(1, max(0, distance/radius)), 0.7)
        let scale = (1.0 - scaledClampedDistance)*zoom + 0.5

        let newOffset = distance * (2.0 - scaledClampedDistance)*sqrt(zoom)
        let newDeltaX = newOffset * cos(theta)
        let newDeltaY = newOffset * sin(theta)

        let newSize = CGSize(width: size.width * scale, height: size.height * scale)
        let newOrigin = CGPoint(x: (newDeltaX + point.x) - newSize.width/2, y: (newDeltaY + point.y) - newSize.height/2)

        // Clamp the opacity to be 0.1 at the lowest
        let opacity = max(0.1, 1.0 - scaledClampedDistance)
        return (CGRect(origin: newOrigin, size: newSize), opacity)
    }
}
```

### Canvas with TimelineView — [22:48]

```swift
struct ContentView: View {
    let symbols = Array(repeating: Symbol("swift"), count: 3166)

    var body: some View {
        TimelineView(.animation) {
           let time = $0.date.timeIntervalSince1970
           Canvas { context, size in
              let metrics = gridMetrics(in: size)
              let focalPoint = focalPoint(at: time, in: size)
              for (index, symbol) in symbols.enumerated() {
                let rect = metrics[index]
                let (sRect, opacity) = rect.fishEyeTransform(
                   around: focalPoint, at: time)

                 context.opacity = opacity
                 let image = context.resolve(symbol.image)
                 context.draw(image, in: sRect.fit(image.size))
              }
           }
        }
    }

    func gridMetrics(in size: CGSize) -> SymbolGridMetrics {
        SymbolGridMetrics(size: size, numberOfSymbols: symbols.count)
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}

struct SymbolGridMetrics {
    let symbolWidth: CGFloat
    let symbolsPerRow: Int
    let numberOfSymbols: Int
    let insetProportion: CGFloat

    init(size: CGSize, numberOfSymbols: Int, insetProportion: CGFloat = 0.1) {
        let areaPerSymbol = (size.width * size.height) / CGFloat(numberOfSymbols)
        self.symbolsPerRow = Int(size.width / sqrt(areaPerSymbol))
        self.symbolWidth = size.width / CGFloat(symbolsPerRow)
        self.numberOfSymbols = numberOfSymbols
        self.insetProportion = insetProportion
    }

    /// Returns the frame in the grid for the symbol at `index` position.
    /// It is not valid to pass an index less than `0` or larger than the number of symbols the grid metrics was created for.
    subscript(_ index: Int) -> CGRect {
        precondition(index >= 0 && index < numberOfSymbols)
        let row = index / symbolsPerRow
        let column = index % symbolsPerRow
        let rect = CGRect(
            x: CGFloat(column) * symbolWidth,
            y: CGFloat(row) * symbolWidth,
            width: symbolWidth, height: symbolWidth)
        return rect.insetBy(dx: symbolWidth * insetProportion, dy: symbolWidth * insetProportion)
    }
}

extension CGRect {
    /// Returns a rect with the aspect ratio of `otherSize`, fitting within `self`.
    func fit(_ otherSize: CGSize) -> CGRect {
        let scale = min(size.width / otherSize.width, size.height / otherSize.height)
        let newSize = CGSize(width: otherSize.width * scale, height: otherSize.height * scale)
        let newOrigin = CGPoint(x: midX - newSize.width/2, y: midY - newSize.height/2)
        return CGRect(origin: newOrigin, size: newSize)
    }

    /// Returns a transformed rect and relative opacity based on a fish eye effect centered around `point`.
    /// The rectangles closer to the center of that point will be larger and brighter, and those further away will be smaller, up to a distance of `radius`.
    func fishEyeTransform(around point: CGPoint?, radius: CGFloat = 200, zoom: CGFloat = 3.0) -> (frame: CGRect, opacity: CGFloat) {
        guard let point = point else {
            return (self, 1.0)
        }

        let deltaX = midX - point.x
        let deltaY = midY - point.y
        let distance = sqrt(deltaX*deltaX + deltaY*deltaY)
        let theta = atan2(deltaY, deltaX)

        let scaledClampedDistance = pow(min(1, max(0, distance/radius)), 0.7)
        let scale = (1.0 - scaledClampedDistance)*zoom + 0.5

        let newOffset = distance * (2.0 - scaledClampedDistance)*sqrt(zoom)
        let newDeltaX = newOffset * cos(theta)
        let newDeltaY = newOffset * sin(theta)

        let newSize = CGSize(width: size.width * scale, height: size.height * scale)
        let newOrigin = CGPoint(x: (newDeltaX + point.x) - newSize.width/2, y: (newDeltaY + point.y) - newSize.height/2)

        // Clamp the opacity to be 0.1 at the lowest
        let opacity = max(0.1, 1.0 - scaledClampedDistance)
        return (CGRect(origin: newOrigin, size: newSize), opacity)
    }

    /// Returns a transformed rect and relative opacity based on a fish eye effect centered around `point`, based on a preset path indexed using `time`.
    func fishEyeTransform(around point: CGPoint, at time: TimeInterval) -> (frame: CGRect, opacity: CGFloat) {
        // Arbitrary zoom and radius calculation based on time
        let zoom = cos(time) + 3.0
        let radius = ((cos(time/5) + 1)/2) * 150 + 150
        return fishEyeTransform(around: point, radius: radius, zoom: zoom)
    }
}

/// Returns a focal point within `size` based on a preset path, indexed using `time`.
func focalPoint(at time: TimeInterval, in size: CGSize) -> CGPoint {
   let offset: CGFloat = min(size.width, size.height)/4
   let distance = ((sin(time/5) + 1)/2) * offset + offset
   let scalePoint = CGPoint(x: size.width / 2 + distance * cos(time / 2), y: size.height / 2 + distance * sin(time / 2))
   return scalePoint
}
```

### Privacy sensitive — [24:10]

```swift
Button {
    showFavoritePicker = true
} label: {
    VStack(alignment: .center) {
        Text("Favorite Symbol")
            .foregroundStyle(.secondary)
        Image(systemName: favoriteSymbol)
            .font(.title2)
            .privacySensitive(true)
   }
}
.tint(.purple)
```

### Privacy sensitive (widgets) — [24:27]

```swift
VStack(alignment: .leading) {
    Text("Favorite Symbol")
        .textCase(.uppercase)
        .font(.caption.bold())

    ContainerRelativeShape()
        .fill(.quaternary)
        .overlay {
            Image(systemName: favoriteSymbol)
                .font(.system(size: 40))
                .privacySensitive(true)
        }
}
```

### Materials — [25:03]

```swift
struct ColorList: View {
    let symbols = Array(repeating: Symbol("swift"), count: 3166)

    var body: some View {
        ZStack {
            gradientBackground
            materialOverlay
        }
    }

    var materialOverlay: some View {
        VStack {
           Text("Symbol Browser")
              .font(.largeTitle.bold())
           Text("\(symbols.count) symbols 🎉")
              .foregroundStyle(.secondary)
              .font(.title2.bold())
        }
        .padding()
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 16.0))
    }

    var gradientBackground: some View {
        LinearGradient(
            gradient: Gradient(colors: [.red, .orange, .yellow, .green, .blue, .indigo, .purple]),
            startPoint: .leading, endPoint: .trailing)
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}
```

### Safe area inset — [25:40]

```swift
struct ContentView: View {
    let newSymbols = Array(repeating: Symbol("swift"), count: 645)
    let systemColors: [Color] = [.red, .orange, .yellow, .green, .mint, .teal, .cyan, .blue, .indigo, .purple, .pink, .gray, .brown]

    var body: some View {
        ScrollView {
            symbolGrid
        }
        .safeAreaInset(edge: .bottom, spacing: 0) {
            VStack(spacing: 0) {
                Divider()
                VStack(spacing: 0) {
                    Text("\(newSymbols.count) new symbols")
                        .foregroundStyle(.primary)
                        .font(.body.bold())
                    Text("\(systemColors.count) system colors")
                        .foregroundStyle(.secondary)
                }
                .padding()
            }
            .background(.regularMaterial)
        }
    }

    var symbolGrid: some View {
        LazyVGrid(columns: [.init(.adaptive(minimum: 40, maximum: 40))]) {
            ForEach(0 ..< newSymbols.count, id: \.self) { index in
                newSymbols[index].image
                    .foregroundStyle(.white)
                    .frame(width: 40, height: 40)
                    .background(systemColors[index % systemColors.count])
            }
        }
        .padding()
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}
```

### Preview orientation — [26:03]

```swift
struct ColorList_Previews: PreviewProvider {
    static var previews: some View {
        ColorList()
            .previewInterfaceOrientation(.portrait)

        ColorList()
            .previewInterfaceOrientation(.landscapeLeft)
    }
}

struct ColorList: View {
    let newSymbols = Array(repeating: Symbol("swift"), count: 645)
    let systemColors: [Color] = [.red, .orange, .yellow, .green, .mint, .teal, .cyan, .blue, .indigo, .purple, .pink, .gray, .brown]

    var body: some View {
        ScrollView {
            symbolGrid
        }
        .safeAreaInset(edge: .bottom, spacing: 0) {
            VStack(spacing: 0) {
                Divider()
                VStack(spacing: 0) {
                    Text("\(newSymbols.count) new symbols")
                        .foregroundStyle(.primary)
                        .font(.body.bold())
                    Text("\(systemColors.count) system colors")
                        .foregroundStyle(.secondary)
                }
                .padding()
            }
            .background(.regularMaterial)
        }
    }

    var symbolGrid: some View {
        LazyVGrid(columns: [.init(.adaptive(minimum: 40, maximum: 40))]) {
            ForEach(0 ..< newSymbols.count, id: \.self) { index in
                newSymbols[index].image
                    .foregroundStyle(.white)
                    .frame(width: 40, height: 40)
                    .background(systemColors[index % systemColors.count])
            }
        }
        .padding()
    }
}

struct Symbol: Identifiable {
    let name: String
    init(_ name: String) { self.name = name }

    var image: Image { Image(systemName: name) }
    var id: String { name }
}
```

### Hello, World! — [27:06]

```swift
Text("Hello, World!")
```

### Markdown Text: strong emphasis — [27:17]

```swift
Text("**Hello**, World!")
```

### Markdown Text: links — [27:24]

```swift
Text("**Hello**, World!")
Text("""
Have a *happy* [WWDC](https://developer.apple.com/wwdc21/)!
""")
```

### Markdown Text: inline code — [27:30]

```swift
Text("""
Is this *too* meta?

`Text("**Hello**, World!")`
`Text(\"\"\"`
`Have a *happy* [WWDC](https://developer.apple.com/wwdc21/)!`
`\"\"\")`
""")
```

### AttributedString — [27:37]

```swift
struct ContentView: View {
    var body: some View {
        Text(formattedDate)
    }

    var formattedDate: AttributedString {
        var formattedDate: AttributedString = Date().formatted(Date.FormatStyle().day().month(.wide).weekday(.wide).attributed)

        let weekday = AttributeContainer.dateField(.weekday)
        let color = AttributeContainer.foregroundColor(.orange)
        formattedDate.replaceAttributes(weekday, with: color)

        return formattedDate
    }
}
```

### Text selection — [29:17]

```swift
struct ContentView: View {
    var activity: Activity = .sample

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ActivityHeader(activity)
            Divider()
            Text(activity.info)
                .textSelection(.enabled)
                .padding()
            Spacer()
        }
        .background()
        .navigationTitle(activity.name)
    }
}

struct ActivityHeader: View {
    var activity: Activity
    init(_ activity: Activity) { self.activity = activity }

    var body: some View {
        VStack(alignment: alignment.horizontal, spacing: 8) {
            HStack(alignment: .firstTextBaseline) {
#if os(macOS)
                Text(activity.name)
                    .font(.title2.bold())
                Spacer()
#endif
                Text(activity.date.formatted(.dateTime.weekday(.wide).day().month().hour().minute()))
                    .foregroundStyle(.secondary)
            }
            HStack(alignment: .firstTextBaseline) {
                Image(systemName: "person.2")
                Text(activity.people.map(\.nameComponents).formatted(.list(memberStyle: .name(style: .short), type: .and)))
            }
        }
#if os(macOS)
        .padding()
#else
        .padding([.horizontal, .bottom])
#endif
        .frame(maxWidth: .infinity, alignment: alignment)
        .background(activity.tint.opacity(0.1).ignoresSafeArea())
    }

    private var alignment: Alignment {
#if os(macOS)
        .leading
#else
        .center
#endif
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")
}

struct Person {
    var givenName: String
    var familyName: String = ""

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Text selection: view hierarchy — [29:28]

```swift
struct ContentView: View {
    var activity: Activity = .sample

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ActivityHeader(activity)
            Divider()
            Text(activity.info)
                .padding()
            Spacer()
        }
        .textSelection(.enabled)
        .background()
        .navigationTitle(activity.name)
    }
}

struct ActivityHeader: View {
    var activity: Activity
    init(_ activity: Activity) { self.activity = activity }

    var body: some View {
        VStack(alignment: alignment.horizontal, spacing: 8) {
            HStack(alignment: .firstTextBaseline) {
#if os(macOS)
                Text(activity.name)
                    .font(.title2.bold())
                Spacer()
#endif
                Text(activity.date.formatted(.dateTime.weekday(.wide).day().month().hour().minute()))
                    .foregroundStyle(.secondary)
            }
            HStack(alignment: .firstTextBaseline) {
                Image(systemName: "person.2")
                Text(activity.people.map(\.nameComponents).formatted(.list(memberStyle: .name(style: .short), type: .and)))
            }
        }
#if os(macOS)
        .padding()
#else
        .padding([.horizontal, .bottom])
#endif
        .frame(maxWidth: .infinity, alignment: alignment)
        .background(activity.tint.opacity(0.1).ignoresSafeArea())
    }

    private var alignment: Alignment {
#if os(macOS)
        .leading
#else
        .center
#endif
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")
}

struct Person {
    var givenName: String
    var familyName: String = ""

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Text formatting: List — [30:03]

```swift
struct ContentView: View {
    var activity: Activity = .sample

    var body: some View {
        Text(activity.people.map(\.nameComponents).formatted(.list(memberStyle: .name(style: .short), type: .and)))
            .scenePadding()
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")
}

struct Person {
    var givenName: String
    var familyName: String = ""

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Text field formatting — [30:43]

```swift
struct ContentView: View {
    @State private var newAttendee = PersonNameComponents()

    var body: some View {
       TextField("New Person", value: $newAttendee,
          format: .name(style: .medium))
    }
}
```

### Text field prompts and labels — [31:09]

```swift
struct ContentView: View {
    @State var activity: Activity = .sample

    var body: some View {
        Form {
            TextField("Name:", text: $activity.name, prompt: Text("New Activity"))
            TextField("Location:", text: $activity.location)
            DatePicker("Date:", selection: $activity.date)
        }
        .frame(minWidth: 250)
        .padding()
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")
}

struct Person {
    var givenName: String
    var familyName: String = ""

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Text field submission — [31:39]

```swift
struct ContentView: View {
    @State private var activity: Activity = .sample
    @State private var newAttendee = PersonNameComponents()

    var body: some View {
        TextField("New Person", value: $newAttendee,
            format: .name(style: .medium)
        )
        .onSubmit {
            activity.append(Person(newAttendee))
            newAttendee = PersonNameComponents()
        }
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Text field submission: submit label — [31:59]

```swift
struct ContentView: View {
    @State private var activity: Activity = .sample
    @State private var newAttendee = PersonNameComponents()

    var body: some View {
        TextField("New Person", value: $newAttendee,
            format: .name(style: .medium)
        )
        .onSubmit {
            activity.append(Person(newAttendee))
            newAttendee = PersonNameComponents()
        }
        .submitLabel(.done)
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Keyboard toolbar — [32:07]

```swift
struct ContentView: View {
    @State private var activity: Activity = .sample
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Name", text: $activity.name, prompt: Text("New Activity"))
            TextField("Location", text: $activity.location)
            DatePicker("Date", selection: $activity.date)
        }
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                Button(action: selectPreviousField) {
                    Label("Previous", systemImage: "chevron.up")
                }
                .disabled(!hasPreviousField)

                Button(action: selectNextField) {
                    Label("Next", systemImage: "chevron.down")
                }
                .disabled(!hasNextField)
            }
        }
    }

    private func selectPreviousField() {
       focusedField = focusedField.map {
          Field(rawValue: $0.rawValue - 1)!
       }
    }

    private var hasPreviousField: Bool {
        if let currentFocusedField = focusedField {
            return currentFocusedField.rawValue > 0
        } else {
            return false
        }
    }

    private func selectNextField() {
       focusedField = focusedField.map {
          Field(rawValue: $0.rawValue + 1)!
       }
    }

    private var hasNextField: Bool {
        if let currentFocusedField = focusedField {
            return currentFocusedField.rawValue < Field.allCases.count
        } else {
            return false
        }
    }
}

private enum Field: Int, Hashable, CaseIterable {
   case name, location, date, addAttendee
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Focus state — [33:05]

```swift
struct ContentView: View {
    @State private var activity: Activity = .sample
    @State private var newAttendee = PersonNameComponents()
    @FocusState private var addAttendeeIsFocused: Bool

    var body: some View {
        VStack {
            Form {
                TextField("Name:", text: $activity.name, prompt: Text("New Activity"))
                TextField("Location:", text: $activity.location)
                DatePicker("Date:", selection: $activity.date)
            }

            TextField("New Person", value: $newAttendee, format: .name(style: .medium))
                .focused($addAttendeeIsFocused)
        }
        .frame(minWidth: 250)
        .scenePadding()
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Focus state: setting focus — [33:16]

```swift
struct ContentView: View {
    @State private var activity: Activity = .sample
    @State private var newAttendee = PersonNameComponents()
    @FocusState private var addAttendeeIsFocused: Bool

    var body: some View {
        VStack {
            Form {
                TextField("Name:", text: $activity.name, prompt: Text("New Activity"))
                TextField("Location:", text: $activity.location)
                DatePicker("Date:", selection: $activity.date)
            }

            VStack(alignment: .leading) {
                TextField("New Person", value: $newAttendee, format: .name(style: .medium))
                    .focused($addAttendeeIsFocused)

                ControlGroup {
                    Button {
                        addAttendeeIsFocused = true
                    } label: {
                       Label("Add Attendee", systemImage: "plus")
                    }
                }
                .fixedSize()
            }
        }
        .frame(minWidth: 250)
        .scenePadding()
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Focus state: Hashable value — [33:30]

```swift
private enum Field: Int, Hashable, CaseIterable {
   case name, location, date, addAttendee
}

struct ContentView: View {
    @State private var activity: Activity = .sample
    @State private var newAttendee = PersonNameComponents()
    @FocusState private var focusedField: Field?

    var body: some View {
        VStack {
            Form {
                TextField("Name:", text: $activity.name, prompt: Text("New Activity"))
                    .focused($focusedField, equals: .name)
                TextField("Location:", text: $activity.location)
                    .focused($focusedField, equals: .location)
                DatePicker("Date:", selection: $activity.date)
                    .focused($focusedField, equals: .date)
            }

            VStack(alignment: .leading) {
                TextField("New Person", value: $newAttendee, format: .name(style: .medium))
                    .focused($focusedField, equals: .addAttendee)

                ControlGroup {
                    Button {
                        focusedField = .addAttendee
                    } label: {
                       Label("Add Attendee", systemImage: "plus")
                    }
                }
                .fixedSize()
            }
        }
        .frame(minWidth: 250)
        .scenePadding()
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Focus state: back/forward controls — [34:03]

```swift
private enum Field: Int, Hashable, CaseIterable {
   case name, location, date, addAttendee
}

struct ContentView: View {
    @State private var activity: Activity = .sample
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Name", text: $activity.name, prompt: Text("New Activity"))
            TextField("Location", text: $activity.location)
            DatePicker("Date", selection: $activity.date)
        }
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                Button(action: selectPreviousField) {
                    Label("Previous", systemImage: "chevron.up")
                }
                .disabled(!canSelectPreviousField)

                Button(action: selectNextField) {
                    Label("Next", systemImage: "chevron.down")
                }
                .disabled(!canSelectNextField)
            }
        }
    }

    private func selectPreviousField() {
       focusedField = focusedField.map {
          Field(rawValue: $0.rawValue - 1)!
       }
    }

    private var canSelectPreviousField: Bool {
        if let currentFocusedField = focusedField {
            return currentFocusedField.rawValue > 0
        } else {
            return false
        }
    }

    private func selectNextField() {
       focusedField = focusedField.map {
          Field(rawValue: $0.rawValue + 1)!
       }
    }

    private var canSelectNextField: Bool {
        if let currentFocusedField = focusedField {
            return currentFocusedField.rawValue < Field.allCases.count
        } else {
            return false
        }
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Focus state: keyboard dismissal — [34:13]

```swift
private enum Field: Int, Hashable, CaseIterable {
   case name, location, date, addAttendee
}

struct ContentView: View {
    @State private var activity: Activity = .sample
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Name", text: $activity.name, prompt: Text("New Activity"))
            TextField("Location", text: $activity.location)
            DatePicker("Date", selection: $activity.date)
        }
    }

    func endEditing() {
        focusedField = nil
    }
}

struct Activity {
    var name: String
    var date: Date
    var location: String
    var people: [Person]
    var info: AttributedString
    var tint: Color = .purple

    static let sample = Activity(name: "What's New in SwiftUI", date: Date(), location: "Apple Park", people: [.init(givenName: "You")], info: "This is some info.")

    mutating func append(_ person: Person) {
        people.append(person)
    }
}

struct Person {
    var givenName: String
    var familyName: String

    init(givenName: String, familyName: String = "") {
        self.givenName = givenName
        self.familyName = familyName
    }

    init(_ nameComponents: PersonNameComponents) {
        givenName = nameComponents.givenName ?? ""
        familyName = nameComponents.familyName ?? ""
    }

    var nameComponents: PersonNameComponents {
        get {
            var components = PersonNameComponents()
            components.givenName = givenName
            if !familyName.isEmpty {
                components.familyName = familyName
            }
            return components
        }
        set {
            givenName = newValue.givenName ?? ""
            familyName = newValue.familyName ?? ""
        }
    }
}
```

### Bordered buttons — [34:55]

```swift
Button("Add") {
   // ... 
}
.buttonStyle(.bordered)
```

### Bordered buttons: view hierarchy — [35:03]

```swift
struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(0..<10) { _ in
                    Button("Add") {
                        //...
                    }
                }
            }
        }
        .buttonStyle(.bordered)
    }
}
```

### Bordered buttons: tinting — [35:09]

```swift
struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(0..<10) { _ in
                    Button("Add") {
                        //...
                    }
                }
            }
        }
        .buttonStyle(.bordered)
        .tint(.green)
    }
}
```

### Control size and prominence — [35:16]

```swift
struct ContentView: View {
    var entry: ButtonEntry = .sample

    var body: some View {
        HStack {
            ForEach(entry.tags) { tag in
                Button(tag.name) {
                    // ...
                }
                .tint(tag.color)
            }
        }
        .buttonStyle(.bordered)
        .controlSize(.small)
        .controlProminence(.increased)
    }
}

struct ButtonEntry {
    struct Tag: Identifiable {
        var name: String
        var color: Color
        var id: String { name }
    }

    var name: String
    var tags: [Tag]

    static let sample = ButtonEntry(name: "Stroopwafel", tags: [Tag(name: "1960s", color: .purple), Tag(name: "bronze", color: .yellow)])
}
```

### Large buttons — [35:34]

```swift
struct ContentView: View {
    var body: some View {
        VStack {
            Button(action: addToJar) {
                Text("Add to Jar").frame(maxWidth: 300)
            }
            .controlProminence(.increased)
            .keyboardShortcut(.defaultAction)

            Button(action: addToWatchlist) {
                Text("Add to Watchlist").frame(maxWidth: 300)
            }
            .tint(.accentColor)
        }
        .buttonStyle(.bordered)
        .controlSize(.large)
    }

    private func addToJar() {}
    private func addToWatchlist() {}
}
```

### Destructive buttons — [37:14]

```swift
struct ContentView: View {
    var entry: ButtonEntry = .sample

    var body: some View {
        ButtonEntryCell(entry)
            .contextMenu {
                Section {
                    Button("Open") {
                        // ...
                    }
                    Button("Delete...", role: .destructive) {
                        // ...
                    }
                }

                Section {
                    Button("Archive") {}

                    Menu("Move to") {
                        ForEach(Jar.allJars) { jar in
                            Button("\(jar.name)") {
                                //addTo(jar)
                            }
                        }
                    }
                }
            }
    }
}

struct ButtonEntryCell: View {
    var entry: ButtonEntry = .sample
    init(_ entry: ButtonEntry) { self.entry = entry }

    var body: some View {
        Text(entry.name)
            .padding()
    }
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }

    static let allJars = [Jar(name: "Secret Stash")]
}

struct ButtonEntry {
    struct Tag: Identifiable {
        var name: String
        var color: Color
        var id: String { name }
    }

    var name: String
    var tags: [Tag]

    static let sample = ButtonEntry(name: "Stroopwafel", tags: [Tag(name: "1960s", color: .purple), Tag(name: "bronze", color: .yellow)])
}
```

### Confirmation dialogs — [37:25]

```swift
struct ContentView: View {
    var entry: ButtonEntry = .sample
    @State private var showConfirmation: Bool = false

    var body: some View {
        ButtonEntryCell(entry)
            .contextMenu {
                Section {
                    Button("Open") {
                        // ...
                    }
                    Button("Delete...", role: .destructive) {
                        showConfirmation = true
                        // ...
                    }
                }

                Section {
                    Button("Archive") {}

                    Menu("Move to") {
                        ForEach(Jar.allJars) { jar in
                            Button("\(jar.name)") {
                                //addTo(jar)
                            }
                        }
                    }
                }
            }
            .confirmationDialog(
                "Are you sure you want to delete \(entry.name)?",
                isPresented: $showConfirmation
            ) {
                Button("Delete", role: .destructive) {
                    // delete the entry
                }
            } message: {
                Text("Deleting \(entry.name) will remove it from all of your jars.")
            }
    }
}

struct ButtonEntryCell: View {
    var entry: ButtonEntry = .sample
    init(_ entry: ButtonEntry) { self.entry = entry }

    var body: some View {
        Text(entry.name)
            .padding()
    }
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }

    static let allJars = [Jar(name: "Secret Stash")]
}

struct ButtonEntry {
    struct Tag: Identifiable {
        var name: String
        var color: Color
        var id: String { name }
    }

    var name: String
    var tags: [Tag]

    static let sample = ButtonEntry(name: "Stroopwafel", tags: [Tag(name: "1960s", color: .purple), Tag(name: "bronze", color: .yellow)])
}
```

### Menu buttons — [37:59]

```swift
struct ContentView: View {
    var buttonEntry: ButtonEntry = .sample
    @StateObject private var jarStore = JarStore()

    var body: some View {
        Menu("Add") {
           ForEach(jarStore.allJars) { jar in
              Button("Add to \(jar.name)") {
                 jarStore.add(buttonEntry, to: jar)
              }
           }
        }
        .menuStyle(BorderedButtonMenuStyle())
        .scenePadding()
    }
}

class JarStore: ObservableObject {
    var allJars: [Jar] = Jar.allJars
    func add(_ entry: ButtonEntry, to jar: Jar) {}
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }
    static let allJars = [Jar(name: "Secret Stash")]
}

struct ButtonEntry {
    var name: String
    static let sample = ButtonEntry(name: "Stroopwafel")
}
```

### Menu buttons: hidden indicator — [38:10]

```swift
struct ContentView: View {
    var buttonEntry: ButtonEntry = .sample
    @StateObject private var jarStore = JarStore()

    var body: some View {
        Menu("Add") {
           ForEach(jarStore.allJars) { jar in
              Button("Add to \(jar.name)") {
                 jarStore.add(buttonEntry, to: jar)
              }
           }
        }
        .menuStyle(BorderedButtonMenuStyle())
        .menuIndicator(.hidden)
        .scenePadding()
    }
}

class JarStore: ObservableObject {
    var allJars: [Jar] = Jar.allJars
    func add(_ entry: ButtonEntry, to jar: Jar) {}
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }
    static let allJars = [Jar(name: "Secret Stash")]
}

struct ButtonEntry {
    var name: String
    static let sample = ButtonEntry(name: "Stroopwafel")
}
```

### Menu buttons: primary action — [38:31]

```swift
struct ContentView: View {
    var buttonEntry: ButtonEntry = .sample
    @StateObject private var jarStore = JarStore()

    var body: some View {
        Menu("Add") {
           ForEach(jarStore.allJars) { jar in
              Button("Add to \(jar.name)") {
                 jarStore.add(buttonEntry, to: jar)
              }
           }
        } primaryAction: {
            jarStore.addToDefaultJar(buttonEntry)
        }
        .menuStyle(BorderedButtonMenuStyle())
        .scenePadding()
    }
}

class JarStore: ObservableObject {
    var allJars: [Jar] = Jar.allJars
    func add(_ entry: ButtonEntry, to jar: Jar) {}
    func addToDefaultJar(_ entry: ButtonEntry) {}
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }
    static let allJars = [Jar(name: "Secret Stash")]
}


struct ButtonEntry {
    var name: String
    static let sample = ButtonEntry(name: "Stroopwafel")
}
```

### Menu buttons: primary action, indicator hidden — [38:42]

```swift
struct ContentView: View {
    var buttonEntry: ButtonEntry = .sample
    @StateObject private var jarStore = JarStore()

    var body: some View {
        Menu("Add") {
           ForEach(jarStore.allJars) { jar in
              Button("Add to \(jar.name)") {
                 jarStore.add(buttonEntry, to: jar)
              }
           }
        } primaryAction: {
            jarStore.addToDefaultJar(buttonEntry)
        }
        .menuStyle(BorderedButtonMenuStyle())
        .menuIndicator(.hidden)
        .scenePadding()
    }
}

class JarStore: ObservableObject {
    var allJars: [Jar] = Jar.allJars
    func add(_ entry: ButtonEntry, to jar: Jar) {}
    func addToDefaultJar(_ entry: ButtonEntry) {}
}

struct Jar: Identifiable {
    var name: String
    var id: String { name }
    static let allJars = [Jar(name: "Secret Stash")]
}


struct ButtonEntry {
    var name: String
    static let sample = ButtonEntry(name: "Stroopwafel")
}
```

### Toggle buttons — [39:01]

```swift
Toggle(isOn: $showOnlyNew) {
    Label("Show New Buttons", systemImage: "sparkles")
}
.toggleStyle(.button)
```

### Control group — [39:13]

```swift
ControlGroup {
    Button(action: archive) {
        Label("Archive", systemImage: "archiveBox")
    }
    Button(action: delete) {
        Label("Delete", systemName: "trash")
    }
}
```

### Control group: back/forward control — [39:26]

```swift
struct ContentView: View {
    @State var current: String = "More buttons"
    @State var history: [String] = ["Text and keyboard", "Advanced graphics", "Beyond lists", "Better lists"]
    @State var forwardHistory: [String] = []

    var body: some View {
        Color.clear
            .toolbar{
                ToolbarItem(placement: .navigation) {
                    ControlGroup {
                        Menu {
                            ForEach(history, id: \.self) { previousSection in
                                Button(previousSection) {
                                    goBack(to: previousSection)
                                }
                            }
                        } label: {
                            Label("Back", systemImage: "chevron.backward")
                        } primaryAction: {
                            goBack(to: history[0])
                        }
                        .disabled(history.isEmpty)

                        Menu {
                            ForEach(forwardHistory, id: \.self) { nextSection in
                                Button(nextSection) {
                                    goForward(to: nextSection)
                                }
                            }
                        } label: {
                            Label("Forward", systemImage: "chevron.forward")
                        } primaryAction: {
                            goForward(to: forwardHistory[0])
                        }
                        .disabled(forwardHistory.isEmpty)
                    }
                    .controlGroupStyle(.navigation)
                }
            }
            .navigationTitle(current)
    }

    private func goBack(to section: String) {
        guard let index = history.firstIndex(of: section) else { return }
        forwardHistory.insert(current, at: 0)
        forwardHistory.insert(contentsOf: history[...history.index(before: index)].reversed(), at: 0)
        history.removeSubrange(...index)
        current = section
    }

    private func goForward(to section: String) {
        guard let index = forwardHistory.firstIndex(of: section) else { return }
        history.insert(current, at: 0)
        history.insert(contentsOf: forwardHistory[...forwardHistory.index(before: index)].reversed(), at: 0)
        forwardHistory.removeSubrange(...index)
        current = section
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10018/4/C1412BB4-40EE-418F-BCFD-09796128093C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10018/4/C1412BB4-40EE-418F-BCFD-09796128093C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10018) — developer.apple.com. Indexed for agent consumption._