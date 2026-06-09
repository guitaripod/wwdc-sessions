---
id: "wwdc2022-10110"
event: "wwdc2022"
year: 2022
title: "Build global apps: Localization by example"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10110"
topics: ["Accessibility & Inclusion", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build global apps: Localization by example

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10110](https://developer.apple.com/videos/play/wwdc2022/10110)

Learn how you can run your apps on devices around the world and help everyone have a great experience — regardless of the language they speak. We'll explore how Apple APIs can provide a solid foundation when creating apps for diverse audiences, and we'll share examples, challenges, and best practices from our own experiences.

**Keywords:** `🌍`, `🌎`, `🌏`, `formatters`, `i10n`, `international`, `internationalization`, `l18n`, `stringsdict`, `swift packages`, `swiftui`, `translation`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,848 words)

## Documentation & Resources

- [Localizing package resources](https://developer.apple.com/documentation/Xcode/localizing-package-resources) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localizing-package-resources
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localizing-package-resources.json
- [Localization](https://developer.apple.com/documentation/Xcode/localization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localization.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/
- [Internationalization and Localization Guide](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/library/content/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html

## Code Snippets

### Declare strings using String(localized) — [1:59]

```swift
let windPerceptionLabelText = String(
    localized: "Wind is making it feel cooler", 
    comment: "Explains the wind is lowering the apparent temperature"
)
```

### Translation example 1 — [2:46]

```swift
let filter = String(localized: "Archive.label",
                 defaultValue: "Archive", 
                      comment: "Name of the Archive folder in the sidebar")

let filter = String(localized: "Archive.menuItem",
                 defaultValue: "Archive", 
                      comment: "Menu item title for moving the email into the Archive folder")
```

### Translation example 2 — [3:40]

```swift
String(localized: "Show weather in \(locationName)", 
       comment: "Title for a user activity to show weather at a specific city")

String(localized: "Show weather in My Location",
       comment: "Title for a user activity to show weather at the user's current location")
```

### Comment example — [4:58]

```swift
String(localized: "Show weather in \(locationName)",
         comment: "Title for a user activity to show weather at a specific city")
```

### Localized remote content example — [6:40]

```swift
let allServerLanguages = ["bg", "de", "en", "es", "kk", "uk"]
let language = Bundle.preferredLocalizations(from: allServerLanguages).first
```

### Numbers in a string example 1 — [7:56]

```swift
String(localized: "\(amountOfRain) in last \(numberOfHours) hour",
         comment: "Label showing how much rain has fallen in the last number of hours")

String(localized: "\(amountOfRain) in last ^[\(numberOfHours) hour](inflect: true)",
         comment: "Label showing how much rain has fallen in the last number of hours")
```

### Numbers in a string example 2 — [8:40]

```swift
if selectedCount == 1 {
    return String(localized: "Remove this city 
                              from your favorites")
} else {
    return String(localized: "Remove these cities 
                              from your favorites")
}
```

### Numbers in a string example 3 — [9:00]

```swift
String(localized: "\(amountOfRain) in last ^[\(numberOfHours) hour](inflect: true).",
         comment: "Label showing how much rain has fallen in the last number of hours")
```

### Formatter example — [9:29]

```swift
let humidity = 54

// In a SwiftUI view
Text(humidity, format: .percent)

// In Swift code
humidity.formatted(.percent)
```

### Formatter example 2 — [10:03]

```swift
date.formatted(
    .dateTime.year()
    .month()   
) // Jun 2022

whatToExpect.formatted()
// New features, exciting API, and advanced tips

amountOfRain.formatted(
    .measurement(
        width: .narrow,
        usage: .rainfall)) // 12mm

(date...<later).formatted(
    .components(
        style: .wide
    )
) // 24 minutes, 18 Seconds

date.formatted(
    .relative(
        presentation: 
            .numeric
    )
) // 2 minutes ago

let components = PersonNameComponents()
…
nameComponentsFormatter
    .string(from: components)
// Andreas Neusüß or 田中陽子

excitementLevel.formatted(
    .number
    .precision(
        .fractionLength(2)
    )
) // 1,001.42

price.formatted(
    .currency(
        code: "EUR"
    )
) // $20.99

distance.formatted(
    .measurement(
        width: .wide,
        usage: .road)
) // 500 feet

bytesCopied.formatted(
    .byteCount(
        style: .file
)) // 42.23 MB
```

### Combine a formatter with text — [11:10]

```swift
func expectedPrecipitationIn24Hours(for valueInMillimeters: Measurement<UnitLength>) -> String {
    // Use user's preferred measures
    let preferredUnit = UnitLength(forLocale: .current, usage: .rainfall)

    let valueInPreferredSystem = valueInMillimeters.converted(to: preferredUnit)

    // Format the amount of rainfall
    let formattedValue = valueInPreferredSystem
        .formatted(.measurement(width: .narrow, usage: .asProvided))

    let integerValue = Int(valueInPreferredSystem.value.rounded())

    // Load and use formatting string
    return String(localized: "EXPECTED_RAINFALL", 
               defaultValue: "\(integerValue) \(formattedValue) expected in next \(24)h.", 
                    comment: "Label - How much precipitation (2nd formatted value, in mm or Inches) is expected in the next 24 hours (3rd, always 24).")
}
```

### Stringsdict examples in English and Spanish — [12:22]

```xml
Localizable.stringsdict English:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>EXPECTED_RAINFALL</key>
    <dict>
        <key>NSStringLocalizedFormatKey</key>
        <string>%#@next_expected_precipitation_amount_24h@</string>
        <key>next_expected_precipitation_amount_24h</key>
        <dict>
            <key>NSStringFormatSpecTypeKey</key>
            <string>NSStringPluralRuleType</string>
            <key>NSStringFormatValueTypeKey</key>
            <string>d</string>
            <key>other</key>
            <string>%2$@ expected in next %3$dh.</string>
        </dict>
    </dict>
</dict>
</plist>

Localizable.stringsdict Spanish:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>EXPECTED_RAINFALL</key>
    <dict>
        <key>NSStringLocalizedFormatKey</key>
        <string>%#@next_expected_precipitation_amount_24h@</string>
        <key>next_expected_precipitation_amount_24h</key>
        <dict>
            <key>NSStringFormatSpecTypeKey</key>
            <string>NSStringPluralRuleType</string>
            <key>NSStringFormatValueTypeKey</key>
            <string>d</string>
            <key>one</key>
            <string>Se prevé %2$@ en las próximas %3$d h.</string>
            <key>other</key>
            <string>Se prevén %2$@ en las próximas %3$d h.</string>
        </dict>
    </dict>
</dict>
</plist>
```

### Swift Package localization example — [13:40]

```swift
let package = Package(
    name: "FoodTruckKit",

    defaultLocalization: "en",

    products: [
       .library(
            name: "FoodTruckKit",
            targets: ["FoodTruckKit"]),
    ],
    …
)
```

### Loading a string in a Swift Package — [14:41]

```swift
let title = String(localized: "Wind",
                      bundle: .module, 
                     comment: "Title for section that
                               shows data about wind.")
```

### Grid example — [18:19]

```swift
// Requires data types "Row" and "row" to be defined

struct WeatherTestView: View {
    var rows: [Row]
    var body: some View {
        Grid(alignment: .leading) {
            ForEach(rows) { row in
                GridRow {
                    Text(row.dayOfWeek)

                    Image(systemName: row.weatherCondition)
                        .symbolRenderingMode(.multicolor)

                    Text(row.minimumTemperature)
                        .gridColumnAlignment(.trailing)

                    Capsule().fill(Color.orange).frame(height: 4)

                    Text(row.maximumTemperature)
                }
                .foregroundColor(.white)
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10110/3/9DDED4EB-547B-46DD-AEE5-9D3F2C60CFF8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10110/3/9DDED4EB-547B-46DD-AEE5-9D3F2C60CFF8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10110) — developer.apple.com. Indexed for agent consumption._
