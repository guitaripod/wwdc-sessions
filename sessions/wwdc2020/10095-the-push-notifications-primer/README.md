---
id: "wwdc2020-10095"
event: "wwdc2020"
year: 2020
title: "The Push Notifications primer"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10095"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# The Push Notifications primer

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10095](https://developer.apple.com/videos/play/wwdc2020/10095)

Help people get the most out of your app with push notifications for important events and updates — and by delivering up-to-date data in the background, so that it is ready when they open your app. Discover how you can use notifications and alert people to timely and relevant information. Learn the differences between alert and background notifications, how to adopt them in your apps, and avoid mistakes by using the right APIs for the job.

**Keywords:** `alert`, `background`, `push`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,814 words)

## Documentation & Resources

- [Implementing Background Push Notifications](https://developer.apple.com/documentation/UserNotifications/implementing-background-push-notifications) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/implementing-background-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/implementing-background-push-notifications.json
- [Implementing Alert Push Notifications](https://developer.apple.com/documentation/UserNotifications/implementing-alert-push-notifications) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/implementing-alert-push-notifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/implementing-alert-push-notifications.json

## Code Snippets

### Registering for notifications — [2:02]

```swift
class AppDelegate: UIResponder, UIApplicationDelegate, UNUserNotificationCenterDelegate {

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        UIApplication.shared.registerForRemoteNotifications()
        UNUserNotificationCenter.current().delegate = self
        return true
    }
```

### UIApplicationDelegate callbacks — [2:36]

```swift
func application(_ application: UIApplication,
                   didFailToRegisterForRemoteNotificationsWithError error: Error) {
    // The token is not currently available.
    print("Remote notification is unavailable: \(error.localizedDescription)")
}

func application(_ application: UIApplication,
                   didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
     // Forward the token to your provider, using a custom method.
     self.forwardTokenToServer(token: deviceToken)
}
```

### Forward token to server — [3:05]

```swift
func forwardTokenToServer(token: Data) {
    let tokenComponents = token.map { data in String(format: "%02.2hhx", data) }
    let deviceTokenString = tokenComponents.joined()
    let queryItems = [URLQueryItem(name: "deviceToken", value: deviceTokenString)]
    var urlComps = URLComponents(string: "www.example.com/register")!
    urlComps.queryItems = queryItems
    guard let url = urlComps.url else {
        return
    }

    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        // Handle data
    }

    task.resume()
}
```

### Request authorization — [3:47]

```swift
@IBAction func subscribeToNotifications(_ sender: Any) {
    let userNotificationCenter = UNUserNotificationCenter.current()
    userNotificationCenter.requestAuthorization(options: [.alert, .sound, .badge]) { (granted, error) in
        print("Permission granted: \(granted)")
    }
}
```

### Payload JSON — [4:43]

```json
{
    "aps" : {
       "alert" : {
            "title" : "Check out our new special!",
            "body" : "Avocado Bacon Burger on sale"
        },
        "sound" : "default",
        "badge" : 1,
   },
    "special" : "avocado_bacon_burger",
    "price" : "9.99"
}
```

### didReceive response — [6:11]

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                            didReceive response: UNNotificationResponse,
                            withCompletionHandler completionHandler: @escaping () -> Void) {
    let userInfo = response.notification.request.content.userInfo
    guard let specialName = userInfo["special"] as? String,
          let specialPriceString = userInfo["price"] as? String,
          let specialPrice = Float(specialPriceString) else {
        // Always call the completion handler when done.
        completionHandler()
        return
    }

    let item = Item(name: specialName, price: specialPrice)
		addItemToCart(item)
  	showCartViewController()
    completionHandler()
 }
```

### Register for remote notifications (Background) — [8:16]

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
       UIApplication.shared.registerForRemoteNotifications()
       return true
    }
```

### Background Notification Payload — [9:05]

```json
{
    "aps" : {
       "content-available" : 1
    },
    "myCustomKey" : "myCustomData"
}
```

### didReceiveRemoteNotification — [9:33]

```swift
func application(_ application: UIApplication,
                     didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                     fetchCompletionHandler completionHandler:
                     @escaping (UIBackgroundFetchResult) -> Void) {
    guard let url = URL(string: "www.example.com/todays-menu") else {
        completionHandler(.failed)
        return
    }

    let task = URLSession.shared.dataTask(with: url) { data, response, error in
        guard let data = data else {
            completionHandler(.noData)
            return
        }

        updateMenu(withData: data)
        completionHandler(.newData)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10095/3/ED74BA77-B586-4360-B7A1-ABA71109064A/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10095) — developer.apple.com. Indexed for agent consumption._
