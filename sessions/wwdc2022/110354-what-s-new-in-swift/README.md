---
id: "wwdc2022-110354"
event: "wwdc2022"
year: 2022
title: "What's new in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110354"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in Swift

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110354](https://developer.apple.com/videos/play/wwdc2022/110354)

Join us for an update on Swift. We'll take you through performance improvements, explore more secure and extensible Swift packages, and share advancements in Swift concurrency. We'll also introduce you to Swift Regex, better generics, and other tools built into the language to help you write more flexible & expressive code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,283 words)

## Documentation & Resources

- [Celebrating learning experiences from the 2021 Swift Mentorship Program](https://www.swift.org/blog/mentorship-2022/) _guide_
- [Contribute to Swift](https://www.swift.org/contributing/) _guide_
- [Swift Mentorship Program](https://swift.org/mentorship/) _documentation_
- [Diversity in Swift](https://swift.org/diversity/) _documentation_

## Code Snippets

### Command plugins — [7:19]

```swift
@main struct MyPlugin: CommandPlugin {

    func performCommand(context: PluginContext, arguments: [String]) throws {
        let process = try Process.run(doccExec, arguments: doccArgs)
        process.waitUntilExit()
    }

}
```

### Build tool plugins — [8:34]

```swift
import PackagePlugin

@main struct MyCoolPlugin: BuildToolPlugin {
    func createBuildCommands(context: TargetBuildContext) throws -> [Command] {
        // Run some command
    }
}
```

### Implementing a build tool plugin — [8:39]

```swift
import PackagePlugin

@main struct MyCoolPlugin: BuildToolPlugin {
    func createBuildCommands(context: TargetBuildContext) throws -> [Command] {

        let generatedSources = context.pluginWorkDirectory.appending("GeneratedSources")

        return [
            .buildCommand(
                displayName: "Running MyTool",
                executable: try context.tool(named: "mycooltool").path,
                arguments: ["create"],
                outputFilesDirectory: generatedSources)
        ]
    }
}
```

### Module disambiguation with module aliases — [9:23]

```swift
let package = Package(
        name: "MyStunningApp",
        dependencies: [
            .package(url: "https://.../swift-metrics.git"),
            .package(url: "https://.../swift-log.git")
        ],
        products: [
            .executable(name: "MyStunningApp", targets: ["MyStunningApp"])
        ],
        targets: [
            .executableTarget(
                name: "MyStunningApp",
                dependencies: [
                    .product(name: "Logging", 
                             package: "swift-log"),
                    .product(name: "Metrics", 
                             package: "swift-metrics",
                             moduleAliases: ["Logging": "MetricsLogging"]),
  ])])
```

### Distinguishing between modules with the same name — [9:42]

```swift
// MyStunningApp

import Logging           // from swift-log
import MetricsLogging    // from swift-metrics

let swiftLogger = Logging.Logger()

let metricsLogger = MetricsLogging.Logger()
```

### Example set of protocols — [11:09]

```swift
public protocol NonEmptyProtocol: Collection
    where Element == C.Element, 
        Index == C.Index {
    associatedtype C: Collection
}

public protocol MultiPoint {
    associatedtype C: CoordinateSystem
    typealias P = Self.C.P

    associatedtype X: NonEmptyProtocol 
        where X.C: NonEmptyProtocol, 
            X.Element == Self.P
}

public protocol CoordinateSystem {
    associatedtype P: Point where Self.P.C == Self
    associatedtype S: Size where Self.S.C == Self
    associatedtype L: Line where Self.L.C == Self
    associatedtype B: BoundingBox where Self.B.C == Self
}

public protocol Line: MultiPoint {}

public protocol Size {
    associatedtype C: CoordinateSystem where Self.C.S == Self
}

public protocol BoundingBox {
    associatedtype C: CoordinateSystem
    typealias P = Self.C.P
    typealias S = Self.C.S
}

public protocol Point {
    associatedtype C: CoordinateSystem where Self.C.P == Self
}
```

### Memory safety in Swift — [13:14]

```swift
var numbers = [3, 2, 1]

numbers.removeAll(where: { number in
    number == numbers.count 
})
```

### Thread safety in Swift — [14:10]

```swift
var numbers = [3, 2, 1]

Task { numbers.append(0) } 

numbers.removeLast()
```

### A distributed actor player and a distributed function — [15:54]

```swift
distributed actor Player {

    var ai: PlayerBotAI?
    var gameState: GameState

    distributed func makeMove() -> GameMove {
        return ai.decideNextMove(given: &gameState)
    }
}
```

### A distributed actor call — [16:20]

```swift
func endOfRound(players: [Player]) async throws {
    // Have each of the players make their move
    for player in players {
        let move = try await player.makeMove()
    }
}
```

### Optional unwrapping — [20:12]

```swift
if let mailmapURL = mailmapURL {

    mailmapLines = try String(contentsOf: mailmapURL).split(separator: "\n")

}
```

### Optional unwrapping with long variable names — [20:29]

```swift
if let workingDirectoryMailmapURL = workingDirectoryMailmapURL {

    mailmapLines = try String(contentsOf: workingDirectoryMailmapURL).split(separator: "\n")

}
```

### Cryptic abbreviated variable names — [20:35]

```swift
if let wdmu = workingDirectoryMailmapURL {

    mailmapLines = try String(contentsOf: wdmu).split(separator: "\n")

}
```

### Unwrapping optionals in Swift 5.7 — [20:46]

```swift
if let workingDirectoryMailmapURL {

    mailmapLines = try String(contentsOf: workingDirectoryMailmapURL).split(separator: "\n")

}

guard let workingDirectoryMailmapURL else { return }

mailmapLines = try String(contentsOf: workingDirectoryMailmapURL).split(separator: "\n")
```

### Closure type inference — [21:07]

```swift
let entries = mailmapLines.compactMap { line in

    try? parseLine(line)

}

func parseLine(_ line: Substring) throws -> MailmapEntry { … }
```

### Type inference for complicated closures — [21:33]

```swift
let entries = mailmapLines.compactMap { line in
    do {        
        return try parseLine(line)
    }
    catch {
        logger.warn("Mailmap error: \(error)")
        return nil
    }
}


func parseLine(_ line: Substring) throws -> MailmapEntry { … }
```

### Mismatches that are harmless in C... — [22:15]

```swift
// Mismatches that are harmless in C…
int mailmap_get_size(mailmap_t *map);
void mailmap_truncate(mailmap_t *map, unsigned *sizeInOut);

void remove_duplicates(mailmap_t *map) {
    int size = mailmap_get_size(map);
    size -= move_duplicates_to_end(map);
    mailmap_truncate(map, &size);
}


// …cause problems in Swift.
func removeDuplicates(from map: UnsafeMutablePointer<mailmap_t>) {
    var size = mailmap_get_size(map)
    size -= moveDuplicatesToEnd(map)
    mailmap_truncate(map, &size)
}
```

### Better interoperability with C-family code — [22:33]

```swift
func removeDuplicates(from map: UnsafeMutablePointer<mailmap_t>) {
    var size = mailmap_get_size(map)
    size -= moveDuplicatesToEnd(map)
    withUnsafeMutablePointer(to: &size) { signedSizePtr in
        signedSizePtr.withMemoryRebound(to: UInt32.self, capacity: 1) { unsignedSizePtr in
            mailmap_truncate(map, unsignedSizePtr)
        }
    }
}
```

### String parsing is hard — [23:41]

```swift
func parseLine(_ line: Substring) throws -> MailmapEntry {
    func trim(_ str: Substring) -> Substring {
        String(str).trimmingCharacters(in: .whitespacesAndNewlines)[...]
    }

    let activeLine = trim(line[..<(line.firstIndex(of: "#") ?? line.endIndex)])
    guard let nameEnd = activeLine.firstIndex(of: "<"),
          let emailEnd = activeLine[nameEnd...].firstIndex(of: ">"),
          trim(activeLine[activeLine.index(after: emailEnd)...]).isEmpty else {
        throw MailmapError.badLine
    }

    let name = nameEnd == activeLine.startIndex ? nil : trim(activeLine[..<nameEnd])
    let email = activeLine[activeLine.index(after: nameEnd)..<emailEnd]

    return MailmapEntry(name: name, email: email)
}
```

### String parsing is still hard with better indexing — [24:05]

```swift
func parseLine(_ line: Substring) throws -> MailmapEntry {
    func trim(_ str: Substring) -> Substring {
        String(str).trimmingCharacters(in: .whitespacesAndNewlines)[...]
    }

    let activeLine = trim(line[..<(line.firstIndex(of: "#") ?? line.endIndex)])
    guard let nameEnd = activeLine.firstIndex(of: "<"),
          let emailEnd = activeLine[nameEnd...].firstIndex(of: ">"),
          trim(activeLine[(emailEnd + 1)...]).isEmpty else {
        throw MailmapError.badLine
    }

    let name = nameEnd == activeLine.startIndex ? nil : trim(activeLine[..<nameEnd])
    let email = activeLine[(nameEnd + 1)..<emailEnd]

    return MailmapEntry(name: name, email: email)
}
```

### What's the problem? — [24:20]

```swift
let line = "Becca Royal-Gordon <beccarg@apple.com>       # Comment"

func parseLine(_ line: Substring) throws -> MailmapEntry {
    func trim(_ str: Substring) -> Substring {
        String(str).trimmingCharacters(in: .whitespacesAndNewlines)[...]
    }

    let activeLine = trim(line[..<(line.firstIndex(of: "#") ?? line.endIndex)])
    guard let nameEnd = activeLine.firstIndex(of: "<"),
          let emailEnd = activeLine[nameEnd...].firstIndex(of: ">"),
          trim(activeLine[activeLine.index(after: emailEnd)...]).isEmpty else {
        throw MailmapError.badLine
    }

    let name = nameEnd == activeLine.startIndex ? nil : trim(activeLine[..<nameEnd])
    let email = activeLine[activeLine.index(after: nameEnd)..<emailEnd]

    return MailmapEntry(name: name, email: email)
}
```

### Drawing a picture — [24:55]

```swift
"Becca Royal-Gordon <beccarg@apple.com>       # Comment"

/  space name space <      email      > space # or EOL /
/  \h* ( [^<#]+? )?? \h* < ( [^>#]+ ) > \h* (?: #|\Z)  /
```

### Swift Regex using a literal — [25:10]

```swift
func parseLine(_ line: Substring) throws -> MailmapEntry {

    let regex = /\h*([^<#]+?)??\h*<([^>#]+)>\h*(?:#|\Z)/

    guard let match = line.prefixMatch(of: regex) else {
        throw MailmapError.badLine
    }

    return MailmapEntry(name: match.1, email: match.2)
}
```

### Did a cat walk across your keyboard? — [25:46]

```swift
/\h*([^<#]+?)??\h*<([^>#]+)>\h*(?:#|\Z)/
```

### Regex builder — [26:34]

```swift
import RegexBuilder

let regex = Regex {
    ZeroOrMore(.horizontalWhitespace)

    Optionally {
        Capture(OneOrMore(.noneOf("<#")))
    }
        .repetitionBehavior(.reluctant)

    ZeroOrMore(.horizontalWhitespace)

    "<"
    Capture(OneOrMore(.noneOf(">#")))
    ">"

    ZeroOrMore(.horizontalWhitespace)
    ChoiceOf {
       "#"
       Anchor.endOfSubjectBeforeNewline
    }
}
```

### Turn a regex into a reusable component — [27:05]

```swift
struct MailmapLine: RegexComponent {
    @RegexComponentBuilder
    var regex: Regex<(Substring, Substring?, Substring)> {
        ZeroOrMore(.horizontalWhitespace)

        Optionally {
            Capture(OneOrMore(.noneOf("<#")))
        }
            .repetitionBehavior(.reluctant)

        ZeroOrMore(.horizontalWhitespace)

        "<"
        Capture(OneOrMore(.noneOf(">#")))
        ">"

        ZeroOrMore(.horizontalWhitespace)
        ChoiceOf {
           "#"
            Anchor.endOfSubjectBeforeNewline
        }
    }
}
```

### Use regex literals within a builder — [27:30]

```swift
struct MailmapLine: RegexComponent {
    @RegexComponentBuilder
    var regex: Regex<(Substring, Substring?, Substring)> {
        ZeroOrMore(.horizontalWhitespace)

        Optionally {
            Capture(OneOrMore(.noneOf("<#")))
        }
            .repetitionBehavior(.reluctant)

        ZeroOrMore(.horizontalWhitespace)

        "<" 
        Capture(OneOrMore(.noneOf(">#")))
        ">" 

        ZeroOrMore(.horizontalWhitespace)
        /#|\Z/
   }
}
```

### Use Date parsers within Regex builders — [27:39]

```swift
struct DatedMailmapLine: RegexComponent {
    @RegexComponentBuilder
    var regex: Regex<(Substring, Substring?, Substring, Date)> {
        ZeroOrMore(.horizontalWhitespace)

        Optionally {
            Capture(OneOrMore(.noneOf("<#")))
        }
            .repetitionBehavior(.reluctant)

        ZeroOrMore(.horizontalWhitespace)

        "<" 
        Capture(OneOrMore(.noneOf(">#")))
        ">" 

        ZeroOrMore(.horizontalWhitespace)

        Capture(.iso8601.year().month().day())

        ZeroOrMore(.horizontalWhitespace)
        /#|\Z/
   }
}
```

### Matching methods and strongly type captures in Regex — [27:49]

```swift
func parseLine(_ line: Substring) throws -> MailmapEntry {

    let regex = /\h*([^<#]+?)??\h*<([^>#]+)>\h*(?:#|\Z)/
    // or let regex = MailmapLine()

    guard let match = line.prefixMatch(of: regex) else {
        throw MailmapError.badLine
    }

    return MailmapEntry(name: match.1, email: match.2)
}
```

### A use case for protocols — [29:02]

```swift
/// Used in the commit list UI
struct HashedMailmap {
    var replacementNames: [String: String] = [:]
}

/// Used in the mailmap editor UI
struct OrderedMailmap {
    var entries: [MailmapEntry] = []
}

protocol Mailmap {
    mutating func addEntry(_ entry: MailmapEntry)
}

extension HashedMailmap: Mailmap { … }
extension OrderedMailmap: Mailmap { … }
```

### Using the Mailmap protocol — [29:26]

```swift
func addEntries1<Map: Mailmap>(_ entries: Array<MailmapEntry>, to mailmap: inout Map) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: Array<MailmapEntry>, to mailmap: inout Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### `Mailmap` and `any Mailmap` — [31:05]

```swift
func addEntries1<Map: Mailmap>(_ entries: Array<MailmapEntry>, to mailmap: inout Map) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: Array<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### Improvements to `any` types — [31:17]

```swift
extension Mailmap {
    mutating func mergeEntries<Other: Mailmap>(from other: Other) { … }
}

func mergeMailmaps(_ a: any Mailmap, _ b: any Mailmap) -> any Mailmap {
    var copy = a
    copy.mergeEntries(from: b)
    return a
}
```

### More improvements to `any` types — [32:21]

```swift
protocol Mailmap: Equatable {
    mutating func addEntry(_ entry: MailmapEntry)
}

func addEntries2(_ entries: Array<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### Using Collection as an `any` type — [32:54]

```swift
protocol Mailmap: Equatable {
    mutating func addEntry(_ entry: MailmapEntry)
}

func addEntries2(_ entries: any Collection<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### Primary associated types — [33:04]

```swift
protocol Collection<Element>: Sequence {
    associatedtype Index: Comparable
    associatedtype Iterator: IteratorProtocol<Element>
    associatedtype SubSequence: Collection<Element>
                                    where SubSequence.Index == Index,
                                          SubSequence.SubSequence == SubSequence

    associatedtype Element
}
```

### Using primary associated types in Collection — [33:42]

```swift
func addEntries1<Entries: Collection<MailmapEntry>, Map: Mailmap>(_ entries: Entries, to mailmap: inout Map) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: any Collection<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

extension Collection<MailmapEntry> { … }
```

### Example of type erasing wrappers — [34:35]

```swift
struct AnySprocket: Sprocket {
    private class Base { … }
    private class Box<S: Sprocket>: Base { … }
    private var box: Base

    // …dozens of lines of code you hate
    // having to maintain…
}
```

### Replace boxes with built-in `any` types — [34:38]

```swift
struct AnySprocket: Sprocket {
    private var box: any Sprocket

    // …fewer lines of code you hate
    // having to maintain…
}
```

### Or try type aliases — [34:44]

```swift
typealias AnySprocket = any Sprocket
```

### `any` types have important limitations — [35:09]

```swift
protocol Mailmap: Equatable {
    mutating func addEntry(_ entry: MailmapEntry)
}

func areMailmapsIdentical(_ a: any Mailmap, _ b: any Mailmap) -> Bool {
    return a == b
}
```

### Using generic types vs. `any` types — [35:44]

```swift
func addEntries1<Entries: Collection<MailmapEntry>, Map: Mailmap>(_ entries: Entries, to mailmap: inout Map) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: any Collection<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### `some Mailmap` and `any Mailmap` — [36:40]

```swift
func addEntries1<Entries: Collection<MailmapEntry>>(_ entries: Entries, to mailmap: inout some Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: any Collection<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

### `some Mailmap` and `any Mailmap` with Collection and primary associated types — [36:50]

```swift
func addEntries1(_ entries: some Collection<MailmapEntry>, to mailmap: inout some Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}

func addEntries2(_ entries: any Collection<MailmapEntry>, to mailmap: inout any Mailmap) {
    for entry in entries {
        mailmap.addEntry(entry)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110354/5/BFF5625D-B11D-4C9D-B82B-E7A89A669475/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110354/5/BFF5625D-B11D-4C9D-B82B-E7A89A669475/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110354) — developer.apple.com. Indexed for agent consumption._
