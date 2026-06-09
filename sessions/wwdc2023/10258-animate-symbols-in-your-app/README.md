---
id: "wwdc2023-10258"
event: "wwdc2023"
year: 2023
title: "Animate symbols in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10258"
topics: ["App Services", "Design", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Animate symbols in your app

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10258](https://developer.apple.com/videos/play/wwdc2023/10258)

Bring delight to your app with animated symbols. Explore the new Symbols framework, which features a unified API to create and configure symbol effects. Learn how SwiftUI, AppKit, and UIKit make it easy to animate symbols in user interfaces. Discover tips and tricks to seamlessly integrate the new animations alongside other app content. To get the most from this session, we recommend first watching “What’s new in SF Symbols 5.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,989 words)

## Code Snippets

### Symbol effects in SwiftUI — [6:02]

```swift
// Symbol effects in SwiftUI

Image(systemName: "wifi.router")
    .symbolEffect(.variableColor.iterative.reversing)
    .symbolEffect(.scale.up)
```

### Symbol effects in AppKit and UIKit — [6:02]

```swift
let imageView: NSImageView = ...

imageView.addSymbolEffect(.variableColor.iterative.reversing)
imageView.addSymbolEffect(.scale.up)
```

### Indefinite symbol effects in SwiftUI — [6:49]

```swift
struct ContentView: View {
    @State var isConnectingToInternet: Bool = true

    var body: some View {
        Image(systemName: "wifi.router")
            .symbolEffect(
                .variableColor.iterative.reversing,
                isActive: isConnectingToInternet
            )
    }
}
```

### Indefinite symbol effects in AppKit and UIKit — [7:09]

```swift
let imageView: NSImageView = ...

imageView.addSymbolEffect(.variableColor.iterative.reversing)

// Later, remove the effect
imageView.removeSymbolEffect(ofType: .variableColor)
```

### Discrete symbol effects in SwiftUI — [8:26]

```swift
struct ContentView: View {
    @State var bounceValue: Int = 0

    var body: some View {
        VStack {
            Image(systemName: "antenna.radiowaves.left.and.right")
                .symbolEffect(
                    .bounce,
                    options: .repeat(2),
                    value: bounceValue
                )

            Button("Animate") {
                bounceValue += 1
            }
        }
    }
}
```

### Discrete symbol effects in AppKit and UIKit — [8:26]

```swift
let imageView: NSImageView = ...

// Bounce
imageView.addSymbolEffect(.bounce, options: .repeat(2))
```

### Content transition symbol effects in SwiftUI — [9:40]

```swift
struct ContentView: View {
    @State var isPaused: Bool = false

    var body: some View {
        Button {
            isPaused.toggle()
        } label: {
            Image(systemName: isPaused ? "pause.fill" : "play.fill")
                .contentTransition(.symbolEffect(.replace.offUp))
        }
    }
}
```

### Content transition symbol effects in AppKit and UIKit — [9:57]

```swift
let imageView: UIImageView = ...
imageView.image = UIImage(systemName: "play.fill")

// Change the image with a Replace effect
let pauseImage = UIImage(systemName: "pause.fill")!
imageView.setSymbolImage(pauseImage, contentTransition: .replace.offUp)
```

### Indefinite Appear and Disappear symbol effects in SwiftUI — [11:14]

```swift
struct ContentView: View {
    @State var isMoonHidden: Bool = false

    var body: some View {
        HStack {
            RoundedRectangle(cornerRadius: 5)

            Image(systemName: "moon.stars")
               .symbolEffect(.disappear, isActive: isMoonHidden)

            Circle()
        }
    }
}
```

### Indefinite Appear and Disappear symbol effects in AppKit and UIKit — [11:30]

```swift
let imageView: UIImageView = ...
imageView.image = UIImage(systemName: "moon.stars")

imageView.addSymbolEffect(.disappear)
// Re-appear the symbol
imageView.addSymbolEffect(.appear)
```

### Transition symbol effects in SwiftUI — [12:38]

```swift
struct ContentView: View {
    @State var isMoonHidden: Bool = false

    var body: some View {
        HStack {
            RoundedRectangle(cornerRadius: 5)

            if !isMoonHidden {
                Image(systemName: "moon.stars")
                    .transition(.symbolEffect(.disappear.down))
            }

            Circle()
        }
    }
}
```

### Appear and Disappear symbol effects in UIKit with completion handler — [12:59]

```swift
let imageView: UIImageView = ...
imageView.image = UIImage(systemName: "moon.stars")

imageView.addSymbolEffect(.disappear) { context in
    if let imageView = context.sender as? UIImageView, context.isFinished {
        imageView.removeFromSuperview()
    } 
}
```

### Symbol effect propagation in SwiftUI — [14:19]

```swift
VStack {
    Image(systemName: "figure.walk")
        .symbolEffectsRemoved()
    Image(systemName: "car")
    Image(systemName: "tram")
}
.symbolEffect(.pulse)
```

### Effects without animation in SwiftUI — [14:55]

```swift
struct ContentView: View {
    @State var isScaledUp: Bool = false

    var body: some View {
        Image(systemName: "iphone.radiowaves.left.and.right")
            .symbolEffect(.scale.up, isActive: isScaledUp)
            .onAppear {
                var transaction = Transaction()
                transaction.disablesAnimations = true
                withTransaction(transaction) {
                    isScaledUp = true
                }
            }
    }
}
```

### Effects without animation in AppKit and UIKit — [15:06]

```swift
// Effects without animation in AppKit and UIKit

let imageView: UIImageView = ...
imageView.image = UIImage(systemName: "iphone.radiowaves.left.and.right")

imageView.addSymbolEffect(.disappear, animated: false)
```

### Variable value animations in SwiftUI — [15:44]

```swift
struct ContentView: View {
    @State var signalLevel: Double = 0.5

    var body: some View {
        Image(systemName: "wifi", variableValue: signalLevel)
    }
}
```

### Variable value animations in AppKit and UIKit — [16:07]

```swift
let imageView: UIImageView = ...
imageView.image = UIImage(systemName: "wifi", variableValue: 1.0)

// Animate to a different Wi-Fi level
let currentSignalImage = UIImage(
    systemName: "wifi",
    variableValue: signalLevel
)!
imageView.setSymbolImage(currentSignalImage, contentTransition: .automatic)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10258/4/F5972AFA-C206-4702-9005-E146CE71FC29/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10258/4/F5972AFA-C206-4702-9005-E146CE71FC29/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10258) — developer.apple.com. Indexed for agent consumption._
