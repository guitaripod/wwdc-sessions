---
id: "wwdc2022-10133"
event: "wwdc2022"
year: 2022
title: "Build a productivity app for Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10133"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Build a productivity app for Apple Watch

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10133](https://developer.apple.com/videos/play/wwdc2022/10133)

Your wrist has never been more productive. Discover how you can use SwiftUI and system features to build a great productivity app for Apple Watch. We’ll show you how you can design great work experiences for the wrist, and explore how you can get text input, display a basic chart, and share content with friends.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,481 words)

## Documentation & Resources

- [Building a productivity app for Apple Watch](https://developer.apple.com/documentation/watchOS-Apps/building-a-productivity-app-for-apple-watch) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/building-a-productivity-app-for-apple-watch
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/building-a-productivity-app-for-apple-watch.json
- [watchOS apps](https://developer.apple.com/documentation/watchOS-Apps) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps.json

## Code Snippets

### Initial ListItem struct — [6:12]

```swift
struct ListItem: Identifiable, Hashable {

    let id = UUID()
    var description: String

    init(_ description: String) {
        self.description = description
    }
}
```

### ItemListModel — [6:24]

```swift
class ItemListModel: NSObject, ObservableObject {
    @Published var items = [ListItem]()
}
```

### Add the ItemListModel as an EnvironmentObject — [6:30]

```swift
@main
struct WatchTaskListSampleApp: App {

    @StateObject var itemListModel = ItemListModel()

    @SceneBuilder var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(itemListModel)
        }
    }
}
```

### Create a simple SwiftUI List — [6:37]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        List {
            ForEach($model.items) { $item in
                ItemRow(item: $item)
            }

            if model.items.isEmpty {
                Text("No items to do!")
                    .foregroundStyle(.gray)
            }
        }
        .navigationTitle("Tasks")
    }
}
```

### TextFieldLink with a simple String — [7:11]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        VStack {
            TextFieldLink("Add") {
                model.items.append(ListItem($0))
            }
        }
        .navigationTitle("Tasks")
    }
}
```

### TextFieldLink with a Label — [7:16]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        VStack {
            TextFieldLink {
                Label(
                    "Add", 
                    systemImage: "plus.circle.fill")
            } onSubmit: {
                model.items.append(ListItem($0))
            }
        }
        .navigationTitle("Tasks")
    }
}
```

### TextFieldLink with foregroundStyle modifier — [7:20]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        VStack {
            TextFieldLink {
                Label(
                    "Add", 
                    systemImage: "plus.circle.fill")
            } onSubmit: {
                model.items.append(ListItem($0))
            }
            .foregroundStyle(.tint)
        }
        .navigationTitle("Tasks")
    }
}
```

### TextFieldLink with buttonStyle modifier — [7:27]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        VStack {
            TextFieldLink {
                Label(
                    "Add", 
                    systemImage: "plus.circle.fill")
            } onSubmit: {
                model.items.append(ListItem($0))
            }
            .buttonStyle(.borderedProminent)
        }
        .navigationTitle("Tasks")
    }
}
```

### Create the AddItemLink View to encapsulate the style and behavior of the TextFieldLink to add list items — [7:30]

```swift
struct AddItemLink: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        TextFieldLink(prompt: Text("New Item")) {
            Label("Add",
                  systemImage: "plus.circle.fill")
        } onSubmit: {
            model.items.append(ListItem($0))
        } 
    }
}
```

### Add a toolbar item to allow people to add new list items — [8:38]

```swift
struct ContentView: View {
    @EnvironmentObject private var model: ItemListModel

    var body: some View {
        List {
            ForEach($model.items) { $item in
                ItemRow(item: $item)
            }

            if model.items.isEmpty {
                Text("No items to do!")
                    .foregroundStyle(.gray)
            }
        }
        .toolbar {
            AddItemLink()
        }
        .navigationTitle("Tasks")
    }
}
```

### Display a modal sheet — [11:40]

```swift
struct ItemRow: View {
    @EnvironmentObject private var model: ItemListModel

