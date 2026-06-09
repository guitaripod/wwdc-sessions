# Optimize custom machine learning operations with Metal tensors

**Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-330](https://developer.apple.com/videos/play/wwdc2026/330)

Unlock powerful machine learning performance with the Metal Tensor API and Metal Performance Primitives (MPP) Tensor Ops library. Discover how to create portable operations that take advantage of Neural Accelerators in Apple M5 and A19 GPUs. Learn to build custom machine learning kernels for your Core AI applications, and find out how to work effectively with quantized data formats and GPU memory optimization.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Running inline ML operations in a shader with Metal 4](https://developer.apple.com/documentation/Metal/running-inline-ml-operations-in-a-shader-with-metal-4) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/running-inline-ml-operations-in-a-shader-with-metal-4
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/running-inline-ml-operations-in-a-shader-with-metal-4.json
- [Machine learning passes](https://developer.apple.com/documentation/Metal/machine-learning-passes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/machine-learning-passes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/machine-learning-passes.json
- [Download the Metal Performance Primitives (MPP) Programming Guide](https://developer.apple.com/download/files/Metal-Performance-Primitives-Programming-Guide.pdf) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/files/Metal-Performance-Primitives-Programming-Guide.pdf
- [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MetalPerformanceShaders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MetalPerformanceShaders.json

## Code Snippets

### Create a quantized MTLTensor — [3:53]

```objectivec
// Creating a tensor with a quantized data type from device

#define RANK 2

MTLTensorDescriptor *tensorDesc = [MTLTensorDescriptor new];

tensorDesc.dataType = MTLTensorDataTypeMetalFloat8E4M3;
tensorDesc.usage = MTLTensorUsageCompute;

NSInteger dimensions[RANK] = {NumCols, NumRows};
tensorDesc.dimensions = [[MTLTensorExtents alloc] initWithRank:RANK values:dimensions];

NSError *err = nil;
id <MTLTensor> tensor = [device newTensorWithDescriptor:tensorDesc error:&err];
```

### Declare a multi-plane tensor with scale factors — [4:48]

```objectivec
// Creating a tensor with a scales auxiliary plane from device

#define RANK 2

MTLTensorAuxiliaryPlaneDescriptor *planeDesc = [MTLTensorAuxiliaryPlaneDescriptor new];
planeDesc.dataType = MTLTensorDataTypeMetalFloat8UE8M0;

NSInteger blockFactors[RANK] = {32, 1};
planeDesc.blockFactors = [[MTLTensorExtents alloc] initWithRank:RANK values:blockFactors];

MTLTensorAuxiliaryPlaneDescriptorMap *auxiliaryPlanes =
    [MTLTensorAuxiliaryPlaneDescriptorMap new];
[auxiliaryPlanes setDescriptor:planeDesc forPlane:MTLTensorPlaneTypeScales];

MTLTensorDescriptor *tensorDesc = [MTLTensorDescriptor new];
tensorDesc.dataType = MTLTensorDataTypeMetalFloat8E4M3;
tensorDesc.usage = MTLTensorUsageCompute;

NSInteger dimensions[RANK] = {NumCols, NumRows};
tensorDesc.dimensions = [[MTLTensorExtents alloc] initWithRank:RANK values:dimensions];
tensorDesc.auxiliaryPlanes = auxiliaryPlanes;

NSError *err = nil;
id <MTLTensor> tensor = [device newTensorWithDescriptor:tensorDesc error:&err];
```

### MSL type aliases for an MXFP8 tensor handle — [6:07]

```objectivec
// Type aliases for a MXFP8 multi-plane tensor handle

#include <metal_tensor>

using namespace metal;

using scales_plane = tensor_blockwise<tensor_plane_scales,
                                      device metal_fp8_ue8m0_format,
                                      32, 1>;

using mxfp8_tensor = tensor<device metal_fp8_e4m3_format,
                            dextents<int, 2>,
                            tensor_handle,
                            scales_plane>;

kernel void matmul(mxfp8_tensor matrixA [[buffer(0)]],
                   mxfp8_tensor matrixB [[buffer(1)]],
                   tensor<device half, dextents<int, 2>> matrixC [[buffer(2)]])
{
    // ...
}
```

### Declare an inline MXFP8 tensor on the stack — [6:51]

```objectivec
// Type aliases for a MXFP8 multi-plane tensor inline

#include <metal_tensor>

using namespace metal;

using scales_plane = tensor_blockwise<tensor_plane_scales,
                                      device metal_fp8_ue8m0_format,
                                      32, 1>;

using mxfp8_tensor_inline = tensor<device metal_fp8_e4m3_format,
                                   dextents<int, 2>,
                                   tensor_inline,
                                   scales_plane>;

// Construct tensor on the stack from buffer pointers
mxfp8_tensor_inline matrixA(dataBufferA,
                             dextents<int, 2>(K, M),
                             array<int, 2>({ 1, K }),
                             scales_plane(scalesBufferA));
```

### Slice tensors and run a quantized matmul — [7:19]

```objectivec
// Slice the tensors to extract the relevant tile
auto tA = matrixA.slice(0, tgid.y * TILEM);
auto tB = matrixB.slice(tgid.x * TILEN, 0);
auto tC = matrixC.slice(tgid.x * TILEN, tgid.y * TILEM);

// Set up the matmul descriptor
constexpr auto descriptor = matmul2d_descriptor(TILEM,                  // M
                                                TILEN,                  // N
                                                dynamic_length_v<int>,  // K
                                                false,   // Left matrix transposed
                                                false);  // Right matrix transposed

matmul2d<descriptor, execution_simdgroups<4>> op;

// Run the op — TensorOps handles dequantization automatically
op.run(tA, tB, tC);
```

### Set up simdgroup-scoped QxK multiplication — [10:27]

```objectivec
// Setup QxK matrix multiplication op
constexpr auto mul_qk_op_desc = matmul2d_descriptor(/* ... */);
matmul2d<mul_qk_op_desc, execution_simdgroups> mul_qk_op;

// Slice Q, K, V
auto tQSlice = tQ.slice<D, ROWS_PER_SIMD>(0, sgid * ROWS_PER_SIMD);
auto tKSlice = tK.slice<D, BK>(0, k);
auto tVSlice = tV.slice<D, BK>(0, k);

// Create cooperative tensor to store tile of QxK
auto ctQK = mul_qk_op.get_destination_cooperative_tensor<decltype(tQSlice),
                                                         decltype(tKSlice),
                                                         float>();

// Multiply QxK
mul_qk_op.run(tQSlice, tKSlice, ctQK);
```

### Compute row-wise reduction for SoftMax — [11:18]

```objectivec
// Create a cooperative tensor to store row reduction output
auto ctTileRowMax = mul_qk_op.get_row_reduction_destination_cooperative_tensor<
                        decltype(tQSlice),
                        decltype(tKSlice),
                        float>();

// Compute max over each row of QxK tile
reduce_rows(ctQK, ctTileRowMax, reduction_operation::max, -INFINITY);
```

### Compute element-wise SoftMax with map_iterator — [11:56]

```objectivec
// Iterate over elements of QxK tile
#pragma clang loop unroll(full)
for (auto it = ctQK.begin(); it != ctQK.end(); it++) {
    // Fetch row max corresponding to this element
    auto row_it = ctRowMax.map_iterator(it);

    // Subtract row max from each element and compute exponent
    *it = exp(*it - *row_it);
}
```

### Reuse cooperative tensor as matmul input — [12:33]

```objectivec
constexpr auto mul_sv_op_desc = matmul2d_descriptor(/* ... */);
matmul2d<mul_sv_op_desc, metal::execution_simdgroup> mul_sv_op;

if (mul_sv_op.is_compatible_as_left_input<float, half, float>(ctQK)) {
    // Directly reuse cooperative tensor as input
    auto ctQKIn = mul_sv_op.get_left_input_cooperative_tensor<float, half, float>(ctQK);
    mul_sv_op.run(ctQKIn, tVSlice, ctO);
} else {
    // Store and reload through threadgroup memory if layout is not compatible
    ctQK.store(tgTensor);
    simdgroup_barrier(mem_flags::mem_threadgroup);

    auto ctQKIn = mul_sv_op.get_left_input_cooperative_tensor<float, half, float>();
    ctQKIn.load(tgTensor);
    mul_sv_op.run(ctQKIn, tVSlice, ctO);
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/330/4/0ff2c290-e47b-4d88-8a8f-0634e11506a4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/330/4/0ff2c290-e47b-4d88-8a8f-0634e11506a4/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._