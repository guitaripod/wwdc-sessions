---
id: "wwdc2026-325"
event: "wwdc2026"
year: 2026
title: "Dive into Core AI model authoring and optimization"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/325"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Dive into Core AI model authoring and optimization

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-325](https://developer.apple.com/videos/play/wwdc2026/325)

Dive into the complete custom model deployment workflow for Apple silicon with the new Core AI framework. Discover powerful techniques for authoring models using custom Metal kernels, alongside platform-aware compression strategies. The new Core AI Debugger offers deep intrinsic analysis, and AI-assisted workflows guide you from initial concept to optimized on-device execution.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,892 words)

## Documentation & Resources

- [Core AI PyTorch Extensions](https://apple.github.io/coreai-torch) _documentation_
- [Core AI Python](https://apple.github.io/coreai-torch/main/coreai-core) _documentation_
- [Core AI Optimization](https://apple.github.io/coreai-optimization) _documentation_
- [Inspecting, debugging, and profiling Core AI models](https://developer.apple.com/documentation/CoreAI/inspecting-debugging-and-profiling-core-ai-models) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI/inspecting-debugging-and-profiling-core-ai-models
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI/inspecting-debugging-and-profiling-core-ai-models.json
- [Inspecting Core AI models with Core AI Debugger](https://developer.apple.com/documentation/CoreAI/inspecting-core-ai-models-with-core-ai-debugger) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI/inspecting-core-ai-models-with-core-ai-debugger
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI/inspecting-core-ai-models-with-core-ai-debugger.json
- [Core AI](https://developer.apple.com/documentation/CoreAI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI.json

## Code Snippets

### Define and export a PyTorch model — [3:27]

```python
import torch
import torch.nn as nn

# Define a simple model
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(256, 512)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        return self.fc2(torch.relu(self.fc1(x)))

# Export with torch.export
model = MLP().eval()
example_input = (torch.randn(1, 256),)
exported_program = torch.export.export(model, example_input)
```

### Convert, optimize and run inference with Core AI — [4:02]

```python
import coreai
import coreai_torch
from coreai.runtime import NDArray

# Convert to Core AI
converter = coreai_torch.TorchConverter()
converter.add_exported_program(
    exported_program,
    input_names=["features"], output_names=["logits"])
core_ai_program = converter.to_coreai()

# Optimize and save to .aimodel
core_ai_program.optimize()
asset = core_ai_program.save_asset("mlp.aimodel")

# Run inference
specialized_model = await AIModel.load("mlp.aimodel")
specialized_function = specialized_model.load_function("main")
result = await specialized_function({"features": NDArray(example[0].numpy())})
```

### Define a SiLU Metal kernel with PyTorch reference — [21:12]

```python
import torch
from coreai_torch.dsl import TorchMetalKernel, MetalParameter

def silu_torch(x):
    return x * torch.sigmoid(x)

SILU_MSL = """
float val = float(x[gid]);
float sig = 1.0f / (1.0f + exp(-val));
y[gid] = TYPE(val * sig);
"""

silu_kernel = TorchMetalKernel(
    name="fused_silu",
    input_names=["x"],
    result_names=["y"],
    src=SILU_MSL,
    torch_defn=silu_torch,
    metal_params=[MetalParameter("gid", "uint", "thread_position_in_grid")],
    template_dtypes={"x": "TYPE"},
)
```

### Use a custom Metal kernel and convert with TorchConverter — [22:09]

```python
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 256)

    def forward(self, x):
        h = self.linear(x)
        n = h.numel()
        return silu_kernel(
            h,
            threads_per_grid_size=(n, 1, 1),
            threads_per_thread_group=(min(n, 256), 1, 1),
            result_shapes=[h.shape],
        )

exported_program = torch.export.export(MyModel(), (torch.randn(1, 256),))

converter = coreai_torch.TorchConverter()
converter.register_custom_kernels([silu_kernel])
converter.add_exported_program(exported_program,
                               input_names=["x"], output_names=["y"])
deployable = converter.to_coreai()  # MSL integrated into asset
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/325/5/8d08c9d4-3c64-49e1-8590-8b76bd9ad4cb/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/325/5/8d08c9d4-3c64-49e1-8590-8b76bd9ad4cb/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/325) — developer.apple.com. Indexed for agent consumption._