---
id: "wwdc2026-232"
event: "wwdc2026"
year: 2026
title: "Run local agentic AI on the Mac using MLX"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/232"
topics: ["AI & Machine Learning"]
platforms: ["macOS"]
hasTranscript: true
---

# Run local agentic AI on the Mac using MLX

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-232](https://developer.apple.com/videos/play/wwdc2026/232)

Run AI agents locally with privacy, low latency, and offline access. Dive into how MLX advancements and Mac hardware make powerful agentic workflows possible entirely on-device. You’ll explore code agents such as OpenCode, see how they integrate into Xcode, learn techniques for multi-Mac scaling, and discover how to integrate tools seamlessly — without ever leaving your machine.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,032 words)

## Documentation & Resources

- [MLX Swift LM on GitHub](https://github.com/ml-explore/mlx-swift-lm) _documentation_
- [MLX Swift Examples](https://github.com/ml-explore/mlx-swift-examples) _samplecode_
- [MLX Examples](https://github.com/ml-explore/mlx-examples) _samplecode_
- [MLX Swift](https://github.com/ml-explore/mlx-swift) _documentation_
- [MLX LM - Python API](https://github.com/ml-explore/mlx-lm) _documentation_
- [MLX Explore - Python API](https://github.com/ml-explore/mlx) _documentation_
- [MLX Framework](https://mlx-framework.org) _documentation_
- [MLX](https://ml-explore.github.io/mlx/) _documentation_

## Code Snippets

### Set up MLX-LM and start the local server — [4:40]

```bash
# Step 1: Install MLX-LM
pip install mlx-lm

# Step 2: Start the server
mlx_lm.server --model mlx-community/Qwen-3.5-4B-8bit

# Step 3: Point your agent to the server
curl -X POST \
  http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"default_model","messages":[{"role":"user","content":"Hello!"}]}'
```

### Configure an agent to use your local MLX server — [5:18]

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "mlx/default_model",
  "small_model": "mlx/default_model",
  "provider": {
    "mlx": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "MLX (local)",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1"
      },
      "models": {
        "default_model": {
          "name": "Default MLX Model"
        }
      }
    }
  }
}
```

### Launch distributed inference with MLX — [8:33]

```bash
mlx.launch --hostfile hosts.json \
  --backend jaccl \
  /remote/path/to/mlx_lm.server \
  --model mlx-community/Qwen-3.5-122B-A3B-8bit
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/232/4/f309be4a-8e5b-4c0f-843a-fcbd84c5e2d1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/232/4/f309be4a-8e5b-4c0f-843a-fcbd84c5e2d1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/232) — developer.apple.com. Indexed for agent consumption._
