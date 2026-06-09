---
id: "wwdc2020-10683"
event: "wwdc2020"
year: 2020
title: "Swan's Quest, Chapter 3: The notable scroll"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10683"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Swan's Quest, Chapter 3: The notable scroll

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10683](https://developer.apple.com/videos/play/wwdc2020/10683)

Swift Playgrounds presents "Swan’s Quest,” an interactive adventure in four chapters for all ages. Calling all musicians! In this chapter, our Hero has found a mysterious scroll of music, and only you can help decode it. (Don’t worry if you can’t read music, our clever Lizard is standing by to assist. It’s sure to be a note-worthy experience.)

By learning a little theory, and mastering time to create tones of different lengths, you just might help our Hero face the music… and move onto the next part of their quest.

Swan’s Quest was created for Swift Playgrounds on iPad and Mac, combining frameworks and resources which power the educational experiences in many of our playgrounds, including Sonic Workshop, Sensor Arcade, and Augmented Reality. To learn more about building your own playgrounds, be sure to watch "Create Swift Playgrounds content for iPad and Mac".

And don’t forget to stop by the Developer Forums and share your solution for our side quest.

**Keywords:** `playgrounds`, `swan's quest`, `swans quest`, `swift`, `swift playgrounds`, `swift playgrounds challenge`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(923 words)

## Documentation & Resources

- [Quest Create playground book](https://developer.apple.com/sample-code/swift/swans-quest/quest-create.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/quest-create.zip
- [Swan's Quest: The notable scroll playground book](https://developer.apple.com/sample-code/swift/swans-quest/the-notable-scroll.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/the-notable-scroll.zip

## Code Snippets

### Example Pitch Implementation — [2:03]

```swift
// Example Pitch implementation

public enum Pitch: Double, PitchProtocol {
    case a4 = 440.0

    var frequency: Double {
        return self.rawValue
    }
}
```

### NoteProtocol — [2:09]

```swift
// Music.swift

public protocol NoteProtocol {

    /// Play this Note through a ToneOutput
    var tone: Tone { get }

    /// The duration of this Note as a multiple of quarter notes,
    /// e.g., a half note is 2.0, an eighth note is 0.5
    var length: Float { get }
}
```

### Example Note implementation — [2:24]

```swift
// Example Note implementation

public enum Note: NoteProtocol {
    case quarter(pitch: Pitch)

    var tone: Tone {
        switch self {
        case .quarter(let pitch):
            return Tone(pitch: pitch.frequency, volume: 0.3)
        }
    }

    var length: Float {
        switch self {
        case .quarter(_):
            return 1.0
        }
    }
}
```

### Play more than one tone redux — [2:51]

```swift
// Play more than one tone redux

let toneOutput = ToneOutput()
let notes = [Note.quarter(pitch: .a4), .half(pitch: .c4), .quarter(pitch: .a4)]

var index = 0
Timer.scheduledTimer(withTimeInterval: 0.4, repeats: true) { timer in
    guard index < tones.count else {
        timer.invalidate()
        owner.endPerformance()
        return
    }

    toneOutput.play(tone: tones[toneIndex].tone)
    index += 1
}
```

### Updating NoteProtocol — [3:18]

```swift
// Music.swift

public protocol NoteProtocol {

    /// Play this Note through a ToneOutput
    var tone: Tone { get }

    /// The duration of this Note as a multiple of quarter notes,
    /// e.g., a half note is 2.0, an eighth note is 0.5
    var length: Float { get }

    /// Length of the smallest Note supported
    static var shortestSupportedNoteLength: Float { get }
}
```

### Updating the Timer interval — [3:36]

```swift
// Play more than one tone redux

let toneOutput = ToneOutput()
let notes = [Note.quarter(pitch: .a4), .half(pitch: .c4), .quarter(pitch: .a4)]
var index = 0

let interval = TimeInterval(Note.shortestSupportedNoteLength * 0.5) // 120 BPM
Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { timer in
    guard index < tones.count else {
        timer.invalidate()
        owner.endPerformance()
        return
    }

    toneOutput.play(tone: tones[toneIndex].tone)
    index += 1
}
```

### Adding subdivide to NoteProtocol — [4:15]

```swift
// Music.swift

public protocol NoteProtocol {
    associatedtype PitchType: PitchProtocol

    /// Play this Note through a ToneOutput
    var tone: Tone { get }

    /// The duration of this Note as a multiple of quarter notes,
    /// e.g., a half note is 2.0, an eighth note is 0.5
    var length: Float { get }

    /// Length of the smallest Note supported
    static var shortestSupportedNoteLength: Float { get }

    /// Subdivide into a series pitches, according to the shortest
    /// supported note
    func subdivide() -> [PitchType]
}
```

### Putting it all together — [4:30]

```swift
// Play more than one tone redux

let toneOutput = ToneOutput()
let notes = [Note.quarter(pitch: .a4), .half(pitch: .a4), .quarter(pitch: .a4)]
var pitches = [Pitch]()
for note in notes {
    pitches.append(contentsOf: note.subdivide())
}
var index = 0

let interval = TimeInterval(Note.shortestSupportedNoteLength * 0.5)
Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { timer in
    guard index < pitches.count else {
        timer.invalidate()
        owner.endPerformance()
        return
    }
    toneOutput.play(tone: Tone(pitch: pitches[index].frequency, volume: 0.3))
    index += 1
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10683/3/ED6FCD26-F83D-4886-B592-D8C93CF836D4/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10683) — developer.apple.com. Indexed for agent consumption._