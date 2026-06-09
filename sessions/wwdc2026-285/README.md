# Discover USDKit and what’s new in OpenUSD

**Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-285](https://developer.apple.com/videos/play/wwdc2026/285)

Dive into the latest advances in Universal Scene Description (USD) support on Apple platforms, including Swift-based USDKit, the new spatial preview API, and enhanced spatial web capabilities. Discover how the latest updates to the OpenUSD standard add support for accessibility, Gaussian splats, and compressed geometry. We’ll also walk through the expanded USD editing and rendering tools in Preview for Mac, showing you how to leverage these capabilities in your own apps.

**Keywords:** `3d`, `3d content`, `3d model`, `augmented reality`, `spatial computing`, `usd`, `usda`, `usdc`, `usdz`, `visionos`

## Transcript

[Read the full transcript](transcript.md)

## Code Snippets

### Opening a USD Stage — [8:12]

```swift
import USDKit

// Create a new empty in-memory stage

let stage = USDStage()

// Open a stage from a file on disk

let url = URL(fileURLWithPath: "/ALab/entry.usda")
let stage = try USDStage.open(url)
```

### Traversing the Stage Hierarchy — [8:44]

```swift
// Traverse all prims looking for the oscilloscope
for prim in stage.descendants {
    if prim.name == "scope" {
        // There it is! 🔬
    }
}

// It wasn't there — define a new Xform prim for it

let scope = stage.definePrim(at: "/World/scope", type: “Xform"))

// Add a file reference to the prim

try scope.references.add(“/ALab/assets/scope.usda”)
```

### Moving a Prim with a Transform Operation — [9:36]

```swift
// Creates xformOp:translate and updates xformOpOrder automatically

scope.addTransformOperation(type: .translate)
scope["xformOp:translate", as: USDValue.Vec3d.self] = [2.5, 0.0, -1.0]
```

### Applying Accessibility Metadata — [10:42]

```swift
// Apply the multi-apply AccessibilityAPI schema with instance name "default"

try scope.applyAPISchema("AccessibilityAPI", instanceName:"default")

// Create the label and description attributes

scope.makeAttribute(named: "accessibility:default:label", as: .string)
scope.makeAttribute(named: "accessibility:default:description", as: .string)

// Set their values

scope["accessibility:default:label", as: String.self] = "Oscilloscope"
scope["accessibility:default:description", as: String.self] = 
    "Vintage signal analyzer with a 3D wireframe display, topped by a color bar test monitor"
```

### Exporting with Mesh and Texture Compression — [12:05]

```swift
let output = URL(fileURLWithPath: "/ALab/alab_compressed.usdz")

// Export the stage as a USDZ package

try stage.exportPackage(
    to: output,
    options: [
        .preferSmallTextureFiles(quality: .standard),   // compress textures
        .preferSmallMeshFiles                           // compress mesh geometry
    ]
)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/285/4/335150b6-c2b8-4711-a632-45a34d449eac/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/285/4/335150b6-c2b8-4711-a632-45a34d449eac/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._