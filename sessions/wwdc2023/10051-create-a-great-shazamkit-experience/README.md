---
id: "wwdc2023-10051"
event: "wwdc2023"
year: 2023
title: "Create a great ShazamKit experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10051"
topics: ["Audio & Video", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Create a great ShazamKit experience

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10051](https://developer.apple.com/videos/play/wwdc2023/10051)

Discover how your app can offer a great audio matching experience with the latest updates to ShazamKit. We’ll take you through matching features, updates to audio recognition, and interactions with the Shazam library. Learn tips and best practices for using ShazamKit in your audio apps. For more on ShazamKit, check out "Create custom catalogs at scale with ShazamKit" from WWDC22 as well as "Explore ShazamKit" and "Create custom audio experiences with ShazamKit" from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,984 words)

## Documentation & Resources

- [ShazamKit](https://developer.apple.com/documentation/ShazamKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ShazamKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ShazamKit.json

## Code Snippets

### Single match with SHManagedSession — [6:46]

```swift
let managedSession = SHManagedSession()

let result = await managedSession.result()

switch result {
 case .match(let match):
        print("Match found. MediaItemsCount: \(match.mediaItems.count)")
 case .noMatch(_):
        print("No match found")
 case .error(_, _):
        print("An error occurred")
}
```

### Multiple matches with SHManagedSession — [7:16]

```swift
let managedSession = SHManagedSession()

// Continuously match 
for await result in managedSession.results {

 switch result {
  case .match(let match):
        print("Match found. MediaItemsCount: \(match.mediaItems.count)")
  case .noMatch(_):
        print("No match found")
  case .error(_, _):
        print("An error occurred")
 }
}
```

### Stop SHManagedSession — [7:37]

```swift
let managedSession = SHManagedSession()

// Cancel the session
managedSession.cancel()
```

### ShazamKit Matcher with SHManagedSession — [8:02]

```swift
import Foundation
import ShazamKit

struct MatchResult: Identifiable, Equatable {
    let id = UUID()
    let match: SHMatch?
}

@MainActor final class Matcher: ObservableObject {

    @Published var isMatching = false
    @Published var currentMatchResult: MatchResult?

    var currentMediaItem: SHMatchedMediaItem? {
        currentMatchResult?.match?.mediaItems.first
    }

    private let session: SHManagedSession

    init() {

        if let catalog = try? ResourcesProvider.catalog() {
            session = SHManagedSession(catalog: catalog)
        } else {
            session = SHManagedSession()
        }
    }

    func match() async {

        isMatching = true

        for await result in session.results {
            switch result {
            case .match(let match):
                Task { @MainActor in
                    self.currentMatchResult = MatchResult(match: match)
                }
            case .noMatch(_):
                print("No match")
                endSession()
            case .error(let error, _):
                print("Error \(error.localizedDescription)")
                endSession()
            }
            stopRecording()
        }
    }

    func stopRecording() {

        session.cancel()
    }

    func endSession() {

        // Reset result of any previous match.
        isMatching = false
        currentMatchResult = MatchResult(match: nil)
    }
}
```

### Preparing SHManagedSession — [10:07]

```swift
let managedSession = SHManagedSession()

await managedSession.prepare()

let result = await managedSession.result()
```

### SHManagedSession Idle State in SwiftUI — [11:39]

```swift
struct MatchView: View {
    let session: SHManagedSession

    var body: some View {
        VStack {
             Text(session.state == .idle ? "Hear Music?" 
                : "Matching")
             if session.state == .matching {
                  ProgressView()
             } else {
                  Button {
                      // start match
                  } label: {
                      Text("Learn the Dance")
                  }
             }
        }       
}
```

### SHManagedSession Matching State in SwiftUI — [12:25]

```swift
struct MatchView: View {
    let session: SHManagedSession

    var body: some View {
        VStack {
             Text(session.state == .idle ? "Hear Music?" 
                : "Matching")
             if session.state == .matching {
                  ProgressView()
             } else {
                  Button {
                      // start match
                  } label: {
                      Text("Learn the Dance")
                  }
             }
        }    
    }
}
```

### Adding with SHLibrary — [15:23]

```swift
func add(mediaItems: [SHMediaItem]) async throws {

    try await SHLibrary.default.addItems(mediaItems)
}
```

### Reading with SHLibrary — [15:34]

```swift
struct LibraryView: View {
    var body: some View {
        List(SHLibrary.default.items) { item in
            MediaItemView(item: item)
        }
    }
}
```

### Reading with SHLibrary in a non-UI context — [16:00]

```swift
// Determine a user’s most popular genre

let currentItems = await SHLibrary.default.items

let genres = currentItems.flatMap { $0.genres }

// count frequency of genres and get the highest
let mostPopularGenre = highestOccurringGenre(from: genres)
```

### SHLibrary Remove — [16:25]

```swift
func remove(mediaItems: [SHMediaItem]) async throws {

    try await SHLibrary.default.removeItems(mediaItems)
}
```

### RecentDancesView with SHLibrary read and delete implementation — [16:42]

```swift
import SwiftUI
import ShazamKit

enum NavigationPath: Hashable {
    case nowPlayingView(videoURL: URL)
    case danceCompletionView
}

struct RecentDancesView: View {
    private enum ViewConstants {
        static let emptyStateImageName: String = "EmptyStateIcon"
        static let emptyStateTextTitle: String = "No Dances Yet?"
        static let emptyStateTextSubtitle: String = "Find some music to start learning"
        static let deleteSwipeViewOpacity: Double = 0.5
        static let matchingStateTextTopPadding: CGFloat = 24
        static let matchingStateTextBottomPadding: CGFloat = 16
        static let progressViewScaleEffect: CGFloat = 1.1
        static let progressViewBottomPadding: CGFloat = 12.0
        static let learnDanceButtonWidth: CGFloat = 250
        static let curvedTopSideRectangleHeight: CGFloat = 200
        static let listRowBottomInset: CGFloat = 30.0
        static let matchingStateText: String = "Get Ready..."
        static let notMatchingStateText: String = "Hear Music?"
        static let noMatchText: String = "No dance video for audio"
        static let navigationTitleText: String = "Recent Dances"
        static let learnDanceButtonText: String = "Learn the Dance"
        static let retryButtonText: String = "Try Again"
        static let cancelButtonText: String = "Cancel"
    }

    // MARK: Properties
    private var isListEmpty: Bool {
        SHLibrary.default.items.isEmpty
    }

    @State private var matchingState: String = ViewConstants.notMatchingStateText
    @State private var matchButtonText: String = ViewConstants.learnDanceButtonText
    @State private var canRetryMatchAttempt = false
    @State private var navigationPath: [NavigationPath] = []

    // MARK: Environment
    @EnvironmentObject private var matcher: Matcher
    @Environment(\.openURL) var openURL
    var body: some View {
        NavigationStack(path: $navigationPath) {
            ZStack(alignment: .bottom) {
                List(SHLibrary.default.items, id: \.self) { mediaItem in
                        RecentDanceRowView(mediaItem: mediaItem)
                            .onTapGesture(perform: {
                                guard let appleMusicURL = mediaItem.appleMusicURL else {
                                    return
                                }
                                openURL(appleMusicURL)
                            })
                            .swipeActions {
                                Button {
                                    Task { try? await SHLibrary.default.removeItems([mediaItem]) }
                                } label: {
                                    Image(systemName: "trash")
                                        .symbolRenderingMode(.hierarchical)
                                }
                                .tint(.appPrimary.opacity(0.5))
                            }
                }
                    .listStyle(.plain)
                    .overlay {
                        if isListEmpty {
                            ContentUnavailableView {
                                Label(ViewConstants.emptyStateTextTitle,
                                      image: ImageResource(name: ViewConstants.emptyStateImageName, bundle: Bundle.main))
                                    .font(.title)
                                    .foregroundStyle(Color.white)
                            } description: {
                                Text(ViewConstants.emptyStateTextSubtitle)
                                    .foregroundStyle(Color.white)
                            }
                        }
                    }
                    .safeAreaInset(edge: .bottom, spacing: ViewConstants.listRowBottomInset) {
                        ZStack(alignment: .top) {
                            CurvedTopSideRectangle()
                            VStack {
                                Text(matchingState)
                                    .font(.body)
                                    .foregroundStyle(.white)
                                    .padding(.top, ViewConstants.matchingStateTextTopPadding)
                                    .padding(.bottom, ViewConstants.matchingStateTextBottomPadding)
                                if matcher.isMatching {
                                    ProgressView()
                                        .progressViewStyle(.circular)
                                        .tint(.appPrimary)
                                        .scaleEffect(x: ViewConstants.progressViewScaleEffect, y: ViewConstants.progressViewScaleEffect)
                                        .padding(.bottom, ViewConstants.progressViewBottomPadding)
                                    Button(ViewConstants.cancelButtonText) {
                                        canRetryMatchAttempt = false
                                        matcher.stopRecording()
                                        matcher.endSession()
                                    }
                                    .foregroundStyle(Color.appPrimary)
                                    .font(.subheadline)
                                    .fontWeight(.semibold)
                                } else {
                                    Button {
                                        Task { await matcher.match() }
                                        matchingState = ViewConstants.matchingStateText
                                        canRetryMatchAttempt = true
                                    } label: {
                                        Text(matchButtonText)
                                            .foregroundStyle(.black)
                                            .font(.title3)
                                            .fontWeight(.heavy)
                                            .frame(maxWidth: .infinity)
                                    }
                                    .frame(width: ViewConstants.learnDanceButtonWidth)
                                    .padding()
                                    .background(Color.appPrimary)
                                    .clipShape(Capsule())
                                }
                            }
                        }
                        .edgesIgnoringSafeArea(.bottom)
                        .frame(height: ViewConstants.curvedTopSideRectangleHeight)
                    }
            }
            .background(Color.appSecondary)
            .navigationTitle(isListEmpty ? "" : ViewConstants.navigationTitleText)
            .preferredColorScheme(.dark)
            .toolbarColorScheme(.dark, for: .navigationBar)
            .navigationBarTitleDisplayMode(.large)
            .toolbarBackground(Color.appSecondary, for: .navigationBar)
            .frame(maxHeight: .infinity)
            .onChange(of: matcher.currentMatchResult, { _, result in

                guard navigationPath.isEmpty else {
                    print("Dance video already displayed")
                    return
                }

                guard let match = result?.match,
                      let url = ResourcesProvider.videoURL(forFilename: match.mediaItems.first?.videoTitle ?? "") else {

                    matchingState = canRetryMatchAttempt ? ViewConstants.noMatchText : ViewConstants.notMatchingStateText
                    matchButtonText = canRetryMatchAttempt ? ViewConstants.retryButtonText : ViewConstants.learnDanceButtonText
                    return
                }

                canRetryMatchAttempt = false

                // Add the video playing view to the navigation stack.
                navigationPath.append(.nowPlayingView(videoURL: url))
            })
            .navigationDestination(for: NavigationPath.self, destination: { newNavigationPath in
                switch newNavigationPath {
                case .nowPlayingView(let videoURL):
                    NowPlayingView(navigationPath: $navigationPath, nowPlayingViewModel: NowPlayingViewModel(player: AVPlayer(url: videoURL)))
                case .danceCompletionView:
                    DanceCompletionView(navigationPath: $navigationPath)
                }
            })
            .onAppear {
                if AVAudioSession.sharedInstance().category != .ambient {
                    Task.detached { try? AVAudioSession.sharedInstance().setCategory(.ambient) }
                }
                matchingState = ViewConstants.notMatchingStateText
                matchButtonText = ViewConstants.learnDanceButtonText
            }
        }
    }
}
```

### Filtering for specific media items — [20:23]

```swift
func match(from televisionShowCatalog: SHCustomCatalog) async -> [SHMatchedMediaItem] {

        let managedSession = SHManagedSession(catalog: televisionShowCatalog)

        let result = await managedSession.result()

        if case .match(let match) = result {

            // filter for only media items related to a particular episode
            let filteredMediaItems = match.mediaItems.filter { $0.title == "Episode 2" }
            return filteredMediaItems
        }

        return []
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10051/4/609FFA81-2E88-4DC5-ACDB-5C4A0C42875D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10051/4/609FFA81-2E88-4DC5-ACDB-5C4A0C42875D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10051) — developer.apple.com. Indexed for agent consumption._
