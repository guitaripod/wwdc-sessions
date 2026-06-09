---
id: "wwdc2022-10137"
event: "wwdc2022"
year: 2022
title: "Swift Charts: Raise the bar "
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10137"
topics: ["Health & Fitness", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Swift Charts: Raise the bar 

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10137](https://developer.apple.com/videos/play/wwdc2022/10137)

Dive deep into data visualizations: Learn how Swift Charts and SwiftUI can help your apps represent complex datasets through a wide variety of chart options. We’ll show you how to plot different kinds of data and compose marks to create more elaborate charts. We’ll also take you through Swift Charts’ extensive chart customization API to help you match the style of your charts to your app.

To get the most out of this session, we recommend you begin with “Hello Swift Charts” from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,645 words)

## Documentation & Resources

- [Swift Charts](https://developer.apple.com/documentation/Charts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Charts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Charts.json
- [Creating a chart using Swift Charts](https://developer.apple.com/documentation/Charts/Creating-a-chart-using-Swift-Charts) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Charts/Creating-a-chart-using-Swift-Charts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Charts/Creating-a-chart-using-Swift-Charts.json
- [Visualizing your app’s data](https://developer.apple.com/documentation/Charts/visualizing-your-app-s-data) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Charts/visualizing-your-app-s-data
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Charts/visualizing-your-app-s-data.json

## Code Snippets

### Top style chart — [3:48]

```swift
import SwiftUI
import Charts

struct TopStyleChart: View {
    let data = [
        (name: "Cachapa", sales: 916),
        (name: "Injera", sales: 850),
        (name: "Crêpe", sales: 802),
        (name: "Jian Bing", sales: 753),
        (name: "Dosa", sales: 654),
        (name: "American", sales: 618)
    ]

    var body: some View {
        Chart(data, id: \.name) {
            BarMark(
                x: .value("Sales", $0.sales),
                y: .value("Name", $0.name)
            )
            // Set the foreground style of the bars.
            .foregroundStyle(.pink)
            // Customize the accessibility label and value.
            .accessibilityLabel($0.name)
            .accessibilityValue("\($0.sales) sold")
        }
    }
}
```

### Daily sales chart — [5:12]

```swift
struct DailySalesChart: View {
    var body: some View {
        Chart {
            ForEach(dailySales, id: \.day) {
                // Try change to LineMark.
                BarMark( 
                    x: .value("Day", $0.day, unit: .day),
                    y: .value("Sales", $0.sales)
                )
            }
        }
    }

    let dailySales: [(day: Date, sales: Int)] = [
        (day: date(year: 2022, month: 5, day: 8), sales: 168),
        (day: date(year: 2022, month: 5, day: 9), sales: 117),
        (day: date(year: 2022, month: 5, day: 10), sales: 106),
        (day: date(year: 2022, month: 5, day: 11), sales: 119),
        (day: date(year: 2022, month: 5, day: 12), sales: 109),
        (day: date(year: 2022, month: 5, day: 13), sales: 104),
        (day: date(year: 2022, month: 5, day: 14), sales: 196),
        (day: date(year: 2022, month: 5, day: 15), sales: 172),
        (day: date(year: 2022, month: 5, day: 16), sales: 122),
        (day: date(year: 2022, month: 5, day: 17), sales: 115),
        (day: date(year: 2022, month: 5, day: 18), sales: 138),
        (day: date(year: 2022, month: 5, day: 19), sales: 110),
        (day: date(year: 2022, month: 5, day: 20), sales: 106),
        (day: date(year: 2022, month: 5, day: 21), sales: 187),
        (day: date(year: 2022, month: 5, day: 22), sales: 187),
        (day: date(year: 2022, month: 5, day: 23), sales: 119),
        (day: date(year: 2022, month: 5, day: 24), sales: 160),
        (day: date(year: 2022, month: 5, day: 25), sales: 144),
        (day: date(year: 2022, month: 5, day: 26), sales: 152),
        (day: date(year: 2022, month: 5, day: 27), sales: 148),
        (day: date(year: 2022, month: 5, day: 28), sales: 240),
        (day: date(year: 2022, month: 5, day: 29), sales: 242),
        (day: date(year: 2022, month: 5, day: 30), sales: 173),
        (day: date(year: 2022, month: 5, day: 31), sales: 143),
        (day: date(year: 2022, month: 6, day: 1), sales: 137),
        (day: date(year: 2022, month: 6, day: 2), sales: 123),
        (day: date(year: 2022, month: 6, day: 3), sales: 146),
        (day: date(year: 2022, month: 6, day: 4), sales: 214),
        (day: date(year: 2022, month: 6, day: 5), sales: 250),
        (day: date(year: 2022, month: 6, day: 6), sales: 146)
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: .init(year: year, month: month, day: day)) ?? Date()
}
```

### Sales by location with line mark — [6:16]

```swift
struct LocationsChart: View {
    var body: some View {
        Chart {
            ForEach(seriesData, id: \.city) { series in
                ForEach(series.data, id: \.weekday) {
                    LineMark(
                        x: .value("Weekday", $0.weekday, unit: .day),
                        y: .value("Sales", $0.sales)
                    )
                }
                .foregroundStyle(by: .value("City", series.city))
                .symbol(by: .value("City", series.city))
                .interpolationMethod(.catmullRom)
            }
        }
    }

    let seriesData = [
        (
            city: "Cupertino", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 54),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 88),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 49),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 125),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 67)
            ]
        ),
        (
            city: "San Francisco", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 81),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 90),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 52),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 72),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 137)
            ]
        )
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Sales by location with bar mark — [7:19]

```swift
struct LocationsChart: View {
    var body: some View {
        Chart {
            ForEach(seriesData, id: \.city) { series in
                ForEach(series.data, id: \.weekday) {
                    BarMark(
                        x: .value("Weekday", $0.weekday, unit: .day),
                        y: .value("Sales", $0.sales)
                    )
                }
                .foregroundStyle(by: .value("City", series.city))
                .position(by: .value("City", series.city))
            }
        }
    }

    let seriesData = [
        (
            city: "Cupertino", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 54),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 88),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 49),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 125),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 67)
            ]
        ),
        (
            city: "San Francisco", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 81),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 90),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 52),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 72),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 137)
            ]
        )
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Monthly sales with line and area marks — [8:02]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart {
            ForEach(data, id: \.month) {
                AreaMark(
                    x: .value("Month", $0.month, unit: .month),
                    yStart: .value("Daily Min", $0.dailyMin),
                    yEnd: .value("Daily Max", $0.dailyMax)
                )
                .opacity(0.3)
                LineMark(
                    x: .value("Month", $0.month, unit: .month),
                    y: .value("Daily Average", $0.dailyAverage)
                )
            }
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952, dailyAverage: 127, dailyMin: 95, dailyMax: 194),
        (month: date(year: 2021, month: 8), sales: 4044, dailyAverage: 130, dailyMin: 96, dailyMax: 189),
        (month: date(year: 2021, month: 9), sales: 3930, dailyAverage: 131, dailyMin: 101, dailyMax: 184),
        (month: date(year: 2021, month: 10), sales: 4217, dailyAverage: 136, dailyMin: 96, dailyMax: 193),
        (month: date(year: 2021, month: 11), sales: 4006, dailyAverage: 134, dailyMin: 104, dailyMax: 202),
        (month: date(year: 2021, month: 12), sales: 3994, dailyAverage: 129, dailyMin: 96, dailyMax: 190),
        (month: date(year: 2022, month: 1), sales: 4202, dailyAverage: 136, dailyMin: 96, dailyMax: 203),
        (month: date(year: 2022, month: 2), sales: 3749, dailyAverage: 134, dailyMin: 98, dailyMax: 200),
        (month: date(year: 2022, month: 3), sales: 4329, dailyAverage: 140, dailyMin: 104, dailyMax: 218),
        (month: date(year: 2022, month: 4), sales: 4084, dailyAverage: 136, dailyMin: 93, dailyMax: 221),
        (month: date(year: 2022, month: 5), sales: 4559, dailyAverage: 147, dailyMin: 104, dailyMax: 242),
        (month: date(year: 2022, month: 6), sales: 1023, dailyAverage: 170, dailyMin: 120, dailyMax: 250)
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Monthly sales with bar and rectangle marks — [8:46]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart {
            ForEach(data, id: \.month) {
                BarMark(
                    x: .value("Month", $0.month, unit: .month),
                    yStart: .value("Daily Min", $0.dailyMin),
                    yEnd: .value("Daily Max", $0.dailyMax),
                    width: .ratio(0.6)
                )
                .opacity(0.3)
                RectangleMark(
                    x: .value("Month", $0.month, unit: .month),
                    y: .value("Daily Average", $0.dailyAverage),
                    width: .ratio(0.6),
                    height: 2
                )
            }
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952, dailyAverage: 127, dailyMin: 95, dailyMax: 194),
        (month: date(year: 2021, month: 8), sales: 4044, dailyAverage: 130, dailyMin: 96, dailyMax: 189),
        (month: date(year: 2021, month: 9), sales: 3930, dailyAverage: 131, dailyMin: 101, dailyMax: 184),
        (month: date(year: 2021, month: 10), sales: 4217, dailyAverage: 136, dailyMin: 96, dailyMax: 193),
        (month: date(year: 2021, month: 11), sales: 4006, dailyAverage: 134, dailyMin: 104, dailyMax: 202),
        (month: date(year: 2021, month: 12), sales: 3994, dailyAverage: 129, dailyMin: 96, dailyMax: 190),
        (month: date(year: 2022, month: 1), sales: 4202, dailyAverage: 136, dailyMin: 96, dailyMax: 203),
        (month: date(year: 2022, month: 2), sales: 3749, dailyAverage: 134, dailyMin: 98, dailyMax: 200),
        (month: date(year: 2022, month: 3), sales: 4329, dailyAverage: 140, dailyMin: 104, dailyMax: 218),
        (month: date(year: 2022, month: 4), sales: 4084, dailyAverage: 136, dailyMin: 93, dailyMax: 221),
        (month: date(year: 2022, month: 5), sales: 4559, dailyAverage: 147, dailyMin: 104, dailyMax: 242),
        (month: date(year: 2022, month: 6), sales: 1023, dailyAverage: 170, dailyMin: 120, dailyMax: 250)
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Monthly sales with average line and annotation — [9:19]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart {
            ForEach(data, id: \.month) {
                BarMark(
                    x: .value("Month", $0.month, unit: .month),
                    yStart: .value("Daily Min", $0.dailyMin),
                    yEnd: .value("Daily Max", $0.dailyMax),
                    width: .ratio(0.6)
                )
                .opacity(0.3)
                RectangleMark(
                    x: .value("Month", $0.month, unit: .month),
                    y: .value("Daily Average", $0.dailyAverage),
                    width: .ratio(0.6),
                    height: 2
                )
            }
            .foregroundStyle(.gray.opacity(0.5))

            RuleMark(
                y: .value("Average", averageValue)
            )
            .lineStyle(StrokeStyle(lineWidth: 3))
            .annotation(position: .top, alignment: .leading) {
                Text("Average: \(averageValue, format: .number)")
                    .font(.headline)
                    .foregroundStyle(.blue)
            }
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952, dailyAverage: 127, dailyMin: 95, dailyMax: 194),
        (month: date(year: 2021, month: 8), sales: 4044, dailyAverage: 130, dailyMin: 96, dailyMax: 189),
        (month: date(year: 2021, month: 9), sales: 3930, dailyAverage: 131, dailyMin: 101, dailyMax: 184),
        (month: date(year: 2021, month: 10), sales: 4217, dailyAverage: 136, dailyMin: 96, dailyMax: 193),
        (month: date(year: 2021, month: 11), sales: 4006, dailyAverage: 134, dailyMin: 104, dailyMax: 202),
        (month: date(year: 2021, month: 12), sales: 3994, dailyAverage: 129, dailyMin: 96, dailyMax: 190),
        (month: date(year: 2022, month: 1), sales: 4202, dailyAverage: 136, dailyMin: 96, dailyMax: 203),
        (month: date(year: 2022, month: 2), sales: 3749, dailyAverage: 134, dailyMin: 98, dailyMax: 200),
        (month: date(year: 2022, month: 3), sales: 4329, dailyAverage: 140, dailyMin: 104, dailyMax: 218),
        (month: date(year: 2022, month: 4), sales: 4084, dailyAverage: 136, dailyMin: 93, dailyMax: 221),
        (month: date(year: 2022, month: 5), sales: 4559, dailyAverage: 147, dailyMin: 104, dailyMax: 242),
        (month: date(year: 2022, month: 6), sales: 1023, dailyAverage: 170, dailyMin: 120, dailyMax: 250)
    ]

    let averageValue = 137
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Chart with custom scales for Y and foreground style — [13:54]

