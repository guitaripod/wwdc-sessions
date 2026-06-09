---
id: "wwdc2022-10155"
event: "wwdc2022"
year: 2022
title: "Take ScreenCaptureKit to the next level"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10155"
topics: ["Audio & Video", "Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# Take ScreenCaptureKit to the next level

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10155](https://developer.apple.com/videos/play/wwdc2022/10155)

Discover how you can support complex screen capture experiences for people using your app with ScreenCaptureKit. We’ll explore many of the advanced options you can incorporate including fine tuning content filters, frame metadata interpretation, window pickers, and more. We’ll also show you how you can configure your stream for optimal performance.

**Keywords:** `audio capture`, `screen capture`, `screencapturekit`, `streaming`, `video capture`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,414 words)

## Documentation & Resources

- [ScreenCaptureKit](https://developer.apple.com/documentation/ScreenCaptureKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ScreenCaptureKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ScreenCaptureKit.json
- [Capturing screen content in macOS](https://developer.apple.com/documentation/ScreenCaptureKit/capturing-screen-content-in-macos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ScreenCaptureKit/capturing-screen-content-in-macos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ScreenCaptureKit/capturing-screen-content-in-macos.json

## Code Snippets

### Create a single window filter — [4:36]

```swift
// Get all available content to share via SCShareableContent
let shareableContent = try await SCShareableContent.excludingDesktopWindows(false, 
       onScreenWindowsOnly: false)

// Get window you want to share from SCShareableContent
guard let window : [SCWindow] = shareableContent.windows.first( where: 
                                    { $0.windowID == windowID }) else { return } 

// Create SCContentFilter for Independent Window
let contentFilter = SCContentFilter(desktopIndependentWindow: window)

// Create SCStreamConfiguration object and enable audio capture
let streamConfig = SCStreamConfiguration()
streamConfig.capturesAudio = true

// Create stream with config and filter
stream = SCStream(filter: contentFilter, configuration: streamConfig, delegate: self)
stream.addStreamOutput(self, type: .screen, sampleHandlerQueue: serialQueue)
stream.startCapture()
```

### Get dirty rects — [9:38]

```swift
// Get dirty rects from CMSampleBuffer dictionary metadata

func streamUpdateHandler(_ stream: SCStream, sampleBuffer: CMSampleBuffer) {
    guard let attachmentsArray = CMSampleBufferGetSampleAttachmentsArray(sampleBuffer, 
                                                          createIfNecessary: false) as? 
                                                         [[SCStreamFrameInfo, Any]], 
        let attachments = attachmentsArray.first else { return }

        let dirtyRects = attachments[.dirtyRects]    
    }
}

// Only encode and transmit the content within dirty rects
```

### Get content rect, content scale and scale factor — [13:34]

```swift
/* Get and use contentRect, contentScale and scaleFactor (pixel density) to convert the captured window back to its native size and pixel density */

func streamUpdateHandler(_ stream: SCStream, sampleBuffer: CMSampleBuffer) {

    guard let attachmentsArray = CMSampleBufferGetSampleAttachmentsArray(sampleBuffer, 
                                                          createIfNecessary: false) as? 
                                                         [[SCStreamFrameInfo, Any]], 
        let attachments = attachmentsArray.first else { return }

        let contentRect = attachments[.contentRect]
        let contentScale = attachments[.contentScale]
        let scaleFactor = attachments[.scaleFactor]

        /* Use contentRect to crop the frame, and then contentScale and 
        scaleFactor to scale it */

    }
}
```

### Create display filter with included windows — [15:37]

```swift
// Get all available content to share via SCShareableContent
let shareableContent = try await SCShareableContent.excludingDesktopWindows(false, 
                                                            onScreenWindowsOnly: false)

// Create SCWindow list using SCShareableContent and the window IDs to capture
let includingWindows = shareableContent.windows.filter { windowIDs.contains($0.windowID)}

// Create SCContentFilter for Full Display Including Windows
let contentFilter = SCContentFilter(display: display, including: includingWindows)

// Create SCStreamConfiguration object and enable audio
let streamConfig = SCStreamConfiguration()
streamConfig.capturesAudio = true

// Create stream
stream = SCStream(filter: contentFilter, configuration: streamConfig, delegate: self)
stream.addStreamOutput(self, type: .screen, sampleHandlerQueue: serialQueue)
stream.startCapture()
```

### Create display filter with included apps — [18:13]

```swift
// Get all available content to share via SCShareableContent
let shareableContent = try await SCShareableContent.excludingDesktopWindows(false, onScreenWindowsOnly: false)

/* Create list of SCRunningApplications using SCShareableContent and the application 
IDs you’d like to capture */
let includingApplications = shareableContent.applications.filter { 
    appBundleIDs.contains($0.bundleIdentifier)
}

// Create SCWindow list using SCShareableContent and the window IDs to except
let exceptingWindows = shareableContent.windows.filter { windowIDs.contains($0.windowID) }

// Create SCContentFilter for Full Display Including Apps, Excepting Windows
let contentFilter = SCContentFilter(display: display, including: includingApplications,
                           exceptingWindows: exceptingWindows)
```

### Create display filter with excluded apps — [20:46]

```swift
// Get all available content to share via SCShareableContent
let shareableContent = try await SCShareableContent.excludingDesktopWindows(false, 
                                         onScreenWindowsOnly: false)

/* Create list of SCRunningApplications using SCShareableContent and the app IDs 
you’d like to exclude */
let excludingApplications = shareableContent.applications.filter { 
    appBundleIDs.contains($0.bundleIdentifier)
}

// Create SCWindow list using SCShareableContent and the window IDs to except
let exceptingWindows = shareableContent.windows.filter { windowIDs.contains($0.windowID) }

// Create SCContentFilter for Full Display Excluding Windows
let contentFilter = SCContentFilter(display: display, 
                        excludingApplications: excludingApplications, 
                        exceptingWindows: exceptingWindows)
```

### Configure 4k 60FPS capture for streaming — [28:46]

```swift
let streamConfiguration = SCStreamConfiguration()

// 4K output size
streamConfiguration.width  = 3840
streamConfiguration.height = 2160

// 60 FPS
streamConfiguration.minimumFrameInterval = CMTime(value: 1, timescale: CMTimeScale(60))

// 420v output pixel format for encoding
streamConfiguration.pixelFormat = kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange

// Source rect(optional)
streamConfiguration.sourceRect = CGRectMake(100, 200, 3940, 2360)

// Set background fill color to black
streamConfiguration.backgroundColor = CGColor.black 

// Include cursor in capture 
streamConfiguration.showsCursor = true

// Valid queue depth is between 3 to 8
streamConfiguration.queueDepth = 5

// Include audio in capture
streamConfiguration.capturesAudio = true
```

### Live downgrade 4k 60FPS to 720p 15FPS — [30:08]

```swift
// Update output dimension down to 720p
streamConfiguration.width  = 1280
streamConfiguration.height = 720

// 15FPS
streamConfiguration.minimumFrameInterval = CMTime(value: 1, timescale: CMTimeScale(15))

// Update the configuration
try await stream.updateConfiguration(streamConfiguration)
```

### Build a window picker with live preview — [31:57]

```swift
// Get all available content to share via SCShareableContent
let shareableContent = try await SCShareableContent.excludingDesktopWindows(false, 
                                        onScreenWindowsOnly: true)

// Create a SCContentFilter for each shareable SCWindows
let contentFilters = shareableContent.windows.map { 
    SCContentFilter(desktopIndependentWindow: $0) 
}

// Stream configuration
let streamConfiguration = SCStreamConfiguration()

// 284x182 frame output
streamConfiguration.width  = 284
streamConfiguration.height = 182
// 5 FPS
streamConfiguration.minimumFrameInterval = CMTime(value: 1, timescale: CMTimeScale(5))
// BGRA pixel format for on screen display
streamConfiguration.pixelFormat = kCVPixelFormatType_32BGRA
// No audio
streamConfiguration.capturesAudio = false
// Does not include cursor in capture 
streamConfiguration.showsCursor = false
// Valid queue depth is between 3 to 8

// Create a SCStream with each SCContentFilter
var streams: [SCStream] = []
for contentFilter in contentFilters {
    let stream = SCStream(filter: contentFilter, streamConfiguration: streamConfig, 
                        delegate: self)
    try stream.addStreamOutput(self, type: .screen, sampleHandlerQueue: serialQueue)
    try await stream.startCapture()
    streams.append(stream)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10155/5/6A4BFEE6-F1BC-4E6A-9A03-13EBF7D38664/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10155/5/6A4BFEE6-F1BC-4E6A-9A03-13EBF7D38664/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10155) — developer.apple.com. Indexed for agent consumption._
