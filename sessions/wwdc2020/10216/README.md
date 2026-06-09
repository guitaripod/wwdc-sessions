---
id: "wwdc2020-10216"
event: "wwdc2020"
year: 2020
title: "What's new in ResearchKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10216"
topics: ["Health & Fitness"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What's new in ResearchKit

**Event:** WWDC20 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10216](https://developer.apple.com/videos/play/wwdc2020/10216)

ResearchKit continues to simplify how developers build research and care apps. Explore how the latest ResearchKit updates expand the boundaries of data researchers can collect. Learn about features like enhanced onboarding, extended options for surveys, and new active tasks. Discover how Apple has partnered with the research community to leverage this framework, helping developers build game-changing apps that empower care teams and the research community.

**Keywords:** `activities`, `chart`, `graph`, `healthkit`, `study`, `task`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,048 words)

## Documentation & Resources

- [Research and Care Website](https://www.researchandcare.org) _documentation_

## Code Snippets

### instructionStep — [3:24]

```swift
let instructionStep = ORKInstructionStep(identifier: "InstructionStepIdentifier")
instructionStep.title = "Welcome!"
instructionStep.detailText = "Thank you for joining our study. Tap Next to learn more before signing up."
instructionStep.image =  UIImage(named: "health_blocks")!
```

### informedConsentInstructionStep — [4:08]

```swift
let informedConsentInstructionStep = ORKInstructionStep(identifier: "ConsentStepIdentifier")
informedConsentInstructionStep.title = "Before You Join"
informedConsentInstructionStep.image = UIImage(named: "informed_consent")!

let heartBodyItem = ORKBodyItem(text: exampleText, 
                                detailText: nil, 
                                image: UIImage(systemName: "heart.fill"), 
                                learnMoreItem: nil, 
                                bodyItemStyle: .image)

informedConsentInstructionStep.bodyItems = [heartBodyItem]
```

### webViewStep — [5:04]

```swift
let webViewStep = ORKWebViewStep(identifier: String(describing: Identifier.webViewStep), html: exampleHtml)
webViewStep.showSignatureAfterContent = true
```

### sesAnswerFormat — [7:43]

```swift
let sesAnswerFormat = ORKSESAnswerFormat(topRungText: "Optimal Health", 
                                         bottomRungText: "Poor Health")

let sesFormItem = ORKFormItem(identifier: "sesIdentifier", 
                                      text: exampleText, 
                                      answerFormat: sesAnswerFormat)
```

### scaleAnswerFormItem — [8:47]

```swift
let scaleAnswerFormat = ORKScaleAnswerFormat(maximumValue: 10, minimumValue: 1, defaultValue: 11, step: 1)
scaleAnswerFormat.shouldShowDontKnowButton = true
scaleAnswerFormat.customDontKnowButtonText = "Prefer not to answer"

let scaleAnswerFormItem = ORKFormItem(identifier: "ScaleAnswerFormItemIdentifier", 
                                      text: "What is your current pain level?", 
                                      answerFormat: scaleAnswerFormat)
```

### textAnswerQuestionStep — [9:47]

```swift
let textAnswerFormat = ORKAnswerFormat.textAnswerFormat()
textAnswerFormat.multipleLines = true
textAnswerFormat.maximumLength = 280;
textAnswerFormat.hideWordCountLabel = false
textAnswerFormat.hideClearButton = false

let textAnswerQuestionStep = ORKQuestionStep(identifier: textAnswerIdentifier),
                                             title: exampleTitle,
                                             question: exampleQuestionText,
                                             answer: textAnswerFormat)
```

### ORKReviewViewController — [11:00]

```swift
let reviewVC = ORKReviewViewController(task: taskViewController.task,
                                       result: taskViewController.result,
                                       delegate: self)
reviewVC.reviewTitle = "Review your response"
reviewVC.text = "Please take a moment to review your responses below. If you need to change any answers just tap the edit button to update your response."
```

### ORK3DModelStep — [14:30]

```swift
let usdzModelManager = ORKUSDZModelManager(usdzFileName: "toy_drummer")
usdzModelManager.allowsSelection = false
usdzModelManager.highlightColor = .yellow
usdzModelManager.enableContinueAfterSelection = false
usdzModelManager.identifiersOfObjectsToHighlight = arrayOfIdentifiers

let threeDimensionalModelStep = ORK3DModelStep(identifier: drummerModelIdentifier,
                                               modelManager: usdzModelManager)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10216/5/10085282-EADD-4030-9CAF-5F5A1D28C4E7/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10216) — developer.apple.com. Indexed for agent consumption._