---
id: "wwdc2021-10232"
event: "wwdc2021"
year: 2021
title: "Meet Shortcuts for macOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10232"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet Shortcuts for macOS

**Event:** WWDC21 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10232](https://developer.apple.com/videos/play/wwdc2021/10232)

Shortcuts is coming to macOS, and your apps are a key part of that process. Discover how you can elevate the capabilities of your app by exposing those features as Shortcuts actions. We’ll show you how to build actions for your macOS apps built with Catalyst or AppKit, deploy actions across platforms, publish and share shortcuts, and enable your app to run shortcuts from other apps. We’ll also take you through how Shortcuts fits in with existing Mac automation technologies like Automator and AppleScript.

**Keywords:** `applescript`, `automation`, `automator`, `command line automation`, `intent`, `shortcuts`, `shortcuts app`, `sirikit`, `suggestions`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,306 words)

## Documentation & Resources

- [Dispatching intents to handlers](https://developer.apple.com/documentation/SiriKit/dispatching-intents-to-handlers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/dispatching-intents-to-handlers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/dispatching-intents-to-handlers.json
- [Offering Actions in the Shortcuts App](https://developer.apple.com/documentation/SiriKit/offering-actions-in-the-shortcuts-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/offering-actions-in-the-shortcuts-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/offering-actions-in-the-shortcuts-app.json

## Code Snippets

### Adding Intent dispatch method in SwiftUI — [17:10]

```swift
import SwiftUI
import Intents

@main
struct SouperTaskApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    func application(_ application: NSApplication, handlerFor intent: INIntent) -> Any? {

    }
}
```

### Resolve intent — [18:32]

```swift
class IntentHandler: NSObject, CreateTaskIntentHandling {
    func resolveTitle(for intent: CreateTaskIntent, with completion: @escaping (INStringResolutionResult) -> Void) {
        guard let title = intent.title, !title.isEmpty else {
            return completion(.needsValue())
        }
        return completion(.success(with: title))
    }

    func resolveDueDate(for intent: CreateTaskIntent, with completion: @escaping (CreateTaskDueDateResolutionResult) -> Void) {
        guard let dateComponents = intent.dueDate else {
            return completion(.needsValue())
        }
        return completion(.success(with: dateComponents))
    }

    ...
}
```

### Date range validation in dueDate resolve method — [19:37]

```swift
func resolveDueDate(for intent: CreateTaskIntent, with completion: @escaping (CreateTaskDueDateResolutionResult) -> Void) {
        guard
            let dateComponents = intent.dueDate,
            let dueDate = Calendar.current.date(from: dateComponents)
        else {
            return completion(.needsValue())
        }
        if dueDate < Date() {
            return completion(.unsupported(forReason: .invalidDate))
        }
        return completion(.success(with: dateComponents))
    }
```

### Handle intent — [20:40]

```swift
class IntentHandler: NSObject, CreateTaskIntentHandling {
    func handle(intent: CreateTaskIntent, completion: @escaping (CreateTaskIntentResponse) -> Void) {
        let title = intent.title!
        let dueDate = intent.dueDate!

        let task = createTask(name: title, due: dueDate)

        let response = CreateTaskIntentResponse(code: .success, userActivity: nil)
        response.task = task
        completion(response)
    }
}
```

### Running Shortcut from AppleScript — [25:39]

```markdown
tell application "Shortcuts Events"
	run the shortcut whose name is "Make GIF"
end tell
```

### Using scripting bridge — [25:49]

```swift
import ScriptingBridge

@objc protocol ShortcutsEvents {
    @objc optional var shortcuts: SBElementArray { get }
}
@objc protocol Shortcut {
    @objc optional var name: String { get }
    @objc optional func run(withInput: Any?) -> Any?
}

extension SBApplication: ShortcutsEvents {}
extension SBObject: Shortcut {}

guard 
    let app: ShortcutsEvents = SBApplication(bundleIdentifier: "com.apple.shortcuts.events"),
    let shortcuts = app.shortcuts else {
    print("Couldn't access shortcuts")
    return
}

guard let shortcut = shortcuts.object(withName: "Make GIF") as? Shortcut else {
    print("Shortcut doesn't exist")
    return
}

_ = shortcut.run?(withInput: nil)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10232/4/F45F16B7-D0DD-4D4D-954B-1704C1063E3C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10232/4/F45F16B7-D0DD-4D4D-954B-1704C1063E3C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10232) — developer.apple.com. Indexed for agent consumption._
