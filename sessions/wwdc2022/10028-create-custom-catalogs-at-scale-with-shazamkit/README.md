---
id: "wwdc2022-10028"
event: "wwdc2022"
year: 2022
title: "Create custom catalogs at scale with ShazamKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10028"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Create custom catalogs at scale with ShazamKit

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10028](https://developer.apple.com/videos/play/wwdc2022/10028)

Learn how ShazamKit can help you build custom catalogs and support exact matching of any audio source within your app — all on-device. Find out how you can easily generate audio signatures and build catalogs at scale through the new ShazamKit CLI. We'll also show you how you can quickly update your app to sync with large amounts of audio content like multiple seasons of a TV show or multiple episodes of a podcast, and we'll share updates to the ShazamKit API and SHMediaItems to help your apps respond precisely to key moments in audio sources using time ranges. For more on ShazamKit, we recommend watching "Explore ShazamKit" and "Create custom audio experiences with ShazamKit" from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,553 words)

## Documentation & Resources

- [ShazamKit](https://developer.apple.com/documentation/ShazamKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ShazamKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ShazamKit.json

## Code Snippets

### Food Math Matcher — [4:26]

```swift
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
The model that is responsible for matching against the catalog and update the SwiftUI Views.
*/

import ShazamKit
import AVFAudio

struct MatchResult {
    var title: String?
    var equation: Equation?
    var episode: Episode?
    var answerRange: ClosedRange<Int>?

    var hasContent: Bool {
        equation != nil || title != nil || answerRange != nil
    }
}

class Matcher: NSObject, ObservableObject, SHSessionDelegate {
    @Published var matchResult: MatchResult?

    private var session: SHSession!
    private let audioEngine = AVAudioEngine()
    private var matchingTask: Task<Void, Never>? = nil

    func match(catalog: SHCustomCatalog) throws {

        session = SHSession(catalog: catalog)
        session.delegate = self

        let audioFormat = AVAudioFormat(standardFormatWithSampleRate: audioEngine.inputNode.outputFormat(forBus: 0).sampleRate,
                                        channels: 1)
        audioEngine.inputNode.installTap(onBus: 0, bufferSize: 2048, format: audioFormat) { [weak session] buffer, audioTime in
            session?.matchStreamingBuffer(buffer, at: audioTime)
        }

        try AVAudioSession.sharedInstance().setCategory(.record)
        AVAudioSession.sharedInstance().requestRecordPermission { [weak self] success in
            guard success, let self = self else { return }

            Task.detached {
                try? self.audioEngine.start()
            }
        }

        Task { @MainActor in
            for await case .match(let match) in session.results {
                self.matchResult = match.matchResult
            }
        }
    }
}

extension SHMatch {

    var matchResult: MatchResult {
        mediaItems.reduce(into: MatchResult()) { result, mediaItem in
            result.title = result.title ?? mediaItem.title
            result.episode = result.episode ?? mediaItem.episode
            result.equation = result.equation ?? mediaItem.equation
            result.answerRange = result.answerRange ?? mediaItem.answerRange
        }
    }
}
```

### Timed Media Items — [13:51]

```swift
// Restrict this media item to only describe the first 5 seconds

 let mediaItem = SHMediaItem(properties: [
            .title: "Title",
            .timeRanges:[0.0..<5.0]
        ])

 let timeRanges: [Range<TimeInterval>] = mediaItem.timeRanges
```

### Combine Catalogs — [16:02]

```swift
let parentCatalog = SHCustomCatalog()

parentCatalog.add(from: URL(fileURLWithPath: "/path/to/Episode1.shazamcatalog"))
parentCatalog.add(from: URL(fileURLWithPath: "/path/to/Episode2.shazamcatalog"))
parentCatalog.add(from: URL(fileURLWithPath: "/path/to/Episode3.shazamcatalog"))
```

### Frequency Skew — [16:58]

```swift
func within(range: Range<Float>, for matchedMediaItem: SHMatchedMediaItem) -> Bool {

	range.contains(matchedMediaItem.frequencySkew)
}
```

### Frequency Skew Ranges — [17:21]

```swift
// Restrict this media item to only describe the first 5 seconds

 let mediaItem = SHMediaItem(properties: [
            .title: “Frequency Skewed Audio”,
            .frequencySkewRanges:[0.01..<0.02]
        ])

 let frequencySkewRanges: [Range<Float>] = mediaItem.frequencySkewRanges
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10028/3/F2DB18FC-F40C-4FB9-A080-5202CE2794CA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10028/3/F2DB18FC-F40C-4FB9-A080-5202CE2794CA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10028) — developer.apple.com. Indexed for agent consumption._
