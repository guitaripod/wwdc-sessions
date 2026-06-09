---
id: "wwdc2024-10181"
event: "wwdc2024"
year: 2024
title: "Xcode essentials"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10181"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Xcode essentials

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10181](https://developer.apple.com/videos/play/wwdc2024/10181)

Edit, debug, commit, repeat. Explore the suite of tools in Xcode that help you iterate quickly when developing apps. Discover tips and tricks to help optimize and boost your development workflow.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,490 words)

## Documentation & Resources

- [Testing](https://developer.apple.com/documentation/Xcode/testing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/testing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/testing.json
- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010
- [Including notes for testers with a beta release of your app](https://developer.apple.com/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/including-notes-for-testers-with-a-beta-release-of-your-app.json
- [Xcode updates](https://developer.apple.com/documentation/Updates/Xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Xcode.json

## Code Snippets

### Warning and error annotations — [10:26]

```swift
#warning("This is a warning annotation")
#error("This is an error annotation")
```

### Mark comments — [10:58]

```swift
// MARK: This is a section title
```

### Placeholder — [14:09]

```swift
<#placeholder#>
```

### showStarView() — [17:30]

```swift
showStarView()
```

### Breakpoint #1 — [17:51]

```swift
let task = URLSession.shared.dataTask(with: cloudURL, completionHandler: handleUpdatesFromCloud)
```

### Breakpoint #2 — [17:53]

```swift
videos = loadVideosFromCloud()
```

### Swift error breakpoint — [18:17]

```swift
let url = try! getVideoResourceFilePath()
```

### Swift error throw — [18:34]

```swift
throw URLLoadError.fileNotFound
```

### Conditional breakpoint — [18:59]

```swift
cloudURL.scheme == "https"
```

### Print statement in conditional breakpoint — [19:18]

```swift
p "Username is \(cloudURL.user())"
```

### guard clause — [19:44]

```swift
guard cloudURLs.allSatisfy({ $0. scheme == "https" }),
    session.configuration.networkServiceType == .video else {
    return
}
```

### p session — [19:56]

```swift
p session
```

### p first part of guard clause — [19:58]

```swift
cloudURLs.allSatisfy({ $0. scheme == "https" })
```

### p second part of guard clause — [20:02]

```swift
p session.configuration.networkServiceType == .video
```

### Random star rating — [20:11]

```swift
var starRating: Int {
  let randomStarRating = Int.random(n: 1..<5)
  return randomStarRating
}
```

### Converting starRatingPercentage to Int — [21:16]

```swift
var starRating: Int {
  return Int((starRatingPercentage * 5).rounded())
}
```

### print statements for debugging — [21:46]

```swift
var releaseDate: Date {
    print("🎬 Entering func \(#function) in \(#fileID)...")
    let currentDate = Date()
    let gregorianCal = Calendar(identifier: .gregorian)
    var components = DateComponents()
    components.year = releaseYear
    print("\(#fileID)@\(#line) \(#function): 📅 releaseYear is \(releaseYear)")
    if releaseYear == gregorianCal.component(.year, from: currentDate) {
        components.month = Int(releaseMonth)
        isNewRelease = true
        print("\(#fileID)@\(#line) \(#function): 🆕 this is a new release!")
    }
    if releaseYear < 2000 {
        isClassicMovie = true
        print("\(#fileID)@\(#line) \(#function): 🎻 this one is a classic!")
    }
    let calendar = Calendar(identifier: .gregorian)
    return calendar.date(from: components)!
}
```

### os_log statements for debugging — [22:09]

```swift
var releaseDate: Date {
    os_log(.debug, "🎬 Entering func \(#function) in \(#file)...")
    let currentDate = Date()
    let gregorianCal = Calendar(identifier: .gregorian)
    var components = DateComponents()
    components.year = releaseYear
    os_log(.info, "📅 releaseYear is \(releaseYear)")
    if releaseYear == gregorianCal.component(.year, from: currentDate) {
        components.month = Int(releaseMonth)
        isNewRelease = true
        os_log(.info, "🆕 this is a new release!")
    }
    if releaseYear < 2000 {
        isClassicMovie = true
        os_log(.info, "🎻 this one is a classic!")
    }
    let calendar = Calendar(identifier: .gregorian)
    return calendar.date(from: components)!
}
```

### Sample unit tests — [23:19]

```swift
import Testing
@testable import Destination_Video

struct DestinationVideo_UnitTests {

    private var library = VideoLibrary()

    // Make sure starRating is returning a percentage
    @Test func testStarRating() async throws {
        for video in library.videos {
            #expect(video.info.starRating > 0)
            #expect(video.info.starRating <= 5)
        }
    }

    // Make sure the library loads data from the json file
    @Test func testLibraryLoaded() async throws {
        #expect(library.videos.count > 1)
    }

}
```

### Sample UI tests — [24:15]

```swift
import XCTest

final class Destination_VideoUITests: XCTestCase {

    private var app: XCUIApplication!

    @MainActor override func setUpWithError() throws {
        // UI tests must launch the application that they test.
        app = XCUIApplication()
        app.launch()

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false
    }

    @MainActor func testABeach() throws {
        // Tap the button to load the detail view for the "A Beach" video
        let aBeachButton = app.buttons["A Beach"].firstMatch
        aBeachButton.tap()

        // Make sure it has a Play Video button after going to that view
        let playButton = app.buttons["Play Video"]
        XCTAssert(playButton.exists)

        // Make sure the star rating for this video contains 4 stars to avoid issue we saw previously where it was only a single star because starRating was incorrectly a percentage instead of an Int
        let theRatingView = app.staticTexts["TheRating"]
        XCTAssert(theRatingView.label.contains("⭐️⭐️⭐️⭐️⭐️"))
    }

    @MainActor func testMainView() throws {
        // We should have at least 10 buttons for the various videos
        let buttons = app.buttons
        XCTAssert(buttons.count >= 10)

        // Check that the most popular videos have buttons for them
        for expectedVideo in ["By the Lake", "Camping in the Woods", "Ocean Breeze"] {
            XCTAssert(app.buttons[expectedVideo].exists)
        }
    }

    @MainActor func testLaunchPerformance() throws {
        if #available(macOS 10.15, iOS 13.0, tvOS 13.0, watchOS 7.0, *) {
            // This measures how long it takes to launch your application.
            measure(metrics: [XCTApplicationLaunchMetric()]) {
                XCUIApplication().launch()
            }
        }
    }
}
```

### Swift Testing tags — [24:19]

```swift
@Test(.tags(.stars)) func testStarRating() async throws {
    for video in library.videos {
        #expect(video.info.starRating > 0)
        #expect(video.info.starRating <= 5)
    }
}

@Test(.tags(.library)) func testLibraryLoaded() async throws {
  #expect(library.videos.count > 1)
}

extension Tag {
  @Tag static var stars: Tag
  @Tag static var library: Tag
}
```

### Running xcodebuild test from the command line — [26:35]

```bash
xcodebuild test -scheme DestinationVideo
xcodebuild test -scheme DestinationVideo -testPlan TestAllTheThings
xcodebuild test -scheme DestinationVideo -testPlan TestAllTheThings -only-testing "Destination VideoUITests/testABeach"
```

### Missing Code Coverage — [29:03]

```swift
func toggleUpNextState(for video: Video) {
    if !upNext.contains(video) {
        // Insert the video at the beginning of the list.
        upNext.insert(video, at: 0)
    } else {
        // Remove the entry with the matching identifier.
        upNext.removeAll(where: { $0.id == video.id })
    }
    // Persist the Up Next state to disk.
    saveUpNext()
}
```

### Code Coverage executed 5 times — [29:19]

```swift
init() {
    // Load all videos available in the library.
    videos = loadVideos()
    // The first time the app launches, set the last three videos as the default Up Next items.
    upNext = loadUpNextVideos(default: Array(videos.suffix(3)))
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10181/4/39C00926-6B07-4887-86C2-95B4CF6C8745/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10181/4/39C00926-6B07-4887-86C2-95B4CF6C8745/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10181) — developer.apple.com. Indexed for agent consumption._
