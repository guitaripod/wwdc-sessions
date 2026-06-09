---
id: "wwdc2021-10256"
event: "wwdc2021"
year: 2021
title: "Meet the Swift Algorithms and Collections packages"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10256"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet the Swift Algorithms and Collections packages

**Event:** WWDC21 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10256](https://developer.apple.com/videos/play/wwdc2021/10256)

Discover two of the latest additions to the list of open-source Swift packages from Apple: Swift Algorithms and Swift Collections. Not only can you use these packages immediately, they also incubate new algorithms and data structures for eventual inclusion in the Swift Standard Library. We’ll show you how you can integrate these packages into your projects and select the right algorithms and data structures to make your code clearer and faster.

**Keywords:** `adjacentpairs`, `array`, `arrayslice`, `buffer`, `chunked`, `chunkedby`, `chunks`, `compactmap`, `deque`, `dictionary`, `double-ended`, `ended`, `filter`, `flatmap`, `flattensequence`, `hashtable`, `joined`, `joinedby`, `joinedsequence`, `lazycompactmap`, `lazyflatmap`, `lazysequence`, `loops`, `map`, `messages`, `nsorderedset`, `ordereddictionary`, `orderedset`, `prefix`, `queue`, `raw`, `reversedcollection`, `set`, `suffix`, `transcript`, `windows`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,459 words)

## Documentation & Resources

