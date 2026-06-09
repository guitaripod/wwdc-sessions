---
id: "wwdc2021-10192"
event: "wwdc2021"
year: 2021
title: "What‘s new in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10192"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What‘s new in Swift

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10192](https://developer.apple.com/videos/play/wwdc2021/10192)

Join us for an update on Swift. Discover the latest language advancements that make your code easier to read and write. Explore the growing number of APIs available as Swift packages. And we’ll introduce you to Swift’s async/await syntax, structured concurrency, and actors.

**Keywords:** `algorithms`, `arc`, `argumentparser`, `asynchronous`, `automatic reference counting`, `aws`, `builds`, `cgfloat`, `codable`, `collections`, `concurrent`, `deque`, `diversity`, `docc`, `documentation`, `double`, `driver`, `enum`, `evolution`, `fish`, `flexible`, `float16`, `functions`, `incremental`, `index`, `lambda`, `lifetimes`, `linux`, `memory`, `mentorship`, `numerics`, `open source`, `optimize`, `ordereddictionary`, `orderedset`, `path`, `property wrappers`, `result builders`, `server`, `static member lookup`, `swiftui`, `system`, `toggle`, `windows`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,927 words)

## Documentation & Resources

- [Package Collections](https://swift.org/blog/package-collections) _documentation_
- [Swift Compiler Driver on GitHub](https://github.com/apple/swift-driver) _documentation_
- [Swift System on GitHub](https://github.com/apple/swift-system) _documentation_
- [Swift Collections on GitHub](https://github.com/apple/swift-collections) _documentation_
- [Swift Algorithms on GitHub](https://github.com/apple/swift-algorithms) _documentation_
- [Swift Package Index](https://swiftpackageindex.com/) _documentation_
- [Swift Mentorship Program](https://swift.org/mentorship/) _documentation_
- [Diversity in Swift](https://swift.org/diversity/) _documentation_
- [Swift Forums](https://forums.swift.org) _developerForum_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_
- [DocC](https://developer.apple.com/documentation/docc) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [Swift AWS Lambda Runtime on GitHub](https://github.com/swift-server/swift-aws-lambda-runtime/) _guide_
- [Swift Argument Parser on GitHub](https://github.com/apple/swift-argument-parser) _documentation_
- [Swift Evolution](https://apple.github.io/swift-evolution/) _guide_
- [Swift Numerics on GitHub](https://github.com/apple/swift-numerics) _documentation_

## Code Snippets

### Deque — [6:16]

```swift
import Collections

var colors: Deque = ["red", "yellow", "blue"]

colors.prepend("green")
colors.append("orange")
// `colors` is now ["green", "red", "yellow", "blue", “orange"]

colors.popFirst() // "green"
colors.popLast() // "orange"
// `colors` is back to ["red", "yellow", "blue"]
```

### Ordered set — [6:25]

```swift
import Collections

var buildingMaterials: OrderedSet = ["straw", "sticks", "bricks"]

for i in 0 ..< buildingMaterials.count {
    print("Little piggie #\(i) built a house of \(buildingMaterials[i])")
}
// Little piggie #0 built a house of straw
// Little piggie #1 built a house of sticks
// Little piggie #2 built a house of bricks

buildingMaterials.append("straw") // (inserted: false, index: 0)
```

### Ordered dictionary — [6:42]

```swift
import Collections

var responses: OrderedDictionary = [200: "OK", 403: "Forbidden", 404: "Not Found"]

for (code, phrase) in responses {
    print("\(code) (\(phrase))")
}
// 200 (OK)
// 403 (Forbidden)
// 404 (Not Found)
```

### Swift Algorithms — [7:39]

```swift
import Algorithms

let testAccounts = [ ... ]

for testGroup in testAccounts.uniquePermutations(ofCount: 0...) {
    try validate(testGroup)
}

let randomGroup = testAccounts.randomSample(count: 5)
```

### Swift System — [7:52]

```swift
import System

let fd: FileDescriptor = try .open(
    "/tmp/a.txt", .writeOnly,
    options: [.create, .truncate], permissions: .ownerReadWrite)
try fd.closeAfter {
    try fd.writeAll("Hello, WWDC!\n".utf8)
}
```

### FilePath manipulation APIs — [8:06]

```swift
import System

var path: FilePath = "/tmp/WWDC2021.txt"
print(path.lastComponent)         // "WWDC2021.txt"

print(path.extension)             // "txt"
path.extension = "pdf"            // path == "/tmp/WWDC2021.pdf"
path.extension = nil              // path == "/tmp/WWDC2021"
print(path.extension)             // nil

path.push("../foo/bar/./")        // path == "/tmp/wwdc2021/../foo/bar/."
path.lexicallyNormalize()         // path == "/tmp/foo/bar"
print(path.ends(with: "foo/bar")) // true!
```

### Float16 support on Apple silicon Macs — [9:01]

```swift
import Numerics

let x: Float16 = 1.5
let y = Float16.exp(x)
```

### Complex elementary functions — [9:05]

```swift
import Numerics

let z = Complex(0, Float16.pi) // πi
let w = Complex.exp(z)         // exp(πi) ≅ -1
```

### AWS Lambda runtime now with async/await — [11:07]

```swift
import AWSLambdaRuntime
import AWSLambdaEvents

@main
struct HelloWorld: LambdaHandler {
    typealias In = APIGatewayV2Request
    typealias Out = APIGatewayV2Response
    func handle(event: In, context: Lambda.Context) async throws -> Out {
        .init(statusCode: .ok, body: "Hello World")
    }
}
```

### Memory management — [14:52]

```swift
class Traveler {
    var destination: String
}

func test() {
    let traveler1 = Traveler(destination: "Unknown")
    // retain
    let traveler2 = traveler1
    // release
    traveler2.destination = "Big Sur"
    // release
    print("Done traveling")
}
```

### Codable synthesis for enums with associated values: A two-case enum — [17:04]

```swift
enum Command {
    case load(key: String)
    case store(key: String, value: Int)
}
```

### Codable synthesis for enums with associated values: Before — [17:11]

```swift
// You used to have to manually implement all of this boilerplate.

enum Command: Codable {
    case load(key: String)
    case store(key: String, value: Int)

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        if container.allKeys.count != 1 {
            let context = DecodingError.Context(
                codingPath: container.codingPath,
                debugDescription: "Invalid number of keys found, expected one.")
            throw DecodingError.typeMismatch(Command.self, context)
        }

        switch container.allKeys.first.unsafelyUnwrapped {
        case .load:
            let nested = try container.nestedContainer(
                keyedBy: LoadCodingKeys.self,
                forKey: .load)
            self = .load(
                key: try nested.decode(String.self, forKey: .key))
        case .store:
            let nested = try container.nestedContainer(
                keyedBy: StoreCodingKeys.self,
                forKey: .store)
            self = .store(
                key: try nested.decode(String.self, forKey: .key),
                value: try nested.decode(Int.self, forKey: .value))
        }
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        switch self {
        case let .load(key):
            var nested = container.nestedContainer(keyedBy: LoadCodingKeys.self, 
                                                   forKey: .load)
            try nested.encode(key, forKey: .key)
        case let .store(key, value):
            var nested = container.nestedContainer(keyedBy: StoreCodingKeys.self, 
                                                   forKey: .store)
            try nested.encode(key, forKey: .key)
            try nested.encode(value, forKey: .value)
        }
    }

    /// Contains keys for all cases of the enum.
    enum CodingKeys: CodingKey {
        case load
        case store
    }

    /// Contains keys for all associated values of `case load`.
    enum LoadCodingKeys: CodingKey {
        case key
    }

    /// Contains keys for all associated values of `case store`.
    enum StoreCodingKeys: CodingKey {
        case key
        case value
    }
}
```

### Codable synthesis for enums with associated values: After — [17:15]

```swift
enum Command: Codable {
    case load(key: String)
    case store(key: String, value: Int)
}
```

### Static member lookup — [17:26]

```swift
enum Coffee {
    case regular
    case decaf
}

func brew(_ coffee: Coffee) { ... }

brew(.regular)
```

### Flexible static member lookup — [17:49]

```swift
protocol Coffee { ... }
struct RegularCoffee: Coffee { }
struct Cappuccino: Coffee { }
extension Coffee where Self == Cappucino {
    static var cappucino: Cappucino { Cappucino() }
}

func brew<CoffeeType: Coffee>(_ coffee: CoffeeType) { ... }

brew(.cappucino.large)
```

### Property wrappers on parameters — [18:25]

```swift
@propertyWrapper
struct NonEmpty<Value: Collection> {
    init(wrappedValue: Value) {
        precondition(!wrappedValue.isEmpty)
        self.wrappedValue = wrappedValue
    }

    var wrappedValue: Value {
        willSet { precondition(!newValue.isEmpty) }
    }
}

func logIn(@NonEmpty _ username: String) {
    print("Logging in: \(username)")
}
```

### Ergonomic improvements in SwiftUI code: Before — [19:02]

```swift
// Instead of writing this...

import SwiftUI

struct SettingsView: View {
    @State var settings: [Setting]

    private let padding = 10.0

    var body: some View {
        List(0 ..< settings.count) { index in
            #if os(macOS)
            Toggle(settings[index].displayName, isOn: $settings[index].isOn)
                .toggleStyle(CheckboxToggleStyle())
            #else
            Toggle(settings[index].displayName, isOn: $settings[index].isOn)
                .toggleStyle(SwitchToggleStyle())
            #endif
        }
        .padding(CGFloat(padding))
    }
}
```

### Ergonomic improvements in SwiftUI code: After — [19:37]

```swift
// You can now write this.

import SwiftUI

struct SettingsView: View {
    @State var settings: [Setting]

    private let padding = 10.0

    var body: some View {
        List($settings) { $setting in
            Toggle(setting.displayName, isOn: $setting.isOn)
              #if os(macOS)
              .toggleStyle(.checkbox)
              #else
              .toggleStyle(.switch)
              #endif
        }
        .padding(padding)
    }
}
```

### Asynchronous programming with async/await: Before — [22:20]

```swift
// Instead of writing this...

func fetchImage(id: String, completion: (UIImage?, Error?) -> Void) {
    let request = self.imageURLRequest(for: id)
    let task = URLSession.shared.dataTask(with: request) {
        data, urlResponse, error in
        if let error = error {
            completion(nil, error)
        } else if let httpResponse = urlResponse as? HTTPURLResponse,
                httpResponse.statusCode != 200 {
            completion(nil, MyTransferError())
        } else if let data = data, let image = UIImage(data: data) {
            completion(image, nil)
        } else {
            completion(nil, MyOtherError())
        }
    }
   task.resume()
}
```

### Asynchronous programming with async/await: URLSession.shared.data(for:) — [23:58]

```swift
let (data, response) = try await URLSession.shared.data(for: request)
```

### Asynchronous programming with async/await: After — [24:40]

```swift
// You can now write this.

func fetchImage(id: String) async throws -> UIImage {
    let request = self.imageURLRequest(for: id)
    let (data, response) = try await URLSession.shared.data(for: request)
    if let httpResponse = response as? HTTPURLResponse,
       httpResponse.statusCode != 200 {
        throw TransferFailure()
    }
    guard let image = UIImage(data: data) else {
        throw ImageDecodingFailure()
    }
    return image
}
```

### Structured concurrency — [27:06]

```swift
func titleImage() async throws -> Image {
    async let background = renderBackground()
    async let foreground = renderForeground()
    let title = try renderTitle()
    return try await merge(background,
                           foreground,
                           title)
}
```

### Actors — [29:26]

```swift
actor Statistics {
    private var counter: Int = 0
    func increment() {
        counter += 1
    }
    func publish() async {
        await sendResults(counter)
    }
}

var statistics = Statistics()
await statistics.increment()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10192/4/1EE1B691-9DDB-4920-BD8C-7E91BDD75BB8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10192/4/1EE1B691-9DDB-4920-BD8C-7E91BDD75BB8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10192) — developer.apple.com. Indexed for agent consumption._
