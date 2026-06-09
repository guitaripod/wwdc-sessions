---
id: "wwdc2020-10647"
event: "wwdc2020"
year: 2020
title: "Become a Simulator expert"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10647"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Become a Simulator expert

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10647](https://developer.apple.com/videos/play/wwdc2020/10647)

Simulator runs your iOS, iPadOS, tvOS, or watchOS apps directly on your Mac — no separate device required. We’ll give you a tour of the app's latest tools and features and show you how to sharpen your Simulator skills. Discover how to test pointer and trackpad support, adjust Simulator preferences, and use command line tools like simctl to help you simulate push notifications in a development environment. While you can get a quick overview of Simulator in this session, for more detailed information about the tool you may want to refresh yourself on “Getting the Most Out of Simulator” from WWDC19.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,299 words)

## Code Snippets

### Grant permission to protected resources — [11:32]

```bash
xcrun simctl privacy booted grant calendar com.example.MyApp

xcrun simctl privacy booted grant photos com.example.MyApp

xcrun simctl privacy booted grant contacts com.example.MyApp
```

### Revoke permission to protected resources — [11:54]

```bash
xcrun simctl privacy booted revoke calendar com.example.MyApp

xcrun simctl privacy booted revoke all com.example.MyApp

xcrun simctl privacy booted reset all
```

### Sample push notification for Simulator — [12:47]

```json
{
  "Simulator Target Bundle": "com.example.MyApp",
  "aps": {
       "alert": {
           "title": "Push Notification",
           "subtitle": "New fruit smoothies are available",
           "body": "We know you'll love these delicious concoctions 🥰"
       }
   }
}
```

### Send a push notification to a specific Bundle ID — [13:15]

```bash
xcrun simctl push booted com.example.MyApp payload.json
```

### Send a push notification to the Bundle ID in the payload — [13:43]

```bash
xcrun simctl push booted payload.json
```

### Record a video — [14:40]

```bash
xcrun simctl io booted recordVideo video.mp4
```

### Record a video in H.264 without the device mask — [15:48]

```bash
xcrun simctl io booted recordVideo --codec h264 --mask ignored video.mp4
```

### Record a video of the external display — [16:23]

```bash
xcrun simctl io booted recordVideo --display external external.mp4
```

### Override the status bar — [18:00]

```bash
xcrun simctl status_bar booted override --time 12:01 --cellularBars 1 --dataNetwork 3g --wifiMode failed
```

### Clear status bar overrides — [18:16]

```bash
xcrun simctl status_bar booted clear
```

### Add a certificate to the root store — [18:47]

```bash
xcrun simctl keychain booted add-root-cert myCA.pem
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10647/6/D236A0D8-F4A2-4213-A8D3-CD986C402338/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10647) — developer.apple.com. Indexed for agent consumption._
