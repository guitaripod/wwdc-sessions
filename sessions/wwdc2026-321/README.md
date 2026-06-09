# Dive into lazy stacks and scrolling with SwiftUI

**Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-321](https://developer.apple.com/videos/play/wwdc2026/321)

Discover the inner workings of lazy stacks in SwiftUI. We’ll explore how LazyVStack and LazyHStack estimate sizes, lazily load subviews, and prefetch content to deliver smooth scrolling experiences. We’ll also cover advanced performance optimizations, state management best practices, and tips for precise programmatic scrolling. To get the most out of this session, we recommend basic familiarity with SwiftUI layout using stacks.

**Keywords:** `screenshots`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Grouping data with lazy stack views](https://developer.apple.com/documentation/SwiftUI/Grouping-Data-with-Lazy-Stack-Views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Grouping-Data-with-Lazy-Stack-Views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Grouping-Data-with-Lazy-Stack-Views.json

## Code Snippets

### Origami app — [1:23]

```swift
// Origami app

struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(steps) { step in
                    StepView(step: step)
                }
            }
        }
    }
}

struct StepView: View { /* ... */ }
```

### Horizontally scrolling showcase — [5:11]

```swift
// Horizontally scrolling showcase

struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(steps) { step in
                    StepView(step: step)
                }
                Showcase()
            }
        }
    }
}

struct StepView: View { /* ... */ }

struct Showcase: View {
    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack {
                ForEach(photos) { photo in
                    PhotoView(photo: photo)
                }
            }
        }
    }
}
```

### Showcase section — [6:30]

```swift
// Showcase section

struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack(pinnedViews: [.sectionHeaders]) {
                ForEach(steps) { step in
                    StepView(step: step)
                }
                Showcase()
            }
        }
    }
}

struct StepView: View { /* ... */ }

struct Showcase: View {
    var body: some View {
        Section {
            ForEach(photos) { photo in
                PhotoView(photo: photo)
            }
        } header: { /* ... */ }
    }
}
```

### Scroll effect — [7:04]

```swift
// Scroll effect

struct ContentView: View { /* ... */ }

struct StepView: View { /* ... */ }

struct Showcase: View {
    var body: some View {
        Section {
            ForEach(photos) { photo in
                PhotoView(photo: photo)
                    .scrollTransition { effect, phase in
                        effect
                            .rotationEffect(.degrees(phase.value * 20))
                            .scaleEffect(1 + phase.value * 0.2)
                    }
            }
        } header: { /* ... */ }
    }
}
```

### Scroll effect — [7:36]

```swift
// Scroll effect

struct ContentView: View { /* ... */ }

struct StepView: View { /* ... */ }

struct Showcase: View {
    var body: some View {
        Section {
            ForEach(photos) { photo in
                PhotoView(photo: photo)
                    .scrollTransition { effect, phase in
                        effect
                            .scaleEffect(1 - abs(phase.value) * 0.1)
                    }
            }
        } header: { /* ... */ }
    }
}
```

### Scroll to Showcase button — [8:20]

```swift
// Absolute offset

struct ContentView: View {
    @State var isScrollToShowcaseVisible = false

    var body: some View {
        ScrollView { /* ... */ }
            .overlay(alignment: .bottom) { /* ... */ }
            .onScrollGeometryChange(for: Bool.self) { geo in
                geo.contentOffset.y <= 100
            } action: { _, newValue in
                self.isScrollToShowcaseVisible = newValue
            }
    }
}
```

### Scroll to Showcase button — [8:51]

```swift
// Absolute offset

struct ContentView: View {
    @State var isScrollToShowcaseVisible = false

    var body: some View {
        ScrollView { /* ... */ }
            .overlay(alignment: .bottom) { /* ... */ }
            .onScrollTargetVisibilityChange(
                idType: Step.ID.self,
                threshold: 0.8
            ) { visibleIDs in
                isScrollToShowcaseVisible = shouldShowScrollButton(visibleIDs: visibleIDs)
            }
    }
}
```

### One resolved subview — [9:29]

```swift
// Origami

struct ContentView: View {
    var body: some View {
        ScrollView {
            LazyVStack {
                ForEach(steps) { step in
                    StepView(step: step)
                }
            }
        }
    }
}

struct StepView: View { /* ... */ }
```

### Multiple resolved subviews — [10:03]

```swift
// Multiple subviews

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    var body: some View {
        StepDiagram(/* ... */)
        StepInstructions(/* ... */)
    }
}
```

### Dynamic number of subviews — [10:52]

```swift
// Dynamic number of views

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    @Environment(\.detailLevel) var detailLevel

    var body: some View {
        if step.isVisible(in: detailLevel) {
            VStack { /* ... */ }
        }
    }
}
```

### Filtering on the view level — [11:46]

```swift
// Dynamic number of views

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    @Environment(\.detailLevel) var detailLevel
    @Environment(\.writingStyle) var writingStyle

    var body: some View {
        if step.isVisible(in: detailLevel) { /* ... */ }
    }
}
```

### Filtering on the data level — [12:15]

```swift
// Filter at the data level

struct ContentView: View {
    @Query var steps: [Step]

    init(detailLevel: DetailLevel) {
        _steps = Query(filter: #Predicate<Step> { step in
            step.detailLevel >= detailLevel
        })
    }

    var body: some View { /* ... */ }
}

struct StepView: View { /* ... */ }
```

### Optional unwrapping — [12:35]

```swift
// Optional unwrapping

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    @Environment(\.apiToken) var token

    var body: some View {
        if let token { /* ... */ }
    }
}
```

### Optional unwrapping — [12:48]

```swift
// Optional unwrapping

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    @Environment(NetworkClient.self) var networkClient

    var body: some View { /* ... */ }
}
```

### Loading more content — [15:28]

```swift
// Loading more content

struct Showcase: View {
    @State var pager = ShowcasePager()

    var body: some View {
        ForEach(pager.pages) { page in
            PageView(page: page)
        }
        if !pager.atEnd {
            ProgressView()
                .progressViewStyle(.circular)
                .onAppear {
                    pager.fetchPage()
                }
        }
    }
}
```

### Setting up lazy stack subview in onAppear — [15:53]

```swift
// onAppear

struct StepView: View {
    let id: Step.ID
    @State var viewModel = StepViewModel()

    var body: some View {
        VStack {
            if let content = viewModel.content { /* ... */ }
        }
        .onAppear {
            viewModel.configure(with: id)
        }
    }
}
```

### Lazy stack subview ready before onAppear — [16:14]

```swift
// onAppear

struct StepView: View {
    @State var viewModel: StepViewModel

    init(id: Step.ID) {
        _viewModel = State(initialValue: StepViewModel(id: id))
    }

    var body: some View { /* ... */ }
}
```

### Loading diagram with task modifier — [16:23]

```swift
// Diagram loading

struct StepView: View {
    let step: Step
    @State var diagramLoader = DiagramLoader()

    @State var diagram: Diagram?

    var body: some View {
        VStack { /* ... */ }
            .task {
                diagram = await diagramLoader.loadDiagram(id: step.id)
            }
    }
}
```

### Loading diagram in initializer — [16:40]

```swift
// Diagram loading

struct StepView: View {
    let step: Step
    @State var diagramLoader: DiagramLoader

    init(step: Step) {
        self.step = step
        _diagramLoader = State(initialValue: DiagramLoader(id: step.id))
    }

    var body: some View { /* ... */ }
}

@Observable
class DiagramLoader { /* ... */ }
```

### Highlight @State variable — [17:16]

```swift
// Highlighting

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step
    @State var isHighlighted = false

    var body: some View { /* ... */ }
}
```

### Highlight @Binding — [17:33]

```swift
// Highlighting

struct ContentView: View {
    @State var highlighted: Set<Step.ID> = []

    var body: some View { /* ... */ }
}

struct StepView: View {
    let step: Step
    @Binding var highlighted: Set<Step.ID>

    var body: some View { /* ... */ }
}
```

### Programmatically scroll to showcase — [17:58]

```swift
// Programmatically scroll to showcase

struct ContentView: View {
    @State var scrollPosition = ScrollPosition()

    var body: some View {
        ScrollView { /* ... */ }
            .scrollPosition($scrollPosition)
            .overlay(alignment: .bottom) {
                Button {
                    scrollToShowcase()
                } label: { /* ... */ }
            }
    }

    func scrollToShowcase() {
        withAnimation {
            scrollPosition.scrollTo(id: "showcase-header")
        }
    }
}
```

### Dynamic number of views — [18:24]

```swift
// Dynamic number of views

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    @Environment(\.detailLevel) var detailLevel

    var body: some View {
        if step.isVisible(in: detailLevel) { /* ... */ }
    }
}
```

### Filter at the data level — [18:53]

```swift
// Filter at the data level

struct ContentView: View {
    @Query var steps: [Step]

    init(detailLevel: DetailLevel) {
        _steps = Query(filter: #Predicate<Step> { step in
            step.detailLevel >= detailLevel
        })
    }

    var body: some View { /* ... */ }
}

struct StepView: View { /* ... */ }
```

### Using onGeometryChange in lazy stack subview — [19:16]

```swift
// Don't change layout after views appear

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step
    @State var subtitleHeight: CGFloat?

    var body: some View {
        VStack {
            StepDiagram(diagram: step.diagram)
                .frame(height: diagramHeight(subtitleHeight: subtitleHeight))
            Title(step.title)
            Subtitle(step.subtitle)
                .onGeometryChange(for: CGFloat.self, of: \.size.height) { _, value in
                    subtitleHeight = value
                }
        }
    }
}
```

### Using custom layout in lazy stack subview — [19:17]

```swift
// Don't change layout after views appear

struct ContentView: View { /* ... */ }

struct StepView: View {
    let step: Step

    var body: some View {
        StepLayout {
            StepDiagram(diagram: step.diagram)
            Title(step.title)
            Subtitle(step.subtitle)
        }
    }
}

struct StepLayout: Layout { /* ... */ }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/321/5/78830752-d07d-4d89-aeab-94405c084de9/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._