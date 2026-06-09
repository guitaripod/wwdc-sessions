---
id: "wwdc2022-10170"
event: "wwdc2022"
year: 2022
title: "Implement App Shortcuts with App Intents"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10170"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Implement App Shortcuts with App Intents

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10170](https://developer.apple.com/videos/play/wwdc2022/10170)

Discover how you can create Shortcuts in your app with zero user setup. We'll show you how App Intents can help you present custom Shortcuts views, and explore how you can add support for parameterized phrases to allow people to quickly express their intent. We'll also share how you can make your App Shortcuts discoverable with a Siri Tip, and Shortcuts links. To get the most out of this session, we recommend a basic familiarity with SwiftUI.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,644 words)

## Documentation & Resources

- [App Intents](https://developer.apple.com/documentation/AppIntents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents.json

## Code Snippets

### Implement an AppIntent — [3:43]

```swift
// StartMeditationIntent creates a meditation session.

import AppIntents

struct StartMeditationIntent: AppIntent {
    static let title: LocalizedStringResource = "Start Meditation Session"

    func perform() async throws -> some IntentResult & ProvidesDialog {
        await MeditationService.startDefaultSession()
        return .result(dialog: "Okay, starting a meditation session.")
    }
}
```

### Create an AppShortcutsProvider — [5:31]

```swift
// An AppShortcut turns an Intent into a full fledged shortcut
// AppShortcuts are returned from a struct that implements the AppShortcuts
// protocol

import AppIntents

struct MeditationShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartMeditationIntent(),
            phrases: ["Start a \(.applicationName)"]
        )
    }
}
```

### Provide multiple phrases — [6:35]

```swift
// An AppShortcut turns an Intent into a full fledged shortcut
// AppShortcuts are returned from a struct that implements the AppShortcuts
// protocol

import AppIntents

struct MeditationShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartMeditationIntent(),
            phrases: [
                "Start a \(.applicationName)",
                "Begin \(.applicationName)",
                "Meditate with \(.applicationName)",
                "Start a session with \(.applicationName)"
            ]
        )
    }
}
```

### Provide a dialog and snippet view — [8:54]

```swift
// Custom views give your intent more personality
// and can convey more information

func perform() async throws -> some ProvidesDialog & ShowsSnippetView {
    await MeditationService.startDefaultSession()

    return .result(
        dialog: "Okay, starting a meditation session.",
        view: MeditationSnippetView()
    )
}
```

### Implement an AppEntity — [10:09]

```swift
// An entity is a type that can be used as a parameter
// for an AppIntent.

import AppIntents

struct MeditationSession: AppEntity {
    let id: UUID
    let name: LocalizedStringResource

    static var typeDisplayName: LocalizedStringResource = "Meditation Session"
    var displayRepresentation: AppIntents.DisplayRepresentation {
        DisplayRepresentation(title: name)
    }

    static var defaultQuery = MeditationSessionQuery()
}
```

### Query for entities — [10:55]

```swift
// Queries allow the App Intents framework to
// look up your entities by their identifier

struct MeditationSessionQuery: EntityQuery {
    func entities(for identifiers: [UUID]) async throws -> [MeditationSession] {
        return identifiers.compactMap { SessionManager.session(for: $0) }
    }
}
```

### Define a parameter — [11:16]

```swift
// Adding a parameter to an intent allows you to prompt the user
// to provide a value for the parameter

struct StartMeditationIntent: AppIntent {

    @Parameter(title: "Session Type")
    var sessionType: SessionType?

    // ...

}
```

### Prompt for values — [13:15]

```swift
// Prompting for values can be done by calling methods
// on the property's wrapper type.

func perform() async throws -> some ProvidesDialog {
    let sessionToRun = self.session ?? try await $session.requestDisambiguation(
           among: SessionManager.allSessions,
           dialog: IntentDialog("What session would you like?")
       )
    }
    await MeditationService.start(session: sessionToRun)
    return .result(
       dialog: "Okay, starting a \(sessionToRun.name) meditation session."
    )
}
```

### Implement suggestedEntities() — [16:11]

```swift
// Queries can provide suggested values for your Entity
// that serve as parameters for App Shortcuts

struct MeditationSessionQuery: EntityQuery {
    func entities(for identifiers: [UUID]) async throws -> [MeditationSession] {
        return identifiers.compactMap { SessionManager.session(for: $0) }
    }

    func suggestedEntities() async throws -> [MeditationSession] {
        return SessionManager.allSessions
    }
}
```

### Update App Shortcut parameters — [16:34]

```swift
// Your app must notify App Intents when your values change
// This is typically best done in your app’s model layer

class SessionModel {
    @Published
    var sessions: [MeditationSession] = []
    private var cancellable: AnyCancellable?

    init() {
        self.cancellable = $sessions.sink { _ in
            MeditationShortcuts.updateAppShortcutParameters()
        }
    }

    // ...

}
```

### Add parameterized phrases — [17:09]

```swift
// Phrases can also contain a single parameter reference

import AppIntents

struct MeditationShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartMeditationIntent(),
            phrases: [
                "Start a \(.applicationName)",
                "Begin \(.applicationName)",
                "Meditate with \(.applicationName)",
                "Start a \(\.$session) session with \(.applicationName)",
                "Begin a \(\.$session) session with \(.applicationName)",
                "Meditate on \(\.$session) with \(.applicationName)"
            ]
        )
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10170/3/30D42D9F-AF97-4B32-B470-C0A9B4D8C279/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10170/3/30D42D9F-AF97-4B32-B470-C0A9B4D8C279/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10170) — developer.apple.com. Indexed for agent consumption._
