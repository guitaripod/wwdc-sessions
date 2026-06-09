---
id: "wwdc2025-307"
event: "wwdc2025"
year: 2025
title: "Explore Swift and Java interoperability"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/307"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Explore Swift and Java interoperability

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-307](https://developer.apple.com/videos/play/wwdc2025/307)

Learn how you can mix Swift and Java in a single codebase. We’ll introduce the swift-java interoperability project, which allows you to use Swift in Java programs or vice versa. We’ll show you how to use the tools and libraries offered by swift-java to write safe and performant code that interoperates between these two runtimes.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,467 words)

## Documentation & Resources

- [SwiftJava](https://github.com/swiftlang/swift-java) _guide_
- [The Swift website](https://www.swift.org) _documentation_
- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Implement JNI native methods in Swift — [9:05]

```swift
import JavaKit
import JavaRuntime

import Crypto

@JavaImplementation("com.example.JNIExample")
extension JNIExample: JNIExampleNativeMethods {

  @JavaMethod
  func compute(_ a: JavaInteger?, _ b: JavaInteger?) -> [UInt8] {
    guard let a else { fatalError("Expected non-null parameter 'a'") }
    guard let a else { fatalError("Expected non-null parameter 'b'") }

    let digest = SHA256Digest([a.intValue(), b.intValue()]) // convenience init defined elsewhere
    return digest.toArray()
  }
}
```

### Resolve Java dependencies with swift-java — [12:30]

```swift
swift-java resolve --module-name JavaApacheCommonsCSV
```

### Use a Java library from Swift — [13:05]

```swift
import JavaKit
import JavaKitIO
import JavaApacheCommonsCSV

let jvm = try JavaVirtualMachine.shared()

let reader = FileReader("sample.csv") // java.io.StringReader

for record in try JavaClass<CSVFormat>().RFC4180.parse(reader)!.getRecords()! {
  for field in record.toList()! {      // Field: hello
    print("Field: \(field)")           // Field: example
  }                                    // Field: csv
}

print("Done.")
```

### Wrap Swift types for Java — [16:22]

```swift
swift-java --input-swift Sources/SwiftyBusiness \ 
--java-package com.example.business \
--output-swift .build/.../outputs/SwiftyBusiness \
--output-java .build/.../outputs/Java ...
```

### Create Swift objects from Java — [18:55]

```csharp
try (var arena = SwiftArena.ofConfined()) {
  var business = new SwiftyBusiness(..., arena);
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/307/5/79c0d8b7-243d-484f-890b-ecebf507a1e7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/307/5/79c0d8b7-243d-484f-890b-ecebf507a1e7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/307) — developer.apple.com. Indexed for agent consumption._