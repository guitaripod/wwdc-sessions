---
id: "wwdc2022-10132"
event: "wwdc2022"
year: 2022
title: "Discover PhotoKit change history"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10132"
topics: ["Photos & Camera"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Discover PhotoKit change history

**Event:** WWDC22 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10132](https://developer.apple.com/videos/play/wwdc2022/10132)

PhotoKit can help you build rich, photo-centric features. Learn how you can easily track changes to image assets with the latest APIs in PhotoKit. We’ll introduce you to the PHPhotoLibrary change history API and demonstrate how you can persist change tokens across launches to help your app recognize additions, deletions, and updates to someone’s photo library. To learn more about Photos library integration, be sure to watch "What's new in the Photos picker" from WWDC22 and "Improve access to Photos in your app" from WWDC21.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,387 words)

## Documentation & Resources

- [PhotoKit](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json

## Code Snippets

### Tracking photo library changes — [0:01]

```swift
// Discover added assets
let options = PHFetchOptions()
options.predicate = NSPredicate(format: "creationDate > %@", lastLaunchDate as CVarArg)
let insertedAssets = PHAsset.fetchAssets(with: options)
```

### Tracking photo library changes (2) — [0:02]

```swift
let fetchResult = PHAsset.fetchAssets(with: localIdentifiers, options: nil)
// Discover all modified and deleted assets
fetchResult.enumerateObjects { asset, idx, stop in
    if asset.modificationDate?.compare(lastLaunchDate) == .orderedDescending {
        // Asset could have been modified
    }
    if !localIdentifiers.contains(asset.localIdentifier) {
        // Asset could have been deleted
    }
}
```

### Fetching persistent changes using persistent change token — [0:03]

```swift
let persistentChanges = try! PHPhotoLibrary.shared().fetchPersistentChanges(since: self.lastStoredToken)

for persistentChange in persistentChanges { 
   if let changeDetails = persistentChange.changeDetails(for: PHObjectType.asset) {
        let updatedIdentifiers = changeDetails.updatedLocalIdentifiers
        let deletedIdentifiers = changeDetails.deletedLocalIdentifiers
        let insertedIdentifiers = changeDetails.insertedLocalIdentifiers
    }
}

// After processing change details
self.lastStoredToken = lastPersistentChange.changeToken
```

### Identifying important changes — [0:04]

```swift
// Get last stored change token
let changeToken = self.lastStoredToken

// Fetch persistent changes
let persistentChanges = try!   
         library.fetchPersistentChanges(since: changeToken)

for persistentChange in persistentChanges {
    // Grab change details and process updates
}
```

### Using inserted identifiers — [0:05]

```swift
let insertedAssets = PHAsset.fetchAssets(with: insertedIdentifiers, options: nil)
insertedAssets.enumerateObjects { asset, idx, stop in
   for hike in hikes {
        let dateInterval = NSDateInterval(start: hike.startDate, end: hike.endDate)
        if dateInterval.contains(asset.creationDate) {
            // This hike contains a new added asset
        }
    }
}
```

### Using updated identifiers — [0:06]

```swift
let updatedAssets = PHAsset.fetchAssets(with: updatedIdentifiers, options: nil)
updatedAssets.enumerateObjects { asset, idx, stop in
    if asset.hasAdjustments {
        // This asset has edits
    }
}
```

### Using deleted identifiers — [0:07]

```swift
for deletedIdentifier in deletedIdentifiers {
    for collage in collages {
        if collage.assetLocalIdentifiers.contains(deletedIdentifier) {
            // This collage needs to be redrawn
        }
    }
}
```

### Handling errors — [0:08]

```swift
do {
    let persistentChanges = try library.fetchPersistentChanges(since: changeToken)
} catch PHPhotosError.persistentChangeTokenExpired,
        PHPhotosError.persistentChangeDetailsUnavailable {
    let fetchResult = PHAsset.fetchAssets(with: trackedIdentifiers, options: options)
    // Use fetch result
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10132/3/E1001357-38F4-429C-A7E2-495996D84893/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10132/3/E1001357-38F4-429C-A7E2-495996D84893/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10132) — developer.apple.com. Indexed for agent consumption._
