# Compose advanced graphics effects with SwiftUI

**Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-322](https://developer.apple.com/videos/play/wwdc2026/322)

Discover how to craft rich, custom experiences by creatively composing SwiftUI layout and graphics APIs. We’ll show you how to break down complex designs and use a creative pipeline to chain simple building blocks together. Learn how to draw with layer shaders, animate with timelines, and anchor views with alignment guides.

**Keywords:** `screenshots`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Alignment](https://developer.apple.com/documentation/SwiftUI/Alignment) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Alignment
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Alignment.json
- [Composing advanced graphics effects with SwiftUI](https://developer.apple.com/documentation/SwiftUI/Composing-advanced-graphics-effects-with-SwiftUI) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Composing-advanced-graphics-effects-with-SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Composing-advanced-graphics-effects-with-SwiftUI.json
- [Shader](https://developer.apple.com/documentation/SwiftUI/Shader) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Shader
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Shader.json

## Code Snippets

### Cover art image — [4:18]

```swift
Image("CoverArt")
```

### Blurred cover art image — [4:24]

```swift
Image("CoverArt")
.blur(radius: 30)
```

### Applying layer effect in SwiftUI — [7:09]

```swift
GeometryReader { proxy in
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(),
            maxSampleOffset: .zero
        )
}
.ignoresSafeArea()
```

### Writing layer effect shader in Metal — [7:21]

```cpp
[[stitchable]] half4 backgroundWarp(
    float2 position, SwiftUI::Layer layer
) {
    return layer.sample(position);
}
```

### Metal shader with offset parameter — [7:39]

```cpp
[[stitchable]] half4 backgroundWarp(
    float2 position, SwiftUI::Layer layer,
    float2 offset
) {
    return layer.sample(position + offset);
}
```

### SwiftUI layer effect with offset parameter — [7:55]

```swift
GeometryReader { proxy in
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(
               .float2(.init(x: 0, y: 0))
            ),
            maxSampleOffset: .zero
        )
}
.ignoresSafeArea()
```

### SwiftUI layer effect with full-width offset — [8:04]

```swift
GeometryReader { proxy in
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(
               .float2(.init(x: proxy.size.width, y: 0))
            ),
            maxSampleOffset: .zero
        )
}
.ignoresSafeArea()
```

### SwiftUI layer effect with noise sampling — [8:37]

```swift
GeometryReader { proxy in
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(
                .float2(proxy.size),
                .image(Image("NoiseTexture"))
            ),
            maxSampleOffset: .zero
        )
}
.ignoresSafeArea()
```

### Metal shader with noise sampling — [8:55]

```cpp
[[stitchable]] half4 backgroundWarp(
    float2 position, SwiftUI::Layer layer,
    float2 size, texture2d<half> noiseTex
) {
    constexpr sampler s(address::repeat, filter::linear);
    float2 uv = position / size;

    half4 n = noiseTex.sample(s, uv);
    float2 offset = (float2(n.r, n.g) - 0.5) * 200.0;

    return layer.sample(position + offset);
}
```

### Metal shader with domain warping — [10:22]

```cpp
[[stitchable]] half4 backgroundWarp(
    float2 position, SwiftUI::Layer layer,
    float2 size, texture2d<half> noiseTex
) {
    constexpr sampler s(address::repeat, filter::linear);
    float2 uv = position / size;

    half4 n = noiseTex.sample(s, uv);

    float2 q = float2(n.r, n.g);
    n = noiseTex.sample(s, uv + q);

    float2 offset = (float2(n.r, n.g) - 0.5) * 200.0;

    return layer.sample(position + offset);
}
```

### SwiftUI layer effect with static visual — [11:16]

```swift
GeometryReader { proxy in
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(
                .float2(proxy.size),
                .image(Image("NoiseTexture"))
            ),
            maxSampleOffset: .zero
        )
}
.ignoresSafeArea()
```

### SwiftUI layer effect with animated visual — [11:37]

```swift
@State private var startDate = Date.now

TimelineView(.animation) { timeline in
    let elapsed = timeline.date.timeIntervalSince(
        startDate
    )
    CoverArtView()
        .layerEffect(
            ShaderLibrary.backgroundWarp(
                .float2(proxy.size),
                .image(Image("NoiseTexture")),
                .float(elapsed)
            ),
            maxSampleOffset: .zero
        )
}
```

### Basic transcript view — [12:15]

```swift
ScrollView {
    LazyVStack(alignment: .leading, spacing: 12) {
        ForEach(sampleTranscript) { line in
                .font(.title)
                .fontWeight(.bold)
        }
    }
}
```

### Time-synced transcript view — [12:33]

```swift
@State private var playback = PlaybackState()

ScrollViewReader { scrollProxy in
    ScrollView {
        LazyVStack(alignment: .leading, spacing: 12) {
            ForEach(sampleTranscript) { line in
                Text(line.text)
                    .transcriptLineStyle(isCurrent: 
                        line.id == playback.currentLineIndex
                    )
            }
        }
    }
    .onChange(of: playback.currentLineIndex, { _, i in
        scrollProxy.scrollTo(i, anchor: .center)
    })
}
```

### Overlay with center alignment — [13:53]

```swift
Text(line.text)
.overlay {
     Text(line.formattedTimestamp)
}
```

### Overlay with bottom leading alignment — [14:06]

```swift
Text(line.text)
.overlay(alignment: .bottomLeading) {
     Text(line.formattedTimestamp)
}
```

### Overlay with alignment guide override — [14:32]

```swift
Text(line.text)
.overlay(alignment: .bottomLeading) {
     Text(line.formattedTimestamp)
         .alignmentGuide(.bottom) { $0[.top] }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/322/4/db4c622a-2091-45ef-a024-df317a5b55a5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/322/4/db4c622a-2091-45ef-a024-df317a5b55a5/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._