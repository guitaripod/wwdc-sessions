---
id: "wwdc2020-10175"
event: "wwdc2020"
year: 2020
title: "The details of UI typography"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10175"
topics: ["Design"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# The details of UI typography

**Event:** WWDC20 · **Topic:** Design · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10175](https://developer.apple.com/videos/play/wwdc2020/10175)

Learn how to achieve exceptional typography in your app’s user interface that enhances legibility, accessibility, and consistency across Apple platforms. Get up to speed on the latest advancements to the San Francisco font family including the move to variable fonts for accommodating optical sizes and weights. We’ll also share tips about how to get the most out of systems fonts, support dynamic type with custom fonts.

For a refresher on the principles behind the San Francisco font family, catch up on “Introducing the New System Fonts” from WWDC15.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,131 words)

## Documentation & Resources

- [Human Interface Guidelines: Typography](https://developer.apple.com/design/human-interface-guidelines/typography) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/typography
- [Building Apps with Dynamic Type](https://developer.apple.com/sample-code/wwdc/2017/Building-Apps-with-Dynamic-Type.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/wwdc/2017/Building-Apps-with-Dynamic-Type.zip

## Code Snippets

### Setting custom tracking — [12:19]

```swift
// UIKit
label.attributedText =
    NSAttributedString(string: "hamburgefonstiv",
        attributes: [kCTTrackingAttributeName as NSAttributedString.Key: -0.5])

// SwiftUI
Text("hamburgefonstiv").tracking(-0.5)
```

### Allow tightening to use tight tracking from system fonts — [12:45]

```swift
// UIKit: UILabel
label.allowsDefaultTighteningForTruncation = true

// AppKit: NSTextField
textField.allowsDefaultTighteningForTruncation = true

// SwiftUI
Text("hamburgefonstiv").allowsTightening(true)
```

### Getting emphasized text styles — [17:45]

```swift
// Getting emphasized text styles

let label = UILabel()
label.text = "Ready. Set. Code."

if let descriptor = UIFontDescriptor
    .preferredFontDescriptor(withTextStyle: .title1)
    .withSymbolicTraits(.traitBold) {
    // 28 pt Bold on iOS
    label.font = .init(descriptor: descriptor, size: 0)
}
```

### Getting emphasized text styles APIs — [18:05]

```swift
// Getting emphasized text styles

// AppKit
let descriptor = NSFontDescriptor
    .preferredFontDescriptor(forTextStyle: .body)
    .withSymbolicTraits(.bold)
// 13 pt Semibold on macOS
let emphasizedBodyFont = NSFont(descriptor: descriptor, size: 0)

// UIKit/Catalyst
if let descriptor = UIFontDescriptor
    .preferredFontDescriptor(withTextStyle: .body)
    .withSymbolicTraits(.traitBold) {
    // 17 pt Semibold on iOS
    let emphasizedBodyFont = UIFont(descriptor: descriptor, size: 0)
}

// SwiftUI
let emphasizedFootnoteFont = Font.footnote.bold() // 13 pt Semibold on iOS
```

### Getting tight leading variant — [19:34]

```swift
// Getting tight leading variant
import UIKit

let label = UILabel()
label.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

if let descriptor = UIFontDescriptor
    .preferredFontDescriptor(withTextStyle: .body)
    .withSymbolicTraits(.traitTightLeading)
    // 20 pt line height
    label.font = UIFont(descriptor: descriptor, size: 0)
}
```

### Getting loose leading variant — [19:49]

```swift
// Getting tight leading variant
import UIKit

let label = UILabel()
label.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

if let descriptor = UIFontDescriptor
    .preferredFontDescriptor(withTextStyle: .body)
    .withSymbolicTraits(.traitLooseLeading)
    // 24 pt line height
    label.font = UIFont(descriptor: descriptor, size: 0)
}
```

### Getting tight/loose leading variant APIs — [20:03]

```swift
// Getting tight/loose leading variant

// AppKit
let descriptor = NSFontDescriptor.preferredFontDescriptor(forTextStyle: .headline)
    .withSymbolicTraits(.tightLeading) // Use .looseLeading for loose leading font
let tightLeadingFont = NSFont(descriptor: descriptor, size: 0) // 14 pt line height

// UIKit/Catalyst
if let descriptor = UIFontDescriptor.preferredFontDescriptor(withTextStyle: .title1)
    .withSymbolicTraits(.traitTightLeading) { // Use .traitLooseLeading for loose leading
    let tightLeadingFont = UIFont(descriptor: descriptor, size: 0) // 36 pt line height
}

// SwiftUI
// Use .loose for loose leading font
let tightLeadingFootnoteFont = Font.footnote.leading(.tight) // 16 pt line height on iOS
```

### Access rounded system font design — [20:56]

```swift
// Access rounded system font design
import UIKit

let label = UILabel()
label.text = "Today"

if let descriptor = UIFontDescriptor
    .preferredFontDescriptor(withTextStyle: .largeTitle)
    .withSymbolicTraits(.traitBold)?
    .withDesign(.rounded) {
    // SF Pro Rounded Bold
    label.font = UIFont(descriptor: descriptor, size: 0)
}
```

### Access system font designs — [21:08]

```swift
// Access system font designs

// Use .serif for New York, .monospaced for SF Mono

// AppKit
let descriptor = NSFontDescriptor.preferredFontDescriptor(forTextStyle: .body)
    .withDesign(.rounded)
let roundedBodyFont = NSFont(descriptor: descriptor, size: 0) // SF Pro Rounded

// UIKit/Catalyst
if let descriptor = UIFontDescriptor.preferredFontDescriptor(withTextStyle: .body)
    .withDesign(.rounded) {
    let roundedBodyFont = UIFont(descriptor: descriptor, size: 0) // SF Pro Rounded
}

// SwiftUI
let roundedBodyFont = Font.system(.body, design: .rounded) // SF Pro Rounded
```

### Support Dynamic Type with custom font in UIKit — [25:05]

```swift
// Support Dynamic Type with custom font in UIKit

if let customFont = UIFont(name: "Charter-Roman", size: 17) {
    let bodyMetrics = UIFontMetrics(forTextStyle: .body)

    // Charter-Roman scaled relative to body text style
    // in different content size categories.
    let customFontScaledLikeBody = bodyMetrics.scaledFont(for: customFont)
    label.font = customFontScaledLikeBody
    label.adjustsFontForContentSizeCategory = true

    // Scaling constant 10 relative to body text style.
    let scaledValue = bodyMetrics.scaledValue(for: 10)
}
```

### Support Dynamic Type with custom fonts in SwiftUI example — [26:25]

```swift
struct ContentView: View {
    let prose = "Apple provides two type families you can use in your iOS apps. San Francisco (SF). San Francisco is a sans serif type family that includes SF Pro, SF Pro Rounded, SF Mono, SF Compact, and SF Compact Rounded."
    @ScaledMetric(relativeTo: .body) var padding: CGFloat = 20

    var body: some View {
        VStack {
            Text("Typography")
                .font(.custom("Avenir-Medium", size: 34, relativeTo: .title))
            Text(prose)
                .font(.custom("Charter-Roman", size: 17))
                .padding(padding)
        }
    }
}
```

### Support Dynamic Type with custom fonts in SwiftUI — [28:29]

```swift
// Support Dynamic Type with custom fonts in SwiftUI

// Text with font Avenir-Roman, scaling relative to title text style.
Text("Typography").font(.custom("Avenir-Roman", size: 34, relativeTo: .title))

// Text with font Helvetica, scaling relative to body text style.
Text("Title").font(.custom("Helvetica", size: 17))

// Text with font Courier, always use fixed size, do not scale according to user setting.
Text("Fixed").font(.custom("Courier", fixedSize: 17))

// Constant 10, scaled relative to title text style.
@ScaledMetric(relativeTo: .title) private var spacing: CGFloat = 10.0
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10175/3/250D121A-0E77-44A1-AF27-373B9AF669EA/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10175) — developer.apple.com. Indexed for agent consumption._