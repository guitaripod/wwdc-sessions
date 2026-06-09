---
id: "wwdc2025-277"
event: "wwdc2025"
year: 2025
title: "Bring advanced speech-to-text to your app with SpeechAnalyzer"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/277"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring advanced speech-to-text to your app with SpeechAnalyzer

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-277](https://developer.apple.com/videos/play/wwdc2025/277)

Discover the new SpeechAnalyzer API for speech to text. We’ll learn about the Swift API and its capabilities, which power features in Notes, Voice Memos, Journal, and more. We’ll dive into details about how speech to text works and how SpeechAnalyzer and SpeechTranscriber can enable you to create exciting, performant features. And you’ll learn how to incorporate SpeechAnalyzer and live transcription into your app with a code-along.

**Keywords:** `machine learning`, `speech-to-text`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,839 words)

## Documentation & Resources

- [Bringing advanced speech-to-text capabilities to your app](https://developer.apple.com/documentation/Speech/bringing-advanced-speech-to-text-capabilities-to-your-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Speech/bringing-advanced-speech-to-text-capabilities-to-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Speech/bringing-advanced-speech-to-text-capabilities-to-your-app.json
- [Speech](https://developer.apple.com/documentation/Speech) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Speech
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Speech.json

## Code Snippets

### Transcribe a file — [5:21]

```swift
// Set up transcriber. Read results asynchronously, and concatenate them together.
let transcriber = SpeechTranscriber(locale: locale, preset: .offlineTranscription)
async let transcriptionFuture = try transcriber.results
    .reduce("") { str, result in str + result.text }

let analyzer = SpeechAnalyzer(modules: [transcriber])
if let lastSample = try await analyzer.analyzeSequence(from: file) {
    try await analyzer.finalizeAndFinish(through: lastSample)
} else {
    await analyzer.cancelAndFinishNow()
}

return try await transcriptionFuture
```

### Speech Transcriber setup (volatile results + timestamps) — [11:02]

```swift
func setUpTranscriber() async throws {
        transcriber = SpeechTranscriber(locale: Locale.current,
                                        transcriptionOptions: [],
                                        reportingOptions: [.volatileResults],
                                        attributeOptions: [.audioTimeRange])
    }
```

### Speech Transcriber setup (volatile results, no timestamps) — [11:47]

```swift
// transcriber = SpeechTranscriber(locale: Locale.current, preset: .progressiveLiveTranscription)
```

### Set up SpeechAnalyzer — [11:54]

```swift
func setUpTranscriber() async throws {
    transcriber = SpeechTranscriber(locale: Locale.current,
                                    transcriptionOptions: [],
                                    reportingOptions: [.volatileResults],
                                    attributeOptions: [.audioTimeRange])

    guard let transcriber else {
        throw TranscriptionError.failedToSetupRecognitionStream
    }

    analyzer = SpeechAnalyzer(modules: [transcriber])
}
```

### Get audio format — [12:00]

```swift
func setUpTranscriber() async throws {
    transcriber = SpeechTranscriber(locale: Locale.current,
                                    transcriptionOptions: [],
                                    reportingOptions: [.volatileResults],
                                    attributeOptions: [.audioTimeRange])

    guard let transcriber else {
        throw TranscriptionError.failedToSetupRecognitionStream
    }

    analyzer = SpeechAnalyzer(modules: [transcriber])

    self.analyzerFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])
}
```

### Ensure models — [12:06]

```swift
func setUpTranscriber() async throws {
    transcriber = SpeechTranscriber(locale: Locale.current,
                                    transcriptionOptions: [],
                                    reportingOptions: [.volatileResults],
                                    attributeOptions: [.audioTimeRange])

    guard let transcriber else {
        throw TranscriptionError.failedToSetupRecognitionStream
    }

    analyzer = SpeechAnalyzer(modules: [transcriber])

    self.analyzerFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])

    do {
        try await ensureModel(transcriber: transcriber, locale: Locale.current)
    } catch let error as TranscriptionError {
        print(error)
        return
    }
}
```

### Finish SpeechAnalyzer setup — [12:15]

```swift
func setUpTranscriber() async throws {
    transcriber = SpeechTranscriber(locale: Locale.current,
                                    transcriptionOptions: [],
                                    reportingOptions: [.volatileResults],
                                    attributeOptions: [.audioTimeRange])

    guard let transcriber else {
        throw TranscriptionError.failedToSetupRecognitionStream
    }

    analyzer = SpeechAnalyzer(modules: [transcriber])

    self.analyzerFormat = await SpeechAnalyzer.bestAvailableAudioFormat(compatibleWith: [transcriber])

    do {
        try await ensureModel(transcriber: transcriber, locale: Locale.current)
    } catch let error as TranscriptionError {
        print(error)
        return
    }

    (inputSequence, inputBuilder) = AsyncStream<AnalyzerInput>.makeStream()

    guard let inputSequence else { return }

    try await analyzer?.start(inputSequence: inputSequence)
}
```

### Check for language support — [12:30]

```swift
public func ensureModel(transcriber: SpeechTranscriber, locale: Locale) async throws {
        guard await supported(locale: locale) else {
            throw TranscriptionError.localeNotSupported
        }
    }

    func supported(locale: Locale) async -> Bool {
        let supported = await SpeechTranscriber.supportedLocales
        return supported.map { $0.identifier(.bcp47) }.contains(locale.identifier(.bcp47))
    }

    func installed(locale: Locale) async -> Bool {
        let installed = await Set(SpeechTranscriber.installedLocales)
        return installed.map { $0.identifier(.bcp47) }.contains(locale.identifier(.bcp47))
    }
```

### Check for model installation — [12:39]

```swift
public func ensureModel(transcriber: SpeechTranscriber, locale: Locale) async throws {
        guard await supported(locale: locale) else {
            throw TranscriptionError.localeNotSupported
        }

        if await installed(locale: locale) {
            return
        } else {
            try await downloadIfNeeded(for: transcriber)
        }
    }

    func supported(locale: Locale) async -> Bool {
        let supported = await SpeechTranscriber.supportedLocales
        return supported.map { $0.identifier(.bcp47) }.contains(locale.identifier(.bcp47))
    }

    func installed(locale: Locale) async -> Bool {
        let installed = await Set(SpeechTranscriber.installedLocales)
        return installed.map { $0.identifier(.bcp47) }.contains(locale.identifier(.bcp47))
    }
```

### Download the model — [12:52]

```swift
func downloadIfNeeded(for module: SpeechTranscriber) async throws {
        if let downloader = try await AssetInventory.assetInstallationRequest(supporting: [module]) {
            self.downloadProgress = downloader.progress
            try await downloader.downloadAndInstall()
        }
    }
```

### Deallocate an asset — [13:19]

```swift
func deallocate() async {
        let allocated = await AssetInventory.allocatedLocales
        for locale in allocated {
            await AssetInventory.deallocate(locale: locale)
        }
    }
```

### Speech result handling — [13:31]

```swift
recognizerTask = Task {
            do {
                for try await case let result in transcriber.results {
                    let text = result.text
                    if result.isFinal {
                        finalizedTranscript += text
                        volatileTranscript = ""
                        updateStoryWithNewText(withFinal: text)
                        print(text.audioTimeRange)
                    } else {
                        volatileTranscript = text
                        volatileTranscript.foregroundColor = .purple.opacity(0.4)
                    }
                }
            } catch {
                print("speech recognition failed")
            }
        }
```

### Set up audio recording — [15:13]

```swift
func record() async throws {
        self.story.url.wrappedValue = url
        guard await isAuthorized() else {
            print("user denied mic permission")
            return
        }
#if os(iOS)
        try setUpAudioSession()
#endif
        try await transcriber.setUpTranscriber()

        for await input in try await audioStream() {
            try await self.transcriber.streamAudioToTranscriber(input)
        }
    }
```

### Set up audio recording via AVAudioEngine — [15:37]

```swift
#if os(iOS)
    func setUpAudioSession() throws {
        let audioSession = AVAudioSession.sharedInstance()
        try audioSession.setCategory(.playAndRecord, mode: .spokenAudio)
        try audioSession.setActive(true, options: .notifyOthersOnDeactivation)
    }
#endif

    private func audioStream() async throws -> AsyncStream<AVAudioPCMBuffer> {
        try setupAudioEngine()
        audioEngine.inputNode.installTap(onBus: 0,
                                         bufferSize: 4096,
                                         format: audioEngine.inputNode.outputFormat(forBus: 0)) { [weak self] (buffer, time) in
            guard let self else { return }
            writeBufferToDisk(buffer: buffer)
            self.outputContinuation?.yield(buffer)
        }

        audioEngine.prepare()
        try audioEngine.start()

        return AsyncStream(AVAudioPCMBuffer.self, bufferingPolicy: .unbounded) {
            continuation in
            outputContinuation = continuation
        }
    }
```

### Stream audio to SpeechAnalyzer and SpeechTranscriber — [16:01]

```swift
func streamAudioToTranscriber(_ buffer: AVAudioPCMBuffer) async throws {
        guard let inputBuilder, let analyzerFormat else {
            throw TranscriptionError.invalidAudioDataType
        }

        let converted = try self.converter.convertBuffer(buffer, to: analyzerFormat)
        let input = AnalyzerInput(buffer: converted)

        inputBuilder.yield(input)
    }
```

### Finalize the transcript stream — [16:29]

```swift
try await analyzer?.finalizeAndFinishThroughEndOfInput()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/277/4/9eedc53d-668f-48f3-9cca-4f2530bbb2ce/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/277/4/9eedc53d-668f-48f3-9cca-4f2530bbb2ce/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/277) — developer.apple.com. Indexed for agent consumption._
