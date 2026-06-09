---
id: "wwdc2023-10159"
event: "wwdc2023"
year: 2023
title: "Beyond scroll views"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10159"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Beyond scroll views

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10159](https://developer.apple.com/videos/play/wwdc2023/10159)

Find out how you can take your scroll views to the next level with the latest APIs in SwiftUI. We’ll show you how to customize scroll views like never before. Explore the relationship between safe areas and a scroll view’s margins, learn how to interact with the content offset of a scroll view, and discover how you can add a bit of flair to your content with scroll transitions.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,272 words)

## Code Snippets

### ScrollView — [0:46]

```swift
struct Item: Identifiable {
    var id: Int
}

struct ContentView: View {
    @State var items: [Item] = (0 ..< 25).map { Item(id: $0) }

    var body: some View {
        ScrollView(.vertical) {
            LazyVStack {
                ForEach(items) { item in
                    ItemView(item: item)
                }
            }
        }
    }
}

struct ItemView: View {
    var item: Item

    var body: some View {
        Text(item, format: .number)
            .padding(.vertical)
            .frame(maxWidth: .infinity)
    }
}
```

### Basic Featured Section — [2:29]

```swift
struct ContentView: View {
    @State var palettes: [Palette] = [
        .init(id: UUID(), name: "Example One"),
        .init(id: UUID(), name: "Example Two"),
        .init(id: UUID(), name: "Example Three"),
    ]

    var body: some View {
        ScrollView {
            GalleryHeroSection(palettes: palettes)
        }
    }
}

struct Palette: Identifiable {
    var id: UUID
    var name: String
}

struct GalleryHeroSection: View {
    var palettes: [Palette]

    var body: some View {
        GallerySection(edge: .top) {
            GalleryHeroContent(palettes: palettes)
        } label: {
            GalleryHeroHeader(palettes: palettes)
        }
    }
}

struct GallerySection<Content: View, Label: View>: View {
    var edge: Edge? = nil
    @ViewBuilder var content: Content
    @ViewBuilder var label: Label

    var body: some View {
        VStack(alignment: .leading) {
            label
                .font(.title2.bold())
            content
        }
        .padding(.top, halfSpacing)
        .padding(.bottom, sectionSpacing)
        .overlay(alignment: .bottom) {
            if edge != .bottom {
                Divider().padding(.horizontal, hMargin)
            }
        }
    }

    var halfSpacing: CGFloat {
        sectionSpacing / 2.0
    }

    var sectionSpacing: CGFloat {
        20.0
    }

    var hMargin: CGFloat {
        #if os(macOS)
        40.0
        #else
        20.0
        #endif
    }
}

struct GalleryHeroContent: View {
    var palettes: [Palette]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: hSpacing) {
                ForEach(palettes) { palette in
                    GalleryHeroView(palette: palette)
                }
            }
        }
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroView: View {
    var palette: Palette

    @Environment(\.horizontalSizeClass) private var sizeClass

    var body: some View {
        colorStack
            .aspectRatio(heroRatio, contentMode: .fit)
            .containerRelativeFrame(
                [.horizontal], count: columns, spacing: hSpacing
            )
            .clipShape(.rect(cornerRadius: 20.0))
    }

    private var columns: Int {
        sizeClass == .compact ? 1 : regularCount
    }

    @ViewBuilder
    private var colorStack: some View {
        let offsetValue = stackPadding
        ZStack {
            Color.red
                .offset(x: offsetValue, y: offsetValue)
            Color.blue
            Color.green
                .offset(x: -offsetValue, y: -offsetValue)
        }
        .padding(stackPadding)
        .background()
    }

    var stackPadding: CGFloat {
        20.0
    }

    var heroRatio: CGFloat {
        16.0 / 9.0
    }

    var regularCount: Int {
        2
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroHeader: View {
    var palettes: [Palette]

    var body: some View {
        Text("Featured")
            .padding(.horizontal, hMargin)
    }

    var hMargin: CGFloat {
        20.0
    }
}
```

### Featured Section with Margins — [4:00]

