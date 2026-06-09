---
id: "tech-talks-501"
event: "tech-talks"
title: "Authoring 4K and HDR HLS Streams"
url: "https://developer.apple.com/videos/play/tech-talks/501"
language: "eng"
words: 484
---

# Authoring 4K and HDR HLS Streams — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/501) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** With the introduction of the revolutionary iPhone X and AppleTV 4K, the video playback experience is taken to a whole new level with the addition for support for high dynamic range and 4K video. 4K typically refers to frame sizes up to 3840 by 2160, offering an exceptionally detailed and high resolution image when compared to HD. Wide color is supported across iOS, macOS, and tvOS, and the media frameworks support up to the rec 2020 color space, which covers about 75 percent of the visible spectrum. The addition of support for HEVC enables the delivery of higher quality video at about a 40 percent lower bit rate compared to H.264.

**[0:48]** HDR video must be delivered using HEVC. There are two HDR formats that we support: Dolby Vision and HDR10. HDR10 utilizes static metadata that is applied to the entire program. This metadata should be in the HEVC configuration box and not stored in individual sample data. For Dolby Vision content, we support Profile 5, which is single-layer, 10-bit HEVC, and up to level 7. For both HDR formats, the content must be encoded using HEVC. You should include HDR variants of less than or equal to 30 frames per second.

**[1:34]** And you must always provide SDR variants for both your primary media content as well as your I-frame playlists. In order to help devices select compatible variants, we have added a new video range tag to the HLS specification. If you include any HDR variants in your playlist, you must include this tag. Declare SDR for any standard dynamic range variants and PQ for HDR10 or Dolby Vision variants. This tag is an advisory to the client so that it will not attempt to play streams that it cannot support. In order to support HDCP TYPE-1 content protection, the new TYPE-1 value has been added to the HDCP level tag.

**[2:22]** This value is typically applied to content with a resolution of greater than 1920 by 1080. This tag is also advisory in nature and prevents the client from attempting to playback content that can't be supported by the currently attached display. To finish up, let's take a quick look at a few examples of how a playlist differentiates the different types of content and how the tags we just discussed are applied. This is an example of a standard dynamic range HEVC stream that does not require HDCP. This second example describes a 4K HDR stream as indicated by the PQ value of the "VIDEO-RANGE" tag. The "CODECS" tag describes it as a Dolby Vision stream, and the "HDCP-LEVEL" tag indicates that TYPE-1

**[3:08]** will be required in order to successfully playback the stream. This 4K HDR10 example only differs from the Dolby Vision example by the "CODECS" tag. The "VIDEO-RANGE" and "HDCP-LEVEL" tags are the same. For more information on HTTP live streaming, please visit devleoper.apple.com/streaming for access to the HLS authoring guide,
