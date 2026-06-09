---
id: "wwdc2021-10191"
event: "wwdc2021"
year: 2021
title: "Deliver a great playback experience on tvOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10191"
topics: ["SwiftUI & UI Frameworks", "Audio & Video"]
platforms: ["tvOS"]
hasTranscript: true
---

# Deliver a great playback experience on tvOS

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10191](https://developer.apple.com/videos/play/wwdc2021/10191)

Find out how you can use Apple TV’s redesigned playback interface to build great media experiences in your apps. Learn how the latest interface helps people access relevant controls and information while maintaining focus on content. We’ll show you how you can adopt AVPlayerViewController and other APIs for your tvOS app to help people find, play, and enjoy content.

To get the most out of this session, we recommend having a basic understanding of AVKit.

**Keywords:** `avplayerviewcontroller`, `content tabs`, `contextual actions`, `title view`, `transport bar`, `transport bar controls`, `tvuikit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,369 words)

## Documentation & Resources

- [Customizing the tvOS Playback Experience](https://developer.apple.com/documentation/AVKit/customizing-the-tvos-playback-experience) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit/customizing-the-tvos-playback-experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit/customizing-the-tvos-playback-experience.json
- [AVKit](https://developer.apple.com/documentation/AVKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVKit.json
- [Human Interface Guidelines: Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-tvos

## Code Snippets

### Transport Bar Controls Example — [4:42]

```swift
let favoriteAction = UIAction(title: "Favorites", image: UIImage(systemName: "heart")) {
    // Add to favorites
}

let submenu = UIMenu(title: "Speed", options: [.displayInline, .singleSelection],
                     children: [ UIAction(…) ])

let menu = UIMenu(image: UIImage(systemName: "gearshape"), children: [submenu, UIAction(…)])
playerViewController.transportBarCustomMenuItems = [favoriteAction, menu]
```

### Content Tabs Example — [6:11]

```swift
// Initialize content tab view controller

customViewController.preferredContentSize = CGSize(width: 0, height: 140)
customViewController.title = "Recommended"
```

### TVMediaItemContentConfiguration Example — [7:08]

```swift
// Configure 16:9 UICollectionView cell
import TVUIKit

var contentConfiguration = TVMediaItemContentConfiguration.wideCell()
contentConfiguration.image = UIImage(imageLiteralResourceName: "tanu")
contentConfiguration.text = "Title"
contentConfiguration.secondaryText = "Secondary text"
contentConfiguration.badgeText = "NEW"
contentConfiguration.badgeProperties.backgroundColor = .systemRed
contentConfiguration.playbackProgress = 0.75

cell.contentConfiguration = contentConfiguration
```

### TVMonogramContentConfiguration Example — [7:36]

```swift
// Configure monogram UICollectionView cell
import TVUIKit

var contentConfiguration = TVMonogramContentConfiguration.cell()
contentConfiguration.image = UIImage(imageLiteralResourceName: "jad")
contentConfiguration.text = "Jad"

cell.contentConfiguration = contentConfiguration
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10191/4/E98B040E-0A40-48C3-85D2-F7F18715F00F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10191/4/E98B040E-0A40-48C3-85D2-F7F18715F00F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10191) — developer.apple.com. Indexed for agent consumption._