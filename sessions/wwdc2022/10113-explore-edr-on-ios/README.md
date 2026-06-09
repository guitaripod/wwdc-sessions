---
id: "wwdc2022-10113"
event: "wwdc2022"
year: 2022
title: "Explore EDR on iOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10113"
topics: ["Audio & Video", "Photos & Camera", "SwiftUI & UI Frameworks", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Explore EDR on iOS

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10113](https://developer.apple.com/videos/play/wwdc2022/10113)

EDR is Apple's High Dynamic Range representation and rendering pipeline. Explore how you can render HDR content using EDR in your app and unleash the dynamic range capabilities of HDR displays on iPhone and iPad. We'll show how you can take advantage of the native EDR APIs on iOS, provide best practices to help you decide when HDR is appropriate, and share tips for tone-mapping and HDR content rendering. We'll also introduce you to Reference Mode and highlight how it provides a reference response to enable color-critical workflows such as color grading, editing, and content review.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,725 words)

## Documentation & Resources

- [CAEDRMetadata](https://developer.apple.com/documentation/QuartzCore/CAEDRMetadata) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/QuartzCore/CAEDRMetadata
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/QuartzCore/CAEDRMetadata.json

## Code Snippets

### Create CGImage and Draw — [9:23]

```swift
// Create CGImage from HDR Image
let isr = CGImageSourceCreateWithURL(HDRImageURL, nil)
let img = CGImageSourceCreateImageAtIndex(isr, 0, nil)

// Draw into floating point bitmap context
let width  = img.width
let height = img.height

let info = CGBitmapInfo(rawValue: kCGBitmapByteOrder16Host |CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.floatComponents.rawValue)

let ctx = CGContext(data: nil, width: width, height: height, bitsPerComponent: 16,
    bytesPerRow: 0, space: layer.colorspace, bitmapInfo: info.rawValue)

ctx?.draw(in: img,
          image: CGRect(x: 0, y: 0, width: CGFloat(width), height: CGFloat(height)))
```

### Create floating point texture and Load EDR bitmap — [10:30]

```swift
// Create floating point texture
let desc = MTLTextureDescriptor()

desc.pixelFormat = .rgba16Float
desc.textureType = .type2D

let texture = layer.device.makeTexture(descriptor: desc)

// Load EDR bitmap into texture
let data = ctx.data

texture.replace(region: MTLRegionMake2D(0, 0, width, height),
                mipmapLevel: 0,
                withBytes: &data,
                bytesPerRow: ctx.bytesPerRow)
```

### CAMetalLayer properties — [11:55]

```swift
// Opt into using EDR
var layer = CAMetalLayer()
layer?.wantsExtendedDynamicRangeContent = true

// Use supported pixel format and color spaces
layer.pixelFormat = MTLPixelFormatRGBA16Float
layer.colorspace  = CGColorSpace(name: kCGColorSpaceExtendedLinearDisplayP3)
```

### UIScreen headroom — [14:42]

```swift
// Query potential headroom
let screen = windowScene.screen
let maxPotentialEDR = screen.potentialEDRHeadroom
if (maxPotentialEDR < 1.5) {
    // SDR path
}

// Query current headroom
func draw(_ rect: CGRect) {
    let maxEDR = screen.currentEDRHeadroom
    // Tone-map to maxEDR
}

// Register for Reference Mode notifications
let notification = NotificationCenter.default
notification.addObserver(self,
                         selector: #selector(screenChangedEvent(_:)),
                         name: UIScreen.referenceDisplayModeStatusDidChangeNotification,
                         object: nil)

// Query for latest status and headroom
func screenChangedEvent(_ notification: Notification?) {
    let status          = screen.referenceDisplayModeStatus
    let maxPotentialEDR = screen.potentialEDRHeadroom
}
```

### CAEDRMetadata and CAMetalLayer — [16:54]

```swift
// Check if EDR metadata is available
let isAvailable = CAEDRMetadata.isAvailable

// Instantiate EDR metadata
// ...

// Apply EDR metadata to layer
let layer: CAMetalLayer? = nil
layer?.edrMetadata = metadata
```

### Instantiating CAEDRMetadata — [17:22]

```swift
// HLG
let edrMetadata = CAEDRMetadata.hlg

// HDR10 (Mastering Display luminance)
let edrMetaData = CAEDRMetadata.hdr10(minLuminance: minLuminance,
                                      maxLuminance: maxContentMasteringDisplayBrightness,
                                      opticalOutputScale: outputScale)

// HDR10 (Supplemental Enhancement Information)
let edrMetaData = CAEDRMetadata.hdr10(displayInfo: displayData,
                                      contentInfo: contentInfo,
                                      opticalOutputScale: outputScale)
```

## Video

- HLS stream: https://events-delivery.apple.com/wwdc22/S6609-rUNWRhfHEGjdhBffWQLkyEHB/cmaf.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10113) — developer.apple.com. Indexed for agent consumption._
