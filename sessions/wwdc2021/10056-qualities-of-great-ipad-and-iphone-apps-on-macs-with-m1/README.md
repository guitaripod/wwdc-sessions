---
id: "wwdc2021-10056"
event: "wwdc2021"
year: 2021
title: "Qualities of great iPad and iPhone apps on Macs with M1"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10056"
topics: ["App Store, Distribution & Marketing", "Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Qualities of great iPad and iPhone apps on Macs with M1

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10056](https://developer.apple.com/videos/play/wwdc2021/10056)

It’s easier than ever to offer your existing iPad and iPhone apps on Macs with M1. We’ll show you how to bring your app to macOS, and explore how the system automatically bridges various features of your app to work on the Mac. We'll also provide guidance on best practices in your iPad app, combined with improvements in macOS Monterey — like Apple Pay support, improved AV handling, and shortcuts — to provide the fullest experience on Macs with M1.

**Keywords:** `alternatives`, `bridging`, `catalyst`, `ios`, `ipad mac`, `iphone mac`, `keyboard`, `mac app store`, `ple silicon`, `uikit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,484 words)

## Documentation & Resources

- [Building and improving your app with Mac Catalyst](https://developer.apple.com/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-and-improving-your-app-with-mac-catalyst.json
- [Running your iOS apps in macOS](https://developer.apple.com/documentation/Apple-Silicon/running-your-ios-apps-in-macos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Apple-Silicon/running-your-ios-apps-in-macos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Apple-Silicon/running-your-ios-apps-in-macos.json

## Code Snippets

### Limit the range of allowable scene sizes — [7:16]

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    guard let windowScene = scene as? UIWindowScene, let sizeRestrictions = windowScene.sizeRestrictions else { return }
    sizeRestrictions.minimumSize = CGSize(width: 640, height: 480)
    sizeRestrictions.maximumSize = CGSize(width: 1920, height: 1080)
}
```

### Automatically enable Touch Alternatives — [15:03]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>defaultEnablement</key>
    <true/>
    <key>version</key>
    <real>1</real>
    <key>requiredOnboarding</key>
    <array>                              <!-- Only include applicable features! -->
        <string>Tap</string>
        <string>Arrow Swipe</string>
        <string>Scroll Drag</string>
        <string>Tilt</string>
        <string>Trackpad Capture</string>
    </array>
</dict>
</plist>
```

### Required delegate method to enable Apple Pay support — [17:17]

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController,
	didRequestMerchantSessionUpdate
	handler: @escaping (PKPaymentRequestMerchantSessionUpdate) -> Void)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10056/3/6A9E120D-9217-4F54-98A5-853D65EDBCDE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10056/3/6A9E120D-9217-4F54-98A5-853D65EDBCDE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10056) — developer.apple.com. Indexed for agent consumption._