    @Binding var item: ListItem
    @State private var showDetail = false

    var body: some View {
        Button {
            showDetail = true
        } label: {
            HStack {
                Text(item.description)
                    .strikethrough(item.isComplete)
                Spacer()
                Image(systemName: "checkmark").opacity(item.isComplete ? 100 : 0)
            }
        }
        .sheet(isPresented: $showDetail) {
            ItemDetail(item: $item)
        }
    }
}
```

### Display a modal sheet with custom toolbar items — [11:58]

```swift
struct ItemRow: View {
    @EnvironmentObject private var model: ItemListModel

    @Binding var item: ListItem
    @State private var showDetail = false

    var body: some View {
        Button {
            showDetail = true
        } label: {
            HStack {
                Text(item.description)
                    .strikethrough(item.isComplete)
                Spacer()
                Image(systemName: "checkmark").opacity(item.isComplete ? 100 : 0)
            }
        }
        .sheet(isPresented: $showDetail) {
            ItemDetail(item: $item)
                .toolbar {
                    ToolbarItem(placement: .confirmationAction) {
                        Button("Done") {
                            showDetail = false
                        }
                    }
                }
        }
    }
}
```

### Add more properties to the ListItem — [12:36]

```swift
struct ListItem: Identifiable, Hashable {

    let id = UUID()
    var description: String
    var estimatedWork: Double = 1.0
    var creationDate = Date()
    var completionDate: Date?

    init(_ description: String) {
        self.description = description
    }

    var isComplete: Bool {
        get {
            completionDate != nil
        }
        set {
            if newValue {
                guard completionDate == nil else { return }
                completionDate = Date()
            } else {
                completionDate = nil
            }
        }
    }
}
```

### Create the ItemDetail View with the Stepper — [12:48]

```swift
struct ItemDetail: View {
    @Binding var item: ListItem

    var body: some View {
        Form {
            Section("List Item") {
                TextField("Item", text: $item.description, prompt: Text("List Item"))
            }
            Section("Estimated Work") {
                Stepper(value: $item.estimatedWork,
                        in: (0.0...14.0),
                        step: 0.5,
                        format: .number) {
                    Text("\(item.estimatedWork, specifier: "%.1f") days")
                }
            }

            Toggle(isOn: $item.isComplete) {
                Text("Completed")
            }
        }
    }
}
```

### A Stepper with Emoji — [13:29]

```swift
// Use a Stepper to edit the stress level of an item
struct StressStepper: View {
    private let stressLevels = [
        "😱", "😡", "😳", "🙁", "🫤", "🙂", "🥳"
    ]
    @State private var stressLevelIndex = 5

    var body: some View {
        VStack {
            Text("Stress Level")
                .font(.system(.footnote, weight: .bold))
                .foregroundStyle(.tint)

            Stepper(value: $stressLevelIndex,
                    in: (0...stressLevels.count-1)) {
                Text(stressLevels[stressLevelIndex])
            }
        }
    }
}
```

### Add a ShareLink to the ItemDetail View — [14:43]

```swift
struct ItemDetail: View {
    @Binding var item: ListItem

    var body: some View {
        Form {
            Section("List Item") {
                TextField("Item", text: $item.description, prompt: Text("List Item"))
            }
            Section("Estimated Work") {
                Stepper(value: $item.estimatedWork,
                        in: (0.0...14.0),
                        step: 0.5,
                        format: .number) {
                    Text("\(item.estimatedWork, specifier: "%.1f") days")
                }
            }

            Toggle(isOn: $item.isComplete) {
                Text("Completed")
            }

            ShareLink(item: item.description,
                      subject: Text("Please help!"),
                      message: Text("(I need some help finishing this.)"),
                      preview: SharePreview("\(item.description)"))
            .buttonStyle(.borderedProminent)
            .buttonBorderShape(.roundedRectangle)
            .listRowInsets(
                EdgeInsets(top: 0, leading: 0, bottom: 0, trailing: 0)
            )
        }
    }
}
```

### Page-style TabView with navigation titles for each page — [16:39]

```swift
struct ContentView: View {
    var body: some View {
        TabView {
            NavigationStack {
                ItemList()
            }
            NavigationStack {
                ProductivityChart()
            }
        }.tabViewStyle(.page)
    }
}
```

### ChartData struct for aggregate data — [17:20]

```swift
/// Aggregate data for charting productivity.
struct ChartData {
    struct DataElement: Identifiable {
        var id: Date { return date }
        let date: Date
        let itemsComplete: Double
    }

