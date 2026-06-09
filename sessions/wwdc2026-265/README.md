# Build real-time apps and services with gRPC and Swift

**Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-265](https://developer.apple.com/videos/play/wwdc2026/265)

Build engaging live experiences with gRPC in your Swift app and backend. gRPC is an open-source RPC framework designed for high-performance, bidirectional streaming APIs. Explore how the gRPC Swift package provides a modern, safe runtime built with Swift concurrency. Learn how integrated tools streamline your workflow and help you deliver real-time features with ease.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [About gRPC](https://grpc.io/) _documentation_
- [gRPC Swift Extras](https://github.com/grpc/grpc-swift-extras) _guide_
- [gRPC Swift Protobuf](https://github.com/grpc/grpc-swift-protobuf) _guide_
- [gRPC Swift NIO Transport](https://github.com/grpc/grpc-swift-nio-transport) _guide_
- [gRPC Swift](https://github.com/grpc/grpc-swift) _guide_
- [Swift on Server](https://www.swift.org/server/) _guide_

## Code Snippets

### ListRaces RPC definition — [3:38]

```bash
edition = "2024";

import "google/protobuf/timestamp.proto";

service SwiftKartService {
  rpc ListRaces(ListRacesRequest) returns (ListRacesResponse);
}

message ListRacesRequest {
  int32 limit = 1 [default = 100];
}

message ListRacesResponse {
  repeated Race races = 1;
}

message Race {
  string name = 1;
  string location = 2;
  google.protobuf.Timestamp start_time = 3;
  int32 laps = 4;
  string championship = 5;
}
```

### grpc-swift-proto-generator-config.json — [5:55]

```json
{
    "generate": {
        "clients": true,
        "servers": false,
        "messages": true
    }
}
```

### Add gRPC imports — [6:24]

```swift
import GRPCCore
import GRPCNIOTransportHTTP2
import SwiftProtobuf
```

### Create a gRPC client connected to a local server — [6:38]

```swift
.task {
    do {
        try await withGRPCClient(
            transport: .http2NIOTS(
                address: .ipv4(host: "127.0.0.1", port: 8080),
                transportSecurity: .tls
            )
        ) { client in
            <#code#>
        }
    } catch {
        print("gRPC error: \(error)")
    }
}
```

### Call the ListRaces RPC and update the view — [7:14]

```swift
.task {
    do {
        try await withGRPCClient(
            transport: .http2NIOTS(
                address: .ipv4(host: "127.0.0.1", port: 8080),
                transportSecurity: .tls
            )
        ) { client in
            let kart = SwiftKartService.Client(wrapping: client)
            let request = ListRacesRequest()
            let response = try await kart.listRaces(request)
            self.races = response.races.map { race in
                RaceInfo(
                    name: race.name,
                    location: race.location,
                    startTime: race.startTime.date,
                    championship: race.championship,
                    laps: Int(race.laps),
                    drivers: race.drivers
                )
            }
        }
    } catch {
        print("gRPC error: \(error)")
    }
}
```

### ClientManager.swift — [8:30]

```swift
import GRPCCore
import GRPCNIOTransportHTTP2
import Synchronization
import SwiftUI

@Observable
final class ClientManager: Sendable {
    fileprivate let state = Mutex(State.disconnected)

    static func makeTransport() throws -> HTTP2ClientTransport.TransportServices {
        try .http2NIOTS(
            target: .ipv4(address: "127.0.0.1", port: 8080),
            transportSecurity: .plaintext
        )
    }

    func withClient(
        body: (_ client: GRPCClient<HTTP2ClientTransport.TransportServices>) async throws -> Void
    ) async throws {
        let client = try connectIfNecessary()
        try await body(client)
    }

    private func connectIfNecessary() throws -> GRPCClient<HTTP2ClientTransport.TransportServices> {
        try self.state.withLock { state in
            try state.connectIfNecessary()
        }
    }

    func disconnect() {
        let client = self.state.withLock { state in
            state.disconnect()
        }

        client?.beginGracefulShutdown()
    }
}

extension ClientManager {
    enum State {
        case connected(GRPCClient<HTTP2ClientTransport.TransportServices>, Task<Void, any Error>)
        case disconnected
    }
}

extension ClientManager.State {
    mutating func connectIfNecessary() throws -> GRPCClient<HTTP2ClientTransport.TransportServices> {
        switch self {
        case .connected(let client, _):
            return client

        case .disconnected:
            let client = try GRPCClient(transport: ClientManager.makeTransport())
            let task = Task { try await client.runConnections() }
            self = .connected(client, task)
            return client
        }
    }

    mutating func disconnect() -> GRPCClient<HTTP2ClientTransport.TransportServices>? {
        switch self {
        case .connected(let client, _):
            self = .disconnected
            return client
        case .disconnected:
            return nil
        }
    }
}
```

### Propagate ClientManager to child views — [8:39]

```swift
import SwiftUI

@main
struct SwiftKartApp: App {
    let manager = ClientManager()

    var body: some Scene {
        WindowGroup {
            RaceScheduleView()
                .environment(manager)
        }
    }
}
```

### Disconnect ClientManager when the scene enters the background phase — [8:52]

```swift
import SwiftUI

@main
struct SwiftKartApp: App {
    let manager = ClientManager()
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            RaceScheduleView()
                .environment(manager)
        }
        .onChange(of: scenePhase) { _, newPhase in
            switch newPhase {
            case .background :
                manager.disconnect()
            case .inactive, .active:
                break
            @unknown default:
                break
            }
        }
    }
}
```

### Inject ClientManager into the view via @Environment — [9:12]

```swift
@Environment(ClientManager.self) var manager
```

### Replace withGRPCClient with manager.withClient — [9:21]

```swift
.task {
    do {
        try await manager.withClient { client in
            let kart = SwiftKartService.Client(wrapping: client)
            let request = ListRacesRequest()
            let response = try await kart.listRaces(request)
            self.races = response.races.map { race in
                RaceInfo(
                    name: race.name,
                    location: race.location,
                    startTime: race.startTime.date,
                    championship: race.championship,
                    laps: Int(race.laps),
                    drivers: race.drivers
                )
            }
        }
    } catch {
        print("gRPC error: \(error)")
    }
}
```

### Using SwiftProtobuf — [9:41]

```swift
var race = Race()
race.name = "Duck Pond Dash"
race.location = "Apple Park, Cupertino"
race.startTime = .init(roundingTimeIntervalSince1970: 1_781_198_600)
race.laps = 6
race.championship = "Corporate Cup"
race.drivers = ["Monty", "Pepper", "Mycroft", "Pancakes", "Duke", "Kiko", "Sissi", "Bo"]

try race.serializedBytes()
```

### Server — [12:32]

```swift
let server = GRPCServer(
    transport: .http2NIOPosix(
        address: .ipv4(host: "127.0.0.1", port: 8080),
        transportSecurity: .plaintext
    ),
    services: [Service()]
)
try await server.serve()
```

### Service — [12:45]

```swift
struct Service: SwiftKartService.SimpleServiceProtocol {
    private let database = RaceDB()

    func listRaces(
        request: ListRacesRequest,
        context: ServerContext
    ) async throws -> ListRacesResponse {
        var response = ListRacesResponse()
        response.races = await database.listRaces(atMost: request.limit)
        return response
    }
}
```

### swift_kart_service.proto — [13:20]

```bash
edition = "2024";

import "google/protobuf/duration.proto";
import "google/protobuf/timestamp.proto";

service SwiftKartService {
  rpc ListRaces(ListRacesRequest) returns (ListRacesResponse);
  rpc FollowRace(stream FollowRaceRequest) returns (stream FollowRaceResponse);
}

message ListRacesRequest {
  int32 limit = 1 [default = 100];
}

message ListRacesResponse {
  repeated Race races = 1;
}

message Race {
  string name = 1;
  string location = 2;
  google.protobuf.Timestamp start_time = 3;
  int32 laps = 4;
  string championship = 5;
  repeated string drivers = 6;
}

message FollowRaceRequest {
  string race_name = 1;
  repeated RaceEventType event_types = 2;
}

enum RaceEventType {
  RACE_EVENT_TYPE_UNSPECIFIED = 0;
  RACE_EVENT_TYPE_KART_LOCATIONS = 1;
  RACE_EVENT_TYPE_STANDINGS = 2;
}

message FollowRaceResponse {
  oneof event {
    KartLocations locations = 1;
    Standings standings = 2;
  }
}

message KartLocations {
  message Kart {
    int32 number = 1;
    double latitude = 2;
    double longitude = 3;
    google.protobuf.Timestamp recorded_at = 4;
  }
  repeated Kart karts = 1;
}

message Standings {
  message Entry {
    int32 kart_number = 1;
    google.protobuf.Duration gap_to_leader = 2;
    int32 position = 3;
    int32 lap = 4;
  }

  repeated Entry entries = 1;
}
```

### FollowRace stub — [14:16]

```swift
func followRace(
    request: RPCAsyncSequence<FollowRaceRequest, any Error>,
    response: RPCWriter<FollowRaceResponse>,
    context: ServerContext
) async throws {
    throw RPCError(code: .unimplemented, message: "FollowRace is unimplemented")
}
```

### Implement the FollowRace RPC — [14:38]

```swift
func followRace(
    request: RPCAsyncSequence<FollowRaceRequest, any Error>,
    response: RPCWriter<FollowRaceResponse>,
    context: ServerContext
) async throws {
    try await withThrowingTaskGroup { group in
        var iterator = request.makeAsyncIterator()
        guard let first = try await iterator.next() else { return }
        let eventTypes = Mutex(Set(first.eventTypes))

        group.addTask {
            let events = tracker.events(forRace: first.raceName).filter { event in
                eventTypes.withLock { $0.contains(event.type) }
            }

            for await event in events {
                var message = FollowRaceResponse()
                switch event {
                case .locations(let locations):
                    message.locations.karts = locations.map { location in
                        var kart = KartLocations.Kart()
                        kart.number = Int32(location.number)
                        kart.latitude = location.latitude
                        kart.longitude = location.longitude
                        return kart
                    }
                case .standings(let standings):
                    message.standings.entries = standings.map { standing in
                        var entry = Standings.Entry()
                        entry.gapToLeader = .init(rounding: standing.delta, rule: .towardZero)
                        entry.kartNumber = Int32(standing.kartNumber)
                        entry.lap = Int32(standing.lap)
                        entry.position = Int32(standing.position)
                        return entry
                    }
                }

                try await response.write(message)
            }
        }

        while let next = try await iterator.next() {
            eventTypes.withLock { $0 = Set(next.eventTypes) }
        }

        group.cancelAll()
    }
}
```

### swift_kart_service.proto — [16:39]

```bash
edition = "2024";

import "google/protobuf/duration.proto";
import "google/protobuf/timestamp.proto";

service SwiftKartService {
  rpc ListRaces(ListRacesRequest) returns (ListRacesResponse);
  rpc FollowRace(stream FollowRaceRequest) returns (stream FollowRaceResponse);
}

message ListRacesRequest {
  int32 limit = 1 [default = 100];
}

message ListRacesResponse {
  repeated Race races = 1;
}

message Race {
  string name = 1;
  string location = 2;
  google.protobuf.Timestamp start_time = 3;
  int32 laps = 4;
  string championship = 5;
  repeated string drivers = 6;
}

message FollowRaceRequest {
  string race_name = 1;
  repeated RaceEventType event_types = 2;
}

enum RaceEventType {
  RACE_EVENT_TYPE_UNSPECIFIED = 0;
  RACE_EVENT_TYPE_KART_LOCATIONS = 1;
  RACE_EVENT_TYPE_STANDINGS = 2;
}

message FollowRaceResponse {
  oneof event {
    KartLocations locations = 1;
    Standings standings = 2;
  }
}

message KartLocations {
  message Kart {
    int32 number = 1;
    double latitude = 2;
    double longitude = 3;
    google.protobuf.Timestamp recorded_at = 4;
  }
  repeated Kart karts = 1;
}

message Standings {
  message Entry {
    int32 kart_number = 1;
    google.protobuf.Duration gap_to_leader = 2;
    int32 position = 3;
    int32 lap = 4;
  }

  repeated Entry entries = 1;
}
```

### swift_kart_service.proto — [16:40]

```bash
edition = "2024";

import "google/protobuf/timestamp.proto";

service SwiftKartService {
  rpc ListRaces(ListRacesRequest) returns (ListRacesResponse);
}

message ListRacesRequest {
  int32 limit = 1 [default = 100];
}

message ListRacesResponse {
  repeated Race races = 1;
}

message Race {
  string name = 1;
  string location = 2;
  google.protobuf.Timestamp start_time = 3;
  int32 laps = 4;
  string championship = 5;
  repeated string drivers = 6;
}
```

### Navigation link to LiveStreamView — [16:56]

```swift
NavigationLink(destination: LiveStreamView(race: race)) {
    Text("Live stream")
}
```

### Call the FollowRace RPC in the LiveStreamView — [17:32]

```swift
import SwiftUI
import GRPCCore
import GRPCNIOTransportHTTP2
import SwiftProtobuf

struct LiveStreamView: View {
    private let race: RaceInfo

    @Environment(ClientManager.self) var manager
    @State private var tracking: KartTrackingViewModel
    @State private var standings: [StandingsEntry] = []
    @State private var showLeaderboard = false
    @State private var continuation: AsyncStream<Bool>.Continuation?

    init(race: RaceInfo) {
        self.race = race
        self.tracking = KartTrackingViewModel(race: race)
    }

    var body: some View {
        VStack {
            KartTrackingMapView(viewModel: tracking)
                .ignoresSafeArea()
                .onAppear { tracking.start() }
                .onDisappear { tracking.stop() }
        }
        .onChange(of: showLeaderboard) { _, newValue in
            continuation?.yield(newValue)
        }
        .sheet(isPresented: $showLeaderboard) {
            LeaderboardView(race: race, standings: standings)
                .presentationDetents([.fraction(0.3), .medium, .large])
                .presentationBackgroundInteraction(.enabled)
        }
        .toolbar {
            Toggle(isOn: $showLeaderboard) {
                Label("Leaderboard", systemImage: "list.number")
            }
        }
        .toolbarBackgroundVisibility(.visible, for: .navigationBar)
        .task {
            do {
                let (stream, continuation) = AsyncStream.makeStream(of: Bool.self)
                self.continuation = continuation
                continuation.yield(showLeaderboard)

                try await manager.withClient { client in
                    let kart = SwiftKartService.Client(wrapping: client)
                    try await kart.followRace { requestStream in
                        for await showLeaderboard in stream {
                            var message = FollowRaceRequest()
                            message.raceName = race.name
                            message.eventTypes = [.kartLocations]
                            if showLeaderboard {
                                message.eventTypes.append(.standings)
                            }
                            try await requestStream.write(message)
                        }
                    } onResponse: { responseStream in
                        for try await message in responseStream.messages {
                            if let event = message.event {
                                await handleEvent(event)
                            }
                        }
                    }

                }
            } catch {
                print("gRPC error: \(error)")
            }
        }
    }

    @MainActor
    private func handleEvent(_ event: FollowRaceResponse.OneOf_Event) {
        switch event {
        case .locations(let locations):
            self.tracking.updateKartCoordinates(
                locations.karts.map {
                    TrackedKart(number: $0.number, latitude: $0.latitude, longitude: $0.longitude)
                }
            )
        case .standings(let standings):
            self.standings = standings.entries.map {
                StandingsEntry(
                    kartNumber: $0.kartNumber,
                    secondsToLeader: $0.gapToLeader.timeInterval,
                    position: $0.position,
                    lap: $0.lap
                )
            }
        }
    }
}

#Preview {
    NavigationStack {
        LiveStreamView(race: .example4)
            .environment(ClientManager())
    }
}
```

### Containerfile — [20:55]

```bash
FROM swift:latest AS builder

# Copy sources into /app
WORKDIR /app
COPY Package.swift Package.resolved .
COPY Sources/ Sources/

# Build the server
RUN swift build -c release --product server
RUN cp "$(swift build -c release --show-bin-path)/server" /usr/bin/server

# Copy the binary from the builder into a smaller runtime image.
FROM swift:slim
COPY --from=builder /usr/bin/server /usr/bin/server

EXPOSE 8080
ENTRYPOINT ["/usr/bin/server"]
```

### Deploy service — [21:56]

```bash
gcloud run deploy wwdc-demo-server \
--image us-central1-docker.pkg.dev/wwdc26/wwdc-demo-server/wwdc-demo-server:latest \
--region us-central1 \
--use-http2 \
--allow-unauthenticated
```

### Target deployed service — [22:22]

```swift
static func makeTransport() throws -> HTTP2ClientTransport.TransportServices {
    try .http2NIOTS(
        target: .dns(host: "wwdc-demo-server-863666503339.us-central1.run.app"),
        transportSecurity: .tls
    )
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/265/4/05249c6d-4136-4164-a8d0-5db0bbb22c7f/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/265/4/05249c6d-4136-4164-a8d0-5db0bbb22c7f/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._