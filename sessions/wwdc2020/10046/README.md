---
id: "wwdc2020-10046"
event: "wwdc2020"
year: 2020
title: "Create complications for Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10046"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["watchOS"]
hasTranscript: true
---

# Create complications for Apple Watch

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10046](https://developer.apple.com/videos/play/wwdc2020/10046)

When you add complications to a Watch app, people can access glanceable and up to date information directly from their watch face. We’ll show you how to create and build complications from the ground up and introduce you to Multiple Complications. Learn how to construct timelines, use families and templates, and discover best practices on crafting a thorough complication experience.

**Keywords:** `🐋`, `🐳`, `⌚️`, `clockkit`, `watchkit`, `watchos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,408 words)

## Documentation & Resources

- [Creating and updating a complication’s timeline](https://developer.apple.com/documentation/ClockKit/creating-and-updating-a-complication-s-timeline) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit/creating-and-updating-a-complication-s-timeline
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit/creating-and-updating-a-complication-s-timeline.json
- [ClockKit](https://developer.apple.com/documentation/ClockKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit.json

## Code Snippets

### CLKComplicationDataSource - Required Methods — [4:54]

```swift
// CLKComplicationDataSource - Required
class ComplicationController: NSObject, CLKComplicationDataSource {

    func getCurrentTimelineEntry(
        for complication: CLKComplication, 
        withHandler handler: @escaping (CLKComplicationTimelineEntry?) -> Void)     
    {
        // Call the handler with the current timeline entry
        handler(createTimelineEntry(forComplication: complication, date: Date()))
    }
}
```

### CLKComplicationDataSource - Timeline Support — [5:16]

```swift
// CLKComplicationDataSource - Timeline Support
extension ComplicationController {

    func getTimelineEndDate(
        for complication: CLKComplication, 
        withHandler handler: @escaping (Date?) -> Void) 
    {
        handler(timeline(for: complication)?.endDate)
    }

    func getTimelineEntries(
        for complication: CLKComplication, 
        after date: Date, 
        limit: Int, 
        withHandler handler: @escaping ([CLKComplicationTimelineEntry]?) -> Void) 
    {
       handler(timeline(for: complication)?.entries(after: date, limit: limit))
    }
}
```

### CLKDateTextProvider initialization — [8:11]

```swift
let longDate: Date = DateComponents(year: 2020, month: 9, day: 23).date ?? Date()
let units: NSCalendar.Unit = [.weekday, .month, .day]
let textProvider = CLKDateTextProvider(date: longDate, units: units)
```

### CLKRelativeDateTextProvider initialization — [8:49]

```swift
let timerStart: Date = …
let units: NSCalendar.Unit = [.hour, .minute, .second]
let textProvider = CLKRelativeDateTextProvider(date: timerStart, style: .timer, units: units)
```

### CLKComplicationDataSource - Multiple Complication Support — [13:16]

```swift
// CLKComplicationDataSource - Multiple Complication Support
extension ComplicationController {
    var descriptors : [CLKComplicationDescriptor] = []
    var dataDict = Dictionary<AnyHashable, Any>()

    for station in data.stations {
        dataDict = [“name": station.name, “shortName": station.shortName]
        descriptors.append(
            CLKComplicationDescriptor(
                identifier: station.name,
                displayName: station.name,
                supportedFamilies: CLKComplicationFamily.allCases,
                userInfo: dataDict))
    }

    descriptors.append(
        CLKComplicationDescriptor(
            identifier: "LogSighting",
            displayName: "Log Sighting",
            supportedFamilies: CLKComplicationFamily.allCases))

    descriptors.append(
        CLKComplicationDescriptor(
            identifier: "SeasonData",
            displayName: "Season Data",
            supportedFamilies: [.graphicRectangular]))

    // Call the handler with the currently supported complication descriptors
    handler(descriptors)
}
```

### CLKComplicationDataSource - Sample Templates — [17:09]

```swift
func getLocalizableSampleTemplate(
    for complication: CLKComplication, 
    withHandler handler: @escaping (CLKComplicationTemplate?) -> Void) 
{
    let template = createSampleTemplate(forComplication: complication)
    handler(template)
}
```

### Whale Watch - Entries — [17:33]

```swift
func createTimelineEntry(
    forComplication complication: CLKComplication, 
    date: Date) -> CLKComplicationTimelineEntry? 
{
    guard let template = createTemplate(forComplication: complication, date: date) else {
        return nil
    }
    return CLKComplicationTimelineEntry(date: date, complicationTemplate: template)
}
```

### Whale Watch - Templates — [17:44]

```swift
func createTemplate(
    forComplication complication: CLKComplication, 
    date: Date) -> CLKComplicationTemplate? 
{
    var station: Station? = nil
    if let stationName = complication.userInfo?["name"] as? String {
        station = data.stations.first(where: { $0.name == stationName })
    }

    let image = UIImage(named: "Spout-small")!
    let spoutFullColorImageProvider = CLKFullColorImageProvider(fullColorImage: image)
    let logSightingTextProvider = CLKSimpleTextProvider(
        text: "Log Sighting", 
        shortText: "Log")

    let defaultTemplate: (CLKComplicationFamily) -> CLKComplicationTemplate = { family -> CLKComplicationTemplate in
      // Return a default complication template for the given family
    }

    switch (complication.family, complication.identifier) {

    case (.graphicRectangular, "SeasonData"):
        return CLKComplicationTemplateGraphicRectangularFullView(
            ChartView(
                seriesData: data.last7DaysSightings, 
                seriesColor: .turquoise)

    case (.graphicCircular, "LogSighting"):
        return CLKComplicationTemplateGraphicCircularStackImage(
            line1ImageProvider: spoutFullColorImageProvider, 
            line2TextProvider: logSightingTextProvider)

    case (.graphicCircular, _):
        guard let station = station else { return defaultTemplate(.graphicCircular) }
        return CLKComplicationTemplateGraphicCircularView(
            SightingTypeView(station: station))

    case (.graphicCorner, _):
        guard let station = station else { return defaultTemplate(.graphicCorner) }
        return CLKComplicationTemplateGraphicCornerTextImage(
            textProvider: station.timeAndShortLocTextProvider, 
            imageProvider: station.whaleActivityFullColorProvider)

    case (.graphicExtraLarge, _):
        guard let station = station else { return defaultTemplate(.graphicExtraLarge) }
        return CLKComplicationTemplateGraphicExtraLargeCircularStackText(
            line1TextProvider: station.timeAndLocationTextProvider, 
            line2TextProvider: station.shortLocationTextProvider)

    default:
        return defaultTemplate(complication.family)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10046/4/F29A4217-89E7-4D20-A3CE-3764F44B16D8/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10046) — developer.apple.com. Indexed for agent consumption._