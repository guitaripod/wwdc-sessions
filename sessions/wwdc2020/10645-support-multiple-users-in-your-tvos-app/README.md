---
id: "wwdc2020-10645"
event: "wwdc2020"
year: 2020
title: "Support multiple users in your tvOS app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10645"
topics: ["Audio & Video"]
platforms: ["tvOS"]
hasTranscript: true
---

# Support multiple users in your tvOS app

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** tvOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10645](https://developer.apple.com/videos/play/wwdc2020/10645)

Share your living room — not your Apple TV apps. When you support profiles within your app, you can customize your experience for each person who uses Apple TV within the same house. Discover how the “Runs as Current User” feature lets someone interact with your app, download local content, and log into iCloud or Game Center, all without affecting their family or housemates. We’ll show you how to implement this capability in your app, save recent data before switching profiles, handle notifications, and safeguard privacy. To get the most out of this session, you should have a basic understanding of modern tvOS frameworks and controls. Watching “Mastering the Living Room with tvOS” will give you a great overview.

**Keywords:** `apple tv`, `apple tv 4k`, `apple tv app`, `game developer`, `games`, `mulituser`, `personalizable`, `personalization`, `personalize`, `profile`, `profiles`, `runs as current user`, `tv`, `tv app`, `tv apps`, `tv dev`, `tv developer`, `tvos`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,358 words)

## Documentation & Resources

- [Supporting Multiple Users in Your tvOS App](https://developer.apple.com/documentation/TVServices/supporting-multiple-users-in-your-tvos-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TVServices/supporting-multiple-users-in-your-tvos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TVServices/supporting-multiple-users-in-your-tvos-app.json
- [Personalizing Your App for Each User on Apple TV](https://developer.apple.com/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv.json
- [Human Interface Guidelines: Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-tvos

## Code Snippets

### Application Lifecycle — [4:15]

```swift
func applicationWillTerminate(_ application: UIApplication) {
    guard game.hasUnsavedChanges else { return }

    let semaphore = DispatchSemaphore(value: 0)
    game.save { _ in semaphore.signal() }
    semaphore.wait()
}
```

### CloudKit Notifications — [5:17]

```swift
func application(
    _ application: UIApplication,
    didReceiveRemoteNotification userInfo: [AnyHashable : Any],
    fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
    if let notification = CKNotification(fromRemoteNotificationDictionary: userInfo),
       notification.subscriptionOwnerUserRecordID == game.currentUserRecordID {
        game.handle(notification, completionHandler: completionHandler)
    }
    else {
        completionHandler(.noData)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10645/5/2E2B228F-1C9A-450E-927C-0FC486316517/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10645) — developer.apple.com. Indexed for agent consumption._
