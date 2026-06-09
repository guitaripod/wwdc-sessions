---
id: "wwdc2024-10207"
event: "wwdc2024"
year: 2024
title: "Migrate your TVML app to SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10207"
topics: ["Audio & Video", "SwiftUI & UI Frameworks"]
platforms: ["tvOS"]
hasTranscript: true
---

# Migrate your TVML app to SwiftUI

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** tvOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10207](https://developer.apple.com/videos/play/wwdc2024/10207)

SwiftUI helps you build great apps on all Apple platforms and is the preferred toolkit for bringing your content into the living room with tvOS 18. Learn how to use SwiftUI to create familiar layouts and controls from TVMLKit, and get tips and best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,839 words)

## Documentation & Resources

- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Creating a tvOS media catalog app in SwiftUI](https://developer.apple.com/documentation/SwiftUI/Creating-a-tvOS-media-catalog-app-in-SwiftUI) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Creating-a-tvOS-media-catalog-app-in-SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Creating-a-tvOS-media-catalog-app-in-SwiftUI.json

## Code Snippets

### Borderless button lockup — [4:18]

```swift
Button {} label: {
    Image("discovery_landscape")
        .resizable()
        .frame(width: 250, height: 375)
    Text("Borderless Portrait")
}
.buttonStyle(.borderless)
```

### Standard content shelf — [5:38]

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 40) {
        ForEach(Asset.allCases) { asset in
            Button {} label: {
                asset.portraitImage
                    .resizable()
                    .aspectRatio(250/375, contentMode: .fit)
                    .containerRelativeFrame(.horizontal, count: 6, spacing: 40)
                Text(asset.title)
            }
        }
    }
}
.scrollClipDisabled()
.buttonStyle(.borderless)
```

### Card button — [8:19]

```swift
ScrollView(.horizontal) {
    LazyHStack(spacing: 48) {
        ForEach(Asset.allCases) { asset in
            Button {} label: {
                HStack(alignment: .top, spacing: 10) {
                    asset.landscapeImage
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .clipShape(RoundedRectangle(cornerRadius: 12))

                    VStack(alignment: .leading) {
                        Text(asset.title)
                            .font(.body)
                        Text("Subtitle text goes here, limited to two lines")
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                            .lineLimit(2)
                        Spacer(minLength: 0)
                        HStack(spacing: 4) {
                            ForEach(1..<4) { _ in
                                Image(systemName: "ellipsis.rectangle.fill")
                            }
                        }
                        .foregroundStyle(.secondary)
                    }
                }
                .padding([.leading, .top, .bottom], 12)
                .padding(.trailing, 20)
                .frame(maxWidth: .infinity)
            }
            .containerRelativeFrame(.horizontal, count: 3, spacing: 48)
        }
    }
}
.scrollClipDisabled()
.buttonStyle(.card)
```

### Landing page — [8:39]

```swift
ScrollView(.vertical) {
    LazyVStack(alignment: .leading, spacing: 26) {
        VStack(alignment: .leading) {
            Text("tvOS with SwiftUI")
                .font(.largeTitle).bold()

            Spacer(minLength: 300)

            HStack {
                Button("Show") {}
                Button(“More Info…”) {}
                Spacer()
            }
            .padding(.bottom, 100)

            Spacer()
        }
        .onScrollVisibilityChange { visible in
            withAnimation {
                belowFold = !visible
            }
        }

        Section("Movie Shelf") {
            MovieShelf()
        }

        Section("TV and Music Shelf") {
            TVMusicShelf()
        }

        Section("Content Cards") {
            CardShelf()
        }
    }
    .scrollTargetLayout()
}
.scrollClipDisabled()
.background(alignment: .top) {
    if !belowFold {
        Image("beach_landscape")
            .resizable()
            .aspectRatio(contentMode: .fill)
            .ignoresSafeArea()
            .mask {
                LinearGradient(stops: [
                    .init(color: .black, location: 0.0),
                    .init(color: .black, location: 0.45),
                    .init(color: .black.opacity(0), location: 0.8)
                ], startPoint: .top, endPoint: .bottom)
            }
    }
}
.scrollTargetBehavior(.viewAligned)
```

### Tab view — [11:13]

```swift
TabView {
    Tab("Stack", systemImage: "line.3.horizontal") {
        StackView()
    }

    // Other Tabs...

    Tab("Search", systemImage: "magnifyingglass") {
        SearchView()
    }
}
```

### Search page — [11:50]

```swift
@State var searchTerm: String = ""

let columns: [GridItem] = Array(repeating: .init(.flexible(), spacing: 40), count: 4)

ScrollView(.vertical) {
    LazyVGrid(columns: columns) {
        ForEach(sortedMatchingAssets) { asset in
            Button {} label: {
                asset.landscapeImage
                    .resizable()
                    .aspectRatio(16 / 9, contentMode: .fit)
                Text(asset.title)
            }
        }
    }
}
.scrollClipDisabled()
.buttonStyle(.borderless)
.searchable(text: $searchTerm)
.searchSuggestions {
    ForEach(suggestedSearchTerms, id: \.self) { suggestion in
        Text(suggestion)
    }
}
```

### Sidebar adaptable tab view style — [14:59]

```swift
TabView {
    Tab("Stack", systemImage: "line.3.horizontal") {
        StackView()
    }

    // Other Tabs...

    Tab("Search", systemImage: "magnifyingglass") {
        SearchView()
    }
}
.tabViewStyle(.sidebarAdaptable)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10207/4/F0BA61BC-1F1D-4128-A2A3-C92C121EEE6F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10207/4/F0BA61BC-1F1D-4128-A2A3-C92C121EEE6F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10207) — developer.apple.com. Indexed for agent consumption._
