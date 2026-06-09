---
id: "wwdc2021-10058"
event: "wwdc2021"
year: 2021
title: "Meet AsyncSequence"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10058"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet AsyncSequence

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10058](https://developer.apple.com/videos/play/wwdc2021/10058)

Iterating over a sequence of values over time is now as easy as writing a “for” loop. Find out how the new AsyncSequence protocol enables a natural, simple syntax for iterating over anything from notifications to bytes being streamed from a server. We'll also show you how to adapt existing code to provide asynchronous sequences of your own.

To get the most out of this session, we recommend first watching “Meet async/await in Swift.”

**Keywords:** `asyncstream`, `await`, `earthquakes`, `lines`, `quakes`, `urlsession`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,290 words)

## Documentation & Resources

- [SE-0314: AsyncStream and AsyncThrowingStream](https://github.com/apple/swift-evolution/blob/main/proposals/0314-async-stream.md) _documentation_
- [SE-0298: Async/Await: Sequences](https://github.com/apple/swift-evolution/blob/main/proposals/0298-asyncsequence.md) _documentation_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_

## Code Snippets

### QuakesTool — [0:37]

```swift
@main
struct QuakesTool {
    static func main() async throws {
        let endpointURL = URL(string: "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv")!

        // skip the header line and iterate each one 
        // to extract the magnitude, time, latitude and longitude
        for try await event in endpointURL.lines.dropFirst() {
            let values = event.split(separator: ",")
            let time = values[0]
            let latitude = values[1]
            let longitude = values[2]
            let magnitude = values[4]
            print("Magnitude \(magnitude) on \(time) at \(latitude) \(longitude)")
        }
    }
}
```

### Iterating a Sequence — [3:24]

```swift
for quake in quakes {
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### How the compiler handles iteration — [3:52]

```swift
var iterator = quakes.makeIterator()
while let quake = iterator.next() {
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### How the compiler handles asynchronous iteration — [4:11]

```swift
var iterator = quakes.makeAsyncIterator()
while let quake = await iterator.next() {
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### Iterating an AsyncSequence — [4:28]

```swift
for await quake in quakes {
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### Terminating iteration early by breaking — [5:36]

```swift
for await quake in quakes {
    if quake.location == nil {
        break
    }
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### Skipping values by continuing — [5:51]

```swift
for await quake in quakes {
    if quake.depth > 5 {
        continue
    }
    if quake.magnitude > 3 {
        displaySignificantEarthquake(quake)
    }
}
```

### AsyncSequence might throw — [6:05]

```swift
do {
    for try await quake in quakeDownload {
        ...
    }
} catch {
    ...
}
```

### Concurrently iterating inside an async task — [7:15]

```swift
let iteration1 = Task {
    for await quake in quakes {
        ...
    }
}

let iteration2 = Task {
    do {
        for try await quake in quakeDownload {
            ...
        }
    } catch {
        ...
    }
}

//... later on  
iteration1.cancel()
iteration2.cancel()
```

### Reading bytes from a FileHandle — [7:56]

```swift
for try await line in FileHandle.standardInput.bytes.lines {
    ...
}
```

### Reading lines from a URL — [8:16]

```swift
let url = URL(fileURLWithPath: "/tmp/somefile.txt")
for try await line in url.lines {
    ...
}
```

### Reading bytes from a URLSession — [8:49]

```swift
let (bytes, response) = try await URLSession.shared.bytes(from: url)

guard let httpResponse = response as? HTTPURLResponse,
      httpResponse.statusCode == 200 /* OK */
else {
    throw MyNetworkingError.invalidServerResponse
}

for try await byte in bytes {
    ...
}
```

### Notifications — [9:12]

```swift
let center = NotificationCenter.default
let notification = await center.notifications(named: .NSPersistentStoreRemoteChange).first {
    $0.userInfo[NSStoreUUIDKey] == storeUUID
}
```

### Using an AsyncStream — [11:10]

```swift
class QuakeMonitor {
    var quakeHandler: (Quake) -> Void
    func startMonitoring()
    func stopMonitoring()
}

let quakes = AsyncStream(Quake.self) { continuation in
    let monitor = QuakeMonitor()
    monitor.quakeHandler = { quake in
        continuation.yield(quake)
    }
    continuation.onTermination = { @Sendable _ in
        monitor.stopMonitoring()
    }
    monitor.startMonitoring()
}

let significantQuakes = quakes.filter { quake in
    quake.magnitude > 3
}

for await quake in significantQuakes {
    ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10058/6/59A23687-3AF9-42AE-A922-079B630ED443/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10058/6/59A23687-3AF9-42AE-A922-079B630ED443/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10058) — developer.apple.com. Indexed for agent consumption._