---
id: "wwdc2020-10049"
event: "wwdc2020"
year: 2020
title: "Keep your complications up to date"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10049"
topics: ["SwiftUI & UI Frameworks", "System Services"]
platforms: ["watchOS"]
hasTranscript: true
---

# Keep your complications up to date

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10049](https://developer.apple.com/videos/play/wwdc2020/10049)

Time is of the essence: Discover how your Apple Watch complications can provide relevant information throughout the day and help people get the information they need, when they need it. Learn best practices for capitalizing on your app’s runtime opportunities, incorporating APIs like background app refresh and URLSession, and implementing well-timed push notifications.

**Keywords:** `🪁`, `⌚️`, `clockkit`, `urlsession`, `watchkit`, `watchos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,626 words)

## Documentation & Resources

- [Creating and updating a complication’s timeline](https://developer.apple.com/documentation/ClockKit/creating-and-updating-a-complication-s-timeline) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit/creating-and-updating-a-complication-s-timeline
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit/creating-and-updating-a-complication-s-timeline.json
- [URLSession Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/URLLoadingSystem/URLLoadingSystem.html) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/library/content/documentation/Cocoa/Conceptual/URLLoadingSystem/URLLoadingSystem.html
- [WatchKit](https://developer.apple.com/documentation/WatchKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WatchKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WatchKit.json
- [ClockKit](https://developer.apple.com/documentation/ClockKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit.json

## Code Snippets

### updateActiveComplications — [3:32]

```swift
class ExtensionDelegate: NSObject, WKExtensionDelegate {

    func updateActiveComplications() {

       let complicationServer = CLKComplicationServer.sharedInstance()

        if let activeComplications = complicationServer.activeComplications {

            for complication in activeComplications {

               complicationServer.reloadTimeline(for: complication)

            }
        } 
    }
}
```

### getCurrentTimelineEntry — [4:26]

```swift
class ComplicationController: NSObject, CLKComplicationDataSource {

    func getCurrentTimelineEntry(for complication: CLKComplication, 
        withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Void) {

        switch (complication.family) {

        case .modularSmall:
           let template = CLKComplicationTemplateModularLargeTallBody.init(
                               headerTextProvider: headerTextProvider, 
                               bodyTextProvider: bodyTextProvider)

            entry = CLKComplicationTimelineEntry(date: Date(), 
                        complicationTemplate: template)
        }

        handler(entry)
    }
}
```

### scheduleBar — [6:06]

```swift
private func scheduleBAR(_ first: Bool) {
        let now = Date()
        let scheduledDate = now.addingTimeInterval(first ? 60 : 15*60)

        let info:NSDictionary = [“submissionDate”:now]

        let wkExt = WKExtension.shared()
        wkExt.scheduleBackgroundRefresh(withPreferredDate: scheduledDate, userInfo:info)
        { (error: Error?) in
            if (error != nil) {
                print("background refresh could not be scheduled \(error.debugDescription)")
            } 
        }
   }
```

### handleBAR — [7:08]

```swift
class ExtensionDelegate: NSObject, WKExtensionDelegate {
    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {

        for task in backgroundTasks {

          switch task {
          case let backgroundTask as WKApplicationRefreshBackgroundTask:

                if let userInfo:NSDictionary = backgroundTask.userInfo as? NSDictionary {
                   if let then:Date = userInfo["submissionDate"] as! Date {
                      let interval = Date.init().timeIntervalSince(then)
                      print("interval since request was made \(interval)")
                   }
                }

                self.updateActiveComplications()

                self.scheduleBAR(first: false)

                backgroundTask.setTaskCompletedWithSnapshot(false)
```

### handleBAR (DataProvider) — [8:47]

```swift
class ExtensionDelegate: NSObject, WKExtensionDelegate {

    var healthDataProvider: HealthDataProvider

    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
        for task in backgroundTasks {
            switch task {
            case let backgroundTask as WKApplicationRefreshBackgroundTask:

                healthDataProvider.refresh() { (update: Bool) -> Void in
                    if update {
                        self.updateActiveComplications()
                    }
                    self.scheduleBAR(first: false)
                    backgroundTask.setTaskCompletedWithSnapshot(false)
                }
```

### Instantiate backgroundURLSession — [11:35]

```swift
class WeatherDataProvider : NSObject, URLSessionDownloadDelegate {

    private lazy var backgroundURLSession: URLSession = {
        let config = URLSessionConfiguration.background(withIdentifier: “BackgroundWeather")
        config.isDiscretionary = false
        config.sessionSendsLaunchEvents = true

        return URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }()
```

### Schedule backgroundURLSessionTask — [12:02]

```swift
func schedule(_ first: Bool) {

        if backgroundTask == nil {

            if let url = self.currentWeatherURLForLocation(delegate.currentLocationCoordinate)
            {
                let bgTask = backgroundURLSession.downloadTask(with: url)

                bgTask.earliestBeginDate = Date().addingTimeInterval(first ? 60 : 15*60)

                bgTask.countOfBytesClientExpectsToSend = 200
                bgTask.countOfBytesClientExpectsToReceive = 1024

                bgTask.resume()

                backgroundTask = bgTask
            }
        }
    }
}
```

### handle backgroundURLSession — [13:29]

```swift
class ExtensionDelegate: NSObject, WKExtensionDelegate {

   var weatherDataProvider:WeatherDataProvider

    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
       for task in backgroundTasks {
           switch task {

                case let urlSessionTask as WKURLSessionRefreshBackgroundTask:

                    weatherDataProvider.refresh() { (update: Bool) -> Void in
                        weatherDataProvider.schedule(first: false)
                        if update {
                            self.updateActiveComplications()
                        }
                        urlSessionTask.setTaskCompletedWithSnapshot(false)
                    }
```

### handle backgroundURLSession — [13:59]

```swift
class WeatherDataProvider : NSObject, URLSessionDownloadDelegate {

    var completionHandler : ((_ update: Bool) -> Void)?

    func refresh(_ completionHandler: @escaping (_ update: Bool) -> Void) {

        self.completionHandler = completionHandler

    }
```

### didFinishDownloadingTo — [14:08]

```swift
class WeatherDataProvider : NSObject, URLSessionDownloadDelegate {

    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {

        if location.isFileURL {
            do {

                let jsonData = try Data(contentsOf: location)
                if let kiteFlyingWeather = KiteFlyingWeather(jsonData) {
                    // Process weather data here.
                }

            } catch let error as NSError {
                print("could not read data from \(location)")
            }
        }
    }
```

### didComplete — [14:23]

```swift
func urlSession(_ session: URLSession, task: URLSessionTask, 
                     didCompleteWithError error: Error?) {

        print("session didCompleteWithError \(error.debugDescription)”)

        DispatchQueue.main.async {

           self.completionHandler?(error == nil)

            self.completionHandler = nil

        }
    }
}
```

### Complication Pushes — [17:53]

```swift
class PushNotificationProvider : NSObject, PKPushRegistryDelegate {

    func startPushKit() -> Void {
        let pushRegistry = PKPushRegistry(queue: .main)
        pushRegistry.delegate = self
        pushRegistry.desiredPushTypes = [.complication]
    }

    func pushRegistry(_ registry: PKPushRegistry, 
                      didUpdate pushCredentials: PKPushCredentials, for type: PKPushType) {
        // Send credentials to server 
    }

    func pushRegistry(_ registry: PKPushRegistry, 
                        didReceiveIncomingPushWith payload: PKPushPayload, 
                        for type: PKPushType, completion: @escaping () -> Void) {
        // Process payload
        delegate.updateActiveComplications()
        completion()
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10049/10/CD3717B4-610A-4738-8C94-A2B995381A44/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10049) — developer.apple.com. Indexed for agent consumption._
