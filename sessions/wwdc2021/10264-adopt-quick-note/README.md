---
id: "wwdc2021-10264"
event: "wwdc2021"
year: 2021
title: "Adopt Quick Note"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10264"
topics: ["Safari & Web", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Adopt Quick Note

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10264](https://developer.apple.com/videos/play/wwdc2021/10264)

Learn how you can link your app to Quick Note and help people quickly connect your content to their notes — and their notes to your content. Discover how Quick Note recognizes and links to app content through NSUserActivity, and find out how you can adopt this API in your app. We’ll take you through the requirements, benefits, and features of supporting Quick Note. We'll also provide guidance and best practices for NSUserActivity to help your app get all of its benefits.

**Keywords:** `quicknote`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,118 words)

## Documentation & Resources

- [NSUserActivity](https://developer.apple.com/documentation/Foundation/NSUserActivity) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/NSUserActivity
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/NSUserActivity.json

## Code Snippets

### How to adopt NSUserActivity to support Quick Note — [16:57]

```swift
// Create the NSUserActivity and describe the content or user activity
let activity = NSUserActivity(activityType: "com.myapp.MyActivityType")
activity.title = document.title

// Set one or more of:
//   .targetContentIdentifier
//   .persistentIdentifier
//   .webpageURL
activity.targetContentIdentifier = "uniqueGlobalStableIdentifier"

// Set userInfo to save app-specific state information 
activity.userInfo = ["myKey": …]

// Attach it to a view controller, window, or other responder; let the system make it current when needed
viewController.userActivity = activity
```

### Handle NSUserActivity continuation in your window scene delegate or app delegate - iOS — [17:02]

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func scene(_ scene: UIScene, willContinueUserActivityWithType userActivityType: String) {
        // show user feedback while waiting for the NSUserActivity to arrive
    }

    func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
        // set up view controllers and views to continue the activity
    }

    func scene(_ scene: UIScene, didFailToContinueUserActivityWithType userActivityType: String, error: Error) {
        // show error about failing to continue an activity
    }

    …
}
```

### Handle NSUserActivity continuation in your window scene delegate or app delegate - macOS — [17:06]

```swift
class AppDelegate: NSObject, NSApplicationDelegate {

    func application(_ application: NSApplication, willContinueUserActivityWithType userActivityType: String) -> Bool {
        // show user feedback while waiting for the NSUserActivity to arrive
        return true
    }

    func application(_ application: NSApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([NSUserActivityRestoring]) -> Void) -> Bool {
        // set up view controllers or documents to continue the activity
        return true
    }

    func application(_ application: NSApplication, didFailToContinueUserActivityWithType userActivityType: String, error: Error) {
        // show error about failing to continue an activity, if appropriate
    }

    …
}
```

### Improve performance with needsSave — [17:26]

```swift
activity.needsSave = true

…

func userActivityWillSave(_ userActivity: NSUserActivity) {
    userActivity.userInfo = [
        "center" : visibleFrame.middle
        "zoomScale" : scrollView.zoomScale
    ]
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10264/3/A5939C70-9333-4792-A9D5-A98FF6347D4C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10264/3/A5939C70-9333-4792-A9D5-A98FF6347D4C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10264) — developer.apple.com. Indexed for agent consumption._
