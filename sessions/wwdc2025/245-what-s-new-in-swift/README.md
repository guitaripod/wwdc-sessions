---
id: "wwdc2025-245"
event: "wwdc2025"
year: 2025
title: "What’s new in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/245"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Swift

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-245](https://developer.apple.com/videos/play/wwdc2025/245)

Join us for an update on Swift. We’ll talk about workflow improvements that make you more productive, and new and modernized library APIs for fundamental programming tasks. We’ll show examples of Swift adoption throughout more layers of the software stack. Finally, we’ll explore new language features for both improving approachability of concurrency, and achieving peak performance when you need it.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,536 words)

## Documentation & Resources

- [The Swift website](https://www.swift.org) _documentation_
- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Subprocess: Call `run` with string — [9:44]

```swift
import Subprocess

let result = try await run(
  .name("pwd")
)
```

### Subprocess: Call `run` with file path — [10:04]

```swift
import Subprocess

let swiftPath = FilePath("/usr/bin/swift")
let result = try await run(
  .path(swiftPath),
  arguments: ["--version"]
)
```

### Subprocess: Accessing standard output — [10:05]

```swift
import Subprocess

let swiftPath = FilePath("/usr/bin/swift")
let result = try await run(
  .path(swiftPath),
  arguments: ["--version"]
)

let swiftVersion = result.standardOutput
```

### NotificationCenter: Dynamic types — [10:51]

```swift
import UIKit

@MainActor 
class KeyboardObserver {
 func registerObserver(screen: UIScreen) {
    let center = NotificationCenter.default
    let token = center.addObserver(
      forName: UIResponder.keyboardWillShowNotification,
      object: screen,
      queue: .main
    ) { notification in
      guard let userInfo = notification.userInfo else { return }
      let startFrame = userInfo[UIResponder.keyboardFrameBeginUserInfoKey] as? CGRect
      let endFrame = userInfo[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect

      guard let startFrame, let endFrame else { return }

      self.keyboardWillShow(startFrame: startFrame, endFrame: endFrame)
    }
  }

  func keyboardWillShow(startFrame: CGRect, endFrame: CGRect) {}
}
```

### NotificationCenter: Concrete types — [11:34]

```swift
import UIKit

@MainActor
class KeyboardObserver {
  func registerObserver(screen: UIScreen) {
    let center = NotificationCenter.default
    let token = center.addObserver(
      of: screen,
      for: .keyboardWillShow
    ) { keyboardState in
      let startFrame = keyboardState.startFrame
      let endFrame = keyboardState.endFrame

      self.keyboardWillShow(startFrame: startFrame, endFrame: endFrame) 
    }
  }

  func keyboardWillShow(startFrame: CGRect, endFrame: CGRect) {}
}
```

### NotificationCenter: Conformances — [12:01]

```swift
extension UIResponder { 
  public struct KeyboardWillShowMessage: NotificationCenter.MainActorMessage
}

extension HTTPCookieStorage {
  public struct CookiesChangedMessage: NotificationCenter.AsyncMessage
}
```

### Observation: The @Observable macro — [12:48]

```swift
import Observation

enum Item {
  case none
  case banana
  case star
}

@Observable
class Player {
  let name: String
  var score: Int = 0
  var item: Item = .none

  init(name: String) {
    self.name = name
  }
}
```

### Observation: The Observations type — [12:58]

```swift
import Observation

enum Item {
  case none
  case banana
  case star
}

@Observable
class Player {
  let name: String
  var score: Int = 0
  var item: Item = .none

  init(name: String) {
    self.name = name
  }
}

let player = Player(name: "Holly")
let values = Observations {
  let score = "\(player.score) points"
  let item =
    switch player.item {
    case .none: "no item"
    case .banana: "a banana"
    case .star: "a star"
    }
  return "\(score) and \(item)"
}
```

### Observation: Transactional updates — [13:56]

```swift
import Observation

enum Item {
  case none
  case banana
  case star
}

@Observable
class Player {
  let name: String
  var score: Int = 0
  var item: Item = .none

  init(name: String) {
    self.name = name
  }
}

let player = Player(name: "Holly")
let values = Observations {
  let score = "\(player.score) points"
  let item =
    switch player.item {
    case .none: "no item"
    case .banana: "a banana"
    case .star: "a star"
    }
  return "\(score) and \(item)"
}

player.score += 2
player.item = .banana
```

### Observation: AsyncSequence — [14:05]

```swift
import Observation

enum Item {
  case none
  case banana
  case star
}

@Observable
class Player {
  let name: String
  var score: Int = 0
  var item: Item = .none

  init(name: String) {
    self.name = name
  }
}

let player = Player(name: "Holly")
let values = Observations {
  let score = "\(player.score) points"
  let item =
    switch player.item {
    case .none: "no item"
    case .banana: "a banana"
    case .star: "a star"
    }
  return "\(score) and \(item)"
}

player.score += 2
player.item = .banana

for await value in values { print(value) }
```

### Swift Testing — [14:17]

```swift
import Testing
import Foundation
import EvolutionMetadataModel

@Test
func validateProposalID() async throws {
  let (data, _) = try await URLSession.shared.data(from: evolutionJSONMetadataURL)

  let jsonDecoder = JSONDecoder()
  let metadata = try jsonDecoder.decode(EvolutionMetadata.self, from: data)
  for proposal in metadata.proposals {
    #expect(proposal.id.starts(with: "SE"))
  }
}
```

### Swift Testing: Attachments — [14:54]

```swift
import Testing
import Foundation
import EvolutionMetadataModel

@Test
func validateProposalID() async throws {
  let (data, _) = try await URLSession.shared.data(from: evolutionJSONMetadataURL) 
  Attachment.record(data, named: "evolution-metadata.json")

  let jsonDecoder = JSONDecoder()
  let metadata = try jsonDecoder.decode(EvolutionMetadata.self, from: data)
  for proposal in metadata.proposals {
    #expect(proposal.id.starts(with: "SE"))
  }
}
```

### Exit Tests: Preconditions — [15:23]

```swift
extension Proposal {
  public var number: Int {
    let components = id.split(separator: "-")
    precondition(
      components.count == 2 && components[1].allSatisfy(\.isNumber),
      "Invalid proposal ID format \(id); expected SE-<Number>"
    )

    return Int(components[1])!
  }
}
```

### Exit Tests: processExitsWith argument — [15:34]

```swift
import Testing
import EvolutionMetadataModel

@Test
func invalidProposalPrefix() async throws {
  await #expect(processExitsWith: .failure) {
    let proposal = Proposal(id: "SE-NNNN")
    _ = proposal.number 
  }
}
```

### Concurrency: Async function error message — [31:06]

```swift
class PhotoProcessor {
  func extractSticker(data: Data, with id: String?) async -> Sticker? {     }
}

@MainActor
final class StickerModel {
  let photoProcessor = PhotoProcessor()

  func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
    guard let data = try await item.loadTransferable(type: Data.self) else {
      return nil
    }

    return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
  }
}
```

### Concurrency: Run async functions on the caller's actor — [32:06]

```swift
// Run async functions on the caller's actor

class PhotoProcessor {
  func extractSticker(data: Data, with id: String?) async -> Sticker? {}
}

@MainActor
final class StickerModel {
  let photoProcessor = PhotoProcessor()

  func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
    guard let data = try await item.loadTransferable(type: Data.self) else {
      return nil
    }

    return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
  }
}
```

### Concurrency: Conformance error — [32:36]

```swift
protocol Exportable {
  func export()
}


extension StickerModel: Exportable { // error: Conformance of 'StickerModel' to protocol 'Exportable' crosses into main actor-isolated code and can cause data races
  func export() {
    photoProcessor.exportAsPNG()
  }
}
```

### Concurrency: Isolated conformances — [33:04]

```swift
// Isolated conformances

protocol Exportable {
  func export()
}


extension StickerModel: @MainActor Exportable {
  func export() {
    photoProcessor.exportAsPNG()
  }
}
```

### Concurrency: Isolated conformance use — [33:20]

```swift
// Isolated conformances

@MainActor
struct ImageExporter {
  var items: [any Exportable]

  mutating func add(_ item: StickerModel) {
    items.append(item)
  }

  func exportAll() {
    for item in items {
      item.export()
    }
  }
}
```

### Concurrency: Isolated conformance error — [33:31]

```swift
// Isolated conformances

nonisolated
struct ImageExporter {
  var items: [any Exportable]

  mutating func add(_ item: StickerModel) {
    items.append(item) // error: Main actor-isolated conformance of 'StickerModel' to 'Exportable' cannot be used in nonisolated context
  }

  func exportAll() {
    for item in items {
      item.export()
    }
  }
}
```

### Concurrency: Unsafe static variable — [33:51]

```swift
final class StickerLibrary {
  static let shared: StickerLibrary = .init() // error: Static property 'shared' is not concurrency-safe because non-'Sendable' type 'StickerLibrary' may have shared mutable state
}
```

### Concurrency: Protecting static variables — [34:01]

```swift
final class StickerLibrary {
  @MainActor
  static let shared: StickerLibrary = .init()
}
```

### Concurrency: Protecting classes — [34:05]

```swift
@MainActor
final class StickerLibrary {
  static let shared: StickerLibrary = .init()
}
```

### Concurrency: A single-threaded program — [34:15]

```swift
@MainActor
final class StickerLibrary {
  static let shared: StickerLibrary = .init()
}

@MainActor
final class StickerModel {
  let photoProcessor: PhotoProcessor

  var selection: [PhotosPickerItem]
}

extension StickerModel: @MainActor Exportable {
  func export() {
    photoProcessor.exportAsPNG()
  }
}
```

### Concurrency: Mode to infer main actor by default — [34:22]

```swift
// Mode to infer main actor by default

final class StickerLibrary {
  static let shared: StickerLibrary = .init()
}

final class StickerModel {
  let photoProcessor: PhotoProcessor

  var selection: [PhotosPickerItem]
}

extension StickerModel: Exportable {
  func export() {
    photoProcessor.exportAsPNG()
  }
}
```

### Concurrency: Explicitly offloading async work — [35:06]

```swift
// Explicitly offloading async work

class PhotoProcessor {
  var cachedStickers: [String: Sticker]

  func extractSticker(data: Data, with id: String) async -> Sticker {
      if let sticker = cachedStickers[id] {
        return sticker
      }

      let sticker = await Self.extractSubject(from: data)
      cachedStickers[id] = sticker
      return sticker
  }

  @concurrent
  static func extractSubject(from data: Data) async -> Sticker {}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/245/5/ffab291a-af6f-4f45-9ee5-d504cabc053c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/245/5/ffab291a-af6f-4f45-9ee5-d504cabc053c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/245) — developer.apple.com. Indexed for agent consumption._
