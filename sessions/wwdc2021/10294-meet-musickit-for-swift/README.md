---
id: "wwdc2021-10294"
event: "wwdc2021"
year: 2021
title: "Meet MusicKit for Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10294"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet MusicKit for Swift

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10294](https://developer.apple.com/videos/play/wwdc2021/10294)

MusicKit makes it easy to integrate Apple Music into your app. Explore the Swift-based framework: We’ll take you through the basic process of using MusicKit — including how to find, request, and play content — and show you how you can incorporate music subscription workflows into your app if someone hasn’t yet signed up to Apple Music.

**Keywords:** `apple music`, `music`, `musickit`, `songs`, `swift`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,846 words)

## Documentation & Resources

- [Using MusicKit to integrate with Apple Music](https://developer.apple.com/documentation/MusicKit/using-musickit-to-integrate-with-apple-music) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MusicKit/using-musickit-to-integrate-with-apple-music
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MusicKit/using-musickit-to-integrate-with-apple-music.json
- [MusicKit](https://developer.apple.com/documentation/musickit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/musickit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/musickit.json

## Code Snippets

### Loading and accessing relationships — [2:56]

```swift
// Loading and accessing relationships

let detailedAlbum = try await album.with([.artists, .tracks, .relatedAlbums])
print("\(detailedAlbum)")

if let tracks = detailedAlbum.tracks {
    print("  Tracks:")
    tracks.prefix(2).forEach { track in
        print("    \(track)")
    }
}
```

### Loading and accessing associations — [3:31]

```swift
// Loading and accessing associations

let detailedAlbum = try await album.with([.artists, .tracks, .relatedAlbums])
print("\(detailedAlbum)")

if let relatedAlbums = detailedAlbum.relatedAlbums {
    print("  \(relatedAlbums.title ?? ""):")
    relatedAlbums.prefix(2).forEach { relatedAlbum in
        print("    \(relatedAlbum)")
    }
}
```

### Loading top level genres — [9:02]

```swift
// Loading top level genres

struct MyGenresResponse: Decodable {
    let data: [Genre]
}

let countryCode = try await MusicDataRequest.currentCountryCode
let url = URL(string: "https://api.music.apple.com/v1/catalog/\(countryCode)/genres")!

let dataRequest = MusicDataRequest(urlRequest: URLRequest(url: url))
let dataResponse = try await dataRequest.response()

let decoder = JSONDecoder()
let genresResponse = try decoder.decode(MyGenresResponse.self, from: dataResponse.data)
print("\(genresResponse.data[9])")
```

### Requesting user consent for MusicKit — [10:49]

```swift
// Requesting user consent for MusicKit

@State var isAuthorizedForMusicKit = false

func requestMusicAuthorization() {
    detach {
        let authorizationStatus = await MusicAuthorization.request()
        if authorizationStatus == .authorized {
            isAuthorizedForMusicKit = true
        } else {
            // User denied permission.
        }
    }
}
```

### Using music subscription to drive state of a play button — [12:54]

```swift
// Using music subscription to drive state of a play button

@State var musicSubscription: MusicSubscription?

var body: some View {
    Button(action: handlePlayButtonSelected) {
        Image(systemName: "play.fill")
    }
    .disabled(!(musicSubscription?.canPlayCatalogContent ?? false))
    .task {
        for await subscription in MusicSubscription.subscriptionUpdates {
            musicSubscription = subscription
        }
    }
}
```

### Showing contextual music subscription offer — [15:34]

```swift
// Showing contextual music subscription offer

@State var musicSubscription: MusicSubscription?
@State var isShowingOffer = false

var offerOptions: MusicSubscriptionOffer.Options {
    var offerOptions = MusicSubscriptionOffer.Options()
    offerOptions.itemID = album.id
    return offerOptions
}

var body: some View {
    Button("Show Subscription Offers", action: showSubscriptionOffer)
        .disabled(!(musicSubscription?.canBecomeSubscriber ?? false))
        .musicSubscriptionOffer(isPresented: $isShowingOffer, options: offerOptions)
}

func showSubscriptionOffer() {
    isShowingOffer = true
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10294/5/DFB67B36-DCDE-49D9-8ED1-AC2A8B566F64/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10294/5/DFB67B36-DCDE-49D9-8ED1-AC2A8B566F64/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10294) — developer.apple.com. Indexed for agent consumption._
