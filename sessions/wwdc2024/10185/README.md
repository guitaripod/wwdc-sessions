---
id: "wwdc2024-10185"
event: "wwdc2024"
year: 2024
title: "Build multilingual-ready apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10185"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Build multilingual-ready apps

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10185](https://developer.apple.com/videos/play/wwdc2024/10185)

Ensure your app works properly and effectively for multilingual users. Learn best practices for text input, display, search, and formatting. Get details on typing in multiple languages without switching between keyboards. And find out how the latest advances in the String Catalog can make localization even easier.

**Keywords:** `🌍`, `🌎`, `🌏`, `automatic grammar agreement`, `formatter`, `hindi`, `i10n`, `keyboard layout guide`, `l18n`, `nstextview`, `sf symbols`, `stringsdict`, `textkit`, `uitextview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,698 words)

## Documentation & Resources

- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### Specify textInputContextIdentifier — [3:18]

```swift
override var textInputContextIdentifier: String? {
    uniqueID
}
```

### Place a view directly above the keyboard — [3:41]

```swift
textView.inputAccessoryView = viewAboveKeyboard
```

### Use keyboardLayoutGuide to adapt to keyboard — [4:00]

```swift
view.keyboardLayoutGuide.topAnchor.constraint(equalToSystemSpacingBelow: textView.bottomAnchor, multiplier: 1.0).isActive = true
```

### Check for marked text before modifying — [4:42]

```swift
if textView.markedTextRange.empty {
    // Perform actions involving editing text
}
```

### Use localizedStandardRange when searching — [5:58]

```swift
let range = text.localizedStandardRange(of: search)
```

### Use color differences to highlight text — [7:24]

```swift
attributedString[range].foregroundColor = highlightColor
```

### Text Styles — [9:39]

```swift
// Text Styles

// SwiftUI
Text("Hello, world!") // uses .body Text Style by default
Text("Hello, world!").font(.title)

// UIKit
let label = UILabel()
label.text = "Hello, world!"
label.font = UIFont.preferredFont(forTextStyle: .body)

// AppKit
let textField = NSTextField(labelWithString: "Hello, world!")
textField.font = NSFont.preferredFont(forTextStyle: .body)

// Keep clipsToBounds off
clipsToBounds = false
```

### Typesetting language — [10:03]

```swift
// Typesetting language

// SwiftUI
Text(verbatim: "Hello, world!").typesettingLanguage(.init(languageCode: .english))

// UIKit
let label = UILabel()
label.text = "Hello, world!"
label.traitOverrides.typesettingLanguage = Locale.Language(languageCode: .english)
```

### Formatting names — [10:29]

```swift
// Formatting names

let nameComponents = PersonNameComponents
  (givenName: "瑗珺", familyName: "汪", nickname: "珺珺")

// Short Name (respects settings like “Prefer Nicknames”)
let shortName =   nameComponents.formatted(.name(style: .short)) // 珺珺

// Abbreviated Name (can be used for monograms)
let monogram =   nameComponents.formatted(.name(style: .abbreviated)) // 汪
```

### Examples of personalizing text — [12:20]

```markdown
"^[Nuestro %@](inflect: true) está ^[hecho](agreeWithArgument: 1) de %@."
"अगर आप पहुँच नहीं ^[पाते हैं](inflect: true)"
"예: ‘^[%@을](inflect: true) 켤 때’"
```

### Format numbers using Text — [13:43]

```swift
Text("\(numberOfDays)-day forecast")
```

### Format numbers using AttributedString — [14:21]

```swift
AttributedString(localized: "10-day forecast")
AttributedString(localized: "0.5× zoom")
```

### Launch to your app’s settings — [15:23]

```swift
// Launch to your app’s settings
if let url =
URL(string: UIApplication.openSettingsURLString) {
   await UIApplication.shared.open(url)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10185/4/B7C5A64E-515C-41CE-A821-E441DE74E0A1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10185/4/B7C5A64E-515C-41CE-A821-E441DE74E0A1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10185) — developer.apple.com. Indexed for agent consumption._