---
id: "wwdc2022-110360"
event: "wwdc2022"
year: 2022
title: "Use Xcode for server-side development"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110360"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Use Xcode for server-side development

**Event:** WWDC22 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110360](https://developer.apple.com/videos/play/wwdc2022/110360)

Discover how you can create, build, and deploy a Swift server app alongside your pre-existing Xcode projects within the same workspace. We'll show you how to create your own local app and test endpoints using Xcode, and explore how you can structure and share code between server and client apps to ease your development process

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,533 words)

## Documentation & Resources

- [Swift on Server](https://www.swift.org/server/) _guide_

## Code Snippets

### Simple, server package manifest — [1:36]

```swift
// swift-tools-version: 5.7

import PackageDescription

let package = Package(
    name: "MyServer",
    platforms: [.macOS("12.0")],
    products: [
        .executable(
            name: "MyServer",
            targets: ["MyServer"]),
    ],
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", .upToNextMajor(from: "4.0.0")),
    ],
    targets: [
        .executableTarget(
            name: "MyServer",
            dependencies: [
                .product(name: "Vapor", package: "vapor")
            ]),
        .testTarget(
            name: "MyServerTests",
            dependencies: ["MyServer"]),
    ]
)
```

### Simple, server code — [2:00]

```swift
import Vapor

@main
public struct MyServer {
    public static func main() async throws {
        let webapp = Application()
        webapp.get("greet", use: Self.greet)
        webapp.post("echo", use: Self.echo)
        try webapp.run()
    }

    static func greet(request: Request) async throws -> String {
        return "Hello from Swift Server"
    }

    static func echo(request: Request) async throws -> String {
        if let body = request.body.string {
            return body
        }
        return ""
    }
}
```

### Using curl to test the local server — [3:42]

```bash
curl http://127.0.0.1:8080/greet; echo
curl http://127.0.0.1:8080/echo --data "Hello from WWDC 2022"; echo
```

### Simple, iOS app server abstraction — [4:10]

```swift
import Foundation

struct MyServerClient {
    let baseURL = URL(string: "http://127.0.0.1:8080")!

    func greet() async throws -> String {
        let url = baseURL.appendingPathComponent("greet")
        let (data, _) = try await URLSession.shared.data(for: URLRequest(url: url))
        guard let responseBody = String(data: data, encoding: .utf8) else {
            throw Errors.invalidResponseEncoding
        }
        return responseBody
    }

    enum Errors: Error {
        case invalidResponseEncoding
    }
}
```

### Simple, iOS app server call SwiftUI integration — [5:00]

```swift
import SwiftUI

struct ContentView: View {
    @State var serverGreeting = ""
    var body: some View {
        Text(serverGreeting)
            .padding()
            .task {
                do {
                    let myServerClient = MyServerClient()
                    self.serverGreeting = try await myServerClient.greet()
                } catch {
                    self.serverGreeting = String(describing: error)
                }
            }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

### Food truck, basic server — [9:51]

```swift
import Foundation
import Vapor

@main
struct FoodTruckServerBootstrap {
    public static func main() async throws {
        // initialize the server
        let foodTruckServer = FoodTruckServer()
        // initialize the web framework and configure the http routes
        let webapp = Application()
        webapp.get("donuts", use: foodTruckServer.listDonuts)
        try webapp.run()
    }
}

struct FoodTruckServer {
    private let storage = Storage()

    func listDonuts(request: Request) async -> Response.Donuts {
        let donuts = self.storage.listDonuts()
        return Response.Donuts(donuts: donuts)
    }

    enum Response {
        struct Donuts: Content {
            var donuts: [Model.Donut]
        }
    }
}

struct Storage {
    var donuts = [Model.Donut]()

    func listDonuts() -> [Model.Donut] {
        return self.donuts
    }
}

enum Model {
    struct Donut: Codable {
        var id: Int
        var name: String
        var date: Date
        var dough: Dough
        var glaze: Glaze?
        var topping: Topping?
    }

    struct Dough: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    struct Glaze: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    struct Topping: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    public struct FlavorProfile: Codable {
        var salty: Int?
        var sweet: Int?
        var bitter: Int?
        var sour: Int?
        var savory: Int?
        var spicy: Int?
    }
}
```

### Food truck, server donuts menu — [12:18]

```json
[
  {
      "id": 0,
      "name": "Deep Space",
      "date": "2022-04-20T00:00:00Z",
      "dough": {
          "name": "Space Strawberry",
          "description": "The Space Strawberry plant grows its fruit as ready-to-pick donut dough.",
          "flavors": {
              "sweet": 3,
              "savory": 2
          }
      },
      "glaze": {
          "name": "Delta Quadrant Slice",
          "description": "Locally sourced, wormhole-to-table slice of the delta quadrant of the galaxy. Now with less hydrogen!",
          "flavors": {
              "salty": 1,
              "sour": 3,
              "spicy": 1
          }
      },
      "topping": {
          "name": "Rainbow Sprinkles",
          "description": "Cultivated from the many naturally occurring rainbows on various ocean planets.",
          "flavors": {
              "salty": 2,
              "sweet": 2,
              "sour": 1
          }
      }
  },
  {
      "id": 1,
      "name": "Chocolate II",
      "date": "2022-04-20T00:00:00Z",
      "dough": {
          "name": "Chocolate II",
          "description": "When Harold Chocolate II discovered this substance in 3028, it finally unlocked the ability of interstellar travel.",
          "flavors": {
              "salty": 1,
              "sweet": 3,
              "bitter": 1,
              "sour": -1,
              "savory": 1
          }
      },
      "glaze": {
          "name": "Chocolate II",
          "description": "A thin layer of melted Chocolate II, flash frozen to fit the standard Space Donut shape. Also useful for cleaning starship engines.",
          "flavors": {
              "salty": 1,
              "sweet": 2,
              "bitter": 1,
              "sour": -1,
              "savory": 2
          }
      },
      "topping": {
          "name": "Chocolate II",
          "description": "Particles of Chocolate II moulded into a sprinkle fashion. Do not feed to space whales.",
          "flavors": {
              "salty": 1,
              "sweet": 2,
              "bitter": 1,
              "sour": -1,
              "savory": 2
          }
      }
  },
  {
      "id": 2,
      "name": "Coffee Caramel",
      "date": "2022-04-20T00:00:00Z",
      "dough": {
          "name": "Hardened Coffee",
          "description": "Unlike other donut sellers, our coffee dough is simply a lot of coffee compressed into an ultra dense torus.",
          "flavors": {
              "sweet": -2,
              "bitter": 4,
              "sour": 2,
              "spicy": 1
          }
      },
      "glaze": {
          "name": "Caramel",
          "description": "Some good old fashioned Earth caramel.",
          "flavors": {
              "salty": 2,
              "sweet": 3,
              "sour": -1,
              "savory": 1
          }
      },
      "topping": {
          "name": "Nebula Bits",
          "description": "Scooped up by starships traveling through a sugar nebula.",
          "flavors": {
              "sweet": 4,
              "spicy": 1
          }
      }
  }
]
```

### Food truck, server package manifest — [12:23]

```swift
// swift-tools-version: 5.7

import PackageDescription

let package = Package(
    name: "FoodTruckServer",
    platforms: [.macOS("12.0")],
    products: [
        .executable(
            name: "FoodTruckServer",
            targets: ["FoodTruckServer"]),
    ],
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", .upToNextMajor(from: "4.0.0")),
    ],
    targets: [
        .executableTarget(
            name: "FoodTruckServer",
            dependencies: [
                .product(name: "Vapor", package: "vapor")
            ],
            resources: [
                .copy("menu.json")
            ]
        ),
        .testTarget(
            name: "FoodTruckServerTests",
            dependencies: ["FoodTruckServer"]),
    ]
)
```

### Food truck, server with integrated storage — [12:30]

```swift
import Foundation
import Vapor