```swift
struct ContentView: View {
    @State var palettes: [Palette] = [
        .init(id: UUID(), name: "Example One"),
        .init(id: UUID(), name: "Example Two"),
        .init(id: UUID(), name: "Example Three"),
    ]

    var body: some View {
        ScrollView {
            GalleryHeroSection(palettes: palettes)
        }
    }
}

struct Palette: Identifiable {
    var id: UUID
    var name: String
}

struct GalleryHeroSection: View {
    var palettes: [Palette]

    var body: some View {
        GallerySection(edge: .top) {
            GalleryHeroContent(palettes: palettes)
        } label: {
            GalleryHeroHeader(palettes: palettes)
        }
    }
}

struct GallerySection<Content: View, Label: View>: View {
    var edge: Edge? = nil
    @ViewBuilder var content: Content
    @ViewBuilder var label: Label

    var body: some View {
        VStack(alignment: .leading) {
            label
                .font(.title2.bold())
            content
        }
        .padding(.top, halfSpacing)
        .padding(.bottom, sectionSpacing)
        .overlay(alignment: .bottom) {
            if edge != .bottom {
                Divider().padding(.horizontal, hMargin)
            }
        }
    }

    var halfSpacing: CGFloat {
        sectionSpacing / 2.0
    }

    var sectionSpacing: CGFloat {
        20.0
    }

    var hMargin: CGFloat {
        #if os(macOS)
        40.0
        #else
        20.0
        #endif
    }
}

struct GalleryHeroContent: View {
    var palettes: [Palette]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: hSpacing) {
                ForEach(palettes) { palette in
                    GalleryHeroView(palette: palette)
                }
            }
        }
        .contentMargins(.horizontal, hMargin)
    }

    var hMargin: CGFloat {
        20.0
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroView: View {
    var palette: Palette

    @Environment(\.horizontalSizeClass) private var sizeClass

    var body: some View {
        colorStack
            .aspectRatio(heroRatio, contentMode: .fit)
            .containerRelativeFrame(
                [.horizontal], count: columns, spacing: hSpacing
            )
            .clipShape(.rect(cornerRadius: 20.0))
    }

    private var columns: Int {
        sizeClass == .compact ? 1 : regularCount
    }

    @ViewBuilder
    private var colorStack: some View {
        let offsetValue = stackPadding
        ZStack {
            Color.red
                .offset(x: offsetValue, y: offsetValue)
            Color.blue
            Color.green
                .offset(x: -offsetValue, y: -offsetValue)
        }
        .padding(stackPadding)
        .background()
    }

    var stackPadding: CGFloat {
        20.0
    }

    var heroRatio: CGFloat {
        16.0 / 9.0
    }

    var regularCount: Int {
        2
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroHeader: View {
    var palettes: [Palette]

    var body: some View {
        Text("Featured")
            .padding(.horizontal, hMargin)
    }

    var hMargin: CGFloat {
        20.0
    }
}
```

### Featured Section + Container Relative Frame — [7:42]

