---
id: "wwdc2020-10684"
event: "wwdc2020"
year: 2020
title: "Swan's Quest, Chapter 4: The sequence completes"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10684"
topics: ["Business & Education", "Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Swan's Quest, Chapter 4: The sequence completes

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10684](https://developer.apple.com/videos/play/wwdc2020/10684)

Swift Playgrounds presents "Swan’s Quest,” an interactive adventure in four chapters for all ages. It’s time for the grand finale: You’ve honed your skills with tones, but in this chapter our Hero needs to sequence multi-part harmony.

Discover how to play pitched instruments with MIDI codes, and you just might help our Hero find the rhythm… and complete their quest.

Swan’s Quest was created for Swift Playgrounds on iPad and Mac, combining frameworks and resources which power the educational experiences in many of our playgrounds, including Sonic Workshop, Sensor Arcade, and Augmented Reality. To learn more about building your own playgrounds, be sure to watch "Create Swift Playgrounds content for iPad and Mac". 

And don’t forget to stop by the Developer Forums and share your solution for our side quests.

**Keywords:** `playground`, `swan's quest`, `swans quest`, `swift`, `swift playgrounds`, `swift playgrounds challenge`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,115 words)

## Documentation & Resources

- [Quest Create playground book](https://developer.apple.com/sample-code/swift/swans-quest/quest-create.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/quest-create.zip
- [Swan's Quest: The sequence completes playground book](https://developer.apple.com/sample-code/swift/swans-quest/the-sequence-completes.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/swift/swans-quest/the-sequence-completes.zip

## Code Snippets

### Barebones example of a sequencer — [2:26]

```swift
// A barebones example of a sequencer

let numberOfBeats = 8   // two bars of 4/4
let duration = 4.0      // seconds

let interval = duration / Double(numberOfBeats)

var index = 0
Timer.scheduledTimer(withTimeInterval: interval, repeats: true) { timer in
    // Play each track's Instrument
    // ...

    index = (index + 1 < numberOfBeats) ? index + 1 : 0
}
```

### Introduction to playInstrument(_:note:volume:) — [3:16]

```swift
// Sequencer.swift

func playInstrument(_ kind: Instrument.Kind, note: MIDINoteProtocol, volume: Double = 75)


// Instrument.swift

public class Instrument {

    /// The kind of included instruments
    public enum Kind: String {
        case electricGuitar, bassGuitar, piano, warmBells, sevenSynth, 
            bassSynth, crystalSynth
    }

    // ...
}
```

### MIDINoteProtocol — [3:38]

```swift
// Sequencer.swift 

protocol MIDINoteProtocol {

    /// note as an 8-bit MIDI code
    var midiCode: UInt8 { get }
}
```

### Example implementation for Notes — [3:48]

```swift
// Example implementation for Notes

enum MIDINotes: UInt8, MIDINoteProtocol {
    case rest = 0

    case C2 = 36
    case D2 = 38
    case E2 = 40
    case F2 = 41
    case G2 = 43
    case A2 = 45
    case B2 = 47

    var midiCode: UInt8 {
        return self.rawValue
    }
}
```

### TrackProtocol — [4:03]

```swift
// Sequencer.swift

protocol TrackProtocol {
    associatedtype NoteType : MidiNoteProtocol

    /// The kind of instrument that the track sequences
    var instrument: Instrument.Kind { get }

    /// Number of beats contained in the sequence
    var length: Int { get }

    /// MIDI code for the sequence frame
    func note(for frame: Int) -> NoteType
}
```

### Example implementation for Tracks — [4:21]

```swift
// Example implementation for Tracks

struct Track : TrackProtocol {
    var instrument: Instrument.Kind
    var length: Int

    var notes: [MIDINotes]? = nil

    func note(for frame: Int) -> MIDINotes {
        guard let n = notes, frame < n.count else {
            return .rest
        }
        return n[frame]
    }
}
```

### Implementing a Sequencer — [4:34]

```swift
// A barebones example of a sequencer

let numberOfBeats = 8   // two bars of 4/4
let duration = 4.0      // seconds

var bass = Track(instrument: .bassGuitar, length: numberOfBeats)
var piano = Track(instrument: .piano, length: numberOfBeats)
let tracks = [bass, piano]

bass.notes =  [.rest, .C2, .A2, .rest, .C2, .A2, .D2, .C2 ]
piano.notes = [.A2, .A2, .C2, .F2, .A2, .C2, .none, .F2]

let interval = duration / Double(numberOfBeats)
var index = 0
Timer.scheduledTimer(withTimeInterval: interval, repeats: true, block: { timer in
    for track in tracks {
        playInstrument(track.instrument, note: track.note(for: index))
    }
    index = (index + 1 < numberOfBeats) ? index + 1 : 0
})
```

### // Getting credit for our work — [5:00]

```swift
// Getting credit for our work

Timer.scheduledTimer(withTimeInterval: interval, repeats: true, block: { timer in
    for track in tracks {
        playInstrument(track.instrument, note: track.note(for: index))
    }

    if index + 1 < numberOfBeats {
        index = index + 1
    }

    else {
        index = 0
        owner.endPerformance()
    }
})
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10684/4/A98BC348-AEAA-412A-98ED-F094D1D9FC2C/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10684) — developer.apple.com. Indexed for agent consumption._