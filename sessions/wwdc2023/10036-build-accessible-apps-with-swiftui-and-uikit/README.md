---
id: "wwdc2023-10036"
event: "wwdc2023"
year: 2023
title: "Build accessible apps with SwiftUI and UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10036"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build accessible apps with SwiftUI and UIKit

**Event:** WWDC23 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10036](https://developer.apple.com/videos/play/wwdc2023/10036)

Discover how advancements in UI frameworks make it easier to build rich, accessible experiences. Find out how technologies like VoiceOver can better interact with your app’s interface through accessibility traits and actions. We’ll share the latest updates to SwiftUI that help you refine your accessibility experience and show you how to keep accessibility information up-to-date in your UIKit apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,073 words)

## Documentation & Resources

- [Accessibility updates](https://developer.apple.com/documentation/Updates/Accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Accessibility.json
- [Accessibility](https://developer.apple.com/documentation/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/accessibility.json

## Code Snippets

### Add the accessibility toggle trait — [1:54]

```swift
import SwiftUI

struct FilterButton: View {
    @State var filter: Bool = false

    var body: some View {
        Button(action: { filter.toggle() }) {
            Text("Filter")
        }
        .background(filter ? darkGreen : lightGreen)
        .accessibilityAddTraits(.isToggle)
    }
}
```

### Add the accessibility toggle trait with UIKit — [2:31]

```swift
import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()

        let filterButton = UIButton(type: .custom)

        setupButtonView()

        filterButton.accessibilityTraits = [.toggleButton]

        view.addSubview(filterButton)
    }
}
```

### Post an accessibility notification — [3:43]

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            PhotoFilterView
                .toolbar {
                    Button(action: {
                        AccessibilityNotification.Announcement("Loading Photos View")
                            .post()
                    }) {
                        Text("Photos")
                    }
                }
        }
    }
}
```

### Assign announcement priority — [5:13]

```swift
import SwiftUI

struct ZoomingImageView: View {

    var defaultPriorityAnnouncement = AttributedString("Opening Camera")

    var lowPriorityAnnouncement: AttributedString {
        var lowPriorityString = AttributedString("Camera Loading")
        lowPriorityString.accessibilitySpeechAnnouncementPriority = .low
        return lowPriorityString
    }

    var highPriorityAnnouncement: AttributedString {
        var highPriorityString = AttributedString("Camera Active")
        highPriorityString.accessibilitySpeechAnnouncementPriority = .high
        return highPriorityString
    }

    // ...
}
```

### Post announcements with priority set — [5:46]

```swift
import SwiftUI

struct CameraButton: View {

    // ...

    var body: some View {
        Button(action: {
            // Open Camera Code
            AccessibilityNotification.Announcement(defaultPriorityAnnouncement).post()
            // Camera Loading Code
            AccessibilityNotification.Announcement(lowPriorityAnnouncement).post()
            // Camera Loaded Code
            AccessibilityNotification.Announcement(highPriorityAnnouncement).post()
        }) {
            Image("Camera")
           }
        }
    }
}
```

### Assign announcement priority with UIKit — [6:15]

```swift
class ViewController: UIViewController {
    let defaultAnnouncement = NSAttributedString(string: "Opening Camera", attributes: 
        [NSAttributedString.Key.UIAccessibilitySpeechAttributeAnnouncementPriority: 
        UIAccessibilityPriority.default]
    )

    let lowPriorityAnnouncement = NSAttributedString(string: "Camera Loading", attributes:   
        [NSAttributedString.Key.UIAccessibilitySpeechAttributeAnnouncementPriority:
        UIAccessibilityPriority.low]
    )

    let highPriorityAnnouncement = NSAttributedString(string: "Camera Active", attributes: 
        [NSAttributedString.Key.UIAccessibilitySpeechAttributeAnnouncementPriority:  
        UIAccessibilityPriority.high]
    )

    // ...
}
```

### Add the accessibility zoom action — [6:56]

```swift
struct ZoomingImageView: View {
    @State private var zoomValue = 1.0
    @State var imageName: String?

    var body: some View {
        Image(imageName ?? "")
            .scaleEffect(zoomValue)
            .accessibilityZoomAction { action in
                let zoomQuantity = "\(Int(zoomValue)) x zoom"
                switch action.direction {
                case .zoomIn:
                    zoomValue += 1.0
                    AccessibilityNotification.Announcement(zoomQuantity).post()
                case .zoomOut:
                    zoomValue -= 1.0
                    AccessibilityNotification.Announcement(zoomQuantity).post()
                }
            }
    }
}
```

### Add the accessibility zoom action with UIKit — [7:18]

```swift
import UIKit

class ViewController: UIViewController {
    let zoomView = ZoomingImageView(frame: .zero)
    let imageView = UIImageView(image: UIImage(named: "tree"))

    override func viewDidLoad() {
        super.viewDidLoad()
        zoomView.isAccessibilityElement = true
        zoomView.accessibilityLabel = "Zooming Image View"
        zoomView.accessibilityTraits = [.image, .supportsZoom]

        zoomView.addSubview(imageView)
        view.addSubview(zoomView)
    }
}
```

### Respond to accessibility zoom actions with UIKit — [7:43]

```swift
import UIKit 

class ZoomingImageView: UIScrollView {
    override func accessibilityZoomIn(at point: CGPoint) -> Bool {
        zoomScale += 1.0

        let zoomQuantity = "\(Int(zoomValue)) x zoom"  
        UIAccessibility.post(notification: .announcement, argument: zoomQuantity)
        return true
    }

    override func accessibilityZoomOut(at point: CGPoint) -> Bool {
        zoomScale -= 1.0

        let zoomQuantity = "\(Int(zoomValue)) x zoom" 
        UIAccessibility.post(notification: .announcement, argument: zoomQuantity)             
        return true
    }
}
```

### Use accessibility direct touch options — [10:10]

```swift
import SwiftUI

struct KeyboardKeyView: View {
    var soundFile: String
    var body: some View {
        Rectangle()
            .fill(.white)
            .frame(width: 35, height: 80)
            .onTapGesture(count: 1) {
                playSound(sound: soundFile, type: "mp3")
            }            
            .accessibilityDirectTouch(options: .silentOnTouch)
    }
}
```

### Use accessibility direct touch options with UIKit — [10:46]

```swift
import UIKit

class ViewController: UIViewController {
    let waveformButton = UIButton(type: .custom)

    override func viewDidLoad() {
        super.viewDidLoad()

        waveformButton.accessibilityTraits = .allowsDirectInteraction
        waveformButton.accessibilityDirectTouchOptions = .silentOnTouch
        waveformButton.addTarget(self, action: #selector(playTone), for: .touchUpInside)

        view.addSubview(waveformButton)
    }
}
```

### Set the accessibility content shape — [12:21]

```swift
import SwiftUI

struct ImageView: View {
    var body: some View {
        Image("circle-red")
            .resizable()
            .frame(width: 200, height: 200)
            .accessibilityLabel("Red")
            .contentShape(.accessibility, Circle())
    }
}
```

### Update accessibility values using block-based setters with UIKit — [13:35]

```swift
import UIKit 

class ViewController: UIViewController {
    var isFiltered = false

    override func viewDidLoad() {
        super.viewDidLoad()
        // Set up views
        zoomView.accessibilityValueBlock = { [weak self] in
            guard let self else { return nil }
            return isFiltered ? "Filtered" : "Not Filtered"
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10036/4/BB960BFD-F982-4800-8060-5674B049AC5A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10036/4/BB960BFD-F982-4800-8060-5674B049AC5A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10036) — developer.apple.com. Indexed for agent consumption._
