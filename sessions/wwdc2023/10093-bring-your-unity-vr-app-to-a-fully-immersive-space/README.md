---
id: "wwdc2023-10093"
event: "wwdc2023"
year: 2023
title: "Bring your Unity VR app to a fully immersive space"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10093"
topics: ["Spatial Computing", "Graphics & Games"]
platforms: ["visionOS"]
hasTranscript: true
---

# Bring your Unity VR app to a fully immersive space

**Event:** WWDC23 · **Topic:** Graphics & Games · **Platforms:** visionOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10093](https://developer.apple.com/videos/play/wwdc2023/10093)

Discover how you can bring your existing Unity VR apps and games to visionOS. We’ll explore workflows that can help you get started and show you how to build for eyes and hands in your apps and games with the Unity Input System. Learn about Unity’s XR Interaction Toolkit, tips for foveated rendering, and best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,497 words)

## Documentation & Resources

- [Apply for the Unity beta](https://create.unity.com/spatial) _documentation_

## Code Snippets

### Translate raw joints into gameplay actions — [12:46]

```csharp
// Translate raw joints into gameplay actions

static bool IsIndexExtended(XRHand hand)
{
    if (!(hand.GetJoint(XRHandJointID.Wrist).TryGetPose(out var wristPose) &&
          hand.GetJoint(XRHandJointID.IndexTip).TryGetPose(out var tipPose) &&
          hand.GetJoint(XRHandJointID.IndexIntermediate).TryGetPose(out var intermediatePose)))
    {
        return false;
    }

    var wristToTip = tipPose.position - wristPose.position;
    var wristToIntermediate = intermediatePose.position - wristPose.position;
    return wristToTip.sqrMagnitude > wristToIntermediate.sqrMagnitude;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10093/4/D52AC313-8624-4177-BB94-C2F64F591723/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10093/4/D52AC313-8624-4177-BB94-C2F64F591723/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10093) — developer.apple.com. Indexed for agent consumption._
