---
id: "wwdc2024-10104"
event: "wwdc2024"
year: 2024
title: "Build a spatial drawing app with RealityKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10104"
topics: ["Developer Tools", "Graphics & Games", "Spatial Computing"]
platforms: ["macOS", "visionOS"]
hasTranscript: true
---

# Build a spatial drawing app with RealityKit

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** macOS, visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10104](https://developer.apple.com/videos/play/wwdc2024/10104)

Harness the power of RealityKit through the process of building a spatial drawing app. As you create an eye-catching spatial experience that integrates RealityKit with ARKit and SwiftUI, you’ll explore how resources work in RealityKit and how to use features like low-level mesh and texture APIs to achieve fast updates of the users’ brush strokes.

**Keywords:** `3d text`, `anchor entity`, `anti aliasing`, `audio`, `blend modes`, `cross platform`, `gpu`, `hand tracking`, `ios`, `low level mesh`, `low level texture`, `macos`, `mesh extrusion`, `metal`, `reality composer pro`, `realitykit`, `rendering`, `spatial tracking`, `visionos`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,420 words)

## Documentation & Resources

- [Drawing paths and shapes](https://developer.apple.com/tutorials/SwiftUI/drawing-paths-and-shapes) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/tutorials/SwiftUI/drawing-paths-and-shapes
- [Creating a spatial drawing app with RealityKit](https://developer.apple.com/documentation/RealityKit/creating-a-spatial-drawing-app-with-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/creating-a-spatial-drawing-app-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/creating-a-spatial-drawing-app-with-realitykit.json
- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Using SpatialTrackingSession — [4:18]

```swift
// Retain the SpatialTrackingSession while your app needs access

let session = SpatialTrackingSession()

// Declare needed tracking capabilities 
let configuration = SpatialTrackingSession.Configuration(tracking: [.hand])

// Request authorization for spatial tracking
let unapprovedCapabilities = await session.run(configuration)

if let unapprovedCapabilities, unapprovedCapabilities.anchor.contains(.hand) {
    // User has rejected hand data for your app.
    // AnchorEntities will continue to remain anchored and update visually
    // However, AnchorEntity.transform will not receive updates
} else {
    // User has approved hand data for your app.
    // AnchorEntity.transform will report hand anchor pose
}
```

### Use MeshResource extrusion — [7:07]

```swift
// Use MeshResource(extruding:) to generate the canvas edge

let path = SwiftUI.Path { path in
    // Generate two concentric circles as a SwiftUI.Path
    path.addArc(center: .zero, radius: outerRadius,
        startAngle: .degrees(0), endAngle: .degrees(360),
        clockwise: true)
    path.addArc(center: .zero, radius: innerRadius,
        startAngle: .degrees(0), endAngle: .degrees(360),
        clockwise: true)
}.normalized(eoFill: true)
var options = MeshResource.ShapeExtrusionOptions()
options.boundaryResolution 
    = .uniformSegmentsPerSpan(segmentCount: 64)
options.extrusionMethod = .linear(depth: extrusionDepth)

return try MeshResource(extruding: path, 
                        extrusionOptions: extrusionOptions)
```

### Highlight HoverEffectComponent — [9:33]

```swift
// Use HoverEffectComponent with .highlight

let placementEntity: Entity = // ...

let hover = HoverEffectComponent(
    .highlight(.init(
        color: UIColor(/* ... */),
        strength: 5.0)
    )
)

placementEntity.components.set(hover)
```

### Using Blend Modes — [9:54]

```swift
// Create an UnlitMaterial with Additive Blend Mode

var descriptor = UnlitMaterial.Program.Descriptor()
descriptor.blendMode = .add

let prog = await UnlitMaterial.Program(descriptor: descriptor)
var material = UnlitMaterial(program: prog)

material.color 
    = UnlitMaterial.BaseColor(tint: UIColor(/* ... */))
```

### Shader based hover effects — [13:45]

```swift
// Use shader-based hover effects

let hoverEffectComponent = HoverEffectComponent(.shader(.default))
entity.components.set(hoverEffectComponent)

let material = try await ShaderGraphMaterial(named: "/Root/SolidPresetBrushMaterial",
                                             from: "PresetBrushMaterial",
                                             in: realityKitContentBundle)

entity.components.set(ModelComponent(mesh: /* ... */, materials: [material]))
```

### Defining a vertex buffer struct for the solid brush — [16:56]

```swift
struct SolidBrushVertex {
    packed_float3 position;
    packed_float3 normal;
    packed_float3 bitangent;
    packed_float2 materialProperties;
    float curveDistance;
    packed_half3 color;
};
```

### Defining LowLevelMesh Attributes for solid brush — [19:27]

```swift
extension SolidBrushVertex {
    static var vertexAttributes: [LowLevelMesh.Attribute] {
        typealias Attribute = LowLevelMesh.Attribute
        return [
            Attribute(semantic: .position, format: MTLVertexFormat.float3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.position)!),
            Attribute(semantic: .normal, format: MTLVertexFormat.float3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.normal)!),
            Attribute(semantic: .bitangent, format: MTLVertexFormat.float3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.bitangent)!),
            Attribute(semantic: .color, format: MTLVertexFormat.half3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.color)!),
            Attribute(semantic: .uv1, format: MTLVertexFormat.float, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.curveDistance)!),
            Attribute(semantic: .uv3, format: MTLVertexFormat.float2, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.materialProperties)!)
        ]
    }
}
```

### Make LowLevelMesh — [21:14]

```swift
private static func makeLowLevelMesh(vertexBufferSize: Int, indexBufferSize: Int, 
                                     meshBounds: BoundingBox) throws -> LowLevelMesh
{
    var descriptor = LowLevelMesh.Descriptor() // Similar to MTLVertexDescriptor

    descriptor.vertexCapacity = vertexBufferSize
    descriptor.indexCapacity = indexBufferSize
    descriptor.vertexAttributes = SolidBrushVertex.vertexAttributes

    let stride = MemoryLayout<SolidBrushVertex>.stride
    descriptor.vertexLayouts = [LowLevelMesh.Layout(bufferIndex: 0, 
                                                    bufferOffset: 0, bufferStride: stride)]

    let mesh = try LowLevelMesh(descriptor: descriptor)

    mesh.parts.append(LowLevelMesh.Part(indexOffset: 0, indexCount: indexBufferSize,
                                        topology: .triangleStrip, materialIndex: 0,
                                        bounds: meshBounds))
    return mesh
}
```

### Creating a MeshResource — [22:28]

```swift
let mesh: LowLevelMesh

let resource = try MeshResource(from: mesh)

entity.components[ModelComponent.self] = ModelComponent(mesh: resource, materials: [...])
```

### Updating vertex data of LowLevelMesh using withUnsafeMutableBytes API — [22:37]

```swift
let mesh: LowLevelMesh

mesh.withUnsafeMutableBytes(bufferIndex: 0) { buffer in
    let vertices: UnsafeMutableBufferPointer<SolidBrushVertex>
        = buffer.bindMemory(to: SolidBrushVertex.self)

    // Write to vertex buffer `vertices`
}
```

### Updating LowLevelMesh index buffers using withUnsafeMutableBytes API — [23:07]

```swift
let mesh: LowLevelMesh

mesh.withUnsafeMutableIndices { buffer in
    let indices: UnsafeMutableBufferPointer<UInt32>
        = buffer.bindMemory(to: UInt32.self)

    // Write to index buffer `indices`
}
```

### Creating a particle brush using LowLevelMesh — [23:58]

```swift
struct SparkleBrushAttributes {
    packed_float3 position;
    packed_half3 color;
    float curveDistance;
    float size;
};

// Describes a particle in the simulation
struct SparkleBrushParticle {
    struct SparkleBrushAttributes attributes;
    packed_float3 velocity;
};

// One quad (4 vertices) is created per particle
struct SparkleBrushVertex {
    struct SparkleBrushAttributes attributes;
    simd_half2 uv;
};
```

### Defining LowLevelMesh Attributes for sparkle brush — [24:58]

```swift
extension SparkleBrushVertex {
    static var vertexAttributes: [LowLevelMesh.Attribute] {
        typealias Attribute = LowLevelMesh.Attribute
        return [
            Attribute(semantic: .position, format: .float3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.attributes.position)!),

            Attribute(semantic: .color, format: .half3, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.attributes.color)!),

            Attribute(semantic: .uv0, format: .half2, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.uv)!),

            Attribute(semantic: .uv1, format: .float, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.attributes.curveDistance)!),

            Attribute(semantic: .uv2, format: .float, layoutIndex: 0,
                      offset: MemoryLayout.offset(of: \Self.attributes.size)!)
        ]
    }
}
```

### Populate LowLevelMesh on GPU — [25:28]

```swift
let inputParticleBuffer: MTLBuffer
let lowLevelMesh: LowLevelMesh

let commandBuffer: MTLCommandBuffer
let encoder: MTLComputeCommandEncoder
let populatePipeline: MTLComputePipelineState

commandBuffer.enqueue()
encoder.setComputePipelineState(populatePipeline)

let vertexBuffer: MTLBuffer = lowLevelMesh.replace(bufferIndex: 0, using: commandBuffer)

encoder.setBuffer(inputParticleBuffer, offset: 0, index: 0)
encoder.setBuffer(vertexBuffer, offset: 0, index: 1)
encoder.dispatchThreadgroups(/* ... */)

// ...
encoder.endEncoding()
commandBuffer.commit()
```

### Use MeshResource extrusion to generate 3D text — [27:01]

```swift
// Use MeshResource(extruding:) to generate 3D text

var textString = AttributedString("RealityKit")
textString.font = .systemFont(ofSize: 8.0)

let secondLineFont = UIFont(name: "ArialRoundedMTBold", 
                            size: 14.0)
let attributes = AttributeContainer([.font: secondLineFont])

textString.append(AttributedString("\nDrawing App", 
                                   attributes: attributes))

let paragraphStyle = NSMutableParagraphStyle()
paragraphStyle.alignment = .center
let centerAttributes 
    = AttributeContainer([.paragraphStyle: paragraphStyle])
textString.mergeAttributes(centerAttributes)

var extrusionOptions = MeshResource.ShapeExtrusionOptions()
extrusionOptions.extrusionMethod = .linear(depth: 2)
extrusionOptions.materialAssignment
        = .init(front: 0, back: 0, extrusion: 1,
                frontChamfer: 1, backChamfer: 1)
extrusionOptions.chamferRadius = 0.1

let textMesh = try await MeshResource(extruding: textString
                          extrusionOptions: extrusionOptions)
```

### Use MeshResource extrusion to turn a SwiftUI Path into 3D mesh — [28:25]

```swift
// Use MeshResource(extruding:) to bring SwiftUI.Path to 3D

let graphic = SwiftUI.Path { path in
    path.move(to: CGPoint(x: -0.7, y: 0.135413))
    path.addCurve(to: CGPoint(x: -0.7, y: 0.042066),
                  control1: CGPoint(x: -0.85, y: 0.067707),
                  control2: CGPoint(x: -0.85, y: 0.021033))
    // ...
}

var options = MeshResource.ShapeExtrusionOptions()
// ...

let graphicMesh = try await MeshResource(extruding: graphic
                          extrusionOptions: options)
```

### Defining a LowLevelTexture — [29:44]

```swift
let descriptor = LowLevelTexture.Descriptor(pixelFormat: .rg16Float,
                                            width: textureResolution, 
                                            height: textureResolution,
                                            textureUsage: [.shaderWrite, .shaderRead])

let lowLevelTexture = try LowLevelTexture(descriptor: descriptor)
var textureResource = try TextureResource(from: lowLevelTexture)

var material = UnlitMaterial()
material.color = .init(tint: .white, texture: .init(textureResource))
```

### Update a LowLevelTexture on the GPU — [30:27]

```swift
let lowLevelTexture: LowLevelTexture

let commandBuffer: MTLCommandBuffer
let encoder: MTLComputeCommandEncoder
let computePipeline: MTLComputePipelineState

commandBuffer.enqueue()
encoder.setComputePipelineState(computePipeline)

let writeTexture: MTLTexture = lowLevelTexture.replace(using: commandBuffer)
encoder.setTexture(writeTexture, index: 0)

// ...

encoder.dispatchThreadgroups(/* ... */)
encoder.endEncoding()
commandBuffer.commit()
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10104/3/818182EE-A12C-4B8F-A02B-93B2C730BFF0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10104/3/818182EE-A12C-4B8F-A02B-93B2C730BFF0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10104) — developer.apple.com. Indexed for agent consumption._
