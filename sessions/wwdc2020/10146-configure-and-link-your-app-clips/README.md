---
id: "wwdc2020-10146"
event: "wwdc2020"
year: 2020
title: "Configure and link your App Clips"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10146"
topics: ["Safari & Web", "SwiftUI & UI Frameworks", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Configure and link your App Clips

**Event:** WWDC20 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10146](https://developer.apple.com/videos/play/wwdc2020/10146)

App Clips are small parts of an app that offer a streamlined, direct experience and help people get what they need at the right time. Learn how you can invoke an App Clip through real-world experiences like App Clip Codes, NFC, and QR codes, or have them appear digitally through apps like Maps or Safari. We’ll show you how to handle links in your App Clip and demonstrate how to set up your associated domains. And discover how you can configure App Clip experiences in App Store Connect, add App Clip banners to your website, and thoroughly test your App Clips through TestFlight. To get the most out of this session, you should have experience using Universal Links and associated domains. For a primer, watch “What’s New in Universal Links” from WWDC19.

**Keywords:** `app clip banner`, `app clip codes`, `app clip experience`, `app store connect`, `maps`, `messages`, `nearby suggestions`, `nfc`, `nsuseractivity`, `qr codes`, `safari`, `web server`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,386 words)

## Documentation & Resources

- [App Clips](https://developer.apple.com/documentation/AppClip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip.json
- [Responding to invocations](https://developer.apple.com/documentation/AppClip/responding-to-invocations) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/responding-to-invocations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/responding-to-invocations.json
- [Configuring App Clip experiences](https://developer.apple.com/documentation/AppClip/configuring-the-launch-experience-of-your-app-clip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/configuring-the-launch-experience-of-your-app-clip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/configuring-the-launch-experience-of-your-app-clip.json
- [Fruta: Building a feature-rich app with SwiftUI](https://developer.apple.com/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui.json

## Code Snippets

### Update the apple-app-site-association file — [5:04]

```json
{
    "appclips": {
        "apps": [ "ABCDE12345.example.fruta.Clip" ]
    },

   ...
}
```

### Configure app clip for link handling (SwiftUI app life cycle) — [6:17]

```swift
import SwiftUI

@main
struct AppClip: App {
    var body: some Scene {
        WindowGroup {
           ContentView()
              .onContinueUserActivity(NSUserActivityTypeBrowsingWeb) { userActivity in
                  guard let incomingURL = userActivity.webpageURL,
                        let components = NSURLComponents(url: incomingURL,
                            resolvingAgainstBaseURL: true) 
                  else {
                      return
                  }

                  // Direct to the linked content in your app clip.
              }
        }
    }
}
```

### Configure app clip for link handling (UIKit scene-based life cycle) — [6:54]

```swift
// Handle NSUserActivity in UISceneDelegate.

class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func scene(_ scene: UIScene, continue userActivity: NSUserActivity) 
    {
        // Get URL components from the incoming user activity
        guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
            let incomingURL = userActivity.webpageURL,
            let components = NSURLComponents(url: incomingURL, 
                resolvingAgainstBaseURL: true) 
        else {
            return
        }

        // Direct to the linked content in your app clip.
    }

}
```

### Configure the Smart App Banner to open app clip (HTML) — [14:35]

```xml
<meta name="apple-itunes-app" 
    content="app-clip-bundle-id=com.example.fruta.Clip,
    app-id=123456789">
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10146/6/F04CF30D-7D67-44DC-83BA-E9AB09BD12F7/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10146) — developer.apple.com. Indexed for agent consumption._
