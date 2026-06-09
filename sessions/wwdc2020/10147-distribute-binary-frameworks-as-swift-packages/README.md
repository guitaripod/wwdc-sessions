---
id: "wwdc2020-10147"
event: "wwdc2020"
year: 2020
title: "Distribute binary frameworks as Swift packages"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10147"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Distribute binary frameworks as Swift packages

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10147](https://developer.apple.com/videos/play/wwdc2020/10147)

Discover how you can add third-party frameworks to your app and keep them up to date using Swift packages in Xcode. We’ll show you how to author packages that reference frameworks, explain binary targets and how to specify them in your package manifest file, and demonstrate how to compute checksums so that your clients always get the exact binary you expect. Frameworks are distributed in the XCFramework format. For further details on creating and versioning an XCFramework, be sure to watch "Binary Frameworks in Swift" from WWDC19.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,128 words)

## Code Snippets

### Adding a Package Dependency to the Package Manifest — [2:37]

```swift
// swift-tools-version:5.3

import PackageDescription

let package = Package(
    name: "package",
    products: [
        .library(
            name: "package",
            targets: ["package"]),
    ],
    dependencies: [
        .package(url: "https://github.com/JohnnyAppleseed2020/BinaryEmoji", from: "1.0.0"),
    ],
    targets: [
        .target(
            name: "package",
            dependencies: ["Emoji"]),
    ]
)
```

### Distributing Binary Frameworks as a Swift Package — [3:04]

```swift
// swift-tools-version:5.3

import PackageDescription

let package = Package(
    name: "Emoji",
    products: [
        .library(name: "Emoji", targets: ["Emoji"])
    ],
    dependencies: [
    ],
    targets: [
        .binaryTarget(
            name: "Emoji",
            url: "https://example.com/Emoji/Emoji-1.0.0.xcframework.zip",
            checksum: "6d988a1a27418674b4d7c31732f6d60e60734ceb11a0ce9b54d1871918d9c194"
        )
    ]
)
```

### Computing the Checksum — [5:43]

```bash
swift package compute-checksum Emoji-1.0.0.xcframework.zip
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10147/3/9A1289F5-A542-4604-BB2E-E7A77AF2C41F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10147) — developer.apple.com. Indexed for agent consumption._
