---
id: "wwdc2021-10013"
event: "wwdc2021"
year: 2021
title: "Build light and fast App Clips"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10013"
topics: ["Essentials", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build light and fast App Clips

**Event:** WWDC21 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10013](https://developer.apple.com/videos/play/wwdc2021/10013)

App Clips give people the power to discover and download a small part of your app at a moment’s notice to complete tasks and transactions. Explore tips and best practices to help you create compact App Clips that emphasize modern features and elegant design. Learn how you can build reliable and secure App Clips to ensure that people can always access your experience when scanning a physical App Clip Code or viewing it through your website. And we’ll take you through specific strategies for testing an App Clip before releasing it to the world.

**Keywords:** `aasa`, `advanced experience`, `all compatible device variants`, `app clip codes`, `app clip invocation`, `app clips`, `app clip size`, `app thinning`, `archive build`, `asset catalogs`, `associated domain configuration`, `build settings`, `bundleid`, `compression`, `deep link`, `domain validation`, `embedded framwork`, `encode as url`, `ephemeral notification`, `fruta`, `lazy loading`, `local experience`, `location confirmation`, `managing complexity`, `maps`, `meta tag`, `nfc`, `physical invocation`, `qr code`, `rebuild from bitcode`, `redirect`, `sf symbols`, `shared asset catalog`, `shared container`, `siri suggestions`, `size optimization`, `size report`, `swcutil`, `testing`, `unique functionality`, `vector graphics`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,823 words)

## Documentation & Resources

- [Reducing your app’s size](https://developer.apple.com/documentation/Xcode/reducing-your-app-s-size) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/reducing-your-app-s-size
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/reducing-your-app-s-size.json
- [Testing the launch experience of your App Clip](https://developer.apple.com/documentation/AppClip/testing-the-launch-experience-of-your-app-clip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/testing-the-launch-experience-of-your-app-clip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/testing-the-launch-experience-of-your-app-clip.json

## Code Snippets

### SF Symbol and Text — [14:18]

```swift
label.text = "Hello"

// TextStyle for label and image
let textStyle = UIFont.TextStyle.largeTitle

// Use the same TextStyle for label and image
label.font = .preferredFont(forTextStyle: textStyle)
let config = UIImage.SymbolConfiguration(textStyle: textStyle)

imageView.image = UIImage(systemName: "pencil.and.outline", withConfiguration: config)

// Align baseline of text and symbol image
imageView.firstBaselineAnchor.constraint(equalTo: label.firstBaselineAnchor).isActive = true
```

### Meta Tag — [18:08]

```xml
<meta name="apple-itunes-app" content="app-id=myAppStoreID, app-clip-bundle-id=appClipBundleID, app-clip-display=card">
```

### Location Confirmation — [27:41]

```swift
if let activationPayload = userActivity?.appClipActivationPayload {
  activationPayload.confirmAcquired(in: region)
  { inRegion, error in
    if let error = error as? APActivationPayloadError {
      if error.code ==
      APActivationPayloadError.disallowed {
        // User denied permission
        // Or invocation was not from visual code or NFC
      } else if error.code ==
      APActivationPayloadError.doesNotMatch {
        // Activation payload is not the most recent
        // Catch in testing. Handle as above.
      }
    } else if error == nil {
      // Platform was able to determine location
      // OK to check inRegion
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10013/5/F623A344-AF7B-44AF-89A0-DF275CE40E7A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10013/5/F623A344-AF7B-44AF-89A0-DF275CE40E7A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10013) — developer.apple.com. Indexed for agent consumption._