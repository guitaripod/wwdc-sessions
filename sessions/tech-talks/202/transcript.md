---
id: "tech-talks-202"
event: "tech-talks"
title: "Updating Your App for Apple TV 4K"
url: "https://developer.apple.com/videos/play/tech-talks/202"
language: "eng"
words: 360
---

# Updating Your App for Apple TV 4K — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/202) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** Apple TV 4K takes the living room experience to a whole new level, with support for 4K resolution, P3 color, HDR video playback, the incredible A10X Fusion processor, and the updated and improved Siri Remote. Updating your app to support these new features is very straightforward. The first step is to add a 2x launch image. Until you do so, tvOS is going to run your app in compatibility mode. While you're at it, you'll also want to add 2x app icons and top shelf images. When attached to a 4K television, UIKit will now automatically select retina assets

**[0:45]** from your asset catalogue. You can inspect what screen scale the device is running in by inspecting the scale property of the main UIScreen. You can also determine the pixel resolution of the attached display by using the nativeBounds property. Just like the latest iOS and macOS devices, we're really excited that Apple TV 4K now supports P3 color. When providing retina assets, you may also want to update your assets to take advantage of this wider color space, allowing your graphics and images to contain even richer and more saturated colors than before. This isn't just for flat images but is supported for layered images as well.

**[1:32]** Media apps will also want to look at updating their streams to include 4K and HDR variants for any content that was produced in these formats. Apple TV 4K supports both Dolby Vision and HDR10 for HDR content, and the addition of support for HEVC enables these higher fidelity and resolution streams while consuming up to 40 percent less bandwidth than comparable streams encoded using H.264. The updated and improved Siri Remote now provides motion data for attitude and rotation rate, in addition to the values for acceleration and gravity that the prior version offered. To determine if the paired remote supports these new features, you can inspect the new GCMotion

**[2:17]** "hasAttitudeAndRotationRate" property. The values for attitude and rotation rate are then provided by the respective GCMotion properties. And with those few changes, you're going to be able to take advantage of all of the new capabilities and performance of Apple TV 4K.
