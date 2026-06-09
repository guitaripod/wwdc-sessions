---
id: "wwdc2025-216"
event: "wwdc2025"
year: 2025
title: "Turbocharge your app for CarPlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/216"
topics: ["System Services", "App Services"]
platforms: ["iOS"]
hasTranscript: true
---

# Turbocharge your app for CarPlay

**Event:** WWDC25 · **Topic:** App Services · **Platforms:** iOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-216](https://developer.apple.com/videos/play/wwdc2025/216)

Learn how to bring your Live Activities and widgets to CarPlay and CarPlay Ultra so people can view progress of their activities and see relevant information at a glance. Explore new template options available to all CarPlay apps, and learn how navigation apps can provide turn-by-turn metadata for display in the car’s instrument cluster or HUD.

**Keywords:** `🚗`, `🚙`, `car`, `instrument cluster`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,077 words)

## Documentation & Resources

- [Adding StandBy and CarPlay support to your widget](https://developer.apple.com/documentation/WidgetKit/adding-standby-and-carplay-support-to-your-widget) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/adding-standby-and-carplay-support-to-your-widget
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/adding-standby-and-carplay-support-to-your-widget.json
- [Additional Tools for Xcode](https://developer.apple.com/download/all/?q=Additional%20Tools%20for%20Xcode) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/all/?q=Additional%20Tools%20for%20Xcode
- [CarPlay for developers](https://developer.apple.com/carplay) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/carplay

## Code Snippets

### Set CarPlay as a disfavored location — [3:21]

```swift
// Disfavored locations modifier for CarPlay

WidgetConfiguration()
    .disfavoredLocations([.carPlay], for: [.systemSmall])
```

### List template with pinned elements with grid buttons — [10:05]

```swift
// Pinned elements

var headerGridButtons: [CPGridButton]?

// Create a Grid Button

class CPGridButton

init(titleVariants: [String],
     image: UIImage,
     handler: ((CPGridButton) -> Void)?)
```

### List template with pinned elements with grid buttons for messages — [10:22]

```swift
// Pinned elements

var headerGridButtons: [CPGridButton]?

// For Communication apps

class CPGridButton

init(titleVariants: [String],
     image: UIImage,
     messageConfiguration: CPMessageGridItemConfiguration?,
     handler: ((CPGridButton) -> Void)?)

class CPMessageGridItemConfiguration

init(conversationIdentifier: String, unread: Bool)
```

### Now playing template with sports mode — [11:20]

```swift
// Now playing template with sports mode

let clock = CPNowPlayingSportsClock(elapsedTime: time, paused: false)

let status = CPNowPlayingSportsEventStatus(
    eventStatusText: ["1st"], // 1st quarter
    eventStatusImage: UIImage(named: "Semifinals"),
    eventClock: clock
)

let sports = CPNowPlayingModeSports(
    leftTeam: getLeftTeam(), // CPNowPlayingSportsTeam
    rightTeam: getRightTeam(), // CPNowPlayingSportsTeam
    eventStatus: status,
    backgroundArtwork: getBackgroundArtwork() // get UIImage
)

CPNowPlayingTemplate.sharedTemplate.nowPlayingMode = sports
```

### Multitouch callbacks — [14:15]

```swift
// Multitouch

// Zoom callback

func mapTemplate(_ mapTemplate: CPMapTemplate,
                 didUpdateZoomGestureWithCenter center: CGPoint,
                 scale: CGFloat,
                 velocity: CGFloat) {     }

// Pitch callback

func mapTemplate(_ mapTemplate: CPMapTemplate,
                 pitchWithCenter center: CGPoint) {     }

// Rotate callback

func mapTemplate(_ mapTemplate: CPMapTemplate,
                 didRotateWithCenter center: CGPoint,
                 rotation: CGFloat,
                 velocity: CGFloat) {     }
```

### Add support for metadata — [16:28]

```swift
// Add support for metadata

// Declare support

func mapTemplateShouldProvideNavigationMetadata(_ mapTemplate: CPMapTemplate) -> Bool {
    true
}

// Provide maneuver information up-front

cpNavigationSession.add(maneuvers)
cpNavigationSession.add(laneGuidance)

// Reroute

cpNavigationSession.pauseTrip(for: .rerouting, description: "Rerouting")
cpNavigationSession.resumeTrip(updatedRouteInformation: cpRouteInformation)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/216/4/e2928559-f686-450b-899e-329e93341e5b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/216/4/e2928559-f686-450b-899e-329e93341e5b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/216) — developer.apple.com. Indexed for agent consumption._
