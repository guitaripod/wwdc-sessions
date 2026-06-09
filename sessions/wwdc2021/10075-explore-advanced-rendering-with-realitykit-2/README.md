---
id: "wwdc2021-10075"
event: "wwdc2021"
year: 2021
title: "Explore advanced rendering with RealityKit 2"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10075"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore advanced rendering with RealityKit 2

**Event:** WWDC21 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10075](https://developer.apple.com/videos/play/wwdc2021/10075)

Create stunning visuals for your augmented reality experiences with cutting-edge rendering advancements in RealityKit. Learn the art of writing custom shaders, draw real-time dynamic meshes, and explore creative post-processing effects to help you stylize your AR scene.

**Keywords:** `3d graphics`, `ar`, `arkit`, `augmented reality`, `core image`, `depth map`, `lidar`, `metal shading language`, `realitykit`, `scenekit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,619 words)

## Documentation & Resources

- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/RealityKit/building-an-immersive-experience-with-realitykit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit/building-an-immersive-experience-with-realitykit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit/building-an-immersive-experience-with-realitykit.json
- [Explore the RealityKit Developer Forums](https://developer.apple.com/forums/tags/realitykit) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/tags/realitykit
- [Displaying a point cloud using scene depth](https://developer.apple.com/documentation/ARKit/displaying-a-point-cloud-using-scene-depth) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/displaying-a-point-cloud-using-scene-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/displaying-a-point-cloud-using-scene-depth.json
- [Creating a fog effect using scene depth](https://developer.apple.com/documentation/ARKit/creating-a-fog-effect-using-scene-depth) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/creating-a-fog-effect-using-scene-depth
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/creating-a-fog-effect-using-scene-depth.json
- [RealityKit](https://developer.apple.com/documentation/RealityKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RealityKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RealityKit.json

## Code Snippets

### Seaweed Shader — [4:52]

```objectivec
#include <RealityKit/RealityKit.h>

[[visible]]
void seaweedGeometry(realitykit::geometry_parameters params)
{
    float spatialScale = 8.0;
    float amplitude = 0.05;

    float3 worldPos = params.geometry().world_position();
    float3 modelPos = params.geometry().model_position();

    float phaseOffset = 3.0 * dot(worldPos, float3(1.0, 0.5, 0.7));
    float time = 0.1 * params.uniforms().time() + phaseOffset;

    float3 maxOffset = float3(sin(spatialScale * 1.1 * (worldPos.x + time)),
                              sin(spatialScale * 1.2 * (worldPos.y + time)),
                              sin(spatialScale * 1.2 * (worldPos.z + time)));

    float3 offset = maxOffset * amplitude * max(0.0, modelPos.y);

    params.geometry().set_model_position_offset(offset);
}
```

### Assign Seaweed Shader — [5:43]

```swift
// Assign seaweed shader to model.

func assignSeaweedShader(to seaweed: ModelEntity)
{
    let library = MTLCreateSystemDefaultDevice()!.makeDefaultLibrary()!

    let geometryModifier = CustomMaterial.GeometryModifier(named: "seaweedGeometry",
                                                           in: library)

    seaweed.model!.materials = seaweed.model!.materials.map { baseMaterial in
        try! CustomMaterial(from: baseMaterial, geometryModifier: geometryModifier)
    }
}
```

### Octopus Shader — [9:21]

```objectivec
#include <RealityKit/RealityKit.h>

void transitionBlend(float time,
                     half3 masks,
                     thread half &blend,
                     thread half &colorBlend)
{
    half noise = masks.r;
    half gradient = masks.g;
    half mask = masks.b;

    half transition = (sin(time * 1.0) + 1) / 2;
    transition = saturate(transition);

    blend = 2 * transition - (noise + gradient) / 2;
    blend = 0.5 + 4.0 * (blend - 0.5); // more contrast
    blend = saturate(blend);
    blend = max(blend, mask);
    blend = 1 - blend;

    colorBlend = min(blend, mix(blend, 1 - transition, 0.8h));
}

[[visible]]
void octopusSurface(realitykit::surface_parameters params)
{
    constexpr sampler bilinear(filter::linear);

    auto tex = params.textures();
    auto surface = params.surface();
    auto material = params.material_constants();

    // USD textures have an inverse y orientation.
    float2 uv = params.geometry().uv0();
    uv.y = 1.0 - uv.y;

    half3 mask = tex.custom().sample(bilinear, uv).rgb;

    half blend, colorBlend;
    transitionBlend(params.uniforms().time(), mask, 
                    blend, colorBlend);

    // Sample both color textures.
    half3 baseColor1, baseColor2;
    baseColor1 = tex.base_color().sample(bilinear, uv).rgb;
    baseColor2 = tex.emissive_color().sample(bilinear, uv).rgb;

    // Blend colors and multiply by the tint.
    half3 blendedColor = mix(baseColor1, baseColor2, colorBlend);
    blendedColor *= half3(material.base_color_tint());

    // Set on the surface.
    surface.set_base_color(blendedColor);

    // Sample the normal and unpack.
    half3 texNormal = tex.normal().sample(bilinear, uv).rgb;
    half3 normal = realitykit::unpack_normal(texNormal);

    // Set on the surface.
    surface.set_normal(float3(normal));

    // Sample material textures.
    half roughness = tex.roughness().sample(bilinear, uv).r;
    half metallic = tex.metallic().sample(bilinear, uv).r;
    half ao = tex.ambient_occlusion().sample(bilinear, uv).r;
    half specular = tex.roughness().sample(bilinear, uv).r;

    // Apply material scaling factors.
    roughness *= material.roughness_scale();
    metallic *= material.metallic_scale();
    specular *= material.specular_scale();

    // Increase roughness for the red octopus.
    roughness *= (1 + blend);

    // Set material properties on the surface.
    surface.set_roughness(roughness);
    surface.set_metallic(metallic);
    surface.set_ambient_occlusion(ao);
    surface.set_specular(specular);
}
```

### Assign Octopus Shader — [11:41]

```swift
// Apply the surface shader to the Octopus.
func assignOctopusShader(to octopus: ModelEntity)
{
    // Load additional textures.
    let color2 = try! TextureResource.load(named: "Octopus/Octopus_bc2")
    let mask = try! TextureResource.load(named: "Octopus/Octopus_mask")

    // Load the surface shader.
    let surfaceShader = CustomMaterial.SurfaceShader(named: "octopusSurface",
                                                     in: library)

    // Construct a new material with the contents of an existing material.
    octopus.model!.materials = octopus.model!.materials.map { baseMaterial in
        let material = try! CustomMaterial(from: baseMaterial
                                           surfaceShader: surfaceShader)
        // Assign additional textures.
        material.emissiveColor.texture = .init(color2)
        material.custom.texture = .init(mask)
        return material
    }
}
```

### CoreImage PostEffect — [14:13]

```swift
// Add RenderCallbacks to the ARView.

var ciContext: CIContext?

func initPostEffect(arView: ARView)
{
    arView.renderCallbacks.prepareWithDevice = { [weak self] device in
        self?.prepareWithDevice(device)
    }
    arView.renderCallbacks.postProcess = { [weak self] context in
        self?.postProcess(context)
    }
}

func prepareWithDevice(_ device: MTLDevice) {
    self.ciContext = CIContext(mtlDevice: device)
}

// The CoreImage thermal filter.
func postProcess(_ context: ARView.PostProcessContext) {
    // Create a CIImage for the input color.
    let sourceColor = CIImage(mtlTexture: context.sourceColorTexture)!

    // Create the thermal filter.
    let thermal = CIFilter.thermal()
    thermal.inputImage = sourceColor

    // Create the CIRenderDestination.
    let destination = CIRenderDestination(mtlTexture: context.targetColorTexture,
                                          commandBuffer: context.commandBuffer)

    // Preserve the image orientation.
    destination.isFlipped = false

    // Instruct CoreImage to start our render task.
    _ = try? self.ciContext?.startTask(toRender: thermal.outputImage!, to: destination)
}
```

### Bloom Post Effect — [16:15]

```swift
var device: MTLDevice!
    var bloomTexture: MTLTexture!

    func initPostEffect(arView: ARView) {
        arView.renderCallbacks.prepareWithDevice = { [weak self] device in
            self?.prepareWithDevice(device)
        }
        arView.renderCallbacks.postProcess = { [weak self] context in
            self?.postProcess(context)
        }
    }

    func prepareWithDevice(_ device: MTLDevice) {
        self.device = device
    }

    func makeTexture(matching texture: MTLTexture) -> MTLTexture {
        let descriptor = MTLTextureDescriptor()
        descriptor.width = texture.width
        descriptor.height = texture.height
        descriptor.pixelFormat = texture.pixelFormat
        descriptor.usage = [.shaderRead, .shaderWrite]

        return device.makeTexture(descriptor: descriptor)!
    }

    func postProcess(_ context: ARView.PostProcessContext) {
        if self.bloomTexture == nil {
            self.bloomTexture = self.makeTexture(matching: context.sourceColorTexture)
        }

        // Reduce areas of 20% brightness or less to zero.
        let brightness = MPSImageThresholdToZero(device: context.device,
                                                 thresholdValue: 0.2,
                                                 linearGrayColorTransform: nil)
        brightness.encode(commandBuffer: context.commandBuffer,
                          sourceTexture: context.sourceColorTexture,
                          destinationTexture: bloomTexture!)

        // Blur the remaining areas.
        let gaussianBlur = MPSImageGaussianBlur(device: context.device, sigma: 9.0)
        gaussianBlur.encode(commandBuffer: context.commandBuffer,
                            inPlaceTexture: &bloomTexture!)

        // Add color plus bloom, writing the result to targetColorTexture.
        let add = MPSImageAdd(device: context.device)
        add.encode(commandBuffer: context.commandBuffer,
                   primaryTexture: context.sourceColorTexture,
                   secondaryTexture: bloomTexture!,
                   destinationTexture: context.targetColorTexture)
    }
```

### SpriteKit Post Effect — [17:15]

```swift
// Initialize the SpriteKit renderer.

    var skRenderer: SKRenderer!

    func initPostEffect(arView: ARView) {
        arView.renderCallbacks.prepareWithDevice = { [weak self] device in
            self?.prepareWithDevice(device)
        }
        arView.renderCallbacks.postProcess = { [weak self] context in
            self?.postProcess(context)
        }
    }

    func prepareWithDevice(_ device: MTLDevice)
        self.skRenderer = SKRenderer(device: device)
        self.skRenderer.scene = SKScene(fileNamed: "GameScene")
        self.skRenderer.scene!.scaleMode = .aspectFill

        // Make the background transparent.
        self.skRenderer.scene!.backgroundColor = .clear
    }

    func postProcess(context: ARView.PostProcessContext) {
        // Blit (Copy) sourceColorTexture onto targetColorTexture.
        let blitEncoder = context.commandBuffer.makeBlitCommandEncoder()
        blitEncoder?.copy(from: context.sourceColorTexture, to: context.targetColorTexture)
        blitEncoder?.endEncoding()

        // Advance the scene to the new time.
        self.skRenderer.update(atTime: context.time)

        // Create a RenderPass writing to the targetColorTexture.
        let desc = MTLRenderPassDescriptor()
        desc.colorAttachments[0].loadAction = .load
        desc.colorAttachments[0].storeAction = .store
        desc.colorAttachments[0].texture = context.targetColorTexture

        // Render!
        self.skRenderer.render(withViewport: CGRect(x: 0, y: 0, 
                                 width: context.targetColorTexture.width, 
                                 height: context.targetColorTexture.height),
                                 commandBuffer: context.commandBuffer,
                                 renderPassDescriptor: desc)
    }
