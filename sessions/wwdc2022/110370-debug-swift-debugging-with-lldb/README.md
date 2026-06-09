---
id: "wwdc2022-110370"
event: "wwdc2022"
year: 2022
title: "Debug Swift debugging with LLDB"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110370"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Debug Swift debugging with LLDB

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-110370](https://developer.apple.com/videos/play/wwdc2022/110370)

Learn how you can set up complex Swift projects for debugging. We'll take you on a deep dive into the internals of LLDB and debug info. We'll also share best practices for complex scenarios such as debugging code built on build servers or code from custom build systems.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,576 words)

## Code Snippets

### Show info about all loaded dylibs — [5:04]

```bash
image list
```

### Show debug info for a code address — [5:24]

```bash
image lookup -va $pc
```

### Show help for target.source-map — [5:58]

```bash
settings list target.source-map
```

### Remap source paths in LLDB — [6:37]

```bash
settings set target.source-map /Volumes/BUILD_SERVER/projects /Users/demo/Desktop/Adventure/3rdparty
```

### Source path remapping — [7:02]

```bash
settings set target.source-map prefix new
```

### Debug prefix map — [8:13]

```bash
-debug-prefix-map $PWD=/BUILDROOT
```

### Print object description of "words" — [8:32]

```bash
po words
expr -O -- words
```

### Evaluate the expression "words" — [8:40]

```bash
p words
expr words
```

### Display the variable "words" — [8:58]

```bash
v words
frame variable words
```

### Raw memory of a Swift variable — [10:10]

```bash
mem read UnsafePointer<Items>(self.inventory)
```

### See diagnostics from LLDB's embedded Swift compiler — [11:59]

```bash
swift-healthcheck
```

### Register Swift modules with the Linker — [15:47]

```bash
ld … -add_ast_path /path/to/My.swiftmodule
```

### Verify Swift modules were registered in binary — [16:05]

```bash
dsymutil -s MyApp | grep .swiftmodule
```

### Wrapping Swift modules in object files on Linux — [16:12]

```bash
swiftc -modulewrap My.swiftmodule -o My.swiftmodule.o
```

### Evaluate the expression "self" — [16:52]

```bash
p self
```

### Print object description of "words" — [16:58]

```bash
po words
expr -O -- words
```

### Step into function call — [17:08]

```bash
s
thread step-in
```

### Step over instruction — [17:10]

```bash
n
thread step-over
```

### Avoiding serialized search paths in Swift modules (command line) — [18:23]

```bash
-no-serialize-debugging-options
```

### Avoiding serialized search paths in Swift modules (Xcode) — [18:24]

```bash
SWIFT_SERIALIZE_DEBUGGING_OPTIONS=NO
```

### Reintroducing search paths in LLDB — [18:32]

```bash
settings set target.swift-extra-clang-flags …
settings set target.swift-framework-search-paths …
settings set target.swift-module-search-paths …
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110370/7/31CCC67C-D5AC-4493-AFB4-7B833E2B8162/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110370/7/31CCC67C-D5AC-4493-AFB4-7B833E2B8162/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110370) — developer.apple.com. Indexed for agent consumption._
