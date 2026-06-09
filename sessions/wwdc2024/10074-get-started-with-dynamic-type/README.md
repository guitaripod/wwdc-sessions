---
id: "wwdc2024-10074"
event: "wwdc2024"
year: 2024
title: "Get started with Dynamic Type"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10074"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Get started with Dynamic Type

**Event:** WWDC24 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10074](https://developer.apple.com/videos/play/wwdc2024/10074)

Dynamic Type lets people choose their preferred text size across the system and all of their apps. To help you get started supporting Dynamic Type, we’ll cover the fundamentals: How it works, how to find issues with scaling text in your app, and how to take practical steps using SwiftUI and UIKit to create a great Dynamic Type experience. We’ll also show how you can best use the Large Content Viewer to make navigation controls accessible to everyone.

**Keywords:** `font`, `font scaling`, `font sizes`, `text accessibility`, `text styles`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,063 words)

## Documentation & Resources

- [Forum: Accessibility & Inclusion](https://developer.apple.com/forums/topics/accessibility-and-inclusion?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/accessibility-and-inclusion?cid=vf-a-0010
- [accessibilityShowsLargeContentViewer()](https://developer.apple.com/documentation/SwiftUI/View/accessibilityShowsLargeContentViewer()) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View/accessibilityShowsLargeContentViewer()
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View/accessibilityShowsLargeContentViewer().json
- [UILargeContentViewerInteraction](https://developer.apple.com/documentation/UIKit/UILargeContentViewerInteraction) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UILargeContentViewerInteraction
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UILargeContentViewerInteraction.json
- [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility
- [Human Interface Guidelines: Typography](https://developer.apple.com/design/human-interface-guidelines/typography) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/typography
- [Enhancing the accessibility of your SwiftUI app](https://developer.apple.com/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/enhancing-the-accessibility-of-your-swiftui-app.json

## Code Snippets

### Built-in text styles with SwiftUI — [3:53]

```swift
// Use built-in text styles with SwiftUI

import SwiftUI

struct ContentView: View {

    var body: some View {
        Text("Hello, World!")
            .font(.title)
    }

}
```

### Built-in text styles in UIKit — [4:06]

```swift
// Built-in text styles in UIKit

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let label = UILabel(frame: .zero)
        setupConstraints()
        label.text = "Hello, World!"
        label.adjustsFontForContentSizeCategory = true
        label.font = .preferredFont(forTextStyle: .title1)
        label.numberOfLines = 0

        self.view.addSubview(label)
    }
}
```

### Dynamic layout in SwiftUI — [7:20]

```swift
// Dynamic layout in SwiftUI

import SwiftUI

struct FigureCell: View {
    @Environment(\.dynamicTypeSize) 
    private var dynamicTypeSize: DynamicTypeSize

    var dynamicLayout: AnyLayout { 
        dynamicTypeSize.isAccessibilitySize ?
        AnyLayout(HStackLayout()) : AnyLayout(VStackLayout())
    }

    let systemImageName: String
    let imageTitle: String

    var body: some View {
        dynamicLayout {
            FigureImage(systemImageName: systemImageName)
            FigureTitle(imageTitle: imageTitle)
        }
    }
}
```

### Dynamic layout in SwiftUI — [7:52]

```swift
// Dynamic layout in SwiftUI

import SwiftUI

struct FigureContentView: View {
    @Environment(\.dynamicTypeSize) 
    private var dynamicTypeSize: DynamicTypeSize

    var dynamicLayout: AnyLayout {
        dynamicTypeSize.isAccessibilitySize ?
        AnyLayout(VStackLayout(alignment: .leading)) : AnyLayout(HStackLayout(alignment: .top))
    }

    var body: some View {
        dynamicLayout {
            FigureCell(systemImageName: "figure.stand", imageTitle: "Standing Figure")
            FigureCell(systemImageName: "figure.wave", imageTitle: "Waving Figure")
            FigureCell(systemImageName: "figure.walk", imageTitle: "Walking Figure")
            FigureCell(systemImageName: "figure.roll", imageTitle: "Rolling Figure")
        }
    }
}
```

### Dynamic layout in UIKit — [8:20]

```swift
// Dynamic layout in UIKit

import UIKit

class ViewController: UIViewController {
    private var mainStackView: UIStackView = UIStackView()

    required init?(coder: NSCoder) {
        super.init(coder: coder)
        NotificationCenter.default.addObserver(self, selector: #selector(textSizeDidChange(_:)), name: UIContentSizeCategory.didChangeNotification, object: nil)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        setupStackView()
    }

    @objc private func textSizeDidChange(_ notification: Notification?) {
        let isAccessibilityCategory = self.traitCollection.preferredContentSizeCategory.isAccessibilityCategory
        mainStackView.axis = isAccessibilityCategory ? .vertical : .horizontal
        setupConstraints()
    }
}
```

### Scale inline images with SwiftUI — [10:12]

```swift
// Inline images in SwiftUI

import SwiftUI

struct ContentView: View {

    var body: some View {
        List {
            FigureListCell(figureName: "Standing Figure",
                systemImage: "figure.stand")
            FigureListCell(figureName: "Rolling Figure",
                  systemImage: "figure.roll")
            FigureListCell(figureName: "Waving Figure",
                systemImage: "figure.wave")
            FigureListCell(figureName: "Walking Figure",
                systemImage: "figure.walk")
        }
    }

}
```

### Scale inline images with UIKit — [10:30]

```swift
// Inline images in UIKit

func attributedStringWithImage(systemImageName: String, imageTitle: String) ->       NSAttributedString {
    let attachment = NSTextAttachment()
    attachment.image = UIImage(systemName: systemImageName)

    let attachmentAttributedString = NSMutableAttributedString(attachment: attachment)
    attachmentAttributedString.append(NSAttributedString(string: imageTitle))

    return attachmentAttributedString
}
```

### Scale images in SwiftUI — [11:05]

```swift
// Scaling images in SwiftUI

import SwiftUI

struct ContentView: View {
    @ScaledMetric var imageWidth = 125.0
    var body: some View {
        VStack {
            Image("Spatula")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: imageWidth)
            Text("Grill Party!")
                .frame(alignment: .center)
        }
    }
}
```

### Scale symbols with UIKit — [11:38]

```swift
// Symbol configuration in UIKit

import UIKit

func imageWithBodyConfiguration(systemImageName: String) -> UIImage? {
  let imageConfiguration = UIImage.SymbolConfiguration(textStyle: .body)
  let configuredImage = UIImage(systemName: systemImageName, withConfiguration: imageConfiguration)
  return configuredImage
}
```

### Add large content viewer support with SwiftUI — [13:15]

```swift
// Large content viewer support in SwiftUI

import SwiftUI

struct FigureBar: View {
    @Binding var selectedFigure: Figure

    var body: some View {
       HStack {
            ForEach(Figure.allCases) { figure in
                FigureButton(figure: figure, isSelected: selectedFigure == figure)
                    .onTapGesture {
                        selectedFigure = figure
                    }
                    .accessibilityShowsLargeContentViewer {
                        Label(figure.imageTitle, systemImage: figure.systemImage)
                    }
            }
        }
    }
}
```

### Add large content viewer support with UIKit — [13:45]

```swift
// Large content viewer support in UIKit

import UIKit

class FigureCell: UIStackView {
    var systemImageName: String!
    var imageTitle: String!
    var imageLabel: UILabel!
    var titleImageView: UIImageView!

    required init(coder: NSCoder) {
        super.init(coder: coder)
        setupFigureCell()
    }

    init(systemImageName: String, imageTitle: String) {
        super.init(frame: .zero)

        self.systemImageName = systemImageName
        self.imageTitle = imageTitle

        setupFigureCell()

        self.addInteraction(UILargeContentViewerInteraction())
        self.showsLargeContentViewer = true
        self.largeContentImage = UIImage(systemName: systemImageName)
        self.scalesLargeContentImage = true
        self.largeContentTitle = imageTitle
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10074/4/3CB84B8B-3CC6-4EAB-AA46-E9FD7D160048/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10074/4/3CB84B8B-3CC6-4EAB-AA46-E9FD7D160048/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10074) — developer.apple.com. Indexed for agent consumption._
