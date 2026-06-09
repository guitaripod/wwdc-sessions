---
id: "wwdc2026-233"
event: "wwdc2026"
year: 2026
title: "Explore distributed inference and training with MLX"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/233"
topics: ["AI & Machine Learning"]
platforms: ["macOS"]
hasTranscript: true
---

# Explore distributed inference and training with MLX

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-233](https://developer.apple.com/videos/play/wwdc2026/233)

Scale your machine learning workloads across multiple Macs using MLX. Learn how to tackle interconnect efficiency, large model inference, request batching, and distributed training challenges. Discover how a few Macs on your desk can replace expensive cloud infrastructure for demanding AI workloads.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,975 words)

## Documentation & Resources

- [MLX Swift LM on GitHub](https://github.com/ml-explore/mlx-swift-lm) _documentation_
- [MLX Swift Examples](https://github.com/ml-explore/mlx-swift-examples) _samplecode_
- [MLX Examples](https://github.com/ml-explore/mlx-examples) _samplecode_
- [MLX Swift](https://github.com/ml-explore/mlx-swift) _documentation_
- [MLX  LM - Python API](https://github.com/ml-explore/mlx-lm) _documentation_
- [MLX Explore - Python API](https://github.com/ml-explore/mlx) _documentation_
- [MLX Framework](https://mlx-framework.org) _documentation_
- [MLX](https://ml-explore.github.io/mlx/) _documentation_

## Code Snippets

### Hostfile format for a 4-node MLX cluster — [8:31]

```json
[
  {
    "ssh": "m3-ultra-0",
    "ips": ["192.168.1.10"],
    "rdma": [null, "rdma_en5", "rdma_en4", "rdma_en3"]
  },
  {
    "ssh": "m3-ultra-1",
    "ips": ["192.168.1.11"],
    "rdma": ["rdma_en5", null, "rdma_en4", "rdma_en3"]
  },
  {
    "ssh": "m3-ultra-2",
    "ips": ["192.168.1.12"],
    "rdma": ["rdma_en5", "rdma_en4", null, "rdma_en3"]
  },
  {
    "ssh": "m3-ultra-3",
    "ips": ["192.168.1.13"],
    "rdma": ["rdma_en5", "rdma_en4", "rdma_en3", null]
  }
]
```

### Generate the cluster hostfile with mlx.distributed_config — [8:56]

```bash
mlx.distributed_config \
--hosts m3-ultra-0,m3-ultra-1,m3-ultra-2,m3-ultra-3 \
--output "m3-ultra-jaccl.json" \
--env MLX_METAL_FAST_SYNCH=1 \
--auto-setup \
--backend jaccl
```

### Run distributed LLM inference with mlx_lm.chat — [11:04]

```bash
# Single-device LLM inference
mlx_lm.chat --model "Qwen/Qwen3.6-27B" --max-tokens 2048

# Distributed LLM inference across the cluster
mlx.launch --hostfile "m3-ultra-jaccl.json" -- \
    /remote/path/to/mlx_lm.chat --model "Qwen/Qwen3.6-27B" --max-tokens 2048
```

### Run distributed inference with pipeline parallelism — [15:03]

```bash
# Tensor parallelism (default)
mlx.launch --hostfile "m3-ultra-jaccl.json" -- \
    /remote/path/to/mlx_lm.chat --model "moonshotai/Kimi-K2.6" \
                                 --max-tokens 2048

# Pipeline parallelism — append --pipeline flag
mlx.launch --hostfile "m3-ultra-jaccl.json" -- \
    /remote/path/to/mlx_lm.chat --model "moonshotai/Kimi-K2.6" \
                                 --max-tokens 2048 \
                                 --pipeline
```

### Run distributed fine-tuning with mlx_lm.lora — [17:18]

```bash
# Single-device fine-tuning
mlx_lm.lora --model "Qwen/Qwen3.5-9B" \
             --data "mlx-community/wikisql" \
             --train --batch-size 4

# Distributed fine-tuning (scale --batch-size by number of devices)
mlx.launch --hostfile "hostfile.json" -- \
    /remote/path/to/mlx_lm.lora --model "Qwen/Qwen3.5-9B" \
                                  --data "mlx-community/wikisql" \
                                  --train --batch-size 16
```

### Distributed inference with the MLX LM Python API — [19:01]

```python
import mlx.core as mx
from mlx_lm import stream_generate
from mlx_lm.utils import sharded_load

# Initialise distributed backend
group = mx.distributed.init(strict=True, backend="jaccl")
# Define parallelism
tensor_group, pipeline_group = group, None

# Shard the model
model, tokenizer = sharded_load("moonshotai/Kimi-K2.6", pipeline_group, tensor_group)
for response in stream_generate(model, tokenizer, prompt, max_tokens=1024):
    if group.rank() == 0:
        print(response.text, end="", flush=True)
```

### Shard a layer with the MLX Python API — [19:31]

```python
import mlx.core as mx
import mlx.nn as nn

# Initialise distributed backend
group = mx.distributed.init(strict=True, backend="jaccl")

# Define layer and shard it column-wise
layer = nn.Linear(1024, 1024)
sharded_layer = nn.layers.distributed.shard_linear(
    layer, strategy="all-to-sharded", group=group
)
data = mx.random.normal((1, 1, 1024))
output = sharded_layer(data)
mx.eval(output)
```

### All-reduce across devices in Python, Swift, and C++ — [19:47]

```python
# Python
import mlx.core as mx
world = mx.distributed.init(strict=True, backend="jaccl")
data = mx.full((4,), float(world.rank()), dtype=mx.float32)
result = mx.distributed.all_sum(data, group=world)
mx.eval(result)

# Swift
let group = try DistributedGroup(strict: .ring)
let data = rank == 0
    ? MLXArray(converting: [1.0, 2.0, 3.0])
    : MLXArray(converting: [5.0, 6.0, 7.0])
let result = try group.allSum(data)

// C++
namespace mx = mlx::core;
auto world = mx::distributed::init(/* strict */ true, "jaccl");
mx::array data = mx::full({4}, static_cast<float>(world.rank()), mx::float32);
mx::array result = mx::distributed::all_sum(data, world);
mx::eval(result);
```

### Standalone distributed sum with the JACCL C++ API — [20:06]

```cpp
#include <jaccl/jaccl.h>
#include <iostream>

int main() {
    // Initialize JACCL group
    auto group = jaccl::init();
    std::cout << "Rank " << group->rank() << " of " << group->size() << std::endl;
    // Perform all-reduce sum
    float data[10] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f, 10.0f};
    float output[10];
    group->all_sum(data, output, sizeof(data), jaccl::Float32);
    std::cout << "Result: " << output[0] << std::endl;
    return 0;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/233/4/379c319a-5718-4fd2-aac6-2f97180c5892/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/233/4/379c319a-5718-4fd2-aac6-2f97180c5892/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/233) — developer.apple.com. Indexed for agent consumption._