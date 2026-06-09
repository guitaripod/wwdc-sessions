---
id: "wwdc2024-10149"
event: "wwdc2024"
year: 2024
title: "Work with windows in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10149"
topics: ["Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Work with windows in SwiftUI

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS, visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10149](https://developer.apple.com/videos/play/wwdc2024/10149)

Learn how to create great single and multi-window apps in visionOS, macOS, and iPadOS. Discover tools that let you programmatically open and close windows, adjust position and size, and even replace one window with another. We’ll also explore design principles for windows that help people use your app within their workflows.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,707 words)

## Documentation & Resources

- [BOT-anist](https://developer.apple.com/documentation/visionOS/BOT-anist) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/BOT-anist
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/BOT-anist.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### BOT-anist scenes — [2:36]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        WindowGroup(id: "editor") {
            EditorContentView()
        }

        WindowGroup(id: "game") {
            GameContentView()
        }
        .windowStyle(.volumetric)
    }
}
```

### Creating the movie WindowGroup — [3:09]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        WindowGroup(id: "editor") {
            EditorContentView()
        }

        WindowGroup(id: "game") {
            GameContentView()
        }
        .windowStyle(.volumetric)

        WindowGroup(id: "movie") {
            MovieContentView()
        }
    }
}
```

### Opening a movie window — [3:55]

```swift
struct EditorContentView: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open Movie", systemImage: "tv") {
            openWindow(id: "movie")
        }
    }
}
```

### Pushing a movie window — [4:45]

```swift
struct EditorContentView: View {
    @Environment(\.pushWindow) private var pushWindow

    var body: some View {
        Button("Open Movie", systemImage: "tv") {
            pushWindow(id: "movie")
        }
    }
}
```

### Toolbar — [5:34]

```swift
CanvasView()
.toolbar {
    ToolbarItem {
        Button(...)
    }
    ...
}
```

### Title menu — [5:40]

```swift
CanvasView()
.toolbar {
    ToolbarTitleMenu {
        Button(...)
    }
    ...
}
```

### Hiding window controls — [5:48]

```swift
WindowGroup(id: "movie") {
    ...
}
.persistentSystemOverlays(.hidden)
```

### Creating the controller window — [6:28]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        ...

        WindowGroup(id: "movie") {
            MovieContentView()
        }

        WindowGroup(id: "controller") {
            ControllerContentView()
        }
    }
}
```

### Opening the controller window — [6:34]

```swift
struct GameContentView: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        ...
        Button("Open Controller", systemImage: "gamecontroller.fill") {
            openWindow(id: "controller")
        }
    }
}
```

### Positioning the controller window — [7:46]

```swift
WindowGroup(id: "controller") {
    ControllerContentView()
}
.defaultWindowPlacement { content, context in
    #if os(visionOS)
    return WindowPlacement(.utilityPanel)
    #elseif os(macOS)
    ...
    #endif
}
```

### Positioning the controller window continued — [8:45]

```swift
WindowGroup(id: "controller") {
    ControllerContentView()
}
.defaultWindowPlacement { content, context in
    #if os(visionOS)
    return WindowPlacement(.utilityPanel)
    #elseif os(macOS)
    let displayBounds = context.defaultDisplay.visibleRect
    let size = content.sizeThatFits(.unspecified)
    let position = CGPoint(
        x: displayBounds.midX - (size.width / 2),
        y: displayBounds.maxY - size.height - 20
    )
    return WindowPlacement(position, size: size)
    #endif
}
```

### Default size — [10:12]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        ...
        WindowGroup(id: "movie") {
            MovieContentView()
        }
        .defaultSize(width: 1166, height: 680)
    }
}
```

### Setting resize limits on the movie window — [10:49]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        ...
        WindowGroup(id: "movie") {
            MovieContentView()
                .frame(
                    minWidth: 680, maxWidth: 2720,
                    minHeight: 680, maxHeight: 1020
                )
        }
        .windowResizability(.contentSize)
    }
}
```

### Controller window resizability — [11:37]

```swift
@main
struct BOTanistApp: App {
    var body: some Scene {
        ...
        WindowGroup(id: "controller") {
            ControllerContentView()
        }
        .windowResizability(.contentSize)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10149/5/D0809E73-22CA-4A6A-9F6B-BC3C19A39167/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10149/5/D0809E73-22CA-4A6A-9F6B-BC3C19A39167/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10149) — developer.apple.com. Indexed for agent consumption._