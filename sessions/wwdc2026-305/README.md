# Enhance RAW image processing with Core Image

**Topic:** Photos & Camera · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-305](https://developer.apple.com/videos/play/wwdc2026/305)

Harness the power of version 9 of the Core Image RAW processing APIs to dramatically improve image quality in your apps, with improved sharpness and more defined color, while using the Apple Neural Engine for optimal performance. Take advantage of the CIRAWFilter API to let your users edit RAW photos by changing exposure, noise reduction, sharpness, contrast and more. And explore new CIImageProcessor APIs that optimize performance by giving you precise control over tile sizing and buffer management.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Extended Virtual Addressing Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing.json

## Code Snippets

### Contact for exports — [11:08]

```swift
let exportCtx = CIContext(options : [
.cacheIntermediate : false,
.memoryLimit : 512 ])
```

### CIImageProcessor with explicit output tile sizes — [12:23]

```swift
import CoreImage

class MyProcessor: CIImageProcessorKernel {
    override class func roi(forInput input: Int32,
                            arguments: [String : Any]?,
                            outputRect: CGRect) -> CGRect { return outputRect }

    override class func process(with inputs: [CIImageProcessorInput]?,
                                arguments: [String : Any]?,
                                output: CIImageProcessorOutput) throws {
        guard let input = inputs?.first,
              let iBuffer = input.pixelBuffer,
              let oBuffer = output.pixelBuffer else { return }

        let iRegion = input.region
        let oRegion = output.region // controlled by Core Image

        // MyCopyBuffer(iBuffer,iRegion, oBuffer,oRegion)
    }
}

let extent = inImg.extent
let tileSize = 512.0 // whatever tile size you want
var tiles: [CIVector] = []
for y in stride(from: extent.minY, to: extent.maxY, by: tileSize) {
    for x in stride(from: extent.minX, to: extent.maxX, by: tileSize) {
        let tile = CGRect(x: x, y: y,
                          width: min(tileSize, extent.maxX - x),
                          height: min(tileSize, extent.maxY - y))
        tiles.append(CIVector(cgRect: tile))
    }
}

let result = try MyProcessor.apply(withTiledExtent: tiles, inputs: [inImg], arguments: [:])
```

### CIImageProcessor using temporary PixelBuffer — [14:24]

```swift
import CoreImage

class MyProcessor: CIImageProcessorKernel {
    override class func process(with inputs: [CIImageProcessorInput]?,
                                arguments: [String: Any]?,
                                output: CIImageProcessorOutput) throws {
        guard let input = inputs?.first,
              let srcPixelBuffer = input.pixelBuffer,
              let dstPixelBuffer = output.pixelBuffer else { return }

        // Get a scratch buffer from Core Image's cache
        guard let scratch = output.temporaryPixelBuffer(identifier : "myScratch",
                   format: kCVPixelFormatType_64RGBAHalf,
                   width: Int(output.region.width),
                   height: Int(output.region.height),
                   pixelBufferAttributes: nil) else { return }

        // Step 1: copy input CVPixelBuffer → scratch
        // Step 2: process pixels in scratch
        // Step 3: copy scratch → output CVPixelBuffer
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/305/5/d8d5f3ce-0ff1-45a3-a630-436743477c62/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/305/5/d8d5f3ce-0ff1-45a3-a630-436743477c62/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._