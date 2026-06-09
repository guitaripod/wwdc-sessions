---
id: "wwdc2025-238"
event: "wwdc2025"
year: 2025
title: "Customize your app for Assistive Access"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/238"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Customize your app for Assistive Access

**Event:** WWDC25 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-238](https://developer.apple.com/videos/play/wwdc2025/238)

Assistive Access is a distinctive, focused iOS experience that makes it easier for people with cognitive disabilities to use iPhone and iPad independently. In iOS and iPadOS 26, you can customize your app when it’s running in Assistive Access to give people greater ease and independence. Learn how to tailor your app using the AssistiveAccess SwiftUI scene type, and explore the key design principles that can help you create a high-quality Assistive Access experience for everyone.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,179 words)

## Documentation & Resources

- [AssistiveAccess](https://developer.apple.com/documentation/SwiftUI/AssistiveAccess) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/AssistiveAccess
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/AssistiveAccess.json
- [Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility
- [UISupportsFullScreenInAssistiveAccess](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UISupportsFullScreenInAssistiveAccess) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BundleResources/Information-Property-List/UISupportsFullScreenInAssistiveAccess
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BundleResources/Information-Property-List/UISupportsFullScreenInAssistiveAccess.json

## Code Snippets

### Create a scene for Assistive Access — [5:21]

```swift
// Create a scene for Assistive Access

import SwiftUI
import SwiftData

@main
struct WWDCDrawApp: App {
  var body: some Scene {
    WindowGroup {
      ContentView()
        .modelContainer(for: [DrawingModel.self])
    }
    AssistiveAccess {
      AssistiveAccessContentView()
          .modelContainer(for: [DrawingModel.self])
    }
  }
}
```

### Display an Assistive Access preview — [6:25]

```swift
// Display an Assistive Access preview

import SwiftUI

struct AssistiveAccessContentView: View {
  @Environment(\.modelContext) var context
  var body: some View {
    VStack {
      Image(systemName: "globe")
        .imageScale(.large)
        .foregroundStyle(.tint)
      Text("Hello, world!")
    }
    .padding()
  }
}

#Preview(traits: .assistiveAccess)
    AssistiveAccessContentView()
}
```

### Declare a SwiftUI scene with UIKit — [6:35]

```swift
// Declare a SwiftUI scene with UIKit

import UIKit
import SwiftUI

class AssistiveAccessSceneDelegate: UIHostingSceneDelegate {

  static var rootScene: some Scene {
    AssistiveAccess {
      AssistiveAccessContentView()
    }
  }

    /* ... */
}
```

### Activate a SwiftUI scene with UIKit — [6:55]

```swift
// Activate a SwiftUI scene with UIKit

import UIKit

@main
class AppDelegate: UIApplicationDelegate {
  func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
    let role = connectingSceneSession.role
    let sceneConfiguration = UISceneConfiguration(name: nil, sessionRole: role)
    if role == .windowAssistiveAccessApplication {
      sceneConfiguration.delegateClass = AssistiveAccessSceneDelegate.self
    }
    return sceneConfiguration
  }
}
```

### Display an icon alongside a navigation title — [14:36]

```swift
// Display an icon alongside a navigation title

import SwiftUI

struct ColorSelectionView: View {
  var body: some View {
    Group {
      List {
        ForEach(ColorMode.allCases) { color in
          NavigationLink(destination: DrawingView(color: color)) {
            ColorThumbnail(color: color)
          }
        }
      }
      .navigationTitle("Draw")
      .assistiveAccessNavigationIcon(systemImage: "hand.draw.fill")
    }
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/238/4/a553c517-f6ca-46e7-b339-36e971996e78/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/238/4/a553c517-f6ca-46e7-b339-36e971996e78/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/238) — developer.apple.com. Indexed for agent consumption._
