---
id: "wwdc2025-298"
event: "wwdc2025"
year: 2025
title: "Explore large language models on Apple silicon with MLX"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/298"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore large language models on Apple silicon with MLX

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-298](https://developer.apple.com/videos/play/wwdc2025/298)

Discover MLX LM – designed specifically to make working with large language models simple and efficient on Apple silicon. We’ll cover how to fine-tune and run inference on state-of-the-art large language models on your Mac, and how to seamlessly integrate them into Swift-based applications and projects.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,077 words)

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

### Running DeepSeek AI's model with MLX LM — [1:12]

```bash
mlx_lm.chat --model mlx-community/DeepSeek-V3-0324-4bit
```

### Text generation with MLX LM — [3:51]

```bash
mlx_lm.generate --model "mlx-community/Mistral-7B-Instruct-v0.3-4bit" \
--prompt "Write a quick sort in Swift"
```

### Changing the model's behavior with flags — [4:35]

```bash
mlx_lm.generate --model "mlx-community/Mistral-7B-Instruct-v0.3-4bit" \
--prompt "Write a quick sort in Swift" \
--top-p 0.5 \
--temp 0.2 \
--max-tokens 1024
```

### Getting help for MLX LM — [4:48]

```bash
mlx_lm.generate --help
```

### MLX LM Python API — [5:26]

```python
# Using MLX LM from Python

from mlx_lm import load, generate

# Load the model and tokenizer directly from HF
model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

# Prepare the prompt for the model
prompt = "Write a quick sort in Swift"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True
)

# Generate the text
text = generate(model, tokenizer, prompt=prompt, verbose=True)
```

### Inspecting model architecture — [6:24]

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

print(model)
print(model.parameters())
print(model.layers[0].self_attn)
```

### Generation with KV cache — [8:01]

```python
from mlx_lm import load, generate
from mlx_lm.models.cache import make_prompt_cache

# Load the model and tokenizer directly from HF
model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

# Prepare the prompt for the model
prompt = "Write a quick sort in Swift"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True
)

cache = make_prompt_cache(model)

# Generate the text
text = generate(model, tokenizer, prompt=prompt, prompt_cache=cache, verbose=True)
```

### Quantization — [9:37]

```bash
mlx_lm.convert --hf-path "mistralai/Mistral-7B-Instruct-v0.3" \
--mlx-path "./mistral-7b-v0.3-4bit" \
--dtype float16 \
--quantize --q-bits 4 --q-group-size 64
```

### Model quantization with MLX LM in Python — [10:33]

```python
from mlx_lm.convert import convert

# We can choose a different quantization per layer
def mixed_quantization(layer_path, layer, model_config):
    if "lm_head" in layer_path or "embed_tokens" in layer_path:
        return {"bits": 6, "group_size": 64}
    elif hasattr(layer, "to_quantized"):
        return {"bits": 4, "group_size": 64}
    else:
        return False

# Convert can be used to change precision, quantize and upload models to HF
convert(
    hf_path="mistralai/Mistral-7B-Instruct-v0.3",
    mlx_path="./mistral-7b-v0.3-mixed-4-6-bit",
    quantize=True,
    quant_predicate=mixed_quantization
)
```

### Model fine-tuning — [13:37]

```bash
mlx_lm.lora --model "mlx-community/Mistral-7B-Instruct-v0.3-4bit" 
						--train 
            --data /path/to/our/data/folder
            --iters 300 
            --batch-size 16
```

### Prompting before fine-tuning — [15:06]

```bash
mlx_lm.generate --model "./mistral-7b-v0.3-4bit" \
--prompt "Who won the latest super bowl?"
```

### Fine-tuning to learn new knowledge — [15:34]

```bash
mlx_lm.lora --model "./mistral-7b-v0.3-4bit" 
						--train 
            --data ./data 
            --iters 300 
            --batch-size 8 
            --mask-prompt 
            --learning-rate 1e-5
```

### Prompting after fine-tuning — [15:48]

```bash
mlx_lm.generate --model "mlx-community/Mistral-7B-Instruct-v0.3-4bit" \
--prompt "Who won the latest super bowl?" \
--adapter "adapters"
```

### Fusing models — [16:29]

```bash
mlx_lm.fuse --model "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
            --adapter-path "path/to/trained/adapters" \
            --save-path "fused-mistral-7b-v0.3-4bit" \
            --upload-repo "my-name/fused-mistral-7b-v0.3-4bit"

# Fusing our fine-tuned model adapters
mlx_lm.fuse --model "./mistral-7b-v0.3-4bit" \
            --adapter-path "adapters" \
            --save-path "fused-mistral-7b-v0.3-4bit"
```

### LLMs in MLX Swift — [17:14]

```swift
import Foundation
import MLX
import MLXLMCommon
import MLXLLM

@main
struct LLM {
    static func main() async throws {
        // Load the model and tokenizer directly from HF
        let modelId = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
        let modelFactory = LLMModelFactory.shared
        let configuration = ModelConfiguration(id: modelId)
        let model = try await modelFactory.loadContainer(configuration: configuration)

        try await model.perform({context in
            // Prepare the prompt for the model
            let prompt = "Write a quicksort in Swift"
            let input = try await context.processor.prepare(input: UserInput(prompt: prompt))

            // Generate the text
            let params = GenerateParameters(temperature: 0.0)
            let tokenStream = try generate(input: input, parameters: params, context: context)
            for await part in tokenStream {
                print(part.chunk ?? "", terminator: "")
            }
        })
    }
}
```

### Generation with KV cache in MLX Swift — [18:00]

```swift
import Foundation
import MLX
import MLXLMCommon
import MLXLLM

@main
struct LLM {
    static func main() async throws {
        // Load the model and tokenizer directly from HF
        let modelId = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
        let modelFactory = LLMModelFactory.shared
        let configuration = ModelConfiguration(id: modelId)
        let model = try await modelFactory.loadContainer(configuration: configuration)

        try await model.perform({context in
            // Prepare the prompt for the model
            let prompt = "Write a quicksort in Swift"
            let input = try await context.processor.prepare(input: UserInput(prompt: prompt))

            // Create the key-value cache
            let generateParameters = GenerateParameters()
            let cache = context.model.newCache(parameters: generateParameters)

            // Low level token iterator
            let tokenIter = try TokenIterator(input: input,
                                              model: context.model,
                                              cache: cache,
                                              parameters: generateParameters)
            let tokenStream = generate(input: input, context: context, iterator: tokenIter)
            for await part in tokenStream {
                print(part.chunk ?? "", terminator: "")
            }
        })
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/298/4/fc7619f7-0729-4d62-9a01-ba6020832cb8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/298/4/fc7619f7-0729-4d62-9a01-ba6020832cb8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/298) — developer.apple.com. Indexed for agent consumption._