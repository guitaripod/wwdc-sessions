---
id: "wwdc2024-10216"
event: "wwdc2024"
year: 2024
title: "Explore the Swift on Server ecosystem"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10216"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Explore the Swift on Server ecosystem

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10216](https://developer.apple.com/videos/play/wwdc2024/10216)

Swift is a great language for writing your server applications, and powers critical services across Apple’s cloud products. We’ll explore tooling, delve into the Swift server package ecosystem, and demonstrate how to interact with databases and add observability to applications.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,459 words)

## Documentation & Resources

- [Swift Server Workgroup](https://www.swift.org/sswg/) _documentation_
- [Swift Package Ecosystem](https://www.swift.org/packages/) _documentation_
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010
- [Swift on Server](https://www.swift.org/server/) _guide_

## Code Snippets

### EventService Package.swift — [3:23]

```swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
  name: "EventService",
  platforms: [.macOS(.v14)],
  dependencies: [
    .package(
      url: "https://github.com/apple/swift-openapi-generator",
      from: "1.2.1"
    ),
    .package(
      url: "https://github.com/apple/swift-openapi-runtime",
      from: "1.4.0"
    ),
    .package(
      url: "https://github.com/vapor/vapor",
      from: "4.99.2"
    ),
    .package(
      url: "https://github.com/swift-server/swift-openapi-vapor",
      from: "1.0.1"
    ),
  ],
  targets: [
    .target(
      name: "EventAPI",
      dependencies: [
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
      ],
      plugins: [
        .plugin(
          name: "OpenAPIGenerator",
          package: "swift-openapi-generator"
        )
      ]
    ),
    .executableTarget(
      name: "EventService",
      dependencies: [
        "EventAPI",
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
        .product(
          name: "OpenAPIVapor",
          package: "swift-openapi-vapor"
        ),
        .product(
          name: "Vapor",
          package: "vapor"
        ),
      ]
    ),
  ]
)
```

### EventService openapi.yaml — [4:05]

```yaml
openapi: "3.1.0"
info:
  title: "EventService"
  version: "1.0.0"
servers:
  - url: "https://localhost:8080/api"
    description: "Example service deployment."
paths:
  /events:
    get:
      operationId: "listEvents"
      responses:
        "200":
          description: "A success response with all events."
          content:
            application/json:
              schema:
                type: "array"
                items:
                  $ref: "#/components/schemas/Event"
    post:
      operationId: "createEvent"
      requestBody:
        description: "The event to create."
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Event'
      responses:
        '201':
          description: "A success indicating the event was created."
        '400':
          description: "A failure indicating the event wasn't created."
components:
  schemas:
    Event:
      type: "object"
      description: "An event."
      properties:
        name:
          type: "string"
          description: "The event's name."
        date:
          type: "string"
          format: "date"
          description: "The day of the event."
        attendee:
          type: "string"
          description: "The name of the person attending the event."
      required:
        - "name"
        - "date"
        - "attendee"
```

### EventService initial implementation — [4:35]

```swift
import OpenAPIRuntime
import OpenAPIVapor
import Vapor
import EventAPI

@main
struct Service {
  static func main() async throws {
    let application = try await Vapor.Application.make()
    let transport = VaporTransport(routesBuilder: application)

    let service = Service()
    try service.registerHandlers(
      on: transport,
      serverURL: URL(string: "/api")!
    )

    try await application.execute()
  }
}

extension Service: APIProtocol {
  func listEvents(
    _ input: Operations.listEvents.Input
  ) async throws -> Operations.listEvents.Output {
    let events: [Components.Schemas.Event] = [
      .init(name: "Server-Side Swift Conference", date: "26.09.2024", attendee: "Gus"),
      .init(name: "Oktoberfest", date: "21.09.2024", attendee: "Werner"),
    ]

    return .ok(.init(body: .json(events)))
  }

  func createEvent(
    _ input: Operations.createEvent.Input
  ) async throws -> Operations.createEvent.Output {
    return .undocumented(statusCode: 501, .init())
  }
}
```

### EventService Package.swift — [6:56]

```swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
  name: "EventService",
  platforms: [.macOS(.v14)],
  dependencies: [
    .package(
      url: "https://github.com/apple/swift-openapi-generator",
      from: "1.2.1"
    ),
    .package(
      url: "https://github.com/apple/swift-openapi-runtime",
      from: "1.4.0"
    ),
    .package(
      url: "https://github.com/vapor/vapor",
      from: "4.99.2"
    ),
    .package(
      url: "https://github.com/swift-server/swift-openapi-vapor",
      from: "1.0.1"
    ),
    .package(
      url: "https://github.com/vapor/postgres-nio",
      from: "1.19.1"
    ),
  ],
  targets: [
    .target(
      name: "EventAPI",
      dependencies: [
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
      ],
      plugins: [
        .plugin(
          name: "OpenAPIGenerator",
          package: "swift-openapi-generator"
        )
      ]
    ),
    .executableTarget(
      name: "EventService",
      dependencies: [
        "EventAPI",
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
        .product(
          name: "OpenAPIVapor",
          package: "swift-openapi-vapor"
        ),
        .product(
          name: "Vapor",
          package: "vapor"
        ),
        .product(
            name: "PostgresNIO",
          package: "postgres-nio"
        ),
      ]
    ),
  ]
)
```

### Implementing the listEvents method — [7:08]

```swift
import OpenAPIRuntime
import OpenAPIVapor
import Vapor
import EventAPI
import PostgresNIO

@main
struct Service {
  let postgresClient: PostgresClient

  static func main() async throws {
    let application = try await Vapor.Application.make()
    let transport = VaporTransport(routesBuilder: application)

    let postgresClient = PostgresClient(
      configuration: .init(
        host: "localhost",
        username: "postgres",
        password: nil,
        database: nil,
        tls: .disable
      )
    )
    let service = Service(postgresClient: postgresClient)
    try service.registerHandlers(
      on: transport,
      serverURL: URL(string: "/api")!
    )

    try await withThrowingDiscardingTaskGroup { group in
      group.addTask {
        await postgresClient.run()
      }

      group.addTask {
        try await application.execute()
      }
    }
  }
}

extension Service: APIProtocol {
  func listEvents(
    _ input: Operations.listEvents.Input
  ) async throws -> Operations.listEvents.Output {
    let rows = try await self.postgresClient.query("SELECT name, date, attendee FROM events")

    var events = [Components.Schemas.Event]()
    for try await (name, date, attendee) in rows.decode((String, String, String).self) {
      events.append(.init(name: name, date: date, attendee: attendee))
    }

    return .ok(.init(body: .json(events)))
  }

  func createEvent(
    _ input: Operations.createEvent.Input
  ) async throws -> Operations.createEvent.Output {
    return .undocumented(statusCode: 501, .init())
  }
}
```

### Implementing the createEvent method — [9:02]

```swift
func createEvent(
  _ input: Operations.createEvent.Input
) async throws -> Operations.createEvent.Output {
  switch input.body {
  case .json(let event):
    try await self.postgresClient.query(
      """
      INSERT INTO events (name, date, attendee)
      VALUES (\(event.name), \(event.date), \(event.attendee))
      """
    )
    return .created(.init())
  }
}
```

### Instrumenting the listEvents method — [11:34]

```swift
func listEvents(
  _ input: Operations.listEvents.Input
) async throws -> Operations.listEvents.Output {
  let logger = Logger(label: "ListEvents")
  logger.info("Handling request", metadata: ["operation": "\(Operations.listEvents.id)"])

  Counter(label: "list.events.counter").increment()

  return try await withSpan("database query") { span in
    let rows = try await postgresClient.query("SELECT name, date, attendee FROM events")
    return try await .ok(.init(body: .json(decodeEvents(rows))))
  }
}
```

### EventService Package.swift — [13:14]

```swift
// swift-tools-version:5.9
import PackageDescription

let package = Package(
  name: "EventService",
  platforms: [.macOS(.v14)],
  dependencies: [
    .package(
      url: "https://github.com/apple/swift-openapi-generator",
      from: "1.2.1"
    ),
    .package(
      url: "https://github.com/apple/swift-openapi-runtime",
      from: "1.4.0"
    ),
    .package(
      url: "https://github.com/vapor/vapor",
      from: "4.99.2"
    ),
    .package(
      url: "https://github.com/swift-server/swift-openapi-vapor",
      from: "1.0.1"
    ),
    .package(
      url: "https://github.com/vapor/postgres-nio",
      from: "1.19.1"
    ),
    .package(
        url: "https://github.com/apple/swift-log",
        from: "1.5.4"
    ),
  ],
  targets: [
    .target(
      name: "EventAPI",
      dependencies: [
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
      ],
      plugins: [
        .plugin(
          name: "OpenAPIGenerator",
          package: "swift-openapi-generator"
        )
      ]
    ),
    .executableTarget(
      name: "EventService",
      dependencies: [
        "EventAPI",
        .product(
          name: "OpenAPIRuntime",
          package: "swift-openapi-runtime"
        ),
        .product(
          name: "OpenAPIVapor",
          package: "swift-openapi-vapor"
        ),
        .product(
          name: "Vapor",
          package: "vapor"
        ),
        .product(
            name: "PostgresNIO",
          package: "postgres-nio"
        ),
        .product(
            name: "Logging",
            package: "swift-log"
        ),
      ]
    ),
  ]
)
```

### Adding logging to the createEvent method — [13:38]

```swift
func createEvent(
  _ input: Operations.createEvent.Input
) async throws -> Operations.createEvent.Output {
  switch input.body {
  case .json(let event):
    do {
      try await self.postgresClient.query(
        """
        INSERT INTO events (name, date, attendee)
        VALUES (\(event.name), \(event.date), \(event.attendee))
        """
      )
      return .created(.init())
    } catch let error as PSQLError {
      let logger = Logger(label: "CreateEvent")

      if let message = error.serverInfo?[.message] {
        logger.info(
          "Failed to create event",
          metadata: ["error.message": "\(message)"]
        )
      }

      return .badRequest(.init())
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10216/4/DB423F7B-5B55-47AE-958F-68C8BF6077A6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10216/4/DB423F7B-5B55-47AE-958F-68C8BF6077A6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10216) — developer.apple.com. Indexed for agent consumption._