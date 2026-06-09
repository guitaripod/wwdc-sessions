---
id: "wwdc2021-10269"
event: "wwdc2021"
year: 2021
title: "Customize your advanced Xcode Cloud workflows"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10269"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Customize your advanced Xcode Cloud workflows

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10269](https://developer.apple.com/videos/play/wwdc2021/10269)

Xcode Cloud integrates with Apple Developer tools and services, all major source control management services, and even social collaboration tools like Slack. If your development process relies on additional tools and external services, however, you can fine-tune your workflows and the behavior of your build.

Learn how you can pass information to your build using environment variables and run additional commands inside your actions using custom build scripts. Find out how to add additional repositories where you and your team might share work. And discover how you can integrate Xcode Cloud with external services using webhooks.

To get the most out of this session, we recommend first watching “Meet Xcode Cloud” and “Explore Xcode Cloud workflows” from WWDC21.

**Keywords:** `build`, `ci`, `continuous integration`, `scripts`, `testflight`, `testing`, `xcode`, `xcode cloud`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,250 words)

## Documentation & Resources

- [Configuring webhooks in Xcode Cloud](https://developer.apple.com/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud.json
- [Environment variable reference](https://developer.apple.com/documentation/Xcode/Environment-Variable-Reference) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Environment-Variable-Reference
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Environment-Variable-Reference.json
- [Writing custom build scripts](https://developer.apple.com/documentation/Xcode/Writing-Custom-Build-Scripts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Writing-Custom-Build-Scripts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Writing-Custom-Build-Scripts.json
- [Configuring your Xcode Cloud workflow’s actions](https://developer.apple.com/documentation/Xcode/Configuring-Your-Xcode-Cloud-Workflow-s-Actions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Your-Xcode-Cloud-Workflow-s-Actions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Your-Xcode-Cloud-Workflow-s-Actions.json
- [Configuring start conditions](https://developer.apple.com/documentation/Xcode/Configuring-Start-Conditions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Start-Conditions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Start-Conditions.json
- [Xcode Cloud workflow reference](https://developer.apple.com/documentation/Xcode/Xcode-Cloud-Workflow-Reference) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Xcode-Cloud-Workflow-Reference
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Xcode-Cloud-Workflow-Reference.json
- [Developing a workflow strategy for Xcode Cloud](https://developer.apple.com/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Developing-a-Workflow-Strategy-for-Xcode-Cloud.json
- [Xcode Cloud](https://developer.apple.com/documentation/Xcode/Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Xcode-Cloud.json

## Code Snippets

### ci_pre_xcodebuild.sh — [9:03]

```bash
#!/bin/sh

#  ci_pre_xcodebuild.sh
#  Fruta
#
#  Made in Vancouver, Canada
#  

if [[ -n $CI_PULL_REQUEST_NUMBER && $CI_XCODEBUILD_ACTION = 'archive' ]];
then
    echo "Setting Fruta Beta App Icon"
    APP_ICON_PATH=$CI_WORKSPACE/Shared/Assets.xcassets/AppIcon.appiconset

    # Remove existing App Icon
    rm -rf $APP_ICON_PATH

    # Replace with Fruta Beta App Icon
    mv "$CI_WORKSPACE/ci_scripts/AppIcon-Beta.appiconset" $APP_ICON_PATH
fi
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10269/3/CA083488-C662-4ADA-8BA2-89647472F1C9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10269/3/CA083488-C662-4ADA-8BA2-89647472F1C9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10269) — developer.apple.com. Indexed for agent consumption._