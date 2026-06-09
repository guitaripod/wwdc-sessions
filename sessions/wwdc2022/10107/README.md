---
id: "wwdc2022-10107"
event: "wwdc2022"
year: 2022
title: "Get it right (to left)"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10107"
topics: ["Accessibility & Inclusion", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Get it right (to left)

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10107](https://developer.apple.com/videos/play/wwdc2022/10107)

Discover how to develop your app so that it can be localized into "right-to-left" languages such as Arabic and Hebrew. We'll take you through important considerations for these languages, share solutions to challenges, and provide best practices for delivering a great right-to-left experience in your app.

**Keywords:** `alignment`, `arabic`, `hebrew`, `i10n`, `internationalization`, `l18n`, `localization`, `ltr`, `pseudolanguage`, `rtl`, `sf symbols`, `writing direction`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,704 words)

## Documentation & Resources

- [Localization](https://developer.apple.com/documentation/Xcode/localization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localization.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/
- [Internationalization and Localization Guide](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html

## Code Snippets

### Control orientation example — [12:55]

```swift
struct ContentView: View {
    var body: some View {
    VStack(alignment: .leading) {
        Button(action: {}) {
            Label("Preview", systemImage: "arrowtriangle.forward.fill")
        }.labelStyle(IconOnRightLabelStyle())

            HStack() {
                Button(action: {}) {
                    Label("Left", systemImage: "arrow.left")
                }.labelStyle(TitleAndIconLabelStyle())

                Button(action: {}) {
                    Label("Right", systemImage: "arrow.right")
                }.labelStyle(IconOnRightLabelStyle())
            }.environment(\.layoutDirection, .leftToRight)
        }.padding()
    }
}
```

### Control orientation custom label style example — [14:22]

```swift
struct IconOnRightLabelStyle : LabelStyle {
    func makeBody(configuration: Configuration) -> some View {
        HStack {
            configuration.title
            configuration.icon
        }
    }
}
```

### Control orientation example — [14:43]

```swift
struct ContentView: View {
    var body: some View {
    VStack(alignment: .leading) {
        Button(action: {}) {
            Label("Preview", systemImage: "arrowtriangle.forward.fill")
        }.labelStyle(IconOnRightLabelStyle())

            HStack() {
                Button(action: {}) {
                    Label("Left", systemImage: "arrow.left")
                }.labelStyle(TitleAndIconLabelStyle())

                Button(action: {}) {
                    Label("Right", systemImage: "arrow.right")
                }.labelStyle(IconOnRightLabelStyle())
            }.environment(\.layoutDirection, .leftToRight)
        }.padding()
    }
}
```

### Control orientation example—keeping controls from reversing — [18:58]

```swift
struct ContentView: View {
    var body: some View {
        VStack(alignment: .leading) {
            Picker(selection: $textStyle, label: Text("Text Style")) {
                Text("B").tag(TextStyle.bold)
                Text("I").tag(TextStyle.italic)
                Text("U").tag(TextStyle.underline)
                Text("S").tag(TextStyle.strikethrough)
            }.pickerStyle(.segmented)

            Picker(selection: $alignment, label: Text("Alignment")) {
                Image(systemName: "text.alignleft").tag(TextAlignment.left)
                Image(systemName: "text.aligncenter").tag(TextAlignment.center)
                Image(systemName: "text.alignright").tag(TextAlignment.right)
           }.pickerStyle(.segmented)
             .environment(\.layoutDirection, .leftToRight)
        }
    }
}
```

### Control orientation example—form with multiline text alignment modifier — [22:38]

```swift
var body: some View {
   Form {
        TextField("Password:", text: $password)
        TextField("Verify:", text: $verifyPassword)
        TextField("Password Hint:\n(Recommended)", text: $passwordHint)
            .multilineTextAlignment(.trailing)
    }.padding()
}
```

### Set up Auto Layout in code — [27:14]

```swift
myView.leadingAnchor.constraint(equalTo: mySuperView.leadingAnchor, constant:16)
```

### Digits in Arabic — [29:05]

```swift
myLabel.string = String(localized: "There are \(peopleInChat) people in this chat.",
                        comment: "Label indicating number of chat participants")

Text("There are \(peopleInChat) people in this chat.",
     comment: "Label indicating number of chat participants")
```

### Digits in Arabic — [30:12]

```swift
myLabel.string = String(localized: "This application supports \(3) file formats.",
comment: "Label showing number of supported file formats
(number is always 3)")
```

### Numbers in RTL text — [31:41]

```swift
myLabel.stringValue = String(localized: "\(percentComplete.formatted(.percent)) complete")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10107/3/85B12DD5-27C3-420C-97F8-4C71326BB3D0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10107/3/85B12DD5-27C3-420C-97F8-4C71326BB3D0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10107) — developer.apple.com. Indexed for agent consumption._