---
id: "wwdc2026-253"
event: "wwdc2026"
year: 2026
title: "Meet the Music Understanding framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/253"
topics: ["AI & Machine Learning", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Meet the Music Understanding framework

**Event:** WWDC26 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-253](https://developer.apple.com/videos/play/wwdc2026/253)

Discover Music Understanding, a new framework that lets your app analyze audio across six dimensions, on device: key, rhythm, structure, pace, instrument activity, and loudness. And use the Music Understanding Lab sample app to visualize each result.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,879 words)

## Documentation & Resources

- [Creating visuals with Music Understanding analysis results](https://developer.apple.com/documentation/MusicUnderstanding/create-visuals-using-musicunderstanding-analysis-results) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MusicUnderstanding/create-visuals-using-musicunderstanding-analysis-results
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MusicUnderstanding/create-visuals-using-musicunderstanding-analysis-results.json
- [Music Understanding](https://developer.apple.com/documentation/MusicUnderstanding) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MusicUnderstanding
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MusicUnderstanding.json

## Code Snippets

### Initialize the session — [4:47]

```swift
import MusicUnderstanding

.fileImporter(isPresented: $isPresented, allowedContentTypes: [.audio]) { result in
    switch result {
    case .success(let url):
        let asset = AVURLAsset(url: url, 
                               options: [AVURLAssetPreferPreciseDurationAndTimingKey : true])
        let session = try await MusicUnderstandingSession(asset: asset)
        let results = try await session.analyze()
    }
}
```

### Inside SessionResult — [5:24]

```swift
import MusicUnderstanding

public struct SessionResult: Codable, Sendable {
    public let instrumentActivity: InstrumentActivityResult?
    public let key: KeyResult?
    public let loudness: LoudnessResult?
    public let pace: PaceResult?
    public let rhythm: RhythmResult?
    public let structure: StructureResult?
}
```

### TimedValue — [5:53]

```swift
import MusicUnderstanding

public struct TimedValue<Value>: Codable, Equatable, Sendable
where Value: Codable & Equatable & Sendable {
    public let time: CMTime
    public let value: Value
}
```

### RangedValue — [5:58]

```swift
import MusicUnderstanding

public struct RangedValue<Value>: Codable, Equatable, Sendable
where Value: Codable & Equatable & Sendable {
    public let range: CMTimeRange
    public let value: Value
}
```

### Key analysis — [6:27]

```swift
public struct KeyResult: Codable, Sendable {
    public let ranges: [MusicUnderstandingSession.RangedValue<KeySignature]
}
```

### KeySignature — [6:43]

```swift
public struct KeySignature: Codable, Hashable, Sendable {
    public let tonic: Tonic
    public let mode: Mode
}
```

### Using tonic — [6:48]

```swift
@frozen public enum Tonic: String, Codable, Hashable, Sendable {
    case aFlat, aSharp, a, bFlat, b, c, cSharp, d, dFlat, dSharp, eFlat, e, f, fSharp, g, gFlat, gSharp
}
```

### Using mode — [6:59]

```swift
public enum Mode: String, Codable, Hashable, Sendable {
    case major, minor
}
```

### Rhythm analysis — [7:16]

```swift
import MusicUnderstanding

public struct RhythmResult: Codable, Sendable {
    public let beats: [CMTime]
    public let bars: [CMTime]
    public let beatsPerMinute: Float?
}
```

### StructureResult — [8:42]

```swift
import MusicUnderstanding

public struct StructureResult: Codable, Sendable {
    public let sections: [CMTimeRange]
    public let segments: [CMTimeRange]
    public let phrases: [CMTimeRange]
}
```

### Analyzing pace — [9:26]

```swift
import MusicUnderstanding

public struct PaceResult: Codable, Sendable {
    public let ranges: [MusicUnderstandingSession.RangedValue<Double>]
}
```

### InstrumentActivityResult — [10:13]

```swift
import MusicUnderstanding

public struct InstrumentActivityResult: Codable, Sendable {
    public let ranges: [Instrument: [CMTimeRange]]
    public let activity: [Instrument: [MusicUnderstandingSession.TimedValue<Float>]]
}
```

### LoudnessResult — [11:45]

```swift
import MusicUnderstanding

public struct LoudnessResult: Codable, Sendable {
    public let integrated: MusicUnderstandingSession.TimedValue<Float>
    public let momentary: [MusicUnderstandingSession.TimedValue<Float>]
    public let shortTerm: [MusicUnderstandingSession.TimedValue<Float>]
    public let peak: MusicUnderstandingSession.TimedValue<Float>
}
```

### Streaming API for loudness — [12:48]

```swift
import MusicUnderstanding

public var loudnessResults: some AsyncSequence<LoudnessResult, any Error> & Sendable
```

### Streaming API for loudness — [12:55]

```swift
import MusicUnderstanding

let audioProvider = AudioProvider()
let session = MusicUnderstandingSession(audioProvider: audioProvider)
await withThrowingTaskGroup(of: Void.self) { taskGroup in
    group.addTask {
        for try await result in await session.loudnessResults {
            updateAudioLevel(result.momentary.value)
        }
    }

    group.addTask {
        try await session.analyze(for: [.loudness])
    }
}
```

### Audio Provider — [13:19]

```swift
import MusicUnderstanding

struct AudioProvider: AsyncSequence, AsyncIteratorProtocol {
   func makeAsyncIterator() -> Self {
        return self
    }

   mutating func next() async -> AVReadOnlyAudioPCMBuffer? {
        // Return the next audio buffer, or nil to signal completion
    }
}
```

### Encode to JSON — [13:55]

```swift
import MusicUnderstanding

let session = try await MusicUnderstandingSession(asset: asset)
let results = try await session.analyze()

let encoder = JSONEncoder()
try encoder.encode(results)
```

### Suggestion for using pace — [14:47]

```swift
let timePerClip = 60 / paceValue
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/253/5/db1c3715-aaaf-42db-8e9e-66d2a0011430/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/253/5/db1c3715-aaaf-42db-8e9e-66d2a0011430/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/253) — developer.apple.com. Indexed for agent consumption._
