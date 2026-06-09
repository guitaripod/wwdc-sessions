---
id: "wwdc2023-10164"
event: "wwdc2023"
year: 2023
title: "What’s new in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10164"
topics: ["Developer Tools", "Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What’s new in Swift

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10164](https://developer.apple.com/videos/play/wwdc2023/10164)

Join us for an update on Swift. We’ll show you how APIs are becoming more extensible and expressive with features like parameter packs and macros. We’ll also take you through improvements to interoperability and share how we’re expanding Swift’s performance and safety benefits everywhere from Foundation to large-scale distributed programs on the server.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,098 words)

## Documentation & Resources

- [Swift CMake Examples](https://github.com/apple/swift-cmake-examples) _samplecode_
- [The Future of Foundation](https://www.swift.org/blog/future-of-foundation/) _guide_
- [Evolving Swift Project Workgroups](https://www.swift.org/blog/evolving-swift-project-workgroups/) _guide_
- [Swift Evolution](https://apple.github.io/swift-evolution/) _guide_

## Code Snippets

### Hard-to-read compound ternary expression — [3:06]

```swift
let bullet =
    isRoot && (count == 0 || !willExpand) ? ""
        : count == 0    ? "- "
        : maxDepth <= 0 ? "▹ " : "▿ "
```

### Familiar and readable chain of if statements — [3:19]

```swift
let bullet =
    if isRoot && (count == 0 || !willExpand) { "" }
    else if count == 0 { "- " }
    else if maxDepth <= 0 { "▹ " }
    else { "▿ " }
```

### Initializing a global variable or stored property — [3:30]

```swift
let attributedName = AttributedString(markdown: displayName)
```

### In 5.9, if statements can be an expression — [3:46]

```swift
let attributedName = 
				if let displayName, !displayName.isEmpty {
            AttributedString(markdown: displayName)
        } else {
            "Untitled"
        }
```

### In Swift 5.7, errors may appear in a different place — [4:31]

```swift
struct ContentView: View {
    enum Destination { case one, two }

    var body: some View {
        List {
            NavigationLink(value: .one) { // The issue actually occurs here
                Text("one")
            }
            NavigationLink(value: .two) {
                Text("two")
            }
        }.navigationDestination(for: Destination.self) {
            $0.view // Error occurs here in 5.7
        }
    }
}
```

### In Swift 5.9, you now receive a more accurate compiler diagnostic — [4:47]

```swift
struct ContentView: View {
    enum Destination { case one, two }

    var body: some View {
        List {
            NavigationLink(value: .one) { //In 5.9, Errors provide a more accurate diagnostic
                Text("one")
            }
            NavigationLink(value: .two) {
                Text("two")
            }
        }.navigationDestination(for: Destination.self) {
            $0.view // Error occurs here in 5.7
        }
    }
}
```

### An API that takes a request type and evaluates it to produce a strongly typed value — [5:47]

```swift
struct Request<Result> { ... }

struct RequestEvaluator {
    func evaluate<Result>(_ request: Request<Result>) -> Result
}

func evaluate(_ request: Request<Bool>) -> Bool {
    return RequestEvaluator().evaluate(request)
}
```

### APIs that abstract over concrete types and varying number of arguments — [6:03]

```swift
let value = RequestEvaluator().evaluate(request)

let (x, y) = RequestEvaluator().evaluate(r1, r2)

let (x, y, z) = RequestEvaluator().evaluate(r1, r2, r3)
```

### Writing multiple overloads for the evaluate function — [6:35]

```swift
func evaluate<Result>(_:) -> (Result)

func evaluate<R1, R2>(_:_:) -> (R1, R2)

func evaluate<R1, R2, R3>(_:_:_:) -> (R1, R2, R3)

func evaluate<R1, R2, R3, R4>(_:_:_:_:)-> (R1, R2, R3, R4)

func evaluate<R1, R2, R3, R4, R5>(_:_:_:_:_:) -> (R1, R2, R3, R4, R5)

func evaluate<R1, R2, R3, R4, R5, R6>(_:_:_:_:_:_:) -> (R1, R2, R3, R4, R5, R6)
```

### Overloads create an arbitrary upper bound for the number of arguments — [6:47]

```swift
//This will cause a compiler error "Extra argument in call"
let results = evaluator.evaluate(r1, r2, r3, r4, r5, r6, r7)
```

### Individual type parameter — [7:12]

```swift
<each Result>
```

### Collapsing the same set of overloads into one single evaluate function — [7:36]

```swift
func evaluate<each Result>(_: repeat Request<each Result>) -> (repeat each Result)
```

### Calling updated evaluate function looks identical to calling an overload — [8:21]

```swift
struct Request<Result> { ... }

struct RequestEvaluator {
    func evaluate<each Result>(_: repeat Request<each Result>) -> (repeat each Result)
}

let results = RequestEvaluator.evaluate(r1, r2, r3)
```

### It isn't clear why an assert function fails — [10:01]

```swift
assert(max(a, b) == c)
```

### XCTest provides an assert-equal operation — [10:20]

```swift
XCAssertEqual(max(a, b), c) //XCTAssertEqual failed: ("10") is not equal to ("17")
```

### Assert as a macro — [11:02]

```swift
#assert(max(a, b) == c)
```

### Macros are distributed as packages — [11:42]

```swift
import PowerAssert
#assert(max(a, b) == c)
```

### Macro declaration for assert — [12:07]

```swift
public macro assert(_ condition: Bool)
```

### Uses are type checked against the parameters — [12:26]

```swift
import PowerAssert
#assert(max(a, b)) //Type 'Int' cannot be a used as a boolean; test for '!= 0' instead
```

### A macro definition — [12:52]

```swift
public macro assert(_ condition: Bool) = #externalMacro(
    module: “PowerAssertPlugin”,
    type: “PowerAssertMacro"
)
```

### Swift compiler passes the source code for the use of the macro — [13:11]

```swift
#assert(a == b)
```

### Compiler plugin produces new source code, which is integrated back into the Swift program — [13:14]

```swift
PowerAssert.Assertion(
    "#assert(a == b)"
) {
    $0.capture(a, column: 8) == $0.capture(b, column: 13)
}
```

### Macro declarations include roles — [13:33]

```swift
// Freestanding macro roles

@freestanding(expression)
public macro assert(_ condition: Bool) = #externalMacro(
    module: “PowerAssertPlugin”,
    type: “PowerAssertMacro"
)
```

### New Foundation Predicate APIs uses a `@freestanding(expression)` macro role — [13:53]

```swift
let pred = #Predicate<Person> {
    $0.favoriteColor == .blue
}

let blueLovers = people.filter(pred)
```

### Predicate expression macro — [14:14]

```swift
// Predicate expression macro

@freestanding(expression) 
public macro Predicate<each Input>(
    _ body: (repeat each Input) -> Bool
) -> Predicate<repeat each Input>
```

### Example of a commonly used enum — [14:48]

```swift
enum Path {
    case relative(String)
    case absolute(String)
}
```

### Checking a specific case, like when filtering all absolute paths — [15:01]

```swift
let absPaths = paths.filter { $0.isAbsolute }
```

### Write an `isAbsolute` check as a computer property... — [15:09]

```swift
extension Path {
    var isAbsolute: Bool {
        if case .absolute = self { true }
        else { false }
    }
}
```

### ...And another for `isRelative` — [15:12]

```swift
extension Path {
    var isRelative: Bool {
        if case .relative = self { true }
        else { false }
    }
}
```

### Augmenting the enum with an attached macro — [15:17]

```swift
@CaseDetection
enum Path {
    case relative(String)
    case absolute(String)
}

let absPaths = paths.filter { $0.isAbsolute }
```

### Macro-expanded code is normal Swift code — [15:36]

```swift
enum Path {
    case relative(String)
    case absolute(String)

    //Expanded @CaseDetection macro integrated into the program.
    var isAbsolute: Bool {
        if case .absolute = self { true }
        else { false }
    }

    var isRelative: Bool {
        if case .relative = self { true }
        else { false }
    }
}
```

### Observation in SwiftUI prior to 5.9 — [16:57]

```swift
// Observation in SwiftUI

final class Person: ObservableObject {
    @Published var name: String
    @Published var age: Int
    @Published var isFavorite: Bool
}

struct ContentView: View {
    @ObservedObject var person: Person

    var body: some View {
        Text("Hello, \(person.name)")
    }
}
```

### Observation now — [17:25]

```swift
// Observation in SwiftUI

@Observable final class Person {
    var name: String
    var age: Int
    var isFavorite: Bool
}

struct ContentView: View {
    var person: Person

    var body: some View {
        Text("Hello, \(person.name)")
    }
}
```

### Observable macro works with 3 macro roles — [17:42]

```swift
@attached(member, names: ...)
@attached(memberAttribute)
@attached(conformance)
public macro Observable() = #externalMacro(...).
```

### Unexpanded macro — [17:52]

```swift
@Observable final class Person {
    var name: String
    var age: Int
    var isFavorite: Bool
}
```

### Expanded member attribute role — [18:05]

```swift
@Observable final class Person {
    var name: String
    var age: Int
    var isFavorite: Bool

		internal let _$observationRegistrar = ObservationRegistrar<Person>()
    internal func access<Member>(
        keyPath: KeyPath<Person, Member>
    ) {
        _$observationRegistrar.access(self, keyPath: keyPath)
    }
    internal func withMutation<Member, T>(
        keyPath: KeyPath<Person, Member>,
        _ mutation: () throws -> T
    ) rethrows -> T {
        try _$observationRegistrar.withMutation(of: self, keyPath: keyPath, mutation)
    }
}
```

### Member attribute role adds `@ObservationTracked` to stored properties — [18:12]

```swift
@Observable final class Person {
    @ObservationTracked var name: String
    @ObservationTracked var age: Int
    @ObservationTracked var isFavorite: Bool

		internal let _$observationRegistrar = ObservationRegistrar<Person>()
    internal func access<Member>(
        keyPath: KeyPath<Person, Member>
    ) {
        _$observationRegistrar.access(self, keyPath: keyPath)
    }
    internal func withMutation<Member, T>(
        keyPath: KeyPath<Person, Member>,
        _ mutation: () throws -> T
    ) rethrows -> T {
        try _$observationRegistrar.withMutation(of: self, keyPath: keyPath, mutation)
    }
}
```

### The @ObservationTracked macro adds getters and setters to stored properties — [18:16]

```swift
@Observable final class Person {
    @ObservationTracked var name: String { get { … } set { … } }
    @ObservationTracked var age: Int { get { … } set { … } }
    @ObservationTracked var isFavorite: Bool { get { … } set { … } }

		internal let _$observationRegistrar = ObservationRegistrar<Person>()
    internal func access<Member>(
        keyPath: KeyPath<Person, Member>
    ) {
        _$observationRegistrar.access(self, keyPath: keyPath)
    }
    internal func withMutation<Member, T>(
        keyPath: KeyPath<Person, Member>,
        _ mutation: () throws -> T
    ) rethrows -> T {
        try _$observationRegistrar.withMutation(of: self, keyPath: keyPath, mutation)
    }
}
```

### All that Swift code is folded away in the @Observable macro — [18:33]

```swift
@Observable final class Person {
    var name: String
    var age: Int
    var isFavorite: Bool
}
```

### A wrapper for a file descriptor — [23:59]

```swift
struct FileDescriptor {
    private var fd: CInt

    init(descriptor: CInt) { self.fd = descriptor }

    func write(buffer: [UInt8]) throws {
        let written = buffer.withUnsafeBufferPointer {
            Darwin.write(fd, $0.baseAddress, $0.count)
        }
        // ...
    }

    func close() {
        Darwin.close(fd)
    }
}
```

### The same FileDescriptor wrapper as a class — [24:30]

```swift
class FileDescriptor {
    private var fd: CInt

    init(descriptor: CInt) { self.fd = descriptor }

    func write(buffer: [UInt8]) throws {
        let written = buffer.withUnsafeBufferPointer {
            Darwin.write(fd, $0.baseAddress, $0.count)
        }
        // ...
    }

    func close() {
        Darwin.close(fd)
    }
    deinit {
        self.close(fd)
    }
}
```

### Going back to the struct — [25:05]

```swift
struct FileDescriptor {
    private var fd: CInt

    init(descriptor: CInt) { self.fd = descriptor }

    func write(buffer: [UInt8]) throws {
        let written = buffer.withUnsafeBufferPointer {
            Darwin.write(fd, $0.baseAddress, $0.count)
        }
        // ...
    }

    func close() {
        Darwin.close(fd)
    }
}
```

### Using Copyable in the FileDescriptor struct — [26:06]

```swift
struct FileDescriptor: ~Copyable {
    private var fd: CInt

    init(descriptor: CInt) { self.fd = descriptor }

    func write(buffer: [UInt8]) throws {
        let written = buffer.withUnsafeBufferPointer {
            Darwin.write(fd, $0.baseAddress, $0.count)
        }
        // ...
    }

    func close() {
        Darwin.close(fd)
    }

    deinit {
        Darwin.close(fd)
    }
}
```

### `close()` can also be marked as consuming — [26:35]

```swift
struct FileDescriptor {
    private var fd: CInt

    init(descriptor: CInt) { self.fd = descriptor }

    func write(buffer: [UInt8]) throws {
        let written = buffer.withUnsafeBufferPointer {
            Darwin.write(fd, $0.baseAddress, $0.count)
        }
        // ...
    }

    consuming func close() {
        Darwin.close(fd)
    }

    deinit {
        Darwin.close(fd)
    }
}
```

### When `close()` is called, it must be the final use — [26:53]

```swift
let file = FileDescriptor(fd: descriptor)
file.write(buffer: data)
file.close()
```

### Compiler errors instead of runtime failures — [27:20]

```swift
let file = FileDescriptor(fd: descriptor)
file.close() // Compiler will indicate where the consuming use is
file.write(buffer: data) // Compiler error: 'file' used after consuming
```

### Using C++ from Swift — [28:52]

```swift
// Person.h
struct Person {
    Person(const Person &);
    Person(Person &&);
    Person &operator=(const Person &);
    Person &operator=(Person &&);
    ~Person();

    std::string name;
    unsigned getAge() const;
};
std::vector<Person> everyone();

// Client.swift
func greetAdults() {
    for person in everyone().filter { $0.getAge() >= 18 } {
        print("Hello, \(person.name)!")
    }
}
```

### Using Swift from C++ — [29:51]

```cpp
// Geometry.swift
struct LabeledPoint {
    var x = 0.0, y = 0.0
    var label: String = “origin”
    mutating func moveBy(x deltaX: Double, y deltaY: Double) { … }
    var magnitude: Double { … }
}

// C++ client
#include <Geometry-Swift.h>

void test() {
    Point origin = Point()
    Point unit = Point::init(1.0, 1.0, “unit”)
    unit.moveBy(2, -2)
    std::cout << unit.label << “ moved to “ << unit.magnitude() << std::endl;
}
```

### An actor that manages a database connection — [35:30]

```swift
// Custom actor executors

actor MyConnection {
    private var database: UnsafeMutablePointer<sqlite3>

    init(filename: String) throws { … }

    func pruneOldEntries() { … }
    func fetchEntry<Entry>(named: String, type: Entry.Type) -> Entry? { … }
}

await connection.pruneOldEntries()
```

### MyConnection with a serial dispatch queue and a custom executor — [35:58]

```swift
actor MyConnection {
  private var database: UnsafeMutablePointer<sqlite3>
  private let queue: DispatchSerialQueue

  nonisolated var unownedExecutor: UnownedSerialExecutor { queue.asUnownedSerialExecutor() }

  init(filename: String, queue: DispatchSerialQueue) throws { … }

  func pruneOldEntries() { … }
  func fetchEntry<Entry>(named: String, type: Entry.Type) -> Entry? { … }
}

await connection.pruneOldEntries()
```

### Dispatch queues conform to SerialExecutor protocol — [36:44]

```swift
// Executor protocols

protocol Executor: AnyObject, Sendable {
    func enqueue(_ job: consuming ExecutorJob)
}

protocol SerialExecutor: Executor {
    func asUnownedSerialExecutor() -> UnownedSerialExecutor
    func isSameExclusiveExecutionContext(other executor: Self) -> Bool
}

extension DispatchSerialQueue: SerialExecutor { … }
```

### C++ implementation of FoundationDB's "master data" actor — [39:22]

```cpp
// C++ implementation of FoundationDB’s “master data” actor

ACTOR Future<Void> getVersion(Reference<MasterData> self, GetCommitVersionRequest req) {
  	state std::map<UID, CommitProxyVersionReplies>::iterator proxyItr = self->lastCommitProxyVersionReplies.find(req.requestingProxy);
  	++self->getCommitVersionRequests;

  	if (proxyItr == self->lastCommitProxyVersionReplies.end()) {
      	req.reply.send(Never());
    	  return Void();
  	}
  	wait(proxyItr->second.latestRequestNum.whenAtLeast(req.requestNum - 1));

  	auto itr = proxyItr->second.replies.find(req.requestNum);
  	if (itr != proxyItr->second.replies.end()) {
    		req.reply.send(itr->second);
    		return Void();
  	}

  	// ...
}
```

### Swift implementation of FoundationDB's "master data" actor — [40:18]

```swift
// Swift implementation of FoundationDB’s “master data” actor
func getVersion(
    myself: MasterData, req: GetCommitVersionRequest
) async -> GetCommitVersionReply? {
    myself.getCommitVersionRequests += 1

    guard let lastVersionReplies = lastCommitProxyVersionReplies[req.requestingProxy] else {
        return nil
    }

    // ...
    var latestRequestNum = try await lastVersionReplies.latestRequestNum
          .atLeast(VersionMetricHandle.ValueType(req.requestNum - UInt64(1)))

    if let lastReply = lastVersionReplies.replies[req.requestNum] {
        return lastReply
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10164/4/6A73A62C-E994-4907-B0CD-58E632F43AF6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10164/4/6A73A62C-E994-4907-B0CD-58E632F43AF6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10164) — developer.apple.com. Indexed for agent consumption._
