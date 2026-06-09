---
id: "wwdc2021-10122"
event: "wwdc2021"
year: 2021
title: "Bring accessibility to charts in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10122"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Bring accessibility to charts in your app

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10122](https://developer.apple.com/videos/play/wwdc2021/10122)

Charts are an essential tool for understanding data, and critical to understanding ourselves, our health, our finances, and our world. Find out how you can make charts accessible in your apps to people with vision impairments through audio graphs and sonified data. And we'll show you how to improve your charts for accessibility through universal design principles and system accessibility settings.

**Keywords:** `accessibilitychartdescriptor`, `accessible chart`, `audio graph`, `audio graphs`, `axcategoricalaxisdescriptor`, `axchart`, `axchartdescriptor`, `axdataseriesdescriptor`, `axnumbericdataaxisdescriptor`, `chart details`, `chartview`, `chart with sound`, `colors`, `contrast ratio`, `datapoint`, `haptic chart feedback`, `high contrast`, `inclusive charts`, `inclusive design`, `low vision`, `reduce transparency`, `sonified chart`, `visual accessibility`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,377 words)

## Documentation & Resources

- [Appearance Effects and Motion](https://developer.apple.com/design/human-interface-guidelines/accessibility/overview/appearance-effects/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility/overview/appearance-effects/
- [Color and Contrast](https://developer.apple.com/design/human-interface-guidelines/accessibility/overview/color-and-contrast/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/accessibility/overview/color-and-contrast/
- [isReduceMotionEnabled](https://developer.apple.com/documentation/UIKit/UIAccessibility/isReduceMotionEnabled) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIAccessibility/isReduceMotionEnabled
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIAccessibility/isReduceMotionEnabled.json
- [accessibilityReduceMotion](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/EnvironmentValues/accessibilityReduceMotion.json
- [Audio graphs](https://developer.apple.com/documentation/Accessibility/audio-graphs) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Accessibility/audio-graphs
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Accessibility/audio-graphs.json

## Code Snippets

### Chart Model — [10:47]

```swift
class ChartView: UIView {
    let model: ChartModel

    func drawChart() {
        // ...
    }
}

struct ChartModel {
    let title: String
    let dataPoints: [DataPoint]

    struct DataPoint {
        let name: String
        let x: Double
        let y: Double
    }
}
```

### ChartView — [10:48]

```swift
extension ChartView {
    public override var accessibilityContainerType: UIAccessibilityContainerType { … }
    public override var accessibilityLabel: String? { … }

    public override var accessibilityElements: [Any]? {
        get {
            return model.dataPoints.map { point in
                let axElement = UIAccessibilityElement(accessibilityContainer: self)
                axElement.accessibilityValue = "\(point.x) cups, \(point.y) lines of code"
                axElement.accessibilityFrameInContainerSpace = frameRect(for: point)
                return axElement
            }
        }
        set {}
    }

 private func frameRect(for dataPoint: DataPoint) -> CGRect {
```

### Basic chart definition example — [14:23]

```swift
struct ChartModel {
    let title: String
    let summary: String
    let xAxis: Axis
    let yAxis: Axis
    let data: [DataPoint]

    struct Axis {
        let title: String
        let range: ClosedRange<Double>
    }

    struct DataPoint {
        let name: String
        let x: Double
        let y: Double
    }
}
```

### Enabling Audio Graphs — [15:08]

```swift
import Accessibility

extension ChartView: AXChart {

public var accessibilityChartDescriptor: AXChartDescriptor? {
    get {
    }
    set {}
    }
}
```

### Chart Descriptor- Basic — [15:35]

```swift
public var accessibilityChartDescriptor: AXChartDescriptor? {
    get {
        let xAxis = AXNumericDataAxisDescriptor( … ) 
        let yAxis = AXNumericDataAxisDescriptor(title: model.yAxis.title,
                                                range: model.yAxis.range,
                                                gridlinePositions:[],
                                                valueDescriptionProvider: { value in
            return "\(value) lines of code"
        })
    }
    set {}
}
```

### Chart Descriptor- Continued — [16:55]

```swift
public var accessibilityChartDescriptor: AXChartDescriptor? {
    get {
        let xAxis = AXNumericDataAxisDescriptor( … )
        let yAxis = AXNumericDataAxisDescriptor( … )
        let series = AXDataSeriesDescriptor( … )
        return AXChartDescriptor(title: model.title,
                                 summary: model.summary,
                                 xAxis: xAxis,
                                 yAxis: yAxis,
                                 additionalAxes: [],
                                 series: [series])
    }
    set {}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10122/6/218A971D-4AB5-4417-96CE-15D01B009082/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10122/6/218A971D-4AB5-4417-96CE-15D01B009082/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10122) — developer.apple.com. Indexed for agent consumption._