    /// Create aggregate chart data from list items.
    /// - Parameter items: An array of list items to aggregate for charting.
    /// - Returns: The chart data source.
    static func createData(_ items: [ListItem]) -> [DataElement] {
        return Dictionary(grouping: items, by: \.completionDate)
            .compactMap {
                guard let date = $0 else { return nil }
                return DataElement(date: date, itemsComplete: Double($1.count))
            }
            .sorted {
                $0.date < $1.date
            }
    }
}
```

### Static sample data for chart and basic bar chart — [17:36]

```swift
extension ChartData {

    /// Some static sample data for displaying a `Chart`.
    static var chartSampleData: [DataElement] {
        let calendar = Calendar.autoupdatingCurrent
        var startDateComponents = calendar.dateComponents(
            [.year, .month, .day], from: Date())
        startDateComponents.setValue(22, for: .day)
        startDateComponents.setValue(5, for: .month)
        startDateComponents.setValue(2022, for: .year)
        startDateComponents.setValue(0, for: .hour)
        startDateComponents.setValue(0, for: .minute)
        startDateComponents.setValue(0, for: .second)
        let startDate = calendar.date(from: startDateComponents)!

        let itemsToAdd = [
            6, 3, 1, 4, 1, 2, 7,
            5, 2, 0, 5, 2, 3, 9
        ]
        var items = [DataElement]()
        for dayOffset in (0..<itemsToAdd.count) {
            items.append(DataElement(
                date: calendar.date(byAdding: .day, value: dayOffset, to: startDate)!,
                itemsComplete: Double(itemsToAdd[dayOffset])))
        }

        return items
    }
}

struct ProductivityChart: View {

    let data = ChartData.createData(
        ListItem.chartSampleData)

    var body: some View {
        Chart(data) { dataPoint in
            BarMark(
                x: .value("Date", dataPoint.date),
                y: .value(
                    “Completed", 
                    dataPoint.itemsComplete)
            )
            .foregroundStyle(Color.accentColor)
        }
        .navigationTitle("Productivity")
        .navigationBarTitleDisplayMode(.inline)
    }
}
```

### Chart with chartXAxis modifier — [17:50]

```swift
struct ProductivityChart: View {

    let data = ChartData.createData(
        ListItem.chartSampleData)

    private var shortDateFormatStyle = DateFormatStyle(dateFormatTemplate: "Md")

    var body: some View {
        Chart(data) { dataPoint in
            BarMark(
                x: .value("Date", dataPoint.date),
                y: .value(
                    “Completed", 
                    dataPoint.itemsComplete)
            )
            .foregroundStyle(Color.accentColor)
        }
      	.chartXAxis {
            AxisMarks(format: shortDateFormatStyle)
        }
        .navigationTitle("Productivity")
        .navigationBarTitleDisplayMode(.inline)
    }
}

/// `ProductivityChart` uses this type to format the dates on the x-axis.
struct DateFormatStyle: FormatStyle {
    enum CodingKeys: CodingKey {
        case dateFormatTemplate
    }

    private var dateFormatTemplate: String
    private var formatter: DateFormatter

    init(dateFormatTemplate: String) {
        self.dateFormatTemplate = dateFormatTemplate
        formatter = DateFormatter()
        formatter.locale = Locale.autoupdatingCurrent
        formatter.setLocalizedDateFormatFromTemplate(dateFormatTemplate)
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        dateFormatTemplate = try container.decode(String.self, forKey: .dateFormatTemplate)
        formatter = DateFormatter()
        formatter.setLocalizedDateFormatFromTemplate(dateFormatTemplate)
    }

    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(dateFormatTemplate, forKey: .dateFormatTemplate)
    }

    func format(_ value: Date) -> String {
        formatter.string(from: value)
    }
}
```

### Add the digitalCrownRotation modifier — [19:05]

```swift
struct ProductivityChart: View {

