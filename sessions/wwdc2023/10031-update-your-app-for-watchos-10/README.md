---
id: "wwdc2023-10031"
event: "wwdc2023"
year: 2023
title: "Update your app for watchOS 10"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10031"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Update your app for watchOS 10

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10031](https://developer.apple.com/videos/play/wwdc2023/10031)

Join us as we update an Apple Watch app to take advantage of the latest features in watchOS 10. In this code-along, we’ll show you how to use the latest SwiftUI APIs to maximize glanceability and reorient app navigation around the Digital Crown.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,747 words)

## Documentation & Resources

- [Updating your app and widgets for watchOS 10](https://developer.apple.com/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/updating-your-app-and-widgets-for-watchos-10.json
- [Human Interface Guidelines: watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-watchos

## Code Snippets

### NavigationSplitView — [4:02]

```swift
NavigationSplitView {
    List(backyardsData.backyards, selection: $selectedBackyard) { backyard in
        BackyardCell(backyard: backyard)
    }
    .listStyle(.carousel)
} detail: {
    if let selectedBackyard {
        BackyardView(backyard: selectedBackyard)
    } else {
        BackyardUnavailableView()
    }
}
```

### Vertical TabView — [6:18]

```swift
TabView {
    TodayView()
        .navigationTitle("Today")
    HabitatGaugeView(level: $waterLevel, habitatType: .water, tintColor: .blue)
        .navigationTitle("Water")
    HabitatGaugeView(level: $foodLevel, habitatType: .food, tintColor: .green)
        .navigationTitle("Food")
    List {
        VisitorView()
            .navigationTitle("Visitors")
    }
}
.tabViewStyle(.verticalPage)
```

### Add refill button to Toolbar — [8:37]

```swift
.toolbar {
    ToolbarItemGroup(placement: .bottomBar) {
        Spacer()
        Button {
            level = Int(min(100, Double(level) + 5))
        } label: {
            Label("Add", systemImage: "plus")
        }
    }
}
```

### HabitatGaugeView background color function and variables — [9:48]

```swift
func backgroundColor(_ level: Int, for type: HabitatType) -> Color {
    let color: Color = type == .food ? .green : .blue
    return level < 40 ? .red : color
}

var waterColor: Color {
    backgroundColor(waterLevel, for: .water)
}

var foodColor: Color {
    backgroundColor(foodLevel, for: .food)
}
```

### .containerBackground within TabView — [10:10]

```swift
TabView {
    TodayView()
        .navigationTitle("Today")
        .containerBackground(Color.accentColor.gradient, for: .tabView)
    HabitatGaugeView(level: $waterLevel, habitatType: .water, tintColor: waterColor)
        .navigationTitle("Water")
        .containerBackground(waterColor.gradient, for: .tabView)
    HabitatGaugeView(level: $foodLevel, habitatType: .food, tintColor: foodColor)
        .navigationTitle("Food")
        .containerBackground(foodColor.gradient, for: .tabView)
    List {
        VisitorView()
            .navigationTitle("Visitors")
            .containerBackground(Color.accentColor.gradient, for: .tabView)
    }
}
.tabViewStyle(.verticalPage)
.environmentObject(backyard)
.navigationTitle(backyard.displayName)
```

### Add material to the backyard name — [11:38]

```swift
.foregroundStyle(.secondary)
.background(Material.ultraThin, in: RoundedRectangle(cornerRadius: 7))
```

### Visitor score overlay with materials — [12:15]

```swift
.overlay(alignment: .topTrailing) {
    Text("\(backyard.visitorScore)")
        .frame(width: 25, height: 25)
        .foregroundStyle(.secondary)
        .background(.ultraThinMaterial, in: .circle)
        .padding(.top, 5)
}
```

### Light materials — [12:20]

```swift
.environment(\.colorScheme, .light)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10031/4/365BFCEA-3567-4F2E-85DC-D6DF144F9B5C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10031/4/365BFCEA-3567-4F2E-85DC-D6DF144F9B5C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10031) — developer.apple.com. Indexed for agent consumption._
