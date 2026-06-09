# What’s new in Swift

**Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-262](https://developer.apple.com/videos/play/wwdc2026/262)

Join us for an update on Swift. Discover the latest language advancements, including updates for everyday ergonomics, improved concurrency, and safer high-performance code. Explore workflow and language interoperability improvements and updates in embedded Swift.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Swift Blog](https://www.swift.org/blog/) _documentation_
- [Explore documentation on swift.org](https://www.swift.org/documentation/) _documentation_
- [Swift Forums](https://forums.swift.org) _developerForum_

## Code Snippets

### Better Swift Concurrency diagnostics (catching in the task) — [1:12]

```swift
Task {
    do {
        try lander.fly(to: moon)
    }
    catch {
        lander.abort()
    }
}
```

### Better Swift Concurrency diagnostics (saving the task for later) — [1:21]

```swift
let landingTask = Task {
    try lander.fly(to: moon)
}

defer {
    await orbiter.rendezvous(with: lander)
}

try await orbiter.justHangOut(waitingFor: landingTask)
```

### Better 'Sendable' conformances — [1:27]

```swift
final class Spacecraft: Sendable {
    ...
    weak let dockedAt: SpaceStation?
    ...
}

class Mission: ~Sendable { ... }

class CrewedMission: Mission, @unchecked Sendable { ... }
```

### More accessible memberwise initializers — [1:48]

```swift
struct Briefing {
    internal var topic: String
    internal var scheduledAt: Date
    private  var attendees: [Person] = []
}

// Generated memberwise initializers:
// extension Briefing {
//     private init(topic: String, scheduledAt: Date, attendees: [Person] = []) { 
//          self.topic = topic
//          self.scheduledAt = scheduledAt
//          self.attendees = attendees
//     }
// 
//     internal init(topic: String, scheduledAt: Date) {
//          self.topic = topic
//          self.scheduledAt = scheduledAt
//          self.attendees = []
//     }
// }
```

### 'anyAppleOS' availability (before) — [2:03]

```swift
extension Mission {
    @available(macOS 27, iOS 27, watchOS 27, tvOS 27, visionOS 27, *)
    func showStatus() { ... }

    @available(macOS 27, iOS 27, watchOS 27, visionOS 27, *)
    @available(tvOS, unavailable)
    func launch() { ... }

    #if os(macOS) || os(iOS) || os(watchOS) || os(tvOS) || os(visionOS)
    func makeLiveActivityWidget() -> some Widget { ... }
    #endif
}
```

### 'anyAppleOS' availability (after) — [2:17]

```swift
extension Mission {
    @available(anyAppleOS 27, *)
    func showStatus() { ... }

    @available(anyAppleOS 27, *)
    @available(tvOS, unavailable)
    func launch() { ... }

    #if os(anyAppleOS)
    func makeLiveActivityWidget() -> some Widget { ... }
    #endif
}
```

### Controlling warnings with '@diagnose' — [2:40]

```swift
@diagnose(DeprecatedDeclaration, as: ignored, reason: "Flying with surplus hardware")
func makeApolloSoyuzMission() -> Mission {
    CrewedMission(
        rocket: makeSaturnIRocket(),
        payload: makeApolloCSM(),
        crew: [.daniellePoole, .nathanMorrison]
    )
}

@diagnose(StrictMemorySafety, as: warning)
func uplinkCommand(from receiver: inout Receiver, to computer: inout Computer) {
    let commandSize = receiver.receiveInt()
    receiver.withReceivedData(byteCount: commandSize) {
        computer.receiveUplinkedCommand($0)
    }
}

@diagnose(ErrorInFutureSwiftVersion, as: error)
func fetchPosition() -> (x: Double, y: Double, z: Double) {
    return self.rotation
}
```

### Clarifying code with module selectors — [3:47]

```swift
import Rocket
import GiftShopToys

let rocket1 = SaturnV()            // could mean `Rocket::SaturnV` or `GiftShopToys::SaturnV`
let rocket2 = Rocket.SaturnV()     // prefers `Rocket::Rocket.SaturnV`
let rocket3 = Rocket::SaturnV()    // correctly finds `Rocket::SaturnV`
```

### Clarifying code with module selectors (module selectors work on members, too) — [5:00]

```swift
//
// Module Chemistry
//

public protocol Flammable { ... }

extension Flammable {
    /// Set `self` on fire.
    public func fire() { ... }
}

//
// Module HumanResources
//

import Chemistry

public protocol Employee { ... }

extension Employee {
    /// Remove `self` from job.
    public func fire() { ... }
}

public class LaunchPadTechnician: Employee, Flammable { ... }

//
// Module main
//

import HumanResources
import Chemistry

let launchPadTechnician = LaunchPadTechnician(...)

launchPadTechnician.HumanResources::fire()
```

### Task cancellation — [6:26]

```swift
// Radio for help

extension Radio {
  func send(_ data: [UInt8] {
    if Task.isCancelled { return }
    // ...
  }
}

extension EmergencyTransponder {
  func sendSOS() {
    radio.send(makeSOSPacket())
  }
}
```

### Task cancellation shield — [6:40]

```swift
// Radio for help

extension Radio {
  func send(_ data: [UInt8] {
    if Task.isCancelled { return }
    // ...
  }
}

extension EmergencyTransponder {
  func sendSOS() {
    withTaskCancellationShield {
    	radio.send(makeSOSPacket())
    }
  }
}
```

### Constructing a new dictionary — [6:53]

```swift
// Map values with keys

func makeCalendarDisplayNames(for missions: [Mission: LaunchWindow]) -> [Mission: String] {
    let new: [Mission: String] = .init(
        uniqueKeysWithValues: missions.lazy.map { mission, launchWindow in
            (mission, makeDisplayName(for: mission, in: launchWindow))
        }
    )
    return new
}
```

### Dictionary.mapKeyedValues — [7:06]

```swift
// Map values with keys

func makeCalendarDisplayNames(for missions: [Mission: LaunchWindow]) -> [Mission: String] {
    missions.mapKeyedValues { mission, launchWindow in
        makeDisplayName(for: mission, in: launchWindow)
    }
}
```

### The new FilePath type — [7:14]

```swift
// FilePath handling macOS-named resources

var path: FilePath = "/var/www/static"
path.components.append("WWDC")
print(path.components)
// [ "var", "www", "static", "WWDC" ]

var path: FilePath = "/var/www/static/..namedresource/rsrc"
print(path.components)
// [ "var", "www", "static" ]
```

### Issue Severity — [7:41]

```swift
// Issue severity

@Test(arguments: allRockets)
func testBurn(rocket: Rocket) throws {
    rocket.burn(for: .seconds(150))
    let remaining = rocket.propellantKg / rocket.totalPropellantKg

    if remaining < 0.10 {
        Issue.record(
            "\(rocket.name) remaining fuel is below 10% reserve target",
            severity: .warning
        )
    }

    #expect(remaining > 0.02, "\(rocket.name) propellant critically low - abort")
}
```

### Test Cancellation — [7:52]

```swift
// Test Cancellation

@Test(arguments: allRockets)
func testBurn(rocket: Rocket) throws {
    // solid-fuel rocket engines can't be stopped
    if rocket.engineType == .solid {
        try Test.cancel("\(rocket.name) has solid fuel")
    }

    rocket.burn(for: .seconds(150))
    let remaining = rocket.propellantKg / rocket.totalPropellantKg

    if remaining < 0.10 {
        Issue.record(
            "\(rocket.name) remaining fuel is below 10% reserve target",
            severity: .warning
        )
    }

    #expect(remaining > 0.02, "\(rocket.name) propellant critically low - abort")
}
```

### XCTest interoperability: Using XCTest from Swift Testing — [8:34]

```swift
// XCTest interoperability: Using XCTest from Swift Testing

func checkedTransmitAndReceive(on radio: Radio,
                               packet: Packet,
                               expectedByteCount: Int) throws -> [UInt8] {
    try radio.transmit(bytes: packet.data)
    let bytes = try radio.receive()
    XCTAssertEqual(bytes.count, expectedByteCount)
    return bytes
}

@Test
func pingTest() throws {
    let radio = Radio()
    let bytes = try checkedTransmitAndReceive(on: radio, packet: .ping, expectedByteCount: 8)
    #expect(bytes == [0x00, 0x00, 0xf0, 0x37, 0x0f, 0xc7, 0x00, 0x01])
}
```

### XCTest interoperability: Using Swift Testing from XCTest — [8:48]

```swift
// XCTest interoperability: Using Swift Testing from XCTest

class RadioTests: XCTestCase {
    func testPingPacketTransmission() {
        let radio = Radio()
        let bytes = try checkedTransmitAndReceive(on: radio,
                                                  packet: .ping,
                                                  expectedByteCount: 8)

        #expect(bytes == [0x00, 0x00, 0xf0, 0x36, 0x0f, 0xc7, 0x00, 0x02])
    }
}
```

### Subprocess Output Stream — [10:01]

```swift
// Subprocess output streaming

let result = try await Subprocess.run(.name("ls"),
                                      input: .none,
                                      output: .sequence,
                                      error: .string(limit:4096)) { execution in
		execution.standardOtput.strings().filter { $0.hasSuffix(".obj") }
}

for try await objectFiles in result.closureOutput {
  	print("Object file: \(objectFile)")
}
```

### Progress Manager - Concurrency — [10:37]

```swift
// Progress reporting - Concurrency

let manager = ProgressManager(totalCount: 100)
try await rocket.launch(mission.subprogress(assigningCount: 100))

extension Rocket {
    func launch(_ progress: consuming Subprogress? = nil) async throws {
        let stage = progress?.start(totalCount: 3)
        try await ignite(); stage?.complete(count: 1)
        try await liftoff(); stage?.complete(count: 1)
        try await stageSeparation(); stage?.complete(count: 1)
    }
}
```

### Progress Manager - progress reporting — [10:37]

```swift
// Progress reporting - progress reporting

let manager = ProgressManager(totalCount: 100)
try await rocket.launch(mission.subprogress(assigningCount: 100))

Task {
    for await update in Observations({ mission.fractionCompleted }) {
        print("🚀 Mission \(Int(update * 100))%")
    }
}
```

### Progress reporting - metadata — [10:37]

```swift
// Progress reporting - metadata

extension Rocket {
    func ascend(_ progress: consuming Subprogress) async throws {
        let stage = progress.start(totalCount: 3)
        stage.detlaV = 3_400; try await burn(); stage.complete(count: 1)
        stage.detlaV = 2_100; try await stageSeparation(); stage.complete(count: 1)
        stage.detlaV = 1_800; try await coast(); stage.complete(count: 1)
    }
}

print("Δv to orbit: \(mission.summary(of: \.deltaV)) m/s")
```

### Directly control inlining (source code) — [20:56]

```swift
func histogram<Values>(of values: Values) -> [256 of Int] where Values: Sequence<UInt8> {
    var result = makeInts(randomized: false)

    for value in values {
        result[Int(value)] += 1
    }

    return result
}

func makeInts(randomized: Bool) -> [256 of Int] {
    if randomized {
        InlineArray { _ in Int.random(in: (.min)...(.max)) }
    } else {
        InlineArray(repeating: 0)
    }
}
```

### Directly control inlining (inlined, but not optimized) — [21:01]

```swift
func histogram<Values>(of values: Values) -> [256 of Int] where Values: Sequence<UInt8> {
    var result = if false {                                                  //
                     InlineArray { _ in Int.random(in: (.min)...(.max)) }    //
                 } else {                                                    // Inlined code
                     InlineArray(repeating: 0)                               //
                 }                                                           //

   for value in values {
        result[Int(value)] += 1
    }
    return result
}

func makeInts(randomized: Bool) -> [256 of Int] {
    if randomized {
        InlineArray { _ in Int.random(in: (.min)...(.max)) }
    } else {
        InlineArray(repeating: 0)
    }
}
```

### Directly control inlining (inlined and optimized) — [21:07]

```swift
func histogram<Values>(of values: Values) -> [256 of Int] where Values: Sequence<UInt8> {
    var result = InlineArray(repeating: 0)    // Inlined and optimized code

   for value in values {
        result[Int(value)] += 1
    }
    return result
}

func makeInts(randomized: Bool) -> [256 of Int] {
    if randomized {
        InlineArray { _ in Int.random(in: (.min)...(.max)) }
    } else {
        InlineArray(repeating: 0)
    }
}
```

### Directly control inlining (preventing inlining) — [21:30]

```swift
@inline(never)
func makeInts(randomized: Bool) -> [256 of Int] {
    if randomized {
        InlineArray { _ in Int.random(in: (.min)...(.max)) }
    } else {
        InlineArray(repeating: 0)
    }
}
```

### Directly control inlining (forcing inlining) — [21:39]

```swift
@inline(always)
func makeInts(randomized: Bool) -> [256 of Int] {
    if randomized {
        InlineArray { _ in Int.random(in: (.min)...(.max)) }
    } else {
        InlineArray(repeating: 0)
    }
}
```

### Making generic functions faster with '@specialized'​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [21:55]

```swift
func histogram<Values>(of values: Values) -> [256 of Int] where Values: Sequence<UInt8> {
    var result = makeInts(randomized: false)

    for value in values {
        result[Int(value)] += 1
    }

    return result
}

// Note: Specialized function doesn't actually have a directly callable name.
func `histogram of [UInt8]`(of values: [UInt8]) -> [256 of Int] {    //
    var result = makeInts(randomized: false)                         //
                                                                     //
    for value in values {                                            //
        result[Int(value)] += 1                                      // Specialized code
    }                                                                //
                                                                     //
    return result                                                    //
}                                                                    //
```

### Making generic functions faster with '@specialized'​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ (explicitly requesting specialization) — [22:17]

```swift
@specialized(where Values == [UInt8])
func histogram<Values>(of values: Values) -> [256 of Int] where Values: Sequence<UInt8> {
    var result = makeInts(randomized: false)

    for value in values {
        result[Int(value)] += 1
    }

    return result
}

// Note: Specialized function doesn't actually have a directly callable name.
func `histogram of [UInt8]`(of values: [UInt8]) -> [256 of Int] {    //
    var result = makeInts(randomized: false)                         //
                                                                     //
    for value in values {                                            //
        result[Int(value)] += 1                                      // Specialized code
    }                                                                //
                                                                     //
    return result                                                    //
}                                                                    //
```

### Associated types can be '~Copyable' and '~Escapable' — [25:46]

```swift
protocol Iterable<Element, Failure>: ~Copyable, ~Escapable {
    associatedtype Element: ~Copyable
    associatedtype IterableIterator: IterableIteratorProtocol<Element, Failure>, ~Copyable, ~Escapable
    associatedtype Failure: Error = Never

    func makeIterableIterator() -> IterableIterator

    var underestimatedCount: Int { get }
}

protocol IterableIteratorProtocol<Element, Failure>: ~Copyable, ~Escapable {
    associatedtype Element: ~Copyable
    associatedtype Failure: Error = Never

    mutating func nextSpan(maximumCount: Int) throws(Failure) -> Span<Element>

    mutating func skip(by maximumOffset: Int) throws(Failure) -> Int
}
```

### The problem with existing accessors — [27:28]

```swift
@safe public struct UniqueBox<Value>: ~Copyable {
    private let valuePointer: UnsafeMutablePointer<Value>

    public init(_ value: consuming Value) {
        valuePointer = UnsafeMutablePointer.allocate(capacity: 1)
        valuePointer.initialize(to: value)
    }

    public var value: Value {
        get { valuePointer.pointee }
        set { valuePointer.pointee = newValue }
    }

    deinit {
        valuePointer.deinitialize(count: 1)
        valuePointer.deallocate()
    }
}
```

### 'borrow' and 'mutate' accessors — [28:19]

```swift
@safe public struct UniqueBox<Value: ~Copyable>: ~Copyable {
    private let valuePointer: UnsafeMutablePointer<Value>

    public init(_ value: consuming Value) {
        valuePointer = UnsafeMutablePointer.allocate(capacity: 1)
        valuePointer.initialize(to: value)
    }

    public var value: Value {
        borrow { valuePointer.pointee }
        mutate { &valuePointer.pointee }
    }

    deinit {
        valuePointer.deinitialize(count: 1)
        valuePointer.deallocate()
    }
}
```

### Using 'MutableRef' to eliminate repeated accesses (with un-hoisted access) — [30:14]

```swift
func updateCount<Key: Hashable>(
    for key: Key,
    from sets: [Set<Key>],
    in counts: inout [Key: Int]
) {
    for set in sets {
        if set.contains(key) {
            counts[key, default: 0] += 1
        }
    }
}
```

### Using 'MutableRef' to eliminate repeated accesses (hoisted by 'inout' parameter) — [30:34]

```swift
func updateCount<Key: Hashable>(
    for key: Key,
    from sets: [Set<Key>],
    in counts: inout [Key: Int]
) {
    func updateCountImpl(count: inout Int) {
        for set in sets {
            if set.contains(key) {
                count += 1
            }
        }
    }

    updateCountImpl(count: &counts[key, default: 0])
}
```

### Using 'MutableRef' to eliminate repeated accesses (hoisted by 'MutableRef') — [30:41]

```swift
func updateCount<Key: Hashable>(
    for key: Key,
    from sets: [Set<Key>],
    in counts: inout [Key: Int]
) {
    var countRef = MutableRef(&counts[key, default: 0])

    for set in sets {
        if set.contains(key) {
            countRef.value += 1
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/262/5/d430e425-34fc-4ed5-b590-507ac593453a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/262/5/d430e425-34fc-4ed5-b590-507ac593453a/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._