    let data = ChartData.createData(
        ListItem.chartSampleData)

    /// The index of the highlighted chart value. This is for crown scrolling.
    @State private var highlightedDateIndex: Int = 0

    /// The current offset of the crown while it's rotating. This sample sets the offset with
    /// the value in the DigitalCrownEvent and uses it to show an intermediate
    /// (between detents) chart value in the view.
    @State private var crownOffset: Double = 0.0

    @State private var isCrownIdle = true

    private var chart: some View {
        Chart(data) { dataPoint in
            BarMark(
                x: .value("Date", dataPoint.date),
                y: .value(
                    “Completed", 
                    dataPoint.itemsComplete)
            )
            .foregroundStyle(Color.accentColor)
        }
      	.chartXAxis {
            AxisMarks(format: shortDateFormatStyle)
        }
    }

    var body: some View {
        chart
            .focusable()
            .digitalCrownRotation(
                detent: $highlightedDateIndex,
                from: 0,
                through: data.count - 1,
                by: 1,
                sensitivity: .medium
            ) { crownEvent in
                isCrownIdle = false
                crownOffset = crownEvent.offset
            } onIdle: {
                isCrownIdle = true
            }
            .navigationTitle("Productivity")
            .navigationBarTitleDisplayMode(.inline)
    }
}
```

### Add a RuleMark to the Chart to show the current Digital Crown position — [21:07]

```swift
/// The date value that corresponds to the crown offset.
private var crownOffsetDate: Date {
    let dateDistance = data[0].date.distance(
        to: data[data.count - 1].date) * (crownOffset / Double(data.count - 1))
    return data[0].date.addingTimeInterval(dateDistance)
}

private var chart: some View {
    Chart(data) { dataPoint in
        BarMark(
            x: .value("Date", dataPoint.date),
            y: .value(
                "Completed", 
                dataPoint.itemsComplete)
        )
        .foregroundStyle(Color.accentColor)

        RuleMark(x: .value("Date", crownOffsetDate))
            .foregroundStyle(Color.appYellow)
    }
    .chartXAxis {
        AxisMarks(format: shortDateFormatStyle)
    }
}
```

### Add animation to dim the crown position line when the scrolling idle state changes — [21:37]

```swift
struct ProductivityChart: View {

    let data = ChartData.createData(
        ListItem.chartSampleData)

    /// The index of the highlighted chart value. This is for crown scrolling.
    @State private var highlightedDateIndex: Int = 0

    /// The current offset of the crown while it's rotating. This sample sets the offset with
    /// the value in the DigitalCrownEvent and uses it to show an intermediate
    /// (between detents) chart value in the view.
    @State private var crownOffset: Double = 0.0

    @State private var isCrownIdle = true

    @State var crownPositionOpacity: CGFloat = 0.2

    private var chart: some View {
        Chart(data) { dataPoint in
            BarMark(
                x: .value("Date", dataPoint.date),
                y: .value(
                    “Completed", 
                    dataPoint.itemsComplete)
            )
            .foregroundStyle(Color.accentColor)

            RuleMark(x: .value("Date", crownOffsetDate))
                .foregroundStyle(Color.appYellow.opacity(crownPositionOpacity))
        }
      	.chartXAxis {
            AxisMarks(format: shortDateFormatStyle)
        }
    }

    var body: some View {
        chart
            .focusable()
            .digitalCrownRotation(
                detent: $highlightedDateIndex,
                from: 0,
                through: data.count - 1,
                by: 1,
                sensitivity: .medium
            ) { crownEvent in
                isCrownIdle = false
                crownOffset = crownEvent.offset
            } onIdle: {
                isCrownIdle = true
            }
            .onChange(of: isCrownIdle) { newValue in
                withAnimation(newValue ? .easeOut : .easeIn) {
                    crownPositionOpacity = newValue ? 0.2 : 1.0
                }
            }
            .navigationTitle("Productivity")
            .navigationBarTitleDisplayMode(.inline)
    }
}
```

### Add an annotation to the bar chart to display the current value — [22:14]

```swift
private func isLastDataPoint(_ dataPoint: ChartData.DataElement) -> Bool {
    data[chartDataRange.upperBound].id == dataPoint.id
}

