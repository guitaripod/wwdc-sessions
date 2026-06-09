---
id: "wwdc2020-10643"
event: "wwdc2020"
year: 2020
title: "Build a SwiftUI view in Swift Playgrounds"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10643"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build a SwiftUI view in Swift Playgrounds

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10643](https://developer.apple.com/videos/play/wwdc2020/10643)

Easily prototype and play around with SwiftUI views when you use them with Swift Playgrounds. We’ll show you how to build a SwiftUI view in a Xcode-compatible playground, and explore tools to help you easily edit and preview your code. For more on Swift Playgrounds, check out our interactive challenge, “Swan's Quest”, and learn to build your own by watching “Create Swift Playgrounds Content for iPad and Mac”.

**Keywords:** `ipad`, `playgrounds`, `swift`, `swift playgrounds`, `swiftui`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,343 words)

## Code Snippets

### Set up for SwiftUI — [2:30]

```swift
import SwiftUI
import PlaygroundSupport
```

### Create a simple SwiftUI view — [2:46]

```swift
struct ProgressView: View {

  var body: some View {
    Text("Hello, world!")
  }

}
```

### Show a SwiftUI live view — [3:12]

```swift
PlaygroundPage.current.setLiveView(ProgressView())
```

### Create a blue circle — [4:01]

```swift
Circle()
	.stroke(lineWidth: 25)
	.foregroundColor(.blue)
```

### Add some padding — [5:06]

```swift
ProgressView().padding(150)
```

### Create an empty ZStack — [5:30]

```swift
ZStack { }
```

### Add a text view — [5:51]

```swift
Text("25%")
```

### Make a struct public — [9:24]

```swift
public struct ProgressView: View {
```

### Make a view's body property public — [9:38]

```swift
public var body: some View {
```

### Make a view's initializer public — [9:45]

```swift
public init(_ progress: Double = 0.3) {
```

### Create another SwiftUI view — [10:12]

```swift
struct Preview: View {

  var body: some View {
    // ...
  }

}
```

### Create a VStack of progress views — [10:21]

```swift
VStack(spacing: 30) {
  ProgressView()
  ProgressView()
}
```

### Add padding to a view — [10:44]

```swift
.padding(100)
```

### Add a system background color to a view — [10:51]

```swift
.background(Color(UIColor.secondarySystemBackground))
```

### Initialize the Preview view — [11:19]

```swift
Preview()
```

### Use an environment modifier to preview dark mode — [11:35]

```swift
.environment(\.colorScheme, .dark)
```

### Create a state variable for tracking progress — [12:12]

```swift
@State var progress = 0.25
```

### Pass the progress to the ProgressView initializer — [12:18]

```swift
ProgressView(progress)
```

### Create a method for incrementing progress — [12:32]

```swift
func increment() {
  self.progress += 0.25
}
```

### Add animation to the increment method — [12:40]

```swift
func increment() {
  withAnimation {
    self.progress += 0.25
  }
}
```

### Create a button — [12:52]

```swift
Button(action: increment)
```

### Add a text label to a button — [13:01]

```swift
Button(action: increment) {
  Text("Increment Progress")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10643/4/1EF945FC-088B-4D21-9838-F7CE638EF399/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10643) — developer.apple.com. Indexed for agent consumption._
