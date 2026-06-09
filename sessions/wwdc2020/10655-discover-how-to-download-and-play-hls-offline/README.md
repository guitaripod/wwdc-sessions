---
id: "wwdc2020-10655"
event: "wwdc2020"
year: 2020
title: "Discover how to download and play HLS offline"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10655"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Discover how to download and play HLS offline

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10655](https://developer.apple.com/videos/play/wwdc2020/10655)

Discover how to play HLS audio or video without an internet connection in your app by downloading HLS content for offline consumption using AVFoundation. Explore best practices for working with your HLS content while offline, learn how to use FairPlay Streaming to protect your offline audio and video, and hear updates on our media download policies.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,507 words)

## Documentation & Resources

- [Using AVFoundation to play and persist HTTP live streams](https://developer.apple.com/documentation/AVFoundation/using-avfoundation-to-play-and-persist-http-live-streams) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/using-avfoundation-to-play-and-persist-http-live-streams
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/using-avfoundation-to-play-and-persist-http-live-streams.json

## Code Snippets

### AVAssetDownloadTask — [2:52]

```swift
let hlsAsset = AVURLAsset(url: assetURL)

let backgroundConfiguration = URLSessionConfiguration.background(
    withIdentifier: "assetDownloadConfigurationIdentifier")
let assetURLSession = AVAssetDownloadURLSession(configuration: backgroundConfiguration,
    assetDownloadDelegate: self, delegateQueue: OperationQueue.main())

// Download a Movie at 2 mbps
let assetDownloadTask = assetURLSession.makeAssetDownloadTask(asset: hlsAsset,
    assetTitle: "My Movie", assetArtworkData: myAssetArtwork,
    options: [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: 2000000])!
assetDownloadTask.resume()



// AVAssetDownloadTask uses automatic media selection
```

### Monitor AVAssetDownloadTask — [3:41]

```swift
// Monitor AVAssetDownloadTask
public protocol AVAssetDownloadDelegate: URLSessionTaskDelegate {


	// Use to monitor progress
	func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask,
		didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue],
		timeRangeExpectedToLoad: CMTimeRange)


	// Listen for completion
	func urlSession(_ session: URLSession, task: URLSessionTask,
		didCompleteWithError error: Error?)

}
```

### Monitoring example — [4:10]

```swift
// Monitoring
MyAssetDownloadDelegate: NSObject, AVAssetDownloadDelegate {
    func urlSession(_ session: URLSession, assetDownloadTask: AVAssetDownloadTask,
didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], timeRangeExpectedToLoad: CMTimeRange) {

		// Convert loadedTimeRanges to CMTimeRanges
		var percentComplete = 0.0
		for value in loadedTimeRanges {
			let loadedTimeRange: CMTimeRange = value.timeRangeValue 
			percentComplete += CMTimeGetSeconds(loadedTimeRange.duration) /
				CMTimeGetSeconds(timeRangeExpectedToLoad.duration)
		}
		percentComplete *= 100
		print("percent complete: \(percentComplete)")
	}
}
```

### Choose media-selections — [4:55]

```swift
let hlsAsset = AVURLAsset(url: assetURL)
let myMediaSelections = [] // audio media-selections followed by subtitle media-selections

guard hlsAsset.statusOfValue(forKey: "availableMediaCharacteristicsWithMediaSelectionOptions", error: nil) 
   == AVKeyValueStatus.loaded else { return }

let mediaCharacteristic = //AVMediaCharacteristic.audible or AVMediaCharacteristic.legible
let mediaSelectionGroup = hlsAsset.mediaSelectionGroup(forMediaCharacteristic: mediaCharacteristic)
if let options = mediaSelectionGroup?.options {
    for option in options {
        // chose your media selection option
        if /* this is my option */ {
            let mutableMediaSelection = hlsAsset.preferredMediaSelection.mutableCopy()
            mutableMediaSelection.select(option, in: mediaSelectionGroup)
            myMediaSelections.append(mutableMediaSelection)
        }
    }
}
```

### AVAggregateAssetDownloadTask — [5:11]

```swift
let hlsAsset = AVURLAsset(url: assetURL)
let myMediaSelections = ...

let backgroundConfiguration = URLSessionConfiguration.background(
    withIdentifier: "assetDownloadConfigurationIdentifier")
let assetURLSession = AVAssetDownloadURLSession(configuration: backgroundConfiguration,
    assetDownloadDelegate: self, delegateQueue: OperationQueue.main())

// Download a Movie at 2 mbps
let aggDownloadTask = assetURLSession.aggregateAssetDownloadTask(with: hlsAsset,
    mediaSelections: myMediaSelections,
    assetTitle: "My Movie",
    assetArtworkData: myAssetArtwork,
    options:[AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: 2000000])!
aggDownloadTask.resume()
```

### Monitor AVAggregateAssetDownloadTask — [6:31]

```swift
// Monitor AVAggregateAssetDownloadTask
public protocol AVAssetDownloadDelegate: URLSessionTaskDelegate {

	// Use to monitor progress
	func urlSession(_ session: URLSession, 
		aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, 
		didLoad timeRange: CMTimeRange, totalTimeRangesLoaded loadedTimeRanges: [NSValue], 
		timeRangeExpectedToLoad: CMTimeRange, 
		for mediaSelection: AVMediaSelection
	)

	// Listen for completion for each media selection
	func urlSession(_ session: URLSession, 
		aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, 
		didCompleteFor mediaSelection: AVMediaSelection)

    // In case of audio rendition, expect calls once for stereo followed by once for multichannel rep.
}
```

### Restore Tasks on App Launch — [7:04]

```swift
// Restore Tasks on App Launch
class MyAppDelegate: UIResponder, UIApplicationDelegate {
	func application(_ application: UIApplication, 
			didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
		let configuration = URLSessionConfiguration.background(withIdentifier:
			"assetDownloadConfigurationIdentifier")
		let session = URLSession(configuration: configuration) 
		session.getAllTasks { tasks in
			for task in tasks {
				if let assetDownloadTask = task as? AVAssetDownloadTask {
					// restore progress indicators, state, etc...
				} 
			}
		}
	}
}
```

### Store the download location — [7:44]

```swift
// Store the download location
public protocol AVAssetDownloadDelegate: URLSessionTaskDelegate {

	// AVAssetDownloadTask
	func urlSession(_ session: URLSession, 
		assetDownloadTask: AVAssetDownloadTask, 
		didFinishDownloadingTo location: URL)

	// AVAggregateAssetDownloadTask
	func urlSession(_ session: URLSession, 
		aggregateAssetDownloadTask: AVAggregateAssetDownloadTask, 
		willDownloadTo location: URL)

}
```

### Instantiating Your AVAsset for Playback — [8:05]

```swift
// Instantiating Your AVAsset for Playback

// 1) Create Asset for AVAssetDownloadTask
let networkURL = URL(string: "http://example.com/master.m3u8")!
let asset = AVURLAsset(url: networkURL)
let task = assetDownloadSession.makeAssetDownloadTask(asset: asset, assetTitle: "My Movie",
assetArtworkData: nil, options: nil)


// 2) Re-use Asset for Playback, Even After Task Restoration at App Launch
let playerItem = AVPlayerItem(asset: task.urlAsset)


// Reusing asset, will allow AVFoundation to optimize resources between playback and download in cases where the playback happens before the download is complete.
```

### Create using file URL — [8:56]

```swift
// Create using file URL

let fileURL = URL(fileURLWithPath: self.savedAssetDownloadLocation)
let asset = AVURLAsset(url: fileURL)

let playerItem = AVPlayerItem(asset: task.urlAsset)
```

### What can I play offline? — [9:16]

```swift
// What can I play offline?

public class AVURLAsset {

	public var assetCache: AVAssetCache? { get }

}

public class AVAssetCache {

	public var isPlayableOffline: Bool { get }

	public func mediaSelectionOptions(in mediaSelectionGroup: AVMediaSelectionGroup)
		-> [AVMediaSelectionOption]

}
```

### Invalidate Offline Key — [11:33]

```swift
// Invalidate Offline Key

public class AVContentKeySession {

	func invalidatePersistableContentKey(_ persistableContentKeyData: Data, 
		options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil, 
		completionHandler handler: @escaping (Data?, Error?) -> Void)


	func invalidateAllPersistableContentKeys(forApp appIdentifier: Data, 
		options: [AVContentKeySessionServerPlaybackContextOption : Any]? = nil, 
		completionHandler handler: @escaping (Data?, Error?) -> Void)


}
```

### Quality Selection — [13:54]

```swift
// Quality Selection

public class AVAssetDownloadTask {

	public let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String

	//Starting in iOS 14

	public let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String

	public let AVAssetDownloadTaskPrefersHDRKey: String

}
```

### Multichannel Audio Selection — [14:30]

```swift
// Multichannel Audio Selection

public class AVAssetDownloadTask {

	public let AVAssetDownloadTaskPrefersMultichannelKey: String

}
```

### AVAssetDownloadStorageManager — [15:51]

```swift
// AVAssetDownloadStorageManager 
// Get the singleton 
let storageManager = AVAssetDownloadStorageManager.shared()

// Create the policy 
let newPolicy = AVMutableAssetDownloadStorageManagementPolicy() 

newPolicy.expirationDate = myExpiryDate

newPolicy.priority = .important 

// Set the policy
storageManager.setStorageManagementPolicy(newPolicy, forURL: myDownloadStorageURL)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10655/3/45C0E27F-A3BA-416D-B037-9BEE7466C11F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10655) — developer.apple.com. Indexed for agent consumption._
