---
id: "wwdc2021-10197"
event: "wwdc2021"
year: 2021
title: "Discover and curate Swift Packages using Collections"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10197"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Discover and curate Swift Packages using Collections

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10197](https://developer.apple.com/videos/play/wwdc2021/10197)

Whether you're curating packages for your team, for education purposes, or to share with other developers, Swift Package Collections can help you discover, explore and import new packages into your project. Discover improvements in the Swift Package workflow using Collections, and learn how you can curate, create, sign, and share your own Swift Package Collections.

**Keywords:** `collection`, `collections`, `dependency`, `dependency management`, `spm`, `swift package collection`, `swift packages`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,010 words)

## Documentation & Resources

- [Swift Package Collection Generator](https://github.com/apple/swift-package-collection-generator) _documentation_

## Code Snippets

### Simple collection — [7:00]

```json
{
  "name": "WWDC21 Demo Collection",
  "overview": "Packages to be used in our demo app",
  "keywords": ["wwdc21"],
  "author": {
    "name": "Boris Buegling"
  }
  "packages": [
    { "url": "https://github.com/apple/swift-format" },
    { "url": "https://github.com/Alamofire/Alamofire" }
  ],
}
```

### Complex collection — [7:17]

```json
{
  "name": "WWDC21 Demo Collection",
  "overview": "Packages to be used in our demo app",
  "keywords": ["wwdc21"],
  "packages": [
    {
      "url": "https://github.com/apple/swift-format",
      "summary": "Formatting technology for Swift source code.",
      "keywords": [“formatting”, "swift"],
      "versions": ["0.50400.0", "0.50300.0"],
      "excludedProducts": ["SwiftFormatConfiguration"],
      "readmeURL": "https://github.com/apple/swift-format/blob/main/README.md"
    },
    { "url": "https://github.com/Alamofire/Alamofire" }
  ],
  "author": {
    "name": "Boris Buegling"
  }
}
```

### Generating a collection — [8:46]

```bash
package-collection-generate --verbose input.json collection.json --auth-token
```

### Signing a collection — [9:30]

```bash
package-collection-sign collection.json collection-signed.json developer-key.pem developer-cert.cer
```

### Adding a collection — [10:15]

```bash
swift package-collection add
```

### Inspecting an entire collection — [10:34]

```bash
swift package-collection describe
```

### Viewing metadata of the swift-format package — [11:11]

```bash
swift package-collection describe https://github.com/apple/swift-format
```

### ReadMe Request — [13:07]

```swift
import Alamofire

struct ContentView: View {
  let readMeURL = "https://raw.githubusercontent.com/apple/swift/main/README.md"

  var body: some View {
    Button("Click me!") {
      AF.request(readMeURL).response { response in
        debugPrint(response)
      }
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10197/5/4B9FBC81-D676-431E-934C-6DD3EE985C64/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10197/5/4B9FBC81-D676-431E-934C-6DD3EE985C64/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10197) — developer.apple.com. Indexed for agent consumption._
