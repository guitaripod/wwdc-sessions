---
id: "wwdc2022-10072"
event: "wwdc2022"
year: 2022
title: "Use SwiftUI with UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10072"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Use SwiftUI with UIKit

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10072](https://developer.apple.com/videos/play/wwdc2022/10072)

Learn how to take advantage of the power of SwiftUI in your UIKit app. Build custom UICollectionView and UITableView cells seamlessly with SwiftUI using UIHostingConfiguration. We’ll also show you how to manage data flow between UIKit and SwiftUI components within your app. To get the most out of this session, we encourage basic familiarity with SwiftUI.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,481 words)

## Documentation & Resources

- [selfSizingInvalidation](https://developer.apple.com/documentation/uikit/uitableview/4001105-selfsizinginvalidation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/uikit/uitableview/4001105-selfsizinginvalidation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/4001105-selfsizinginvalidation.json
- [selfSizingInvalidation](https://developer.apple.com/documentation/uikit/uicollectionview/4001100-selfsizinginvalidation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/uikit/uicollectionview/4001100-selfsizinginvalidation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/4001100-selfsizinginvalidation.json
- [Managing model data in your app](https://developer.apple.com/documentation/SwiftUI/Managing-model-data-in-your-app) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Managing-model-data-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Managing-model-data-in-your-app.json
- [UIHostingConfiguration](https://developer.apple.com/documentation/SwiftUI/UIHostingConfiguration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/UIHostingConfiguration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/UIHostingConfiguration.json
- [UIHostingController](https://developer.apple.com/documentation/SwiftUI/UIHostingController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/UIHostingController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/UIHostingController.json
- [Using SwiftUI with UIKit](https://developer.apple.com/documentation/UIKit/using-swiftui-with-uikit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/using-swiftui-with-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/using-swiftui-with-uikit.json
- [UIViewController](https://developer.apple.com/documentation/UIKit/UIViewController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIViewController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIViewController.json

## Code Snippets

### Presenting a UIHostingController — [2:09]

```swift
// Presenting a UIHostingController

let heartRateView = HeartRateView() // a SwiftUI view
let hostingController = UIHostingController(rootView: heartRateView)

// Present the hosting controller modally
self.present(hostingController, animated: true)
```

### Embedding a UIHostingController — [2:31]

```swift
// Embedding a UIHostingController

let heartRateView = HeartRateView() // a SwiftUI view
let hostingController = UIHostingController(rootView: heartRateView)

// Add the hosting controller as a child view controller
self.addChild(hostingController)
self.view.addSubview(hostingController.view)
hostingController.didMove(toParent: self)

// Now position & size the hosting controller’s view as desired…
```

### Presenting UIHostingController as a popover — [3:13]

```swift
// Presenting UIHostingController as a popover

let heartRateView = HeartRateView() // a SwiftUI view
let hostingController = UIHostingController(rootView: heartRateView)

// Enable automatic preferredContentSize updates on the hosting controller
hostingController.sizingOptions = .preferredContentSize

hostingController.modalPresentationStyle = .popover
self.present(hostingController, animated: true)
```

### Passing data to SwiftUI with manual UIHostingController updates — [5:27]

```swift
// Passing data to SwiftUI with manual UIHostingController updates

struct HeartRateView: View {
    var beatsPerMinute: Int

    var body: some View {
        Text("\(beatsPerMinute) BPM")
    }
}

class HeartRateViewController: UIViewController {
    let hostingController: UIHostingController< HeartRateView >
    var beatsPerMinute: Int {
        didSet { update() }
    }

    func update() {
        hostingController.rootView = HeartRateView(beatsPerMinute: beatsPerMinute)
    }
}
```

### Passing an ObservableObject to automatically update SwiftUI views — [7:51]

```swift
// Passing an ObservableObject to automatically update SwiftUI views

class HeartData: ObservableObject {
    @Published var beatsPerMinute: Int

    init(beatsPerMinute: Int) {
       self.beatsPerMinute = beatsPerMinute
    }
}

struct HeartRateView: View {
    @ObservedObject var data: HeartData

    var body: some View {
        Text("\(data.beatsPerMinute) BPM")
    }
}
```

### Passing an ObservableObject to automatically update SwiftUI views — [8:30]

```swift
// Passing an ObservableObject to automatically update SwiftUI views

class HeartRateViewController: UIViewController {
    let data: HeartData
    let hostingController: UIHostingController<HeartRateView>  

    init(data: HeartData) {
        self.data = data
        let heartRateView = HeartRateView(data: data)
        self.hostingController = UIHostingController(rootView: heartRateView)
    }
}
```

### UIHostingConfiguration — [9:52]

```swift
cell.contentConfiguration = UIHostingConfiguration {
  // Start writing SwiftUI here!
}
```

### Building a custom cell using SwiftUI with UIHostingConfiguration — [11:02]

```swift
// Building a custom cell using SwiftUI with UIHostingConfiguration

cell.contentConfiguration = UIHostingConfiguration {
    HeartRateTitleView()
}

struct HeartRateTitleView: View {
    var body: some View {
        HStack {
            Label("Heart Rate", systemImage: "heart.fill")
                .foregroundStyle(.pink)
                .font(.system(.subheadline, weight: .bold))
            Spacer()
            Text(Date(), style: .time)
                .foregroundStyle(.secondary)
                .font(.footnote)
        }
    }
}
```

### Building a custom cell using SwiftUI with UIHostingConfiguration — [12:46]

```swift
// Building a custom cell using SwiftUI with UIHostingConfiguration

cell.contentConfiguration = UIHostingConfiguration {
    VStack(alignment: .leading) {
        HeartRateTitleView()
        Spacer()
        HeartRateBPMView()
    }
}

struct HeartRateBPMView: View {
    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text("90")
                .font(.system(.title, weight: .semibold))
            Text("BPM")
                .foregroundStyle(.secondary)
                .font(.system(.subheadline, weight: .bold))
        }
    }
}
```

### Building a custom cell using SwiftUI with UIHostingConfiguration, with a chart! — [13:41]

```swift
// Building a custom cell using SwiftUI with UIHostingConfiguration

cell.contentConfiguration = UIHostingConfiguration {
    VStack(alignment: .leading) {
        HeartRateTitleView()
        Spacer()
        HStack(alignment: .bottom) {
            HeartRateBPMView()
            Spacer()
            Chart(heartRateSamples) { sample in
                LineMark(x: .value("Time", sample.time),
                         y: .value("BPM", sample.beatsPerMinute))
                   .symbol(Circle().strokeBorder(lineWidth: 2))
                   .foregroundStyle(.pink)
            }
        }
    }
}
```

### Content margins — [14:41]

```swift
cell.contentConfiguration = UIHostingConfiguration {
    HeartRateBPMView()
}
.margins(.horizontal, 16)
```

### Cell backgrounds — [15:16]

```swift
cell.contentConfiguration = UIHostingConfiguration {
   HeartTitleView()
} 
.background(.pink)
```

### List swipe actions — [16:32]

```swift
cell.contentConfiguration = UIHostingConfiguration {
    MedicalConditionView()
        .swipeActions(edge: .trailing) { … }
}
```

### Incorporating UIKit cell states — [17:25]

```swift
// Incorporating UIKit cell states

cell.configurationUpdateHandler = { cell, state in
    cell.contentConfiguration = UIHostingConfiguration {
      HStack {
        HealthCategoryView()
            Spacer()
            if state.isSelected {
                Image(systemName: "checkmark")
            }
        }
    }
}
```

### Creating a two-way binding to data in SwiftUI — [23:17]

```swift
// Creating a two-way binding to data in SwiftUI

class MedicalCondition: Identifiable, ObservableObject {
    let id: UUID

    @Published var text: String
}

struct MedicalConditionView: View {
    @ObservedObject var condition: MedicalCondition

    var body: some View {
        HStack {

            Spacer()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10072/4/03036EB8-1A2E-4ADD-A5A3-C50A9AFA841C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10072/4/03036EB8-1A2E-4ADD-A5A3-C50A9AFA841C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10072) — developer.apple.com. Indexed for agent consumption._
