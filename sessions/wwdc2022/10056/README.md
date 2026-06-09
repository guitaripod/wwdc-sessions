---
id: "wwdc2022-10056"
event: "wwdc2022"
year: 2022
title: "Compose custom layouts with SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10056"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Compose custom layouts with SwiftUI

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10056](https://developer.apple.com/videos/play/wwdc2022/10056)

SwiftUI now offers powerful tools to level up your layouts and arrange views for your app’s interface. We’ll introduce you to the Grid container, which helps you create highly customizable, two-dimensional layouts, and show you how you can use the Layout protocol to build your own containers with completely custom behavior. We’ll also explore how you can create seamless animated transitions between your layout types, and share tips and best practices for creating great interfaces.


**Keywords:** `anylayout`, `apply different layouts`, `arrange buttons`, `bounds`, `button`, `cache: inout void`, `cat`, `columns`, `dog`, `equalwidthhstack`, `equatable`, `frame()`, `geometry reader`, `goldfish`, `grid`, `gridcolumnalignment`, `gridrow`, `identifiable`, `layout`, `layout protocol`, `layout tools`, `lazy grid`, `lazyhgrid`, `leading edge`, `.origin`, `placesubviews`, `rows`, `sizethatfits`, `trailing edge`, `view`, `view modifier`, `view spacing`, `viewthatfits`, `vstack`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,634 words)

## Documentation & Resources

