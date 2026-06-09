---
id: "wwdc2024-10067"
event: "wwdc2024"
year: 2024
title: "Bring context to today’s weather"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10067"
topics: ["Maps & Location"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Bring context to today’s weather

**Event:** WWDC24 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10067](https://developer.apple.com/videos/play/wwdc2024/10067)

Harness the power of WeatherKit to get detailed weather forecast data such as precipitation amounts by type, cloud cover by altitude, or maximum wind speed. Find out how you can summarize weather by different parts of the day and highlight significant upcoming changes to temperature or precipitation. Understand how you can compare current weather to the past through our Historical Comparisons dataset and dive into historical weather statistics for any location in the world. We’ll also explore how you can do all of this faster with our Swift and REST APIs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,459 words)

## Documentation & Resources

- [WeatherKit REST API](https://developer.apple.com/documentation/WeatherKitRESTAPI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WeatherKitRESTAPI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WeatherKitRESTAPI.json
- [Request authentication for WeatherKit REST API](https://developer.apple.com/documentation/WeatherKitRESTAPI/request-authentication-for-weatherkit-rest-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WeatherKitRESTAPI/request-authentication-for-weatherkit-rest-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WeatherKitRESTAPI/request-authentication-for-weatherkit-rest-api.json
- [Forum: Maps & Location](https://developer.apple.com/forums/topics/maps-and-location?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/maps-and-location?cid=vf-a-0010
- [WeatherKit](https://developer.apple.com/documentation/WeatherKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WeatherKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WeatherKit.json

## Code Snippets

### Fetch Precipitation Amount — [2:40]

```swift
import CoreLocation
import Foundation
import WeatherKit


extension CLLocation {
    static var newYork: CLLocation {
        CLLocation(latitude: 50.710, longitude: -74.006)
    }
}

let hourlyPrecipitation = try await WeatherService()
    .weather(for: .newYork, including: .hourly)
    .map(\.precipitationAmount)
```

### Fetch Precipitation Amount (REST) — [3:25]

```markdown
https://weatherkit.apple.com/api/v2/weather/en-US/40.710/-74.006?dataSets=forecastHourly&relativeHourlyStart=0&relativeHourlyEnd=1&hourlyRelativeTo=now&timezone=America/New_York
```

### Weather Changes — [6:05]

```swift
import CoreLocation
import Foundation
import WeatherKit


extension Date {
    var isTomorrow: Bool {
        return Calendar.current.isDateInTomorrow(self)
    }
}

let changes = try await WeatherService()
   .weather(for: .newYork, including: .changes)

let lowTemperatureChanges = changes?
   .filter(\.date.isTomorrow)
   .map(\.lowTemperature)

if let lowTemperatureChanges, lowTemperatureChanges.contains(.decrease) {
   // Lower temperatures expected tomorrow

}
```

### Weather Changes (REST) — [6:43]

```markdown
https://weatherkit.apple.com/api/v2/weather/en-US/40.710/-74.006?dataSets=weatherChanges
```

### Historical Comparisons — [8:17]

```swift
import CoreLocation
import Foundation
import WeatherKit


let mostSignificant = try await WeatherService()
    .weather(for: .newYork, including: .historicalComparisons)?
    .first

switch mostSignificant {
case .highTemperature(let trend), .lowTemperature(let trend):
    // Display temperature trend
    break
case .some, .none:
    break
}
```

### Historical Comparisons (REST) — [8:36]

```markdown
https://weatherkit.apple.com/api/v2/weather/en-US/40.710/-74.006?dataSets=historicalComparisons
```

### Monthly Statistics — [11:11]

```swift
import CoreLocation
import Foundation
import WeatherKit


let averagePrecipitation = try await WeatherService()
    .monthlyStatistics(
        for: .newYork,
        startMonth: 1,
        endMonth: 12,
        including: .precipitation
    )

let averagePrecipitationAmountsPerMonth = Dictionary(
    grouping: averagePrecipitation,
    by: \.month
)
```

### Monthly Statistics (REST) — [11:41]

```markdown
https://weatherkit.apple.com/api/v2/statistics/monthly/40.710/-74.006?dataSets=precipitation&start=1&end=12
```

### Daily Summary — [12:52]

```swift
import CoreLocation
import Foundation
import WeatherKit


extension Date {
    static var thirtyDaysAgo: Date {
        return Calendar.current.date(byAdding: .day, value: -30, to: .now)!
    }
}

let pastThirtyDaysSummary = try await WeatherService()
    .dailySummary(
       for: .newYork,
       forDaysIn: DateInterval(start: .thirtyDaysAgo, end: .now),
       including: .precipitation
    )
    .first

if let pastThirtyDaysSummary {
    // We have a daily weather summary for each day in the past 30 days

}
```

### Daily Summary (REST) — [13:22]

```markdown
https://weatherkit.apple.com/api/v2/summary/daily/40.710/-74.006?dataSets=precipitation&start=2024-05-12&end=2024-06-10
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10067/5/24B0D3B9-2CAA-4132-B63B-EEA93B0837EF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10067/5/24B0D3B9-2CAA-4132-B63B-EEA93B0837EF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10067) — developer.apple.com. Indexed for agent consumption._
