---
id: "wwdc2020-10214"
event: "wwdc2020"
year: 2020
title: "Port your Mac app to Apple silicon"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10214"
topics: ["Developer Tools"]
platforms: ["macOS"]
hasTranscript: true
---

# Port your Mac app to Apple silicon

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** macOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10214](https://developer.apple.com/videos/play/wwdc2020/10214)

Your porting questions, answered: Learn how to recompile your macOS app for Apple silicon Macs and build universal apps that launch faster, have better performance, and support the future of the platform. We’ll show you how Xcode makes it simple to build a universal macOS binary and go through running, debugging, and testing your app. Learn what changes to low-level code you might need to make, find out how to handle in-process and out-of-process plug-ins, and discover some useful tips for working with universal apps. We’ve designed this session for experienced macOS developers who want to get their existing apps running natively on Apple silicon Macs. You can learn more about doing so in the Apple silicon documentation. For more information on the transition to Apple silicon, watch "Explore the new system architecture of Apple silicon Macs", "Bring your Metal app to Apple silicon Macs", and "Optimize Metal Performance for Apple silicon Macs". And to learn how to run your iPhone and iPad apps on Mac, check out "iPad and iPhone apps on Apple silicon Macs".

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,615 words)

## Documentation & Resources

- [Learn more about Apple Silicon](https://developer.apple.com/documentation/apple-silicon) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/apple-silicon
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/apple-silicon.json

## Code Snippets

### Don’t assume the time is returned in nanoseconds — [21:19]

```swift
// Don’t assume the time is returned in nanoseconds

func monotonicTimestampInSeconds() -> Double {
  let ticks = mach_absolute_time()
  let seconds = Double(ticks) / 1_000_000_000
  return seconds
}
```

### Use clock_gettime_nsec_np to read timestamp in nanoseconds — [21:40]

```swift
// Use clock_gettime_nsec_np to read timestamp in nanoseconds

func monotonicTimestampInSeconds() -> Double {
  let nanoseconds = clock_gettime_nsec_np(CLOCK_UPTIME_RAW)
  let seconds = Double(nanoseconds) / 1_000_000_000
  return seconds
}
```

### Avoid spinlocks and spinning to check for work — [26:40]

```swift
func performWorkUnderSpinlock() { 
  spinlock_lock()
  performWork()
  spinlock_unlock()
}

func retrieveNextWorkTask() -> WorkTask {
  while true {
    let task = queue.sync { taskQueue.pop() }
    if let task = task { return task }
    else { continue }
  }
}
```

### Prefer blocking locks and condition variables — [27:03]

```swift
func performWorkUnderSpinlock() { 
  os_unfair_lock_lock()
  performWork()
  os_unfair_lock_unlock()
}

func retrieveNextWorkTask() -> WorkTask {
  condition.lock()
  while !taskQueue.hasAnyWork {
    condition.wait()
  }
  let task = taskQueue.pop()
  condition.unlock()
  return task
}
```

### Load a plug-in dynamically — [33:51]

```objectivec
void *plugin_module = dlopen("./path/to/plugin.dylib", RTLD_NOW);
if (plugin_module == NULL) {
  fprintf(stderr, "loading module failed:\n");
  fprintf(stderr, "%s\n", dlerror());
  return 0;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10214/7/871FAB69-F6A4-470A-80F0-00028CDC0E58/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10214) — developer.apple.com. Indexed for agent consumption._