```

### ARKit AR Depth — [19:08]

```swift
let width = context.sourceColorTexture.width
let height = context.sourceColorTexture.height

let transform =   
  arView.session.currentFrame!.displayTransform(
    for: self.orientation,
    viewportSize: CGSize(width: width, height: height)
  ).inverted()
```

### Depth Fog Shader — [20:01]

```objectivec
typedef struct
{
    simd_float4x4 viewMatrixInverse;
    simd_float4x4 viewMatrix;

    simd_float2x2 arTransform;
    simd_float2 arOffset;

    float fogMaxDistance;
    float fogMaxIntensity;
    float fogExponent;
} DepthFogParams;

float linearizeDepth(float sampleDepth, float4x4 viewMatrix)
{
    constexpr float kDepthEpsilon = 1e-5f;

    float d = max(kDepthEpsilon, sampleDepth);

    // linearize (we have reverse infinite projection);
    d = abs(-viewMatrix[3].z / d);

    return d;
}

constexpr sampler textureSampler(address::clamp_to_edge, filter::linear);

float getDepth(uint2 gid,
               constant DepthFogParams &args,
               texture2d<float, access::sample> inDepth,
               depth2d<float, access::sample> arDepth)
{
    // normalized coordinates
    float2 coords = float2(gid) / float2(inDepth.get_width(), inDepth.get_height());

    float2 arDepthCoords = args.arTransform * coords + args.arOffset;

    float realDepth = arDepth.sample(textureSampler, arDepthCoords);
    float virtualDepth = linearizeDepth(inDepth.sample(textureSampler, coords)[0], args.viewMatrix);

    return min(virtualDepth, realDepth);
}

