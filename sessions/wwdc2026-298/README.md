# Meet the Evaluations framework

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-298](https://developer.apple.com/videos/play/wwdc2026/298)

Learn how to evaluate model-driven experiences using the Evaluations framework. In a probabilistic world, unit tests alone won’t suffice. Discover how to define metrics, automatically grade outputs, and aggregate statistics to ensure your AI-powered features perform reliably across Apple’s platforms.

**Keywords:** `ai`, `machine learning`, `testing`, `xcode`, `xctest`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Book Tracker: Using Evaluations to evaluate an intelligent feature](https://developer.apple.com/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.json
- [Designing datasets to test your feature](https://developer.apple.com/documentation/Evaluations/designing-evaluation-datasets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/designing-evaluation-datasets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/designing-evaluation-datasets.json
- [Designing effective evaluations](https://developer.apple.com/documentation/Evaluations/designing-effective-evaluations) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/designing-effective-evaluations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/designing-effective-evaluations.json
- [Evaluating language model responses](https://developer.apple.com/documentation/Evaluations/evaluating-language-model-responses) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/evaluating-language-model-responses
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/evaluating-language-model-responses.json

## Code Snippets

### Define an Evaluation — [4:54]

```swift
// Evaluations
import Evaluations

struct BookTaggingEvaluation: Evaluation {

}
```

### Run with Swift Testing and an optimization target — [8:02]

```swift
// Optimization Target
@Test("Book Tag Evaluations", .evaluates(evaluation, info: evaluationInfo))
func evaluateBookTagging() async throws {
    let result = EvaluationContext.current.result

    let rangeMetric = BookTagEvaluationTests.evaluation.tagCount
    #expect(result.aggregateValue(.mean(of: rangeMetric)) >= 0.8)
}
```

### Constrain output with a Generable @Guide — [10:09]

```swift
// BookTags.swift
@Generable
struct BookTags: Codable {
    @Guide(description: "Descriptive tags capturing themes, genres, moods, and topics from the summary", .count(3...8))
    var tags: [String]
} snippet.
```

### Define the dataset with ModelSample — [11:15]

```swift
// BookTaggingEvaluation
var dataset = ArrayLoader(samples: [
    ModelSample(prompt: "okay I am OBSESSED and I need everyone to read this RIGHT NOW...",
                expected: BookTags(tags: ["classic", "romance", "wit", "regency"])),

    ModelSample(prompt: "Read this in one sitting between midnight and 4am and I cannot...",
                expected: BookTags(tags: ["classic", "gothic", "horror", "vampire", "suspense"])),
])

// Or load your whole library:
var dataset = ArrayLoader(samples:
    Book.sampleBooks.map { book in
        ModelSample(prompt: book.review, expected: BookTags(tags: book.tags))
    }
)
```

### Synthesize more samples with a SampleGenerator — [12:53]

```swift
// Synthesizing more inputs
let samples: [ModelSample<String>] = [
    ModelSample(prompt: "The largest planet in our solar system...", expected: "Jupiter."),
    ModelSample(prompt: "The capital of Thailand...", expected: "Bangkok."),
    ModelSample(prompt: "Swift is...", expected: "a powerful programming language."),
    ModelSample(prompt: "All those moments will be lost in time...", expected: "Like tears in rain.")
]

for try await sample in samples.makeSamples(
    """
    Generate diverse sentence completions about the listed topics:
      - The Solar System
      - World Capitals 
    """,
    targetCount: 1000) {
        samples.append(sample)
}
```

### More evaluators: word count and genre — [14:02]

```swift
let wordCount = Metric("WordCount")

Evaluator { _, subject in
    for tag in subject.value.tags {
        if tag.contains(" ") {
            return wordCount.failing(rationale: "Tag \(tag) contains multiple words")
        }
    }
    return wordCount.passing()
}

let hasGenreTag = Metric("HasGenreTag")

Evaluator { _, subject in
    let tags = subject.value.tags.map { $0.lowercased() }
    let knownGenres = await BookTaggingService.knownGenres
    for tag in tags {
        if knownGenres.contains(tag) {
            return hasGenreTag.passing(rationale: "Matched \(tag)")
        }
    }
    return hasGenreTag.failing() 
}
```

### Define a Metric and Evaluator — [14:03]

```swift
let tagCount = Metric("TagCount")

var evaluators: Evaluators {

    // Tag count is within the required 3–8 range
    Evaluator { _, subject in 
        let count = subject.value.tags.count
        if (count >= 3 && count <= 8) {
            return tagCount.passing(rationale: "\(count) tags")
        } 
        return tagCount.failing(rationale: "Got \(count) tags, expected 3–8")
    }
}
```

### Aggregate metrics across samples — [14:27]

```swift
let tagCount = Metric("TagCount")
let tagTotal = Metric("TagTotal")

func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    aggregator.computeMean(of: tagCount)
    aggregator.group("Distribution of Tag Totals") { aggregator in
        aggregator.computeStandardDeviation(of: tagTotal)
        aggregator.computeMean(of: tagTotal)
        aggregator.computeVariance(of: tagTotal)
    }
}
```

### Iterate the feature's instructions (hill-climbing) — [15:33]

```swift
// BookTaggingService.swift
let instructions = Instructions {
    """
    You are a librarian and literary analyst. Given a reader's
    freeform summary of a book they read — describing their
    thoughts, feelings, and what stood out — generate a set of
    descriptive tags reflected in the summary.

    Rules:
     - Return between 3 and 8 tags.
     - Tags should be lowercase, concise (single word or hyphenated), and descriptive.
     - Tags should include the book's genre, chosen from the included list of known genres.

    Known Genres:
     - \(Self.knownGenres.joined(separator: ", "))
    """
}
```

### Build a model judge — [18:53]

```swift
ModelJudgeEvaluator(
    "TagQuality",
    scale: .numeric([
        4: "Tags are relevant and helpful for browsing",
        3: "Mostly relevant, one tag too vague or generic",
        2: "Several tags are wrong or generic",
        1: "Unhelpful or irrelevant"
    ]),   
    judge: PrivateCloudComputeLanguageModel()
)
```

### Split into score dimensions — [22:17]

```swift
// BookTaggingEvaluation.swift
ScoreDimension(
    "Relevance",
    description: """
        Whether each tag describes a quality, theme, or tone
        of the book itself rather than incidental details or
        the reader's personal reactions.
        """,
    scale: .numeric([
        4: "Every tag describes the book itself",
        3: "Most tags describe the book",
        2: "Some tags describe personal reactions",
        1: "Tags don't meaningfully describe the book"
    ])    
)
// Define `usefulness` the same way as a second ScoreDimension.
```

### Add dimensions to the judge — [22:32]

```swift
// BookTaggingEvaluation.swift
var evaluators: Evaluators {

    Evaluator {  }  

    Evaluator {  }

    Evaluator {  }

    ModelJudgeEvaluator(
        judge: PrivateCloudComputeLanguageModel(),
        dimensions: [relevance, usefulness]
    )
}
```

### Add app context with a ModelJudgePrompt — [23:17]

```swift
// BookTaggingEvaluation.swift
ModelJudgeEvaluator(
    judge: PrivateCloudComputeLanguageModel(),
    dimensions: [relevance, usefulness],
    prompt: ModelJudgePrompt( 
        instructions: """
            You are evaluating tags generated for a personal book-tracking app where users
            organize their library by browsing and filtering tags.
            """,
        evaluationTarget: { value in
            "\(value.tags.count) Generated tags: " + value.tags.joined(separator: ", ")
        },
        reference: { input, _ in 
            let expectedTags = input.expected?.tags.joined(separator: ", ")
            return ["Expected Tags": expectedTags ?? "No expected tags defined"]
        }
    )
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/298/5/0ffb7161-1edb-4e6f-872d-55be82c4402d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/298/5/0ffb7161-1edb-4e6f-872d-55be82c4402d/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._