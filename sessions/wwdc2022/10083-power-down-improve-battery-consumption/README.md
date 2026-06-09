---
id: "wwdc2022-10083"
event: "wwdc2022"
year: 2022
title: "Power down: Improve battery consumption"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10083"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Power down: Improve battery consumption

**Event:** WWDC22 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10083](https://developer.apple.com/videos/play/wwdc2022/10083)

Discover how you can limit your power usage and help people get even more out of your app. We'll show you how you can reduce battery drain from your app by making four key changes to your code. Learn how to add Dark Mode to your app and benefit from OLED displays, audit frame rates from secondary animations, limit background data processing, and defer long running tasks.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,509 words)

## Documentation & Resources

- [Refreshing and Maintaining Your App Using Background Tasks](https://developer.apple.com/documentation/BackgroundTasks/refreshing-and-maintaining-your-app-using-background-tasks) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundTasks/refreshing-and-maintaining-your-app-using-background-tasks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundTasks/refreshing-and-maintaining-your-app-using-background-tasks.json
- [Adopting iOS Dark Mode](https://developer.apple.com/documentation/UIKit/adopting-ios-dark-mode) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adopting-ios-dark-mode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adopting-ios-dark-mode.json
- [Background Tasks](https://developer.apple.com/documentation/BackgroundTasks) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundTasks
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundTasks.json

## Code Snippets

### Create a CADisplayLink — [8:02]

```swift
// Create a display link

func createDisplayLink() {
   let displayLink = CADisplayLink(target: self, selector: #selector(step))

    // Configure your desired refresh rate by calling preferredFrameRateRange
    displayLink.preferredFrameRateRange = CAFrameRateRange(minimum: 10,
                                                           maximum: 60,
                                                           preferred: 30)

// then activate your CADisplayLink by adding it to the main runloop.
    displayLink.add(to: .current, forMode: .defaultRunLoopMode)
}
```

### Discretionary URLSession — [16:03]

```swift
// Set up background URL session 
let config = URLSessionConfiguration.background(withIdentifier: "com.app.attachments") 
let session = URLSession(configuration: config, delegate: ..., delegateQueue: ...) 

// Set discretionary 
config.isDiscretionary = true

// Set timeout intervals
config.timeoutIntervalForResource = 24 * 60 * 60 
config.timeoutIntervalForRequest = 60 

// Create request and task 
var request = URLRequest(url: url) 
request.addValue("...", forHTTPHeaderField: "...") 
let task = session.downloadTask(with: request) 

// Set time window of two hours
task.earliestBeginDate = Date(timeIntervalSinceNow: 2 * 60 * 60) 

// Set workload size 
task.countOfBytesClientExpectsToSend = 160 
task.countOfBytesClientExpectsToReceive = 4096 

task.resume()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10083/4/B0CF7C82-605A-4F0E-9BF2-C1F540932B45/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10083/4/B0CF7C82-605A-4F0E-9BF2-C1F540932B45/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10083) — developer.apple.com. Indexed for agent consumption._
