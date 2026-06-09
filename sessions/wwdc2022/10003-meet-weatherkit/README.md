---
id: "wwdc2022-10003"
event: "wwdc2022"
year: 2022
title: "Meet WeatherKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10003"
topics: ["Maps & Location", "Safari & Web", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet WeatherKit

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10003](https://developer.apple.com/videos/play/wwdc2022/10003)

WeatherKit offers valuable weather data for your apps and services to help people stay up to date on the latest conditions. Learn how to use Swift and REST APIs to access information about the current weather, 10-day hourly forecasts for temperature, expected precipitation, wind reports, the UV Index, and more. We’ll also share how WeatherKit can provide timely, hyperlocal weather information without compromising someone’s personal data or their privacy.

**Keywords:** `api`, `browser`, `rest`, `weather`, `web`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,787 words)

## Documentation & Resources

- [WeatherKit](https://developer.apple.com/documentation/WeatherKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WeatherKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WeatherKit.json

## Code Snippets

### Request the weather in Swift — [4:28]

```swift
// Request the weather

import WeatherKit
import CoreLocation


let weatherService = WeatherService()

let syracuse = CLLocation(latitude: 43, longitude: -76)

let weather = try! await weatherService.weather(for: syracuse)

let temperature = weather.currentWeather.temperature

let uvIndex = weather.currentWeather.uvIndex
```

### Request the weather via REST API — [7:56]

```javascript
/* Request a token */
const tokenResponse = await fetch('https://example.com/token');
const token = await tokenResponse.text();

/* Get my weather object */
const url = "https://weatherkit.apple.com/1/weather/en-US/41.029/-74.642?dataSets=weatherAlerts&country=US"

const weatherResponse = await fetch(url, {
headers: {
"Authorization": token
}
});
const weather = await weatherResponse.json();

/* Check for active weather alerts */
const alerts = weather.weatherAlerts;
const detailsUrl = weather.weatherAlerts.detailsUrl;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10003/5/C8AAE478-A435-4DA4-8256-F32941E32204/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10003/5/C8AAE478-A435-4DA4-8256-F32941E32204/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10003) — developer.apple.com. Indexed for agent consumption._
