# Secure your app: mitigate risks to agentic features

**Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-347](https://developer.apple.com/videos/play/wwdc2026/347)

Explore how to evaluate threats from indirect prompt injection, such as data exfiltration and unintended actions. Discover system safeguards and security best practices for using App Intents and the Foundation Models framework, including mitigations such as user confirmations, secure prompt design, and authentication.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Security Overview](https://developer.apple.com/security/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/security/

## Code Snippets

### Tools — [12:50]

```swift
// Tools

struct OrderTeaTool: Tool {
  let name = "orderTeaTool"
  let description: String = "Orders a particular quantity of a tea from the store."
  // Arguments
  // Implementation
}

struct PostAndFetchPublicFeedTool: Tool {
  let name = "postAndFetchPublicFeedTool"
  let description: String = "Posts a message to the public feed.”
  // Arguments
  // Implementation
}
```

### Profile — [13:13]

```swift
// Profile

class LooseLeafAgent {
  struct DefaultProfile: LanguageModelSession.DynamicProfile {
    var body: some DynamicProfile {
      Profile {
        Instructions("You are a helpful, tea-loving assistant ... ")

        OrderTeaTool()
        PostAndFetchPublicFeedTool()
      }
      .model(SystemLanguageModel())
    }
  }
}
```

### Session — [13:28]

```swift
// Session 

class LooseLeafAgent {
  struct DefaultProfile: LanguageModelSession.DynamicProfile {
    var body: some DynamicProfile {
      Profile {
        Instructions("You are a helpful, tea-loving assistant ... ")

        OrderTeaTool()
        PostAndFetchPublicFeedTool()
      }
      .model(SystemLanguageModel())
    }
  }

  let session: LanguageModelSession

  public init() {
    self.session = LanguageModelSession(profile: DefaultProfile())
  }
}
```

### Confirmation via onToolCall — [14:33]

```swift
// Confirmation via onToolCall

var body: some DynamicProfile {
  Profile {
    Instructions("You are a helpful, tea-loving assistant ... ")

    OrderTeaTool() // Financial impact; risky tool.
    // Other Tools
  }

  .onToolCall { call in
    guard call.toolName == "orderTeaTool" else {
      return
    }
    guard ConfirmationAction.confirmWithUser() else {
      throw LooseLeafError.userConfirmationDenied
    }
  }
}
```

### Spotlighting via historyTransform — [15:56]

```swift
// Spotlighting via historyTransform

var body: some DynamicProfile {
  Profile {
    Instructions("You are a helpful, tea-loving assistant ... ")

    PostAndFetchPublicFeedTool() // Returns untrusted data; requires spotlighting
    // Other Tools
  }

  .historyTransform {γentries in
    entries.map { entry in
      guard case .toolOutput(var toolOutput) = entry,
        toolOutput.toolName == "postAndFetchPublicFeedTool"
      else {
        return entry
      }
    }
    toolOutput.segments = toolOutput.segments.map { segment in
      delimit(segment: segment,
              startDelimiter: "<<UNTRUSTED>>",
              endDelimiter: "<</UNTRUSTED>>")
    }
    return .toolOutput(toolOutput)
  }
}

func delimit(segment: Transcript.Segment,
             startDelimiter: String,
             endDelimiter: String) -> Transcript.Segment
```

### Redaction via historyTransform — [16:48]

```swift
// Redaction via historyTransform

var body: some DynamicProfile {
  Profile {
    Instructions("You are a helpful, tea-loving assistant ... ")

    PostAndFetchPublicFeedTool() // Returns untrusted data; requires spotlighting
    // Other Tools
  }

  .historyTransform {γentries in
    entries.map { entry in
      guard case .toolOutput(var toolOutput) = entry,
        toolOutput.toolName == "postAndFetchPublicFeedTool"
      else {
        return entry
      }
    }
    toolOutput.segments = toolOutput.segments.map { segment in
      redactPII(segment: segment,
                placeHolder: "[REDACTED]")
    }
    return .toolOutput(toolOutput)
  }
}

func redactPII(segment: Transcript.Segment,
               placeHolder: String) -> Transcript.Segment
```

### Intent authentication policy — [23:08]

```swift
// Intent authentication policy

struct DeletePhotoIntent: DeleteIntent {
    var entities: [LooseLeafPhoto]

    static var authenticationPolicy: IntentAuthenticationPolicy = .requiresAuthentication

    func perform() async throws -> some IntentResult {
        // Implementation
    }
}
```

### Schema authentication policy — [23:27]

```swift
// Schema authentication policy

@AppIntent(schema: .photos.deleteAssets)
struct DeletePhotoIntent {
    var entities: [LooseLeafPhoto]

    // Example: Schema default authentication policy is .requiresAuthentication

    func perform() async throws -> some IntentResult {
        // Implementation
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/347/4/07cdbfeb-280a-49e3-aeba-c18fbb0d32b4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/347/4/07cdbfeb-280a-49e3-aeba-c18fbb0d32b4/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._