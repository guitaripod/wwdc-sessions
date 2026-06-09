---
id: "wwdc2025-227"
event: "wwdc2025"
year: 2025
title: "Finish tasks in the background"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/227"
topics: ["System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Finish tasks in the background

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-227](https://developer.apple.com/videos/play/wwdc2025/227)

Discover background execution advancements and understand how the system schedules runtime. We’ll discuss how to get the most out of background runtime to allow your app to deliver features in the background while maintaining a great foreground experience. We’ll also cover how APIs provide background runtime for your app, and how each API is tailored for different use cases — including new APIs in iOS and iPadOS 26 that let your app finish tasks as your app transitions from the foreground to the background.



## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,803 words)

## Documentation & Resources

- [Uploading asset resources in the background](https://developer.apple.com/documentation/PhotoKit/uploading-asset-resources-in-the-background) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PhotoKit/uploading-asset-resources-in-the-background
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PhotoKit/uploading-asset-resources-in-the-background.json
- [Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/BackgroundTasks/performing-long-running-tasks-on-ios-and-ipados) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundTasks/performing-long-running-tasks-on-ios-and-ipados
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundTasks/performing-long-running-tasks-on-ios-and-ipados.json
- [Background Tasks](https://developer.apple.com/documentation/BackgroundTasks) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundTasks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundTasks.json

## Code Snippets

### Register an app refresh task — [8:27]

```swift
import BackgroundTasks
import SwiftUI

@main
struct ColorFeed: App {
    var body: some Scene {
        WindowGroup {
            // ...
        }
        .backgroundTask(.appRefresh("com.colorfeed.wwdc25.appRefresh")) {
            await self.handleAppRefreshTask()
        }
    }
}
```

### Register a processing task — [9:45]

```swift
import BackgroundTasks
import UIKit

class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        BGTaskScheduler.shared.register(
            forTaskWithIdentifier: "com.example.apple-samplecode.ColorFeed.db_cleaning",
            using: nil
        ) { task in
            self.handleAppRefresh(task: task as! BGProcessingTask)
        }
    }

    func submitProcessingTaskRequest() {
        let request = BGProcessingTaskRequest(
            identifier: "com.example.apple-samplecode.ColorFeed.db_cleaning"
        )
        request.requiresNetworkConnectivity = true
        request.requiresExternalPower = true

        BGTaskScheduler.shared.submit(request)! 
    }
}
```

### Begin and end background task — [10:51]

```swift
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    var backgroundTaskID: UIBackgroundTaskIdentifier = .invalid

    func saveState() { /*  ... */ }

    func handlePersistence() {
        let app = UIApplication.shared
        guard backgroundTaskID != .invalid else { return }
        backgroundTaskID = app.beginBackgroundTask(withName: "Finish Export") {
            app.endBackgroundTask(self.backgroundTaskID)
            self.backgroundTaskID = .invalid
        }

        self.saveState()

        app.endBackgroundTask(backgroundTaskID)
        backgroundTaskID = .invalid
    }
}
```

### Continued processing task registration — [14:00]

```swift
import BackgroundTasks

func handleDialogConfirmation() {
    BGTaskScheduler.shared.register("com.colorfeed.wwdc25.userTask") { task in
        let task = task as! BGContinuedProcessingTask

        var shouldContinue = true
        task.expirationHandler = {
            shouldContinue = false
        }

        task.progress.totalUnitCount = 100
        task.progress.completedUnitCount = 0

        while shouldContinue {
            // Do some work
            task.progress.completedUnitCount += 1
        }

        task.setTaskCompleted(success: true)
    }
}
```

### Continued processing task submission — [15:47]

```swift
import BackgroundTasks

func submitContinuedProcessingTaskRequest() {
    let request = BGContinuedProcessingTaskRequest(
        identifier: "com.colorfeed.wwdc25.userTask",
        title: "A succinct title",
        subtitle: "A useful and informative subtitle"
    )

    request.strategy = .fail

    BGTaskScheduler.shared.submit(request)!
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/227/4/b4d5d5a5-5c5a-4f37-a4ad-66fea0b6f25d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/227/4/b4d5d5a5-5c5a-4f37-a4ad-66fea0b6f25d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/227) — developer.apple.com. Indexed for agent consumption._