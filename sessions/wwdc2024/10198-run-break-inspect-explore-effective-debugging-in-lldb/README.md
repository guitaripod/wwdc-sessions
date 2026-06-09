---
id: "wwdc2024-10198"
event: "wwdc2024"
year: 2024
title: "Run, Break, Inspect: Explore effective debugging in LLDB"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10198"
topics: ["Swift", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Run, Break, Inspect: Explore effective debugging in LLDB

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10198](https://developer.apple.com/videos/play/wwdc2024/10198)

Learn how to use LLDB to explore and debug codebases. We’ll show you how to make the most of crashlogs and backtraces, and how to supercharge breakpoints with actions and complex stop conditions. We’ll also explore how the “p” command and the latest features in Swift 6 can enhance your debugging experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,863 words)

## Documentation & Resources

- [The LLDB debugger](https://lldb.llvm.org/) _documentation_
- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010

## Code Snippets

### WatchLater button — [8:09]

```swift
Button(action: { watchLater.toggle(video: video) }) {
  let inList = watchLater.isInList(video: video)
  Label(inList ? "In Watch Later" : "Add to Watch Later",
  systemImage: inList ? "checkmark" : "plus")
}
```

### Printing watch later list information — [12:54]

```swift
p watchLater.count
p watchLater.last!.name
```

### Breakpoint actions: Printing name of the most recently added video — [13:45]

```swift
p "last video is \(watchLater.last?.name)"
```

### Breakpoint actions: on the command line — [14:42]

```swift
b DetailView.swift:70
break command add
p "last video is \(watchLater.last?.name)"
continue
DONE
```

### @DebugDescriptio macro example — [26:46]

```swift
// Type summaries

@DebugDescription
struct WatchLaterItem {
    let video: Video
    let name: String
    let addedOn: Date

    var debugDescription: String {
        "\(name) - \(addedOn)"
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10198/4/A6D919A0-000B-4A54-AE83-6F261757D780/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10198/4/A6D919A0-000B-4A54-AE83-6F261757D780/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10198) — developer.apple.com. Indexed for agent consumption._
