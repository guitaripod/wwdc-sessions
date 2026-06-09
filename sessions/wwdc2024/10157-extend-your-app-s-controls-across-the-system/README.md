---
id: "wwdc2024-10157"
event: "wwdc2024"
year: 2024
title: "Extend your app’s controls across the system"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10157"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Extend your app’s controls across the system

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10157](https://developer.apple.com/videos/play/wwdc2024/10157)

Bring your app’s controls to Control Center, the Lock Screen, and beyond. Learn how you can use WidgetKit to extend your app’s controls to the system experience. We’ll cover how you can to build a control, tailor its appearance, and make it configurable.

**Keywords:** `controlwidget`, `controlwidgetbutton`, `controlwidgettoggle`, `widgetkit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,574 words)

## Documentation & Resources

- [Creating a camera experience for the Lock Screen](https://developer.apple.com/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/LockedCameraCapture/Creating-a-camera-experience-for-the-Lock-Screen.json
- [Updating controls locally and remotely](https://developer.apple.com/documentation/WidgetKit/Updating-controls-locally-and-remotely) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Updating-controls-locally-and-remotely
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Updating-controls-locally-and-remotely.json
- [Adding refinements and configuration to controls](https://developer.apple.com/documentation/WidgetKit/Adding-refinements-and-configuration-to-controls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Adding-refinements-and-configuration-to-controls
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Adding-refinements-and-configuration-to-controls.json
- [Creating controls to perform actions across the system](https://developer.apple.com/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system.json
- [Human Interface Guidelines: Controls](https://developer.apple.com/design/human-interface-guidelines/controls) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/controls
- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010

## Code Snippets

### Add the control to the Widget Bundle — [3:13]

```swift
@main
struct ProductivityExtensionBundle: WidgetBundle {

    var body: some Widget {
        ChecklistWidget()
        TaskCounterWidget()
        TimerToggle()
    }

}
```

### Complete the control — [3:29]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle"
        ) {
            ControlWidgetToggle(
                "Work Timer",
                isOn: TimerManager.shared.isRunning,
                action: ToggleTimerIntent()
            ) { _ in
                Image(systemName:
                      "hourglass.bottomhalf.filled")
            }
        }
    }
}
```

### Specify different symbols when on and off​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ — [4:41]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle"
        ) {
            ControlWidgetToggle(
                "Work Timer",
                isOn: TimerManager.shared.isRunning,
                action: ToggleTimerIntent()
            ) { isOn in
                Image(systemName: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
            }
        }
    }
}
```

### Specify custom value text​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​ and add a custom tint color — [5:21]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle"
        ) {
            ControlWidgetToggle(
                "Work Timer",
                isOn: TimerManager.shared.isRunning,
                action: ToggleTimerIntent()
            ) { isOn in
                Label(isOn ? "Running" : "Stopped",
                      systemImage: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
            }
            .tint(.purple)
        }
    }
}
```

### Implement timer toggling — [8:14]

```swift
struct ToggleTimerIntent: SetValueIntent, LiveActivityIntent {
    static let title: LocalizedStringResource = "Productivity Timer"

    @Parameter(title: "Running")
    var value: Bool  // The timer’s running state

    func perform() throws -> some IntentResult {
        TimerManager.shared.setTimerRunning(value)
        return .result()
    }
}
```

### Refresh the control from within the app — [8:54]

```swift
func timerManager(_ manager: TimerManager,
                  timerDidChange timer: ProductivityTimer) {
    ControlCenter.shared.reloadControls(
        ofKind: "com.apple.Productivity.TimerToggle"
    )
}
```

### Define a Value Provider — [10:03]

```swift
struct TimerValueProvider: ControlValueProvider {

    func currentValue() async throws -> Bool {
        try await TimerManager.shared.fetchRunningState()
    }

    let previewValue: Bool = false
}
```

### Provide asynchronously fetched state with a Value Provider — [11:00]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        StaticControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle",
            provider: TimerValueProvider()
        ) { isRunning in
            ControlWidgetToggle(
                "Work Timer",
                isOn: isRunning,
                action: ToggleTimerIntent()
            ) { isOn in
                Label(isOn ? "Running" : "Stopped",
                      systemImage: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
            }
            .tint(.purple)
        }
    }
}
```

### Make the Value Provider configurable — [13:06]

```swift
struct ConfigurableTimerValueProvider: AppIntentControlValueProvider {
    func currentValue(configuration: SelectTimerIntent) async throws -> TimerState {
        let timer = configuration.timer
        let isRunning = try await TimerManager.shared.fetchTimerRunning(timer: timer)
        return TimerState(timer: timer, isRunning: isRunning)
    }

    func previewValue(configuration: SelectTimerIntent) -> TimerState {
        return TimerState(timer: configuration.timer, isRunning: false)
    }
}
```

### Make the timer configurable — [13:40]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle",
            provider: ConfigurableTimerValueProvider()
        ) { timerState in
            ControlWidgetToggle(
                timerState.timer.name,
                isOn: timerState.isRunning,
                action: ToggleTimerIntent(timer: timerState.timer)
            ) { isOn in
                Label(isOn ? "Running" : "Stopped",
                      systemImage: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
            }
            .tint(.purple)
        }
    }
}
```

### Prompt for user configuration automatically — [14:26]

```swift
struct SomeControl: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(
            // ...
        )
        .promptsForUserConfiguration()
    }
}
```

### Custom action hint -> hint treated as verb phrase — [15:42]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle",
            provider: ConfigurableTimerValueProvider()
        ) { timerState in
            ControlWidgetToggle(
                timerState.timer.name,
                isOn: timerState.isRunning,
                action: ToggleTimerIntent(timer: timerState.timer)
            ) { isOn in
                Label(isOn ? "Running" : "Stopped",
                      systemImage: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
                .controlWidgetActionHint(isOn ?
                                         "Start" : "Stop")
            }
            .tint(.purple)
        }
    }
}
```

### Specify a display name and add a description — [16:56]

```swift
struct TimerToggle: ControlWidget {
    var body: some ControlWidgetConfiguration {
        AppIntentControlConfiguration(
            kind: "com.apple.Productivity.TimerToggle",
            provider: ConfigurableTimerValueProvider()
        ) { timerState in
            ControlWidgetToggle(
                timerState.timer.name,
                isOn: timerState.isRunning,
                action: ToggleTimerIntent(timer: timerState.timer)
            ) { isOn in
                Label(isOn ? "Running" : "Stopped",
                      systemImage: isOn
                      ? "hourglass"
                      : "hourglass.bottomhalf.filled")
                .controlWidgetActionHint(isOn ?
                                         "Start" : "Stop")
            }
            .tint(.purple)
        }
        .displayName("Productivity Timer")
        .description("Start and stop a productivity timer.")
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10157/5/5DC0FBFA-B601-4A2F-BE3D-40FBF3757522/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10157/5/5DC0FBFA-B601-4A2F-BE3D-40FBF3757522/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10157) — developer.apple.com. Indexed for agent consumption._
