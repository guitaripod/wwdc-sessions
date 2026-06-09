---
id: "wwdc2022-110352"
event: "wwdc2022"
year: 2022
title: "Embrace Swift generics"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110352"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Embrace Swift generics

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110352](https://developer.apple.com/videos/play/wwdc2022/110352)

Generics are a fundamental tool for writing abstract code in Swift. Learn how you can identify opportunities for abstraction as your code evolves, evaluate strategies for writing one piece of code with many behaviors, and discover language features in Swift 5.7 that can help you make generic code easier to write and understand.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,864 words)

## Documentation & Resources

- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### Complete example — [27:10]

```swift
protocol AnimalFeed {
  associatedtype CropType: Crop where CropType.Feed == Self
  static func grow() -> CropType
}

protocol Crop {
  associatedtype Feed: AnimalFeed where Feed.CropType == Self
  func harvest() -> Feed
}

protocol Animal {
  associatedtype Feed: AnimalFeed
  func eat(_ food: Feed)
}

struct Farm {
  func feed(_ animal: some Animal) {
    let crop = type(of: animal).Feed.grow()
    let produce = crop.harvest()
    animal.eat(produce)
  }

  func feedAll(_ animals: [any Animal]) {
    for animal in animals {
      feed(animal)
    }
  }
}

struct Cow: Animal {
  func eat(_ food: Hay) {}
}

struct Hay: AnimalFeed {
  static func grow() -> Alfalfa {
    Alfalfa()
  }
}

struct Alfalfa: Crop {
  func harvest() -> Hay {
    Hay()
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110352/3/961EB9A0-3340-443A-8C57-8665B9034F1D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110352/3/961EB9A0-3340-443A-8C57-8665B9034F1D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110352) — developer.apple.com. Indexed for agent consumption._
