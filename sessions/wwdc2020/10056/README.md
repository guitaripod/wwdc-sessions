---
id: "wwdc2020-10056"
event: "wwdc2020"
year: 2020
title: "Optimize the interface of your Mac Catalyst app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10056"
topics: ["Developer Tools", "SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Optimize the interface of your Mac Catalyst app

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10056](https://developer.apple.com/videos/play/wwdc2020/10056)

Discover how to tailor your Mac Catalyst app so that it looks and feels even more at home on the Mac by using the new “Optimize Interface for Mac” option in Xcode. Explore new layout and appearance options for Catalyst apps, and learn how they can provide you with graphical performance gains, sharper text, and an interface designed specifically for Apple’s desktops and laptops. We’ll show you how to take advantage of these options and provide best practices for organizing your code when developing for multiple platforms.

Developers actively working on a Mac Catalyst project will get the most out of watching this session. If you’re new to Catalyst, we recommend watching “Designing iPad Apps for Mac” and "Introducing iPad Apps for Mac" for an introduction.

For more on working with Mac Catalyst, check out "What's new in Mac Catalyst”

**Keywords:** `button placement`, `catalyst`, `controls`, `custom artwork`, `font sizes`, `gestures`, `groupbox`, `idiom chooser`, `ipad apps on the mac`, `layouts`, `mac idiom`, `navigation bar`, `optimize`, `optimize interface for mac`, `scaled`, `swiftui`, `toolbar`, `uigesturerecognizer`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,904 words)

## Documentation & Resources

- [Human Interface Guidelines: Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/mac-catalyst
- [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/mac-catalyst
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/mac-catalyst.json
- [Optimizing your iPad app for Mac](https://developer.apple.com/documentation/UIKit/optimizing-your-ipad-app-for-mac) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/optimizing-your-ipad-app-for-mac
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/optimizing-your-ipad-app-for-mac.json
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.json

## Code Snippets

### Hide Navigation Bar in Mac Idiom — [22:04]

```swift
if traitCollection.userInterfaceIdiom == .mac {
    navigationController?.setNavigationBarHidden(true, animated: false)
}
```

### Idiom vs conditional compilation block — [29:33]

```swift
// Idiom vs conditional compilation block

if traitCollection.userInterfaceIdiom == .mac {
    // "Optimize Interface for Mac" specific code
}


#if targetEnvironment(macCatalyst)
    // Mac Catalyst specific code
#endif


if traitCollection.userInterfaceIdiom == .mac {
    // "Optimize Interface for Mac" specific code
} else if traitCollection.userInterfaceIdiom == .pad {
    #if targetEnvironment(macCatalyst)
        // Mac Catalyst specific code
    #else
        // iPad specific code
    #endif
}
```

### SwiftUI GroupBox — [31:26]

```swift
// Nested GroupBoxes

struct ContentView: View {
    var body: some View {
        GroupBox {
            VStack {
                Text("High level information")
                GroupBox {
                    Text("Some elaborate details")
                }
            }
        }
    }
}
```

### SwiftUI Toggle — [32:00]

```swift
// DefaultToggleStyle

struct ContentView: View {
    @State var completed: Bool = false

    var body: some View {
        Toggle("Complete?", isOn: $completed)
    }
}
```

### SwiftUI Button — [32:35]

```swift
// System Button with SF Symbol

struct ContentView: View {
    var body: some View {
        Button(action: { }, label: {
            HStack {
                Image(systemName: "rays")
                Text("Click Me!")
            }
        })
    }
}
```

### SwiftUI DatePicker — [32:56]

```swift
// DefaultDatePickerStyle

struct ContentView: View {
    @State var dueDate = Date()

    var body: some View {
        DatePicker("Due:", selection: $dueDate)
    }
}
```

### SwiftUI Picker — [33:14]

```swift
// DefaultPickerStyle

struct ContentView: View {
    @State var sizeIndex = 2

    var body: some View {
        Picker("Size:", selection: $sizeIndex) {
            Text("Small").tag(1)
            Text("Medium").tag(2)
            Text("Large").tag(3)
        }
    }
}
```

### SwiftUI Nineties Style Button — [33:55]

```swift
// Custom gradient button

struct CustomNinetiesButtonStyle: ButtonStyle {
    var angle: Angle = .degrees(54.95)

    func gradient(shifted: Bool) -> AngularGradient {
        let lightTeal = Color(#colorLiteral(red: 0.2785285413, green: 0.9299042821, blue: 0.9448828101, alpha: 1))
        let yellow    = Color(#colorLiteral(red: 0.9300076365, green: 0.8226149678, blue: 0.59575665, alpha: 1))
        let pink      = Color(#colorLiteral(red: 0.9437599778, green: 0.3392140865, blue: 0.8994731307, alpha: 1))
        let purple    = Color(#colorLiteral(red: 0.5234025717, green: 0.3247769475, blue: 0.9921132922, alpha: 1))
        let softBlue  = Color(#colorLiteral(red: 0.137432307, green: 0.5998355746, blue: 0.9898411632, alpha: 1))

        let gradient = Gradient(stops:
                                    [.init(color:lightTeal, location: 0.2),
                                     .init(color: softBlue, location: 0.4),
                                     .init(color: purple, location: 0.6),
                                     .init(color: pink, location: 0.8),
                                     .init(color: yellow, location: 1.0)])

        return AngularGradient(gradient: gradient, center: .init(x: 0.25, y: 0.55), angle: shifted ? angle : .zero)
    }

    func makeBody(configuration: ButtonStyleConfiguration) -> some View {
        let background = NinetiesBackground(isPressed: configuration.isPressed,
                                            pressedGradient: gradient(shifted: false),
                                            unpressedGradient: gradient(shifted: true))
        return configuration.label
            .foregroundColor(configuration.isPressed ? Color.pink : Color.white)
            .modifier(background)
    }

    struct NinetiesBackground: ViewModifier {
        let isPressed: Bool
        let pressedGradient: AngularGradient
        let unpressedGradient: AngularGradient

        func body(content: Content) -> some View {
            let foreground = content
                    .padding(.horizontal, 24)
                    .padding(.vertical, 14)
                    .foregroundColor(.white)
            return foreground
                .background(Capsule().fill(isPressed ? pressedGradient : unpressedGradient))
        }
    }
}
struct ContentView: View {

    var body: some View {
      Button("Awesome", action: {})
          .buttonStyle(CustomNinetiesButtonStyle())
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10056/11/7A6C9FD8-33A7-4FA5-BF00-AA6A9D0A1A5B/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10056) — developer.apple.com. Indexed for agent consumption._