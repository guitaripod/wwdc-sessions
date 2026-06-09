---
id: "wwdc2023-10033"
event: "wwdc2023"
year: 2023
title: "Extend Speech Synthesis with personal and custom voices"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10033"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Extend Speech Synthesis with personal and custom voices

**Event:** WWDC23 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10033](https://developer.apple.com/videos/play/wwdc2023/10033)

Bring the latest advancements in Speech Synthesis to your apps. Learn how you can integrate your custom speech synthesizer and voices into iOS and macOS. We’ll show you how SSML is used to generate expressive speech synthesis, and explore how Personal Voice can enable your augmentative and assistive communication app to speak on a person’s behalf in an authentic way.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,713 words)

## Documentation & Resources

- [Audio Unit](https://developer.apple.com/documentation/AudioUnit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AudioUnit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AudioUnit.json
- [Creating an audio unit extension](https://developer.apple.com/documentation/AVFAudio/creating-an-audio-unit-extension) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFAudio/creating-an-audio-unit-extension
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFAudio/creating-an-audio-unit-extension.json
- [Speech Synthesis Markup Language (SSML)](https://www.w3.org/TR/speech-synthesis/) _guide_
- [Speech synthesis](https://developer.apple.com/documentation/AVFoundation/speech-synthesis) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/speech-synthesis
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/speech-synthesis.json

## Code Snippets

### SSML phrase — [2:10]

```xml
<speak>
    Hello
    <break time="1s"/>
    <prosody rate="200%">nice to meet you!</prosody>
</speak>
```

### SSML utterance — [2:29]

```swift
let ssml = """
    <speak>
        Hello
        <break time="1s" />
        <prosody rate="200%">nice to meet you!</prosody>
    </speak>
"""

guard let ssmlUtterance = AVSpeechUtterance(ssmlRepresentation: ssml) else {
    return
}

self.synthesizer.speak(ssmlUtterance)
```

### Create a host app — [4:33]

```swift
struct ContentView: View {

    var body: some View {
        List {
            Section("My Awesome Voices") {
                ForEach(availableVoices) { voice in
                    HStack {
                        Text(voice.name)
                        Spacer()
                        Button("Buy") {
                            // Buy this voice...
                        }
                    }
                }
            }
        }
    }

    var availableVoices: [WWDCVoice] {
        return [
            WWDCVoice(name: "Screen Reader Voice", id: "com.example.screen-reader-voice"),
            WWDCVoice(name: "Reading Voice", id: "com.example.reading-voice")
        ]
    }   
}
```

### Keep track of purchased voices — [5:04]

```swift
struct ContentView: View {

    @State var purchasedVoices: [WWDCVoice] = []

    var body: some View {
        NavigationStack {
            List {
                MyAwesomeVoicesSection
                Section("Purchased Voices") {
                    ForEach(purchasedVoices) { voice in
                        NavigationLink {
                            // Destination View
                        } label: {
                            Text(voice.name)
                        }
                    }
                }
            }
        }
    }
}
```

### Inform the system when available voices change — [5:13]

```swift
struct ContentView: View {

    @State var purchasedVoices: [WWDCVoice] = []

    var body: some View {
        List {
            MyAwesomeVoicesSection
            PurchasedVoicesSection
        }
    }

    func purchase(voice: WWDCVoice) {
        // Append voice to list of purchased voices
        purchasedVoices.append(voice)

        // Inform system of change in voices
        AVSpeechSynthesisProviderVoice.updateSpeechVoices()
    }
}
```

### Update UI with purchased voices — [5:39]

```swift
struct ContentView: View {

    @State var purchasedVoices: [WWDCVoice] = []

    var body: some View {
        List {
            Section("My Awesome Voices") {
                ForEach(availableVoices.filter { !purchasedVoices.contains($0) }) { voice in
                    HStack {
                        Text(voice.name)
                        Spacer()
                        Button("Buy") {
                            purchase(voice: voice)
                        }
                    }
                }
            }
            PurchasedVoicesSection
        }
    }
}
```

### Save available voices into UserDefaults — [5:46]

```swift
struct ContentView: View {

    let groupDefaults = UserDefaults(suiteName: "group.com.example.SpeechSynthesizerApp")!

    @State var purchasedVoices: [WWDCVoice] = []

    var body: some View {
        List {
            MyAwesomeVoicesSection
            PurchasedVoicesSection
        }
    }

    func purchase(voice: WWDCVoice) {
        // Append voice to list of purchased voices
        purchasedVoices.append(voice)

        // Write purchasedVoices to defaults
        updatePurchasedVoices()

        // Inform system of change in voices
        AVSpeechSynthesisProviderVoice.updateSpeechVoices()
    }
}
```

### Monitor for system voice changes — [6:25]

```swift
struct ContentView: View {

    @State var systemVoices: [AVSpeechSynthesisVoice] = AVSpeechSynthesisVoice.speechVoices()

    var body: some View {
        List {
            MyAwesomeVoicesSection
            PurchasedVoicesSection
            Section("System Voices") {
                ForEach(systemVoices.filter { $0.language == "en-US" }) { voice in
                    Text(voice.name)
                }
            }
        }
        .onReceive(NotificationCenter.default
            .publisher(for: AVSpeechSynthesizer.availableVoicesDidChangeNotification)) { _ in
                systemVoices = AVSpeechSynthesisVoice.speechVoices()
        }
    }
}
```

### Override speechVoices getter — [6:53]

```swift
// Implement a synthesis provider

public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override var speechVoices: [AVSpeechSynthesisProviderVoice] {
        get { }
    }
}
```

### Use UserDefaults to provide set of available voices — [7:02]

```swift
public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override var speechVoices: [AVSpeechSynthesisProviderVoice] {
        get {
            let voices: [String : String] = groupDefaults.value(forKey: "voices") as? [String : String] ?? [:]
            return voices.map { key, value in
                return AVSpeechSynthesisProviderVoice(name: value,
                                                identifier: key,
                                          primaryLanguages: ["en-US"],
                                        supportedLanguages: ["en-US"] )
            }
        }
    }
}
```

### Use your synthesis engine on each synthesis request — [7:22]

```swift
public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override func synthesizeSpeechRequest(speechRequest: AVSpeechSynthesisProviderRequest) {
        currentBuffer = getAudioBuffer(for: speechRequest.voice, with: speechRequest.ssmlRepresentation)
        framePosition = 0
    }
}
```

### Handle request cancellation — [8:14]

```swift
public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override func synthesizeSpeechRequest(speechRequest: AVSpeechSynthesisProviderRequest) {
        currentBuffer = getAudioBuffer(for: speechRequest.voice, with: speechRequest.ssmlRepresentation)
        framePosition = 0
    }

    public override func cancelSpeechRequest() {
        currentBuffer = nil
    }
}
```

### Override internalRenderBlock — [8:28]

```swift
public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override var internalRenderBlock: AUInternalRenderBlock {
       return { [weak self]
           actionFlags, timestamp, frameCount, outputBusNumber, outputAudioBufferList, _, _ in
           guard let self else { return kAudio_ParamError }

           return noErr
       }
    }
}
```

### Implement the render block — [8:42]

```swift
public class WWDCSynthAudioUnit: AVSpeechSynthesisProviderAudioUnit {
    public override var internalRenderBlock: AUInternalRenderBlock {
       return { [weak self]
           actionFlags, timestamp, frameCount, outputBusNumber, outputAudioBufferList, _, _ in
           guard let self else { return kAudio_ParamError }

           // This is the audio buffer we are going to fill up
           var unsafeBuffer = UnsafeMutableAudioBufferListPointer(outputAudioBufferList)[0]
           let frames = unsafeBuffer.mData!.assumingMemoryBound(to: Float32.self)

           var sourceBuffer = UnsafeMutableAudioBufferListPointer(self.currentBuffer!.mutableAudioBufferList)[0]
           let sourceFrames = sourceBuffer.mData!.assumingMemoryBound(to: Float32.self)

           for frame in 0..<frameCount {
               if frames.count > frame && sourceFrames.count > self.framePosition {
                   frames[Int(frame)] = sourceFrames[Int(self.framePosition)]
                   self.framePosition += 1
                   if self.framePosition >= self.currentBuffer!.frameLength {
                       break
                   }
               }
           }

           return noErr
       }
    }
}
```

### Request authorization for Personal Voice — [11:10]

```swift
struct ContentView: View {

    @State private var personalVoices: [AVSpeechSynthesisVoice] = []

    func fetchPersonalVoices() async {
        AVSpeechSynthesizer.requestPersonalVoiceAuthorization() { status in
            if status == .authorized {
                personalVoices = AVSpeechSynthesisVoice.speechVoices().filter { $0.voiceTraits.contains(.isPersonalVoice) }
            }
        }
    }
}
```

### Use Personal Voice — [11:34]

```swift
func speakUtterance(string: String) {
    let utterance = AVSpeechUtterance(string: string)
    if let voice = personalVoices.first {
        utterance.voice = voice
        syntheizer.speak(utterance)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10033/4/2BED83CA-28F2-4B53-ACB4-EF89AB371676/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10033/4/2BED83CA-28F2-4B53-ACB4-EF89AB371676/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10033) — developer.apple.com. Indexed for agent consumption._
