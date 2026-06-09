---
id: "wwdc2020-10672"
event: "wwdc2020"
year: 2020
title: "What's new in ClassKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10672"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in ClassKit

**Event:** WWDC20 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10672](https://developer.apple.com/videos/play/wwdc2020/10672)

The ClassKit framework helps you surface educational activities within your app to teachers through the Schoolwork app. Discover how to provide a richer assignment experience for students and teachers through enhanced metadata properties and progress reporting. We’ll also show you how the new ClassKit Catalog APIs decouple management of your content from that of your app and improve overall discoverability.

**Keywords:** `classroom`, `education`, `educators`, `school`, `testing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,542 words)

## Documentation & Resources

- [ClassKit](https://developer.apple.com/documentation/ClassKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClassKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClassKit.json

## Code Snippets

### Add Thumbnail and Summary to Quiz Context — [6:25]

```swift
// Create a context for quiz
let quizContext = CLSContext.init(type: CLSContextType.quiz, identifier: "science_Investigation_quiz", title: "Measurements Quiz")

// Add a summary describing this context
quizContext.summary = "A short quiz to test how much students know about scientific measurements and how to examine and analyze scientific data."

// Add a thumbnail for this context — ClassKit will downsize thumbnails to 330 x 330 px if needed
let bundle = Bundle.main
if let resourceURL = bundle.resourceURL {
    let imageURL = resourceURL.appendingPathComponent("measurements_quiz.jpg")
    if let thumbnail = thumbnailFromImage(atURL: imageURL) {
        quizContext.thumbnail = thumbnail
    }
}
```

### thumbnailFromImage — [6:52]

```swift
// Create a thumbnail of maximum dimension 330 x 330 px from an image file
func thumbnailFromImage(atURL: URL) -> CGImage? {
   if let imageSource = CGImageSourceCreateWithURL(atURL as CFURL, nil) {
       let thumbnailOptions = [kCGImageSourceCreateThumbnailFromImageAlways as String: true,
                               kCGImageSourceThumbnailMaxPixelSize as String: 330]
       return CGImageSourceCreateThumbnailAtIndex(
           imageSource, 0, thumbnailOptions as CFDictionary);
   }
   return nil
}
```

### Add suggestedAge and suggestedCompletionTime — [7:59]

```swift
// Add suggested age range appropriate for the content — ages 9 to 11 years

quizContext.suggestedAge = NSRange(9...11)

// Add suggested time to complete this quiz — 15 to 20 minutes

quizContext.suggestedCompletionTime = NSRange(15...20)
```

### Add progress reporting capabilities — [8:15]

```swift
// Add progress reporting capabilities

let reportingPercentDetails = "Reports percentage of progress"
let reportingCapabilityPercent = CLSProgressReportingCapability.init(
        kind: .percent,
        details: reportingPercentDetails)

let reportingQuantityDetails = "Reports number of hints used"
let reportingCapabilityQuantity = CLSProgressReportingCapability.init(
        kind: .quantity,
        details: reportingQuantityDetails)

quizContext.addProgressReportingCapabilities([reportingCapabilityPercent,
                                       reportingCapabilityQuantity])
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10672/4/F7DFFF2A-0E82-4B7F-BE8A-7C92F5A2E21C/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10672) — developer.apple.com. Indexed for agent consumption._
