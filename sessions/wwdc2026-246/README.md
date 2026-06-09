# LLM search using Core Spotlight

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-246](https://developer.apple.com/videos/play/wwdc2026/246)

Level up basic search into a retrieval-augmented system using SpotlightSearchTool and LanguageModelSession. Explore Core Spotlight integration, delegate-based hydration patterns, and how metadata quality impacts your search results. Learn how to use custom PipelineStages for tasks like sentiment analysis. Discover best practices for indexing and building flexible, context-rich search experiences in your app.

**Keywords:** `ai`, `machine learning`, `spotlight`, `spot light`, `spotlight search`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Spotlight search tool](https://developer.apple.com/documentation/CoreSpotlight/Spotlight-search-tool) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreSpotlight/Spotlight-search-tool
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreSpotlight/Spotlight-search-tool.json
- [Making your indexed content available to Foundation Models](https://developer.apple.com/documentation/CoreSpotlight/making-your-indexed-content-available-to-foundation-models) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreSpotlight/making-your-indexed-content-available-to-foundation-models
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreSpotlight/making-your-indexed-content-available-to-foundation-models.json

## Code Snippets

### Ask the model with a Foundation Models session — [0:59]

```swift
let response = try await session.respond(to: "What are some nice hikes near water?")
```

### Set up SpotlightSearchTool — [4:20]

```swift
// Set up SpotlightSearchTool
import CoreSpotlight
import FoundationModels

// In one line, the tool is ready to search your app's Core Spotlight index
let tool = SpotlightSearchTool()

// Or provide a custom configuration — e.g. search file paths in your app's sandbox
let fileTool = SpotlightSearchTool(
    configuration: .init(
        sources: [
            .files
        ]
    )
)
```

### Add SpotlightSearchTool to a session — [4:50]

```swift
// Add SpotlightSearchTool to a session
import CoreSpotlight
import FoundationModels

let tool = SpotlightSearchTool()

let session = LanguageModelSession(model: model, tools: [tool], instructions: instructions)

let response = try await session.respond(to: "What hikes have I gone on?")
```

### Implement an index delegate — [6:24]

```swift
// Implement an index delegate
import CoreSpotlight

class IndexDelegate: NSObject, CSSearchableIndexDelegate {

    // Called when the index requests searchable items for the provided identifiers
    func searchableItems(forIdentifiers identifiers: [String]) async -> [CSSearchableItem] {
        let entries = await mystore.fetchEntries(ids: identifiers)
        return entries.map { makeSearchableItem(from: $0) }
    }
}
```

### Track the query token for refresh — [7:37]

```swift
// Track the query token for refresh
import CoreSpotlight
import FoundationModels

let tool = SpotlightSearchTool()

for await reply in tool.searchResults {

    if reply.queryToken != currentToken {
        // New query — start a new display section
        currentToken = reply.queryToken
    }

    switch reply.content {
    case .items(let searchItems):
    }
}
```

### Set a dynamic guidance profile — [8:42]

```swift
// Set a dynamic guidance profile
import CoreSpotlight
import FoundationModels

let profile = SpotlightSearchTool.GuidanceProfile(
    textMatch: true,
    dates: true,
    people: false,
    attributes: [.title, .altitude, .completionDate]
)

let tool = SpotlightSearchTool(
    configuration: .init(
        guide: .init(level: .dynamic(profile))
    )
)

// On-device models have smaller context — prefer focused guidance
let focusedTool = SpotlightSearchTool(
    configuration: .init(
        guide: .init(level: .focused(.items))
    )
)
```

### Implement a ContactResolver — [9:32]

```swift
// Implement a ContactResolver
import CoreSpotlight
import FoundationModels

struct MyContactResolver: ContactResolver {

    func userIdentity() -> ResolvedContact {
        // Pull from whatever identity source your app has —
        // account profile, Contacts framework, sign-in session, etc.
        var contact = ResolvedContact(displayName: "Jane Doe")
        contact.emailAddresses = ["jane@example.com", "jdoe@work.com"]
        contact.names = ["Jane", "JD"]
        return contact
    }
}

tool.contactResolver = MyContactResolver()
```

### Define a custom stage — [11:34]

```swift
// Define a custom stage
import CoreSpotlight
import FoundationModels

@Generable
struct HappinessStage: CustomStage {
    static var name = "happiness"
    static var description = "Scores hike by how happy the author was"
    static var inputTypes: [SearchPipelineDataType] = [.items]
    static var outputTypes: [SearchPipelineDataType] = [.scoredItems]

    @Guide(description: "Minimum happiness score (0.0-1.0) to include in results")
    var threshold: Double?

    func execute(on input: SearchPipelineData) async throws -> SearchPipelineData {
        return SearchPipelineData(payload: .scoredItems(sorted))
    }
}

// Register the stage by adding it to the tool's configuration
let tool = SpotlightSearchTool(configuration: .init(
    customStages: [.happinessBoost(threshold: 0.5)])
)
```

### Handle a reply data types — [12:10]

```swift
// Handle a reply data types
import CoreSpotlight
import FoundationModels

for await reply in tool.searchResults {

    let label = reply.label
    case .items(let searchItems):
    case .scoredItems(let scored):
    case .groupedItems(let groups):
    case .count(let count):
    case .table(let table):
    case .statistic(let statistic):
    case .text(let text):
        continue
    }   
}
```

### Define an evaluation dataset with ModelSampleProtocol — [13:47]

```swift
// Evaluations
import Evaluations

struct TrailRequest: ModelSampleProtocol {

    typealias ExpectedValue = String                    // sample response
    typealias Expectation   = TrajectoryExpectation     

    var input:  ModelSampleInput
    var output: ModelSampleOutput<String, TrajectoryExpectation>

    var expectedIdentifiers: [String]
}
```

### Define the trajectory expectation — [15:06]

```swift
// Evaluations
import Evaluations

TrajectoryExpectation(
    unordered: [
        ToolExpectation("searchSpotlight", arguments: [.keyOnly(argumentName: "query")])
    ]   
)
```

### Run the evaluation test — — [15:17]

```swift
@Test("Trail search evaluation meets quality thresholds")
func trailSearchEval() async throws {

    let items = try Self.loadItems()
    let samples = try Self.loadSamples()

    try await Self.indexDelegate.indexSearchableItems(items)
    let tool = Self.makeSearchTool()

    let evaluation = TrailSearchEvaluation(
        tool: tool,
        dataset: ArrayLoader(samples: samples)
    )   

    let result = try await evaluation.run()
    let coverageMean = result.aggregateValue(.mean(of: Metric("ResultCoverage")))
    #expect(coverageMean >= 0.5, "Result coverage should be at least 50% across queries")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/246/4/b390ab9d-d231-4cf5-9d1b-e4270ef5012b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/246/4/b390ab9d-d231-4cf5-9d1b-e4270ef5012b/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._