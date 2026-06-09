---
id: "wwdc2020-10048"
event: "wwdc2020"
year: 2020
title: "Build complications in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10048"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Build complications in SwiftUI

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10048](https://developer.apple.com/videos/play/wwdc2020/10048)

Spice up your graphic complications on Apple Watch using SwiftUI. We’ll teach you how to use custom SwiftUI views in complications on watch faces like Meridian and Infograph, look at some best practices when creating your complications, and show you how to preview your work in Xcode 12.

To get the most out of this session, you should be familiar with the basics of SwiftUI and building complications on Apple Watch. For an overview, watch “Create Complications for Apple Watch” and read “Building watchOS App Interfaces with SwiftUI.”

Once you’ve discovered how to build graphic complications in SwiftUI, you can combine this with other watchOS 7 features like multiple complications and Face Sharing to create a watch face packed with personality and customized for people who love your app.

**Keywords:** `⌚️`, `clockkit`, `watchkit`, `watchos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,532 words)

## Documentation & Resources

- [Creating and updating a complication’s timeline](https://developer.apple.com/documentation/ClockKit/creating-and-updating-a-complication-s-timeline) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit/creating-and-updating-a-complication-s-timeline
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit/creating-and-updating-a-complication-s-timeline.json
- [Building a watchOS app](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/building_a_watchos_app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/building_a_watchos_app.json
- [ClockKit](https://developer.apple.com/documentation/ClockKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit.json

## Code Snippets

### Relative Text — [3:17]

```swift
import SwiftUI
import ClockKit

struct RelativeText: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("Count Down")
                .font(.headline)
                .foregroundColor(.accentColor)
            Label("Nap Time", systemImage: "moon.fill")
            Text(Date() + 100, style: .relative)
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

struct RelativeText_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicRectangularFullView(RelativeText())
            .previewContext()
    }
}
```

### Timer Text — [3:26]

```swift
import SwiftUI
import ClockKit

struct TimerText: View {
    var body: some View {
        VStack(alignment: .leading) {
            Label("Sourdough Timer", systemImage: "timer")
                .foregroundColor(.orange)
            Text("Time remaining: \(Date() + 100, style: .timer)")
        }
        .frame(maxWidth: .infinity, alignment: .leading)
    }
}

struct TimerText_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicRectangularFullView(TimerText())
            .previewContext()
    }
}
```

### Progress View Sample #1 — [4:04]

```swift
import SwiftUI
import ClockKit

struct ProgressSample: View {
    var body: some View {
        ProgressView(value: 0.7)
            .progressViewStyle(CircularProgressViewStyle())
    }
}

struct ProgressSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(ProgressSample())
            .previewContext()
    }
}
```

### Progress View Sample #2 — [4:15]

```swift
import SwiftUI
import ClockKit

struct ProgressSample: View {
    var body: some View {
        ProgressView(value: 0.7) {
            Image(systemName: "music.note")
        }
        .progressViewStyle(CircularProgressViewStyle())
    }
}

struct ProgressSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(ProgressSample())
            .previewContext()
    }
}
```

### Progress View Sample #3 — [4:23]

```swift
import SwiftUI
import ClockKit

struct ProgressSample: View {
    var body: some View {
        ProgressView(value: 0.7) {
            Image(systemName: "music.note")
        }
        .progressViewStyle(CircularProgressViewStyle(tint: .red))
    }
}

struct ProgressSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(ProgressSample())
            .previewContext()
    }
}
```

### Progress View Sample #4 — [4:29]

```swift
import SwiftUI
import ClockKit

struct ProgressSample: View {
    var body: some View {
        VStack(alignment: .leading) {
            Text("Water Reminder")
                .foregroundColor(.blue)
            Text("32 oz. consumed")
            ProgressView(value: 0.7)
                .progressViewStyle(LinearProgressViewStyle(tint: .blue))
        }

    }
}

struct ProgressSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicRectangularFullView(ProgressSample())
            .previewContext()
    }
}
```

### Gauge Sample #1 — [4:45]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    var body: some View {
        Gauge(value: 5.8, in: 3...10) {
            Image(systemName: "drop.fill")
                .foregroundColor(.green)
        }
        .gaugeStyle(CircularGaugeStyle())
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(GaugeSample())
            .previewContext()
    }
}
```

### Gauge Sample #2 — [4:55]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    @State var acidity = 5.8

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Image(systemName: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        }
        .gaugeStyle(CircularGaugeStyle())
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(GaugeSample())
            .previewContext()
    }
}
```

### Gauge Sample #3 — [5:02]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    @State var acidity = 5.8

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Image(systemName: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        } minimumValueLabel: {
            Text("3")
        } maximumValueLabel: {
            Text("10")
        }
        .gaugeStyle(CircularGaugeStyle())
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(GaugeSample())
            .previewContext()
    }
}
```

### Gauge Sample #4 — [5:14]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    @State var acidity = 5.8

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Image(systemName: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        } minimumValueLabel: {
            Text("3")
        } maximumValueLabel: {
            Text("10")
        }
        .gaugeStyle(CircularGaugeStyle(tint: .green))
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(GaugeSample())
            .previewContext()
    }
}
```

### Gauge Sample #5 — [5:21]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    @State var acidity = 5.8

    var body: some View {
        Gauge(value: acidity, in: 3...10) {
            Image(systemName: "drop.fill")
                .foregroundColor(.green)
        } currentValueLabel: {
            Text("\(acidity, specifier: "%.1f")")
        } minimumValueLabel: {
            Text("3")
        } maximumValueLabel: {
            Text("10")
        }
        .gaugeStyle(
            CircularGaugeStyle(
                tint: Gradient(colors: [.orange, .yellow, .green, .blue, .purple])
            )
        )
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicCircularView(GaugeSample())
            .previewContext()
    }
}
```

### Gauge Sample #6 — [5:34]

```swift
import SwiftUI
import ClockKit

struct GaugeSample: View {
    @State var acidity = 5.8

    var body: some View {
        VStack(alignment: .leading) {
            Text("Garden Soil Acidity")
                .foregroundColor(.green)
            Gauge(value: acidity, in: 3...10) {
                Image(systemName: "drop.fill")
                    .foregroundColor(.green)
            } currentValueLabel: {
                Text("\(acidity, specifier: "%.1f")")
            } minimumValueLabel: {
                Text("3")
            } maximumValueLabel: {
                Text("10")
            }
            .gaugeStyle(
                LinearGaugeStyle(
                    tint: Gradient(colors: [.orange, .yellow, .green, .blue, .purple])
                )
            )
        }
    }
}

struct GaugeSample_Previews: PreviewProvider {
    static var previews: some View {
        CLKComplicationTemplateGraphicRectangularFullView(GaugeSample())
            .previewContext()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10048/4/A4A61EDD-9948-4DB8-98BB-8BA633D211CC/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10048) — developer.apple.com. Indexed for agent consumption._