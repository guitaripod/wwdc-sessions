---
id: "wwdc2020-10169"
event: "wwdc2020"
year: 2020
title: "Swift packages: Resources and localization"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10169"
topics: ["Accessibility & Inclusion", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Swift packages: Resources and localization

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10169](https://developer.apple.com/videos/play/wwdc2020/10169)

Bring your resources along for the ride when you organize and share code using Swift packages. Discover how to include assets like images and storyboards in a package and how to access them from code. And learn how to add localized strings to make your code accessible to people around the world. To get the most out of this session, you should be familiar with Swift and packaging code. For an overview, watch “Creating Swift Packages” from WWDC19.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,526 words)

## Documentation & Resources

- [Language and Locale IDs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html
- [PackageDescription](https://developer.apple.com/documentation/PackageDescription) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PackageDescription
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PackageDescription.json

## Code Snippets

### Package Manifest file — [4:09]

```swift
// swift-tools-version:5.3
import PackageDescription

let package = Package(name: "MyGame",
    products: [
        .library(name: "GameLogic",
            targets: ["GameLogic"])
    ],
    targets: [
        .target(name: "GameLogic",
            excludes: [
                "Internal Notes.txt",
                "Artwork Creation"],
            resources: [
                .process("Logo.png"),
                .copy("Game Data")]
        )
    ]
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10169/3/0F6E83BB-5FF5-4627-9C42-F111EF4B4098/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10169) — developer.apple.com. Indexed for agent consumption._