[[kernel]]
void depthFog(uint2 gid [[thread_position_in_grid]],
              constant DepthFogParams& args [[buffer(0)]],
              texture2d<half, access::sample> inColor [[texture(0)]],
              texture2d<float, access::sample> inDepth [[texture(1)]],
              texture2d<half, access::write> outColor [[texture(2)]],
              depth2d<float, access::sample> arDepth [[texture(3)]]
)
{
    const half4 fogColor = half4(0.5, 0.5, 0.5, 1.0);

    float depth = getDepth(gid, args, inDepth, arDepth);

    // Ignore depth values greater than the maximum fog distance.
    float fogAmount = saturate(depth / args.fogMaxDistance);
    float fogBlend = pow(fogAmount, args.fogExponent) * args.fogMaxIntensity;

    half4 nearColor = inColor.read(gid);
    half4 color = mix(nearColor, fogColor, fogBlend);

    outColor.write(color, gid);
}
```

### MeshResource.Contents extension — [23:32]

```swift
// Examine each vertex in a mesh.

extension MeshResource.Contents {
    func forEachVertex(_ callback: (SIMD3<Float>) -> Void) {
        for instance in self.instances {
            guard let model = self.models[instance.model] else { continue }
            let instanceToModel = instance.transform
            for part in model.parts {
                for position in part.positions {
                    let vertex = instanceToModel * SIMD4<Float>(position, 1.0)
                    callback([vertex.x, vertex.y, vertex.z])
                }
            }
        }
    }
}
```

### Mesh Radii — [24:20]

```swift
struct Slices {
    var radii : [Float] = []
    var range : ClosedRange<Float> = 0...0