```swift
struct ContentView: View {
    @State var palettes: [Palette] = [
        .init(id: UUID(), name: "Example One"),
        .init(id: UUID(), name: "Example Two"),
        .init(id: UUID(), name: "Example Three"),
    ]

    var body: some View {
        ScrollView {
            GalleryHeroSection(palettes: palettes)
        }
    }
}

struct Palette: Identifiable {
    var id: UUID
    var name: String
}

struct GalleryHeroSection: View {
    var palettes: [Palette]

    var body: some View {
        GallerySection(edge: .top) {
            GalleryHeroContent(palettes: palettes)
        } label: {
            GalleryHeroHeader(palettes: palettes)
        }
    }
}

struct GallerySection<Content: View, Label: View>: View {
    var edge: Edge? = nil
    @ViewBuilder var content: Content
    @ViewBuilder var label: Label

    var body: some View {
        VStack(alignment: .leading) {
            label
                .font(.title2.bold())
            content
        }
        .padding(.top, halfSpacing)
        .padding(.bottom, sectionSpacing)
        .overlay(alignment: .bottom) {
            if edge != .bottom {
                Divider().padding(.horizontal, hMargin)
            }
        }
    }

    var halfSpacing: CGFloat {
        sectionSpacing / 2.0
    }

    var sectionSpacing: CGFloat {
        20.0
    }

    var hMargin: CGFloat {
        #if os(macOS)
        40.0
        #else
        20.0
        #endif
    }
}

struct GalleryHeroContent: View {
    var palettes: [Palette]

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: hSpacing) {
                ForEach(palettes) { palette in
                    GalleryHeroView(palette: palette)
                }
            }
            .scrollTargetLayout()
        }
        .contentMargins(.horizontal, hMargin)
        .scrollTargetBehavior(.viewAligned)
    }

    var hMargin: CGFloat {
        20.0
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroView: View {
    var palette: Palette

    @Environment(\.horizontalSizeClass) private var sizeClass

    var body: some View {
        colorStack
            .aspectRatio(heroRatio, contentMode: .fit)
            .containerRelativeFrame(
                [.horizontal], count: columns, spacing: hSpacing
            )
            .clipShape(.rect(cornerRadius: 20.0))
    }

    private var columns: Int {
        sizeClass == .compact ? 1 : regularCount
    }

    @ViewBuilder
    private var colorStack: some View {
        let offsetValue = stackPadding
        ZStack {
            Color.red
                .offset(x: offsetValue, y: offsetValue)
            Color.blue
            Color.green
                .offset(x: -offsetValue, y: -offsetValue)
        }
        .padding(stackPadding)
        .background()
    }

    var stackPadding: CGFloat {
        20.0
    }

    var heroRatio: CGFloat {
        16.0 / 9.0
    }

    var regularCount: Int {
        2
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroHeader: View {
    var palettes: [Palette]

    var body: some View {
        Text("Featured")
            .padding(.horizontal, hMargin)
    }

    var hMargin: CGFloat {
        20.0
    }
}
```

### Featured Section + Scroll Position — [9:46]

