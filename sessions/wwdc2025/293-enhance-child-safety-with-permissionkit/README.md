---
id: "wwdc2025-293"
event: "wwdc2025"
year: 2025
title: "Enhance child safety with PermissionKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/293"
topics: ["App Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance child safety with PermissionKit

**Event:** WWDC25 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-293](https://developer.apple.com/videos/play/wwdc2025/293)

Discover how PermissionKit helps you enhance communication safety for children in your app. We’ll show you how to use this new framework to create age-appropriate communication experiences and leverage Family Sharing for parental approvals. You’ll learn how to build permission requests that seamlessly integrate with Messages, handle parental responses, and adapt your UI for child users. To get the most out of this session, we recommend first watching “Deliver age-appropriate experiences in your app” from WWDC25.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,781 words)

## Documentation & Resources

- [Design safe and age‑appropriate experiences for your apps and games](https://developer.apple.com/kids/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/kids/
- [Declared Age Range](https://developer.apple.com/documentation/DeclaredAgeRange) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeclaredAgeRange
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeclaredAgeRange.json
- [PermissionKit](https://developer.apple.com/documentation/PermissionKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PermissionKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PermissionKit.json

## Code Snippets

### Tailor your UI for children — [4:03]

```swift
import PermissionKit

let knownHandles = await CommunicationLimits.current.knownHandles(in: conversation.participants)

if knownHandles.isSuperset(of: conversation.participants) {
    // Show content
} else {
    // Hide content
}
```

### Create a question — [5:15]

```swift
import PermissionKit

var question = PermissionQuestion(handles: [
    CommunicationHandle(value: "dragonslayer42", kind: .custom),
    CommunicationHandle(value: "progamer67", kind: .custom)
])
```

### Create a question - additional metadata — [5:38]

```swift
import PermissionKit

let people = [
    PersonInformation(
        handle: CommunicationHandle(value: "dragonslayer42", kind: .custom),
        nameComponents: nameComponents,
        avatarImage: profilePic
    ),
    PersonInformation(
        handle: CommunicationHandle(value: "progamer67", kind: .custom)
    )
]

var topic = CommunicationTopic(personInformation: people)
topic.actions = [.message]

var question = PermissionQuestion(communicationTopic: topic)
```

### Ask a question - SwiftUI — [6:25]

```swift
import PermissionKit
import SwiftUI

struct ContentView: View {
    let question: PermissionQuestion<CommunicationTopic>

    var body: some View {
        // ...
        CommunicationLimitsButton(question: question) {
            Label("Ask Permission", systemImage: "paperplane")
        }
    }
}
```

### Ask a question - UIKit — [6:43]

```swift
import PermissionKit
import UIKit

try await CommunicationLimits.current.ask(question, in: viewController)
```

### Ask a question - AppKit — [6:54]

```swift
import PermissionKit
import AppKit

try await CommunicationLimits.current.ask(question, in: window)
```

### Parent/guardian responses — [7:19]

```swift
import PermissionKit
import SwiftUI

struct ChatsView: View {
    @State var isShowingResponseAlert = false

    var body: some View {
        List {
           // ...
        }
        .task {
            let updates = CommunicationLimits.current.updates
            for await update in updates {
                // Received a response!
                self.isShowingResponseAlert = true
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/293/4/3d149cec-af19-46df-9916-67a21d041047/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/293/4/3d149cec-af19-46df-9916-67a21d041047/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/293) — developer.apple.com. Indexed for agent consumption._
