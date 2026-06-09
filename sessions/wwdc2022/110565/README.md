---
id: "wwdc2022-110565"
event: "wwdc2022"
year: 2022
title: "Display HDR video in EDR with AVFoundation and Metal"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110565"
topics: ["Audio & Video", "Photos & Camera", "SwiftUI & UI Frameworks", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Display HDR video in EDR with AVFoundation and Metal

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-110565](https://developer.apple.com/videos/play/wwdc2022/110565)

Learn how you can take advantage of AVFoundation and Metal to build an efficient EDR pipeline. Follow along as we demonstrate how you can use AVPlayer to display HDR video as EDR, add playback into an app view, render it with Metal, and use Core Image or custom Metal shaders to add video effects such as keying or color management. Whether you develop games or pro apps, we'll help you decide which frameworks to use and share best practices for selecting transports, colorspaces, and pixelbuffer formats.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,090 words)

## Documentation & Resources

- [Learn more about AVFoundation](https://developer.apple.com/av-foundation/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/av-foundation/

## Code Snippets

### Playing media using AVPlayerViewController — [6:58]

```swift
// Playing media using AVPlayerViewController
let player = AVPlayer(URL: videoURL)

// Creating a player view controller
var playerViewController = AVPlayerViewController()

playerViewController.player = player

self.presentViewController(playerViewController, animated: true) {
   playerViewController.player!.play()
}
```

### Playing media using AVPlayer and AVPlayerLayer — [7:38]

```swift
// Playing media using AVPlayer and AVPlayerLayer
let player = AVPlayer(URL: videoURL)

var playerLayer = AVPlayerLayer(player: player)

playerLayer.frame = self.view.bounds

self.view.layer.addSublayer(playerLayer)

player.play()
```

### CAMetalLayer Properties — [9:28]

```swift
// Opt into using EDR
let layer: CAMetalLayer
layer.wantsExtendedDynamicRangeContent = true

// Use half-float pixel format
layer.pixelFormat = MTLPixelFormatRGBA16Float

// Use extended linear display P3 color space
layer.colorspace = kCGColorSpaceExtendedLinearDisplayP3
```

### Create an AVPlayerItemVideoOutput — [11:33]

```swift
let videoColorProperties = [
    AVVideoColorPrimariesKey: AVVideoColorPrimaries_P3_D65,
    AVVideoTransferFunctionKey: AVVideoTransferFunction_Linear,
    AVVideoYCbCrMatrixKey: AVVideoYCbCrMatrix_ITU_R_2020
]

let outputVideoSettings = [
    AVVideoAllowWideColorKey: true,
    AVVideoColorPropertiesKey: videoColorProperties,
    kCVPixelBufferPixelFormatTypeKey as String: NSNumber(value: kCVPixelFormatType_64RGBAHalf)
] as [String : Any]

// Create a player item video output
let videoPlayerItemOutput 
= AVPlayerItemVideoOutput(outputSettings: outputVideoSettings)
```

### Create a display link — [13:02]

```swift
// Create a display link
lazy var displayLink: CADisplayLink 
= CADisplayLink(target: self, 
                selector: #selector(displayLinkCopyPixelBuffers(link:)))

var statusObserver: NSKeyValueObservation?

statusObserver = videoPlayerItem.observe(\.status,
      options: [.new, .old],
      changeHandler: { playerItem, change in
        if playerItem.status == .readyToPlay {
          playerItem.add(videoPlayerItemOutput)
          displayLink.add(to: .main, forMode: .common)
          videoPlayer?.play()
        }
     })
}
```

### Run DisplayLink to get pixel buffers — [14:16]

```swift
@objc func displayLinkCopyPixelBuffers(link: CADisplayLink) 
{
  let currentTime = videoPlayerItemOutput.itemTime(forHostTime: CACurrentMediaTime())

  if videoPlayerItemOutput.hasNewPixelBuffer(forItemTime: currentTime)
  {
      if let buffer 
      = videoPlayerItemOutput.copyPixelBuffer(forItemTime: currentTime, 
	                                          itemTimeForDisplay: nil) 
	  {
        let image = CIImage(cvPixelBuffer: buffer!)

        let filter = CIFilter.sepiaTone()
        filter.inputImage = image
        output = filter.outputImage ?? CIImage.empty()

        // use context to render to you CIRenderDestination
     }
 }
}
```

### Integrate Core Image — [15:53]

```swift
@objc func displayLinkCopyPixelBuffers(link: CADisplayLink) 
{
  let currentTime = videoPlayerItemOutput.itemTime(forHostTime: CACurrentMediaTime())

  if videoPlayerItemOutput.hasNewPixelBuffer(forItemTime: currentTime)
  {
      if let buffer 
      = videoPlayerItemOutput.copyPixelBuffer(forItemTime: currentTime, 
	                                          itemTimeForDisplay: nil) 
	  {
        let image = CIImage(cvPixelBuffer: buffer)

        let filter = CIFilter.sepiaTone()
        filter.inputImage = image
        output = filter.outputImage ?? CIImage.empty()

        // use context to render to your CIRenderDestination
     }
  }
}
```

### Using CVMetalTextureCache — [19:13]

```swift
// Create a CVMetalTextureCacheRef

let mtlDevice = MTLCreateSystemDefaultDevice()

var mtlTextureCache: CVMetalTextureCache? = nil

CVMetalTextureCacheCreate(allocator: kCFAllocatorDefault, 
                          cacheAttributes: nil, 
                          metalDevice: mtlDevice, 
                          textureAttributes: nil, 
                          cacheOut: &mtlTextureCache)

// Create a CVMetalTextureRef using metalTextureCache and our pixelBuffer
let width  = CVPixelBufferGetWidth(pixelBuffer)
let height = CVPixelBufferGetHeight(pixelBuffer)

var cvTexture : CVMetalTexture? = nil

CVMetalTextureCacheCreateTextureFromImage(allocator: kCFAllocatorDefault, 
                                          textureCache: mtlTextureCache, 
                                          sourceImage: pixelBuffer, 
                                          textureAttributes: nil, 
                                          pixelFormat: MTLPixelFormatRGBA16Float, 
                                          width: width, 
                                          height: height, 
                                          planeIndex: 0, 
                                          textureOut: &cvTexture)

let texture = CVMetalTextureGetTexture(cvTexture)

// In Obj-C, release CVMetalTextureRef in Metal command buffer completion handlers
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110565/4/46CD2F39-5184-416E-A4F4-E57AEAF92AC8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110565/4/46CD2F39-5184-416E-A4F4-E57AEAF92AC8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110565) — developer.apple.com. Indexed for agent consumption._