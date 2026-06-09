---
id: "wwdc2026-230"
event: "wwdc2026"
year: 2026
title: "What’s new in assessment on macOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/230"
topics: ["App Services", "Business & Education"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in assessment on macOS

**Event:** WWDC26 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-230](https://developer.apple.com/videos/play/wwdc2026/230)

Explore the Automatic Assessment Configuration framework on macOS to deliver secure tests for education apps. Learn how to leverage new APIs to create a secure, configurable testing environment that incorporates more system-level features on Mac. Find out how built-in system prechecks and accessibility controls make it easier than ever to deliver a reliable exam experience.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,871 words)

## Documentation & Resources

- [Automatic Assessment Configuration](https://developer.apple.com/documentation/AutomaticAssessmentConfiguration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AutomaticAssessmentConfiguration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AutomaticAssessmentConfiguration.json

## Code Snippets

### Set up precondition checks — [2:30]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowLockdownMode = false
    configuration.allowPrivateRelay = false
    configuration.requiresSIP = true
    configuration.requiresManagedDevice = true
    configuration.requiresSingleUser = true
    configuration.requiresUserAccountType = .standard

    return configuration
}
```

### Restrict accessibility features — [4:01]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowsAccessibilityVoiceOver = true
    configuration.allowsAccessibilitySwitchControl = false
    configuration.allowsAccessibilityAlternativeInputMethods = true
    configuration.allowsAccessibilityBackgroundSounds = true
    configuration.allowsAccessibilityHoverText = true
    configuration.allowsAccessibilityLiveSpeech = true
    configuration.allowsAccessibilitySpokenContent = true
    configuration.allowsAccessibilityVoiceControl = true
    configuration.allowsAccessibilityZoom = true

    return configuration
}
```

### Customize the Menu Bar items — [5:32]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowsMenuBar = true
    configuration.allowedMenuBarItems = [
        .battery,
        .clock,
        .volume
    ]
    configuration.allowedAppleMenuItems = [
        .sleep
    ]

    return configuration
}
```

### Define input restrictions — [7:01]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowsDictation = false
    configuration.allowsAutoFill = false
    configuration.allowsStructuralInput = false
    configuration.allowsEmojiKeyboard = false

    return configuration
}
```

### Enable dock appearance — [7:38]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowsDock = true

    return configuration
}
```

### Set allowed directories and files — [8:35]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowedDirectoriesAndFiles = [
        URL(fileURLWithPath: "~/Documents/")
    ]

    return configuration
}
```

### Set application launch restrictions — [9:58]

```swift
import AutomaticAssessmentConfiguration

func makeAssessmentConfiguration() -> AEAssessmentConfiguration {
    let configuration = AEAssessmentConfiguration()

    configuration.allowOnlyParticipantsToRun = true
    configuration.allowsUserScriptExecution = false

    return configuration
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/230/4/03914f48-0bbe-4f2d-bb09-3ae676579cf2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/230/4/03914f48-0bbe-4f2d-bb09-3ae676579cf2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/230) — developer.apple.com. Indexed for agent consumption._
