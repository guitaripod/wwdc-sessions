---
id: "wwdc2020-10061"
event: "wwdc2020"
year: 2020
title: "Expand your SiriKit Media Intents to more platforms"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10061"
topics: ["App Services", "Audio & Video"]
platforms: ["iOS", "iPadOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Expand your SiriKit Media Intents to more platforms

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10061](https://developer.apple.com/videos/play/wwdc2020/10061)

Discover how you can enable Siri summoning for your music or audio app using SiriKit Media Intents. We’ll walk you through how to add Siri support to your music, podcast, or other audio service on more of our platforms, including HomePod and Apple TV, so people can start listening by just asking Siri. And learn about new APIs that let you support alternative results, helping people listen more quickly without leaving the Siri interface.

**Keywords:** `audio`, `audiobooks`, `conversational interaction`, `design`, `intents`, `intentsui`, `media`, `music`, `podcasts`, `siri`, `sirikit`, `sirikit media intents`, `siri remote`, `voice`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,715 words)

## Documentation & Resources

- [If you’d like to integrate your music service with HomePod, let us know](https://developer.apple.com/contact/request/sirikit-media-intent-for-homepod) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/contact/request/sirikit-media-intent-for-homepod
- [Providing Hands-Free App Control with Intents](https://developer.apple.com/documentation/SiriKit/providing-hands-free-app-control-with-intents) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/providing-hands-free-app-control-with-intents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/providing-hands-free-app-control-with-intents.json
- [Managing Audio with SiriKit](https://developer.apple.com/documentation/SiriKit/managing-audio-with-sirikit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/managing-audio-with-sirikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/managing-audio-with-sirikit.json

## Code Snippets

### resolveMediaItems method — [2:45]

```swift
func resolveMediaItems(for intent: INPlayMediaIntent, with completion: @escaping ([INPlayMediaMediaItemResolutionResult]) -> Void) {
}
```

### handle with .continueInApp — [3:03]

```swift
func handle(intent: INPlayMediaIntent, completion: (INPlayMediaIntentResponse) -> Void) {
  completion(INPlayMediaIntentResponse(code: .continueInApp, userActivity: nil))
}
```

### Singular successWithResolvedMediaItem call — [5:24]

```swift
INPlayMediaMediaItemResolutionResult.success(with: mediaItems[0])
```

### Plural successesWithResolvedMediaItems call — [5:40]

```swift
INPlayMediaMediaItemResolutionResult.successes(with: mediaItems)
```

### handle with .handleInApp — [6:07]

```swift
func handle(intent: INPlayMediaIntent, completion: (INPlayMediaIntentResponse) -> Void) {
  completion(INPlayMediaIntentResponse(code: .handleInApp, userActivity: nil))
}
```

### ControlAudio resolveMediaItems — [6:37]

```swift
func resolveMediaItems(for intent: INPlayMediaIntent, with completion: @escaping ([INPlayMediaMediaItemResolutionResult]) -> Void) {
    let mediaSearch = intent.mediaSearch
    resolveMediaItems(for: mediaSearch) { optionalMediaItems in
        guard let mediaItems = optionalMediaItems else {
            return
        }
        completion(INPlayMediaMediaItemResolutionResult.successes(with: mediaItems))
    }
}
```

### App prewarming background appLaunch — [10:24]

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Locate any app prewarming logic in this method -- fetch credentials, get audio player ready, etc.
    return true
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10061/7/0C05700A-690E-443C-9984-6792A466E6CA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10061) — developer.apple.com. Indexed for agent consumption._
