---
id: "wwdc2026-324"
event: "wwdc2026"
year: 2026
title: "Meet Core AI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/324"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Meet Core AI

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-324](https://developer.apple.com/videos/play/wwdc2026/324)

Discover Core AI, Apple’s new framework for on-device AI model deployment. Tour the ecosystem, from Python libraries for converting, authoring, and optimizing models, to a Swift API for simple plug-and-play inference and advanced use cases with strict latency and memory requirements. Explore the new Core AI models repository with ready-to-run examples for popular architectures. See how deep Xcode integration, including ahead-of-time model compilation, streamlines the workflow so you can deliver smarter, more responsive app experiences.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,348 words)

## Documentation & Resources

- [Core AI PyTorch Extensions](https://apple.github.io/coreai-torch) _documentation_
- [Core AI Python](https://apple.github.io/coreai-torch/main/coreai-core) _documentation_
- [Core AI Optimization](https://apple.github.io/coreai-optimization) _documentation_
- [Core AI](https://developer.apple.com/documentation/CoreAI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI.json
- [Compiling Core AI models ahead of time](https://developer.apple.com/documentation/CoreAI/compiling-core-ai-models-ahead-of-time) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI/compiling-core-ai-models-ahead-of-time
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI/compiling-core-ai-models-ahead-of-time.json
- [Managing model specialization and caching](https://developer.apple.com/documentation/CoreAI/managing-model-specialization-and-caching) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreAI/managing-model-specialization-and-caching
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreAI/managing-model-specialization-and-caching.json

## Code Snippets

### Convert a PyTorch model to Core AI — [5:08]

```python
import torch
import coreai_torch
# Load trained snake model and sample input for tracing
pt_model = SnakeTransformer().load_checkpoint("snake.pt")
example  = torch.randn(1, 5, 16)

# Export the torch program including dynamic shape for input sequence
seq_len  = torch.export.Dim("seq_len", min=1, max=256)
exported = torch.export.export(
    pt_model, args=(example,), 
    dynamic_shapes={"features": {1: seq_len}},
)
exported = exported.run_decompositions(coreai_torch.get_decomp_table())

# Convert torch graph → Core AI graph
ai_program = coreai_torch.TorchConverter().add_exported_program(
    exported, input_names=["features"], output_names=["logits"],
).to_coreai()

# Save as a .aimodel asset the runtime can load
ai_program.save_asset("SnakeTransformer.aimodel")
```

### Verify converted model numerics — [5:44]

```python
import torch
import numpy as np
from coreai. runtime import AIModel, NDArray
# Load models
pt_model = SnakeTransformer().load_checkpoint("snake.pt")
ai_model = await AIModel.load("SnakeTransformer.aimodel")
function = ai_model.load_function("main")
# Assemble input sample - 10 frames of 16-dim game features, shape (1, 10, 16)
features = np.array(lextract_features(game) for - in range (10)],
dtype=np.float32)[np.newaxis]
# PyTorch reference
with torch.no_grad():
	pytorch_logits = pt_model(torch.from_numpy(features)) . numpy )[0, -1]
# Core AI inference
result = await function({ "features": NDArray(data=features)} )
coreai_logits = result["logits"]. numpy()[0, -1]
# Validate
max_diff = np.max(np.abs(pytorch_logits - coreai_logits))
	assert max_diff < 0.01
```

### Core AI framework core types — [7:41]

```swift
// Core types within Core AI
import CoreAI

// Load the '.aimodel' file
let model = try await AIModel(contentsOf: modelURL)

// Load the main inference function
let mainFunction: InferenceFunction = try model.loadFunction(named: "main")!

// Construct the n-dimensional input data
let inputNDArray: NDArray = nextInput()

// Run inference
var outputs = try await mainFunction.run(inputs: ["input": inputNDArray])

guard let outputNDArray = outputs.remove("output")?.ndArray else {
  // Handle unexpected missing output
}
```

### Initialize ModelPlayer with AIModel — [8:33]

```swift
// Initialize the player by loading the AIModel and InferenceFunction
struct ModelPlayer {
  let nextActionFunction: InferenceFunction

  init(modelURL: URL) async throws {
    let model = try await AIModel(contentsOf: modelURL)
    self.nextActionFunction = try model.loadFunction(named: "main")!
  }
}
```

### Run inference with NDArray inputs — [8:49]

```swift
extension ModelPlayer: SnakePlayer {

  mutating func chooseAction(game: SnakeGame) async throws -> Direction {

    // Create an NDArray for the next input and write board features into it
    var inputFeatures = NDArray(shape: [game.stepCount, hiddenDim], scalarType: .float32)
    writeFeatures(of: game, into: inputFeatures.mutableView())

    // Run inference and extract the expected logits output NDArray
    var outputs = try await nextActionFunction.run(inputs: ["features": inputFeatures])
    guard let logits = outputs.remove("logits")?.ndArray else {
      throw ModelError.missingOutput
    }

    return predictedDirection(from: logits.view())
  }

  func writeFeatures(of game: SnakeGame, into view: consuming NDArray.MutableView<Float>) { … }
  func predictedDirection(from logits: NDArray.View<Float>) -> Direction { … }
}
```

### Input features for the snake model — [10:10]

```swift
// Features at each time step
var features = [Float]()

// Distance to wall in all directions, normalized between [0, 1]
features += [dWallUp, dWallDown, dWallLeft, dWallRight]

// Distance to nearest food, normalized between [-1, 1]
features += [dFoodX, dFoodY]

// Direction encoded as one-hot: [1,0,0,0]=up, [0,1,0,0]=down, etc.
features += dir.oneHotEncoding

// Distance to the other snake, normalized to [-1, 1]
features += [dUserX, dUserY]

// Direction of the opponent snake
features += dirU.oneHotEncoding
```

### Add KV cache buffers to PyTorch module — [12:18]

```python
# Update torch module to include key and value caches
# Use register_buffer to later make the exported torch program treat them as mutable

class SnakeTransformerStateful(nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.register_buffer(
            "k_cache", torch.zeros(N_LAYERS, 1, MAX_SEQ_LEN, D_MODEL))
        self.register_buffer(
            "v_cache", torch.zeros(N_LAYERS, 1, MAX_SEQ_LEN, D_MODEL))
        # …
```

### Update forward pass to read/write KV caches — [12:50]

```python
# During forward pass, read/write KV caches

class SnakeTransformerStateful(nn.Module):

    def forward(self, features, position_ids):
        new_k, new_v = [], []
        for i, block in enumerate(self.blocks):
            # read previous keys/values from caches
            k_prev = self.k_cache[i]
            v_prev = self.v_cache[i]
            # ... compute q/k/v for the new token, attend over valid prefix ...
            new_k.append(k_updated)
            new_v.append(v_updated)

        # Update key/value caches
        self.k_cache.copy_(torch.stack(new_k))
        self.v_cache.copy_(torch.stack(new_v))

        return self.action_head(self.ln_final(x))
```

### Re-convert model with state names — [12:59]

```python
# Updated coreai-torch conversion code using key/value cache states
import torch
import coreai_torch

exported = torch.export.export(
    stateful_model,
    args=(example_features, example_position_ids),
    dynamic_shapes={"position_ids": {1: seq_len}},
)
exported = exported.run_decompositions(coreai_torch.get_decomp_table())

ai_program = coreai_torch.TorchConverter().add_exported_program(
    exported,
    input_names=["features", "position_ids"],
    state_names=["keyCache", "valueCache"],
    output_names=["logits"],
).to_coreai()

ai_program.save_asset("SnakeTransformer.aimodel")
```

### Store KV cache NDArrays in ModelPlayer — [13:17]

```swift
// Add stored properties for the key and value caches
struct ModelPlayer {
    let nextActionFunction: InferenceFunction

    var keyCache: NDArray
    var valueCache: NDArray

    init(modelURL: URL) async throws {
        let model = try await AIModel(contentsOf: modelURL)
        self.nextActionFunction = try model.loadFunction(named: "main")!

        self.keyCache = NDArray(shape: [layers, maxContext, hiddenDim], scalarType: .float32)
        self.valueCache = NDArray(shape: [layers, maxContext, hiddenDim], scalarType: .float32)
    }
}
```

### Pass state views to inference function — [13:45]

```swift
extension ModelPlayer: SnakePlayer {
    mutating func chooseAction(game: SnakeGame, snakeID: Int) async throws -> Direction {
        // …

        var stateViews = InferenceFunction.MutableViews()
        stateViews.insert(&keyCache, for: "keyCache")
        stateViews.insert(&valueCache, for: "valueCache")

        // Run inference and extract the expected logits output NDArray
        var outputs = try await nextActionFunction.run(
            inputs: ["features": inputFeatures],
            states: stateViews)
        // …
    }
}
```

### Check model cache before loading — [16:22]

```swift
// Check if your model can be loaded from the cache
let cache = AIModelCache.default

guard let model = try cache.model(for: modelURL, options: .default) else {
    Task { @MainActor in
        informUser("Preparing AI features. This may take a while…")
    }
}
```

### Request model specialization — [16:42]

```swift
// Explicitly request specialization
try await AIModel.specialize(contentsOf: modelURL)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/324/4/3b67b624-4060-495f-9ba7-659805ee6b88/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/324/4/3b67b624-4060-495f-9ba7-659805ee6b88/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/324) — developer.apple.com. Indexed for agent consumption._
