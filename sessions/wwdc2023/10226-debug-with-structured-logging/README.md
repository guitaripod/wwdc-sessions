---
id: "wwdc2023-10226"
event: "wwdc2023"
year: 2023
title: "Debug with structured logging"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10226"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Debug with structured logging

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10226](https://developer.apple.com/videos/play/wwdc2023/10226)

Discover the debug console in Xcode 15 and learn how you can improve your diagnostic experience through logging. Explore how you can navigate your logs easily and efficiently using advanced filtering and improved visualization. We’ll also show you how to use the dwim-print command to evaluate expressions in your code while debugging.

**Keywords:** `⚡️`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,402 words)

## Documentation & Resources

- [Logging](https://developer.apple.com/documentation/os/logging) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/os/logging
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/os/logging.json

## Code Snippets

### Calling setDisplayName from Edit Account page — [5:17]

```swift
.onSubmit {
    logger.info("Requesting to change displayName to \(displayName)")
    accountViewModel.setDisplayName(displayName)
}
```

### Account Data Setters (Before Fix) — [5:34]

```swift
public func setDisplayName(_ newDisplayName: String) {
    logger.info("Sending Request to update DisplayName")

    Database.setValueForKey(Database.Key.displayName, value: newDisplayName, forAccount: account.id)

    logger.info("Updated DisplayName to '\(newDisplayName)'")
}

public func setEmailAddressName(_ newEmailAddress: String) {
    logger.info("Sending Request to update EmailAddress")

    Database.setValueForKey(Database.Key.emailAddress, value: newEmailAddress, forAccount: account.id)

    logger.info("Updated EmailAddress to '\(newEmailAddress)'")
}
```

### Account Data Setters (After Fix) — [6:04]

```swift
public func setDisplayName(_ newDisplayName: String) {
    logger.info("Sending Request to update DisplayName")

    Database.setValueForKey(Database.Key.displayName, value: newDisplayName, forAccount: account.id)

    account.displayName = newDisplayName

    logger.info("Updated DisplayName to '\(newDisplayName)'")
}

public func setEmailAddressName(_ newEmailAddress: String) {
    logger.info("Sending Request to update EmailAddress")

    Database.setValueForKey(Database.Key.emailAddress, value: newEmailAddress, forAccount: account.id)

    account.emailAddress = newEmailAddress

    logger.info("Updated EmailAddress to '\(newEmailAddress)'")
}
```

### po account — [6:35]

```bash
(lldb) po account
```

### po account (with result) — [6:39]

```bash
(lldb) po account
<Account: 0x60000223b2a0>
```

### p account — [7:00]

```bash
(lldb) p account
```

### po account (with result) — [7:04]

```bash
(lldb) p account
(BackyardBirdsData.Account) =0x000060000223b2a0 {
	id = 3A9FC684-8DFC-4D7D-B645-E393AEBA14EE
	joinDate = 2023-06-05 16:41:00 UTC
	displayName = "Sample Account"
	emailAddress = "sample_account@icloud.com"
	isPremiumMember = true
}
```

### p account (after fix) — [7:18]

```bash
(lldb) p account
(BackyardBirdsData.Account) =0x000060000223b2a0 {
	id = 3A9FC684-8DFC-4D7D-B645-E393AEBA14EE
	joinDate = 2023-06-05 16:41:00 UTC
	displayName = "Johnny Appleseed"
	emailAddress = "johnny_appleseed@icloud.com"
	isPremiumMember = true
}
```

### Login Method Skeleton — [9:43]

```swift
func login(password: String) -> Error? {
    var error: Error? = nil

    //...

    loggedIn = true
    return error
}
```

### Login Method with Print Statements — [9:56]

```swift
func login(password: String) -> Error? {
    var error: Error? = nil
    print("Logging in user '\(username)'...")

    …

    if let error {
        print("User '\(username)' failed to log in. Error: \(error)")
    } else {
        loggedIn = true
        print("User '\(username)' logged in successfully.")
    }
    return error
}
```

### Login Method with Extended Print Statements — [10:18]

```swift
func login(password: String) -> Error? {
    var error: Error? = nil
    print("🤖 Logging in user '\(username)'... (\(#file):\(#line))")

    //...

    if let error {
        print("🤖 User '\(username)' failed to log in. Error: \(error) (\(#file):\(#line))")
    } else {
        loggedIn = true
        print("🤖 User '\(username)' logged in successfully. (\(#file):\(#line))")
    }
    return error
}
```

### Login Method with Partial OSLog Transition — [10:40]

```swift
import OSLog

let logger = Logger(subsystem: "BackyardBirdsData", category: "Account")

func login(password: String) -> Error? {
    var error: Error? = nil
    print("🤖 Logging in user '\(username)'... (\(#file):\(#line))")

    //...

    if let error {
        print("🤖 User '\(username)' failed to log in. Error: \(error) (\(#file):\(#line))")
    } else {
        loggedIn = true
        print("🤖 User '\(username)' logged in successfully. (\(#file):\(#line))")
    }
    return error
}
```

### Login Method with OSLog Statements — [11:00]

```swift
import OSLog

let logger = Logger(subsystem: "BackyardBirdsData", category: "Account")

func login(password: String) -> Error? {
    var error: Error? = nil
    logger.info("Logging in user '\(username)'...")

    //...

    if let error {
        logger.error("User '\(username)' failed to log in. Error: \(error)")
    } else {
        loggedIn = true
        logger.notice("User '\(username)' logged in successfully.")
    }
    return error
}
```

### Example Logging Statements — [11:16]

```swift
let logger = Logger(subsystem: "BackyardBirdsData", category: "Account")
logger.error("User '\(username)' failed to log in. Error: \(error)")
logger.notice("User '\(username)' logged in successfully.")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10226/5/FFFDC5A2-A309-4C9B-B908-B19B51F18FB0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10226/5/FFFDC5A2-A309-4C9B-B908-B19B51F18FB0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10226) — developer.apple.com. Indexed for agent consumption._
