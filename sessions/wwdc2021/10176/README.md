---
id: "wwdc2021-10176"
event: "wwdc2021"
year: 2021
title: "Craft search experiences in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10176"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Craft search experiences in SwiftUI

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10176](https://developer.apple.com/videos/play/wwdc2021/10176)

Discover how you can help people quickly find specific content within your apps. Learn how to use SwiftUI’s .searchable modifier in conjunction with other views to best incorporate search for your app. And we’ll show you how to elevate your implementation by providing search suggestions to help people understand the types of searches they can perform.

**Keywords:** `collections of data`, `configured search field`, `filter`, `finding data`, `implement search`, `issearching`, `native search`, `navigationview`, `navigation view`, `.onsubmit`, `results`, `search`, `searchable`, `.searchable`, `searchable modifier`, `search bar`, `.searchcompletion`, `search completion`, `search field`, `search field column`, `search query`, `search tab`, `side bar`, `suggestions`, `swiftui`, `toolbar`, `two column`, `weather app`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,894 words)

## Code Snippets

### Colors Suggestions — [0:10]

```swift
struct ColorsContentView: View {
    @State var text = ""

    var body: some View {
        NavigationView {
            Sidebar()
            DetailView()
        }
        .searchable(text: $text) {
           ForEach(suggestions) { suggestion in
                Button {
                    text = suggestion.text
                } label: {
                    ColorsSuggestionLabel(suggestion)
                }
            }
        }
    }
}
```

### New Searchable Modifier — [1:17]

```swift
ContentView()
.searchable(text: $text)
```

### Weather Search — [1:58]

```swift
NavigationView {
    WeatherList(text: $text) {
        ForEach(data) { item in
            WeatherCell(item)
        }
    }
}
.searchable(text: $text)
```

### Weather List — [3:11]

```swift
struct WeatherList: View {
    @Binding var text: String

    @Environment(\.isSearching)
    private var isSearching: Bool

    var body: some View {
        WeatherCitiesList()
            .overlay {
                if isSearching && !text.isEmpty {
                    WeatherSearchResults()
                }
            }
    }
}
```

### Colors Search — [5:07]

```swift
struct ColorsContentView: View {
    @State var text = ""

    var body: some View {
        NavigationView {
            Sidebar()
            DetailView()
        }
        .searchable(text: $text)
    }
}
```

### Colors Search with TV — [7:15]

```swift
struct ColorsContentView: View {
    @State var text = ""

    var body: some View {
        NavigationView {
            #if os(tvOS)
            TabView {
                Sidebar()
                ColorsSearch()
                    .searchable(text: $text)
            }
            #else
            Sidebar()
            DetailView()
            #endif
        }
        #if !os(tvOS)
        .searchable(text: $text)
        #endif
    }
}
```

### Colors Search Completions — [9:09]

```swift
struct ColorsContentView: View {
    @State var text = ""

    var body: some View {
        NavigationView {
            Sidebar()
            DetailView()
        }
        .searchable(text: $text) {
           ForEach(suggestions) { suggestion in
                ColorsSuggestionLabel(suggestion)
                    .searchCompletion(suggestion.text)
            }
        }
    }
}
```

### On Submit — [10:21]

```swift
ContentView()
.searchable(text: $text) {
    MySearchSuggestions()
}
.onSubmit(of: .search) {
    fetchResults()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10176/7/5699E756-ACAC-4EFA-801B-5709E5EDF434/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10176/7/5699E756-ACAC-4EFA-801B-5709E5EDF434/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10176) — developer.apple.com. Indexed for agent consumption._