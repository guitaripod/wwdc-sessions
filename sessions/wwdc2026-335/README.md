# Improve your prompts by hill-climbing with Evaluations

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-335](https://developer.apple.com/videos/play/wwdc2026/335)

Learn comparative evaluation techniques to guide your prompt engineering and select the right model for your app. Explore how to baseline performance, expand your evaluation strategy, and convert results to JSON for integration with other tools. Discover when to apply different prompting strategies and how to iteratively refine prompts for best results.

**Keywords:** `ai`, `machine learning`, `testing`, `xcode`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Book Tracker: Using Evaluations to evaluate an intelligent feature](https://developer.apple.com/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.json
- [Designing effective model-as-judge evaluators](https://developer.apple.com/documentation/Evaluations/designing-effective-model-judges) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/designing-effective-model-judges
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/designing-effective-model-judges.json
- [Designing specific, measurable criteria in an evaluation suite](https://developer.apple.com/documentation/Evaluations/designing-evaluation-criteria) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Evaluations/designing-evaluation-criteria
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Evaluations/designing-evaluation-criteria.json

## Code Snippets

### The BookTaggingEvaluation — [3:54]

```swift
// MARK: - Evaluation
struct BookTaggingEvaluation: Evaluation {
    func subject(from sample: ModelSample<BookTags>) async throws -> ModelSubject<BookTags> {
        let result = try await BookTaggingService.generateTags(for: sample.promptDescription)
        return ModelSubject(value: result)
    }

    // MARK: - Dataset
    var dataset = ArrayLoader(samples:
        Book.sampleBooks.map { book in
            ModelSample(prompt: book.review, expected: BookTags(tags: book.tags))
        }
    )

    // MARK: - Evaluators & Metrics
    var tagCount = Metric("Tag Count")
    let hasGenreTag = Metric("Has Genre Tag")
    let noDuplicates = Metric("No Duplicates")

    let relevance = ScoreDimension(
        "Relevance",
        description: """
            Whether each tag describes a quality, theme, or tone of the
            book itself rather than incidental details or the reader's
            personal reactions.
            """,
        scale: .numeric([
            4: "Every tag describes the book itself",
            3: "Most tags describe the book, one picks up a reader reaction or minor detail",
            2: "Most tags are surface details or personal reactions, not book descriptors",
            1: "Tags don't meaningfully describe the book"
        ])
    )

    let usefulness = ScoreDimension(
        "Usefulness",
        description: """
            Whether tags are at the right granularity for browsing — broad
            enough that multiple books could share the tag, specific enough
            to help filter.
            """,
        scale: .numeric([
            4: "Every tag could group multiple books while still narrowing a search",
            3: "Most tags are at the right level, one is either too broad or too narrow",
            2: "Most tags are too broad to filter or too narrow to group",
            1: "Tags would not help with browsing"
        ])
    )

    var evaluators: Evaluators {
        // 1. Tag count is within the required 3–8 range
        Evaluator { _, subject in
            let count = subject.value.tags.count
            if (count >= 3 && count <= 8) {
                return tagCount.passing(rationale: "\(count) tags")
            }
            return tagCount.failing(rationale: "Got \(count) tags, expected 3–8")
        }

        // 2. At least one tag identifies the genre or literary form
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

        // 3. No duplicate tags
        Evaluator { _, subject in
            let uniqueCount = Set(subject.value.tags.map { $0.lowercased() }).count
            if (subject.value.tags.count - uniqueCount) > 0 {
                return noDuplicates.failing(rationale: "Found \(subject.value.tags.count - uniqueCount) duplicates")
            }
            return noDuplicates.passing()
        }

        // 4. Overall tag quality — groundedness, coverage, specificity
        ModelJudgeEvaluator(
            judge: .default,
            dimensions: [relevance, usefulness],
            prompt: ModelJudgePrompt(
                instructions: """
                    You are evaluating automatically generated tags for Shelf, a personal
                    book tracking app. Users write a short summary of their reading
                    experience, and the app generates tags to make their library browsable.
                    A good tag describes the book itself — its genre, themes, tone, or
                    setting. A bad tag picks up incidental details or the reader's personal
                    reactions that don't describe the book.
                    """,
                evaluationTarget: { output in output.tags.joined(separator: ", ") },
                reference: { input, _ in
                    ["Expected Tags": input.expected?.tags.joined(separator: ", ") ?? ""]
                }
            )
        )
    }

    // MARK: - Analysis
    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.group("Heuristics") { group in
            group.computeMean(of: tagCount)
            group.computeMean(of: hasGenreTag)
            group.computeMean(of: noDuplicates)
        }
        aggregator.group("Quality") { group in
            group.computeMean(of: relevance.metric)
            group.computeMean(of: usefulness.metric)
        }
    }
}
```

### Refined Relevance & Usefulness score dimensions — [4:05]

```swift
let relevance = ScoreDimension(
    "Relevance",
    description: """
        Whether each tag describes the book itself — its genre, themes,
        tone, or setting — rather than the reader's reactions, meta-
        commentary about the review, or facts about the author. A book
        can be "suspenseful" (a property of the text); a reader is
        "exhausted" (a reaction). Mis-labeling the genre is a serious failure.
        """,
    scale: .numeric([
        4: "Every tag describes the book itself",
        3: "Most tags describe the book, one picks up a reader reaction or minor detail",
        2: "Most tags are surface details or personal reactions, not book descriptors",
        1: "Tags don't meaningfully describe the book"
    ])
)

let usefulness = ScoreDimension(
    "Usefulness",
    description: """
        Whether tags work as library shelf labels — broad enough that
        several books could plausibly share the tag, specific enough to
        meaningfully narrow a search. Standard genre and theme tags work;
        made-up phrases, character names, hyper-specific descriptors, and
        overly generic words like "interesting" don't.
        """,
    scale: .numeric([
        4: "Every tag could group multiple books while still narrowing a search",
        3: "Most tags are at the right level, one is either too broad or too narrow",
        2: "Most tags are too broad to filter or too narrow to group",
        1: "Tags would not help with browsing"
    ])
)
```

### The alignment dataset, extracted to JSON — [11:56]

```swift
// Model judge alignment dataset
[
  {
    "input": "I have read this book more times than I can count…",
    "response": "[\"literary-fiction\", \"historical-fiction\", \"family-drama\", \"romantic-drama\", 
\"character-driven\", \"emotional-intensity\", \"multigenerational-narrative\", \"penned-by-a-woman\"]"
  }
  // ... add your expert ratings to each entry
]
```

### The judge alignment evaluation: dataset, subject, evaluator — [12:31]

```swift
// Model judge alignment evaluation
struct BookTagJudgmentCalibration: Evaluation {

    // MARK: Dataset — load the extracted summary/tag pairs
    static let samples: [ModelSample<BookTagJudgmentValue>] = {
        guard let url = Bundle(for: BundleToken.self).url(
                forResource: "BookTaggingEvaluation-extracted", withExtension: "json"),
              let data = try? Data(contentsOf: url) else { return [] }
        // Build ModelSample array (adding expert ratings)
        // ...
    }()

    var dataset: some Loader { ArrayLoader(samples: Self.samples) }

    // MARK: Capture Subject — tags are already generated, so just return them
    func subject(from sample: ModelSample<BookTagJudgmentValue>) async throws -> ModelSubject<BookTagJudgmentValue> {
        ModelSubject(value: sample.expected ?? BookTagJudgmentValue(
            tags: [], expertRelevanceScore: 0, expertUsefulnessScore: 0))
    }

    // MARK: Evaluators — the same model judge as the book-tags evaluation
    var evaluators: Evaluators {
        ModelJudgeEvaluator(
            judge: .default,
            dimensions: [relevance, usefulness],
            prompt: ModelJudgePrompt(
                instructions: "You are evaluating automatically generated tags for Book Tracker…",
                evaluationTarget: { output in output.tags.joined(separator: ", ") },
                reference: { input, _ in
                    ["Expected Tags": input.expected?.tags.joined(separator: ", ") ?? ""]
                }
            )
        )
    }
}
```

### Cohen's kappa aggregation — [13:00]

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    let expertRelevance = Self.samples.map { Double($0.expected?.expertRelevanceScore ?? 0) }
    let expertUsefulness = Self.samples.map { Double($0.expected?.expertUsefulnessScore ?? 0) }

    aggregator.group("Relevance") { group in
        group.computeMean(of: relevance.metric)
        group.computeStandardDeviation(of: relevance.metric)
        group.custom(of: relevance.metric, label: "Relevance Alignment Score") { judge in
            cohensKappa(ratings1: expertRelevance, ratings2: judge) ?? 0
        }
    }
    aggregator.group("Usefulness") { group in
        group.computeMean(of: usefulness.metric)
        group.computeStandardDeviation(of: usefulness.metric)
        group.custom(of: usefulness.metric, label: "Usefulness Alignment Score") { judge in
            cohensKappa(ratings1: expertUsefulness, ratings2: judge) ?? 0
        }
    }
}
```

### The judge calibration test — [13:24]

```swift
// Model judge alignment tests
@Suite("Book Tag Judge Calibration")
struct BookTagJudgmentCalibrationTests {
    static let evaluation = BookTagJudgmentCalibration()

    @Test("Judge Calibration", .evaluates(evaluation))
    func evaluateJudgeCalibration() async throws {
        let result = EvaluationContext.current.result

        let usefulnessMetric = BookTagJudgmentCalibrationTests.evaluation.usefulness.metric
        let relevanceMetric = BookTagJudgmentCalibrationTests.evaluation.relevance.metric

        #expect(result.aggregateValue(.custom(label: "Relevance: Judge vs Expert")) > 0.6)
        #expect(result.aggregateValue(.custom(label: "Usefulness: Judge vs Expert")) > 0.6)
    }
}
```

### The experimental judge prompt — [16:33]

```swift
// Experimental evaluation
struct BookTagJudgmentCalibrationExperimental: Evaluation {
    var evaluators: Evaluators {
        ModelJudgeEvaluator(
            judge: .default,
            dimensions: [relevance, usefulness],
            prompt: ModelJudgePrompt(
                instructions: """
                    You are an experienced reader and librarian evaluating tags
                    automatically generated for Book Tracker... Score the tag set on two
                    independent dimensions: Relevance and Usefulness.

                    ## What a good tag looks like
                    - Genre/form, theme/subject, tone/atmosphere, setting/era

                    ## Common failure modes
                    - Reader reactions, meta-commentary, author facts, genre contradictions
                    """,   // ← full prompt is ~40 lines; abbreviated here
                evaluationTarget: { output in output.tags.joined(separator: ", ") },
                reference: { input, _ in
                    ["Book Review": input.promptDescription,
                     "Tags Generated for the Review": input.expected?.tags.joined(separator: ", ") ?? ""]
                }
            )
        )
    }
}
```

### Few-shot worked examples in the judge prompt — [20:12]

```swift
struct ExperimentalBookTagJudgmentCalibration: Evaluation {
    var evaluators: Evaluators {
        ModelJudgeEvaluator(
            judge: SystemLanguageModel(),
            dimensions: [relevance, usefulness],
            prompt: ModelJudgePrompt(
                instructions: """
                    You are calibrating with an expert librarian who scores
                    automatically generated tags for Book Tracker... Your goal is to
                    match how the librarian scores. Use the worked examples to calibrate.

                    ## Worked examples
                    ### Example A — clean fit (Pride and Prejudice)
                    Tags: romance, historical-fiction, love, redemption, passion
                    Librarian: Relevance 4, Usefulness 4

                    ### Example E — flat genre contradiction (Frankenstein)
                    Tags: horror, science-fiction, ... self-help, self-improvement
                    Librarian: Relevance 2, Usefulness 3
                    ... (6 examples A–F; keep the set small to avoid overfitting)
                    """,   // ← full prompt is ~60 lines; abbreviated here
                evaluationTarget: { output in output.tags.joined(separator: ", ") },
                reference: { input, _ in
                    ["Book Review": input.promptDescription,
                     "Tags Generated for the Review": input.expected?.tags.joined(separator: ", ") ?? ""]
                }
            )
        )
    }
}

9. The BookLookupTool — slides 166–167
```

### The BookLookupTool — [22:03]

```swift
// Book Information Lookup Tool
struct BookLookupTool: Tool {
    let name = "lookupBook"
    let description = "Looks up the title and author of a book given distinguishing details — such as character names, 
settings, quoted lines, or notable plot points — extracted from a reader's review."

    @Generable
    struct Arguments {
        @Guide(description: "Distinguishing details from the review that identify the book, such as character names, 
settings, quoted lines, or notable plot points.")
        var details: String
    }

    @Generable
    struct Output {
        @Guide(description: "The title of the identified book, or an empty string if no match was found.")
        var title: String

        @Guide(description: "The author of the identified book, or an empty string if no match was found.")
        var author: String
    }

    func call(arguments: Arguments) async throws -> Output {
        let needles = arguments.details
            .lowercased()
            .split(whereSeparator: { !$0.isLetter && !$0.isNumber })
            .map(String.init)
            .filter { $0.count >= 4 }

        let best = Book.sampleBooks
            .map { book -> (book: Book, score: Int) in
                let review = book.review.lowercased()
                let score = needles.reduce(0) { partial, needle in
                    partial + (review.contains(needle) ? 1 : 0)
                }
                return (book, score)
            }
            .max(by: { $0.score < $1.score })

        guard let match = best, match.score > 0 else {
            return Output(title: "", author: "")
        }
        return Output(title: match.book.title, author: match.book.author)
    }
}
```

### BookTaggingService with a tools parameter — [22:36]

```swift
// Book Tagging Service
struct BookTaggingService {
    static func generateTags(for review: String, tools: [any Tool] = []) async throws -> BookTags {
        let prompt = tagsPrompt(review: review)
        let session = LanguageModelSession(
            model: SystemLanguageModel(guardrails: .permissiveContentTransformations),
            tools: tools,
            instructions: instructions
        )
        let response = try await session.respond(to: prompt, generating: BookTags.self)
        return response.content
    }
}
```

### Evaluation with the lookup tool — [22:57]

```swift
// Evaluation of tags with tool
struct BookTaggingWithLookupEvaluation: Evaluation {
    func subject(from sample: ModelSample<BookTags>) async throws -> ModelSubject<BookTags> {
        let result = try await BookTaggingService.generateTags(
            for: sample.promptDescription,
            tools: [BookLookupTool()]
        )
        return ModelSubject(value: result)
    }
    // ... same dataset, evaluators, and aggregation as BookTaggingEvaluation
}
```

### Compare with/without the tool in one suite — [23:09]

```swift
@Suite("Book Tag Evaluations")
struct BookTagEvaluationTests {
    static let evaluation = BookTaggingEvaluation()
    static let lookupEvaluation = BookTaggingWithLookupEvaluation()

    @Test("Book Tag Evaluations", .evaluates(evaluation, info: evaluationInfo))
    func evaluateBookTagging() async throws {
        let result = EvaluationContext.current.result
        let rangeMetric = BookTagEvaluationTests.evaluation.tagCount
        let dupeMetric = BookTagEvaluationTests.evaluation.noDuplicates
        #expect(result.aggregateValue(.mean(of: rangeMetric)) >= 0.8)
        #expect(result.aggregateValue(.mean(of: dupeMetric)) == 1)
    }

    @Test("Book Tag Evaluations (with BookLookupTool)", .evaluates(lookupEvaluation, info: lookupEvaluationInfo))
    func evaluateBookTaggingWithLookup() async throws {
        let result = EvaluationContext.current.result
        let rangeMetric = BookTagEvaluationTests.lookupEvaluation.tagCount
        let dupeMetric = BookTagEvaluationTests.lookupEvaluation.noDuplicates
        #expect(result.aggregateValue(.mean(of: rangeMetric)) >= 0.8)
        #expect(result.aggregateValue(.mean(of: dupeMetric)) == 1)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/335/4/a464d330-6aa2-456d-9a07-eae997aef08c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/335/4/a464d330-6aa2-456d-9a07-eae997aef08c/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._