---
id: "wwdc2020-10160"
event: "wwdc2020"
year: 2020
title: "Formatters: Make data human-friendly"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10160"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Formatters: Make data human-friendly

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10160](https://developer.apple.com/videos/play/wwdc2020/10160)

Save yourself time and frustration: When you display data in your app — including dates, times, measurements, names, lists, numbers, or strings — learn how to format it correctly and provide a great experience. We'll walk you through the Formatter APIs as well as how SwiftUI works with stringsdict, and show you how they can help do the heavy lifting of formatting data. Learn about best practices and how to avoid common mistakes.

**Keywords:** `internationalization`, `localization`, `nsformatter`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,686 words)

## Documentation & Resources

- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/
- [Xcode Help: Add language plural variants](https://help.apple.com/xcode/mac/current/#/devd9af5f7ae) _documentation_
- [Unicode Date Field Symbol Table](https://www.unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table) _guide_
- [Displaying Human-Friendly Content](https://developer.apple.com/documentation/Foundation/displaying-human-friendly-content) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/displaying-human-friendly-content
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/displaying-human-friendly-content.json

## Code Snippets

### Dates and times — [2:25]

```swift
// Dates and Times

// Date with Day/Month/Year and Time
let dateFormatter = DateFormatter()
dateFormatter.dateStyle = .medium
dateFormatter.timeStyle = .short
dateFormatter.string(from: Date())

// Day of Week + Date + Month
let dateFormatter = DateFormatter()
dateFormatter.setLocalizedDateFormatFromTemplate
    ("MMMMdEEEE")
dateFormatter.string(from: Date())

// Abbreviated Day of Week
let dateFormatter = DateFormatter()
dateFormatter.setLocalizedDateFormatFromTemplate
    ("ccccc")
dateFormatter.string(from: Date())
```

### Date components formatter — [5:56]

```swift
// Dates and Times

// Date and Time Components
let formatter = DateComponentsFormatter()
formatter.unitsStyle = .abbreviated
let components = DateComponents(hour: 2, minute: 26)
formatter.string(from: components)

// Date and Time Intervals
let formatter = DateIntervalFormatter()
formatter.dateTemplate = "dMMM"
formatter.string(from: startDate, to: endDate)

// Relative Dates and Times
let formatter = RelativeDateTimeFormatter()
formatter.dateTimeStyle = .named
formatter.localizedString(from: DateComponents(day: -1))
```

### Measurements — [6:29]

```swift
// Measurements

// Temperature
let formatter = MeasurementFormatter()
let temperature = Measurement<UnitTemperature>
    (value: 16, unit: .celsius)
formatter.numberFormatter.maximumFractionDigits = 0
formatter.string(from: temperature)

// Speed
let speed = Measurement<UnitSpeed>
    (value: 14, unit: .kilometersPerHour)
formatter.string(from: speed)

// Pressure
let pressure = Measurement<UnitPressure>
    (value: 1.01885, unit: .bars)
formatter.string(from: pressure)
```

### Names — [7:49]

```swift
// Names

let formatter = PersonNameComponentsFormatter()
var nameComponents = PersonNameComponents()
nameComponents.familyName = "Iwasaki"
nameComponents.givenName = "Akiya"
nameComponents.nickname = "Aki-chan"

// Full Name
formatter.string(from: nameComponents)

// Short Name: Respects User Preferences
formatter.style = .short
formatter.string(from: nameComponents)

// Abbreviated Name
formatter.style = .abbreviated
formatter.string(from: nameComponents)
```

### Abbreviated name (monogram) — [8:31]

```swift
// Abbreviated Name: Monogram
formatter.style = .abbreviated
let monogram = formatter.string(from: nameComponents)
if (monogram.count <= 2) {
    // Use Monogram
}
else {
    // Use Icon
}
```

### Name formatter — [9:23]

```swift
// Names

let formatter = PersonNameComponentsFormatter()
var nameComponents = PersonNameComponents()
nameComponents.familyName = "岩崎"
nameComponents.givenName = "晃也"
nameComponents.nickname = "あきちゃん"

// Full Name
formatter.string(from: nameComponents)

// Short Name: Respects User Preferences
formatter.style = .short
formatter.string(from: nameComponents)

// Abbreviated Name
formatter.style = .abbreviated
formatter.string(from: nameComponents)
```

### Lists — [10:15]

```swift
// Lists

// English Localization

let items = [ "English", "French", "Spanish" ] ListFormatter.localizedString(byJoining: items)

let items = [ "English", "Spanish" ] ListFormatter.localizedString(byJoining: items)

let items = [ "Spanish", "English" ] ListFormatter.localizedString(byJoining: items)

// Spanish Localization

let items = [ "Inglés", "Español" ] ListFormatter.localizedString(byJoining: items)

let items = [ "Español", "Inglés" ] ListFormatter.localizedString(byJoining: items)
```

### Numbers — [12:01]

```swift
// Numbers

let formatter = NumberFormatter()
formatter.numberStyle = .decimal
formatter.string(from: 32.768) // French (France)

let formatter = NumberFormatter()
formatter.numberStyle = .decimal
formatter.string(from: 32.768) // Arabic (Egypt)

formatter.percentSymbol

formatter.decimalSeparator
```

### Numbers formatter — [12:33]

```swift
// Numbers

let formatter = NumberFormatter()
formatter.numberStyle = .percent
formatter.string(from: 0.71) // English (US)

let formatter = NumberFormatter()
formatter.numberStyle = .percent
formatter.string(from: 0.71) // Turkish (Turkey)
```

### Strings — [13:24]

```swift
// Strings

var body: some View {
    Text("\(photosCount) Photos Selected")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10160/4/CC254390-2967-444F-B9EA-01A5DE7E8D39/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10160) — developer.apple.com. Indexed for agent consumption._