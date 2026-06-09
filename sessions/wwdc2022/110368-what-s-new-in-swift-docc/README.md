---
id: "wwdc2022-110368"
event: "wwdc2022"
year: 2022
title: "What's new in Swift-DocC"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110368"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in Swift-DocC

**Event:** WWDC22 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110368](https://developer.apple.com/videos/play/wwdc2022/110368)

Join us for an exciting update on Swift-DocC and learn how you can write and share documentation for your own projects. We'll explore improvements to Swift-DocC navigation and share how you can compile documentation for application targets and Objective-C code. We'll also show you how to publish your content straight to hosting services like GitHub Pages.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,666 words)

## Documentation & Resources

- [Documenting apps, frameworks, and packages](https://developer.apple.com/documentation/Xcode/documenting-apps-frameworks-and-packages) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/documenting-apps-frameworks-and-packages
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/documenting-apps-frameworks-and-packages.json
- [SwiftDocCPlugin](https://apple.github.io/swift-docc-plugin/documentation/swiftdoccplugin/) _documentation_
- [DocC](https://developer.apple.com/documentation/docc) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [SlothCreator: Building DocC documentation in Xcode](https://developer.apple.com/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode.json

## Code Snippets

### Documenting the SlothView struct — [3:21]

```swift
/// A view that displays a sloth.
///
/// This is the main view of ``SlothyApp``.
/// Create a sloth view by providing a binding to a sloth.
///
/// ```swift
/// @State private var sloth: Sloth
///
/// var body: some View {
///     SlothView(sloth: $sloth)
/// }
/// ```
struct SlothView: View {
    // ...
}
```

### Documenting an initializer — [4:25]

```swift
struct SlothView: View {
    /// Creates a view that displays the specified sloth.
    ///
    /// - Parameter sloth: The sloth the user will edit.
    init(sloth: Binding<Sloth>) {
				// ...
    }
}
```

### Documenting the SLOSound Objective-C class — [5:24]

```objectivec
/// A sound that can be played.
///
/// Use an instance of this type to play a sound
/// to the user in response to an action or
/// event.
@interface SLOSound : NSObject

/// Creates a sound given its name and path on
/// disk.
///
/// - Parameters:
///   - name: The name of the sound.
///   - filePath: The path to the sound file on disk.
- (id)initWithName:(NSString *)name
          filePath:(NSString *)filePath;

@end
```

### Documenting the top-level page for the Slothy app — [6:48]

```markdown
# ``Slothy``

An app to create and care for custom sloths.

## Overview

Slothy is an iOS app that allows users to create and care for virtual sloths.

![An illustration displaying the UI for finding, creating, and taking care of a sloth in Slothy.](slothy.png)

The Slothy app project contains views to present Slothy's user interface, and utilities to play sounds as the user interacts with the app.
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110368/6/40936E45-C4DD-4831-B7B9-146B53027E76/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110368/6/40936E45-C4DD-4831-B7B9-146B53027E76/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110368) — developer.apple.com. Indexed for agent consumption._