```swift
struct ContentView: View {
    @State var palettes: [Palette] = [
        .init(id: UUID(), name: "Example One"),
        .init(id: UUID(), name: "Example Two"),
        .init(id: UUID(), name: "Example Three"),
    ]

    var body: some View {
        ScrollView {
            GalleryHeroSection(palettes: palettes)
        }
    }
}

struct Palette: Identifiable {
    var id: UUID
    var name: String
}

struct GalleryHeroSection: View {
    var palettes: [Palette]
    @State var mainID: Palette.ID? = nil

    var body: some View {
        GallerySection(edge: .top) {
            GalleryHeroContent(palettes: palettes, mainID: $mainID)
        } label: {
            GalleryHeroHeader(palettes: palettes, mainID: $mainID)
        }
    }
}

struct GallerySection<Content: View, Label: View>: View {
    var edge: Edge? = nil
    @ViewBuilder var content: Content
    @ViewBuilder var label: Label

    var body: some View {
        VStack(alignment: .leading) {
            label
                .font(.title2.bold())
            content
        }
        .padding(.top, halfSpacing)
        .padding(.bottom, sectionSpacing)
        .overlay(alignment: .bottom) {
            if edge != .bottom {
                Divider().padding(.horizontal, hMargin)
            }
        }
    }

    var halfSpacing: CGFloat {
        sectionSpacing / 2.0
    }

    var sectionSpacing: CGFloat {
        20.0
    }

    var hMargin: CGFloat {
        #if os(macOS)
        40.0
        #else
        20.0
        #endif
    }
}

struct GalleryHeroContent: View {
    var palettes: [Palette]
    @Binding var mainID: Palette.ID?

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: hSpacing) {
                ForEach(palettes) { palette in
                    GalleryHeroView(palette: palette)
                }
            }
            .scrollTargetLayout()
        }
        .contentMargins(.horizontal, hMargin)
        .scrollTargetBehavior(.viewAligned)
        .scrollPosition(id: $mainID)
        .scrollIndicators(.never)
    }

    var hMargin: CGFloat {
        20.0
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroView: View {
    var palette: Palette

    @Environment(\.horizontalSizeClass) private var sizeClass

    var body: some View {
        colorStack
            .aspectRatio(heroRatio, contentMode: .fit)
            .containerRelativeFrame(
                [.horizontal], count: columns, spacing: hSpacing
            )
            .clipShape(.rect(cornerRadius: 20.0))
    }

    private var columns: Int {
        sizeClass == .compact ? 1 : regularCount
    }

    @ViewBuilder
    private var colorStack: some View {
        let offsetValue = stackPadding
        ZStack {
            Color.red
                .offset(x: offsetValue, y: offsetValue)
            Color.blue
            Color.green
                .offset(x: -offsetValue, y: -offsetValue)
        }
        .padding(stackPadding)
        .background()
    }

    var stackPadding: CGFloat {
        20.0
    }

    var heroRatio: CGFloat {
        16.0 / 9.0
    }

    var regularCount: Int {
        2
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroHeader: View {
    var palettes: [Palette]
    @Binding var mainID: Palette.ID?

    var body: some View {
        VStack(alignment: .leading, spacing: 2.0) {
            Text("Featured")
            Spacer().frame(maxWidth: .infinity)
        }
        .padding(.horizontal, hMargin)
        #if os(macOS)
        .overlay {
            HStack(spacing: 0.0) {
                GalleryPaddle(edge: .leading) {
                    scrollToPreviousID()
                }
                Spacer().frame(maxWidth: .infinity)
                GalleryPaddle(edge: .trailing) {
                    scrollToNextID()
                }
            }
        }
        #endif
    }

    private func scrollToNextID() {
        guard let id = mainID, id != palettes.last?.id,
              let index = palettes.firstIndex(where: { $0.id == id })
        else { return }

        withAnimation {
            mainID = palettes[index + 1].id
        }
    }

    private func scrollToPreviousID() {
        guard let id = mainID, id != palettes.first?.id,
              let index = palettes.firstIndex(where: { $0.id == id })
        else { return }

        withAnimation {
            mainID = palettes[index - 1].id
        }
    }

    var hMargin: CGFloat {
        20.0
    }
}

struct GalleryPaddle: View {
    var edge: HorizontalEdge
    var action: () -> Void

    var body: some View {
        Button {
            action()
        } label: {
            Label(labelText, systemImage: labelIcon)
        }
        .buttonStyle(.paddle)
        .font(nil)
    }

    var labelText: String {
        switch edge {
        case .leading:
            return "Backwards"
        case .trailing:
            return "Forwards"
        }
    }

    var labelIcon: String {
        switch edge {
        case .leading:
            return "chevron.backward"
        case .trailing:
            return "chevron.forward"
        }
    }
}

private struct PaddleButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .imageScale(.large)
            .labelStyle(.iconOnly)
    }
}

extension ButtonStyle where Self == PaddleButtonStyle {
    static var paddle: Self { .init() }
}
```

### Featured Section + Scroll Transition — [12:34]

