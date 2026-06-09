---
id: "wwdc2026-388"
event: "wwdc2026"
year: 2026
title: "Find and fix performance issues in your Metal games"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/388"
topics: ["Developer Tools", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Find and fix performance issues in your Metal games

**Event:** WWDC26 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-388](https://developer.apple.com/videos/play/wwdc2026/388)

Track down hard-to-find game performance issues with powerful Metal tools. Discover how to collect rich performance data using Game Performance Overview in Instruments, run background traces with metalperftrace on macOS and Control Center on iOS, and use the new StateReporting API to correlate metrics directly to your game’s runtime state. Turn hours of telemetry into clear, actionable insights.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,852 words)

## Documentation & Resources

- [Understanding the Metal Performance HUD metrics](https://developer.apple.com/documentation/Xcode/Understanding-metal-performance-hud-metrics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Understanding-metal-performance-hud-metrics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Understanding-metal-performance-hud-metrics.json
- [Monitoring your Metal app’s graphics performance](https://developer.apple.com/documentation/Xcode/Monitoring-your-Metal-apps-graphics-performance) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Monitoring-your-Metal-apps-graphics-performance
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Monitoring-your-Metal-apps-graphics-performance.json
- [Getting started with StateReporting](https://developer.apple.com/documentation/StateReporting/getting-started-with-statereporting) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StateReporting/getting-started-with-statereporting
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StateReporting/getting-started-with-statereporting.json
- [Metal debugger](https://developer.apple.com/documentation/Xcode/Metal-debugger) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Metal-debugger
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Metal-debugger.json

## Code Snippets

### Collect a trace with metalperftrace — [5:00]

```bash
# Collect the last 5 hours
metalperftrace collect /tmp --last 5h

# Output
# Metal performance traces collected to: /tmp
# /tmp/MetalPerfTrace_20260401_094100_to_144100.atrc

# Or collect an explicit time range
metalperftrace collect /tmp \
  --start 2026-04-01T09:41:00 \
  --end 2026-04-01T12:41:00
```

### Print a trace overview — [7:02]

```bash
metalperftrace overview /Data/MyGameTrace.atrc

# [Modern Renderer pid:13833]
# Mem: 2146.1 MiB (2343.9 Peak, 1199.4 Metal)
# Total CPU Time: 2417.601s (33.17% Sys, 66.83% User)
# Instructions: 9944836683668 (5.75% P, 94.25% E)
# Cycles: 5176430469224 (4.45% P, 95.55% E)
# Disk Reads / Writes: 317.37 / 0.04 MiB (Logical Write 0.04)
# Layer 0x729293000 (3456x2104) Interval 300.065s Active 300.065s
#   59.7 FPS  17735 Frames  188 Skipped
#   Frame Time avg: 16.74ms min: 8.33 max: 125.00 stddev: 3.70
#   CPU Begin-to-Present avg: 3.99ms min: 1.40 max: 94.37 stddev: 1.80
#   On-GPU Time avg: 13.39ms min: 5.24 max: 37.57 stddev: 1.43
#   Next Drawable Wait avg: 0.26ms min: 0.00 max: 91.08 stddev: 1.75
#   Shader Compilation Time: 0.000s (Total: 0, Cached: 18)
```

### Filter by process and emit JSON — [7:58]

```objectivec
// Report state transitions
#import <StateReporting/StateReporting.h>

NSString *domain = @"com.mygame.level";
SRStateReporter *reporter = [SRStateReporter reporterForDomain:domain];

[reporter reportTransitionToStateLabel:@"Level 1"
                        stableMetadata:nil
                      volatileMetadata:nil];

[reporter reportTransitionToStateLabel:@"Level 1"
                        stableMetadata:@{ @"id": @1001 }
                      volatileMetadata:nil];

[reporter reportVolatileMetadataUpdate:@{ @"health": @100 }];
```

### Include full state transitions in overview — [13:55]

```bash
metalperftrace overview /Data/MyGameTrace.atrc --include-state-transitions

# [States]
# com.mygame.graphics
#   High (30.59%, 14.996s)  raytracing: 1  shadow: ultra
#   Medium (69.38%, 34.012s)  raytracing: 0  shadow: medium
# com.mygame.level
#   Level 1 (20.47%, 10.033s)  biome: forest   id: 1001
#   Level 2 (79.53%, 38.991s)  biome: volcano  id: 1002
```

### Aggregate metrics by state — [14:15]

```bash
# Aggregate across all domains / transitions
metalperftrace overview /Data/MyGameTrace.atrc --aggregate

# Aggregate one domain
metalperftrace overview /Data/MyGameTrace.atrc --aggregate \
  --domain com.mygame.graphics

# Aggregate a specific state label within a domain
metalperftrace overview /Data/MyGameTrace.atrc --aggregate \
  --domain com.mygame.graphics \
  --state-label "High"
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/388/4/682e727f-75f9-441f-81d9-2d6f38bde4b0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/388/4/682e727f-75f9-441f-81d9-2d6f38bde4b0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/388) — developer.apple.com. Indexed for agent consumption._