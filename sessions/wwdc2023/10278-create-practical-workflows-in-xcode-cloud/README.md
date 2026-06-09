---
id: "wwdc2023-10278"
event: "wwdc2023"
year: 2023
title: "Create practical workflows in Xcode Cloud"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10278"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Create practical workflows in Xcode Cloud

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10278](https://developer.apple.com/videos/play/wwdc2023/10278)

Learn how Xcode Cloud can help teams of all shapes and sizes in their development process. We’ll share different ways to configure actions to help you create simple yet powerful workflows, and show you how to extend Xcode Cloud when you integrate with additional tools.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,502 words)

## Documentation & Resources

- [Xcode Cloud Workflows and Builds](https://developer.apple.com/documentation/AppStoreConnectAPI/xcode-cloud-workflows-and-builds) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppStoreConnectAPI/xcode-cloud-workflows-and-builds
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppStoreConnectAPI/xcode-cloud-workflows-and-builds.json
- [Improving code assessment by organizing tests into test plans](https://developer.apple.com/documentation/Xcode/organizing-tests-to-improve-feedback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/organizing-tests-to-improve-feedback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/organizing-tests-to-improve-feedback.json
- [Making dependencies available to Xcode Cloud](https://developer.apple.com/documentation/Xcode/Making-Dependencies-Available-to-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Making-Dependencies-Available-to-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Making-Dependencies-Available-to-Xcode-Cloud.json
- [Configuring webhooks in Xcode Cloud](https://developer.apple.com/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud.json
- [Environment variable reference](https://developer.apple.com/documentation/Xcode/Environment-Variable-Reference) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Environment-Variable-Reference
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Environment-Variable-Reference.json
- [Writing custom build scripts](https://developer.apple.com/documentation/Xcode/Writing-Custom-Build-Scripts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Writing-Custom-Build-Scripts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Writing-Custom-Build-Scripts.json
- [Xcode Cloud workflow reference](https://developer.apple.com/documentation/Xcode/Xcode-Cloud-Workflow-Reference) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Xcode-Cloud-Workflow-Reference
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Xcode-Cloud-Workflow-Reference.json
- [Developing a workflow strategy for Xcode Cloud](https://developer.apple.com/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud.json
- [Configuring your first Xcode Cloud workflow](https://developer.apple.com/documentation/Xcode/Configuring-Your-First-Xcode-Cloud-Workflow) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Your-First-Xcode-Cloud-Workflow
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Your-First-Xcode-Cloud-Workflow.json

## Code Snippets

### Pre-build script that replaces the app icon for beta builds — [14:38]

```bash
#!/bin/sh
# ci_pre_xcodebuild.sh
#

if [[ "$CI_XCODEBUILD_ACTION" == "archive" && "$CI_WORKFLOW" == "Beta" ]]; then
    echo "Replacing app icon with beta icon"
    mv BetaAppIcon.appiconset ../App/Assets.xcassets/AppIcon.appiconset
fi
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10278/4/A5414C99-EB05-48CC-B09F-9A322FBEF0C6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10278/4/A5414C99-EB05-48CC-B09F-9A322FBEF0C6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10278) — developer.apple.com. Indexed for agent consumption._