    var sliceHeight: Float {
        return (range.upperBound - range.lowerBound) / Float(sliceCount)
    }

    var sliceCount: Int {
        return radii.count
    }

    func heightAt(index: Int) -> Float {
        return range.lowerBound + Float(index) * self.sliceHeight + self.sliceHeight * 0.5
    }

    func radiusAt(y: Float) -> Float {
        let relativeY = y - heightAt(index: 0)
        if relativeY < 0 {
            return radii.first!
        }

        let slice = relativeY / sliceHeight
        let sliceIndex = Int(slice)

        if sliceIndex+1 >= sliceCount {
            return radii.last!
        }

        // 0 to 1
        let t = (slice - floor(slice))

        // linearly interpolate between two closest values
        let prev = radii[sliceIndex]
        let next = radii[sliceIndex+1]

        return mix(prev, next, t)
    }

    func radiusAtIndex(i: Float) -> Float {
        let asFloat = i * Float(radii.count)
        var prevIndex = Int(asFloat.rounded(.down))
        var nextIndex = Int(asFloat.rounded(.up))

        if prevIndex < 0 {
            prevIndex = 0
        }

        if nextIndex >= radii.count {
            nextIndex = radii.count - 1
        }

        let prev = radii[prevIndex]
        let next = radii[nextIndex]

        let remainder = asFloat - Float(prevIndex)
        let lerped = mix(prev, next, remainder)

        return lerped + 0.5
    }
}

