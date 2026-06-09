---
id: "wwdc2021-10160"
event: "wwdc2021"
year: 2021
title: "Capture and process ProRAW images"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10160"
topics: ["Graphics & Games", "Photos & Camera"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Capture and process ProRAW images

**Event:** WWDC21 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10160](https://developer.apple.com/videos/play/wwdc2021/10160)

When you support ProRAW in your app, you can help photographers easily capture and edit images by combining standard RAW information with Apple’s advanced computational photography techniques. We’ll take you through an overview of the format, including the look and feel of ProRAW images, quality metrics, and compatibility with your app. From there, we’ll explore how you can incorporate ProRAW into your app at every stage of the production pipeline, including capturing imagery with AVFoundation, storage using PhotoKit, and editing with Core Image.

**Keywords:** `coreimage`, `filters`, `photo effects`, `photography`, `photos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,111 words)

## Documentation & Resources

- [Capturing still and Live Photos](https://developer.apple.com/documentation/AVFoundation/capturing-still-and-live-photos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-still-and-live-photos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-still-and-live-photos.json
- [Capturing photos in RAW and Apple ProRAW formats](https://developer.apple.com/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capturing-photos-in-raw-and-apple-proraw-formats.json
- [PhotoKit](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json
- [Core Image](https://developer.apple.com/documentation/CoreImage) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreImage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreImage.json
- [Photos](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json
- [Capture setup](https://developer.apple.com/documentation/AVFoundation/capture-setup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/capture-setup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/capture-setup.json

## Code Snippets

### Setting up device and session — [7:52]

```swift
// Use the .photo preset

private let session = AVCaptureSession()
private func configureSession() {
  session.beginConfiguration()
	session.sessionPreset = .photo
	//...
}
```

### Setting up device and session — [8:03]

```swift
// Or optionally find a format that supports highest quality photos

guard let format = device.formats.first(where: { $0.isHighestPhotoQualitySupported }) else {
  // handle failure to find a format that supports highest quality stills
} 
do 
{	
  try device.lockForConfiguration()
  {
    // ...
  }
  device.unlockForConfiguration()
} 
catch 
{
  // handle the exception
}
```

### Setting up photo output 1 — [8:39]

```swift
// Enable ProRAW on the photo output

private let photoOutput = AVCapturePhotoOutput()
private func configurePhotoOutput() {
  photoOutput.isHighResolutionCaptureEnabled = true
	photoOutput.isAppleProRAWEnabled = photoOutput.isAppleProRAWSupported
	//...
}
```

### Setting up photo output 2 — [8:59]

```swift
// Select the desired photo quality prioritization

private let photoOutput = AVCapturePhotoOutput()
private func configurePhotoOutput() {
	photoOutput.isHighResolutionCaptureEnabled = true
	photoOutput.isAppleProRAWEnabled           = photoOutput.isAppleProRAWSupported
	photoOutput.maxPhotoQualityPrioritization  = .quality // or .speed .balanced
  //...
}
```

### Prepare for ProRAW capture 1 — [9:26]

```swift
// Find a supported ProRAW pixel format

guard let proRawPixelFormat = photoOutput.availableRawPhotoPixelFormatTypes.first(
  where: {
    AVCapturePhotoOutput.isAppleProRAWPixelFormat($0) 
  }) 
else {
	// Apple ProRAW is not supported with this device / format
}

// For Bayer RAW pixel format use

AVCapturePhotoOutput.isBayerRAWPixelFormat()
```

### Prepare for ProRAW capture 2 — [10:09]

```swift
// Create photo settings for ProRAW only capture

let photoSettings = AVCapturePhotoSettings(rawPixelFormatType: proRawPixelFormat)

// Create photo settings for processed photo + ProRAW capture

guard let processedPhotoCodecType = photoOutput.availablePhotoCodecTypes.first 
else 
{
	// handle failure to find a processed photo codec type
}
let photoSettings = AVCapturePhotoSettings(rawPixelFormatType: proRawPixelFormat,
	processedFormat: [AVVideoCodecKey: processedPhotoCodecType])
```

### Prepare for ProRAW capture 3 — [10:53]

```swift
// Select a supported thumbnail codec type and thumbnail dimensions

guard let thumbnailPhotoCodecType = photoSettings.availableRawEmbeddedThumbnailPhotoCodecTypes.first 
else 
{
  // handle failure to find an available thumbnail photo codec type
}

let dimensions = device.activeFormat.highResolutionStillImageDimensions

photoSettings.rawEmbeddedThumbnailPhotoFormat = [
  AVVideoCodecKey: thumbnailPhotoCodecType,
  AVVideoWidthKey: dimensions.width,
  AVVideoHeightKey: dimensions.height]
```

### Prepare for ProRAW capture 4 — [11:08]

```swift
// Select the desired quality prioritization for the capture

photoSettings.photoQualityPrioritization = .quality // or .speed .balanced

// Optionally, request a preview image

if let previewPixelFormat = photoSettings.availablePreviewPhotoPixelFormatTypes.first
{	
  photoSettings.previewPhotoFormat = [kCVPixelBufferPixelFormatTypeKey as String: previewPixelFormat]
}

// Capture!

photoOutput.capturePhoto(with: photoSettings, delegate: delegate)
```

### Consuming captured ProRAW 1 — [11:44]

```swift
func photoOutput(_ output: AVCapturePhotoOutput,
                 didFinishProcessingPhoto photo: AVCapturePhoto,
                 error: Error?) 
{
  guard error == nil 
  else 
  {
    // handle failure from the photo capture
  }
	if let preview = photo.previewPixelBuffer 
  { 
    // photo.previewCGImageRepresentation()
    // display the preview
  }
	if photo.isRawPhoto 
  {
		guard let proRAWFileDataRepresentation = photo.fileDataRepresentation() 
    else 
    {
      // handle failure to get ProRAW DNG file data representation
    }
		guard let proRAWPixelBuffer = photo.pixelBuffer 
    else 
    {
      // handle failure to get ProRAW pixel data
    }
		// use the file or pixel data
	}
```

### Consuming captured ProRAW 2 — [12:52]

```swift
// Provide settings for lossless compression with less bits

class AppleProRAWCustomizer: NSObject, AVCapturePhotoFileDataRepresentationCustomizer 
{
	func replacementAppleProRAWCompressionSettings(for photo: AVCapturePhoto,
                                                 defaultSettings: [String : Any],
                                                 maximumBitDepth: Int) -> [String : Any] 
  {
    return [AVVideoAppleProRAWBitDepthKey: min(10, maximumBitDepth),
            AVVideoQualityKey: 1.00]
  }
}
```

### Consuming captured ProRAW 3 — [13:35]

```swift
// Provide settings for lossy compression

class AppleProRAWCustomizer: NSObject, AVCapturePhotoFileDataRepresentationCustomizer 
{
	func replacementAppleProRAWCompressionSettings(
    for photo: AVCapturePhoto,
    defaultSettings: [String : Any],
    maximumBitDepth: Int) -> [String : Any] 
  {
    return [AVVideoAppleProRAWBitDepthKey: min(8, maximumBitDepth),
            AVVideoQualityKey: 0.90]
  }
}
```

### Consuming captured ProRAW 4 — [13:51]

```swift
// Customizing the compression settings for the captured ProRAW photo

func photoOutput(_ output: AVCapturePhotoOutput,
                 didFinishProcessingPhoto photo: AVCapturePhoto,
                 error: Error?) 
{
  guard error == nil 
  else 
  {
    // handle failure from the photo capture
  }
    if photo.isRawPhoto 
  {
		let customizer = AppleProRAWCustomizer()
		guard let customizedFileData = photo.fileDataRepresentation(with: customizer) 
    else 
    {
      // handle failure to get customized ProRAW DNG file data representation
    }
		// use the file data
	}
```

### Saving a ProRAW asset with PhotoKit — [15:19]

```swift
PHPhotoLibrary.shared().performChanges 
{
    let creationRequest = PHAssetCreationRequest.forAsset()

    creationRequest.addResource(with:.photo, 
                                fileURL:proRawFileURL, 
                                options:nil)
} 
completionHandler: 
{ 
  success, error in
  // handle the success and possible error
}
```

### Fetching RAW assets from the photo library — [15:45]

```swift
// New enum PHAssetCollectionSubtype.smartAlbumRAW

PHAssetCollection.fetchAssetCollections(with: .smartAlbum, 
                                        subtype: .smartAlbumRAW, 
                                        options: nil)
```

### Retrieving RAW resources from a PHAsset — [17:16]

```swift
let resources = PHAssetResource.assetResources(for: asset)
for resource in resources 
{
  if (resource.type == .photo || resource.type == .alternatePhoto) 
  {
    if let resourceUTType = UTType(resource.uniformTypeIdentifier) 
    {
      if resourceUTType.conforms(to: UTType.rawImage) 
      {
        let resourceManager = PHAssetResourceManager.default()
        resourceManager.requestData(for: resource, options: nil) 
        { 
          data in
          // use the data
        } 
        completionHandler: 
        { 
          error in
          // handle any error 
        }
      }
    }
  }
}
```

### Getting CIImages from a ProRAW — [18:28]

```swift
// Getting the preview image

let isrc  = CGImageSourceCreateWithURL(url as CFURL, nil)
let cgimg = CGImageSourceCreateThumbnailAtIndex(isrc!, 0, nil)

return CIImage(cgImage: cgimg)
```

### Getting CIImages from a ProRAW  2 (New in iOS 15 and macOS 12) — [18:36]

```swift
// Getting the preview image

let rawFilter = CIRAWFilter(imageURL: url)

return rawFilter.previewImage
```

### Getting CIImages from a ProRAW 3 — [18:44]

```swift
// Getting the preview image

let rawFilter = CIRAWFilter(imageURL: url)

return rawFilter.previewImage

// Getting segmentation mattes images

return CIImage(contentsOf: url,
               options: [.auxiliarySemanticSegmentationSkinMatte : true])
```

### Getting CIImages from a ProRAW 4 — [18:56]

```swift
// Getting the preview image

let rawFilter = CIRAWFilter(imageURL: url)

return rawFilter.previewImage

// Getting segmentation mattes images

let rawFilter = CIRAWFilter(imageURL: url)

return rawFilter.semanticSegmentationSkinMatte
```

### Getting CIImages from a ProRAW 5 — [19:09]

```swift
// Getting the primary image

return CIImage(contentsOf: url, options:nil)

let rawFilter = CIFilter(imageURL: url, options:nil)

return rawFilter.outputImage
```

### Applying common user adjustments — [19:31]

```swift
func get_adjusted_raw_image (url: URL) -> CIImage?
{
    // Load the image
    let rawFilter = CIFilter(imageURL: url, options:nil)

    // Change one or more filter inputs
    rawFilter.setValue(value, forKey: CIRAWFilterOption.keyName.rawValue)

    // Get the adjusted image
    return rawFilter.outputImage
}
```

### Applying common user adjustments 2 — [19:54]

```swift
func get_adjusted_raw_image (url: URL) -> CIImage?
{
    // Load the image
    let rawFilter = CIRAWFilter(imageURL: url)

    // Change one or more filter inputs
    rawFilter.property = value

    // Get the adjusted image
    return rawFilter.outputImage
}
```

### Applying common user adjustments 3 — [20:17]

```swift
// Exposure

rawFilter.exposure = -1.0

// Temperature and tint

rawFilter.neutralTemperature = 6500  // in °K
rawFilter.neutralTint        = 0.0

// Sharpness

rawFilter.sharpnessAmount = 0.5

// Local tone map strength

rawFilter.localToneMapAmount = 0.5
```

### Getting linear scene-referred output 1 — [21:40]

```swift
// Turn off the filter inputs that apply the default look to the RAW

rawFilter.baselineExposure      = 0.0
rawFilter.shadowBias            = 0.0
rawFilter.boostAmount           = 0.0
rawFilter.localToneMapAmount    = 0.0
rawFilter.isGamutMappingEnabled = false

let linearRawImage = rawFilter.outputImage
```

### Getting linear scene-referred output 2 — [22:00]

```swift
// Use the linear image with other filters

let histogram = CIFilter.areaHistogram()

histogram.inputImage = linearRawImage
histogram.extent     = linearRawImage.extent

// Or render it to a RGBAh buffer

let rd = CIRenderDestination(bitmapData: data.mutableBytes,
                             width: 􀠪imageWidth, 
                             height: 􀠪imageHeight, 
                             bytesPerRow: 􀠪rowBytes,
                             format: .RGBAh)

rd.colorSpace = CGColorSpace(name: CGColorSpace.extendedLinearITUR_2020)

let task = context.startTask(toRender: rawFilter.outputImage, 
                             from: rect, 
                             to: rd, 
                             at: point)

task.waitUntilCompleted()
```

### Saving edits to other file formats 1 (8-bit HEIC) — [23:54]

```swift
// Saving to 8-bit HEIC

try ciContext.writeHEIFRepresentation(of: rawFilter!.outputImage!,
                                      to: theURL,
                                      format: .RGBA8,
                                      colorSpace: CGColorSpace(name: CGColorSpace.displayP3)!,
                                      options: [:])
```

### Saving edits to other file formats 2 (10-bit HEIC) — [24:12]

```swift
// Saving to 10-bit HEIC

try ciContext.writeHEIF10Representation(of: rawFilter!.outputImage!,
                                        to: theURL,
                                        format: .RGBA8,
                                        colorSpace: CGColorSpace(name: CGColorSpace.displayP3)!, 
                                        options: [:])
```

### Displaying to a Metal Kit View in EDR on Mac — [24:51]

```swift
class MyView : MTKView {
  var context: CIContext
  var commandQueue: MTLCommandQueue
  //...
}
```

### Displaying to a Metal Kit View in EDR on Mac — [25:13]

```swift
// Create a Metal Kit View subclass

class MyView : MTKView {
  var context: CIContext
  var commandQueue: MTLCommandQueue
  //...
}

// Init your Metal Kit View for EDR

colorPixelFormat = MTLPixelFormat.rgba16Float

if let caml = layer as? CAMetalLayer {
  caml.wantsExtendedDynamicRangeContent = true
  //...
}

// Ask the filter for an image designed for EDR and render it

rawFilter.extendedDynamicRangeAmount = 1.0

context.startTask(toRender: rawFilter.outputImage, 
                  from: rect, 
                  to: rd, 
                  at: point)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10160/6/08FEC739-8354-4B2F-B06F-F7F8FCD5E6ED/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10160/6/08FEC739-8354-4B2F-B06F-F7F8FCD5E6ED/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10160) — developer.apple.com. Indexed for agent consumption._