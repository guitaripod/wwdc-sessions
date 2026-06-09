---
id: "wwdc2021-10278"
event: "wwdc2021"
year: 2021
title: "Practice audio haptic design"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10278"
topics: ["Design", "Graphics & Games", "Spatial Computing", "Audio & Video"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Practice audio haptic design

**Event:** WWDC21 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10278](https://developer.apple.com/videos/play/wwdc2021/10278)

Discover how you can deliver rich app experiences that include animation, sound, and haptics on iPhone. Learn key concepts for designing multimodal experiences within the Core Haptics framework. We’ll take you through our sample HapticRicochet app — where haptic and sound feedback is designed in harmony with key interactive moments — and show you how to create magical and delightful experiences. To get the most out of this session, we recommend first watching “Expanding the Sensory Experience with Core Haptics” from WWDC19, and checking out the HapticBounce sample project (which requires Xcode, iPhone 8 or newer, and a basic knowledge of Swift). Familiarity with Core Haptics is helpful, but not required.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,094 words)

## Documentation & Resources

- [Delivering Rich App Experiences with Haptics](https://developer.apple.com/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreHaptics/delivering-rich-app-experiences-with-haptics.json
- [Core Haptics](https://developer.apple.com/documentation/CoreHaptics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreHaptics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreHaptics.json
- [Human Interface Guidelines: Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/playing-haptics

## Code Snippets

### Shield — [8:05]

```swift
// Initialize shield.
func initializeShieldHaptics() {
    // Create a pattern from the shield asset.
    let pattern = createPatternFromAHAP("ShieldTransient")!

    // Create a player from the shield pattern.
    shieldPlayer = try? engine.makePlayer(with: pattern)
}

/ Play shield transformation.
func shield() {
    // …
    // start player for haptics and audio.
    startPlayer(shieldPlayer)

    // Play shield animation
    isAnimating = true
    sphereView.layer.add(shieldAnimation, forKey: "Width")
    // …
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10278/6/22D440E4-3CF8-4968-8FCB-6F21B4587DAD/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10278/6/22D440E4-3CF8-4968-8FCB-6F21B4587DAD/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10278) — developer.apple.com. Indexed for agent consumption._
