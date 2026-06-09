---
id: "wwdc2026-339"
event: "wwdc2026"
year: 2026
title: "Bring an LLM provider to the Foundation Models framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/339"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Bring an LLM provider to the Foundation Models framework

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-339](https://developer.apple.com/videos/play/wwdc2026/339)

Extend the Foundation Models framework by implementing a LanguageModelExecutor for new models. Explore how to interface with the LanguageModelSession’s transcript, manage session state effectively, and optimize KV cache utilization. Find out how to support custom segment types and unlock advanced capabilities for your generative AI features.

**Keywords:** `ai`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,146 words)

## Documentation & Resources

- [Foundation Models](https://developer.apple.com/documentation/FoundationModels) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels.json
- [Core AI Models](https://github.com/apple/coreai-models) _documentation_
- [MLX Swift LM on GitHub](https://github.com/ml-explore/mlx-swift-lm) _documentation_

## Code Snippets

### Choose a language model — [2:00]

```swift
import FoundationModels
import MLXFoundationModels

// On-device Apple Foundation Model
let model = SystemLanguageModel()

// Private Cloud Compute model
// let model = PrivateCloudComputeLanguageModel()

// Custom Core AI model
// let model = try await CoreAILanguageModel(resourcesAt: modelURL)

// Open-source MLX model from HuggingFace
// let model = MLXLanguageModel(modelID: "mlx-community/my-model")

let session = LanguageModelSession(model: model)
let response = try await session.respond(to: "...")
print(response.content)
```

### Configure Package.swift for your model package — [3:46]

```swift
// Package.swift

let package = Package(
    name: "MyModel",
    platforms: [
        .macOS(.v27), .iOS(.v27), .visionOS(.v27), .watchOS(.v27)
    ],
    products: [
        .library(name: "MyModel", targets: ["MyModel"])
    ],
    dependencies: [
        .package(url: "...", .upToNextMinor(from: "1.0.0"))
    ],
    targets: [
        .target(name: "MyModelRuntime"),
        // public: LanguageModel conformance
        .target(name: "MyModel", dependencies: ["MyModelRuntime"]),
        .testTarget(name: "MyModelTests", dependencies: ["MyModel"])
    ]
)
```

### LanguageModel and LanguageModelExecutor protocols — [4:56]

```swift
// LanguageModel protocol

public protocol LanguageModel: Sendable {
    var capabilities: LanguageModelCapabilities { get }
    var executorConfiguration: Executor.Configuration { get }
}

// LanguageModelExecutor protocol

public protocol LanguageModelExecutor: Sendable {
    init(configuration: Configuration) throws
    func prewarm(model: Model, transcript: Transcript)
    func respond(
        to request: LanguageModelExecutorGenerationRequest,
        model: Model,
        streamingInto channel: LanguageModelExecutorGenerationChannel
    ) async throws
}
```

### Implement LanguageModel and Executor conformances — [6:25]

```swift
// LanguageModel conformance
public struct MyLanguageModel: LanguageModel {
    typealias Executor = MyLanguageModelExecutor

    public var capabilities: LanguageModelCapabilities {
        LanguageModelCapabilities(capabilities: [
            .toolCalling, .guidedGeneration, .reasoning
        ])
    }

    public var executorConfiguration: Executor.Configuration {
        Executor.Configuration(/* ... */)
    }
}

// Executor conformance
public struct MyLanguageModelExecutor: LanguageModelExecutor {
    public typealias Model = MyLanguageModel

    public struct Configuration: Hashable, Sendable { /* ... */ }

    public init(configuration: Configuration) throws { /* ... */ }

    public func respond(
        to request: LanguageModelExecutorGenerationRequest,
        model: MyLanguageModel,
        streamingInto channel: LanguageModelExecutorGenerationChannel
    ) async throws { /* ... */ }
}
```

### Manage model resources with prewarm and respond — [7:28]

```swift
// One approach to managing resources

struct MyLanguageModelExecutor: LanguageModelExecutor {

    private mutating func loadModelIfNeeded() throws -> LoadedWeights {
        let weights = try loadedModel ?? loadWeights()
        loadedModel = weights
        return weights
    }

    func prewarm(transcript: Transcript) {
        loadedModel = try? loadModelIfNeeded()
    }

    func respond( ... ) async throws {
        let weights = try loadModelIfNeeded()
        // ...generate with 'weights'...
    }
}
```

### Map Transcript entries to model messages — [9:00]

```swift
// Transcript entries

let transcript = Transcript(entries: [
    .instructions( ... ),  // "You are a helpful assistant"

    .prompt( ... ),        // "What's the weather in Pittsburgh?"
    .toolCalls( ... ),     // getWeather(location: "Pittsburgh")
    .toolOutput( ... ),    // 65°F, sunny
    .response( ... ),      // "It's 65°F and sunny in Pittsburgh"

    .prompt( ... ),        // "What's the address of Apple Park?"
    .response( ... ),      // "One Apple Park Way, Cupertino, CA 95014"
])
```

### Read generation and context options from the request — [10:42]

```swift
// Parse generation and context options

func respond(
    to request: LanguageModelExecutorGenerationRequest,
    model: MyLanguageModel,
    streamingInto channel: LanguageModelExecutorGenerationChannel
) async throws {
    let reasoningLevel = request.contextOptions.reasoningLevel
    let temperature = request.generationOptions.temperature
    let maxTokens = request.generationOptions.maximumResponseTokens
}
```

### Stream tokens and metadata through the channel — [11:47]

```swift
// Streaming text tokens

func respond( ... ) async throws {
    // 1. Report metadata
    await channel.send(.response(action: .updateMetadata([
        "modelID": "my-model-2026-06-08",
        "requestID": request.id.uuidString
    ])))
    // 2. Report prompt token usage before generating
    await channel.send(.response(action: .updateUsage(
        input: .init(totalTokenCount: promptTokens, cachedTokenCount: cachedTokens),
        output: .init(totalTokenCount: 0, reasoningTokenCount: 0)
    )))
    // 3. Stream text deltas as the model generates
    for try await token in tokens {
        await channel.send(.response(action: .appendText(token)))
    }
}
```

### Honor the developer's intent or throw — [13:33]

```swift
// Honor the developer's intention where possible

// The developer set sampling: .greedy, but our service only takes temperature
if request.generationOptions.sampling?.kind == .greedy {
    serviceRequest.temperature = 0
}

// Otherwise, throw an error

// The token budget is too small to satisfy the schema
if let schema = request.schema,
   let budget = request.generationOptions.maximumResponseTokens,
   budget < minimumTokens(for: schema) {
    throw LanguageModelError.unsupportedCapability(
        .init(
            capability: .guidedGeneration,
            debugDescription: "Token budget too small to satisfy this schema."
        )
    )
}
```

### Built-in errors that any model can throw — [13:57]

```swift
// Built-in errors that any model can throw

public enum LanguageModelError: LocalizedError, CustomDebugStringConvertible {
    // Transcript grew past the model's context window. Trim entries and retry.
    case contextSizeExceeded(     )
    // Too many requests in a short window. Space them out or reduce load.
    case rateLimited(     )
    // Model declined to answer. Fall back to a message of your choosing.
    case refusal(     )
    // Safety guardrails tripped on the prompt or the response.
    case guardrailViolation(     )
    // Model lacks a feature you used, such as guided generation or tools.
    case unsupportedCapability(     )
    // Prompt contains content the model can't process (bad files, unknown formats).
    case unsupportedTranscriptContent(     )
    // A generation guide (e.g., a regex pattern) isn't supported by this model.
    case unsupportedGenerationGuide(     )
    // Prompt asked for output in a language or locale the model doesn't support.
    case unsupportedLanguageOrLocale(     )
    // Request timed out before the model produced a response.
    case timeout(     )
}
```

### Handle errors from your model executor — [14:14]

```swift
// Custom errors

public enum MyModelError: Error, LocalizedError {
    // User hit monthly token limit. Prompt upgrade or wait for reset.
    case exceededSubscriptionTierLimit
    // Model variant isn't enabled on this account.
    case modelNotProvisioned
    // Billing or policy review locked this account.
    case accountSuspended

    public var errorDescription: String? {
        switch self {
        case .exceededSubscriptionTierLimit:
            String(localized: "Your plan limit has been reached.")
        // ...
        }
    }
}
```

### Attach custom metadata to responses — [16:08]

```swift
// Attach service-specific performance metadata

let elapsed = Date().timeIntervalSince(startTime)
let tokensPerSecond = Double(tokenCount) / elapsed
let timeToFirstToken = firstTokenTime?.timeIntervalSince(startTime) ?? 0

await channel.send(.metadataUpdate([
    "tokensPerSecond": tokensPerSecond,
    "timeToFirstToken": timeToFirstToken
]))
```

### Define and use custom Transcript segments — [17:05]

```swift
// Define a custom segment
public struct AudioSegment: Transcript.CustomSegment {
    public var id: String
    public var content: URL
}

// Pass it in a prompt
let recording = AudioSegment(id: UUID().uuidString, content: URL(filePath: "/path/to/recording.m4a"))
let response = try await session.respond {
    "Where was Frank Lloyd Wright's original architecture school located?"
    recording
}

// Emit a custom segment from the executor
for try await event in stream {
    switch event {
    case .audioFileGenerated(let file):
        await channel.send(.response(action: .updateCustomSegment(
            AudioSegment(id: file.id, content: file.url)
        )))
    }
}
```

### Implement server-side tools in your model — [18:09]

```swift
// Configure server-side tools
public struct MyLanguageModel: LanguageModel {
    public struct ServerTool: Sendable {
        public static let webSearch: ServerTool = ...
    }
    public init(serverTools: [ServerTool] = []) { }
}

// Surface tool results through the channel
let client = MyServerClient(serverTools: model.serverTools)
let response = try await client.send(prompt: .init(request))
for try await chunk in response {
    switch chunk {
    case .webSearch(let webSearch):
        await channel.send(.response(action: .updateCustomSegment(
            WebSearchSegment(url: webSearch.url, content: webSearch.html)
        )))
    case .textDelta(let textDelta):
        await channel.send(.response(action: .appendText(
            textDelta.text, tokenCount: textDelta.tokenCount
        )))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/339/4/334f1ee9-4263-4c86-9b10-632f0f2edab1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/339/4/334f1ee9-4263-4c86-9b10-632f0f2edab1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/339) — developer.apple.com. Indexed for agent consumption._