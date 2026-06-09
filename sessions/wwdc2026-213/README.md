# Translate your app using agents in Xcode

**Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-213](https://developer.apple.com/videos/play/wwdc2026/213)

Find out how Xcode and coding agents help you translate String Catalogs using the context of your app. We’ll walk through strategies for reviewing translated output and iterating on your localizations, so you can deliver a tailored experience to people around the world.

**Keywords:** `🍁`, `l10n`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Localizing your app using agents](https://developer.apple.com/documentation/Xcode/localizing-your-app-using-agents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localizing-your-app-using-agents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localizing-your-app-using-agents.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### Localizing strings in SwiftUI — [3:02]

```swift
// Localizing strings in SwiftUI

Text("Hello, world!", comment: "A standard greeting")
```

### Localizing strings in SwiftUI with custom table name — [3:11]

```swift
// Localizing strings in SwiftUI with custom table name

Text("Hello, world!", tableName: "Greetings", comment: "A standard greeting")
```

### Localizing strings in SwiftUI — [11:21]

```swift
// Localizing strings in SwiftUI

Text("Hello, world!", comment: "A standard greeting")
```

### Localizing strings elsewhere — [11:25]

```swift
// Localizing strings elsewhere

String(localized: "Hello, world!", comment: "A standard greeting")

LocalizedStringResource("Hello World!", bundle: #bundle, comment: "A standard greeting")
```

### Field for machine-translated strings in the XLIFF — [13:39]

```xml
// Field for machine-translated strings in the XLIFF

<trans-unit id="Grand Canyon" xml:space="preserve">
  <source>Grand Canyon</source>
  <target state="translated" state-qualifier="leveraged-mt">Grand Canyon</target>
  <note>Name of the ‘Grand Canyon’ landmark.</note>
</trans-unit>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/213/4/be1ee662-a447-4df4-89a5-5411447c0eeb/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/213/4/be1ee662-a447-4df4-89a5-5411447c0eeb/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._