- [Layout containers](https://developer.apple.com/documentation/swiftui/layout-fundamentals) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/layout-fundamentals
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/layout-fundamentals.json
- [ViewThatFits](https://developer.apple.com/documentation/SwiftUI/ViewThatFits) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ViewThatFits
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ViewThatFits.json
- [AnyLayout](https://developer.apple.com/documentation/SwiftUI/AnyLayout) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/AnyLayout
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/AnyLayout.json
- [Layout](https://developer.apple.com/documentation/SwiftUI/Layout) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Layout
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Layout.json
- [Grid](https://developer.apple.com/documentation/SwiftUI/Grid) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Grid
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Grid.json
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/SwiftUI/composing-custom-layouts-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/composing-custom-layouts-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/composing-custom-layouts-with-swiftui.json

## Code Snippets

### Grid with explicit rows — [4:28]

```swift
struct Leaderboard: View {
    var body: some View {
        Grid {
            GridRow {
                Text("Cat")
                ProgressView(value: 0.5)
                Text("25")
            }
            GridRow {
                Text("Goldfish")
                ProgressView(value: 0.2)
                Text("9")
            }
            GridRow {
                Text("Dog")
                ProgressView(value: 0.3)
                Text("16")
            }
        }
    }
}
```

### Data model — [5:16]

```swift
struct Pet: Identifiable, Equatable {
    let type: String
    var votes: Int = 0
    var id: String { type }

    static var exampleData: [Pet] = [
        Pet(type: "Cat", votes: 25),
        Pet(type: "Goldfish", votes: 9),
        Pet(type: "Dog", votes: 16)
    ]
}
```

### Final Leaderboard — [5:41]

```swift
struct Leaderboard: View {
    var pets: [Pet]
    var totalVotes: Int

    var body: some View {
        Grid(alignment: .leading) {
            ForEach(pets) { pet in
                GridRow {
                    Text(pet.type)
                    ProgressView(
                        value: Double(pet.votes),
                        total: Double(totalVotes))
                    Text("\(pet.votes)")
                        .gridColumnAlignment(.trailing)
                }

                Divider()
            }
        }
        .padding()
    }
}
```

### Layout protocol stubs for required methods — [10:53]

```swift
struct MyEqualWidthHStack: Layout {
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout Void
    ) -> CGSize {
        // Return a size.
    }

    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Subviews,
        cache: inout Void
    ) {
        // Place child views.
    }
}
```

### Maximum size helper method — [13:44]

```swift
private func maxSize(subviews: Subviews) -> CGSize {
    let subviewSizes = subviews.map { $0.sizeThatFits(.unspecified) }
    let maxSize: CGSize = subviewSizes.reduce(.zero) { currentMax, subviewSize in
        CGSize(
            width: max(currentMax.width, subviewSize.width),
            height: max(currentMax.height, subviewSize.height))
    }

    return maxSize
}
```

### Spacing helper method — [15:40]

```swift
private func spacing(subviews: Subviews) -> [CGFloat] {
    subviews.indices.map { index in
        guard index < subviews.count - 1 else { return 0 }
        return subviews[index].spacing.distance(
            to: subviews[index + 1].spacing,
            along: .horizontal)
    }
}
```

### Size that fits implementation — [16:33]

```swift
func sizeThatFits(
    proposal: ProposedViewSize,
    subviews: Subviews,
    cache: inout Void
) -> CGSize {
    // Return a size.
    guard !subviews.isEmpty else { return .zero }

    let maxSize = maxSize(subviews: subviews)
    let spacing = spacing(subviews: subviews)
    let totalSpacing = spacing.reduce(0) { $0 + $1 }

    return CGSize(
        width: maxSize.width * CGFloat(subviews.count) + totalSpacing,
        height: maxSize.height)
}
```

### Place subviews implementation — [16:51]

```swift
func placeSubviews(
    in bounds: CGRect,
    proposal: ProposedViewSize,
    subviews: Subviews,
    cache: inout Void
) {
    // Place child views.
    guard !subviews.isEmpty else { return }

    let maxSize = maxSize(subviews: subviews)
    let spacing = spacing(subviews: subviews)

    let placementProposal = ProposedViewSize(width: maxSize.width, height: maxSize.height)
    var x = bounds.minX + maxSize.width / 2

    for index in subviews.indices {
        subviews[index].place(
            at: CGPoint(x: x, y: bounds.midY),
            anchor: .center,
            proposal: placementProposal)
        x += maxSize.width + spacing[index]
    }
}
```

### Custom layout instantiation — [18:07]

```swift
MyEqualWidthHStack {
    ForEach($pets) { $pet in
        Button {
            pet.votes += 1
        } label: {
            Text(pet.type)
                .frame(maxWidth: .infinity)
        }
        .buttonStyle(.bordered)
    }
}
```

### Buttons helper view — [20:12]

```swift
struct Buttons: View {
    @Binding var pets: [Pet]

    var body: some View {
        ForEach($pets) { $pet in
            Button {
                pet.votes += 1
            } label: {
                Text(pet.type)
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
        }
    }
}
```

### Final voting buttons view — [21:08]

```swift
struct StackedButtons: View {
    @Binding var pets: [Pet]

    var body: some View {
        ViewThatFits {
            MyEqualWidthHStack {
                Buttons(pets: $pets)
            }
            MyEqualWidthVStack {
                Buttons(pets: $pets)
            }
        }
    }
}
```

### Radial size that fits — [22:30]

```swift
func sizeThatFits(
    proposal: ProposedViewSize,
    subviews: Subviews,
    cache: inout Void
)  -> CGSize {
    // Take whatever space is offered.
    return proposal.replacingUnspecifiedDimensions()
}
```

### Radial place subviews without offsets — [22:52]

```swift
func placeSubviews(
    in bounds: CGRect,
    proposal: ProposedViewSize,
    subviews: Subviews,
    cache: inout Void
) {
    let radius = min(bounds.size.width, bounds.size.height) / 3.0
    let angle = Angle.degrees(360.0 / Double(subviews.count)).radians
    let offset = 0 // This depends on rank...

    for (index, subview) in subviews.enumerated() {
        var point = CGPoint(x: 0, y: -radius)
            .applying(CGAffineTransform(
                rotationAngle: angle * Double(index) + offset))

        point.x += bounds.midX
        point.y += bounds.midY

        subview.place(at: point, anchor: .center, proposal: .unspecified)
    }
}
```

### Rank value — [23:42]

```swift
private struct Rank: LayoutValueKey {
    static let defaultValue: Int = 1
}

extension View {
    func rank(_ value: Int) -> some View {
        layoutValue(key: Rank.self, value: value)
    }
}
```

### Radial place subviews with offsets — [24:21]

```swift
func placeSubviews(
    in bounds: CGRect,
    proposal: ProposedViewSize,
    subviews: Subviews,
    cache: inout Void
) {
    let radius = min(bounds.size.width, bounds.size.height) / 3.0
    let angle = Angle.degrees(360.0 / Double(subviews.count)).radians

    let ranks = subviews.map { subview in
        subview[Rank.self]
    }
    let offset = getOffset(ranks)

    for (index, subview) in subviews.enumerated() {
        var point = CGPoint(x: 0, y: -radius)
            .applying(CGAffineTransform(
                rotationAngle: angle * Double(index) + offset))
        point.x += bounds.midX
        point.y += bounds.midY
        subview.place(at: point, anchor: .center, proposal: .unspecified)
    }
}
```

### Final profile view — [25:18]

```swift
struct Profile: View {
    var pets: [Pet]
    var isThreeWayTie: Bool

    var body: some View {
        let layout = isThreeWayTie ? AnyLayout(HStackLayout()) : AnyLayout(MyRadialLayout())

        Podium() // Creates the background that shows ranks.
            .overlay(alignment: .top) {
                layout {
                    ForEach(pets) { pet in
                        Avatar(pet: pet)
                            .rank(rank(pet))
                    }
                }
                .animation(.default, value: pets)
            }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10056/5/F52141E2-6868-4629-A64D-83E618CD6CD5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10056/5/F52141E2-6868-4629-A64D-83E618CD6CD5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10056) — developer.apple.com. Indexed for agent consumption._