- [Collection](https://developer.apple.com/documentation/Swift/Collection) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/Collection
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/Collection.json
- [Sequence](https://developer.apple.com/documentation/Swift/Sequence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/Sequence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/Sequence.json
- [Swift Collections on GitHub](https://github.com/apple/swift-collections) _documentation_
- [Swift Algorithms on GitHub](https://github.com/apple/swift-algorithms) _documentation_
- [Swift Forums](https://forums.swift.org) _developerForum_

## Code Snippets

### The map algorithm — [1:00]

```swift
// Raw loop:
var selectedMessages: [Message] = []
for indexPath in indexPathsForSelectedRows {
    selectedMessages.append(messages[indexPath.row])
}

// Using `map` makes this clearer and faster.
indexPathsForSelectedRows.map { messages[$0.row] }
```

### The compactMap algorithm — [1:36]

```swift
// Raw loop:
var attachments: [Attachment] = []
for message in messages {
    if let attachment = message.attachment {
        attachments.append(attachment)
    }
}

// The above is just a `map` and a `filter`.
messages
    .filter { $0.attachment != nil }
    .map { $0.attachment! }

// This pattern is so common we have a special name and algorithm for it.
messages.compactMap { $0.attachment }
```

### The flatMap algorithm — [2:06]

```swift
extension Message {
    func makeMessageParts() -> [TranscriptItem]
}

messages // [Message]
    .map { $0.makeMessageParts() } // [[TranscriptItem]]
    .joined() // [TranscriptItem]

// This pattern is so common that we have another special kind of map for it.
messages // [Message]
    .flatMap { $0.makeMessageParts() }  // [TranscriptItem]
```

### Chaining together algorithms — [3:00]

```swift
// Raw loop:
var photos: [PhotoItem] = []
for item in transcript.reversed() {
    if let photo = item as? PhotoItem {
        photos.append(photo)
        if photos.count == 6 {
            break
        }
    }
}

// The above can be expressed more concisely by chaining together algorithms.
transcript
    .reversed() // [TranscriptItem]
    .compactMap { $0 as? PhotoItem } // [PhotoItem]
    .prefix(6) // [PhotoItem]

// This gives us more flexibility to express this code more clearly.
transcript
    .compactMap { $0 as? PhotoItem } // [PhotoItem]
    .suffix(6) // [PhotoItem]
    .reversed() // [PhotoItem]
```

### Lazy adapters — [4:19]

```swift
extension Message {
    func makeMessageParts() -> [TranscriptItem]
}

messages
    .map { $0.makeMessageParts() } // [[TranscriptItem]]
    .joined() // FlattenSequence<[[TranscriptItem]]>
```

### Lazy algorithm chains — [4:58]

```swift
transcript
    .lazy // LazySequence<[TranscriptItem]>
    .compactMap { $0 as? PhotoItem } // LazyCompactMap<[TranscriptItem], PhotoItem>
    .suffix(6) // LazyCompactMap<ArraySlice<TranscriptItem>, PhotoItem>
    .reversed() // ReversedCollection<LazyCompactMap<ArraySlice<TranscriptItem>, PhotoItem>>
```

### Wrapping a lazy algorithm chain in an Array initializer — [5:48]

```swift
Array(
    transcript
        .lazy
        .compactMap { $0 as? PhotoItem }
        .suffix(6)
        .reversed()
)
```

### windows(ofCount:) — [7:13]

```swift
import Algorithms

let x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for window in x.windows(ofCount: 3) {
    print(window)
}

// Prints [0, 1, 2]
// Prints [1, 2, 3]
// Prints [2, 3, 4]
// Prints [3, 4, 5]
```

### adjacentPairs() — [7:30]

```swift
import Algorithms

let x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for (prev, next) in x.adjacentPairs() {
    print((prev, next))
}

// Prints (0, 1)
// Prints (1, 2)
// Prints (2, 3)
// Prints (3, 4)
```

### chunks(ofCount:) — [7:45]

```swift
import Algorithms

let x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for chunk in x.chunks(ofCount: 3) {
    print(chunk)
}

// Prints [0, 1, 2]
// Prints [3, 4, 5]
// Prints [6, 7, 8]
// Prints [9]
```

### chunked(on:) — [8:08]

```swift
import Algorithms

let x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for (isPrime, chunk) in x.chunked(on: \.isPrime) {
    print((isPrime, chunk))
}

// Prints (false, [0, 1])
// Prints (true, [2, 3])
// Prints (false, [4])
// Prints (true, [5])
```

### Recognizing the chunked(on:) pattern — [8:33]

```swift
// Raw loop:
var prev: Element?
for element in collection {
    if prev?.value != element.value {
        // do work
    }
    prev = element
}

// The above is just `chunked(on:)`.
for (value, chunk) in collection.chunked(on: \.value) {
    // do work
}
```

### Mapping, chunking, and joining — [8:49]

```swift
import Algorithms

extension Message {
    func makeMessageParts() -> [TranscriptItem]
}

transcript = Array(
    messages
        .lazy
        .flatMap { $0.makeMessageParts() }
        .chunked { $1.date.timeIntervalSince($0.date) < 60 * 60 }
        .joined { DateItem(date: $1.first!.date) }
)
```

### Double-ended queues — [14:56]

```swift
var queue: Deque = ["A", "B", "C"]

queue.append("D")
queue.append("E")
queue.removeFirst()  // "A"
queue.removeFirst()  // "B"

queue.prepend("F")
queue.prepend("G")
queue.removeLast()   // "E"
queue.removeLast()   // "D"
```

### Deque protocol conformances — [15:46]

```swift
var items: Deque = ["D", "E", "f"]
print(items[1])  // "E"
items[2] = "F"
items.insert(contentsOf: ["A", "B", "C"], at: 0)
print(items[1])  // "B"
```

### Accessing elements is still efficient — [17:31]

```swift
var items: Deque = ["D", "E", "F"]
print(items[1])  // "E"
items.insert(contentsOf: ["A", "B", "C"], at: 0)
print(items[1])  // "B"
```

### Removing elements at random is twice as fast on average — [18:39]

```swift
var items: Deque = ["A", "B", "C", "D", "E", "F"]
items.removeSubrange(1 ..< 3)
```

### Unordered sets — [19:33]

```swift
let first: Set = ["A", "B", "C", "D", "E", "F"]
print(first)  // ["B", "E", "C", "F", "D", "A"]
let second: Set = ["A", "B", "C", "D", "E", "F"]
print(second)  // ["A", "D", "E", "F", "C", "B"]
print(first == second)  // true
```

### Ordered sets — [20:26]

```swift
let first: OrderedSet = ["A", "B", "C", "D", "E", "F"]
print(first)         // ["A", "B", "C", "D", "E", "F"]

let second: OrderedSet = ["F", "E", "D", "C", "B", "A"]

print(first == second)                      // false
print(first.unordered == second.unordered)  // true
```

### Ordered sets resemble how arrays work — [21:04]

```swift
var items: OrderedSet = ["E", "D", "C", "B", "A"]
items[3]  // "B"
items.append("F")         // (inserted: true, index: 5)
items.insert("B", at: 1)  // (inserted: false, index: 3)
items.remove("E")
items.sort()
items.shuffle()
```

### Ordered sets implement high-level set operations — [22:32]

```swift
var items: OrderedSet = ["B", "D", "E"]
items.formUnion(["A", "B", "C", "F"])
items.subtract(["A", "B", "G"])

let other: OrderedSet = ["C", "D", "E", "F"]
print(items == other)  // false
print(items.unordered == other.unordered)  // true
```

### Ordered dictionaries — [26:46]

```swift
var dict: OrderedDictionary = [2: "two", 1: "one", 0: "zero"]

print(dict[1])  // Optional("one")
print(dict)     // [2: "two", 1: "one", 0: "zero"]

dict[3] = "three"
dict[1] = nil
print(dict)     // [2: "two", 0: "zero", 3: "three"]
```

### Subscripting always means the keying subscript — [27:38]

```swift
var dict: OrderedDictionary = [2: "two", 0: "zero", 3: "three"]

print(dict[0])           // Optional("zero")       

print(dict.elements[0])  // (key: 2, value: "two")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10256/8/389DAED7-3871-4195-95B0-59E7F10A5E52/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10256/8/389DAED7-3871-4195-95B0-59E7F10A5E52/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10256) — developer.apple.com. Indexed for agent consumption._
