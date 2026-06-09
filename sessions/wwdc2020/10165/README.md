---
id: "wwdc2020-10165"
event: "wwdc2020"
year: 2020
title: "Embrace Swift type inference"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10165"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Embrace Swift type inference

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10165](https://developer.apple.com/videos/play/wwdc2020/10165)

Swift uses type inference to help you write clean, concise code without compromising type safety. We’ll show you how the compiler seeks out clues in your code to solve the type inference puzzle. Discover what happens when the compiler can't come to a solution, and find out how Xcode 12 integrates error tracking to help you understand and fix mistakes at compile time.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,171 words)

## Documentation & Resources

- [The Swift Programming Language](https://docs.swift.org/swift-book/) _guide_

## Code Snippets

### SmoothieList — [2:56]

```swift
import SwiftUI

struct SmoothieList: View {
    var smoothies: [Smoothie]

    @State var searchPhrase = ""

    var body: some View {
        FilteredList(
            smoothies,
            filterBy: \.title,
            isIncluded: { title in title.hasSubstring(searchPhrase) }
        ) { smoothie in
            SmoothieRowView(smoothie: smoothie)
        }
    }
}

extension String {
    /// Returns `true` if this string contains the provided substring,
    /// or if the substring is empty. Otherwise, returns `false`.
    ///
    /// - Parameter substring: The substring to search for within
    ///   this string.
    func hasSubstring(_ substring: String) -> Bool {
        substring.isEmpty || contains(substring)
    }
}
```

### FilteredList — [3:53]

```swift
import SwiftUI

public struct FilteredList<Element, FilterKey, RowContent>: View
        where Element: Identifiable, RowContent: View {

    private let data: [Element]
    private let filterKey: KeyPath<Element, FilterKey>
    private let isIncluded: (FilterKey) -> Bool
    private let rowContent: (Element) -> RowContent

    public init(
        _ data: [Element],
        filterBy key: KeyPath<Element, FilterKey>,
        isIncluded: @escaping (FilterKey) -> Bool,
        @ViewBuilder rowContent: @escaping (Element) -> RowContent
    ) {
        self.data = data
        self.filterKey = key
        self.isIncluded = isIncluded
        self.rowContent = rowContent
    }

    public var body: some View {
        let filteredData = data.filter {
            isIncluded($0[keyPath: filterKey])
        }

        return List(filteredData, rowContent: rowContent)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10165/4/F5BC5595-D6B4-4C08-B9EC-E801F766386B/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10165) — developer.apple.com. Indexed for agent consumption._