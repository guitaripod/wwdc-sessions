# Create robust evaluations for agentic apps

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-299](https://developer.apple.com/videos/play/wwdc2026/299)

Learn how to leverage advanced features of the Evaluations framework to build robust evaluations for your app. Explore evaluating flows with tool calling and dynamic conditions, and how to define what correct behavior means for your use case. Discover how to generate synthetic data, use judges effectively, and validate your datasets for reliable results.


**Keywords:** `ai`, `machine learning`, `testing`, `xcode`, `xctest`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Book Tracker: Using Evaluations to evaluate an intelligent feature](https://developer.apple.com/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.json
- [Generating synthetic datasets](https://developer.apple.com/documentation/Evaluations/generating-synthetic-evaluation-datasets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/generating-synthetic-evaluation-datasets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/generating-synthetic-evaluation-datasets.json
- [Evaluating tool-calling behavior](https://developer.apple.com/documentation/Evaluations/evaluating-tool-calling-behavior) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/evaluating-tool-calling-behavior
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/evaluating-tool-calling-behavior.json
- [Scoring with model-as-judge evaluators](https://developer.apple.com/documentation/Evaluations/scoring-with-model-as-judge-evaluators) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/scoring-with-model-as-judge-evaluators
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/scoring-with-model-as-judge-evaluators.json

## Code Snippets

### Generate synthetic data with makeSamples — [5:16]

```swift
// Synthetic data
let prompt = Prompt("""
    Generate diverse range of book reviews and corresponding tags.
    Cover a wide range of genres, time periods, cultures, and
    reader personas. Do not repeat books already in the dataset.
    """)

let dataset = Book.sampleBooks.map { book in
    ModelSample(prompt: book.review, expected: BookTags(tags: book.tags))
}

let targetCount = 100
var expandedDataset = dataset

for try await sample in dataset.makeSamples(prompt, targetCount: targetCount) {
    expandedDataset.append(sample)
    print("Generated \(expandedDataset.count) samples so far.")
}

2. Configure a custom SampleGenerator — slides 30–43

// Define your own configuration
let generator = SampleGenerator<ModelSample<BookTags>>(
    prompt,
    samples: dataset,
    targetCount: targetCount,
    sessionProvider: {
        LanguageModelSession( 
            model: PrivateCloudComputeLanguageModel(),
            instructions: """
                You are a synthetic data generator for a book-tracking app's evaluation suite.
                Your job is to produce realistic, diverse book entries that will stress-test
                a tagging system.

                Rules:
                - Review must be at least 100 characters long.
                - Review should cover a mix of genre, mood/tone, and themes.
                - Reviews should vary in length.
                - Create between 3 and 8 tags.
                - Tags must be lowercase.
                """ 
        )
    }
)
```

### Configure a custom SampleGenerator — [5:53]

```swift
// Define your own configuration
let generator = SampleGenerator<ModelSample<BookTags>>(
    prompt,
    samples: dataset,
    targetCount: targetCount,
    sessionProvider: {
        LanguageModelSession( 
            model: PrivateCloudComputeLanguageModel(),
            instructions: """
                You are a synthetic data generator for a book-tracking app's evaluation suite.
                Your job is to produce realistic, diverse book entries that will stress-test
                a tagging system.

                Rules:
                - Review must be at least 100 characters long.
                - Review should cover a mix of genre, mood/tone, and themes.
                - Reviews should vary in length.
                - Create between 3 and 8 tags.
                - Tags must be lowercase.
                """ 
        )
    }
)
```

### Validate generated samples — [10:37]

```swift
// Define validation metrics
validator: { sample in
    guard let book = sample.expected else { return false }

    // Review must be at least 100 characters
    guard sample.promptDescription.count >= 100 else { return false }

    // Must have between 3 and 8 tags
    guard (3...8).contains(book.tags.count) else { return false }

    // All tags must be lowercase
    guard book.tags.allSatisfy({ $0 == $0.lowercased() }) else { return false }

    return true
}
```

### Access valid and invalid results — [10:58]

```swift
// Accessing results
for try await sample in generator.run() {
    // During iteration
    expandedDataset.append(sample)
}

// After iteration
let allSamples = await generator.samples
let invalidSamples = await generator.invalidSamples

print("Generated \(allSamples.count) new samples. Total: \(expandedDataset.count)")
```

### Define a tool's Generable argument — [15:30]

```swift
@Generable
struct SearchBooksArguments {
    @Guide(description: "A freeform search term to match against titles, reviews, or tags")
    var query: String?

    @Guide(description: "Filter results to books with this specific tag")
    var tag: String?

    @Guide(description: "Filter results by mood")
    var mood: String?

    @Guide(description: "Filter results by genre")
    var genre: String?

    @Guide(description: "Maximum number of results to return. Defaults to 5.")
    var limit: Int? 
}
```

### A basic trajectory expectation — [16:37]

```swift
// "Find books tagged gothic"
TrajectoryExpectation(
    unordered: [
        ToolExpectation(
            "searchBooks",
            arguments: [
                .exact(argumentName: "tag", value: .string("gothic"))
            ]
        )
    ]
)
```

### Match arguments by intent (naturalLanguage) — [17:07]

```swift
// "Find something cheerful"
TrajectoryExpectation(
    "searchBooks",
    arguments: [
        .naturalLanguage(
            argumentName: "mood",
            criteria: "Should relate to uplifting, hopeful, or positive feelings"
        )
    ]
)
Other matchers available: .contains, .oneOf, .pattern, .range, and more.
```

### Expect tool calls in order — [17:34]

```swift
// "Find gothic books and show details on the first"
TrajectoryExpectation(
    ordered: [
        ToolExpectation(
            "searchBooks",
            arguments: [
                .exact(argumentName: "tag", value: .string("gothic"))
            ]
        ),
        ToolExpectation(
            "getBookDetails",
            arguments: [
                .keyOnly(argumentName: "bookId")
            ]
        )
    ]
)
```

### Disallow specific tool calls — [17:55]

```swift
// "Show only sci-fi books. Don't look for similar ones."
TrajectoryExpectation(
    unordered: [
        ToolExpectation(
            "searchBooks",
            arguments: [
                .naturalLanguage(
                    argumentName: "genre",
                    criteria: "Should refer to science fiction")
            ]
        )
    ],
    disallowed: [
        ToolExpectation("findSimilarBooks")
    ]
)
```

### Build a tool call evaluation — [18:14]

```swift
// Tool call evaluations
let samples = SampleArrayLoader(samples: [
    ModelSample(
        prompt: "Find all the books tagged with 'gothic'.",
        instructions: "Help the user explore their book collection.",
        expectations: TrajectoryExpectation(  )
    )
])

struct BookLibraryToolCallEval: Evaluation {
    var dataset = samples

    let pass = Metric("All Passed")
    let percent = Metric("Percentage Passed")

    var evaluators: Evaluators { 
        ToolCallEvaluator(allPass: pass, percentagePass: percent)
    }
}
```

### Synthesize tool-evaluation samples — [19:20]

```swift
// Tool call evaluations
let prompt = Prompt("""
    Generate diverse user queries for a personal book library assistant.
    Each sample needs a prompt (what the user says), and a trajectory
    expectation describing which tools should be called and in what order.
    """)

let instructions = """
    AVAILABLE TOOLS:
    - searchBooks(query?, tag?, mood?, genre?, limit?): search the library
    - getBookDetails(bookId): full details for one book
    - findSimilarBooks(bookId, maxResults?): find books sharing tags
    ORDER REQUIREMENTS:
    - searchBooks must comes before getBookDetails or findSimilarBooks
    - Use TrajectoryExpectation(ordered:) when sequence matters, else (unordered:)
    USE THESE ARGUMENT MATCHERS:
    - .exact for precise values, .naturalLanguage for fuzzy matching
    - .keyOnly when any value is acceptable, .range for numeric constraints
    - .contains/.hasPrefix/.hasSuffix for partial string matching
    """
```

### Validate tool-evaluation samples — [19:51]

```swift
// Tool call evaluations
validator: { sample in
    // Must have expectations defined
    guard sample.output.expectations != nil else { return false }

    let expectations = sample.output.expectations!

    // Must reference at least one tool
    let totalExpectations = expectations.ordered.count + expectations.unordered.count
    guard totalExpectations > 0 else { return false }

    // All tool names must be from the valid set
    let validTools: Set<String> = ["searchBooks", "getBookDetails", "findSimilarBooks"]
    let allExpectations = expectations.ordered + expectations.unordered + expectations.disallowed
    for expectation in allExpectations {
        guard validTools.contains(expectation.name) else { return false }
    }

    return true
}

---
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/299/4/ef9fbc06-fc78-4896-9848-0f0fe2e75fb9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/299/4/ef9fbc06-fc78-4896-9848-0f0fe2e75fb9/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._