```swift
struct LocationsChart: View {
    var body: some View {
        Chart {
            ForEach(seriesData, id: \.city) { series in
                ForEach(series.data, id: \.weekday) {
                    LineMark(
                        x: .value("Weekday", $0.weekday, unit: .day),
                        y: .value("Sales", $0.sales)
                    )
                }
                .foregroundStyle(by: .value("City", series.city))
                .symbol(by: .value("City", series.city))
                .interpolationMethod(.catmullRom)
            }
        }
        .chartYScale(domain: 0 ... 200)
        .chartForegroundStyleScale([
            "San Francisco": .orange,
            "Cupertino": .pink
        ])
    }

    let seriesData = [
        (
            city: "Cupertino", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 54),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 88),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 49),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 42),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 125),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 67)
            ]
        ),
        (
            city: "San Francisco", data: [
                (weekday: date(year: 2022, month: 5, day: 2), sales: 81),
                (weekday: date(year: 2022, month: 5, day: 3), sales: 90),
                (weekday: date(year: 2022, month: 5, day: 4), sales: 52),
                (weekday: date(year: 2022, month: 5, day: 5), sales: 72),
                (weekday: date(year: 2022, month: 5, day: 6), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 7), sales: 84),
                (weekday: date(year: 2022, month: 5, day: 8), sales: 137)
            ]
        )
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Chart with custom X axis — [15:16]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart(data, id: \.month) {
            BarMark(
                x: .value("Month", $0.month, unit: .month),
                y: .value("Sales", $0.sales)
            )
        }
        .chartXAxis {
            AxisMarks( values: .stride(by: .month) ) { value in
                AxisGridLine()
                AxisTick()
                AxisValueLabel(
                    format: .dateTime.month(.narrow)
                )
            }
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952),
        (month: date(year: 2021, month: 8), sales: 4044),
        (month: date(year: 2021, month: 9), sales: 3930),
        (month: date(year: 2021, month: 10), sales: 4217),
        (month: date(year: 2021, month: 11), sales: 4006),
        (month: date(year: 2021, month: 12), sales: 3994),
        (month: date(year: 2022, month: 1), sales: 4202),
        (month: date(year: 2022, month: 2), sales: 3749),
        (month: date(year: 2022, month: 3), sales: 4329),
        (month: date(year: 2022, month: 4), sales: 4084),
        (month: date(year: 2022, month: 5), sales: 4559),
        (month: date(year: 2022, month: 6), sales: 1023)
    ]

    let averageValue = 137
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Chart with custom X axis and conditional content for axis marks — [16:17]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart(data, id: \.month) {
            BarMark(
                x: .value("Month", $0.month, unit: .month),
                y: .value("Sales", $0.sales)
            )
        }
        .chartXAxis {
            AxisMarks(values: .stride(by: .month)) { value in
                if value.as(Date.self)!.isFirstMonthOfQuarter {
                    AxisGridLine().foregroundStyle(.black)
                    AxisTick().foregroundStyle(.black)
                    AxisValueLabel(
                        format: .dateTime.month(.narrow)
                    )
                } else {
                    AxisGridLine()
                }
            }
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952),
        (month: date(year: 2021, month: 8), sales: 4044),
        (month: date(year: 2021, month: 9), sales: 3930),
        (month: date(year: 2021, month: 10), sales: 4217),
        (month: date(year: 2021, month: 11), sales: 4006),
        (month: date(year: 2021, month: 12), sales: 3994),
        (month: date(year: 2022, month: 1), sales: 4202),
        (month: date(year: 2022, month: 2), sales: 3749),
        (month: date(year: 2022, month: 3), sales: 4329),
        (month: date(year: 2022, month: 4), sales: 4084),
        (month: date(year: 2022, month: 5), sales: 4559),
        (month: date(year: 2022, month: 6), sales: 1023)
    ]

    let averageValue = 137
}

extension Date {
    var isFirstMonthOfQuarter: Bool {
        Calendar.current.component(.month, from: self) % 3 == 1
    }
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Chart with custom Y axis — [17:00]

```swift
struct MonthlySalesChart: View {
    var body: some View {
        Chart(data, id: \.month) {
            BarMark(
                x: .value("Month", $0.month, unit: .month),
                y: .value("Sales", $0.sales)
            )
        }
        .chartYAxis {
            AxisMarks( preset: .extended, position: .leading)
        }
    }

