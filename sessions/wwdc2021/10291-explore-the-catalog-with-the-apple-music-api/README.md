---
id: "wwdc2021-10291"
event: "wwdc2021"
year: 2021
title: "Explore the catalog with the Apple Music API"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10291"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Explore the catalog with the Apple Music API

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10291](https://developer.apple.com/videos/play/wwdc2021/10291)

Discover how you can use the Apple Music API to fetch music catalog metadata for your app. Explore the latest updates to the API as well as some advanced techniques for shaping your requests and highlighting the right metadata for a project. To get the most out of this session, we recommend some familiarity with the Apple Music API.

**Keywords:** `apple music`, `music`, `musickit`, `musickitjs`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,177 words)

## Documentation & Resources

- [MusicKit](https://developer.apple.com/musickit/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/musickit/

## Code Snippets

### Search Suggestions Terms Request — [1:25]

```json
/v1/catalog/us/search/suggestions?term=taylor&kinds=terms
```

### Search Suggestions Top Results Request — [2:09]

```json
/v1/catalog/us/search/suggestions?term=taylor&kinds=topResults&types=artists,songs
```

### Search Suggestions Relate Albums Request — [3:47]

```json
/v1/catalog/us/search/suggestions?term=taylor&kinds=topResults&types=artists,albums,songs&relate[songs]=albums
```

### Search Suggestions Extend artistUrl Request — [5:03]

```json
/v1/catalog/us/search/suggestions?term=taylor&kinds=topResults&types=artists,albums,songs&relate[songs]=albums&extend[songs]=artistUrl
```

### Artist Top Songs View Request — [6:16]

```json
/v1/catalog/us/artists/159260351?views=top-songs
```

### Top Charts Request — [6:59]

```json
/v1/catalog/us/charts?types=playlists&with=dailyGlobalTopCharts,cityCharts
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10291/3/F3E513AE-7D59-4677-BA86-19148C5DE3E4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10291/3/F3E513AE-7D59-4677-BA86-19148C5DE3E4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10291) — developer.apple.com. Indexed for agent consumption._
