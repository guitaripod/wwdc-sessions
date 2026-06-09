---
id: "wwdc2025-325"
event: "wwdc2025"
year: 2025
title: "Discover Apple-Hosted Background Assets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/325"
topics: ["App Services", "App Store, Distribution & Marketing", "Graphics & Games", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Discover Apple-Hosted Background Assets

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-325](https://developer.apple.com/videos/play/wwdc2025/325)

Building on Background Assets, this session will introduce the new capability to download asset packs of content for games and other applications. Learn how Apple can host these asset packs for you or how to manage self-hosting options. We’ll delve into the native API integration and the corresponding App Store implementations, providing you with the tools to enhance your app’s content delivery and user experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,361 words)

## Documentation & Resources

- [Background assets](https://developer.apple.com/documentation/AppStoreConnectAPI/background-assets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppStoreConnectAPI/background-assets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppStoreConnectAPI/background-assets.json
- [Testing asset packs locally](https://developer.apple.com/documentation/BackgroundAssets/testing-asset-packs-locally) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundAssets/testing-asset-packs-locally
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundAssets/testing-asset-packs-locally.json
- [Maximum build file sizes](https://developer.apple.com/help/app-store-connect/reference/maximum-build-file-sizes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/help/app-store-connect/reference/maximum-build-file-sizes
- [Overview of Apple-hosted asset packs](https://developer.apple.com/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs

## Code Snippets

### Fill out the manifest — [8:26]

```json
{
	"assetPackID": "[Asset-Pack ID]",
	"downloadPolicy": {
		"essential": { // Possible keys: “essential”, “prefetch”, or “onDemand”
			// Essential and prefetch download policies require a list of installation event types. For an on-demand download policy, the value for the “onDemand” key must be an empty object.
			"installationEventTypes": [
				// Remove undesired elements from this array.
				"firstInstallation",
				"subsequentUpdate"
			]
		}
	},
	"fileSelectors": [
		// You can add as many file and/or directory selectors as you want.
		{
			"file": "[Path to File]"
		},
		{
			"directory": "[Path to Directory]"
		}
	],
	"platforms": [
		// Remove undesired elements from this array.
		"iOS",
		"macOS",
		"tvOS",
		"visionOS"
	]
}
```

### Add a downloader extension — [10:44]

```swift
import BackgroundAssets
import ExtensionFoundation
import StoreKit

@main
struct DownloaderExtension: StoreDownloaderExtension {

	func shouldDownload(_ assetPack: AssetPack) -> Bool {
		return true
	}

}
```

### Download an asset pack — [11:39]

```swift
let assetPack = try await AssetPackManager.shared.assetPack(withID: "Tutorial")

// Await status updates for progress information
let statusUpdates = AssetPackManager.shared.statusUpdates(forAssetPackWithID: "Tutorial")
Task {
	for await statusUpdate in statusUpdates {
		// …
  }
}

// Download the asset pack
try await AssetPackManager.shared.ensureLocalAvailability(of: assetPack)
```

### Receive download status updates in Objective-C — [12:22]

```objectivec
#import <BackgroundAssets/BackgroundAssets.h>

@interface ManagedAssetPackDownloadDelegate : NSObject <BAManagedAssetPackDownloadDelegate>

@end

@implementation ManagedAssetPackDownloadDelegate

- (void)downloadOfAssetPackBegan:(BAAssetPack *)assetPack { /* … */ }

- (void)downloadOfAssetPackPaused:(BAAssetPack *)assetPack { /* … */ }

- (void)downloadOfAssetPackFinished:(BAAssetPack *)assetPack { /* … */ }

- (void)downloadOfAssetPack:(BAAssetPack *)assetPack hasProgress:(NSProgress *)progress { /* … */ }

- (void)downloadOfAssetPack:(BAAssetPack *)assetPack failedWithError:(NSError *)error { /* … */ }

@end
```

### Attach the delegate in Objective-C — [12:29]

```objectivec
static void attachDelegate(ManagedAssetPackDownloadDelegate *delegate) {
	[[BAAssetPackManager sharedManager] setDelegate:delegate];
}
```

### Cancel an asset-pack download — [12:33]

```swift
let statusUpdates = AssetPackManager.shared.statusUpdates(forAssetPackWithID: "Tutorial")
for await statusUpdate in statusUpdates {
	if case .downloading(_, let progress) = statusUpdate {
		progress.cancel()
	}
}
```

### Use an asset pack — [12:41]

```swift
// Read a file into memory
let videoData = try AssetPackManager.shared.contents(at: "Videos/Introduction.m4v")

// Open a file descriptor
let videoDescriptor = try AssetPackManager.shared.descriptor(for: "Videos/Introduction.m4v")
defer {
	do {
		try videoDescriptor.close()
	} catch {
		// …
	}
}
```

### Remove an asset pack — [13:56]

```swift
// Remove the asset pack
try await AssetPackManager.shared.remove(assetPackWithID: "Tutorial")

// Redownload the asset pack
let assetPack = try await AssetPackManager.shared.assetPack(withID: "Tutorial")
try await AssetPackManager.shared.ensureLocalAvailability(of: assetPack)
```

### Info.plist — [14:53]

```xml
<key>BAAppGroupID</key>
<string>group.com.naturelab.thecoast</string>
<key>BAHasManagedAssetPacks</key>
<true/>
<key>BAUsesAppleHosting</key>
<true/>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/325/6/cda561c7-42e2-4bcb-a7a2-e52259a23c5d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/325/6/cda561c7-42e2-4bcb-a7a2-e52259a23c5d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/325) — developer.apple.com. Indexed for agent consumption._
