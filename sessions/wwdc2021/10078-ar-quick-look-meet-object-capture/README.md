---
id: "wwdc2021-10078"
event: "wwdc2021"
year: 2021
title: "AR Quick Look, meet Object Capture"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10078"
topics: ["Essentials", "Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# AR Quick Look, meet Object Capture

**Event:** WWDC21 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10078](https://developer.apple.com/videos/play/wwdc2021/10078)

Discover simple ways to bring your Object Capture assets to AR Quick Look while optimizing for visual quality and file size. Explore ways you can integrate AR Quick Look and Object Capture to help create entirely new experiences. To get the most out of this session, we recommend first watching “Advances in AR Quick Look” from WWDC19. You can also learn how to integrate Apple Pay and custom actions with AR on the web through “Shop online with AR Quick Look” from WWDC20.

**Keywords:** `3d model`, `ar`, `arkit`, `augmented reality`, `object capture`, `reality composer`, `realitykit`, `usdz`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,277 words)

## Documentation & Resources

- [Search developer forums for AR Quick Look](https://developer.apple.com/forums/tags/ar-quick-look) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/ar-quick-look
- [Adding an Apple Pay Button or a Custom Action in AR Quick Look](https://developer.apple.com/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look.json
- [AR Quick Look Gallery](https://developer.apple.com/arkit/gallery) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/arkit/gallery
- [ARKit](https://developer.apple.com/documentation/ARKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit.json

## Code Snippets

### Integrating AR Quick Look in your app — [8:02]

```swift
// File: MyPreviewController.swift
func presentARQuickLook() {
	let previewController = QLPreviewController()
	previewController.dataSource = self
	present(previewController, animated: true)
}

// MARK: QLPreviewControllerDataSource
func previewController(
  _ controller: QLPreviewController, previewItemAt index: Int) -> QLPreviewItem {
	  let previewItem = ARQuickLookPreviewItem(fileAt: fileURL) // Local file URL

	  return previewItem
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10078/7/D952E090-6CA8-4748-9B71-385AC16452AF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10078/7/D952E090-6CA8-4748-9B71-385AC16452AF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10078) — developer.apple.com. Indexed for agent consumption._
