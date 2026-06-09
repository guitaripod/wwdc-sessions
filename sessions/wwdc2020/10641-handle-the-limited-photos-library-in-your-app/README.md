---
id: "wwdc2020-10641"
event: "wwdc2020"
year: 2020
title: "Handle the Limited Photos Library in your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10641"
topics: ["Privacy & Security", "SwiftUI & UI Frameworks", "Photos & Camera"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Handle the Limited Photos Library in your app

**Event:** WWDC20 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10641](https://developer.apple.com/videos/play/wwdc2020/10641)

Access the photos and videos you need for your app while preserving privacy. With the new Limited Photos Library feature, people can directly control which photos and videos an app can access to protect their private content. We’ll explore how this feature may affect your app, and take you through alternatives like PHPicker. Check out “Meet the New Photos Picker” to learn more about PHPicker and how this this fully private picker can help you avoid requiring full Photos Library access in your app.

**Keywords:** `photokit`, `photo library`, `photos`, `photos api`, `picker`, `privacy`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,240 words)

## Documentation & Resources

- [PhotoKit](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json

## Code Snippets

### Query for authorization status — [8:36]

```swift
import Photos

let accessLevel: PHAccessLevel = .readWrite
let authorizationStatus = PHPhotoLibrary.authorizationStatus(for: accessLevel)

switch authorizationStatus {
case .limited:
    print("limited authorization granted")
default:
    //FIXME: Implement handling for all authorizationStatus values
    print("Not implemented")
}
```

### Request read/write authorization — [9:43]

```swift
import Photos

let requiredAccessLevel: PHAccessLevel = .readWrite
PHPhotoLibrary.requestAuthorization(for: requiredAccessLevel) { authorizationStatus in
    switch authorizationStatus {
    case .limited:
        print("limited authorization granted")
    default:
        //FIXME: Implement handling for all authorizationStatus
        print("Unimplemented")

    }
}
```

### Present the limited library management UI — [12:04]

```swift
import PhotosUI

let library = PHPhotoLibrary.shared()
let viewController = self

library.presentLimitedLibraryPicker(from: viewController)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10641/5/51B91C53-BFDD-41DD-9EA3-418DE396897F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10641) — developer.apple.com. Indexed for agent consumption._
