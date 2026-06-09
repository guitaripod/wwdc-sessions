---
id: "wwdc2020-10207"
event: "wwdc2020"
year: 2020
title: "SF Symbols 2"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10207"
topics: ["SwiftUI & UI Frameworks", "Design"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# SF Symbols 2

**Event:** WWDC20 · **Topic:** Design · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10207](https://developer.apple.com/videos/play/wwdc2020/10207)

SF Symbols make it easy to adopt high-quality, Apple-designed symbols created to look great with San Francisco, the system font for all Apple platforms. Discover how you can use SF Symbols in AppKit, UIKit, and SwiftUI. Learn how to work with SF Symbols in common design tools and how to use them in code. And we’ll walk you through the latest updates, including additions to the repertoire, alignment improvements, changes with right-to-left localization, and multicolor symbols.

This session focuses on the latest features in SF Symbols 2. While not required, we recommend watching "Introducing SF Symbols" from WWDC19. If you’re planning to incorporate symbol assets into SwiftUI, you may also benefit from watching “Building Custom Views with SwiftUI."

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,964 words)

## Code Snippets

### Symbol usage demo, part 1 — [5:29]

```swift
// SF Symbols: simple usage and symbol configuration

import UIKit

class MainPlayerViewController: UIViewController {

    @IBOutlet weak var playButton: UIButton!
    @IBOutlet weak var shuffleButton: UIButton!
    @IBOutlet weak var playImageView: UIImageView!
    @IBOutlet weak var shuffleImageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupButtons()
    }

    func setupButtons() {
        playImageView.image = UIImage(systemName: "")
        shuffleImageView.image = UIImage(systemName: "")
    }

    @IBAction func playAction(_ sender: Any) {
    }

    @IBAction func shuffleAction(_ sender: Any) {
    }

}
```

### Symbol usage demo, wrong string to initializer — [6:07]

```swift
// do NOT use symbol characters in code

let shuffleImage = UIImage(systemName: "􀊝")






// always use symbol names in code

let shuffleImage = UIImage(systemName: "shuffle")
```

### Symbol usage demo, scales — [7:01]

```swift
// SF Symbols: simple usage and symbol configuration

import UIKit

class MainPlayerViewController: UIViewController {

    @IBOutlet weak var playButton: UIButton!
    @IBOutlet weak var shuffleButton: UIButton!
    @IBOutlet weak var playImageView: UIImageView!
    @IBOutlet weak var shuffleImageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupButtons()
    }

    func setupButtons() {
        let buttonConfig = UIImage.SymbolConfiguration(scale: .small)
        playImageView.preferredSymbolConfiguration = buttonConfig
        playImageView.image = UIImage(systemName: "play.fill")
        shuffleImageView.preferredSymbolConfiguration = buttonConfig
        shuffleImageView.image = UIImage(systemName: "shuffle")
    }

    @IBAction func playAction(_ sender: Any) {
    }

    @IBAction func shuffleAction(_ sender: Any) {
    }

}
```

### Symbol usage demo, textStyles — [7:13]

```swift
// SF Symbols: simple usage and symbol configuration

import UIKit

class MainPlayerViewController: UIViewController {

    @IBOutlet weak var playButton: UIButton!
    @IBOutlet weak var shuffleButton: UIButton!
    @IBOutlet weak var playImageView: UIImageView!
    @IBOutlet weak var shuffleImageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        setupButtons()
    }

    func setupButtons() {
        let buttonConfig = UIImage.SymbolConfiguration(textStyle: .headline, scale: .small)
        playImageView.preferredSymbolConfiguration = buttonConfig
        playImageView.image = UIImage(systemName: "play.fill")
        shuffleImageView.preferredSymbolConfiguration = buttonConfig
        shuffleImageView.image = UIImage(systemName: "shuffle")
    }

    @IBAction func playAction(_ sender: Any) {
    }

    @IBAction func shuffleAction(_ sender: Any) {
    }

}
```

### SwiftUI symbol usage — [7:44]

```swift
// SF Symbols in SwiftUI
import SwiftUI

struct ContentView: View {
    var body: some View {
        Image(systemName: "shuffle")
            .font(.headline)
            .imageScale(.small)
    }
}
```

### SF Symbols in SwiftUI (Label) — [8:10]

```swift
// SF Symbols in SwiftUI
import SwiftUI

struct ContentView: View {
    var body: some View {
        Label("Sharing location", 
              systemImage: "location.fill")
    }
}
```

### SF Symbols in SwiftUI (Text + Image) — [8:12]

```swift
// SF Symbols in SwiftUI
import SwiftUI

struct ContentView: View {
    var body: some View {
        let glyph = Image(systemName: "location.fill")
        return Text("\(glyph) Sharing location")
    }
}
```

### Using SF Symbols in AppKit — [8:52]

```swift
// Using SF Symbols in AppKit

if let shuffleImage = NSImage(
    systemSymbolName: "shuffle", accessibilityDescription: "shuffle") {
    shuffleImageView.image = shuffleImage

    // Configure symbols
    let config = NSImage.SymbolConfiguration(textStyle: .body, scale: .small)
    let shuffleButtonImage = shuffleImage.withSymbolConfiguration(config)
}
```

### Symbol initializer for old and new templates — [11:45]

```swift
// loading symbols from Template V1 and V2

let shuffleImage = UIImage(systemName: "shuffle")
```

### Tinting symbols in AppKit — [15:44]

```swift
// Tinting symbols

if let folder = NSImage(
    systemSymbolName: "folder.badge.plus", accessibilityDescription: "add folder") {
    folder.isTemplate = true
}

if let folder = NSImage(
    systemSymbolName: "folder.badge.plus", accessibilityDescription: "add folder") {
    folder.isTemplate = false
}
```

### Using symbols in AppKit, recap — [18:10]

```swift
// Using SF Symbols in AppKit

if let shuffleImage = NSImage(
    systemSymbolName: "shuffle", accessibilityDescription: "shuffle") {
    shuffleImageView.image = shuffleImage

    // Configure symbols
    let config = NSImage.SymbolConfiguration(textStyle: .body, scale: .small)
    let shuffleButtonImage = shuffleImage.withSymbolConfiguration(config)
}
```

### Using color symbols recap — [18:24]

```swift
// Tinting symbols

folder.isTemplate = true

folder.isTemplate = false
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10207/4/56001BC4-A5FE-4734-A5EB-377771B6FED3/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10207) — developer.apple.com. Indexed for agent consumption._