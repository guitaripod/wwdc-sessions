---
id: "wwdc2019-506"
event: "wwdc2019"
title: "HEVC Video with Alpha"
url: "https://developer.apple.com/videos/play/wwdc2019/506"
language: "eng"
words: 1601
---

# HEVC Video with Alpha — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/506) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hello everyone. My name is Shiva Sundar, and I'm extremely excited to talk about HEVC Video with Alpha. You're probably familiar with Alpha channels in image files today. Alpha channels are ubiquitous in image files, in our apps and on the web. When there's an Alpha channel in an image file, every pixel in the image gets opacity along with its color. This allows us to have an image that has a complex, non-rectangular shape but looks natural when composited against many different backgrounds.

**[0:52]** So Alpha and transparency are common and used all over the web principally by still image formats like PNG. Alpha in video has been less common. It has been a professional video workflow tool. The formats used in professional video workflows like Apple ProRes 4444 are very high data rate and not appropriate for delivery. In 2017, Apple introduced support for the HEIF image file format, which lets us take advantage of the advanced lossy compression technologies in HEVC to compress

**[1:37]** still images. HEIF also lets you include an Alpha channel in image files. In fact, this year we are adding support for HEIF sequences, which lets you have multiple images in a single file. HEIF sequences also support Alpha channels. For some time we've recognized the need for a lower bitrate way to include Alpha in motion video. And so we said let's use that advanced loosy compression technology to support Alpha channels in video files as well. Playback of HEVC video with Alpha is supported in iOS 13,

**[2:24]** tvOS 13 and macOS Catalina on all supported devices and computers. Encoding is supported on all of those devices and computers that have an HEVC encoder. Having a video with Alpha format that works well at bit rates low enough for distribution opens up many opportunities. You can have rich, non-rectangular motion video content that you incorporate as a layer as part of your app's expressive experience. It could be pre-rendered like an animation. Such an element can move around on top of a complicated

**[3:09]** background and you could even have several of them to give a feeling of depth or complex interactions. Because these are movies they can have synchronized sound tracks so the characters in these non-rectangular movies can talk. Highly professional. Alpha channel. Content. For you. Woo-hoo. Woo-hoo. They could be integrated into games using SpriteKit, SceneKit or Metal. In this context, we have provided you with some sample code on how to record a SceneKit scene into a HEVC video with Alpha and how to render another in a SpriteKit scene. On web pages, they could bring

**[3:55]** interactive elements to life. HEVC video with Alpha is supported by Safari in iOS 13 and macOS Catalina. Safari can also tell the web page whether this feature is supported. For more information on using the media capabilities API, be sure to check out the What's New in Authentication, Safari and WebKit video. The ability to distribute video with Alpha at low bitrates opens opportunities for authoring apps to provide background removal. Here I am in front of a green

**[4:40]** sheet hung from the wall recorded using an iPhone. I wish I was here. I used a custom video compositor with a co-image filter to replace the green pixels with transparency and exported it to a video with Alpha. I wish I was here. And now I can overlay this video on any background I like. I wish I was here.

**[5:25]** We are providing sample code showing how to do this and write the resulting HEVC video with Alpha movie. So how does this work? As you know, movie files contain tracks of various media types. A video track contains video frames. HEVC video with Alpha is contained inside a single video track in the movie. In the single track, each frame contains 2 parts called layers and each layer is compressed using the HEVC codec. The base layer contains the colored image of the frame as

**[6:10]** usual. The Alpha layer contains just the Alpha channel of the frame. This is done using special HEVC syntax which identifies the 2 layers. The HEVC rules for this syntax mean that the HEVC decoder that does not know how to handle the Alpha layer will ignore it and display the base layer alone. Let's move along and talk about how to use it. HEVC with Alpha encoding is integrated into numerous AV Foundation APIs. Let's look at content creation, for example. You can render video frames with

**[6:55]** Alpha in your application and use AVAssetWriter to encode them and write them to a movie file. You can use new presets available with AVAssetExportSession to transcode video formats containing Alpha including Apple ProRes 4444 into HEVC with Alpha. These new HEVC presets have the suffix with Alpha. You can also use AVAssettExportSession to burn in a specific background color converting a movie with Alpha into a movie without Alpha, that will play on players that don't

