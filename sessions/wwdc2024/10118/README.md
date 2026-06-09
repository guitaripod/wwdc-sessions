---
id: "wwdc2024-10118"
event: "wwdc2024"
year: 2024
title: "What’s new in UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10118"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What’s new in UIKit

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10118](https://developer.apple.com/videos/play/wwdc2024/10118)

Explore everything new in UIKit, including tab and document launch experiences, transitions, and text and input changes. We’ll also discuss better-than-ever interoperability between UIKit and SwiftUI animations and gestures, as well as general improvements throughout UIKit.

**Keywords:** `symbols`, `traits`, `uiupdatelink`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,701 words)

## Documentation & Resources

- [Automatic trait tracking](https://developer.apple.com/documentation/UIKit/automatic-trait-tracking) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/automatic-trait-tracking
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/automatic-trait-tracking.json
- [UIUpdateLink](https://developer.apple.com/documentation/UIKit/UIUpdateLink) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIUpdateLink
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIUpdateLink.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/UIKit.json

## Code Snippets

### Using SwiftUI to animate UIViews with gestures — [0:01]

```swift
switch gesture.state {
case .changed:
    UIView.animate(.interactiveSpring) {
        bead.center = gesture.translation
    }

case .ended:
    UIView.animate(.spring) {
        bead.center = endOfBracelet
    }
}
```

### Setting failure requirements between gestures — [0:02]

```swift
// Inner SwiftUI double tap gesture

Circle()
    .gesture(doubleTap, name: "SwiftUIDoubleTap")


// Outer UIKit single tap gesture

func gestureRecognizer(
    _ gestureRecognizer: UIGestureRecognizer, 
    shouldRequireFailureOf other: UIGestureRecognizer
) -> Bool {
    other.name == "SwiftUIDoubleTap"
}
```

### Responding to horizontalSizeClass trait — [0:03]

```swift
class MyView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()

        if traitCollection.horizontalSizeClass == .compact {
            // apply compact layout
        } else {
            // apply regular layout
        }
    }
}
```

### Using the new automatic content and background configurations — [0:04]

```swift
func configurations(for location: FileLocation) ->
    (UIListContentConfiguration, UIBackgroundConfiguration) {

    var contentConfiguration = UIListContentConfiguration.cell()
    let backgroundConfiguration = UIBackgroundConfiguration.listCell()

    contentConfiguration.text = location.title
    contentConfiguration.image = location.thumbnailImage

    return (contentConfiguration, backgroundConfiguration)
}
```

### Using UIUpdateLink — [0:05]

```swift
let updateLink = UIUpdateLink(
    view: view,
    actionTarget: self,
    selector: #selector(update)
)
updateLink.requiresContinuousUpdates = true
updateLink.isEnabled = true

@objc func update(updateLink: UIUpdateLink,
                  updateInfo: UIUpdateInfo) {
    view.center.y = sin(updateInfo.modelTime)
        * 100 + view.bounds.midY
}
```

### An example of providing UICanvasFeedbackGenerator with additional context — [0:06]

```swift
@ViewLoading var feedbackGenerator: UICanvasFeedbackGenerator

override func viewDidLoad() {
    super.viewDidLoad()
    feedbackGenerator = UICanvasFeedbackGenerator(view: view)
}

func dragAligned(_ sender: UIPanGestureRecognizer) {
    feedbackGenerator.alignmentOccurred(at: sender.location(in: view))
}
```

### Using new attributes for highlight — [0:07]

```swift
var attributes = [NSAttributedString.Key: Any]()

// Highlight style
attributes[.textHighlightStyle] = 
NSAttributedString.TextHighlightStyle.default

// Highlight color scheme
attributes[.textHighlightColorScheme] =
NSAttributedString.TextHighlightColorScheme.default
```

### Customizing formatting panel — [0:08]

```swift
textView.textFormattingConfiguration = .init(groups: [
    .group([
        .component(.fontAttributes, .mini),
        .component(.fontPicker, .regular),
        .component(.textColor, .mini)
    ]),
    .group([
        .component(.fontPointSize, .mini),
        .component(.listStyles, .regular),
        .component(.highlight, .mini)
    ])
])
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10118/4/16FC914B-F442-41A4-AFF4-5047A3FF7125/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10118/4/16FC914B-F442-41A4-AFF4-5047A3FF7125/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10118) — developer.apple.com. Indexed for agent consumption._