---
id: "wwdc2025-313"
event: "wwdc2025"
year: 2025
title: "Bring Swift Charts to the third dimension"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/313"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Bring Swift Charts to the third dimension

**Event:** WWDC25 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-313](https://developer.apple.com/videos/play/wwdc2025/313)

Learn how to bring your 2D Swift Charts to the third dimension with Chart3D and visualize your data sets from completely new perspectives. Plot your data in 3D, visualize mathematical surfaces, and customize everything from the camera to the materials to make your 3D charts more intuitive and delightful. 

To get the most out of this session, we recommend being familiar with creating 2D Swift Charts.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,450 words)

## Documentation & Resources

- [Swift Charts updates](https://developer.apple.com/documentation/Updates/SwiftCharts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/SwiftCharts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/SwiftCharts.json
- [Swift Charts](https://developer.apple.com/documentation/Charts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Charts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Charts.json

## Code Snippets

### A scatterplot of a penguin's flipper length and weight — [2:03]

```swift
// A scatterplot of a penguin's flipper length and weight

import SwiftUI
import Charts

struct PenguinChart: View {
  var body: some View {
    Chart(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartXScale(domain: 160...240)
    .chartYScale(domain: 2...7)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### A scatterplot of a penguin's beak length and weight — [2:39]

```swift
// A scatterplot of a penguin's beak length and weight

import SwiftUI
import Charts

struct PenguinChart: View {
  var body: some View {
    Chart(penguins) { penguin in
      PointMark(
        x: .value("Beak Length", penguin.beakLength),
        y: .value("Weight", penguin.weight)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chartXAxisLabel("Beak Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartXScale(domain: 30...60)
    .chartYScale(domain: 2...7)
    .chartXAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### A scatterplot of a penguin's beak length and flipper length — [2:51]

```swift
// A scatterplot of a penguin's beak length and flipper length

import SwiftUI
import Charts

struct PenguinChart: View {
  var body: some View {
    Chart(penguins) { penguin in
      PointMark(
        x: .value("Beak Length", penguin.beakLength),
        y: .value("Flipper Length", penguin.flipperLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chartXAxisLabel("Beak Length (mm)")
    .chartYAxisLabel("Flipper Length (mm)")
    .chartXScale(domain: 30...60)
    .chartYScale(domain: 160...240)
    .chartXAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### A scatterplot of a penguin's flipper length, beak length, and weight — [3:28]

```swift
// A scatterplot of a penguin's flipper length, beak length, and weight

import SwiftUI
import Charts

struct PenguinChart: View {
  var body: some View {
    Chart3D(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight),
        z: .value("Beak Length", penguin.beakLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### A surface plot showing mathematical functions (x * z) — [5:19]

```swift
// A surface plot showing mathematical functions

import SwiftUI
import Charts

var SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        // (Double, Double) -> Double
        x * z
      }
    }
  }
}
```

### A surface plot showing mathematical functions — [5:43]

```swift
// A surface plot showing mathematical functions

import SwiftUI
import Charts

var SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        // (Double, Double) -> Double
        (sin(5 * x) + sin(5 * z)) / 2
      }
    }
  }
}
```

### A surface plot showing mathematical functions (-z) — [5:46]

```swift
// A surface plot showing mathematical functions

import SwiftUI
import Charts

var SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        // (Double, Double) -> Double
        -z
      }
    }
  }
}
```

### Present a linear regression of the penguin data — [6:19]

```swift
// Present a linear regression of the penguin data

import SwiftUI
import Charts
import CreateML
import TabularData

final class LinearRegression: Sendable {
  let regressor: MLLinearRegressor

  init<Data: RandomAccessCollection>(
    _ data: Data,
    x xPath: KeyPath<Data.Element, Double>,
    y yPath: KeyPath<Data.Element, Double>,
    z zPath: KeyPath<Data.Element, Double>
  ) {
    let x = Column(name: "X", contents: data.map { $0[keyPath: xPath] })
    let y = Column(name: "Y", contents: data.map { $0[keyPath: yPath] })
    let z = Column(name: "Z", contents: data.map { $0[keyPath: zPath] })
    let data = DataFrame(columns: [x, y, z].map { $0.eraseToAnyColumn() })
    regressor = try! MLLinearRegressor(trainingData: data, targetColumn: "Y")
  }

  func callAsFunction(_ x: Double, _ z: Double) -> Double {
    let x = Column(name: "X", contents: [x])
    let z = Column(name: "Z", contents: [z])
    let data = DataFrame(columns: [x, z].map { $0.eraseToAnyColumn() })
    return (try? regressor.predictions(from: data))?.first as? Double ?? .nan
  }
}

let linearRegression = LinearRegression(
  penguins,
  x: \.flipperLength,
  y: \.weight,
  z: \.beakLength
)

struct PenguinChart: some View {
  var body: some View {
    Chart3D {
      ForEach(penguins) { penguin in
        PointMark(
          x: .value("Flipper Length", penguin.flipperLength),
          y: .value("Weight", penguin.weight),
          z: .value("Beak Length", penguin.beakLength),
        )
        .foregroundStyle(by: .value("Species", penguin.species))
      }

      SurfacePlot(x: "Flipper Length", y: "Weight", z: "Beak Length") { flipperLength, beakLength in
        linearRegression(flipperLength, beakLength)
      }
      .foregroundStyle(.gray)
    }
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### Adjust the initial chart pose (Default) — [7:50]

```swift
// Adjust the initial chart pose

import SwiftUI
import Charts

struct PenguinChart: View {
  @State var pose: Chart3DPose = .default

  var body: some View {
    Chart3D(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight),
        z: .value("Beak Length", penguin.beakLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chart3DPose($pose)
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### Adjust the initial chart pose (Front) — [8:02]

```swift
// Adjust the initial chart pose

import SwiftUI
import Charts

struct PenguinChart: View {
  @State var pose: Chart3DPose = .front

  var body: some View {
    Chart3D(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight),
        z: .value("Beak Length", penguin.beakLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chart3DPose($pose)
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### Adjust the initial chart pose (Custom) — [8:09]

```swift
// Adjust the initial chart pose

import SwiftUI
import Charts

struct PenguinChart: View {
  @State var pose = Chart3DPose(
    azimuth: .degrees(20),
    inclination: .degrees(7)
  )

  var body: some View {
    Chart3D(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight),
        z: .value("Beak Length", penguin.beakLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chart3DPose($pose)
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### Adjust the initial chart pose and camera projection — [9:15]

```swift
// Adjust the initial chart pose and camera projection

import SwiftUI
import Charts

struct PenguinChart: View {
  @State var pose = Chart3DPose(
    azimuth: .degrees(20),
    inclination: .degrees(7)
  )

  var body: some View {
    Chart3D(penguins) { penguin in
      PointMark(
        x: .value("Flipper Length", penguin.flipperLength),
        y: .value("Weight", penguin.weight),
        z: .value("Beak Length", penguin.beakLength)
      )
      .foregroundStyle(by: .value("Species", penguin.species))
    }
    .chart3DPose($pose)
    .chart3DCameraProjection(.perspective)
    .chartXAxisLabel("Flipper Length (mm)")
    .chartYAxisLabel("Weight (kg)")
    .chartZAxisLabel("Beak Length (mm)")
    .chartXScale(domain: 160...240, range: -0.5...0.5)
    .chartYScale(domain: 2...7, range: -0.5...0.5)
    .chartZScale(domain: 30...60, range: -0.5...0.5)
    .chartXAxis {
      AxisMarks(values: [160, 180, 200, 220, 240]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartYAxis {
      AxisMarks(values: [2, 3, 4, 5, 6, 7]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
    .chartZAxis {
      AxisMarks(values: [30, 40, 50, 60]) {
        AxisTick()
        AxisGridLine()
        AxisValueLabel()
      }
    }
  }
}
```

### Customize the surface styles for a sinc function — [9:24]

```swift
// Customize the surface styles for a sinc function

import SwiftUI
import Charts

struct SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        let h = hypot(x, z)
        return sin(h) / h
      }
    }
    .chartXScale(domain: -10...10, range: -0.5...0.5)
    .chartZScale(domain: -10...10, range: -0.5...0.5)
    .chartYScale(domain: -0.23...1, range: -0.5...0.5)
  }
}
```

### Customize the surface styles for a sinc function (EllipticalGradient) — [9:29]

```swift
// Customize the surface styles for a sinc function

import SwiftUI
import Charts

struct SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        let h = hypot(x, z)
        return sin(h) / h
      }
      .foregroundStyle(EllipticalGradient(colors: [.red, .orange, .yellow, .green, .blue, .indigo, .purple]))
    }
    .chartXScale(domain: -10...10, range: -0.5...0.5)
    .chartZScale(domain: -10...10, range: -0.5...0.5)
    .chartYScale(domain: -0.23...1, range: -0.5...0.5)
  }
}
```

### Customize the surface styles for a sinc function (heightBased) — [9:38]

```swift
// Customize the surface styles for a sinc function

import SwiftUI
import Charts

struct SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        let h = hypot(x, z)
        return sin(h) / h
      }
      .foregroundStyle(.heightBased)
    }
    .chartXScale(domain: -10...10, range: -0.5...0.5)
    .chartZScale(domain: -10...10, range: -0.5...0.5)
    .chartYScale(domain: -0.23...1, range: -0.5...0.5)
  }
}
```

### Customize the surface styles for a sinc function (normalBased) — [9:47]

```swift
// Customize the surface styles for a sinc function

import SwiftUI
import Charts

struct SurfacePlotChart: View {
  var body: some View {
    Chart3D {
      SurfacePlot(x: "X", y: "Y", z: "Z") { x, z in
        let h = hypot(x, z)
        return sin(h) / h
      }
      .foregroundStyle(.normalBased)
    }
    .chartXScale(domain: -10...10, range: -0.5...0.5)
    .chartZScale(domain: -10...10, range: -0.5...0.5)
    .chartYScale(domain: -0.23...1, range: -0.5...0.5)
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/313/5/01490c3f-6737-43db-b2fb-f3ccfb1e824c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/313/5/01490c3f-6737-43db-b2fb-f3ccfb1e824c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/313) — developer.apple.com. Indexed for agent consumption._