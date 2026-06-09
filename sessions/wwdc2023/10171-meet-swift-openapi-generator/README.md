---
id: "wwdc2023-10171"
event: "wwdc2023"
year: 2023
title: "Meet Swift OpenAPI Generator"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10171"
topics: ["Developer Tools", "Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet Swift OpenAPI Generator

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-09 · **Session:** [wwdc2023-10171](https://developer.apple.com/videos/play/wwdc2023/10171)

Discover how Swift OpenAPI Generator can help you work with HTTP server APIs whether you’re extending an iOS app or writing a server in Swift. We’ll show you how this package plugin can streamline your workflow and simplify your codebase by generating code from an OpenAPI document.

**Keywords:** `🐱`, `😸`, `😹`, `😺`, `😻`, `😼`, `😽`, `😾`, `😿`, `🙀`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,135 words)

## Documentation & Resources

- [URLSession Transport for Swift OpenAPI Generator](https://github.com/apple/swift-openapi-urlsession) _guide_
- [Swift OpenAPI Generator Runtime](http://github.com/apple/swift-openapi-runtime) _guide_
- [Swift OpenAPI Generator package plugin](https://github.com/apple/swift-openapi-generator) _guide_

## Code Snippets

### Example OpenAPI document — [4:17]

```yaml
openapi: "3.0.3"
info:
  title: "GreetingService"
  version: "1.0.0"
servers:
- url: "http://localhost:8080/api"
  description: "Production"
paths:
  /greet:
    get:
      operationId: "getGreeting"
      parameters:
      - name: "name"
        required: false
        in: "query"
        description: "Personalizes the greeting."
        schema:
          type: "string"
      responses:
        "200":
          description: "Returns a greeting"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Greeting"
```

### CatService openapi.yaml — [7:05]

```yaml
openapi: "3.0.3"
info:
  title: CatService
  version: 1.0.0
servers:
  - url: http://localhost:8080/api
    description: "Localhost cats 🙀"
paths:
  /emoji:
    get:
      operationId: getEmoji
      parameters:
      - name: count
        required: false
        in: query
        description: "The number of cats to return. 😽😽😽"
        schema:
          type: integer
      responses:
        '200':
          description: "Returns a random emoji, of a cat, ofc! 😻"
          content:
            text/plain:
              schema:
                type: string
```

### Making API calls from your app — [8:03]

```swift
import SwiftUI
import OpenAPIRuntime
import OpenAPIURLSession

#Preview {
    ContentView()
}

struct ContentView: View {
    @State private var emoji = "🫥"

    var body: some View {
        VStack {
            Text(emoji).font(.system(size: 100))
            Button("Get cat!") {
                Task { try? await updateEmoji() }
            }
        }
        .padding()
        .buttonStyle(.borderedProminent)
    }

    let client: Client

    init() {
        self.client = Client(
            serverURL: try! Servers.server1(),
            transport: URLSessionTransport()
        )
    }

    func updateEmoji() async throws {
        let response = try await client.getEmoji(Operations.getEmoji.Input())

        switch response {
        case let .ok(okResponse):
            switch okResponse.body {
            case .text(let text):
                emoji = text
            }
        case .undocumented(statusCode: let statusCode, _):
            print("cat-astrophe: \(statusCode)")
            emoji = "🙉"
        }
    }
}
```

### CatServiceClient openapi-generator-config.yaml — [9:48]

```yaml
generate:
  - types
  - client
```

### Adapting as the API evolves — [13:24]

```swift
import SwiftUI
import OpenAPIRuntime
import OpenAPIURLSession

#Preview {
    ContentView()
}

struct ContentView: View {
    @State private var emoji = "🫥"

    var body: some View {
        VStack {
            Text(emoji).font(.system(size: 100))
            Button("Get cat!") {
                Task { try? await updateEmoji() }
            }
            Button("More cats!") {
                Task { try? await updateEmoji(count: 3) }
            }
        }
        .padding()
        .buttonStyle(.borderedProminent)
    }

    let client: Client

    init() {
        self.client = Client(
            serverURL: try! Servers.server1(),
            transport: URLSessionTransport()
        )
    }

    func updateEmoji(count: Int = 1) async throws {
        let response = try await client.getEmoji(Operations.getEmoji.Input(
            query: Operations.getEmoji.Input.Query(count: count)
        ))

        switch response {
        case let .ok(okResponse):
            switch okResponse.body {
            case .text(let text):
                emoji = text
            }
        case .undocumented(statusCode: let statusCode, _):
            print("cat-astrophe: \(statusCode)")
            emoji = "🙉"
        }
    }
}
```

### Testing your app with mocks — [15:06]

```swift
import SwiftUI
import OpenAPIRuntime
import OpenAPIURLSession

#Preview {
    ContentView(client: MockClient())
}

struct ContentView<C: APIProtocol>: View {
    @State private var emoji = "🫥"

    var body: some View {
        VStack {
            Text(emoji).font(.system(size: 100))
            Button("Get cat!") {
                Task { try? await updateEmoji() }
            }
            Button("More cats!") {
                Task { try? await updateEmoji(count: 3) }
            }
        }
        .padding()
        .buttonStyle(.borderedProminent)
    }

    let client: C

    init(client: C) {
        self.client = client
    }

    init() where C == Client {
        self.client = Client(
            serverURL: try! Servers.server1(),
            transport: URLSessionTransport()
        )
    }

    func updateEmoji(count: Int = 1) async throws {
        let response = try await client.getEmoji(Operations.getEmoji.Input(
            query: Operations.getEmoji.Input.Query(count: count)
        ))

        switch response {
        case let .ok(okResponse):
            switch okResponse.body {
            case .text(let text):
                emoji = text
            }
        case .undocumented(statusCode: let statusCode, _):
            print("cat-astrophe: \(statusCode)")
            emoji = "🙉"
        }
    }
}

struct MockClient: APIProtocol {
    func getEmoji(_ input: Operations.getEmoji.Input) async throws -> Operations.getEmoji.Output {
        let count = input.query.count ?? 1
        let emojis = String(repeating: "🤖", count: count)
        return .ok(Operations.getEmoji.Output.Ok(
            body: .text(emojis)
        ))
    }
}
```

### Implementing a backend server — [16:58]

```swift
import Foundation
import OpenAPIRuntime
import OpenAPIVapor
import Vapor

struct Handler: APIProtocol {
    func getEmoji(_ input: Operations.getEmoji.Input) async throws -> Operations.getEmoji.Output {
        let candidates = "🐱😹😻🙀😿😽😸😺😾😼"
        let chosen = String(candidates.randomElement()!)
        let count = input.query.count ?? 1
        let emojis = String(repeating: chosen, count: count)
        return .ok(Operations.getEmoji.Output.Ok(body: .text(emojis)))
    }
}

@main
struct CatService {
    public static func main() throws {
        let app = Vapor.Application()
        let transport = VaporTransport(routesBuilder: app)
        let handler = Handler()
        try handler.registerHandlers(on: transport, serverURL: Servers.server1())
        try app.run()
    }
}
```

### CatService Package.swift — [18:43]

```swift
// swift-tools-version: 5.8
import PackageDescription

let package = Package(
    name: "CatService",
    platforms: [
        .macOS(.v13),
    ],
    dependencies: [
        .package(
             url: "https://github.com/apple/swift-openapi-generator",
            .upToNextMinor(from: "0.1.0")
        ),
        .package(
            url: "https://github.com/apple/swift-openapi-runtime",
            .upToNextMinor(from: "0.1.0")
        ),
        .package(
            url: "https://github.com/swift-server/swift-openapi-vapor",
            .upToNextMinor(from: "0.1.0")
        ),
        .package(
            url: "https://github.com/vapor/vapor",
            .upToNextMajor(from: "4.69.2")
        ),
    ],
    targets: [
        .executableTarget(
            name: "CatService",
            dependencies: [
                .product(name: "OpenAPIRuntime", package: "swift-openapi-runtime"),
                .product(name: "OpenAPIVapor", package: "swift-openapi-vapor"),
                .product(name: "Vapor", package: "vapor"),
            ],
            resources: [
                .process("Resources/cat.mp4"),
            ],
            plugins: [
                .plugin(name: "OpenAPIGenerator", package: "swift-openapi-generator"),
            ]
        ),
    ]
)
```

### CatService openapi.yaml — [19:08]

```yaml
openapi: "3.0.3"
info:
  title: CatService
  version: 1.0.0
servers:
  - url: http://localhost:8080/api
    description: "Localhost cats 🙀"
paths:
  /emoji:
    get:
      operationId: getEmoji
      parameters:
      - name: count
        required: false
        in: query
        description: "The number of cats to return. 😽😽😽"
        schema:
          type: integer
      responses:
        '200':
          description: "Returns a random emoji, of a cat, ofc! 😻"
          content:
            text/plain:
              schema:
                type: string
```

### CatService openapi-generator-config.yaml — [19:10]

```yaml
generate:
  - types
  - server
```

### Adding an operation to the OpenAPI document — [20:11]

```yaml
openapi: "3.0.3"
info:
  title: CatService
  version: 1.0.0
servers:
  - url: http://localhost:8080/api
    description: "Localhost cats 🙀"
paths:
  /emoji:
    get:
      operationId: getEmoji
      parameters:
      - name: count
        required: false
        in: query
        description: "The number of cats to return. 😽😽😽"
        schema:
          type: integer
      responses:
        '200':
          description: "Returns a random emoji, of a cat, ofc! 😻"
          content:
            text/plain:
              schema:
                type: string

  /clip:
    get:
      operationId: getClip
      responses:
        '200':
          description: "Returns a cat video! 😽"
          content:
            video/mp4:
              schema:
                type: string
                format: binary
```

### Adding a new API operation — [20:26]

```swift
import Foundation
import OpenAPIRuntime
import OpenAPIVapor
import Vapor

struct Handler: APIProtocol {
    func getClip(_ input: Operations.getClip.Input) async throws -> Operations.getClip.Output {
        let clipResourceURL = Bundle.module.url(forResource: "cat", withExtension: "mp4")!
        let clipData = try Data(contentsOf: clipResourceURL)
        return .ok(Operations.getClip.Output.Ok(body: .binary(clipData)))
    }

    func getEmoji(_ input: Operations.getEmoji.Input) async throws -> Operations.getEmoji.Output {
        let candidates = "🐱😹😻🙀😿😽😸😺😾😼"
        let chosen = String(candidates.randomElement()!)
        let count = input.query.count ?? 1
        let emojis = String(repeating: chosen, count: count)
        return .ok(Operations.getEmoji.Output.Ok(body: .text(emojis)))
    }
}

@main
struct CatService {
    public static func main() throws {
        let app = Vapor.Application()
        let transport = VaporTransport(routesBuilder: app)
        let handler = Handler()
        try handler.registerHandlers(on: transport, serverURL: Servers.server1())
        try app.run()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10171/6/B3B8830B-E039-4E13-B13E-989D45016244/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10171/6/B3B8830B-E039-4E13-B13E-989D45016244/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10171) — developer.apple.com. Indexed for agent consumption._
