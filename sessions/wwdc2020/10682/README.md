---
id: "wwdc2020-10682"
event: "wwdc2020"
year: 2020
title: "Swan's Quest, Chapter 2: A time for tones"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10682"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Swan's Quest, Chapter 2: A time for tones

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10682](https://developer.apple.com/videos/play/wwdc2020/10682)

Swift Playgrounds presents "Swan’s Quest,” an interactive adventure in four chapters for all ages. In this chapter, our Hero needs your help decoding the Swan’s scroll. Call forth the best of your audio abilities on this one — you’re going to need them.

Discover how to convert Swift Playgrounds into a tone generator, and you just might help our Hero find the missing message… and move onto the next part of their quest.

Swan’s Quest was created for Swift Playgrounds on iPad and Mac, combining frameworks and resources which power the educational experiences in many of our playgrounds, including Sonic Workshop, Sensor Arcade, and Augmented Reality. To learn more about building your own playgrounds, be sure to watch "Create Swift Playgrounds content for iPad and Mac".

And don’t forget to stop by the Developer Forums and share your solution for our side quest.

**Keywords:** `playgrounds`, `swan's quest`, `swans quest`, `swift`, `swift playgrounds`, `swift playgrounds challenge`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(799 words)

## Documentation & Resources

- [Quest Create playground book](https://developer.apple.com/sample-code/swift/swans-quest/quest-create.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/quest-create.zip
- [Swan's Quest: A time for tones playground book](https://developer.apple.com/sample-code/swift/swans-quest/a-time-for-tones.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/a-time-for-tones.zip

## Code Snippets

### ToneOutput.swift — [1:09]

```swift
//  ToneOutput.swift

public class ToneOutput : AURenderCallbackDelegate {
    let sampleRate = 44100.0

    public func play(tone: Tone) { /**/ }

    public func stopTones() { /**/ }

    // ...

}
```

### Inside the Tone type — [1:30]

```swift
//  ToneOutput.swift

public struct Tone: Codable {
    public var pitch: Double
    public var volume: Double

    // ...
}
```

### Play a middle A — [1:45]

```swift
// Play a middle A

import SPCAudio

let toneOutput = ToneOutput()
let middleA = Tone(pitch: 440.0, volume: 0.3) 
toneOutput.play(tone: middleA)
```

### Play a middle A for 0.5 seconds — [2:21]

```swift
// Play a middle A

import SPCAudio

let toneOutput = ToneOutput()
let a4 = Tone(pitch: 440.0, volume: 0.3)
toneOutput.play(tone: a4)

DispatchQueue.main.asyncAfter(deadline: .now() + DispatchTimeInterval.milliseconds(400)) {
    toneOutput.stopTones()
}
```

### Play more than one tone — [2:51]

```swift
// Play more than one tone

let toneOutput = ToneOutput()
let tones = [
    Tone(pitch: 440.00, volume: 0.3),
    Tone(pitch: 493.88, volume: 0.3),
    Tone(pitch: 523.25, volume: 0.3) 
]

var toneIndex = 0
Timer.scheduledTimer(withTimeInterval: 0.4, repeats: true) { timer in
    guard toneIndex < tones.count else {
        toneOutput.stopTones()
        timer.invalidate()
        owner.endPerformance()
        return
    }

    toneOutput.play(tone: tones[toneIndex])
    toneIndex += 1
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10682/3/B984C50E-3AF2-42F2-9BD0-219FC77E8074/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10682) — developer.apple.com. Indexed for agent consumption._