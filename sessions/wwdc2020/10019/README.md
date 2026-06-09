---
id: "wwdc2020-10019"
event: "wwdc2020"
year: 2020
title: "App accessibility for Switch Control"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10019"
topics: ["Design", "SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# App accessibility for Switch Control

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10019](https://developer.apple.com/videos/play/wwdc2020/10019)

Switch Control is a powerful accessibility technology for anyone with very limited mobility. The feature is available natively on iOS, and you can create an even better Switch Control experience in your app with tips, tricks, and a few APIs. We’ll walk you through how people use Switch Control, as well as provide best practices for supporting it in your app effectively. 

To get the most out of this session, you should be familiar with general accessibility principles and VoiceOver accessibility APIs. Check out "Making Apps More Accessible With Custom Actions," "Writing Great Accessibility Labels, and "VoiceOver: App Testing Beyond The Visuals" for more information.

**Keywords:** `accessibility`, `assistive technology`, `custom actions`, `isswitchcontrolrunning`, `motor impairment`, `switch control`, `switches`, `uiaccessibilitycustomaction`, `voiceover`, `voice over`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,303 words)

## Documentation & Resources

- [Accessibility for UIKit](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/accessibility-for-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/accessibility-for-uikit.json

## Code Snippets

### Navigation Style and Element Ordering — [7:53]

```swift
containerView.accessibilityNavigationStyle = .combined

containerView.accessibilityElements = [ levelFourView, levelFiveView, levelSixView]
```

### Follow Focus API — [8:47]

```swift
// Following Focus API 

class CardView : UIView { 
    var orientation: CardOrientation

    enum CardOrientation {
        case front
        case back
    }

    override func accessibilityElementDidBecomeFocused() {
        self.flip(to: .front)
    } 

		override func accessibilityElementDidLoseFocus() {
        self.flip(to: .back)
    }

// The rest of the class…
}
```

### Custom Actions API — [9:56]

```swift
// Custom Actions API (VoiceOver uses this too)

func configureActions() {

  let pinAction = UIAccessibilityCustomAction(
      name: "Pin Card") { (_) -> Bool in
          self.setPinned(true)
          return true
      }
  pinAction.image = UIImage(systemName: "pin")

  let addAction = UIAccessibilityCustomAction(
      name: "Add Card") { (_) -> Bool in
          self.setSelected(true)
          return true
      }
    addAction.image = UIImage(systemName: "add.square")


	self.accessibilityCustomActions = [addAction, pinAction]
}
```

### Other Useful API — [11:51]

```swift
static var isSwitchControlRunning: Bool { get }

var accessibilityRespondsToUserInteraction: Bool { get set }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10019/8/B498FE5F-E963-44CB-BE5E-1053289B5D7B/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10019) — developer.apple.com. Indexed for agent consumption._