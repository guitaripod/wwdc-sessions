---
id: "wwdc2022-110347"
event: "wwdc2022"
year: 2022
title: "Explore more content with MusicKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110347"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore more content with MusicKit

**Event:** WWDC22 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110347](https://developer.apple.com/videos/play/wwdc2022/110347)

Discover how you can enhance and personalize your app using MusicKit. We’ll take you through the latest additions to the MusicKit framework and explore how you can bring music content to your app through requests, metadata, and more.

**Keywords:** `apple music`, `music`, `musickit`, `music library`, `playlists`, `songs`, `swift`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,152 words)

## Documentation & Resources

- [Explore more content with MusicKit](https://developer.apple.com/documentation/musickit/explore_more_content_with_musickit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/musickit/explore_more_content_with_musickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/musickit/explore_more_content_with_musickit.json
- [MusicKit](https://developer.apple.com/documentation/musickit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/musickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/musickit.json

## Code Snippets

### Existing catalog search request — [4:20]

```swift
// Loading catalog search top results

var searchRequest = MusicCatalogSearchRequest(
  term: "Hello",
  types: [
    Artist.self,
    Album.self,
    Song.self
  ]
)

let searchResponse = try await searchRequest.response()
print("\(searchResponse)")
```

### Loading catalog search top results — [4:44]

```swift
// Loading catalog search top results

var searchRequest = MusicCatalogSearchRequest(
  term: "Hello",
  types: [
    Artist.self,
    Album.self,
    Song.self
  ]
)

searchRequest.includeTopResults = true
let searchResponse = try await searchRequest.response()
print("\(searchResponse.topResults)")
```

### Loading search suggestions — [5:09]

```swift
// Loading suggestions

let request = MusicCatalogSearchSuggestionsRequest(term: "shaz")
let response = try await request.response()
print("\(response)")
```

### Loading catalog top charts — [6:30]

```swift
// Loading catalog top charts.

let request = MusicCatalogChartsRequest(
  kinds: [.dailyGlobalTop, .mostPlayed, .cityTop],
  types: [Song.self, Playlist.self]
)
let response = try await request.response()
print("\(response.playlistCharts.first)")
```

### Loading audio variants — [8:10]

```swift
// Loading audio variants

let album = …
let detailedAlbum = try await album.with(.audioVariants)
print("\(detailedAlbum.debugDescription)")
```

### Showing currently playing audio variants — [9:09]

```swift
// Showing currently playing audio variants

@ObservedObject var musicPlayerQueue = ApplicationMusicPlayer.shared.queue
@ObservedObject var musicPlayerState = ApplicationMusicPlayer.shared.state

var body: some View {
  if let currentEntry = musicPlayerQueue.currentEntry {
    VStack {
      MyPlayerEntryView(currentEntry)
      if musicPlayerState.audioVariant == .dolbyAtmos {
        Image("dolby-atmos-badge")
      }
    }
  }
}
```

### Loading recently played containers — [10:28]

```swift
// Loading recently played containers

let request = MusicRecentlyPlayedContainerRequest()
let response = try await request.response()
print("\(response)")
```

### Loading recently played songs — [10:41]

```swift
// Loading recently played songs

let request = MusicRecentlyPlayedRequest<Song>()
let response = try await request.response()
print("\(response)")
```

### Loading personal recommendations and printing first recommendation — [11:21]

```swift
// Loading personal recommendations

let request = MusicPersonalRecommendationsRequest()
let response = try await request.response()
print("\(response.recommendations.first)")
```

### Loading personal recommendations and printing second recommendation — [11:51]

```swift
// Loading personal recommendations

let request = MusicPersonalRecommendationsRequest()
let response = try await request.response()
print("\(response.recommendations[1])")
```

### Loading library playlists — [13:36]

```swift
@MainActor
private func loadLibraryPlaylists() async throws {
  let request = MusicLibraryRequest<Playlist>()
  let response = try await request.response()
  self.response = response
}
```

### Displaying library playlists — [14:23]

```swift
List {
  Section(header: Text("Library Playlists").fontWeight(.semibold)) {
    ForEach(response.items) { playlist in
      PlaylistCell(playlist)
    }
  }
}
```

### Fetching all albums in the library — [15:47]

```swift
// Fetching all albums in the library

let request = MusicLibraryRequest<Album>()

let response = try await request.response()
print("\(response)")
```

### Fetching all compilations in the library — [16:38]

```swift
// Fetching all compilations in the library

var request = MusicLibraryRequest<Album>()
request.filter(matching: \.isCompilation, equalTo: true)

let response = try await request.response()
print("\(response)")
```

### Fetching all dance compilations in the library — [17:08]

```swift
// Fetching all dance compilations in the library

var request = MusicLibraryRequest<Album>()
request.filter(matching: \.isCompilation, equalTo: true) 
request.filter(matching: \.genres, contains: danceGenre)

let response = try await request.response()
print("\(response)")
```

### Fetching all downloaded dance compilations in the library — [17:29]

```swift
// Fetching all downloaded dance compilations in the library

var request = MusicLibraryRequest<Album>()
request.filter(matching: \.isCompilation, equalTo: true) 
request.filter(matching: \.genres, contains: danceGenre)
request.includeDownloadedContentOnly = true

let response = try await request.response()
print("\(response)")
```

### Fetching all albums sectioned by genre — [18:29]

```swift
// Fetching all albums sectioned by genre

var request = MusicLibrarySectionedRequest<Genre, Album>()

let response = try await request.response()
print("\(response)")
```

### Fetching all albums sectioned by genre sorted by artist name — [19:04]

```swift
// Fetching all albums sectioned by genre sorted by artist name

var request = MusicLibrarySectionedRequest<Genre, Album>()
request.sortItems(by: \.artistName, ascending: true)

let response = try await request.response()
print("\(response)")
```

### Fetching relationships using the with method without a preferred source — [20:58]

```swift
// Fetching relationships using the with method

let album = …
let detailedAlbum = try await album.with(.tracks)
print("\(album.tracks)")
```

### Fetching relationships using the with method and a preferred source — [21:11]

```swift
// Fetching relationships using the with method

let album = …
let detailedAlbum = try await album.with(.tracks, preferredSource: .library)
print("\(album.tracks)")
```

### Adding a track to a playlist — [22:09]

```swift
Task { 
  try await MusicLibrary.shared(add: selectedTrack, to: playlist)
  isShowingPlaylistPicker = false
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110347/3/9A5697EE-37FC-497A-AD9F-5033E026866E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110347/3/9A5697EE-37FC-497A-AD9F-5033E026866E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110347) — developer.apple.com. Indexed for agent consumption._
