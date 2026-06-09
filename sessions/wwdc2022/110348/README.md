---
id: "wwdc2022-110348"
event: "wwdc2022"
year: 2022
title: "Build your first app in Swift Playgrounds"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110348"
topics: ["Business & Education", "Developer Tools", "Essentials", "Health & Fitness", "Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build your first app in Swift Playgrounds

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110348](https://developer.apple.com/videos/play/wwdc2022/110348)

Learn how you can easily prototype and build apps with Swift Playgrounds. We’ll show you how to create an app from a blank project, build its interface with SwiftUI, and use Swift Package Manager to add extra functionality from an open source package. We'll also explore how you can debug issues using Previews and the console and take you through submitting an app to App Store Connect for distribution via TestFlight.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,103 words)

## Code Snippets

### First Tea Item — [3:31]

```swift
Text("Jasmine Green")
```

### List Of Teas — [3:39]

```swift
Text("Jasmine Green")
Text("English Breakfast")
Text("Byte's Oolong")
Text("Golden Tippy Assam")
Text("Matt P's Tea Party")
Text("Darjeeling")
Text("Genmaicha")
Text("Jasmine Green")
Text("Vanilla Rooibos")
```

### OrderedSet of Teas — [4:45]

```swift
let teas: OrderedSet<String> = ["Byte's Oolong", "Golden Tippy Assam", "English Breakfast", "Matt P's Tea Party", "Darjeeling", "Genmaicha", "Jasmine Green", "Vanilla Rooibos"]
```

### ForEach View — [5:28]

```swift
ForEach(teas, id: \.self) { tea in
     Text(tea)
}
```

### Initial Preview Provider — [8:45]

```swift
struct TeaWheelView_Previews: PreviewProvider {
    static let items: [String] = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    static var previews: some View {
        Text("Hello, world!")
    }
}
```

### Preview Provider with TeaWheelView — [9:22]

```swift
struct TeaWheelView_Previews: PreviewProvider {
    static let items: [String] = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    static var previews: some View {
        TeaWheelView(items, id: \.self)
            .padding()
    }
}
```

### TeaWheelView in Assistant Tab — [10:40]

```swift
TeaWheelView(dataSource.teas, action: { tea in
    lastPickedTea = tea
    showPickAlert = true
})
```

### Preview Provider with Print Statement — [11:55]

```swift
struct TeaWheelView_Previews: PreviewProvider {
    static let items: [String] = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    static var previews: some View {
        TeaWheelView(items, id: \.self) {
            print($0)
        }
            .padding()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110348/5/EF06F7AC-5379-4AFF-A0AB-FD1413B78098/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110348/5/EF06F7AC-5379-4AFF-A0AB-FD1413B78098/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110348) — developer.apple.com. Indexed for agent consumption._