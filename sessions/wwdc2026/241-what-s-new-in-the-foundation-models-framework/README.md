---
id: "wwdc2026-241"
event: "wwdc2026"
year: 2026
title: "What’s new in the Foundation Models framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/241"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# What’s new in the Foundation Models framework

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-241](https://developer.apple.com/videos/play/wwdc2026/241)

Explore what’s new in the Foundation Models framework. Learn how to access Private Cloud Compute, integrate third-party and open source models, and work with vision capabilities. Discover context management APIs, built-in semantic search, and powerful primitives for creating agentic experiences in your apps.

**Keywords:** `ai`, `machine learning`, `models`, `prompt`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,697 words)

## Documentation & Resources

- [Expanding generation with tool calling](https://developer.apple.com/documentation/FoundationModels/expanding-generation-with-tool-calling) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/expanding-generation-with-tool-calling
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/expanding-generation-with-tool-calling.json
- [Analyzing images with multimodal prompting](https://developer.apple.com/documentation/FoundationModels/analyzing-images-with-multimodal-prompting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/analyzing-images-with-multimodal-prompting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/analyzing-images-with-multimodal-prompting.json
- [Composing dynamic sessions with instructions and profiles](https://developer.apple.com/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/composing-dynamic-sessions-with-instructions-and-profiles.json
- [Adding server-side intelligence with Private Cloud Compute](https://developer.apple.com/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute.json

## Code Snippets

### Context size and token counting — [2:46]

```swift
// Context size and token counting

  let model = SystemLanguageModel()
  print(model.contextSize)
  // 8192

  let count = try await model.tokenCount(for: "What are the Japanese characters for origami?")
  print(count)
```

### Attachable image types — [3:52]

```swift
// Insert c// Attachable image types

  let response = try await session.respond {
      "What animal is this?"
      Attachment(UIImage(...))
  }ode snippet.
```

### Inspecting usage — [8:45]

```swift
// Inspecting usage

  let response = try await session.respond(
      to: "Recommend a craft that doesn't require scissors.",
      contextOptions: ContextOptions(reasoningLevel: .light)
  )

  print(response.usage.input.totalTokenCount)
  print(response.usage.input.cachedTokenCount)

  print(response.usage.output.totalTokenCount)
  print(response.usage.output.reasoningTokenCount)
```

### Routing between craft analysis and brainstorm — [11:55]

```swift
// Routing between craft analysis and brainstorm

  @Observable
  final class AppStates {
      var mode: Mode
  }

  let appStates: AppStates
  var session: LanguageModelSession?

  func updateSession() {
      let originalTranscript = session?.transcript.dropFirstInstructions() ?? Transcript()

      // Create a new session with new instructions and tools
      switch appStates.mode {
      case .craftAnalysis:
          session = LanguageModelSession(
              tools: [
                  RecordImageAnalysisTool(),
                  SwitchModeTool(states: appStates)
              ],
              instructions: "Analyze the user's craft project...",
              transcript: originalTranscript
          )
      case .brainstorm:
          session = LanguageModelSession(
              tools: [
                  RecordBrainstormTool(),
              ],
              instructions: "Brainstorm some ideas...",
              transcript: originalTranscript
          )
      }
  }

  struct SwitchModeTool: Tool {
      let description = "Switch to a different mode."
      let states: AppStates

      @Generable
      struct Arguments {
          let mode: Mode
      }

      func call(arguments: Arguments) async throws -> some PromptRepresentable {
          appStates.mode = arguments.mode
          return "Successfully switched to \(arguments.mode)."
      }
  }

  // If mode changes, update the session
  withObservationTracking {
      appStates.mode
  } onChange: {
      updateSession()
  }
```

### Describing the profile for craft app — [12:42]

```swift
// Describing the profile for craft app

  struct CraftProfile: LanguageModelSession.DynamicProfile {
      var body: some DynamicProfile {
          Profile {
              Instructions {
                  """
                  You are an expert crafting assistant. \
                  Record craft project image analyses   \
                  using the recordImageAnalysis tool.
                  """
              }
              RecordImageAnalysisTool()
          }
      }
  }

  let session = LanguageModelSession(
      profile: CraftProfile()
  )
```

### Describing the profile for craft app — [14:36]

```swift
// Describing the profile for craft app

  struct CraftProfile: LanguageModelSession.DynamicProfile {
      let states: CraftProjectStates

      var body: some DynamicProfile {
          switch states.mode {
          case .craftAnalysis:
              Profile {
                  Instructions { /* ... */ }
                  RecordImageAnalysisTool()
                  SwitchModeTool(states: states)
              }
          case .brainstorm:
              Profile {
                  Instructions { /* ... */ }
                  BrainstormRecordTool()
              }
              .model(states.privateCloudCompute)
              .reasoningLevel(.deep)
          }
      }
  }
```

### Foundation Models SDK for Python — [18:29]

```swift
# Foundation Models SDK for Python

  import apple_fm_sdk as fm

  model = fm.SystemLanguageModel()

  # Check the model's availability
  is_available, reason = model.is_available()

  if is_available:

      # Create a session
      session = fm.LanguageModelSession(model=model)

      # Generate a response
      response = await session.respond(prompt="Hello!")
      print(response)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/241/6/900558cb-1997-490a-9aac-2461b209e578/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/241/6/900558cb-1997-490a-9aac-2461b209e578/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/241) — developer.apple.com. Indexed for agent consumption._
