---
id: "wwdc2021-10017"
event: "wwdc2021"
year: 2021
title: "Bring Core Data concurrency to Swift and SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10017"
topics: ["Swift", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Bring Core Data concurrency to Swift and SwiftUI

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10017](https://developer.apple.com/videos/play/wwdc2021/10017)

Discover how Core Data is adopting the new concurrency capabilities of Swift 5.5, leading to more concise, efficient, and safe asynchronous code. We'll show you how to update Core Data in your apps to work with concurrency, and detail the many other improvements throughout the framework that make working with Swift and SwiftUI more expressive and powerful.

**Keywords:** `async`, `await`, `batch insert request`, `.binary`, `core data`, `data persistence`, `dictionary`, `dynamic configuration`, `earthquakes app`, `enqueued`, `fetch request`, `.inmemory`, `lazy entity resolution`, `managed object`, `managed object context`, `nsattributedescription`, `nsattributedescription.attributetype`, `nsmanagedobjectcontext`, `nspersistentcontainer`, `nspersistentstorecoordinator`, `perform`, `performandwait`, `perform and wait`, `perform(.enqueued)`, `persist data`, `persistence`, `persistent store`, `predicates`, `routing errors`, `sectioned fetching`, `sectionedfetchrequest`, `sectionidentifier`, `shared data`, `sort descriptors`, `sort order`, `.sqlite`, `swift`, `swift concurrency`, `swiftui`, `try await`, `.xml`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,075 words)

## Documentation & Resources