private var chart: some View {
    Chart(chartData) { dataPoint in
        BarMark(x: .value("Date", dataPoint.date, unit: .day),
        y: .value("Completed", dataPoint.itemsComplete))
        .foregroundStyle(Color.accentColor)
        .annotation(
            position: isLastDataPoint(dataPoint) ? .topLeading : .topTrailing,
            spacing: 0
        ) {
            Text("\(dataPoint.itemsComplete, format: .number)")
                .foregroundStyle(dataPoint.date == crownOffsetDate ? Color.appYellow : Color.clear)
        }

        RuleMark(x: .value("Date", crownOffsetDate, unit: .day))
            .foregroundStyle(Color.appYellow.opacity(crownPositionOpacity))
    }
    .chartXAxis {
        AxisMarks(format: shortDateFormatStyle)
    }
}
```

### Make the chart data range scrollable — [22:44]

```swift
@State var chartDataRange = (0...6)

private func updateChartDataRange() {
    if (highlightedDateIndex - chartDataRange.lowerBound) < 2, chartDataRange.lowerBound > 0 {
        let newLowerBound = max(0, chartDataRange.lowerBound - 1)
        let newUpperBound = min(newLowerBound + 6, data.count - 1)
        chartDataRange = (newLowerBound...newUpperBound)
        return
    }
    if (chartDataRange.upperBound - highlightedDateIndex) < 2, chartDataRange.upperBound < data.count - 1 {
        let newUpperBound = min(chartDataRange.upperBound + 1, data.count - 1)
        let newLowerBound = max(0, newUpperBound - 6)
        chartDataRange = (newLowerBound...newUpperBound)
        return
    }
}

private var chartData: [ChartData.DataElement] {
    Array(data[chartDataRange.clamped(to: (0...data.count - 1))])
}

private var chart: some View {
    Chart(chartData) { dataPoint in
        BarMark(x: .value("Date", dataPoint.date, unit: .day),
                y: .value("Completed", dataPoint.itemsComplete)
        )
        .foregroundStyle(Color.accentColor)
        .annotation(
            position: isLastDataPoint(dataPoint) ? .topLeading : .topTrailing,
            spacing: 0
        ) {
            Text("\(dataPoint.itemsComplete, format: .number)")
                .foregroundStyle(dataPoint.date == crownOffsetDate ? Color.appYellow : Color.clear)
        }

        RuleMark(x: .value("Date", crownOffsetDate, unit: .day))
            .foregroundStyle(Color.appYellow.opacity(crownPositionOpacity))
    }
    .chartXAxis {
        AxisMarks(format: shortDateFormatStyle)
    }
}

var body: some View {
    chart
        .focusable()
        .digitalCrownRotation(
            detent: $highlightedDateIndex,
            from: 0,
            through: data.count - 1,
            by: 1,
            sensitivity: .medium
        ) { crownEvent in
            isCrownIdle = false
            crownOffset = crownEvent.offset
        } onIdle: {
            isCrownIdle = true
        }
        .onChange(of: isCrownIdle) { newValue in
            withAnimation(newValue ? .easeOut : .easeIn) {
                crownPositionOpacity = newValue ? 0.2 : 1.0
            }
        }
        .onChange(of: highlightedDateIndex) { newValue in
            withAnimation {
                updateChartDataRange()
            }
        }
        .navigationTitle("Productivity")
        .navigationBarTitleDisplayMode(.inline)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10133/4/BBFD71DD-1E5F-4843-861E-0D333BAA1A3F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10133/4/BBFD71DD-1E5F-4843-861E-0D333BAA1A3F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10133) — developer.apple.com. Indexed for agent consumption._