func meshRadii(for mesh: MeshResource, numSlices: Int) -> Slices {
    var radiusForSlice: [Float] = .init(repeating: 0, count: numSlices)

    let (minY, maxY) = (mesh.bounds.min.y, mesh.bounds.max.y)
    mesh.contents.forEachVertex { modelPos in
        let normalizedY = (modelPos.y - minY) / (maxY - minY)
        let sliceY = min(Int(normalizedY * Float(numSlices)), numSlices - 1)

        let radius = length(SIMD2<Float>(modelPos.x, modelPos.z))
        radiusForSlice[sliceY] = max(radiusForSlice[sliceY], radius)
    }

    return Slices(radii: radiusForSlice, range: minY...maxY)
}
```

### Spiral Point — [25:58]

```swift
// The angle between two consecutive segments.
let theta = (2 * .pi) / Float(segmentsPerRevolution)

// How far to step in the y direction per segment.
let yStep = height / Float(totalSegments)

func p(_ i: Int, radius: Float = 1.0) 
     -> SIMD3<Float>
{
    let y = yStep * Float(i)

    let x = radius * cos(Float(i) * theta)
    let z = radius * sin(Float(i) * theta)

    return SIMD3<Float>(x, y, z)
}
```

### Generate Spiral — [26:37]

```swift
extension MeshResource {
    static func generateSpiral(
        radiusAt: (Float)->Float,
        radiusAtIndex: (Float)->Float,
        thickness: Float,
        height: Float,
        revolutions: Int,
        segmentsPerRevolution: Int) -> MeshResource
    {
        let totalSegments = revolutions * segmentsPerRevolution
        let totalVertices = (totalSegments + 1) * 2

        var positions: [SIMD3<Float>] = []
        var normals: [SIMD3<Float>] = []
        var indices: [UInt32] = []
        var uvs: [SIMD2<Float>] = []

        positions.reserveCapacity(totalVertices)
        normals.reserveCapacity(totalVertices)
        uvs.reserveCapacity(totalVertices)
        indices.reserveCapacity(totalSegments * 4)

        for i in 0..<totalSegments {
            let theta = Float(i) / Float(segmentsPerRevolution) * 2 * .pi
            let t = Float(i) / Float(totalSegments)
            let segmentY = t * height

            if i > 0 {
                let base = UInt32(positions.count - 2)
                let prevInner = base
                let prevOuter = base + 1
                let newInner = base + 2
                let newOuter = base + 3

                indices.append(contentsOf: [
                    prevInner, newOuter, prevOuter, // first triangle
                    prevInner, newInner, newOuter // second triangle
                ])
            }

            let radialDirection = SIMD3<Float>(cos(theta), 0, sin(theta))
            let radius = radiusAtIndex(t)

            var position = radialDirection * radius
            position.y = segmentY

            positions.append(position)
            positions.append(position + [0, thickness, 0])

            normals.append(-radialDirection)
            normals.append(-radialDirection)

            // U = in/out
            // V = distance along spiral
            uvs.append(.init(0.0, t))
            uvs.append(.init(1.0, t))
        }

        var mesh = MeshDescriptor()
        mesh.positions = .init(positions)
        mesh.normals = .init(normals)
        mesh.primitives = .triangles(indices)
        mesh.textureCoordinates = .init(uvs)

        return try! MeshResource.generate(from: [mesh])
    }
}
```

### Update Spiral — [28:17]

```swift
if var contents = spiralEntity?.model?.mesh.contents {
    contents.models = .init(contents.models.map { model in
        var newModel = model
        newModel.parts = .init(model.parts.map { part in
            let start = min(self.allIndices.count, max(0, numIndices - stripeSize))
            let end = max(0, min(self.allIndices.count, numIndices))

            var newPart = part
            newPart.triangleIndices = .init(self.allIndices[start..<end])
            return newPart
        })
        return newModel
    })
    try? spiralEntity?.model?.mesh.replace(with: contents)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10075/6/81A03814-3C6E-4B82-A5BB-92160CD0EF78/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10075/6/81A03814-3C6E-4B82-A5BB-92160CD0EF78/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10075) — developer.apple.com. Indexed for agent consumption._
