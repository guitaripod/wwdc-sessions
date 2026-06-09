---
id: "wwdc2023-10108"
event: "wwdc2023"
year: 2023
title: "What’s new in Background Assets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10108"
topics: ["Graphics & Games", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in Background Assets

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10108](https://developer.apple.com/videos/play/wwdc2023/10108)

Waiting is no fun! Discover how Background Assets can help your app download content before it even launches. We’ll show you how to integrate Background Assets into an existing app, explore when to use essential or non-essential assets, and learn how to make debugging your extension a breeze.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,965 words)

## Documentation & Resources

- [Downloading essential assets in the background](https://developer.apple.com/documentation/BackgroundAssets/downloading-essential-assets-in-the-background) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundAssets/downloading-essential-assets-in-the-background
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundAssets/downloading-essential-assets-in-the-background.json
- [Background Assets](https://developer.apple.com/documentation/BackgroundAssets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundAssets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundAssets.json

## Code Snippets

### Info.plist requirements (old) — [16:09]

```swift
|Key|Type|Description|
|-|-|-|
|BAInitialDownloadRestrictions|Dictionary|The restrictions that apply to the set of assets that download prior to first app launch.
|BADownloadAllowance|Number|The combined size of the initial set of non-Essential asset downloads. Stored inside the BAInitialDownloadRestrictions dictionary.
|BADownloadDomainAllowList|Array|Array of domains that can assets can be downloaded from prior to first app launch. Stored inside the BAInitialDownloadRestrictions dictionary.
|BAMaxInstallSize|Number|The combined size (in bytes) on disk of the Non-Essential assets that download immediately after app installation.
|BAManifestURL|String|URL of the application's manifest.
```

### Info.plist requirements (new) — [16:22]

```swift
|Key|Type|Description|
|-|-|-|
|BAInitialDownloadRestrictions|Dictionary|The restrictions that apply to the set of assets that download prior to first app launch.
|BADownloadAllowance|Number|The combined size of the initial set of non-Essential asset downloads. Stored inside the BAInitialDownloadRestrictions dictionary.
|**BAEssentialDownloadAllowance**|Number|The combined size (in bytes) of the initial set of Essential asset downloads, including your manifest. Stored inside the BAInitialDownloadRestrictions dictionary.
|BADownloadDomainAllowList|Array|Array of domains that can assets can be downloaded from prior to first app launch. Stored inside the BAInitialDownloadRestrictions dictionary.
|BAMaxInstallSize|Number|The combined size (in bytes) on disk of the Non-Essential assets that download immediately after app installation.
|**BAEssentialMaxInstallSize**|Number|The combined size (in bytes) on disk of the Essential downloads that occur during app installation.
|BAManifestURL|String|URL of the application's manifest.
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10108/4/ABFECE71-93F9-4920-8A81-C99BB04A5FF3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10108/4/ABFECE71-93F9-4920-8A81-C99BB04A5FF3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10108) — developer.apple.com. Indexed for agent consumption._