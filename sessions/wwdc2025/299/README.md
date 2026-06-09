---
id: "wwdc2025-299"
event: "wwdc2025"
year: 2025
title: "Deliver age-appropriate experiences in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/299"
topics: ["System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Deliver age-appropriate experiences in your app

**Event:** WWDC25 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-299](https://developer.apple.com/videos/play/wwdc2025/299)

Learn how to deliver age-appropriate experiences in your app with the new Declared Age Range API. We’ll cover how parents can allow their child to share an age range with an app to ensure a safe experience in a privacy-preserving way. We’ll also explore how this framework can help you tailor your app’s content and features based on a user’s age, and show you how to implement age gates, understand caching, and respect user privacy while creating safer and more engaging experiences.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,959 words)

## Documentation & Resources

- [Design safe and age‑appropriate experiences for your apps and games](https://developer.apple.com/kids/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/kids/
- [Helping Protect Kids Online](https://developer.apple.com/support/downloads/Helping-Protect-Kids-Online-2025.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/support/downloads/Helping-Protect-Kids-Online-2025.pdf
- [Declared Age Range](https://developer.apple.com/documentation/DeclaredAgeRange) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeclaredAgeRange
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeclaredAgeRange.json

## Code Snippets

### Request an age range — [8:03]

```swift
// Request an age range

import SwiftUI
import DeclaredAgeRange

struct LandmarkDetail: View {
    // ...
    @State var photoSharingEnabled = false
    @Environment(\.requestAgeRange) var requestAgeRange

    var body: some View {
        ScrollView {
            // ...
            Button("Share Photos") {}
                .disabled(!photoSharingEnabled)
        }
        .task {
            await requestAgeRangeHelper()
        }
    }

    func requestAgeRangeHelper() async {
        do {
            // TODO: Check user region
            let ageRangeResponse = try await requestAgeRange(ageGates: 16)
            switch ageRangeResponse {
            case let .sharing(range):
                 // Age range shared
                if let lowerBound = range.lowerBound, lowerBound >= 16 {
                    photoSharingEnabled = true
                }
                // guardianDeclared, selfDeclared
                print(range.ageRangeDeclaration)
            case .declinedSharing:
                // Declined to share
                print("Declined to share")
            }
        } catch AgeRangeService.Error.invalidRequest {
            print("Handle invalid request error")
        } catch AgeRangeService.Error.notAvailable {
            print("Handle not available error")
        } catch {
            print("Unhandled error: \(error)")
        }
    }
}
```

### Communication Limits — [11:49]

```swift
// Request an age range

func requestAgeRangeHelper() async {
    do {
        // TODO: Check user region
        let ageRangeResponse = try await requestAgeRange(ageGates: 16)
        switch ageRangeResponse {
        case let .sharing(range):
            if range.activeParentalControls.contains(.communicationLimits) {
                print("Communication Limits enabled")
            }
            // ...
        case .declinedSharing:
            // Declined to share
            print("Declined to share")
        }
    } catch {
        // ...
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/299/4/ffa39510-a851-4af3-9584-7e37abdfc5bf/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/299/4/ffa39510-a851-4af3-9584-7e37abdfc5bf/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/299) — developer.apple.com. Indexed for agent consumption._