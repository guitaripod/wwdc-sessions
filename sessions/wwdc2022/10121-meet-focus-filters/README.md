---
id: "wwdc2022-10121"
event: "wwdc2022"
year: 2022
title: "Meet Focus filters"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10121"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Meet Focus filters

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10121](https://developer.apple.com/videos/play/wwdc2022/10121)

Discover how you can customize app behaviors based on someone's currently enabled Focus. We'll show you how to use App Intents to define your app's Focus filters, act on changes from the system, and present your app's views in different ways. We'll also explore how you can filter notifications and update badge counts. To get the most out of this session, we recommend first watching "Dive into App Intents" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,192 words)

## Documentation & Resources

- [Focus](https://developer.apple.com/documentation/AppIntents/focus) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/focus
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/focus.json
- [User Notifications](https://developer.apple.com/documentation/UserNotifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications.json

## Code Snippets

### Implementing SetFocusFilterIntent — [4:57]

```swift
// Implementing SetFocusFilterIntent

import AppIntents

struct ExampleChatAppFocusFilter: SetFocusFilterIntent {

    static var title: LocalizedStringResource = "Set account, status & look"
    static var description: LocalizedStringResource? = """
        Select an account, set your status, and configure
        the look of Example Chat App.
    """
}
```

### Defining your Parameters & Entities — [7:02]

```swift
// Defining your Parameters & Entities

import AppIntents

struct ExampleChatAppFocusFilter: SetFocusFilterIntent {

    @Parameter(title: "Use Dark Mode", default: false)
    var alwaysUseDarkMode: Bool

    @Parameter(title: "Status Message")
    var status: String?

    @Parameter(title: "Selected Account")
    var account: AccountEntity?

    // ...
}
```

### Display Representation — [8:43]

```swift
// Display Representation

struct ExampleChatAppFocusFilter: SetFocusFilterIntent {
    // ...

    var localizedDarkModeString: String {
        return self.alwaysUseDarkMode ? "Dark" : "Dynamic"
    }

    var displayRepresentation: DisplayRepresentation {
        var titleList: [LocalizedStringResource] = [], subtitleList: [String] = []
        if let account = self.account {
            titleList.append("Account")
            subtitleList.append(account.displayName)
        }
        if let status = self.status {
            titleList.append("Status")
            subtitleList.append(status)
        }
        titleList.append("Look")
        subtitleList.append(self.localizedDarkModeString)

        let title = LocalizedStringResource("Set \(titleList, format: .list(type: .and))")
        let subtitle = LocalizedStringResource("\(subtitleList.formatted())")

        return DisplayRepresentation(title: title, subtitle: subtitle)
    }

    // ...
}
```

### Implementing Perform on your Focus filter — [11:24]

```swift
// Implementing Perform on your Focus filter

import AppIntents

struct ExampleChatAppFocusFilter: SetFocusFilterIntent {
    // ...

    func perform() async throws -> some IntentResult {
        let myData = AppData(
            alwaysUseDarkMode: self.alwaysUseDarkMode,
            status: self.status,
            account: self.account
        )
        myModel.shared.updateAppWithData(myData)
        return .result()
    }

    // ...
}
```

### Calling Current — [11:47]

```swift
// Calling Current

import AppIntents

func updateCurrentFilter() async throws {
    do {
        let currentFilter = try await ExampleChatAppFocusFilter.current
        let myData = AppData(
            myRequiredBoolValue: currentFilter.myRequiredBoolValue,
            myOptionalStringValue: currentFilter.myOptionalStringValue,
            myOptionalAppEnum: currentFilter.myOptionalAppEnum,
            myAppEntity: currentFilter.myAppEntity
        )
        myModel.shared.updateAppWithData(myData)
    } catch let error {
        print("Error loading current filter: \(error.localizedDescription)")
        throw error
    }
}
```

### Set a filterPredicate — [13:27]

```swift
// Set filterPredicate on an App context

import AppIntents

struct ExampleChatAppFocusFilter: SetFocusFilterIntent {

    var appContext: FocusFilterAppContext {
        let allowedAccountList = [account.identifier]
        let predicate = NSPredicate(format: "SELF IN %@", allowedAccountList)
        return FocusFilterAppContext(notificationFilterPredicate: predicate)
    }
}
```

### Pass filterCriteria on UNNotificationContent — [13:53]

```swift
// Pass filterCriteria on UNNotificationContent

let content = UNMutableNotificationContent()
content.title = "Curt Rothert"
content.subtitle = "Slide Feedback"
content.body = "The run through today was great. I had few comments about slide 22 and 28."
content.filterCriteria = "work-account-identifier"
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10121/5/E497A884-24B9-4D6C-A35D-6F9BEEB985B6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10121/5/E497A884-24B9-4D6C-A35D-6F9BEEB985B6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10121) — developer.apple.com. Indexed for agent consumption._