@main
struct FoodTruckServerBootstrap {
    public static func main() async throws {
        // initialize the server
        let foodTruckServer = FoodTruckServer()
        try await foodTruckServer.bootstrap()
        // initialize the web framework and configure the http routes
        let webapp = Application()
        webapp.get("donuts", use: foodTruckServer.listDonuts)
        try webapp.run()
    }
}

struct FoodTruckServer {
    private let storage = Storage()

    func bootstrap() async throws {
        try await self.storage.load()
    }

    func listDonuts(request: Request) async -> Response.Donuts {
        let donuts = await self.storage.listDonuts()
        return Response.Donuts(donuts: donuts)
    }

    enum Response {
        struct Donuts: Content {
            var donuts: [Model.Donut]
        }
    }
}

actor Storage {
    let jsonDecoder: JSONDecoder
    var donuts = [Model.Donut]()

    init() {
        self.jsonDecoder = JSONDecoder()
        self.jsonDecoder.dateDecodingStrategy = .iso8601
    }

    func load() throws {
        guard let path = Bundle.module.path(forResource: "menu", ofType: "json") else {
            throw Errors.menuFileNotFound
        }
        guard let data = FileManager.default.contents(atPath: path) else {
            throw Errors.failedLoadingMenu
        }

        self.donuts = try self.jsonDecoder.decode([Model.Donut].self, from: data)
    }

    func listDonuts() -> [Model.Donut] {
        return self.donuts
    }

    enum Errors: Error {
        case menuFileNotFound
        case failedLoadingMenu
    }
}

enum Model {
    struct Donut: Codable {
        var id: Int
        var name: String
        var date: Date
        var dough: Dough
        var glaze: Glaze?
        var topping: Topping?
    }

    struct Dough: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    struct Glaze: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    struct Topping: Codable {
        var name: String
        var description: String
        var flavors: FlavorProfile
    }

    public struct FlavorProfile: Codable {
        var salty: Int?
        var sweet: Int?
        var bitter: Int?
        var sour: Int?
        var savory: Int?
        var spicy: Int?
    }
}
```

### Using curl and jq to test the local server — [14:42]

```bash
curl http://127.0.0.1:8080/donuts | jq .
curl http://127.0.0.1:8080/donuts | jq '.donuts[] .name'
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110360/3/95EF8495-F291-49FD-8958-276AC76C222D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110360/3/95EF8495-F291-49FD-8958-276AC76C222D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110360) — developer.apple.com. Indexed for agent consumption._