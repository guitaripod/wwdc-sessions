---
id: "wwdc2026-379"
event: "wwdc2026"
year: 2026
title: "Meet Trust Insights"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/379"
topics: ["Business & Education", "Privacy & Security"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet Trust Insights

**Event:** WWDC26 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-379](https://developer.apple.com/videos/play/wwdc2026/379)

Uncover how Trust Insights can help protect people from social scams and coercion. Explore how this new framework uses privacy-preserving machine learning to detect when someone may be coached into risky actions. Find out how to integrate Trust Insights into your app, interpret its signals, and design thoughtful interventions that safeguard people while respecting their privacy.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,560 words)

## Documentation & Resources

- [Trust Insights](https://developer.apple.com/documentation/TrustInsights) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TrustInsights
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TrustInsights.json

## Code Snippets

### Generating insights — [3:01]

```swift
import TrustInsights

let request = IsLikelyBeingCoachedInsight.request(schema: .version1, modelVersion: .current)
let context = InsightEvaluator.InsightContext(operationCategory: .resourceUse,
                                              requestedEvaluations: request)

let evaluator = InsightEvaluator()
guard try await evaluator.requestAuthorization(for: context) == .authorized else { return }

let assessment = try await evaluator.requestEvaluation(context: context)
do {
    try handleAssessment(assessment)
} catch {
    // Handle error
}

assessment.reportConsumption(.usedIncreasedFriction)
```

### Handling results for IsLikelyBeingCoachedInsight — [5:37]

```swift
func handleAssessment(_ assessment: InsightEvaluation<IsLikelyBeingCoachedInsight>) throws {
	switch try assessment.insight.outcome.get() {
		case .unknown:

		case .medium:

		case .high:

		@unknown default:

	}
}
```

### Real-time consumption feedback — [7:05]

```swift
import TrustInsights

let request = IsLikelyBeingCoachedInsight.request(schema: .version1, modelVersion: .current)
let context = InsightEvaluator.InsightContext(operationCategory: .resourceUse,
                                              requestedEvaluations: request)

let evaluator = InsightEvaluator()
guard try await evaluator.requestAuthorization(for: context) == .authorized else { return }

let assessment = try await evaluator.requestEvaluation(context: context)
do {
    try handleAssessment(assessment)
} catch {
    // Handle error
}

assessment.reportConsumption(.usedIncreasedFriction)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/379/4/e12c4703-5c00-44f7-a5f8-80f6e5b7ebd5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/379/4/e12c4703-5c00-44f7-a5f8-80f6e5b7ebd5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/379) — developer.apple.com. Indexed for agent consumption._
