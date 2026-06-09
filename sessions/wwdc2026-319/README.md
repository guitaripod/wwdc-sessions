# Build with the new Apple Foundation Model on Private Cloud Compute

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-319](https://developer.apple.com/videos/play/wwdc2026/319)

Private Cloud Compute lets you access powerful, frontier-class models while protecting user privacy. Explore how it works and how to access it using the Foundation Models framework. Discover best practices for checking availability and handling graceful fallbacks in your apps.

**Keywords:** `ai`, `machine learning`, `xcode`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Adding server-side intelligence with Private Cloud Compute](https://developer.apple.com/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/adding-server-side-intelligence-with-private-cloud-compute.json

## Code Snippets

### Prompt the on-device model — [2:49]

```swift
import FoundationModels

let session = LanguageModelSession()
let response = try await session.respond(to: "Summarize this article: \(article)")
```

### Switch to the PCC server model (one-line change) — [3:02]

```swift
import FoundationModels

let session = LanguageModelSession(
    model: PrivateCloudComputeLanguageModel()
)
let response = try await session.respond(to: "Summarize this article: \(article)")
```

### Structured output and tools work the same — [3:25]

```swift
import FoundationModels

@Generable
struct ArticleSummary {
    let oneLineSummary: String
    let keyPoints: [String]
}

struct FindRelatedArticlesTool: Tool {

}

let session = LanguageModelSession(
    model: PrivateCloudComputeLanguageModel(),
    tools: [FindRelatedArticlesTool.self]
)

let response = try await session.respond(
    to: "Summarize this article: \(article)",
    generating: ArticleSummary.self
)
```

### Check availability — [3:51]

```swift
import FoundationModels

struct ArticleSummarizationView: View {
    private var model = PrivateCloudComputeLanguageModel()

    var body: some View {
        if model.isAvailable {
            // Show UI for making request
        } else {
            // Fall back
        }
    }
}
```

### Set a reasoning level — [5:26]

```swift
let response = try await session.respond(
    to: prompt,
    contextOptions: ContextOptions(reasoningLevel: .light)
)
// Reasoning levels: .light, .moderate, .deep
```

### Read the context size — [5:58]

```swift
SystemLanguageModel().contextSize
// 4096 on 26.0
// 8192 on 27.0 (newer devices)

PrivateCloudComputeLanguageModel().contextSize
// 32768
```

### Handle usage limits — [9:41]

```swift
struct ArticleSummarizationView: View {
    private var model = PrivateCloudComputeLanguageModel()

    var body: some View {
        if case .belowLimit(let info) = model.quotaUsage.status {
            if info.isApproachingLimit {
                Text("Nearing usage limit.")
                    .foregroundStyle(Color.orange)
            }
        }
        if model.quotaUsage.isLimitReached {
            Text("Usage limit exceeded.")
                .foregroundStyle(Color.red)
        }
        if let suggestion = model.quotaUsage.limitIncreaseSuggestion {
            Button("Show options") {
                suggestion.show()
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/319/4/1a3ac4f6-73d2-4a24-9e5d-0cfd56564f42/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/319/4/1a3ac4f6-73d2-4a24-9e5d-0cfd56564f42/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._