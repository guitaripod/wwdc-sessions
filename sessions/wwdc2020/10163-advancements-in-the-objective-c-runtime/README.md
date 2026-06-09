---
id: "wwdc2020-10163"
event: "wwdc2020"
year: 2020
title: "Advancements in the Objective-C runtime"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10163"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Advancements in the Objective-C runtime

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10163](https://developer.apple.com/videos/play/wwdc2020/10163)

Dive into the microscopic world of low-level bits and bytes that underlie every Objective-C and Swift class. Find out how recent changes to internal data structures, method lists, and tagged pointers provide better performance and lower memory usage. We’ll demonstrate how to recognize and fix crashes in code that depend on internal details, and show you how to keep your code unaffected by changes to the runtime.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,867 words)

## Documentation & Resources

- [Objective-C Runtime](https://developer.apple.com/documentation/ObjectiveC/objective-c-runtime) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ObjectiveC/objective-c-runtime
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ObjectiveC/objective-c-runtime.json

## Code Snippets

### Use the heap command to calculate memory savings — [5:37]

```bash
heap Mail | egrep 'class_rw|COUNT'
```

### Use the APIs — [7:35]

```objectivec
class_getName

class_getSuperclass

class_copyMethodList
```

### Use the APIs — [14:38]

```objectivec
method_getName

method_getTypeEncoding

method_getImplementation
```

### Use the APIs — [21:52]

```objectivec
if ([obj isKindOfClass:[NSString class]]) {
    // a string
}
NSUInteger length = [obj length];


if (CFGetTypeID(obj) == CFStringGetTypeID()) {
    // a string
}
CFIndex length = CFStringGetLength(obj);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10163/5/69E6CEAB-D828-495C-B745-D48BF721F796/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10163) — developer.apple.com. Indexed for agent consumption._
