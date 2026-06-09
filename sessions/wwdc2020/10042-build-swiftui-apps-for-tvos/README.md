---
id: "wwdc2020-10042"
event: "wwdc2020"
year: 2020
title: "Build SwiftUI apps for tvOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10042"
topics: ["SwiftUI & UI Frameworks", "Audio & Video"]
platforms: ["tvOS"]
hasTranscript: true
---

# Build SwiftUI apps for tvOS

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** tvOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10042](https://developer.apple.com/videos/play/wwdc2020/10042)

Add a new dimension to your tvOS app with SwiftUI. We’ll show you how to build layouts powered by SwiftUI and customize your interface with custom buttons, provide more functionality in your app with a context menu, check if views are focused, and manage default focus. To get the most out of this session, you should be comfortable with SwiftUI. For a primer, watch “Introducing SwiftUI: Building Your First App” and “SwiftUI On All Devices.”

**Keywords:** `apple tv`, `apple tv 4k`, `apple tv app`, `focus`, `focus engine`, `lazy grids`, `swift`, `swift developer`, `swiftui`, `tv`, `tv dev`, `tv developer`, `tvos`, `tv swift`, `tv swiftui`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,875 words)

## Documentation & Resources

- [Supporting Multiple Users in Your tvOS App](https://developer.apple.com/documentation/TVServices/supporting-multiple-users-in-your-tvos-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TVServices/supporting-multiple-users-in-your-tvos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TVServices/supporting-multiple-users-in-your-tvos-app.json
- [isFocused](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isFocused) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/EnvironmentValues/isFocused
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/EnvironmentValues/isFocused.json
- [prefersDefaultFocus(_:in:)](https://developer.apple.com/documentation/SwiftUI/View/prefersDefaultFocus(_:in:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View/prefersDefaultFocus(_:in:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View/prefersDefaultFocus(_:in:).json
- [CardButtonStyle](https://developer.apple.com/documentation/SwiftUI/CardButtonStyle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/CardButtonStyle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/CardButtonStyle.json
- [Learn to Make Apps with SwiftUI](https://developer.apple.com/tutorials/swiftui) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/tutorials/swiftui
- [SwiftUI](https://developer.apple.com/documentation/SwiftUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI.json
- [Human Interface Guidelines: Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-tvos

## Code Snippets

### CardButtonStyle — [1:42]

```swift
Button(albumLabel, action: playAlbum)
    .buttonStyle(CardButtonStyle())
```

### Custom Button Styles — [2:24]

```swift
struct MyNewButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
           .background(configuration.isPressed ? … : …) // Custom styling
    }
}           

Button(albumLabel, action: playAlbum)
    .buttonStyle(MyNewButtonStyle())
```

### Context Menus — [3:19]

```swift
AlbumView()
    .contextMenu {
        Button("Add to Favorites", action: addAlbumToFavorites)
        Button("View Artist", action: viewArtistPage)
        Button("Discover Similar Albums", action: viewSimilarAlbums)
    }
```

### isFocused Environment Variable — [5:47]

```swift
struct SongView: View {
    var body: some View {
        Button(action: playSong) {
            VStack {
                Image(albumArt)
                DetailsView(...)
            }
        }.buttonStyle(MyCustomButtonStyle())
    }
}

struct DetailsView: View {
    ...
    @Environment(\.isFocused) var isFocused: Bool
    var body: some View {
        VStack {
            Text(songName)
            Text(isFocused ? artistAndAlbum : artistName)
        }
    }
}
```

### Login Screen (Default Focus) — [8:42]

```swift
var body: some View {
    VStack {
        TextField("Username", text: $username)

        SecureField("Password", text: $password)

        Button("Log In", action: logIn)

    }

}
```

### Default Focus — [8:51]

```swift
@Namespace private var namespace
@State private var areCredentialsFilled: Bool

var body: some View {
    VStack {
        TextField("Username", text: $username)
            .prefersDefaultFocus(!areCredentialsFilled, in: namespace)            
        SecureField("Password", text: $password)

        Button("Log In", action: logIn)
           .prefersDefaultFocus(areCredentialsFilled, in: namespace)
    }
    .focusScope(namespace)
}
```

### Reset Focus — [11:12]

```swift
@Namespace private var namespace
@State private var areCredentialsFilled: Bool
@Environment(\.resetFocus) var resetFocus

var body: some View {
    VStack {
        TextField("Username", text: $username)
            .prefersDefaultFocus(!areCredentialsFilled, in: namespace)            
        SecureField("Password", text: $password)

        Button("Log In", action: logIn)
           .prefersDefaultFocus(areCredentialsFilled, in: namespace)

        Button("Clear", action: { 
            username = ""; password = ""
            areCredentialsFilled = false
            resetFocus(in: namespace)
        })
    }
    .focusScope(namespace)
}
```

### Lazy Grids — [12:45]

```swift
struct ShelfView: View {
    var body: some View {
        ScrollView([.horizontal]) {
            LazyHGrid(rows: [GridItem()]) {
                ForEach(playlists, id: \.self) { playlist in                
                    Button(action: goToPlaylist) {
                        Image(playlist.coverImage)
                            .resizable()
                            .frame(…)
                    }
                    .buttonStyle(CardButtonStyle())
                }
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10042/4/B38E5ED8-1188-4675-877A-272A47769177/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10042) — developer.apple.com. Indexed for agent consumption._
