---
id: "wwdc2022-110403"
event: "wwdc2022"
year: 2022
title: "Meet Background Assets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110403"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet Background Assets

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110403](https://developer.apple.com/videos/play/wwdc2022/110403)

Discover how you can use the Background Assets framework to download large files directly from your CDN and improve the initial launch experience of your apps and games. We’ll show you how to schedule background downloads during initial app install, app updates, and periodically as someone uses the app. We’ll also explore how you can manage scheduled downloads to make sure people have the content they want, when they want it.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,825 words)

## Documentation & Resources

- [NSBundleResourceRequest](https://developer.apple.com/documentation/Foundation/NSBundleResourceRequest) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/NSBundleResourceRequest
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/NSBundleResourceRequest.json
- [Background Assets](https://developer.apple.com/documentation/BackgroundAssets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundAssets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundAssets.json

## Code Snippets

### Getting started with Background Assets — [5:28]

```swift
// Getting started with Background Assets
import BackgroundAssets

let url = URL(string: "https://cdn.example.com/large-asset.bin")!
let appGroupIdentifier = "group.WWDC.AssetContainer"
let download = BAURLDownload ( identifier: "Large-Asset",
                               request: URLRequest(url:url),
                               applicationGroupIdentifier:
                                appGroupIdentifier )

let manager = BADownloadManager.shared
manager.delegate = self  // BADownloadManagerDelegate protocol

// Schedule download at an opportunistic time determined by the system
do {
    try manager.schedule(download)
} catch {
    print("Failed to schedule download. \(error)")
}

// or Schedule download in foreground
do {
    try manager.startForegroundDownload(download)
} catch {
    print("Failed to start foreground download. \(error)")
}

// or Promote downloads to foreground.
do {
    for download in try await manager.fetchCurrentDownloads) {
       try manager.startForegroundDownload(download)
    }
} catch {
    print("Failed to promote downloads to foreground \(error)")
}
```

### BADownloadManager delegate protocol — [10:28]

```swift
// BADownloadManager protocol definition
public protocol BADownloadManagerDelegate : NSObjectProtocol {
    optional func downloadDidBegin(_ download: BADownload)

    optional func downloadDidPause(_ download: BADownload)

    optional func download(_ download: BADownload,
                           bytesWritten: Int64,
                           totalBytesWritten: Int64,
                           totalExpectedBytes: Int64)

    optional func download(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)

    optional func download(_ download: BADownload, failedWithError error: Error)

    optional func download(_ download: BADownload, finishedWithFileURL fileURL: URL)
}
```

### BADownloaderExtension protocol — [15:37]

```swift
// BADownloaderExtension protocol definition
public protocol BADownloaderExtension : NSObjectProtocol {
    optional func applicationDidInstall(metadata: BAApplicationExtensionInfo)

    optional func applicationDidUpdate(metadata: BAApplicationExtensionInfo)

    optional func checkForUpdates(metadata: BAApplicationExtensionInfo)

    optional func download(_ download: BADownload, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)

    optional func backgroundDownloadDidFail(failedDownload: BADownload)

    optional func backgroundDownloadDidFinish(finishedDownload: BADownload, fileURL: URL)

    optional func extensionWillTerminate()
}
```

### Synchronizing between app and extension — [19:40]

```swift
// Synchronizing between app and extension
func download(_ download: BADownload, finishedWithFileURL fileURL: URL) {
    let manager = BADownloadManager.shared
    manager.withExclusiveControl { error in
        guard error == nil else {
            print("Unable to acquire exclusive control \(String(describing: error))")
            return
        }
        // Exclusive control acquired
        // All code in this scope ensures mutual exclusion between extension and app
        do {
            let data = try Data(contentsOf: fileURL, options: .mappedIfSafe)
            // Do something with memory mapped data
            try FileManager.default.removeItem(at: fileURL)
        } catch {
            print("Unable to read/cleanup file data. \(error)")
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110403/3/7B38146A-41F4-422B-A863-6E4277C76C6E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110403/3/7B38146A-41F4-422B-A863-6E4277C76C6E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110403) — developer.apple.com. Indexed for agent consumption._