**[7:40]** support HEVC with Alpha. Or you can also use the HEVC with Alpha video encoder directly via VTCompressionSession. Looking at AVFoundation's playback APIs, HEVC with Alpha is supported by AVPlayer and AVPlayerLayer for display in your apps view hierarchy via Core Animation, AppKit and UIKit. The video in AVPlayerLayer will be displayed with a transparent background and composed with the rest of the layers and views.

**[8:25]** Alternatively you can access a sequence of decoded video frames directly using AVPlayerItemVideoOutput. This is a great choice when you want to incorporate those video frames into a custom rendering you're doing using Metal, SpriteKit and other GPU-based rendering APIs. If you need to decode frames for another purpose, you can use AVAssetImageGenerator directory and individual frame of the movie as a CGImage with Alpha. You can use AVAssetReader to extract video frames for use in a non-playback workflow.

**[9:13]** You can also use the HEVC with Alpha video decoder directly via VTDecompressionSession. In short because HEVC with Alpha is integrated into AVFoundation at the level of a video codec, it fits in well into all these familiar API workflows. Now let us see how we can accomplish this in code. When encoding a movie, when configuring your AVAssetWriter input or VTCompressionSession, use the video codec type HEVC with Alpha. This is a special signal that

**[9:59]** the Alpha channel should be encoded. The encoded file will have the standard HEVC codec type. It will be backwards compatible. An HEVC player that does not understand Alpha will display only the base video layer. It will ignore the Alpha portion. If you work with Alpha channels, you may know that there are 2 strategies for how to write video data to a file, premultiplied Alpha or straight Alpha, also known as unassociated Alpha or non-premultiplied Alpha. The tradeoffs between these choices are beyond the scope of this talk. If you're familiar with these,

**[10:44]** what you need to know is that both are supported. If you're not similar with these, we recommend the default, which is premultiplied Alpha. It's the natural choice in most GPU-based rendering parts and it scales better. Now looking at the code, you may specify the Alpha mode by either configuring the compression session or as a buffer attachment. As a safety mechanism if the setting and the buffer attachment are both specified and they do not match, the encoding operation will fail. Our APIs require the Alpha channel to be encoded with

**[11:29]** fixed quality because video encoding artifacts in the Alpha channel can be bothersome in ways that the same artifacts wouldn't be in the base layer. Our APIs let you control the base layers bitrate and the Alpha channel's quality separately if you need to. Now, looking at the code you can specify the Alpha layer quality using target quality for Alpha parameter. It is arranged between 0 and 1 where 1 means it is close to lossless. The bitrate parameter you specify only applies to the base layer and is ignored by the Alpha layer. To detect the presence of an

**[12:15]** Alpha channel, you can either test AV media characteristic containsAlphaChannel or you can query the format description extension contains Alpha channel. If you are trying to export HEVC with Alpha movie, use to determine compatibility API to validate that Alpha is present in the source asset. This validation only takes the source movie into account not the video composition. So you must skip it if you are using a video composition to generate a new Alpha channel from sources that do not have Alpha channels. There are a lot of video players

**[13:01]** in the ecosystem. Many of them don't support HEVC let alone HEVC with Alpha. You can remove the Alpha channel by burning in a solid background color. We have added some convenience API and sample code to help simplify this conversion. If you're looking to build support into a non-Apple media framework, we have published a specification for an interoperability profile that you should read, but if you can't wait, here is a sneak peek. To summarize, HEVC video with Alpha is a cool new feature.

**[13:48]** It takes advantage of HEVC's state of the art compression technology. It is supported on iOS 13, tvOS 13 and macOS Catalina. It takes advantage of hardware acceleration on recent devices. It is well integrated into AVFoundation for use in your apps. It is also integrated in Safari for use in your web experiences. HEVC with Alpha brings us new opportunities for creative expression for both developers and users alike. We can't wait to see the ways you can take advantage of it in your apps.
