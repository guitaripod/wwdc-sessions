---
id: "wwdc2020-10005"
event: "wwdc2020"
year: 2020
title: "What's new in assessment"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10005"
topics: ["Privacy & Security", "Business & Education"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in assessment

**Event:** WWDC20 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10005](https://developer.apple.com/videos/play/wwdc2020/10005)

It’s now easier than ever to deliver academic tests on the Mac. Learn how education developers can leverage the Automatic Assessment Configuration framework for iPhone, iPad, and Mac to deliver tests and assess students across all devices. And discover how developers can enable restricted features within tests and exams on iOS to accommodate student needs or suit the test content.

**Keywords:** `assessment`, `catalyst`, `curriculum`, `education`, `student`, `testing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,501 words)

## Documentation & Resources

- [Automatic Assessment Configuration](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AutomaticAssessmentConfiguration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AutomaticAssessmentConfiguration.json

## Code Snippets

### Working with AAC — [3:51]

```swift
import AutomaticAssessmentConfiguration

class AssessmentManager: NSObject {
    private var assessmentSession: AEAssessmentSession?

    func beginAssessmentMode() {
        let config = AEAssessmentConfiguration() // Configure AAC behavior

        let session = AEAssessmentSession(configuration: config) // Construct your session

        session.delegate = self // Receive lifecycle events via delegation

        assessmentSession = session // Retain the session

        // Present assessment mode bringup transition UI
        // ...

        session.begin()
    }

    func endAssessmentMode() {
        guard let session = assessmentSession else {
            return
        }

        // Present assessment mode teardown transition UI
        // ...

        session.end()
    }
}

extension AssessmentManager: AEAssessmentSessionDelegate {

    func assessmentSessionDidBegin(_ session: AEAssessmentSession) {
        // Stop showing assessment mode bringup transition UI
        // ...

        // Present sensitive testing content
        // ...
    }

    func assessmentSession(_ session: AEAssessmentSession, failedToBeginWithError error: Error) {
        // Stop showing assessment mode bringup transition UI
        // ...

        // Present some kind of error UI
        // ...

        // Release your reference to the AEAssessmentSession
        assessmentSession = nil
    }

    func assessmentSessionDidEnd(_ session: AEAssessmentSession) {
        //  Stop showing assessment mode teardown transition UI
        // ...

        // Present your post-test UI
        // (maybe a result, a confirmation, or just the initial view)
        // ...

        // Release your reference to the AEAssessmentSession
        assessmentSession = nil
    }

    func assessmentSession(_ session: AEAssessmentSession, wasInterruptedWithError error: Error) {
        // Hide all sensitive UI
        // ...

        // Present some kind of error UI
        // ...

        session.end()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10005/3/50CEFA81-2D73-4ACC-B274-399608A1BAAF/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10005) — developer.apple.com. Indexed for agent consumption._
