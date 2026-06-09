# Build agentic app experiences with the Foundation Models framework

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-242](https://developer.apple.com/videos/play/wwdc2026/242)

Learn how to take your intelligence features further with Foundation Models framework primitives for dynamic context and agentic workflows. We’ll walk through engineering shared context, setting up privacy boundaries, and managing key value caching. Discover how to orchestrate smooth handoffs between local and server models.


**Keywords:** `ai`, `machine learning`, `xcode`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Composing dynamic sessions with instructions and profiles](https://developer.apple.com/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles.json

## Code Snippets

### DynamicInstructions — [5:04]

```swift
// DynamicInstructions

struct BrainstormFacilitator: DynamicInstructions {
    var orchestrator: CraftOrchestrator
    var body: some DynamicInstructions {
        Instructions {
            "You are a warm and friendly expert crafting brainstorm facilitator."
        }
        // Tools
        GenerateProjectTitle()
        // Conditionally include Origami knowledge
        if orchestrator.techniques.contains(.origami) {
            OrigamiExpert()
        }
    }
}
```

### DynamicProfile — [6:41]

```swift
// DynamicProfile

struct CraftProfile: LanguageModelSession.DynamicProfile {
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .brainstorming:
            Profile { BrainstormFacilitator(orchestrator: orchestrator) }
                .model(orchestrator.pccLanguageModel)
                .temperature(1)
        case .planning:
            Profile { TutorialAuthor(orchestrator: orchestrator) }
                .model(orchestrator.pccLanguageModel)
                .reasoningLevel(.deep)
        case .reviewing:
            Profile { CraftCoach() }
                .model(orchestrator.systemLanguageModel)
        }
    }
}
```

### Initialize your session with your dynamic profile — [6:43]

```swift
// Initialize your session with your dynamic profile
let session = LanguageModelSession(profile: CraftProfile(orchestrator: orchestrator))
```

### Transcript management — [8:33]

```swift
// Transcript management

struct CraftProfile: LanguageModelSession.DynamicProfile {
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .reviewing:
            Profile { CraftCoach() }
                .model(orchestrator.systemLanguageModel)
                .historyTransform { history in
                    // Update the history for your profile
                    guard let latestResponseIndex = lastResponseEntryIndex(history) else {
                        return history
                    }
                    let filteredHistory = history[0..<latestResponseIndex].filter { entry in
                        isToolCallsOrToolOutput(entry)
                    }
                    return filteredHistory + history[latestResponseIndex...]
                }
        }
    }
}
```

### Custom modifiers — [9:15]

```swift
// Custom modifiers

struct DroppingToolCallsProfileModifier: LanguageModelSession.DynamicProfileModifier {
    func body(content: Content) -> some DynamicProfile {
        content
            .historyTransform { history in
                guard let latestResponseIndex = lastResponseEntryIndex(history) else {
                    return history
                }
                let filteredHistory = history[0..<latestResponseIndex].filter { entry in
                    isToolCallsOrToolOutput(entry)
                }
                return filteredHistory + history[latestResponseIndex...]
            }
    }
}

extension LanguageModelSession.DynamicProfile {
    func droppingCompletedToolCalls() -> some DynamicProfile {
        self.modifier(DroppingToolCallsProfileModifier())
    }
}
```

### History management modifiers — [9:27]

```swift
// History management modifiers

import FoundationModelsUtilities

struct CraftProfile: LanguageModelSession.DynamicProfile {
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .reviewing:
            Profile { CraftCoach() }
                // Keep the most recent 10 entries
                // after dropping finished tool calls
                .rollingWindow(size: .entries(10))
                .droppingCompletedToolCalls()
        }
    }
}
```

### Lifecycle modifiers — [10:48]

```swift
// Lifecycle modifiers

struct CraftProfile: LanguageModelSession.DynamicProfile {
    @SessionProperty(\.history) var history
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .planning:
            Profile { TutorialAuthor(orchestrator: orchestrator) }
                .model(orchestrator.pccLanguageModel)
                .reasoningLevel(.deep)
                .onResponse {
                    // Update history
                    if history.count > 50, let responseIndex = lastResponseIndex(history) {
                        history = history[responseIndex...]
                    }
                }
        }
    }
}
```

### Declare a custom session property — [11:40]

```swift
// Session properties — declaration

extension SessionPropertyValues {
    @SessionPropertyEntry var summary: String?
}
```

### Read and write session properties in a profile — [12:24]

```swift
// Session properties

struct CraftProfile: LanguageModelSession.DynamicProfile {
    @SessionProperty(\.history) var history
    @SessionProperty(\.summary) var summary
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .planning:
            Profile {
                TutorialAuthor(orchestrator: orchestrator)
                if let summary {
                    Instructions { "Summary: \(summary)" }
                }
            }
            .onResponse {
                if history.count > 50, let responseIndex = lastResponse(history.prefix(40)) {
                    summary = try await summarize(history[0..<responseIndex])
                    history = history[responseIndex...]
                }
            }
        }
    }
}
```

### Orchestration: baton-pass — [13:02]

```swift
// Baton-pass

struct CraftProfile: LanguageModelSession.DynamicProfile {
    var orchestrator: CraftOrchestrator
    var body: some DynamicProfile {
        switch orchestrator.mode {
        case .brainstorm:
            Profile {
                BrainstormInstructions()
                BatonPassTool()
            }
            .onToolCall { orchestrator.mode = .tutorial }
            .model(orchestrator.serverModel)
        case .tutorial:
            Profile {
                TutorialInstructions()
                BatonPassTool()
            }
            .onToolCall { orchestrator.mode = .brainstorm }
            .model(orchestrator.systemModel)
        }
    }
}
```

### Orchestration: phone-a-friend — [14:14]

```swift
// Phone-a-friend

struct CraftProfile: LanguageModelSession.DynamicProfile {
    var body: some DynamicProfile {
        Profile {
            BrainstormInstructions()
            PhoneFriendTool(
                name: "generate_title",
                description: "Generate a creative project title",
                profile: TitleProfile()
            )
        }
    }
}

struct PhoneFriendTool<P: LanguageModelSession.DynamicProfile>: Tool {
    func call(arguments: GeneratedContent) async throws -> String {
        let session = LanguageModelSession(profile: profile())
        let response = try await session.respond(to: arguments)
        return response.content
    }
}
```

### The skills pattern — [15:15]

```swift
// The skills pattern

struct CraftingSkills: LanguageModelSession.DynamicInstructions {
    var activations: SkillActivations
    var body: some DynamicInstructions {
        Skills(activations: activations) {
            Skill(
                name: "origami_folds",
                description: "Details about specific types of folds",
                prompt: """
                    Valley Fold: Paper is folded toward you, creating a V-shaped crease
                    Mountain Fold: Paper is folded away from you, creating an inverted V
                    ...
                    """
            )
            Skill(...)
            Skill(...)
        }
    }
}
```

### Tool calling mode — [15:31]

```swift
// Tool calling mode

public struct ToolCallingMode: Sendable {
    public static let allowed: ToolCallingMode
    public static let disallowed: ToolCallingMode
    public static let required: ToolCallingMode
}

// Pass tool calling mode as a profile modifier
struct OrigamiExpert: LanguageModelSession.DynamicProfile {
    var body: some LanguageModelSession.DynamicProfile {
        Profile {
            Instructions("You are an origami expert")
            QueryOrigamiDatabaseTool()
            ShowDirectionsTool()
        }
        .toolCallingMode(.required)
    }
}

// Or pass it as a generation option
let response = try await session.respond(
    to: "Write out the instructions for folding a paper crane.",
    options: GenerationOptions(toolCallingMode: .required)
)
```

### Escaping a tool call loop — [16:47]

```swift
// Escaping a tool call loop

struct OrigamiExpert: LanguageModelSession.DynamicProfile {
    let state: OrigamiAppState

    var body: some LanguageModelSession.DynamicProfile {
        Profile {
            Instructions("Answer questions about how to fold origami")
            QueryOrigamiDatabaseTool()
        }
        .toolCallingMode(state.queriedDatabase ? .disallowed : .required)
        .onToolCall { state.queriedDatabase = true }
    }
}
```

### Define a tool that throws an error — [16:57]

```swift
// Define a tool that throws an error
    var output: String?

    @Generable struct Arguments {
        var answer: String
    }

    func call(arguments: Arguments) async throws -> Never {
        output = arguments.answer
        throw CancellationError()
    }
}
```

### Set the transcript error handling policy — [17:28]

```swift
// Specify transcript behavior on a profile
struct OrigamiExpert: LanguageModelSession.DynamicProfile {
    let state: OrigamiAppState

    var body: some LanguageModelSession.DynamicProfile {
        Profile {
            Instructions("Answer questions about how to fold origami")
            QueryOrigamiDatabaseTool()
        }
        .transcriptErrorHandlingPolicy(.preserveTranscript)
    }
}

// Or specify it on a session
let session = LanguageModelSession()
session.transcriptErrorHandlingPolicy = .preserveTranscript

// Policy options
extension LanguageModelSession {
    public struct TranscriptErrorHandlingPolicy: Sendable {
        // Roll the transcript back to its previous state
        public static let revertTranscript: TranscriptErrorHandlingPolicy
        // Keep the transcript in state following an error
        public static let preserveTranscript: TranscriptErrorHandlingPolicy
    }
}
```

### Transcript mutation — [17:51]

```swift
// Transcript mutation

public final class LanguageModelSession: Sendable {
    public var transcriptErrorHandlingPolicy: TranscriptErrorHandlingPolicy { get set }

    // Transcript is now settable
    public var transcript: Transcript { get set }

    // But you must not modify it during a response!
    public var isResponding: Bool { get }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/242/4/7f05515d-be1a-43a0-9962-a1f77f115666/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/242/4/7f05515d-be1a-43a0-9962-a1f77f115666/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._