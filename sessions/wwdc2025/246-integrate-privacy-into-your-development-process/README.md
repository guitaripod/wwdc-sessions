---
id: "wwdc2025-246"
event: "wwdc2025"
year: 2025
title: "Integrate privacy into your development process"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/246"
topics: ["Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Integrate privacy into your development process

**Event:** WWDC25 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-246](https://developer.apple.com/videos/play/wwdc2025/246)

Learn how to build privacy into your apps from the planning stages through deployment. We’ll cover practical ways to integrate privacy at each step of the development lifecycle, focusing on data minimization, on-device processing, and transparency and control. You’ll discover how to use Apple’s tools and frameworks to protect user data and create a privacy-respecting app experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,904 words)

## Documentation & Resources

- [Swift Homomorphic Encryption](https://github.com/apple/swift-homomorphic-encryption) _samplecode_
- [Configuring app groups](https://developer.apple.com/documentation/Xcode/configuring-app-groups) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/configuring-app-groups
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/configuring-app-groups.json
- [AdAttributionKit](https://developer.apple.com/documentation/AdAttributionKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit.json
- [Privacy manifest files](https://developer.apple.com/documentation/BundleResources/privacy-manifest-files) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BundleResources/privacy-manifest-files
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BundleResources/privacy-manifest-files.json
- [Explore the Human Interface Guidelines for privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/privacy

## Code Snippets

### Create an inline Photos picker — [10:29]

```swift
// Create an inline Photos picker

// Define the app's Photos picker
PhotosPicker(
    selection: $viewModel.selection,
    matching: .images,
    preferredItemEncoding: .current,
    photoLibrary: .shared()
) {
    Text("Select Photos")
}

// Configure a half-height Photos picker
.photosPickerStyle(.inline)
.ignoresSafeArea()
.frame(height: 340)
```

### Display the Location Button — [11:33]

```swift
// Display the Location Button

LocationButton(LocationButton.Title.currentLocation) {
    // Start updating location when user taps the button.
    // Location button doesn't require the additional
    // step of calling 'requestWhenInUseAuthorization()'.
    manager.startUpdatingLocation()
}.foregroundColor(Color.white)
    .cornerRadius(27)
    .frame(width: 210, height: 54)
    .padding(.bottom, 30)
```

### Encrypting data in CloudKit — [13:48]

```swift
myRecord.encryptedValues["encryptedStringField"] = "Sensitive value"

let decryptedString = myRecord.encryptedValues["encryptedStringField"] as? String
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/246/4/37a0cde9-fca8-4877-b05c-95e677c0e2b0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/246/4/37a0cde9-fca8-4877-b05c-95e677c0e2b0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/246) — developer.apple.com. Indexed for agent consumption._
