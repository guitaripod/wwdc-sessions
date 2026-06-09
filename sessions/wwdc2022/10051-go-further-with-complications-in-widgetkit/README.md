---
id: "wwdc2022-10051"
event: "wwdc2022"
year: 2022
title: "Go further with Complications in WidgetKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10051"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["watchOS"]
hasTranscript: true
---

# Go further with Complications in WidgetKit

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10051](https://developer.apple.com/videos/play/wwdc2022/10051)

Discover how you can use WidgetKit to create beautiful complications on watch faces. We'll introduce you to the watchOS-specific features found in WidgetKit, and help you migrate from existing ClockKit complications. For more on WidgetKit, watch “Complications and Widgets: Reloaded” from WWDC22.

**Keywords:** `accessory circular family`, `accessory corner`, `accessory inline`, `accessory inline family`, `accessory rectangular`, `accessorywidgetbackground`, `auxiliary content`, `circular complication`, `clkcomplicationintentmigrationconfiguration`, `clkcomplicationwidgetmigrator`, `clockkit`, `coffeetracker`, `coffee tracker`, `complication`, `complication data source`, `configuration`, `corner complication`, `entries`, `extra large watch face`, `intent-based`, `migration`, `rich complications`, `.showswidgetlabel`, `shows widget label`, `static`, `swiftui`, `templates`, `timelines`, `views`, `watch faces`, `watch specific family`, `widget extension`, `widgetkit`, `.widgetlabel`, `widget label`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,525 words)

## Documentation & Resources

- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Converting-A-ClockKit-App
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Converting-A-ClockKit-App.json
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications.json
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations.json
- [WidgetKit](https://developer.apple.com/documentation/WidgetKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WidgetKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WidgetKit.json

## Code Snippets

### Large Corner — [3:06]

```swift
struct CornerView: View {
    let value: Double

    var body: some View {

        ZStack {
            AccessoryWidgetBackground()
            Image(systemName: "cup.and.saucer.fill")
                .font(.title.bold())
                .widgetAccentable()
        }

    }
}
```

### Corner with Gauge — [3:27]

```swift
struct CornerView: View {
    let value: Double

    var body: some View {

        ZStack {
            AccessoryWidgetBackground()
            Image(systemName: "cup.and.saucer.fill")
                .font(.title.bold())
                .widgetAccentable()
        }
        .widgetLabel {
            Gauge(value: value,
              in: 0...500) {
                Text("MG")
            } currentValueLabel: {
                Text("\(Int(value))")
            } minimumValueLabel: {
                Text("0")
            } maximumValueLabel: {
                Text("500")
            }
        }


    }
}
```

### Circular Gauge — [4:24]

```swift
struct CircularView: View {
    let value: Double

    var body: some View {

        Gauge(value: value,
              in: 0...500) {
            Text("MG")
        } currentValueLabel: {
            Text("\(Int(value))")
        }
        .gaugeStyle(.circular)

    }
}
```

### Circular Gauge with Widget Label — [4:34]

```swift
struct CircularView: View {
    let value: Double

    var body: some View {
        let mg = value.inMG()

        Gauge(value: value,
              in: 0...500) {
            Text("MG")
        } currentValueLabel: {
            Text("\(Int(value))")
        }
        .gaugeStyle(.circular)
        .widgetLabel {
            Text("\(mg, formatter: mgFormatter) Caffeine")
        }

    }

    var mgFormatter: Formatter {
        let formatter = MeasurementFormatter()
        formatter.unitOptions = [.providedUnit]
        return formatter
    }
}

extension Double {
    func inMG() -> Measurement<UnitMass> {
        Measurement<UnitMass>(value: self, unit: .milligrams)
    }
}
```

### Circular Stack with Widget Label — [4:51]

```swift
struct CircularView: View {
    let value: Double

    var body: some View {
        let mg = value.inMG()

        ZStack {
            AccessoryWidgetBackground()
            Image(systemName: "cup.and.saucer.fill")
                .font(.title.bold())
                .widgetAccentable()
        }
        .widgetLabel {
            Text("\(mg, formatter: mgFormatter) Caffeine")
        }

    }

    var mgFormatter: Formatter {
        let formatter = MeasurementFormatter()
        formatter.unitOptions = [.providedUnit]
        return formatter
    }
}

extension Double {
    func inMG() -> Measurement<UnitMass> {
        Measurement<UnitMass>(value: self, unit: .milligrams)
    }
}
```

### Circular Stack or Gauge — [5:12]

```swift
struct CircularView: View {
    let value: Double
    @Environment(\.showsWidgetLabel) var showsWidgetLabel

    var body: some View {
        let mg = value.inMG()
        if showsWidgetLabel {
            ZStack {
                AccessoryWidgetBackground()
                Image(systemName: "cup.and.saucer.fill")
                    .font(.title.bold())
                    .widgetAccentable()
            }
            .widgetLabel {
                Text("\(mg, formatter: mgFormatter) Caffeine")
            }
        }
        else {
            Gauge(value: value,
                  in: 0...500) {
                Text("MG")
            } currentValueLabel: {
                Text("\(Int(value))")
            }
            .gaugeStyle(.circular)
        }

    }

    var mgFormatter: Formatter {
        let formatter = MeasurementFormatter()
        formatter.unitOptions = [.providedUnit]
        return formatter
    }
}

extension Double {
    func inMG() -> Measurement<UnitMass> {
        Measurement<UnitMass>(value: self, unit: .milligrams)
    }
}
```

### Widget Migrator — [9:47]

```swift
var widgetMigrator: CLKComplicationWidgetMigrator {
    self
}
```

### Static Migration Configuration — [9:56]

```swift
func widgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor) async -> CLKComplicationWidgetMigrationConfiguration? {
    CLKComplicationStaticWidgetMigrationConfiguration(kind: "CoffeeTracker", extensionBundleIdentifier: widgetBundle)
}
```

### Intent Migration Configuration — [10:03]

```swift
func widgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor) async -> CLKComplicationWidgetMigrationConfiguration? {
    CLKComplicationIntentWidgetMigrationConfiguration(kind: "CoffeeTracker", extensionBundleIdentifier: widgetBundle, intent: intent, localizedDisplayName: "Coffee Tracker")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10051/3/912F72F4-A83D-4923-A276-8B231CB7D837/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10051/3/912F72F4-A83D-4923-A276-8B231CB7D837/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10051) — developer.apple.com. Indexed for agent consumption._
