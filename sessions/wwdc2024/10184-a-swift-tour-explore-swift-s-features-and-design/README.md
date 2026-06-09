---
id: "wwdc2024-10184"
event: "wwdc2024"
year: 2024
title: "A Swift Tour: Explore Swift’s features and design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10184"
topics: ["Developer Tools", "Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# A Swift Tour: Explore Swift’s features and design

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10184](https://developer.apple.com/videos/play/wwdc2024/10184)

Learn the essential features and design philosophy of the Swift programming language. We’ll explore how to model data, handle errors, use protocols, write concurrent code, and more while building up a Swift package that has a library, an HTTP server, and a command line client. Whether you’re just beginning your Swift journey or have been with us from the start, this talk will help you get the most out of the language.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,497 words)

## Documentation & Resources

- [Tools used: Windows](https://www.microsoft.com/en-us/windows/) _guide_
- [Tools used: Visual Studio Code](https://code.visualstudio.com) _guide_
- [Tools used: Ubuntu](https://ubuntu.com/desktop) _guide_
- [Wrapping C/C++ Library in Swift](https://www.swift.org/documentation/articles/wrapping-c-cpp-library-in-swift.html) _documentation_
- [Value and Reference types](https://www.swift.org/documentation/articles/value-and-reference-types.html) _documentation_
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010
- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Integer variables — [1:49]

```swift
var x: Int = 1
var y: Int = x
x = 42
y
```

### User struct — [3:04]

```swift
struct User {
    let username: String
    var isVisible: Bool = true
    var friends: [String] = []
}

var alice = User(username: "alice")
alice.friends = ["charlie"]

var bruno = User(username: "bruno")
bruno.friends = alice.friends

alice.friends.append("dash")
bruno.friends
```

### User struct error handling — [3:05]

```swift
struct User {
    let username: String
    var isVisible: Bool = true
    var friends: [String] = []

    mutating func addFriend(username: String) throws {
        guard username != self.username else {
            throw SocialError.befriendingSelf
        }
        guard !friends.contains(username) else {
            throw SocialError.duplicateFriend(username: username)
        }
        friends.append(username)
    }
}

enum SocialError: Error {
    case befriendingSelf
    case duplicateFriend(username: String)
}

var alice = User(username: "alice")
do {
    try alice.addFriend(username: "charlie")
    try alice.addFriend(username: "charlie")
} catch {
    error
}

var allUsers = [
    "alice": alice
]

func findUser(_ username: String) -> User? {
    allUsers[username]
}

if let charlie = findUser("charlie") {
    print("Found \(charlie)")
} else {
    print("charlie not found")
}

let dash = findUser("dash")!
```

### SocialGraph package manifest — [11:01]

```swift
// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "SocialGraph",
    products: [
        .library(
            name: "SocialGraph",
            targets: ["SocialGraph"]),
    ],
    dependencies: [
      .package(url: "https://github.com/apple/swift-testing.git", branch: "main"),
    ],
    targets: [
        .target(
            name: "SocialGraph"),
        .testTarget(
            name: "SocialGraphTests",
            dependencies: [
                "SocialGraph",
                .product(name: "Testing", package: "swift-testing"),
            ]),
    ]
)
```

### User struct — [11:12]

```swift
/// Represents a user in the social graph.
public struct User: Equatable, Hashable {
    /// The user's username, which must be unique in the service.
    public let username: String

    /// Whether or not the user should be considered visible
    /// when performing queries.
    public var isVisible: Bool

    /// The usernames of the user's friends.
    public private(set) var friends: [String]

    public init(
        username: String,
        isVisible: Bool = true,
        friends: [String] = []
    ) {
        self.username = username
        self.isVisible = isVisible
        self.friends = friends
    }

    /// Adds a username to the user's list of friends. Throws an
    /// error if the username cannot be added.
    public mutating func addFriend(username: String) throws {
        guard username != self.username else {
            throw SocialError.befriendingSelf
        }
        guard !friends.contains(username) else {
            throw SocialError.alreadyFriend(username: username)
        }
        friends.append(username)
    }
}
```

### Classes — [12:36]

```swift
class Pet {
    func speak() {}
}

class Cat: Pet {
    override func speak() { print("meow") }

    func purr() { print("purr") }
}

let pet: Pet = Cat()
pet.speak()

if let cat = pet as? Cat {
    cat.purr()
}
```

### Automatic reference counting — [12:59]

```swift
class Pet {
    var toy: Toy?
}

class Toy {}

let toy = Toy()
let pets = [Pet()]

// Give toy to pets
for pet in pets {
    pet.toy = toy
}

// Take toy from pets
for pet in pets {
    pet.toy = nil
}
```

### Reference cycles — [13:26]

```swift
class Pet {
    weak var owner: Owner?
}

class Owner {
    var pets: [Pet]
}
```

### Protocols — [14:20]

```swift
protocol StringIdentifiable {
    var identifier: String { get }
}

extension User: StringIdentifiable {
    var identifier: String {
        username
    }
}
```

### Common capabilities of Collections — [15:21]

```swift
let string = "🥚🐣🐥🐓"
for char in string {
    print(char)
}
// => "🥚" "🐣" "🐥" "🐓"

print(string[string.startIndex])
// => "🥚"
```

### Collection algorithms — [15:31]

```swift
let numbers = [1, 4, 7, 10, 13]

let numberStrings = numbers.map { number in
    String(number)
}
// => ["1", "4", "7", "10", "13"]

let primeNumbers = numbers.filter { number in
    number.isPrime
}
// => [1, 7, 13]

let sum = numbers.reduce(0) { partial, number in
    partial + number
}
// => 35
```

### Collection algorithms with anonymous parameters — [15:45]

```swift
let numbers = [1, 4, 7, 10, 13]

let numberStrings = numbers.map { String($0) }
// => ["1", "4", "7", "10", "13"]



let primeNumbers = numbers.filter { $0.isPrime }
// => [1, 7, 13]



let sum = numbers.reduce(0) { $0 + $1 }
// => 35
```

### Friends of friends algorithm — [16:13]

```swift
/// An in-memory store for users of the service.
public class UserStore {
    var allUsers: [String: User] = [:]
}

extension UserStore {
    /// If the username maps to a User and that user is visible,
    /// returns the User. Returns nil otherwise.
    public func lookUpUser(_ username: String) -> User? {
        guard let user = allUsers[username],
              user.isVisible else {
            return nil
        }
        return user
    }

    /// If the username maps to a User and that user is visible,
    /// returns the User. Otherwise, throws an error.
    public func user(for username: String) throws -> User {
        guard let user = lookUpUser(username) else {
            throw SocialError.userNotFound(username: username)
        }
        return user
    }

    public func friendsOfFriends(_ username: String) throws -> [String] {
        let user = try user(for: username)
        let excluded = Set(user.friends + [username])
        return user.friends
            .compactMap { lookUpUser($0) }      // [String] -> [User]
            .flatMap { $0.friends }             // [User] -> [String]
            .filter { !excluded.contains($0) }  // drop excluded
            .uniqued()
    }
}

extension Collection where Element: Hashable {
    func uniqued() -> [Element] {
        let unique = Set(self)
        return Array(unique)
    }
}
```

### async/await — [19:23]

```swift
/// Makes a network request to download an image.
func fetchUserAvatar(for username: String) async -> Image {
    // ...
}

let avatar = await fetchUserAvatar(for: "alice")
```

### Server — [19:43]

```swift
import Hummingbird
import SocialGraph

let router = Router()

extension UserStore {
    static let shared = UserStore.makeSampleStore()
}

let app = Application(
    router: router,
    configuration: .init(address: .hostname("127.0.0.1", port: 8080))
)

print("Starting server...")
try await app.runService()
```

### Data race example — [20:20]

```swift
// Look up user
let user = allUsers[username]

// Store new user
allUsers[username] = user

// UserStore
var allUsers: [String: User]
```

### Server with friendsOfFriends route — [22:24]

```swift
import Hummingbird
import SocialGraph

let router = Router()

extension UserStore {
    static let shared = UserStore.makeSampleStore()
}

router.get("friendsOfFriends") { request, context -> [String] in
    let username = try request.queryArgument(for: "username")
    return try await UserStore.shared.friendsOfFriends(username)
}

let app = Application(
    router: router,
    configuration: .init(address: .hostname("127.0.0.1", port: 8080))
)

print("Starting server...")
try await app.runService()
```

### Property wrappers — [23:27]

```swift
struct FriendsOfFriends: AsyncParsableCommand {
    @Argument var username: String

    mutating func run() async throws {
        // ...
    }
}
```

### SocialGraph command line client — [23:57]

```swift
import ArgumentParser
import SocialGraph

@main
struct SocialGraphClient: AsyncParsableCommand {
    static let configuration = CommandConfiguration(
        abstract: "A utility for querying the social graph",
        subcommands: [
            FriendsOfFriends.self,
        ])
}

struct FriendsOfFriends: AsyncParsableCommand {
    @Argument(help: "The username to look up friends of friends for")
    var username: String

    func run() async throws {
        var request = Request(command: "friendsOfFriends", returning: [String].self)
        request.arguments = ["username" : username]
        let result = try await request.get()
        print(result)
    }
}
```

### Result builders — [26:07]

```swift
import RegexBuilder

let dollarValueRegex = Regex {  // Equivalent to "\$[0-9]+\.[0-9][0-9]"
    "$"
    OneOrMore(.digit)
    "."
    Repeat(.digit, count: 2)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10184/4/9805A8C3-1B6A-43C6-AA4B-C8A8FBBECE62/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10184/4/9805A8C3-1B6A-43C6-AA4B-C8A8FBBECE62/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10184) — developer.apple.com. Indexed for agent consumption._
