---
id: "wwdc2023-10224"
event: "wwdc2023"
year: 2023
title: "Simplify distribution in Xcode and Xcode Cloud"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10224"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Simplify distribution in Xcode and Xcode Cloud

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10224](https://developer.apple.com/videos/play/wwdc2023/10224)

Discover how to share your app using Xcode’s streamlined distribution, which allows you to submit your app to TestFlight or the App Store with one click. We’ll also show you how to use Xcode Cloud to simplify your distribution process by automatically including notes for testers in TestFlight, and use post-action to automatically notarize your Mac apps.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,363 words)

## Documentation & Resources

- [Including notes for testers with a beta release of your app](https://developer.apple.com/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app.json
- [Distributing your app for beta testing and releases](https://developer.apple.com/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/distributing-your-app-for-beta-testing-and-releases.json

## Code Snippets

### Use Xcode Cloud to add a Git commit message to TestFlight What to Test — [8:50]

```bash
#!/bin/zsh
#  ci_post_xcodebuild.sh

if [[ -d "$CI_APP_STORE_SIGNED_APP_PATH" ]]; then
  TESTFLIGHT_DIR_PATH=../TestFlight
  mkdir $TESTFLIGHT_DIR_PATH
  git log -1 --pretty=format:"%s" >! $TESTFLIGHT_DIR_PATH/WhatToTest.en-US.txt
fi
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10224/4/3FB069F4-A143-41C4-945E-76651EFF81CF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10224/4/3FB069F4-A143-41C4-945E-76651EFF81CF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10224) — developer.apple.com. Indexed for agent consumption._
