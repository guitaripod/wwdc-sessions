---
id: "wwdc2025-315"
event: "wwdc2025"
year: 2025
title: "Get started with MLX for Apple silicon"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/315"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Get started with MLX for Apple silicon

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-315](https://developer.apple.com/videos/play/wwdc2025/315)

MLX is a flexible and efficient array framework for numerical computing and machine learning on Apple silicon. We’ll explore fundamental features including unified memory, lazy computation, and function transformations. We’ll also look at more advanced techniques for building and accelerating machine learning models across Apple’s platforms using Swift and Python APIs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,925 words)

## Documentation & Resources

- [MLX Swift Examples](https://github.com/ml-explore/mlx-swift-examples) _samplecode_
- [MLX Examples](https://github.com/ml-explore/mlx-examples) _samplecode_
- [MLX Swift](https://github.com/ml-explore/mlx-swift) _documentation_
- [MLX  LM - Python API](https://github.com/ml-explore/mlx-lm) _documentation_
- [MLX Explore - Python API](https://github.com/ml-explore/mlx) _documentation_
- [MLX Framework](https://mlx-framework.org) _documentation_
- [MLX Llama Inference](https://ml-explore.github.io/mlx/build/html/examples/llama-inference.html) _documentation_
- [MLX](https://ml-explore.github.io/mlx/) _documentation_

## Code Snippets

### Basics — [3:48]

```python
import mlx.core as mx

# Make an array
a = mx.array([1, 2, 3])

# Make another array
b = mx.array([4, 5, 6])

# Do an operation
c = a + b

# Access information about the array
shape = c.shape
dtype = c.dtype

print(f"Result c: {c}")
print(f"Shape: {shape}")
print(f"Data type: {dtype}")
```

### Unified memory — [5:31]

```python
import mlx.core as mx

a = mx.array([1, 2, 3])
b = mx.array([4, 5, 6])

c = mx.add(a, b, stream=mx.gpu)
d = mx.multiply(a, b, stream=mx.cpu)

print(f"c computed on the GPU: {c}")
print(f"d computed on the CPU: {d}")
```

### Lazy computation — [6:20]

```python
import mlx.core as mx

# Make an array
a = mx.array([1, 2, 3])

# Make another array
b = mx.array([4, 5, 6])

# Do an operation
c = a + b

# Evaluates c before printing it
print(c)

# Also evaluates c
c_list = c.tolist()

# Also evaluates c
mx.eval(c)

print(f"Evaluate c by converting to list: {c_list}")
print(f"Evaluate c using print: {c}")
print(f"Evaluate c using mx.eval(): {c}")
```

### Function transformation — [7:32]

```python
import mlx.core as mx

def sin(x):
    return mx.sin(x)

dfdx = mx.grad(sin)

def sin(x):
    return mx.sin(x)

d2fdx2 = mx.grad(mx.grad(mx.sin))

# Computes the second derivative of sine at 1.0
d2fdx2(mx.array(1.0))
```

### Neural Networks in MLX — [9:16]

```python
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

class MLP(nn.Module):
    """A simple MLP."""

    def __init__(self, dim, h_dim):
        super().__init__()
        self.linear1 = nn.Linear(dim, h_dim)
        self.linear2 = nn.Linear(h_dim, dim)

    def __call__(self, x):
        x = self.linear1(x)
        x = nn.relu(x)
        x = self.linear2(x)
        return x
```

### MLX and PyTorch — [9:57]

```python
# MLX version
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

class MLP(nn.Module):
    """A simple MLP."""

    def __init__(self, dim, h_dim):
        super().__init__()
        self.linear1 = nn.Linear(dim, h_dim)
        self.linear2 = nn.Linear(h_dim, dim)

    def __call__(self, x):
        x = self.linear1(x)
        x = nn.relu(x)
        x = self.linear2(x)
        return x

# PyTorch version
import torch
import torch.nn as nn
import torch.optim as optim

class MLP(nn.Module):
    """A simple MLP."""

    def __init__(self, dim, h_dim):
        super().__init__()
        self.linear1 = nn.Linear(dim, h_dim)
        self.linear2 = nn.Linear(h_dim, dim)

    def forward(self, x):
        x = self.linear1(x)
        x = x.relu()
        x = self.linear2(x)
        return x
```

### Compiling MLX functions — [11:35]

```python
import mlx.core as mx
import math

def gelu(x):
    return x * (1 + mx.erf(x / math.sqrt(2))) / 2

@mx.compile
def compiled_gelu(x):
    return x * (1 + mx.erf(x / math.sqrt(2))) / 2

x = mx.random.normal(shape=(4,))

out = gelu(x)
compiled_out = compiled_gelu(x)
print(f"gelu:          {out}")
print(f"compiled gelu: {compiled_out}")
```

### MLX Fast package — [12:32]

```python
import mlx.core as mx
import time

def rms_norm(x, weight, eps=1e-5):
    y = x.astype(mx.float32)
    y = y * mx.rsqrt(mx.mean(
        mx.square(y), 
        axis=-1, 
        keepdims=True,
    ) + eps)
    return (weight * y).astype(x.dtype)

batch_size = 8192
feature_dim = 4096
iterations = 1000

x = mx.random.normal([batch_size, feature_dim])
weight = mx.ones(feature_dim)
bias = mx.zeros(feature_dim)

start_time = time.perf_counter()
for _ in range(iterations):
    y = rms_norm(x, weight, eps=1e-5)
    mx.eval(y)
rms_norm_time = time.perf_counter() - start_time
print(f"rms_norm execution: {gelu_time:0.4f} sec")

start_time = time.perf_counter()
for _ in range(iterations):
    mx.eval(mx.fast.rms_norm(x, weight, eps=1e-5))
fast_rms_norm_time = time.perf_counter() - start_time
print(f"mx.fast.rms_norm execution: {compiled_gelu_time:0.4f} sec")

print(f"mx.fast.rms_norm speedup: {rms_norm_time/fast_rms_norm_time:0.2f}x")
```

### Custom Metal kernel — [13:30]

```python
import mlx.core as mx

# Build the kernel
source = """
    uint elem = thread_position_in_grid.x;
    out[elem] = metal::exp(inp[elem]);
"""
kernel = mx.fast.metal_kernel(
    name="myexp",
    input_names=["inp"],
    output_names=["out"],
    source=source,
)

# Call the kernel on a sample input
x = mx.array([1.0, 2.0, 3.0])
out = kernel(
    inputs=[x],
    grid=(x.size, 1, 1),
    threadgroup=(256, 1, 1),
    output_shapes=[x.shape],
    output_dtypes=[x.dtype],
)[0]
print(out)
```

### Quantization — [14:41]

```python
import mlx.core as mx

x = mx.random.normal([1024])
weight = mx.random.normal([1024, 1024])

quantized_weight, scales, biases = mx.quantize(
        weight, bits=4, group_size=32,
)

y = mx.quantized_matmul(
    x,
    quantized_weight,
    scales=scales,
    biases=biases,
    bits=4,
    group_size=32,
)

w_orig = mx.dequantize(
    quantized_weight,
    scales=scales,
    biases=biases,
    bits=4,
    group_size=32,
)
```

### Quantized models — [15:23]

```python
import mlx.nn as nn

model = nn.Sequential(
    nn.Embedding(100, 32),
    nn.Linear(32, 32),
    nn.Linear(32, 32),
    nn.Linear(32, 1),
)

print(model)

nn.quantize(
    model,
    bits=4,
    group_size=32,
)

print(model)
```

### Distributed — [16:50]

```python
import mlx.core as mx

group = mx.distributed.init()

world_size = group.size()
rank = group.rank()

x = mx.array([1.0])

x_sum = mx.distributed.all_sum(x)

print(x_sum)
```

### Distributed launcher — [17:20]

```bash
mlx.launch --hosts ip1, ip2, ip3, ip4 my_script.py
```

### MLX Swift — [18:20]

```swift
// Swift
import MLX

// Make an array
let a = MLXArray([1, 2, 3])

// Make another array
let b = MLXArray([1, 2, 3])

// Do an operation
let c = a + b

// Access information about the array
let shape = c.shape
let dtype = c.dtype

// Print results
print("a: \(a)")
print("b: \(b)")
print("c = a + b: \(c)")
print("shape: \(shape)")
print("dtype: \(dtype)")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/315/4/7321e1ec-e5c2-45a5-a0ea-5e84afc61e0b/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/315/4/7321e1ec-e5c2-45a5-a0ea-5e84afc61e0b/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/315) — developer.apple.com. Indexed for agent consumption._