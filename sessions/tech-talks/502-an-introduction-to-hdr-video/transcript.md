---
id: "tech-talks-502"
event: "tech-talks"
title: "An Introduction to HDR Video"
url: "https://developer.apple.com/videos/play/tech-talks/502"
language: "eng"
words: 924
---

# An Introduction to HDR Video — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/502) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:01]** With the introduction of the revolutionary iPhone X and Apple TV 4K, the video experience is taken to a whole new level with the addition of support for high dynamic range video. With HD, you only see 16 million colors. But with HDR, you see one billion colors. HDR allows content creators to use a much richer and vibrant color palette, which results in unbelievable and stunning image quality. To better understand how HDR works, let's first take a look at the evolution in color capabilities. Here is a representation of the visible color spectrum. With the introduction of HD in 1990, the color space was defined in ITU Rec 709

**[0:46]** and covered about 36 percent of the visible spectrum. But, a lot has changed since 1990, and since then, the P3 color space was introduced. This color space is widely supported across our platforms for all types of app content. Then in 2012, Recommendation 2020 was introduced to define the color space for Ultra High-Definition television, which offers a much wider color space that covers more than 75 percent of the visible spectrum. Video content can now be delivered to supported devices in any of these three color spaces, enabling far more realistic and rich color reproduction. But, the color space itself isn't the whole story.

**[1:32]** The luminance range and settings of the target display is also extremely important and impacts how a given color is going to be perceived. This combination of color space and luminance range is often described as the color volume, with the luminance values on a logarithmic scale. With standard dynamic range content, it is assumed that displays offer a peak luminance of 100 nits, yielding a relatively modest color volume. However, HDR formats are designed to support displays capable of up to 10,000 nits of peak luminance, yielding a much richer color volume for content creators to work with. To further understand the impact of luminance, let's take a look at a 100 percent red square

**[2:18]** in the P3 color space. If the brightness setting of the display is at about 50 percent, the red square might look something like this. However, if the brightness of the display is turned up, the very same RGB value looks quite different and more intense. Similarly, if the brightness is turned down, it looks much more dull. As you can see in this illustration, simply utilizing the RGB values without having control or context of the luminance of the display leads to vastly different color perception by the viewer. This also doesn't take into account other influencing factors such as the ambient light level or the color temperature of the ambient light. Another key goal of HDR is to help improve

**[3:05]** consistency in playback across different displays. In SDR video, the target display is assumed to be capable of up to approximately 100 nits of peak brightness. However, the actual capabilities of modern displays far exceeds this value, and so each display then attempts to interpolate the appropriate brightness levels to match its own luminance range. This leads to all kinds of variance in the appearance of a given video across different displays, and in many cases, a very loose interpretation of the original artistic intent. Now that you have a basic understanding of the key elements of color and luminance, and some of the goals of HDR, let's dig into the types of HDR video that we support.

**[3:51]** We support two HDR standards: Dolby Vision and HDR10. These two formats share some common principles, but also differ in many ways. One of the commonalities between the formats is how the luminance values are encoded. Because the human eye is more sensitive in dark ranges than light ranges, the luminance values are encoded on a curve, so that greater detail in darks can be encoded using the limited bits available. In SDR, the gamma curve was relatively shallow, but this was sufficient for the assumed peak target display luminance of 100 nits. For HDR, a new luminance encoding curve has been introduced. Known as the Perceptual Quantizer, it can better map these perceptible luminance changes

**[4:36]** across the broader, 10,000 nit range. This curve, described in SMPTE ST 2084, allows for even smoother gradation of dark luminance values, yielding a far better experience for the viewer. This curve is utilized by both Dolby Vision and HDR10. In HDR10, a static set of metadata is included in the video stream. This metadata includes information about the display on which the content was originally mastered, such as its effective color gamut, white point, and luminance range. It also includes information about the content itself, namely the peak and average luminance levels.

**[5:21]** This metadata can then be used by the target display to tone map the content to the output capabilities of the display. With HDR10, the metadata is applied to the entire length of the program. Dolby Vision gives you even more control, allowing for metadata to be conveyed dynamically on a scene-by-scene, or even frame-by-frame basis. This way, the available luminance range of the display can be optimized throughout a program that might include both very dark and very bright scenes. The format also carries a much broader metadata set, further enabling the target display to perform much more detailed tone mapping and detail management.

**[6:09]** Finally, Dolby operates a certification program to ensure that each Dolby Vision capable display is consistent, so content will always be displayed as intended. For more information on authoring your HDR content for delivery to supported devices,
