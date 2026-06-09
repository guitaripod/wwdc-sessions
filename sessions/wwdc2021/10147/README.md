---
id: "wwdc2021-10147"
event: "wwdc2021"
year: 2021
title: "Optimize for variable refresh rate displays"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10147"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Optimize for variable refresh rate displays

**Event:** WWDC21 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10147](https://developer.apple.com/videos/play/wwdc2021/10147)

Discover how to achieve smooth screen updates on all Apple platforms that support dynamic display timing. Learn techniques for pacing full-screen game updates on Adaptive Sync displays in macOS, and find out how Low Power Mode and other system states affect frame rate availability on ProMotion displays. We’ll also share best practices for driving custom drawing using display link APIs.

**Keywords:** `display`, `display p3`, `game dev`, `game developer`, `metal`, `metal shading language`, `metal tools`, `optimization`, `proapps`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,629 words)

## Documentation & Resources

- [Metal Feature Set Tables](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/metal/Metal-Feature-Set-Tables.pdf
- [Metal](https://developer.apple.com/documentation/Metal) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal.json

## Code Snippets

### Is Adaptive-Sync scheduling enabled — [5:51]

```objectivec
// Detecting an Adaptive-Sync display

- (BOOL) isAdaptiveSyncSupported:(NSScreen *)screen {
    NSTimeInterval minInterval = screen.minimumRefreshInterval;  
    NSTimeInterval maxInterval = screen.maximumRefreshInterval;  
    return minInterval != maxInterval;
}

// Detecting full-screen

- (BOOL) isWindowFullscreen:(NSWindow *)window {
    return ([window styleMask] &= NSFullScreenWindowMask) == NSFullScreenWindowMask;
}

// Tying it all together

- (BOOL) isAdaptiveSyncSchedulingEnabled:(NSScreen *)window {
    NSScreen* windowScreen = [window screen];
    return [self isWindowFullscreen:window] && [self isAdaptiveSyncSupported:windowScreen];
}
```

### Leverage Drawable present calls — [6:49]

```objectivec
// Drawable present APIs with frame-pacing

[commandBuffer presentDrawable:drawable afterMinimumDuration:interval];
[commandBuffer presentDrawable:drawable atTime:t];

// Drawable present API without frame-pacing

[commandBuffer presentDrawable:drawable];
```

### A simple example — [7:11]

```objectivec
id<CAMetalDrawable> currentDrawable = [metalLayer nextDrawable];

// Your encoder and command buffers here

[commandBuffer presentDrawable:currentDrawable];
```

### Adaptive-Sync in your app 1 — [7:55]

```objectivec
id<CAMetalDrawable> currentDrawable = [metalLayer nextDrawable];

NSTimeInterval userFramerateCap = 78.0;
NSTimeInterval userInterval     =  1.0 / userFramerateCap;

// Your encoders and command buffers are still here
[commandBuffer presentDrawable:currentDrawable afterMinimumDuration:userInterval];
```

### Adaptive-Sync in your app 2 — [8:43]

```objectivec
id<CAMetalDrawable> currentDrawable = [metalLayer nextDrawable];

// Your encoders and command buffers are still available!

NSTimeInterval averageGPUTime = screen.minimumRefreshInterval;

[commandBuffer presentDrawable:currentDrawable afterMinimumDuration:averageGPUTime];

[commandBuffer addCompletedHandler:^(id<MTLCommandBuffer> buffer) {
  const NSTimeInterval GPUTime = buffer.GPUEndTime - buffer.GPUStartTime;

  // Use an exponential moving average
  const double alpha = .25;

  averageGPUTime = (GPUTime * alpha) + (averageGPUTime * (1.0 - alpha));
}];
```

### Query the display refresh rate at runtime — [15:36]

```objectivec
// Maximum frame rate from UIKit

NSInteger maxRate = [[UIScreen mainScreen] maximumFramesPerSecond];

// Current maximum frame rate from CoreAnimation

NSInteger currentMaxRate = round(1 / link.duration);
```

### Use the actual frame rate of the CADisplayLink — [17:06]

```objectivec
CADisplayLink *link = [CADisplayLink displayLinkWithTarget:self 
                                                  selector:@selector(displayLinkCallback:)];

[link setPreferredFramesPerSecond:40];
[link addToRunLoop:[NSRunLoop currentRunLoop] forMode:NSDefaultRunLoopMode];

- (void)displayLinkCallback:(CADisplayLink *)link {
    CFTimeInterval interval = link.targetTimestamp - link.timestamp;

    //...
}
```

### Dynamically compute the time delta 1 — [21:47]

```objectivec
- (void)displayLinkCallback:(CADisplayLink *)link {
    progress += link.targetTimestamp - link.timestamp;
    [self renderAnimationWithProgress:progress];
}
```

### Dynamically compute the time delta 2 — [21:57]

```objectivec
- (void)displayLinkCallback:(CADisplayLink *)link {
    progress += link.targetTimestamp - previousTargetTimestamp;
    previousTargetTimestamp = link.targetTimestamp;

    [self renderAnimationWithProgress:progress];
}
```

### Dynamically compute the time delta 3 — [22:08]

```objectivec
- (void)displayLinkCallback:(CADisplayLink *)link {
    progress += link.targetTimestamp - previousTargetTimestamp;
    previousTargetTimestamp = link.targetTimestamp;

    [self renderAnimationWithProgress:progress withDeadline:link.targetTimestamp];
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10147/5/B362C41F-D567-4137-8333-0B4FF56AD528/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10147/5/B362C41F-D567-4137-8333-0B4FF56AD528/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10147) — developer.apple.com. Indexed for agent consumption._