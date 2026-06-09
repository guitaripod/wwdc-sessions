---
id: "wwdc2020-10142"
event: "wwdc2020"
year: 2020
title: "Build scalable enterprise app suites"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10142"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build scalable enterprise app suites

**Event:** WWDC20 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10142](https://developer.apple.com/videos/play/wwdc2020/10142)

Learn how to build focused enterprise apps that work well together. In this session, we’ll introduce you to Apple Retail’s suite of enterprise apps, which help employees interact with customers, track operations, manage stores, and stay connected. Discover how Apple Retail created a unified set of apps by adopting Swift Packages and testing for app scalability. And explore how managing apps in production with configurations can help tailor app suites to different regions and locations.

**Keywords:** `enterprise`, `swift packages`, `testing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,488 words)

## Code Snippets

### App Groups — [2:02]

```swift
let sharedDefaults = UserDefaults(suiteName: “group.com.apple.myappgroup")!

sharedDefaults.set("My Cool Value", forKey: "MyKeyName")

let myKeyNameValue = sharedDefaults.string(forKey: "MyKeyName")
```

### BarcodeScannerViewController — [5:04]

```swift
import RetailScanner

let scanOptions = BarcodeScanOptions()
scanOptions.scanRegion = .regular
scanOptions.shouldAddSupplementaryView = false
scanOptions.shouldShowBarcodeDetector = true

let barcodeViewController = BarcodeScannerViewController(scanOptions: scanOptions)
barcodeViewController.delegate = self
```

### OCRScannerViewController — [5:29]

```swift
import RetailScanner

let scanOptions = OCRScanOptions(
    scanRegion: .custom(CGSize(width: 400, height: 100)),
    accessibilityBehavior: .vibrate,
    shouldAddSupplementaryView: true,
    validation: nil, 
    shouldShowResultView: true
)
scanOptions.recognitionLevel = .fast

let ocrViewController = OCRScannerViewController(
    scanOptions: scanOptions
)
ocrViewController.delegate = self
```

### Config-driven UI - Client based configuration hosted by server — [12:26]

```swift
func configuredCellForLabel(for customerInfoField: CustomerInfoField, at indexPath: IndexPath) -> UITableViewCell { . . . }



func configuredCellForPhoneNumber(for customerInfoField: CustomerInfoField, at indexPath: IndexPath) -> UITableViewCell { . . . }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10142/6/570BD5D0-7BC7-4D3A-A1EC-E67D13CD87E0/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10142) — developer.apple.com. Indexed for agent consumption._