- [Loading and displaying a large data feed](https://developer.apple.com/documentation/SwiftUI/loading-and-displaying-a-large-data-feed) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/loading-and-displaying-a-large-data-feed
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/loading-and-displaying-a-large-data-feed.json

## Code Snippets

### FetchRequest dynamic configuration: sort descriptors — [20:36]

```swift
private let sorts = [(
    name: "Time",
    descriptors: [SortDescriptor(\Quake.time, order: .reverse)]
), (
    name: "Time",
    descriptors: [SortDescriptor(\Quake.time, order: .forward)]
), (
    name: "Magnitude",
    descriptors: [SortDescriptor(\Quake.magnitude, order: .reverse)]
), (
    name: "Magnitude",
    descriptors: [SortDescriptor(\Quake.magnitude, order: .forward)]
)]

struct ContentView: View {
    @FetchRequest(sortDescriptors: [SortDescriptor(\Quake.time, order: .reverse)])
    private var quakes: FetchedResults<Quake>

    @State private var selectedSort = SelectedSort()

    var body: some View {
        List(quakes) { quake in
            QuakeRow(quake: quake)
        }
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                SortMenu(selection: $selectedSort)
                .onChange(of: selectedSort) { _ in
                    let sortBy = sorts[selectedSort.index]
                    quakes.sortDescriptors = sortBy.descriptors
                }
            }
        }
    }

    struct SelectedSort: Equatable {
        var by = 0
        var order = 0
        var index: Int { by + order }
    }

    struct SortMenu: View {
        @Binding private var selectedSort: SelectedSort

        init(selection: Binding<SelectedSort>) {
            _selectedSort = selection
        }

        var body: some View {
            Menu {
                Picker("Sort By", selection: $selectedSort.by) {
                    ForEach(Array(stride(from: 0, to: sorts.count, by: 2)), id: \.self) { index in
                        Text(sorts[index].name).tag(index)
                    }
                }
                Picker("Sort Order", selection: $selectedSort.order) {
                    let sortBy = sorts[selectedSort.by + selectedSort.order]
                    let sortOrders = sortOrders(for: sortBy.name)
                    ForEach(0..<sortOrders.count, id: \.self) { index in
                        Text(sortOrders[index]).tag(index)
                    }
                }
            } label: {
                Label("More", systemImage: "ellipsis.circle")
            }
            .pickerStyle(InlinePickerStyle())
        }

        private func sortOrders(for name: String) -> [String] {
            switch name {
            case "Magnitude":
                return ["Highest to Lowest", "Lowest to Highest"]
            case "Time":
                return ["Newest on Top", "Oldest on Top"]
            default:
                return []
            }
        }
    }
}
```

### FetchRequest dynamic configuration: predicates — [21:33]

```swift
struct ContentView: View {
    @FetchRequest(sortDescriptors: [SortDescriptor(\Quake.time, order: .reverse)])
    private var quakes: FetchedResults<Quake>

    @State private var searchText = ""
    var query: Binding<String> {
        Binding {
            searchText
        } set: { newValue in
            searchText = newValue
            quakes.nsPredicate = newValue.isEmpty
                               ? nil
                               : NSPredicate(format: "place CONTAINS %@", newValue)
        }
    }

    var body: some View {
        List(quakes) { quake in
            QuakeRow(quake: quake)
        }
        .searchable(text: query)
    }
}
```

### SectionedFetchRequest — [23:26]

```swift
extension Quake {
    lazy var dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "MMMM d, yyyy"
        return formatter
    }()

    @objc var day: String {
        return dateFormatter.string(from: time)
    }
}

struct ContentView: View {
    @SectionedFetchRequest(
        sectionIdentifier: \.day,
        sortDescriptors: [SortDescriptor(\Quake.time, order: .reverse)])
    private var quakes: SectionedFetchResults<String, Quake>

    var body: some View {
        List {
            ForEach(quakes) { section in
                Section(header: Text(section.id)) {
                    ForEach(section) { quake in
                        QuakeRow(quake: quake)
                    }
                }
            }
        }
    }
}
```

### SectionedFetchRequest dynamic configuration: sort descriptors — [24:56]

```swift
extension Quake {
    lazy var dateFormatter: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "MMMM d, yyyy"
        return formatter
    }()

    @objc var day: String {
        return dateFormatter.string(from: time)
    }

    @objc var magnitude_str: String {
        return "\(magnitude)"
    }
}

private let sorts = [(
    name: "Time",
    descriptors: [SortDescriptor(\Quake.time, order: .reverse)],
    section: \Quake.day
), (
    name: "Time",
    descriptors: [SortDescriptor(\Quake.time, order: .forward)],
    section: \Quake.day
), (
    name: "Magnitude",
    descriptors: [SortDescriptor(\Quake.magnitude, order: .reverse)],
    section: \Quake.magnitude_str
), (
    name: "Magnitude",
    descriptors: [SortDescriptor(\Quake.magnitude, order: .forward)],
    section: \Quake.magnitude_str
)]

struct ContentView: View {
    @SectionedFetchRequest(
        sectionIdentifier: \.day,
        sortDescriptors: [SortDescriptor(\Quake.time, order: .reverse)])
    private var quakes: SectionedFetchResults<String, Quake>

    @State private var selectedSort = SelectedSort()

    var body: some View {
        List {
            ForEach(quakes) { section in
                Section(header: Text(section.id)) {
                    ForEach(section) { quake in
                        QuakeRow(quake: quake)
                    }
                }
            }
        }
        .toolbar {
            ToolbarItem(placement: .primaryAction) {
                SortMenu(selection: $selectedSort)
                .onChange(of: selectedSort) { _ in
                    let sortBy = sorts[selectedSort.index]
                    let config = quakes
                    config.sectionIdentifier = sortBy.section
                    config.sortDescriptors = sortBy.descriptors
                }
            }
        }
    }

    struct SelectedSort: Equatable {
        var by = 0
        var order = 0
        var index: Int { by + order }
    }

    struct SortMenu: View {
        @Binding private var selectedSort: SelectedSort

        init(selection: Binding<SelectedSort>) {
            _selectedSort = selection
        }

        var body: some View {
            Menu {
                Picker("Sort By", selection: $selectedSort.by) {
                    ForEach(Array(stride(from: 0, to: sorts.count, by: 2)), id: \.self) { index in
                        Text(sorts[index].name).tag(index)
                    }
                }
                Picker("Sort Order", selection: $selectedSort.order) {
                    let sortBy = sorts[selectedSort.by + selectedSort.order]
                    let sortOrders = sortOrders(for: sortBy.name)
                    ForEach(0..<sortOrders.count, id: \.self) { index in
                        Text(sortOrders[index]).tag(index)
                    }
                }
            } label: {
                Label("More", systemImage: "ellipsis.circle")
            }
            .pickerStyle(InlinePickerStyle())
        }

        private func sortOrders(for name: String) -> [String] {
            switch name {
            case "Magnitude":
                return ["Highest to Lowest", "Lowest to Highest"]
            case "Time":
                return ["Newest on Top", "Oldest on Top"]
            default:
                return []
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10017/4/F075C8AE-C8D2-40F9-8520-018581E3A771/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10017/4/F075C8AE-C8D2-40F9-8520-018581E3A771/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10017) — developer.apple.com. Indexed for agent consumption._
