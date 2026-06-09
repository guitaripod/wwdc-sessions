---
id: "wwdc2023-10136"
event: "wwdc2023"
year: 2023
title: "What’s new in ScreenCaptureKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10136"
topics: ["Audio & Video", "Photos & Camera", "Graphics & Games"]
platforms: ["macOS"]
hasTranscript: true
---

# What’s new in ScreenCaptureKit

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** macOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10136](https://developer.apple.com/videos/play/wwdc2023/10136)

Level up your screen sharing experience with the latest features in ScreenCaptureKit. Explore the built-in system picker, Presenter Overlay, and screenshot capabilities, and learn how to incorporate these features into your existing ScreenCaptureKit app or game.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,149 words)

## Documentation & Resources

- [ScreenCaptureKit](https://developer.apple.com/documentation/ScreenCaptureKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ScreenCaptureKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ScreenCaptureKit.json

## Code Snippets

### Set up delegate for stream — [3:32]

```swift
// Set up delegate for stream
let stream = SCStream(filter: filter, configuration: config, delegate: self)

// delegate method for Presenter Overlay applied
func stream(_ stream: SCStream, outputEffectDidStart didStart: bool) {
    // if Presenter Overlay is on, present banner in app to notify
    if didStart == true {
        presentBanner()
        turnOffCamera()
    } else {
        turnOnCamera()
    }
}
```

### Set up content sharing picker instance — [6:48]

```swift
// Set up content sharing picker instance
    let picker = SCContentSharingPicker.shared()
    picker.addObserver(self)
    picker.active = true

    // show system level picker button
    func showSystemPicker(sender: UIButton!) {
        picker.present(for stream: nil, using contentStyle:.window)
    }

    // observer call back for picker
    func contentSharingPicker(_ picker: SCContentSharingPicker, didUpdateWith filter:                                          
    SCContentFilter, for stream: SCStream?) {
       if let stream = stream {
            stream.updateContentFilter(filter)
        } else {
            let stream = SCStream(filter: filter, configuration: config, delegate: self)
        }
    }
```

### Observer call back for picker did fail and did cancel — [7:41]

```swift
// Set up content sharing picker instance
    let picker = SCContentSharingPicker.shared()
    picker.addObserver(self)
    picker.active = true

    // show system level picker button
    func showSystemPicker(sender: UIButton!) {
        picker.present(for stream: nil, using contentStyle:.window)
    }

    // observer call back for picker did fail
    func contentSharingPicker(contentSharingPickerStartDidFailWith error:NSError) {
        if error {
            presentNotifications(error: error)
        }
    }

    // observer call back for picker did cancel
    func contentSharingPicker(_ picker: SCContentSharingPicker, didCancel for stream: SCStream?) {
       if stream {
           resetStateForStream(stream: stream)
       }
    }
```

### Per-stream configuration — [8:41]

```swift
// Set up content sharing picker instance
    let picker = SCContentSharingPicker.shared()
    picker.addObserver(self)
    picker.active = true

    // Create configurations
    let pickerConfig = SCContentSharingPickerConfiguration()

    // Set Picker configuration
    pickerConfig.excludedBundleIDs = [“com.foo.myApp”,”com.foo.myApp2”]
    pickerConfig.allowsRepicking = true

    // Create configurations
    picker.setConfiguration(pickerConfig, for: stream)

    func showSystemPicker(sender: UIButton!) {
        picker.present(for stream: nil, using contentStyle:.window)
    }
```

### Call the screenshot API — [12:26]

```swift
// Call the screenshot API

class SCScreenshotManager : NSObject {

class func captureSampleBuffer(contentFilter: SCContentFilter, 
                               configuration: SCStreamConfiguration)
  															async throws -> CMSampleBuffer

class func captureImage(contentFilter: SCContentFilter,
                        configuration: SCStreamConfiguration)
  											async throws -> GImage
}
```

### Take a screenshot with ScreenCaptureKit — [12:44]

```swift
// Don't forget to customize the content you want in your screenshot
// Use SCShareableContent or SCContentSharingPicker to pick your content
let display = nil;

// Create your SCContentFilter and SCStreamConfiguration
// Customize these lines to use the content you want and desired config options
let myContentFilter = SCContentFilter(display: display,
                             excludingApplications: [],
                             exceptingWindows: []);
let myConfiguration = SCStreamConfiguration();

// Call the screenshot API and get your screenshot image
if let screenshot = try? await SCScreenshotManager.captureSampleBuffer(contentFilter: myContentFilter, configuration:
                                                       myConfiguration) {
    print("Fetched screenshot.")
} else {
    print("Failed to fetch screenshot.")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10136/6/998A4D51-FB97-4CB9-959F-65B5827F9926/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10136/6/998A4D51-FB97-4CB9-959F-65B5827F9926/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10136) — developer.apple.com. Indexed for agent consumption._
