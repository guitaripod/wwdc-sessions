---
id: "wwdc2024-10070"
event: "wwdc2024"
year: 2024
title: "Customize feature discovery with TipKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10070"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Customize feature discovery with TipKit

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10070](https://developer.apple.com/videos/play/wwdc2024/10070)

Focused on feature discovery, the TipKit framework makes it easy to display tips in your app. Now you can group tips so features are discovered in the ideal order, make tips reusable with custom tip identifiers, match the look and feel to your app, and sync tips using CloudKit. Learn how you can use the latest advances in TipKit to help people discover everything your app has to offer.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,313 words)

## Documentation & Resources

- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010
- [TipKit](https://developer.apple.com/documentation/TipKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TipKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TipKit.json

## Code Snippets

### Create new tips — [1:43]

```swift
// Create new tips

struct ShowLocationTip: Tip {
    var title: Text {
        Text("Show your location")
    }

    var message: Text? {
        Text("Tap the compass to highlight your current location on the map.")
    }

    var image: Image? {
        Image(systemName: "location.circle")
    }
}
```

### Create new tips — [1:54]

```swift
// Create new tips

struct ShowLocationTip: Tip {
    var title: Text {
        Text("Show your location")
    }

    var message: Text? {
        Text("Tap the compass to highlight your current location on the map.")
    }

    var image: Image? {
        Image(systemName: "location.circle")
    }
}

struct RotateMapTip: Tip {
    var title: Text {
        Text("Reorient the map")
    }

    var message: Text? {
        Text("Tap and hold on the compass to rotate the map back to 0° North.")
    }

    var image: Image? {
        Image(systemName: "hand.tap")
    }
}
```

### Show popover tips — [2:09]

```swift
// Show popover tips

struct MapCompassControl: View {
    let showLocationTip = ShowLocationTip()
    let rotateMapTip = RotateMapTip()

    var body: some View {
        CompassDial()
            .popoverTip(showLocationTip)
            .popoverTip(rotateMapTip)
            .onTapGesture {
                showCurrentLocation()
            }
            .onLongPressGesture(minimumDuration: 0.1) {
                reorientMapHeading()
            }
    }
}
```

### Create a TipGroup — [2:41]

```swift
// Create a TipGroup

struct MapCompassControl: View {
    @State
    var compassTips: TipGroup(.ordered) {
        ShowLocationTip()
        RotateMapTip()
    }

    var body: some View {
        CompassDial()
            .popoverTip(compassTips.currentTip)
            .onTapGesture {
                showCurrentLocation()
            }
            .onLongPressGesture(minimumDuration: 0.1) {
                reorientMapHeading()
            }
    }
}
```

### Show TipGroup tips on different views — [3:15]

```swift
// Show TipGroup tips on different views

struct MapControlsStack: View {
    @State
    var compassTips: TipGroup(.ordered) {
        ShowLocationTip()
        RotateMapTip()
    }

    var body: some View {
        VStack {
            ShowLocationButton()
                .popoverTip(compassTips.currentTip as? ShowLocationTip)
            RotateMapButton()
                .popoverTip(compassTips.currentTip as? RotateMapTip)
        }
    }
}
```

### Invalidate tips — [3:50]

```swift
// Invalidate tips

struct MapCompassControl: View {
    @State
    var compassTips: TipGroup(.ordered) {
        showLocationTip
        rotateMapTip
    }

    var body: some View {
        CompassDial()
            .popoverTip(compassTips.currentTip)
            .onTapGesture {
                showLocationTip.invalidate(reason: .actionPerformed)
                showCurrentLocation()
            }
            .onLongPressGesture(minimumDuration: 0.1) {
                rotateMapTip.invalidate(reason: .actionPerformed)
                reorientMapHeading()
            }
    }
}
```

### Create a tip — [5:37]

```swift
// Create a tip

struct ButlerForkTip: Tip {
    var title: Text {
        Text("Butler Fork is now available")
    }

    var message: Text? {
        Text("To see key trail info, tap Big Cottonwood Canyon on the map.")
    }

    var actions: [Action] {
        Action(title: "Go there now")
    }

    var rules: [Rule] {
        #Rule(Region.bigCottonwoodCanyon.didVisitEvent) {
            $0.donations.count > 3
        }
    }
}
```

### Show a TipView — [6:01]

```swift
// Show a TipView

struct ButlerForkTip: Tip {
    var title: Text {
        Text("Butler Fork is now available")
    }

    var message: Text? {
        Text("To see key trail info, tap Big Cottonwood Canyon on the map.")
    }

    var actions: [Action] {
        Action(title: "Go there now")
    }

    var rules: [Rule] {
        #Rule(Region.bigCottonwoodCanyon.didVisitEvent) {
            $0.donations.count > 3
        }
    }
}

struct TrailList: View {
    var trails: [Trail]

    var body: some View {
        ScrollView {
            let butlerForkTip = ButlerForkTip()
            TipView(butlerForkTip) { _ in
                highlightButlerForkTrail()
            }

            ListSection(title: "Trails", trails: trails)
        }
    }
}
```

### Create a reusable tip — [6:45]

```swift
// Create a reusable tip

struct NewTrailTip: Tip {
    let newTrail: Trail

    var title: Text {
        Text("\(newTrail.name) is now available")
    }

    var message: Text? {
        Text("To see key trail info, tap \(newTrail.region) on the map.")
    }

    var actions: [Action] {
        Action(title: "Go there now")
    }

    var id: String {
        "NewTrailTip-\(newTrail.id)"
    }

    var rules: [Rule] {
        #Rule(newTrail.region.didVisitEvent) {
            $0.donations.count > 3
        }
    }
}
```

### Show a TipView — [7:26]

```swift
// Show a TipView

struct NewTrailTip: Tip {
    let newTrail: Trail

    var title: Text {
        Text("\(newTrail.name) is now available")
    }

    var message: Text? {
        Text("To see key trail info, tap \(newTrail.region) on the map.")
    }

    var actions: [Action] {
        Action(title: "Go there now")
    }

    var id: String {
        "NewTrailTip-\(newTrail.id)"
    }

    var rules: [Rule] {
        #Rule(newTrail.region.didVisitEvent) {
            $0.donations.count > 3
        }
    }
}

struct TrailList: View {
    var trails: [Trail]
    let newTrail: Trail

    var body: some View {
        ScrollView {
            let newTrailTip = NewTrailTip(newTrail: newTrail)
            TipView(newTrailTip) { _ in
                highlightTrail(newTrailTip)
            }

            ListSection(title: "Trails", trails: trails)
        }
    }
}
```

### Create a custom TipViewStyle — [8:55]

```swift
// Create a custom TipViewStyle

struct NewTrailTipViewStyle: TipViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        let tip = configuration.tip as! NewTrailTip

        TrailImage(imageName: tip.newTrail.heroImage)
            .frame(maxHeight: 150)
            .overlay {
                VStack {
                    configuration.title.font(.title)
                    configuration.message.font(.subheadline)
                }
            }
    }
}

extension NewTrailTipViewStyle {
    struct TrailImage: View {
        let imageName: String

        var body: some View {
            Image(imageName)
                .resizable()
                .aspectRatio(contentMode: .fill)
        }
    }
}
```

### Apply a TipViewStyle — [9:20]

```swift
// Apply a TipViewStyle

struct NewTrailTipViewStyle: TipViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        let tip = configuration.tip as! NewTrailTip

        TrailImage(imageName: tip.newTrail.heroImage)
            .frame(maxHeight: 150)
            .overlay {
                VStack {
                    configuration.title.font(.title)
                    configuration.message.font(.subheadline)
                }
            }
    }
}

extension NewTrailTipViewStyle {
    struct TrailImage: View {
        let imageName: String

        var body: some View {
            Image(imageName)
                .resizable()
                .aspectRatio(contentMode: .fill)
        }
    }
}

struct TrailList: View {
    var trails: [Trail]
    let newTrail: Trail

    var body: some View {
        ScrollView {
            let newTrailTip = NewTrailTip(newTrail: newTrail)
            TipView(newTrailTip) { _ in
                highlightTrail(newTrailTip)
            }
            .tipViewStyle(NewTrailTipViewStyle())

            ListSection(title: "Trails", trails: trails)
        }
    }
}
```

### Add the tip's action handler — [9:45]

```swift
// Apply a TipViewStyle

struct NewTrailTipViewStyle: TipViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        let tip = configuration.tip as! NewTrailTip
        let highlightTrailAction = configuration.actions.first!

        TrailImage(imageName: tip.newTrail.heroImage)
            .frame(maxHeight: 150)
            .onTapGesture { highlightTrailAction.handler() }
            .overlay {
                VStack {
                    configuration.title.font(.title)
                    HStack {
                        configuration.message.font(.subheadline)
                        Spacer()
                        Image(systemName: "chevron.forward.circle")
                            .foregroundStyle(.white)
                    }
                }
            }
    }
}

extension NewTrailTipViewStyle {
    struct TrailImage: View {
        let imageName: String

        var body: some View {
            Image(imageName)
                .resizable()
                .aspectRatio(contentMode: .fill)
        }
    }
}

struct TrailList: View {
    var trails: [Trail]
    let newTrail: Trail

    var body: some View {
        ScrollView {
            let newTrailTip = NewTrailTip(newTrail: newTrail)
            TipView(newTrailTip) { _ in
                highlightTrail(newTrailTip)
            }
            .tipViewStyle(NewTrailTipViewStyle())

            ListSection(title: "Trails", trails: trails)
        }
    }
}
```

### Add CloudKit sync for tips — [11:38]

```swift
// Add CloudKit sync for tips

@main
struct TipKitTrails: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .task {
                    await configureTips()
                }
        }
    }

    func configureTips() async {
        do {
            try Tips.configure([
                .cloudKitContainer(.named("iCloud.com.apple.TipKitTrails.tips")),
                .displayFrequency(.weekly)
            ])
        }
        catch {
            print("Unable to configure tips: \(error)")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10070/5/8C64605E-ECD1-4D14-8B43-D7E3E751FAA3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10070/5/8C64605E-ECD1-4D14-8B43-D7E3E751FAA3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10070) — developer.apple.com. Indexed for agent consumption._
