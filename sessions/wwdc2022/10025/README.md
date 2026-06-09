---
id: "wwdc2022-10025"
event: "wwdc2022"
year: 2022
title: "Capture machine-readable codes and text with VisionKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10025"
topics: ["Photos & Camera", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Capture machine-readable codes and text with VisionKit

**Event:** WWDC22 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10025](https://developer.apple.com/videos/play/wwdc2022/10025)

Meet the Data Scanner in VisionKit: This framework combines AVCapture and Vision to enable live capture of machine-readable codes and text through a simple Swift API. We’ll show you how to control the types of content your app can capture by specifying barcode symbologies and language selection. We’ll also explore how you can enable guidance in your app, customize item highlighting or regions of interest, and handle interactions after your app detects an item.

For more on interacting with Live Text through still images or paused video frames, watch "Add Live Text interaction to your app" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,890 words)

## Documentation & Resources

- [Scanning data with the camera](https://developer.apple.com/documentation/VisionKit/scanning-data-with-the-camera) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VisionKit/scanning-data-with-the-camera
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VisionKit/scanning-data-with-the-camera.json

## Code Snippets

### Creating a data scanner instance and present it — [4:40]

```swift
import VisionKit

// Specify the types of data to recognize
let recognizedDataTypes:Set<DataScannerViewController.RecognizedDataType> = [
    .barcode(symbologies: [.qr]),
  	// uncomment to filter on specific languages (e.g., Japanese)
    // .text(languages: ["ja"])
    // uncomment to filter on specific content types (e.g., URLs)
		// .text(textContentType: .URL)
]

// Create the data scanner, present it, and start scanning!
let dataScanner = DataScannerViewController(recognizedDataTypes: recognizedDataTypes)
present(dataScanner, animated: true) {
    try? dataScanner.startScanning()
}
```

### Set a delegate — [8:11]

```swift
// Specify the types of data to recognize
let recognizedDataTypes:Set<DataScannerViewController.RecognizedDataType> = [
    .barcode(symbologies: [.qr]),
    .text(textContentType: .URL)
]

// Create the data scanner, present it, and start scanning!
let dataScanner = DataScannerViewController(recognizedDataTypes: recognizedDataTypes)
dataScanner.delegate = self.present(dataScanner, animated: true) {
    try? dataScanner.startScanning()
}
```

### Handling tap interactions — [8:19]

```swift
func dataScanner(_ dataScanner: DataScannerViewController, didTapOn item: RecognizedItem) {
    switch item {
    case .text(let text):
        print("text: \(text.transcript)")
    case .barcode(let barcode):
        print("barcode: \(barcode.payloadStringValue ?? "unknown")")
    default:
        print("unexpected item")
    }
}
```

### Adding custom highlights via the didAdd delegate method — [9:11]

```swift
// Dictionary to store our custom highlights keyed by their associated item ID.
var itemHighlightViews: [RecognizedItem.ID: HighlightView] = [:]

// For each new item, create a new highlight view and add it to the view hierarchy.
func dataScanner(_ dataScanner: DataScannerViewController, didAdd addItems: [RecognizedItem], allItems: [RecognizedItem]) {
    for item in addedItems {
        let newView = newHighlightView(forItem: item)
        itemHighlightViews[item.id] = newView
        dataScanner.overlayContainerView.addSubview(newView)
    }
}
```

### Animating custom highlights during the didUpdate delegate method — [9:37]

```swift
// Animate highlight views to their new bounds
func dataScanner(_ dataScanner: DataScannerViewController, didUpdate updatedItems: [RecognizedItem], allItems: [RecognizedItem]) {
    for item in updatedItems {
        if let view = itemHighlightViews[item.id] {
            animate(view: view, toNewBounds: item.bounds)
        }
    }
}
```

### Removing custom highlights during the didRemove delegate callback — [10:03]

```swift
// Remove highlights when their associated items are removed.
func dataScanner(_ dataScanner: DataScannerViewController, didRemove removedItems: [RecognizedItem], allItems: [RecognizedItem]) {
    for item in removedItems {
        if let view = itemHighlightViews[item.id] {
            itemHighlightViews.removeValue(forKey: item.id)
            view.removeFromSuperview()
        }
    }
}
```

### Take a still photo and save it to the camera roll — [10:54]

```swift
// Take a still photo and save to the camera roll
if let image = try? await dataScanner.capturePhoto() {
    UIImageWriteToSavedPhotosAlbum(image, nil, nil, nil)
}
```

### Using the recognizedItems async stream to keep track of items — [11:10]

```swift
// Send a notification when the recognized items change.
var currentItems: [RecognizedItem] = []

func updateViaAsyncStream() async {
    guard let scanner = dataScannerViewController else { return }

    let stream = scanner.recognizedItems
    for await newItems: [RecognizedItem] in stream {
        let diff = newItems.difference(from: currentItems) { a, b in
            return a.id == b.id
        }

        if !diff.isEmpty {
            currentItems = newItems
            sendDidChangeNotification()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10025/4/5DB691AA-D403-4394-885D-0F1F18772715/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10025/4/5DB691AA-D403-4394-885D-0F1F18772715/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10025) — developer.apple.com. Indexed for agent consumption._