```swift
struct ContentView: View {
    @State var palettes: [Palette] = [
        .init(id: UUID(), name: "Example One"),
        .init(id: UUID(), name: "Example Two"),
        .init(id: UUID(), name: "Example Three"),
    ]

    var body: some View {
        ScrollView {
            GalleryHeroSection(palettes: palettes)
        }
    }
}

struct Palette: Identifiable {
    var id: UUID
    var name: String
}

struct GalleryHeroSection: View {
    var palettes: [Palette]
    @State var mainID: Palette.ID? = nil

    var body: some View {
        GallerySection(edge: .top) {
            GalleryHeroContent(palettes: palettes, mainID: $mainID)
        } label: {
            GalleryHeroHeader(palettes: palettes, mainID: $mainID)
        }
    }
}

struct GallerySection<Content: View, Label: View>: View {
    var edge: Edge? = nil
    @ViewBuilder var content: Content
    @ViewBuilder var label: Label

    var body: some View {
        VStack(alignment: .leading) {
            label
                .font(.title2.bold())
            content
        }
        .padding(.top, halfSpacing)
        .padding(.bottom, sectionSpacing)
        .overlay(alignment: .bottom) {
            if edge != .bottom {
                Divider().padding(.horizontal, hMargin)
            }
        }
    }

    var halfSpacing: CGFloat {
        sectionSpacing / 2.0
    }

    var sectionSpacing: CGFloat {
        20.0
    }

    var hMargin: CGFloat {
        #if os(macOS)
        40.0
        #else
        20.0
        #endif
    }
}

struct GalleryHeroContent: View {
    var palettes: [Palette]
    @Binding var mainID: Palette.ID?

    var body: some View {
        ScrollView(.horizontal) {
            LazyHStack(spacing: hSpacing) {
                ForEach(palettes) { palette in
                    GalleryHeroView(palette: palette)
                }
            }
            .scrollTargetLayout()
        }
        .contentMargins(.horizontal, hMargin)
        .scrollTargetBehavior(.viewAligned)
        .scrollPosition(id: $mainID)
        .scrollIndicators(.never)
    }

    var hMargin: CGFloat {
        20.0
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroView: View {
    var palette: Palette

    @Environment(\.horizontalSizeClass) private var sizeClass

    var body: some View {
        colorStack
            .aspectRatio(heroRatio, contentMode: .fit)
            .containerRelativeFrame(
                [.horizontal], count: columns, spacing: hSpacing
            )
            .clipShape(.rect(cornerRadius: 20.0))
            .scrollTransition(axis: .horizontal) { content, phase in
                content
                    .scaleEffect(
                        x: phase.isIdentity ? 1.0 : 0.80,
                        y: phase.isIdentity ? 1.0 : 0.80)
            }
    }

    private var columns: Int {
        sizeClass == .compact ? 1 : regularCount
    }

    @ViewBuilder
    private var colorStack: some View {
        let offsetValue = stackPadding
        ZStack {
            Color.red
                .offset(x: offsetValue, y: offsetValue)
            Color.blue
            Color.green
                .offset(x: -offsetValue, y: -offsetValue)
        }
        .padding(stackPadding)
        .background()
    }

    var stackPadding: CGFloat {
        20.0
    }

    var heroRatio: CGFloat {
        16.0 / 9.0
    }

    var regularCount: Int {
        2
    }

    var hSpacing: CGFloat {
        10.0
    }
}

struct GalleryHeroHeader: View {
    var palettes: [Palette]
    @Binding var mainID: Palette.ID?

    var body: some View {
        VStack(alignment: .leading, spacing: 2.0) {
            Text("Featured")
            Spacer().frame(maxWidth: .infinity)
        }
        .padding(.horizontal, hMargin)
        #if os(macOS)
        .overlay {
            HStack(spacing: 0.0) {
                GalleryPaddle(edge: .leading) {
                    scrollToPreviousID()
                }
                Spacer().frame(maxWidth: .infinity)
                GalleryPaddle(edge: .trailing) {
                    scrollToNextID()
                }
            }
        }
        #endif
    }

    private func scrollToNextID() {
        guard let id = mainID, id != palettes.last?.id,
              let index = palettes.firstIndex(where: { $0.id == id })
        else { return }

        withAnimation {
            mainID = palettes[index + 1].id
        }
    }

    private func scrollToPreviousID() {
        guard let id = mainID, id != palettes.first?.id,
              let index = palettes.firstIndex(where: { $0.id == id })
        else { return }

        withAnimation {
            mainID = palettes[index - 1].id
        }
    }

    var hMargin: CGFloat {
        20.0
    }
}

struct GalleryPaddle: View {
    var edge: HorizontalEdge
    var action: () -> Void

    var body: some View {
        Button {
            action()
        } label: {
            Label(labelText, systemImage: labelIcon)
        }
        .buttonStyle(.paddle)
        .font(nil)
    }

    var labelText: String {
        switch edge {
        case .leading:
            return "Backwards"
        case .trailing:
            return "Forwards"
        }
    }

    var labelIcon: String {
        switch edge {
        case .leading:
            return "chevron.backward"
        case .trailing:
            return "chevron.forward"
        }
    }
}

private struct PaddleButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .imageScale(.large)
            .labelStyle(.iconOnly)
    }
}

extension ButtonStyle where Self == PaddleButtonStyle {
    static var paddle: Self { .init() }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10159/4/DCE1F4A7-9E0E-4F48-B70A-6C44D758769E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10159) — developer.apple.com. Indexed for agent consumption._
