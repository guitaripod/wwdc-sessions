---
id: "tech-talks-10858"
event: "tech-talks"
year: 2017
title: "Discover Metal enhancements for A14 Bionic"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/10858"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Discover Metal enhancements for A14 Bionic

**Event:** Tech Talks · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS · **Published:** 2020-10-21 · **Session:** [tech-talks-10858](https://developer.apple.com/videos/play/tech-talks/10858)

Explore how Metal is bringing sophisticated rendering and powerful compute features to A14 Bionic. We’ll take you through the Metal capabilities delivered in the Apple GPU Family 7 feature set, including new texture addressing modes, fast SIMD reduction and matrix multiplication operations, and a deep dive into implementing a visibility buffer using barycentric coordinates and primitive ID.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,225 words)

## Documentation & Resources

- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Visibility buffer - Geometry stage — [9:50]

```swift
// Vertex Shader - Geometry stage

vertex float4 geoVertex(float3* pos   [[buffer(0)]], 
                        float4x4* vpm [[buffer(1)]],
                        Uint vid      [[vertex_id]]) {
   float3 p = pos[vid];          // Position fetch
   return doTransform(p, vpm);   // Transform step
}


// Fragment Shader - Geometry stage

fragment VisBufferFragment geoFrag(uint primid  [[primitive_id]],
                                   float3 baryc [[barycentric_coords]],
                                   uint drawid  [[buffer(0)]]) { 
   VisBufferFragment out;    out.surface_id  = makeID(primid, drawid);   // Combine draw ID and primitive ID
   out.barycentric = baryc.xy; 
   return out;
}
```

### Visibility buffer - Lighting stage — [10:21]

```swift
// Lighting Compute Kernel

kernel lightingCompute(Draws* draws          [[buffer(0)]],
                       texture2d<float4> lit [[texture(0)]]) {

  /* Reconstruction using Visibility Buffer */
  MaterialInput mi  = doReconstruct(surface_id, baryc, draws);

  /* Apply material model */
  MaterialOutput mo = doMaterial(mi, mat);

  /* Apply lighting function */
  lit[thread_id]    = doLighting(mo, lights);

}
```

### Visibility buffer - Reconstruction step — [12:27]

```swift
MaterialInput doReconstruct (uint32 surface_id, short2 baryc, Draws* draws, Mesh* meshes)
{
    MaterialInput mi;

    /* Retrieve primitive ID and Draw ID */
    uint primid   = surface_id & 0x0000FFFF; uint surface_id = ids >> 16;
    /* Retrieve the 3rd barycentric coordinate */
    float3 bc     = float3(baryc.xy, 1.0 - baryc.x - baryc.y);
    /* Retrieve (mesh ID, vertex ID) using primitive ID and draw ID */
    uint meshid   = draws[drawid].meshid;
    uint3 vertid  = uint3(draws[meshid].ib[primid*3+0], 
                          draws[meshid].ib[primid*3+1], 
                          draws[meshid].ib[primid*3+2]);
    /* Interpolate vertex buffer data cross barycentric coordinates */
    mi.uv  = meshes[meshid].vb[vertid.x].uv.xy * bc.x +
             meshes[meshid].vb[vertid.y].uv.xy * bc.y +
             meshes[meshid].vb[vertid.z].uv.xy * bc.z;
    /* Other draw state such as normals */
    mi.normal     = normalize(draws[drawid].vpm * float4(normal, 0)).xyz;

    return mi;
}
```

### Texture addressing modes — [15:25]

```swift
/* * rAddressMode : The address mode for the texture depth (r) coordinate.
   * sAddressMode : The address mode for the texture width (s) coordinate.
   * tAddressMode : The address mode for the texture height (t) coordinate.
   * borderColor : The border color for clamped texture values.
 */

let device = MTLCreateSystemDefaultDevice()!

let samplerDesc = MTLSamplerDescriptor()

/* … Program other sample state… */
samplerDesc.magFilter = .linear;

samplerDesc.sAddressMode = .mirrorClampToEdge
samplerDesc.tAddressMode = .mirrorClampToEdge

samplerDesc.rAddressMode = .clampToBorderColor
samplerDesc.borderColor  = .transparentBlack

let samplerState = device.makeSamplerState(descriptor: samplerDesc)!
```

### SIMD reduce_sum — [20:45]

```swift
void reduce_sum(device float const* input_array,
                device float* total_sum)
{
     threadgroup float SSA[32];

     float a = input_array[read_offset];

     float simdgroup_sum = simd_sum(a);

     SSA[sg_index] = simdgroup_sum;

     threadgroup_barrier(mem_flags::mem_threadgroup);

     if (simdgroup_index_in_threadgroup == 0)
     {
         *total_sum  = simd_sum(SSA[sg_index]);
     }
}
```

### SIMD 16x16 matrix multiplication — [24:56]

```swift
// SIMD 16x16 matrix multiplication

void matmul(threadgroup float const* A, threadgroup float const* B, threadgroup float* C)
{

    simdgroup_float8x8 matA, matB, matC(0.0f);


    A += A_increment(sg_index, A_row_stride);
    B += B_increment(sg_index, B_row_stride);
    C += C_increment(sg_index, C_row_stride);

    for (ushort k = 0; k < 16; k += 8) {
        simdgroup_load(matA, A + k, A_row_stride);
        simdgroup_load(matB, B + k * B_row_stride, B_row_stride);
        simdgroup_multiply_accumulate(matC, matA, matB, matC);
    }

    simdgroup_store(matC, C, C_row_stride);

}
```

### Metal Performance Shaders — [25:51]

```swift
// General matrix multiplication
let matMulKernel = MPSMatrixMultiplication(device: device!, resultRows: M, 
    resultColumns: N, interiorColumns: K)
matMulKernel.encode(commandBuffer: commandBuffer, leftMatrix: A, rightMatrix: B,
    resultMatrix: C)

// CNN convolution
let convKernel = MPSCNNConvolution(device: device!, weights: convDataSource)
convKernel.encodeBatch(commandBuffer: commandBuffer, 
    sourceImages: sources, destinationImages: results)

// MPS Graph
let graph = MPSGraph()
let A = graph.placeholder(shape:[M, K], dataType: .float32)
let B = graph.placeholder(shape:[K, N], dataType: .float32)
let C = graph.matrixMultiplication(primaryTensor: A, secondaryTensor: B)
graph.run(feeds: [A, B] targetTensors: C targetOperations: nil)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/10858/2/870884DF-CCA3-41E5-9AAC-9A3DCBF0615E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/tech-talks/10858/2/870884DF-CCA3-41E5-9AAC-9A3DCBF0615E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/10858) — developer.apple.com. Indexed for agent consumption._