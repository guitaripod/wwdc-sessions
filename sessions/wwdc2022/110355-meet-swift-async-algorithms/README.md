---
id: "wwdc2022-110355"
event: "wwdc2022"
year: 2022
title: "Meet Swift Async Algorithms"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110355"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet Swift Async Algorithms

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110355](https://developer.apple.com/videos/play/wwdc2022/110355)

Discover the latest open source Swift package from Apple: Swift Async Algorithms. We'll explore algorithms from this package that you can use with AsyncSequence, including zip, merge, and throttle. Follow along with us as we use these algorithms to build a great messaging app. We'll also share best practices for combining multiple AsyncSequences and using the Swift Clock type to work with values over time. To get the most out of this session, we recommend watching "Meet AsyncSequence."

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,899 words)

## Documentation & Resources

- [Swift Async Algorithms package](https://github.com/apple/swift-async-algorithms) _guide_
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/) _guide_
- [AsyncSequence](https://developer.apple.com/documentation/Swift/AsyncSequence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/AsyncSequence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/AsyncSequence.json

## Code Snippets

### The messaging app — [2:01]

```swift
struct Account {
  var messages: AsyncStream<Message>
}  

actor AccountManager {
  var primaryAccount: Account
  var secondaryAccount: Account? 
}

protocol MessagePreview {
  func displayPreviews(_ manager: AccountManager) async }
```

### Zip — [3:16]

```swift
// upload attachments of videos and previews such that every video has a preview that are created concurrently so that neither blocks each other. 

for try await (vid, preview) in zip(videos, previews) {
  try await upload(vid, preview)
}
```

### Merge — [5:09]

```swift
// Display previews of messages from either the primary or secondary account

for try await message in merge(primaryAccount.messages, secondaryAccount.messages) {
  displayPreview(message)
}
```

### Suspending Clock — [6:37]

```swift
// Sleep until a given deadline

let clock = SuspendingClock()
var deadline = clock.now + .seconds(3)
try await clock.sleep(until: deadline)
```

### Suspending Clock vs. Continuous Clock — [6:56]

```swift
let clock = SuspendingClock()
let elapsed = await clock.measure {
  await someLongRunningWork()
}
//Elapsed time reads 00:05.40

let clock = ContinuousClock()
let elapsed = await clock.measure {
  await someLongRunningWork()
}
//Elapsed time reads 00:19.54
```

### Control searching messages — [8:34]

```swift
// Control searching messages

class SearchController {
  let searchResults = AsyncChannel<SearchResult>()

  func search<SearchValues: AsyncSequence>(_ searchValues: SearchValues) 
    where SearchValues.Element == String 
}
```

### Debounce — [9:16]

```swift
let queries = searchValues
   .debounce(for: .milliseconds(300))

for await query in queries {
  let results = try await performSearch(query)
  await channel.send(results) }
```

### Chunked by — [10:21]

```swift
let batches = outboundMessages.chunked(
  by: .repeating(every: .milliseconds(500))
)

let encoder = JSONEncoder() 
for await batch in batches {
  let data = try encoder.encode(batch)
  try await postToServer(data) 
}
```

### Conversions in initializers — [11:22]

```swift
// Create a message with awaiting attachments to be encoded
init<Attachments: AsyncSequence>(_ attachments: Attachments) async rethrows {
  self.attachments = try await Array(attachments)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110355/4/459D7B80-E4A7-428F-ADA8-EF2543CE3350/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110355/4/459D7B80-E4A7-428F-ADA8-EF2543CE3350/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110355) — developer.apple.com. Indexed for agent consumption._
