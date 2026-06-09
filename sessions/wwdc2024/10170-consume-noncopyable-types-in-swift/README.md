---
id: "wwdc2024-10170"
event: "wwdc2024"
year: 2024
title: "Consume noncopyable types in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10170"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Consume noncopyable types in Swift

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10170](https://developer.apple.com/videos/play/wwdc2024/10170)

Get started with noncopyable types in Swift. Discover what copying means in Swift, when you might want to use a noncopyable type, and how value ownership lets you state your intentions clearly.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,081 words)

## Documentation & Resources

- [Copyable](https://developer.apple.com/documentation/Swift/Copyable) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/Copyable
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/Copyable.json
- [Swift Evolution: Noncopyable Standard Library Primitives](https://github.com/apple/swift-evolution/blob/main/proposals/0437-noncopyable-stdlib-primitives.md) _documentation_
- [Swift Evolution: Borrowing and consuming pattern matching for noncopyable types](https://github.com/apple/swift-evolution/blob/main/proposals/0432-noncopyable-switch.md) _documentation_
- [Swift Evolution: Noncopyable Generics](https://github.com/apple/swift-evolution/blob/main/proposals/0427-noncopyable-generics.md) _documentation_
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010

## Code Snippets

### Player as a struct — [0:52]

```swift
struct Player {
  var icon: String
}

func test() {
  let player1 = Player(icon: "🐸")
  var player2 = player1
  player2.icon = "🚚"
  assert(player1.icon == "🐸")
}
```

### Player as a class — [1:55]

```swift
class PlayerClass {
  var icon: String
  init(_ icon: String) { self.icon = icon }
}

func test() {
  let player1 = PlayerClass("🐸")
  let player2 = player1
  player2.icon = "🚚"
  assert(player1.icon == "🐸")
}
```

### Deeply copying a PlayerClass — [3:00]

```swift
class PlayerClass {
  var data: Icon
  init(_ icon: String) { self.data = Icon(icon) }

  init(from other: PlayerClass) {
    self.data = Icon(from: other.data)
  } 
}

func test() {
  let player1 = PlayerClass("🐸")
  var player2 = player1
  player2 = PlayerClass(from: player2)
  player2.data.icon = "🚚"
  assert(player1.data.icon == "🐸")
}

struct Icon {
  var icon: String
  init(_ icon: String) { self.icon = icon }
  init(from other: Icon) { self.icon = other.icon }
}
```

### Copyable BankTransfer — [5:10]

```swift
class BankTransfer {
  var complete = false

  func run() {
    assert(!complete)
    // .. do it ..
    complete = true
  }

  deinit {
    if !complete { cancel() }
  }

  func cancel() { /* ... */ }
}

func schedule(_ transfer: BankTransfer,
              _ delay: Duration) async throws {

  if delay < .seconds(1) {
    transfer.run()
  }

  try await Task.sleep(for: delay)
  transfer.run()
}

func startPayment() async {
  let payment = BankTransfer()
  log.append(payment)
  try? await schedule(payment, .seconds(3))
}

let log = Log()

final class Log: Sendable {
  func append(_ transfer: BankTransfer) { /* ... */ }
}
```

### Copying FloppyDisk — [7:46]

```swift
struct FloppyDisk: ~Copyable {}

func copyFloppy() {
  let system = FloppyDisk()
  let backup = consume system
  load(system)
  // ...
}

func load(_ disk: borrowing FloppyDisk) {}
```

### Missing ownership for FloppyDisk — [8:18]

```swift
struct FloppyDisk: ~Copyable { }

func newDisk() -> FloppyDisk {
  let result = FloppyDisk()
  format(result)
  return result
}

func format(_ disk: FloppyDisk) {
  // ...
}
```

### Consuming ownership — [9:00]

```swift
struct FloppyDisk: ~Copyable { }

func newDisk() -> FloppyDisk {
  let result = FloppyDisk()
  format(result)
  return result
}

func format(_ disk: consuming FloppyDisk) {
  // ...
}
```

### Borrowing ownership — [9:26]

```swift
struct FloppyDisk: ~Copyable { }

func newDisk() -> FloppyDisk {
  let result = FloppyDisk()
  format(result)
  return result
}

func format(_ disk: borrowing FloppyDisk) {
  var tempDisk = disk
  // ...
}
```

### Inout ownership — [9:55]

```swift
struct FloppyDisk: ~Copyable { }

func newDisk() -> FloppyDisk {
  var result = FloppyDisk()
  format(&result)
  return result
}

func format(_ disk: inout FloppyDisk) {
  var tempDisk = disk
  // ...
  disk = tempDisk
}
```

### Noncopyable BankTransfer — [10:28]

```swift
struct BankTransfer: ~Copyable {
  consuming func run() {
    // .. do it ..
    discard self
  }

  deinit {
    cancel()
  }

  consuming func cancel() {
    // .. do the cancellation ..
    discard self
  }
}
```

### Schedule function for noncopyable BankTransfer — [11:10]

```swift
func schedule(_ transfer: consuming BankTransfer,
              _ delay: Duration) async throws {

  if delay < .seconds(1) {
    transfer.run()
    return
  }

  try await Task.sleep(for: delay)
  transfer.run()
}
```

### Overview of conformance constraints — [12:12]

```swift
struct Command { }

protocol Runnable {
  consuming func run()
}

extension Command: Runnable {
  func run() { /* ... */ }
}

func execute1<T>(_ t: T) {}

func execute2<T>(_ t: T) 
  where T: Runnable {
  t.run()
}

func test(_ cmd: Command, _ str: String) {
  execute1(cmd)
  execute1(str)

  execute2(cmd)
  execute2(str) // expected error: 'execute2' requires that 'String' conform to 'Runnable'
}
```

### Noncopyable generics: 'execute' function — [15:50]

```swift
protocol Runnable: ~Copyable {
  consuming func run()
}

struct Command: Runnable {
  func run() { /* ... */ }
}

struct BankTransfer: ~Copyable, Runnable {
  consuming func run() { /* ... */ }
}

func execute2<T>(_ t: T)
  where T: Runnable {
  t.run()
}

func execute3<T>(_ t: consuming T)
  where T: Runnable,
        T: ~Copyable {
  t.run()
}

func test() {
  execute2(Command())
  execute2(BankTransfer()) // expected error: 'execute2' requires that 'BankTransfer' conform to 'Copyable'

  execute3(Command())
  execute3(BankTransfer())
}
```

### Conditionally Copyable — [18:05]

```swift
struct Job<Action: Runnable & ~Copyable>: ~Copyable {
  var action: Action?
}

func runEndlessly(_ job: consuming Job<Command>) {
  while true {
    let current = copy job
    current.action?.run()
  }
}

extension Job: Copyable where Action: Copyable {}

protocol Runnable: ~Copyable {
  consuming func run()
}

struct Command: Runnable {
  func run() { /* ... */ }
}
```

### Extensions of types with noncopyable generic parameters — [19:27]

```swift
extension Job {
  func getAction() -> Action? {
    return action
  }
}

func inspectCmd(_ cmdJob: Job<Command>) {
  let _ = cmdJob.getAction()
  let _ = cmdJob.getAction()
}

func inspectXfer(_ transferJob: borrowing Job<BankTransfer>) {
  let _ = transferJob.getAction() // expected error: method 'getAction' requires that 'BankTransfer' conform to 'Copyable'
}


struct Job<Action: Runnable & ~Copyable>: ~Copyable {
  var action: Action?
}

extension Job: Copyable where Action: Copyable {}

protocol Runnable: ~Copyable {
  consuming func run()
}

struct Command: Runnable {
  func run() { /* ... */ }
}

struct BankTransfer: ~Copyable, Runnable {
  consuming func run() { /* ... */ }
}
```

### Cancellable for Jobs with Copyable actions — [20:14]

```swift
protocol Cancellable {
  mutating func cancel()
}

extension Job: Cancellable {
  mutating func cancel() {
    action = nil
  }
}
```

### Cancellable for all Jobs — [21:00]

```swift
protocol Cancellable: ~Copyable {
  mutating func cancel()
}

extension Job: Cancellable where Action: ~Copyable {
  mutating func cancel() {
    action = nil
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10170/4/993789F1-AF44-4E20-8C66-BF59DAC6C1F6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10170/4/993789F1-AF44-4E20-8C66-BF59DAC6C1F6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10170) — developer.apple.com. Indexed for agent consumption._