    let data = [
        (month: date(year: 2021, month: 7), sales: 3952),
        (month: date(year: 2021, month: 8), sales: 4044),
        (month: date(year: 2021, month: 9), sales: 3930),
        (month: date(year: 2021, month: 10), sales: 4217),
        (month: date(year: 2021, month: 11), sales: 4006),
        (month: date(year: 2021, month: 12), sales: 3994),
        (month: date(year: 2022, month: 1), sales: 4202),
        (month: date(year: 2022, month: 2), sales: 3749),
        (month: date(year: 2022, month: 3), sales: 4329),
        (month: date(year: 2022, month: 4), sales: 4084),
        (month: date(year: 2022, month: 5), sales: 4559),
        (month: date(year: 2022, month: 6), sales: 1023)
    ]

    let averageValue = 137
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

### Chart with plot area style — [18:26]

```swift
struct TopStyleChart: View {
    var body: some View {
        Chart(data, id: \.name) {
            BarMark(
                x: .value("Sales", $0.sales),
                y: .value("Name", $0.name)
            )
            // Set the foreground style of the bars.
            .foregroundStyle(.pink)
            // Customize the accessibility label and value.
            .accessibilityLabel($0.name)
            .accessibilityValue("\($0.sales) sold")
        }
        .chartPlotStyle { plotArea in
            plotArea.frame(height: 60 * 6)
                    .background(.pink.opacity(0.2))
                    .border(.pink, width: 1)
        }
    }

    let data = [
        (name: "Cachapa", sales: 916),
        (name: "Injera", sales: 850),
        (name: "Crêpe", sales: 802),
        (name: "Jian Bing", sales: 753),
        (name: "Dosa", sales: 654),
        (name: "American", sales: 618)
    ]
}
```

### Chart with brushing interaction — [20:03]

```swift
struct InteractiveBrushingChart: View {
    @State var range: (Date, Date)? = nil

    var body: some View {
        Chart {
            ForEach(data, id: \.day) {
                LineMark(
                    x: .value("Month", $0.day, unit: .day),
                    y: .value("Sales", $0.sales)
                )
                .interpolationMethod(.catmullRom)
                .symbol(Circle().strokeBorder(lineWidth: 2))
            }
            if let (start, end) = range {
                RectangleMark(
                    xStart: .value("Selection Start", start),
                    xEnd: .value("Selection End", end)
                )
                .foregroundStyle(.gray.opacity(0.2))
            }
        }
        .chartOverlay { proxy in
            GeometryReader { nthGeoItem in
                Rectangle().fill(.clear).contentShape(Rectangle())
                    .gesture(DragGesture()
                        .onChanged { value in
                            // Find the x-coordinates in the chart’s plot area.
                            let xStart = value.startLocation.x - nthGeoItem[proxy.plotAreaFrame].origin.x
                            let xCurrent = value.location.x - nthGeoItem[proxy.plotAreaFrame].origin.x
                            // Find the date values at the x-coordinates.
                            if let dateStart: Date = proxy.value(atX: xStart),
                               let dateCurrent: Date = proxy.value(atX: xCurrent) {
                                range = (dateStart, dateCurrent)
                            }
                        }
                        .onEnded { _ in range = nil } // Clear the state on gesture end.
                    )
            }
        }
    }

    let data: [(day: Date, sales: Int)] = [
        (day: date(year: 2022, month: 5, day: 8), sales: 168),
        (day: date(year: 2022, month: 5, day: 9), sales: 117),
        (day: date(year: 2022, month: 5, day: 10), sales: 106),
        (day: date(year: 2022, month: 5, day: 11), sales: 119),
        (day: date(year: 2022, month: 5, day: 12), sales: 109),
        (day: date(year: 2022, month: 5, day: 13), sales: 104),
        (day: date(year: 2022, month: 5, day: 14), sales: 196),
        (day: date(year: 2022, month: 5, day: 15), sales: 172),
        (day: date(year: 2022, month: 5, day: 16), sales: 122),
        (day: date(year: 2022, month: 5, day: 17), sales: 115),
        (day: date(year: 2022, month: 5, day: 18), sales: 138),
        (day: date(year: 2022, month: 5, day: 19), sales: 110),
        (day: date(year: 2022, month: 5, day: 20), sales: 106),
        (day: date(year: 2022, month: 5, day: 21), sales: 187),
        (day: date(year: 2022, month: 5, day: 22), sales: 187),
        (day: date(year: 2022, month: 5, day: 23), sales: 119),
        (day: date(year: 2022, month: 5, day: 24), sales: 160),
        (day: date(year: 2022, month: 5, day: 25), sales: 144),
        (day: date(year: 2022, month: 5, day: 26), sales: 152),
        (day: date(year: 2022, month: 5, day: 27), sales: 148),
        (day: date(year: 2022, month: 5, day: 28), sales: 240),
        (day: date(year: 2022, month: 5, day: 29), sales: 242),
        (day: date(year: 2022, month: 5, day: 30), sales: 173),
        (day: date(year: 2022, month: 5, day: 31), sales: 143),
        (day: date(year: 2022, month: 6, day: 1), sales: 137),
        (day: date(year: 2022, month: 6, day: 2), sales: 123),
        (day: date(year: 2022, month: 6, day: 3), sales: 146),
        (day: date(year: 2022, month: 6, day: 4), sales: 214),
        (day: date(year: 2022, month: 6, day: 5), sales: 250),
        (day: date(year: 2022, month: 6, day: 6), sales: 146)
    ]
}

func date(year: Int, month: Int, day: Int = 1) -> Date {
    Calendar.current.date(from: DateComponents(year: year, month: month, day: day)) ?? Date()
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10137/3/AB0A9BA9-E0B1-440B-98E6-E9C8A395FF34/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10137/3/AB0A9BA9-E0B1-440B-98E6-E9C8A395FF34/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10137) — developer.apple.com. Indexed for agent consumption._